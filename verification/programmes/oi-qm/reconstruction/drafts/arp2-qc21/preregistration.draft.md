# ARP-2, Q-C2-1: which-path recording and complementarity in a two-path experiment built from the OI substratum and named observational-incompleteness principles, a fragment-relative classical-model test, and the non-Clifford operation through detector records. Native round ARP-2-QC21 — PREREGISTRATION (draft r15 implementation)

**Status: WIP / UNVERIFIED implementation draft, not a candidate `F`.** Model-written.

**r15 implementation.** The owner approved R1–R7 defaults, R8 alternative, R9 default and R10 narrowing,
with initial `S_max = 100000`, at [#1169 c.6778994857](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6778994857),
2026-11-10, answering **“Approve rulings and bounded implementation”**. The exact question and answer are
retained in OWNER-DECISIONS.md. Approval covers bounded implementation, permitted non-scientific checks,
independent implementation review, ordinary PR CI and a separate design-run request. It authorizes no
scientific/local-A3/design/stress/gate run, dispatch, F/E/freeze, workflow-splice publication, premise or merge.
Other pre-F evidence, measurements, pins, source retention and owner commitments remain pending.

**Historical revision notes below state the position at each earlier revision. Current R1–R10 authority
is the r15 owner section and precondition 2; earlier pending/default statements do not govern r15.**
- **r14d.** Paper-only response to R14C-B1 to B3 and r14c-N1 to N9, from the archived r14c review
  (`6677f389a603e249a9e0e8c7e0e80ef5edeebf67`). Designation identity is checked; R2's alternative names both
  guard changes; R10 distinguishes exceptions from conditional landing language and names the dependent sites.
  All R1–R10 choices remain `PENDING`. `DISPOSITIONS-r14d.md` traces the changes; `IMPL-DELTA-r14d.md` is an
  implementation plan, not an updated or tested implementation. The first r14d preparation review at
  `5e160d3e80dc7dcdfea3db537cbf99fde63ff02d` returned REVISE (minor); R14D-B1's confirmation-copy limitation
  is propagated to C-STATELESS's descriptions, with R14D-N1's explicit attempt-status field. A focused
  independent check of this correction is required; no new ACCEPT is asserted here.
  No design run, fixture-mode local run, scientific computation, workflow splice, F/E or merge is authorized.
  Historical rN-directory references below describe archived session copies, not directories on this tracking
  branch. Published r14b remains at commit `8f969ab6f6cbd2d04fff86cdff2b85d92433a12f`; archived r14c is at
  `820519cf011c09b37690213a758106ed3aa15cc2:handoff-20261109/qc21/preregistration.draft.md`.
- **r14c.** In place: R14B-B1 to B3 and r14b-N1 to N9 only (`review/REVIEW-QC21-r14b.md`, `95dcec39…`). `order`
  reads `F`'s designation comment; R1's lowering rule and R2's alternative are restated; A3b runs `always()`; the
  inputs pin `tools/v3_verifier.py`; shared-method changes of ARP-3-QC22 r14a are ported (the ports among edit rows 109–125), and
  the §A.42 item 8 dispositions of host-time records are open ruling R10. Found via that round's r14a review
  (its Rc1): the no-unapproved-F1 rule holds for an attempt whose A3 never started (edit row 126). The
  dispositions are in `DISPOSITIONS-r14c.md`. r14b is kept in `r14b/`.
- **r14b.** In place: R14A-B1, r14a-N1 to N13 and the implementation items I1–I5 only
  (`review/REVIEW-QC21-r14a.md`, `f30841ba…`). `verdict` reads comments through the frozen template
  `issues/comments/{DEC}` and requires every approval entry to hold, the `E` dispatch's included (edit rows
  99–108). UPR-BC with an `out_of_scope` or `undecided` completion is open ruling R9. The dispositions are in
  `DISPOSITIONS-r14b.md`. r14a is kept in `r14a/`.
- **r14a.** In place: R14-B1, R14-B2 and r14-N2 to N20 only (`review/REVIEW-QC21-r14.md`, `e11f4668…`), and six
  defects of the shared method found via ARP-3-QC22 r14 (its R13-N6, N8, N9, N10, N17 and B4). The
  owner-reserved choices that r14 made in applying D19–D23, and the defaults r14a added where r14 was silent (R3's
  SF-2 part, R7 and R8), are open rulings R1–R8 of precondition 2, each `PENDING` with its draft default. The
  dispositions are in `DISPOSITIONS-r14a.md`. r14 is kept in `r14/`.
- **r14.** Records the owner's D19–D23 decisions and four safeguards (#1169 c.6740078002, "Adopt and authorize";
  *Owner decisions D19 to D23*) and applies them only: D19 (0)(c), (i)(a), (ii)(b), (iii)(c), (iv)(a); D20 (b);
  D21 (b); D22 (a); D23 (c); the safeguards as frozen rules SG-1 to SG-4. The stress test ST-BP is specified and not
  run (C.8 item 2); the caps it fixes are `PENDING`. The r13a nit is closed: D19 (i)(d) is not selected, so no "not
  decided" outcome or token exists. The dispositions are in `DISPOSITIONS-r14.md`. r13a is kept in `r13a/`.
- **r13a.** In place: R13-B1 and R13-B2 only (`review/REVIEW-QC21-r13.md`, `43c7cef7…`; PLAN §21). D21 (b) now
  restores the S1 binding, and D19 gains (0)(c), (i)(d) and (i)(e). r13 is kept in `r13/`.
- **r13.** Resolves in the text the nineteen items the implementer reported against r11b with the r12 STAB hook
  (PLAN §20, items 1–19), the placement of STAB-FALSE, and the location of the `K = 2` certificate (C.8 item 12).
  Each resolution is classified IMPL (an implementation clarification that preserves the approved definitions, controls
  and outcome rules) or SCI (a scientific scope change; owner, 2026-11-09). IMPL resolutions are in the text. SCI
  resolutions are not adopted: each is a flagged owner decision with neutral options (D19 to D23, decided at r14:
  *Owner decisions D19 to D23*). The passages carried from the
  round's r5, r6 and r7 drafts are stated in Appendix D. The r12a nits are in. r12 is kept in `r12/`, r12a in `r12a/`.
- **r12a.** In place: r12-N1 to N3 only (`review/REVIEW-QC21-r12.md`, `dac201a3…`; PLAN §19). r12 is kept in `r12/`.
- **r12.** Records the two independent proof reviews and applies their consequences only: the STAB field, the
  STAB-conditioned sentences, the withdrawal of r6's `arccos(3/5)` sentence, the STAB controls and LP-1. The
  dispositions are in PLAN §18. r11b is kept in `r11b/`.
- **r11b.** In place: R11a-B1 only (`review/REVIEW-QC21-r11a.md`, `eebd2d6d…`). GT-ACT moves to a dedicated
  disposable branch, which is not recorded. r11a is kept in `r11a/`.
- **r11a.** In place: the r11 re-review's R11-B1 and r11-N1 to N3 only (`review/REVIEW-QC21-r11.md`, `7d81f43c…`;
  PLAN §16). r11 is kept in `r11/`.
- **r11.** It applies the r10 re-review (`review/REVIEW-QC21-r10.md`, `b01baa3e…`; R10-B1 to R10-B5, r10-N1 to N5)
  and the owner's D12 waiver (c.6735159962). The dispositions are in PLAN §15. r10 is kept in `r10/`. r11 is not
  reviewed.
- **r10.** Built on the owner's freeze decisions (#1169 c.6735014875; *Owner decisions at the freeze*). r10 adds:
  - the representation ledger with REP-INV;
  - the attribution field `ATTR`;
  - the three A/B report fields;
  - the review status of the two sketches;
  - the copied ARP-3-QC22 text (Appendix C);
  - the fills.

  r10 is not reviewed. The dispositions are in PLAN §14. r9a is kept in `r9a/`.
- **r9a.** The r9 confirming check (`review/REVIEW-QC21-r9.md`, `50779a74…`, ACCEPT-WITH-NITS) is applied in place:
  r9-N1 to r9-N4 only. r9 is kept in `r9/`.
- **r9.** The r8 re-review (`review/REVIEW-QC21-r8.md`, `32bec1f0…`) returned REVISE (minor) and reports the
  design-level fixed point reached. r9 applies only R8-B1, R8-B2 and r8-N1–N8 (PLAN §12). r8 is kept in `r8/`.
- **Review history.** r6 was reviewed REVISE (`review/REVIEW-QC21-r6.md`, `facdd215…`). r7 (`r7/preregistration-r7.draft.md`,
  `e75f0bc6…`) applied that review and was re-reviewed REVISE (`review/REVIEW-QC21-r7.md`, `a9488c6f…`; blockers
  R7-B1–B5, nits r7-N1–N6). r8 applies the re-review: P is restated around complementarity, construction A is renamed
  for what it is, `mech_change` is computed, `K` becomes a kernel, B's LP reads its whole `Acc`, and D16 is restated.
  The dispositions are in PLAN §11. r8 is not re-reviewed.
- **Inputs.** The paper model is `DESIGN-DS.md` r13. `REACHABLE.md` r3 is unchanged.
- **Governance.** This file is the control plane of a native round under `AGENTS.md` §A.39, drafted on its own guiding
  pull request from `D`. The owner designates `F` and `E` and approves each dispatch (#1169 c.6723329527).
- **ARP-1** has landed (precondition 1).
- **`PENDING` discipline.** Every `PENDING` field is filled before `F`. Control P refuses any unbackticked occurrence of
  that word. A placeholder is therefore written unbackticked; a backticked `PENDING` names the word and is not a
  placeholder (re-review R14-B1).

```v3-round
round ARP-2-QC21
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-arp2-qc21-20261108/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-arp2-qc21-20261108/
record AM verification/receipts/ARP-2-QC21.json
execution M .github/workflows/verify.yml
```

**Frozen expectation for the two blocks.**
- The three round lines are those above.
- The governed-paths digest is `1d195f938f5467d1549f7755bcafce2109abbfbcb57a7ff2243fa09a67e9982e` (`governed_digest`,
  `tools/v3_verifier.py` at `2cd49dc0`).
- The digest is recomputed if the directory's date changes when `D` is cut (PENDING: date confirmed). Control T
  re-derives both at `F`, S1 and `E`.

The record directory holds:
- this file and its amendments (before `F` only);
- `qc21_check.py` and `controls.py`;
- `evidence/`;
- `result.md`.

The one execution path is `.github/workflows/verify.yml`. No manuscript, built artifact, kernel module,
`verification/ROADMAP.md`, input record or other round's record changes under any outcome.

**Terminology** (owner, c.6734304025). Designs say "OI substratum plus independently justified
observational-incompleteness principles, with every additional assumption identified and tested separately", never
"native OI dynamics", except inside the owner's verbatim quotations.
- **Construction A** is the deterministic substratum alone.
- **Construction B** is A plus the named principles of *The A/B typing*.
- "Native round" in this file's title is §A.39's protocol term.

## Authority (quoted with author and time)

All entries are amaybaum, OWNER, on #1169, verbatim from the comment. The five passages carried from r5 are inlined
first:

- **Programme authorization, #1169 c.6723277401** (amaybaum, 2026-11-08T15:21:11Z), bound passages verbatim:

  > 2. **Q-C2-1** — Execute after M-ARC has completed and its results have been independently reviewed.

  > - Prepare a separate, fully specified preregistration, including assumptions, controls, outcome classifications
  >   and stopping conditions.
  > - Preserve negative, inconclusive and vacuous results without reinterpretation or post-hoc changes to
  >   acceptance criteria.
  > - Stop and report any failed gate, unresolved blocker or material deviation rather than bypassing it.

  > Preparation may overlap where scientifically independent, but **scientific executions must be sequential**, with
  > each result informing the next investigation's preregistration without retroactively changing earlier tests.

  > The priority is genuine assumption removal, not obtaining a positive result by introducing equivalent
  > assumptions under different names.

- **Designation boundaries, #1169 c.6723329527** (2026-11-08T15:25:55Z), verbatim:

  > Before each freeze, present the reviewed candidate F, exact commit, independent-review verdict, controls and
  > outstanding blockers for my designation. Before each execution, present the exact execution head E and proposed
  > dispatch for my approval.

  > No automatic freezes or dispatches. The halt-only rule remains mandatory, and any failed gate stops progression.

- **Assumption-dependence direction, #1169 c.6723491138** (amaybaum, OWNER, 2026-11-08T15:40:41Z), verbatim:

  > The preregistered outcomes should remain unchanged. Any broader conclusion should be separately qualified, and new
  > variants should be tested in new rounds rather than retroactively modifying the original experiment.

  > Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still produce valid
  > probabilities, observable quantum predictions and consistent behavior across repeated experiments.

- **Owner directions on interpretation and preparation, #1169 c.6723571280** (posted as amaybaum, author association
  OWNER, 2026-11-08T15:47:58Z, recording the owner's chat directions verbatim). Bound passages, verbatim from that
  comment:

  > * Q-C2-1: Establish reachable hidden laws before designing the executable test. A non-Clifford result must emerge
  >   from the dynamics, not be embedded in the definitions.

  > One additional principle should guide interpretation: failure to construct a witness is not proof that no witness
  > exists, unless a theorem establishes that impossibility within a clearly stated scope.

  > Which apparent obstacles survive when we retain only native OI principles and genuinely observable quantum
  > requirements?

  > | Finding | Scientific significance |
  > | --- | --- |
  > | An imported assumption causes an apparent obstruction | We identify an unnecessarily restrictive test |
  > | Removing that assumption yields a valid OI mechanism | We overcome a genuine obstruction in the tested model |
  > | The mechanism reproduces the required quantum predictions, measurements and composition | We advance toward operational equivalence |
  >
  > The third is what ultimately matters. We cannot establish equivalence merely by escaping a no-go theorem.

  > Continue preparing M-ARC, Q-C2-1 and Q-C2-2 in parallel, while preserving the authorized sequential execution
  > order:
  >
  > M-ARC → Q-C2-1 → Q-C2-2 → drive-phase check.

  > Our ultimate objective remains unchanged: establish whether OI can reproduce quantum mechanics through its own
  > mechanisms, rather than through assumptions that already encode quantum behavior.


- **Owner directions on the EOI audit, #1169 c.6723585151** (posted as amaybaum, author association OWNER,
  2026-11-08T15:49:15Z, recording earlier chat directions verbatim). Bound passages, verbatim:

  > What genuinely emerges from OI alone? Reserve this classification for behavior obtained without inserting the
  > quantum target into the physical assumptions.

  > * Add a hidden-prior sensitivity requirement. When a result changes under correlated hidden distributions, its
  >   stated scope must identify that dependence.
  > * Separate representation from mechanism. A unitary lift, Born-rule marginal or Lüders instrument imported
  >   mathematically must never be credited as an OI physical derivation.

  > Hidden information can influence physical dynamics without being accessible to the embedded observer.
  >
  > A proof that excludes such memory is valid only within that restricted model; it cannot automatically establish a
  > limitation of OI generally.


- **c.6733621500** (2026-11-09T06:16:40Z): "Proceed as suggested.  We should also keep in mind that in reality the
  observer only accesses the quantum effects indirectly through interference, etc.  So the experiment should also only
  test through indirect access as well.  In fact, we should make the test setup as close to the double slit experiment
  as possible."
- **c.6733711272** (06:23:04Z):
  - "1. Double-slit interference is not sufficient to establish quantum behavior. Classical electromagnetic waves can
    produce interference fringes, lose them when paths are distinguishable, and recover them under suitable erasure
    arrangements. Consequently, Q-C2-1 must test more than whether OI produces fringes."
  - "2. Third-order interference is not a good quantum-versus-classical discriminator. Standard quantum mechanics has no
    genuine third-order interference under the idealized definition, but classical wave superposition also has this
    property. Moreover, an actual third-order test needs at least three paths, not two. It can test compatibility with
    a quantum prediction, but cannot independently establish genuinely quantum behavior."
  - "3. The quantum eraser needs a more precise observation rule. An observer can avoid directly reading hidden paths
    while still recording detector outcomes and correlations. In a standard quantum eraser, the unsorted screen
    distribution does not recover fringes. Interference appears in appropriately conditioned subsets. The design must
    therefore distinguish indirectly accessible detector records from direct access to hidden variables. These are not
    the same thing."
  - "4. Q-C2-1 must retain its original mathematical target. The established purpose includes investigating whether
    non-Clifford behavior can emerge from OI's native dynamics without being assumed. Ordinary double-slit interference
    does not establish that. The revised experiment must retain a separately defined test of the required operation,
    its physical origin, and its behavior under composition. Otherwise, we risk producing a convincing interference
    demonstration that does not advance the OI–QM equivalence proof."
  - "I would also resolve the freeze decision now: make indirect access the only decisive observation interface for
    Q-C2-1. Any old direct-access calculations may remain as separate mathematical diagnostics, but must not determine
    the quantum-behavior verdict."
  - "Finally, M-ARC should be characterized precisely: its survival result establishes no exposure under a specific
    mathematical test. It does not prove that indirect interference measurements cannot reveal relevant information."
  - "Can OI's own hidden dynamics generate quantum-specific operational behavior that an observer detects indirectly,
    without importing the quantum mechanism being investigated?"
- **c.6733796760** (06:29:08Z), verbatim from the comment (its excerpts, as recorded):

  > The biggest gap is that observing interference fringes is not enough. Classical waves produce fringes too. We need to demonstrate that OI generates the relevant quantum behavior through its own dynamics, without assuming that behavior in advance.
  >
  > 1. An actual OI mechanism producing the pattern — Specify how native OI dynamics creates two alternatives, preserves their relevant relationship, recombines them and produces detection probabilities. None of the quantum mixing or Born-rule machinery should be silently inserted as an assumption.
  >
  > 2. A controllable phase difference — Vary the relative phase between the paths and predict how the screen distribution changes. The model needs to generate the phase-dependent statistics, not simply reproduce a preselected picture of fringes.
  >
  > 3. Which-path and eraser controls — Show what happens when a path record is created, kept, or erased. Measure interference visibility and distinguishability quantitatively. … An eraser test may require correlations between screen detections and an accessible marker detector; screen counts alone may be insufficient.
  >
  > 4. A genuinely nonclassical discriminator — One option is combining interference with single-quantum anticorrelation … Alternatively, a carefully specified contextuality or Bell-type test could be used. The witness must match the physical system and explicitly state which classical models it excludes.
  >
  > 5. A test of the actual missing quantum operation — … The design must identify the candidate operation, show how to implement it repeatedly, and test its composition using accessible measurements. A fringe pattern alone cannot establish this.
  >
  > 6. Frozen predictions and failure conditions — Before execution, specify the source preparation, path settings, detector model, classical alternatives, exact or approximate tolerances, numerical limits, and expected outcomes. Include controls that detect classical look-alikes. A positive outcome must not be awarded merely because no classical explanation was found.
  >
  > | Level | What is demonstrated | Significance for OI |
  > | 1 | OI produces phase-dependent interference | Quantum-compatible behavior |
  > | 2 | OI satisfies a specified nonclassicality witness | Excludes a defined class of classical explanations |
  > | 3 | OI independently generates the required coherent operations | Addresses a major missing mechanism |
  > | 4 | OI reproduces compatible measurements, preparations and repeated compositions | Advances toward operational QM equivalence |
  >
  > … reaching Level 2 does not automatically establish Level 3, and even Level 3 does not establish full equivalence.
  >
  > My recommended change to Q-C2-1: Make the double-slit experiment the operational setup, but define two separate acceptance tests: interference generation and quantum-specific discrimination. Retain native operation generation and composition as explicit scientific obligations.

- **c.6733825267** (06:31:11Z): "It is the physical availability of which-path information, not a conscious observer
  looking at the detector, that matters. Even unread measurement records can suppress interference." "The detector
  should ideally mark the path without absorbing the particle or simply blocking a slit. Otherwise, the changed screen
  pattern has a trivial alternative explanation." "Can native OI dynamics reproduce the transition from interference to
  non-interference when a which-path detector is activated, while preserving the same underlying two-path experiment?"
  "That should be the primary experiment." "… reproducing this transition would be a meaningful step toward quantum
  behavior, though not by itself proof of full OI–QM equivalence."
- **c.6733855134** (06:33:17Z): "The detector must leave distinguishable physical records depending on which path was
  taken, even though nobody reads those records. Simply activating a device must not automatically count as a
  successful which-path measurement." "Unchanged single-path screen patterns are a good control, but not sufficient. A
  detector could randomly disturb the relative phase between paths, destroying interference without retaining useful
  which-path information. I would therefore add a sham detector control: an interaction that produces comparable
  disturbance but does not encode the path." Its table includes: "Sham detector, no path record | Interference retained,
  if the interaction preserves coherence". "The third outcome is a control target, not a guaranteed result; the sham
  interaction must be designed and validated accordingly."
- **c.6733935953** (06:38:58Z): "The screen pattern alone cannot always distinguish which-path recording from random
  dephasing. Both processes can produce exactly the same loss of interference." "The experiment can distinguish their
  causes only by combining screen results with independently validated properties of the apparatus. Those validation
  checks must remain separate from what the modeled observer is allowed to access." "I would also describe the
  dephasing control as having no path-correlated record, rather than no physical record whatsoever. A source of random
  phase noise may itself leave physical traces."
- **c.6734304025** (07:04:54Z): "Every experiment should compare at least two constructions: A. Deterministic substratum
  alone … B. Strengthened observational incompleteness — Does adding independently justified OI constraints enable the
  phenomenon, using the same underlying dynamics wherever possible?" "If both A and B reproduce quantum behavior,
  observational incompleteness may not be necessary for that result. If A fails and B succeeds, we have evidence that the
  additional OI structure matters. We would still need to determine whether the relevant conditions are genuinely
  implied by OI or are independently introduced physical hypotheses. And if B fails, we should investigate whether the
  failure follows from OI itself or from unnecessarily restrictive modeling assumptions." "I would explicitly replace
  the phrase native OI dynamics in future experimental designs with "OI substratum plus independently justified
  observational-incompleteness principles, with every additional assumption identified and tested separately.""
  It also gives the three-way typing: "Established native principles", "Candidate strengthened principles" and
  "Imported quantum assumptions".
- **c.6734374076** (07:09:34Z): "… the ablation should therefore test both whether the principle changes the reachable
  observable predictions and whether it changes which mechanisms can be justified. A stronger principle that merely
  describes observation differently must not be credited with generating new physical dynamics." The planning Issue
  #1210 (QPHEN) maps QX-0 and QX-2 to P and QX-7 to C.
- **c.6734561591** (07:22:01Z), the owner's validation point, verbatim: "One especially important point is that the
  apparatus checks must validate properties of a mechanism generated by OI, rather than introduce the desired quantum
  behavior as an assumption." It is applied through *The two layers*, `K` (a kernel computed from the construction),
  TOMO, and the computed `mech_change`.

- **c.6735159962** (2026-11-09T08:02:29Z), D12 revised for Q-C2-1, verbatim from the comment's excerpts:

  > We can remove D12's additional GitHub Environment approval requirement from Q-C2-1 and rely on the existing V3 protocol.
  >
  > * D12: Remove the GitHub Environment requirement.
  > * V3: Retain the existing F/E designations, exact-head CI attestations, receipts, and verification.
  > * Execution: Preserve the existing owner approvals for scientific dispatches. Do not add a second GitHub approval.
  > * Safeguards: Keep the workflow controls that distinguish authorized scientific runs from ordinary CI and detect unexpected executions.
  > * Review: Have the independent reviewer verify the revised workflow before freezing r10.
  >
  > The tradeoff is that unauthorized computation is not necessarily prevented from starting, but the experiment's controls can detect it and reject the affected round. V3 alone does not enforce GitHub-side authorization.
  >
  > This decision applies to Q-C2-1. Q-C2-2's previously approved Environment requirement remains separate unless we explicitly revise it too.
  >
  > My recommendation: Record D12 as GitHub Environment gate waived by owner; existing V3 governance retained, and continue preparing Q-C2-1 without the additional setup step.

## Owner decisions at the freeze (recorded; #1169 c.6735014875, amaybaum, OWNER, 2026-11-09T07:52:50Z)

The decisions are quoted verbatim below. They "authorize incorporating these choices into the design and continuing the
already-approved preparation. They do not designate F, approve scientific execution, or authorize a merge beyond
existing permissions."

> | L | (i) Complementarity | Level 1 must require the detector-dependent interference transition, not fringes alone. |
> | D18 | (a), conditional | Permit explicitly identified representation choices, but verify they introduce no quantum dynamics, probabilities, or desired outcomes. |
> | D15 | (a) All nine readings | Accept as a candidate strengthened access principle, not an established native OI consequence. |
> | D4 | (a) Phases | Test what existing OI dynamics can produce before introducing quarter phases or NNB. |
>
> I also accept the drafted selections for D1–D3, D5–D11, D13, D16, D17 and the A/B classification, subject to the already agreed independent-review safeguards.
>
> The Level 1 result should continue to distinguish a known paper construction from a new, independently generated physical mechanism. Passing a consistency check must not be presented as a new derivation.
>
> D18 — Representation choices: I accept option (a) only if the path, port, calibration and U′ mappings are recorded in a separate, explicit representation ledger. … The reviewer should confirm that changing these mappings does not secretly insert coherent mixing, quantum probabilities, or contextuality. If an identification supplies a quantum-specific resource, it must instead be classified as an imported assumption.
>
> D14 — Sham detectors: I support option (d) insofar as the sham never changes the primary detector-off/on interference statistic. But the previous attribution rule must survive: if the sham also suppresses interference, the result cannot be reported as a transition attributable to which-path recording. The frozen procedure should mechanically distinguish the observed interference contrast from the separately validated causal attribution. This prevents the experimenter from choosing a favorable interpretation after seeing results.
>
> Lemma P and the cone argument: Send both for independent review. Do not accept either unreviewed sketch as an established result. … A failed proof review should block reliance on that sketch, not automatically invalidate the rest of Q-C2-1.
>
> The decisions above authorize incorporating these choices into the design and continuing the already-approved preparation. They do not designate F, approve scientific execution, or authorize a merge beyond existing permissions.
>
> I also want the final A/B comparison to report separately whether strengthened OI: changes the observable predictions; changes which mechanisms can be justified; merely restricts observational access.
>
> Final decision: Accept recommendations with the D18 and D14 conditions above. Require independent review of Lemma P and the cone argument. Proceed with preparation, but retain all freeze and dispatch gates.

**As applied in this file.**

| item | decision | where applied |
| --- | --- | --- |
| L | (i): Level 1 iff P-COMPLEMENTARITY, with the Level-1 presentation rule | *Levels*; the frozen P texts |
| D1 | (a): r5's direct-access calculations kept as labelled diagnostics. The owner's "Accept recommendations" (c.6735014875) covers it: the recommendation put to the owner was D1(a) | *The two layers* |
| D2 | (a): P is run as a consistency check of a paper derivation, disclosed | hazard 1; the freeze disclosure |
| D3 | (a): the encoded path | *The model of P* |
| D4 | (a): phases `{0, π}`. "Test what existing OI dynamics can produce before introducing quarter phases or NNB." | *The model of P* |
| D5 | (a): native-rule detectors in every arm (L-HET) | *Obligation C* |
| D6 | (a): `K ∈ {6, 12}` | *Obligation C* |
| D7 | (a): B-P plus B-C for flagged instances | *Test B* |
| D8 | (a): the eraser is required | *Test P* |
| D9 | (a): `DESIGN-DS.md` lands as a separate paper record before `D`. The owner's "Accept recommendations" (c.6735014875) covers it: the recommendation put to the owner was D9(a) | precondition 3 |
| D10 | (a): ARP-3-QC22 r13's method, guard machinery and execution design are copied, with D12's removals (Appendix C) | *Test B*; Appendix C |
| D11 | (a): composition with a second system is a later round (NR-11) | *Obligation C* |
| D12 | **GitHub Environment gate waived by owner; existing V3 governance retained** (c.6735159962, revising c.6735014875 for Q-C2-1). Owner approval of each dispatch stays; unauthorized computation is detected and rejected, not prevented | *Scope of authorization and detection*; Appendix C |
| D13 | (a): the marker-strength finding is reported; no mixed arm | *Test P* |
| D14 | (d), with the attribution rule kept as a separate frozen field (`ATTR`) | *Test P* |
| D15 | (a): all nine readings; `Acc(B-P)` typed **candidate strengthened** (access principle), not established native | *Test B*; *Levels* |
| D16 | (a): C's end-of-run carrier meters count as indirect access | *The two layers* |
| D17 | (a): Level 2 from B-P only; the Level-3 qualifier is printed | *Levels* |
| D18 | (a), **conditional**: the representation ledger and its invariance check (*The representation ledger*) | *The representation ledger*; the controls |
| A/B | the reviewer's typing, adopted as frozen | *The A/B typing* |
| Lemma P and the cone argument | independently reviewed: Lemma P PROVED (conditional on Theorem C(ii) and the link hypotheses); the cone argument PROVED UNDER STATED EXTRA HYPOTHESES (STAB) | *Proof reviews* |

## Owner decisions D19 to D23 (recorded; #1169 c.6740078002, amaybaum, OWNER, 2026-11-09T12:29:10Z)

**The record.** #1169 c.6740078002, posted as amaybaum, author association OWNER, 2026-11-09T12:29:10Z, recording the
owner's answer given in the coordinating Claude Code session. The question put to the owner, verbatim from the
comment:

> Do you, as owner, adopt Q-C2-1 D19–D23 as recommended and authorize the preparation work?
>
> Decisions: D19(0) c, (i) a, (ii) b, (iii) c, (iv) a; D20 b; D21 b; D22 a; D23 c.
>
> Safeguards: no narrowing to manufacture success; resource limits fixed before execution, with an over-limit B-P giving VOID/inconclusive under the frozen rules; a failure in C doesn't erase P's result, but compromised provenance invalidates every affected result; no imported quantum mechanism via representation choices, comparison maps or reductions.
>
> Authorized now: r14, bringing the scripts up to date, ordinary non-scientific self-tests, and independent preparation review.
>
> Not authorized: design run, gate tests, F designation or dispatch, any scientific computation. Q-C2-1 is completed before Q-C2-2 is activated.

The owner's answer, verbatim: **"Adopt and authorize"**. The comment adds, verbatim: "The options are those of the
decision sheet, c.6737336374. D19 (i)(d) is not selected, so the owner's separate-outcome condition for it does not
arise." The decision sheet is #1169 c.6737336374 (posted as amaybaum, author association OWNER,
2026-11-09T10:05:40Z). Its recommendations were the coordinator's; the record above adopts them.

**Scope of the authorization.** Authorized: this revision, the scripts brought up to it with fixture-only self-tests,
and an independent preparation review. Not authorized: the design run (which runs the stress test ST-BP of C.8
item 2), the gate tests, `F`'s designation or dispatch, and any scientific computation. Nothing in this file has been
run under this record.

**As applied in this file.**

| item | decision | where applied |
| --- | --- | --- |
| D19 (0) | (c): the caps count the extreme rays of `cone{a_p}`; each removed row is certified exactly | *Test B*; B-RAY; C.8 items 1 and 15 |
| D19 (i) | (a): B-P's caps and budget are raised from the stress test ST-BP at 32 preparations and fixed before `F`; a B-P over them gives B-VOID, reported as a limitation | *Test B*; C.7; C.8 items 1 and 2 |
| D19 (ii) | (b): construction A of B is reported only | *Test B*; C.8 item 13 |
| D19 (iii) | (c): B-C is reported only, for every flagged instance | *Test B*; *Obligation C*; C.8 item 13; D.4 |
| D19 (iv) | (a): an instance is flagged iff the conjunction of `decide-c`'s step 2, 3 or 4 holds | *Obligation C* |
| D20 | (b): the diagnostics are bounded to depth 1 (27,600 propagations) | *The two layers*; *Runtime*; D.2; D.6 |
| D21 | (b): VOID is test-level; the S1 binding is restored by the artifact-zip comparison | *Test B*; *Levels*; *Stop rule*; *Scope of authorization and detection*; edit rows 72–90; C.8 items 3, 7 and 14 |
| D22 | (a): slot 0 ↔ `X`, slot 1 ↔ `Z`, with CNOT-marker arms; a QM benchmark that gates nothing | *Test B*; the QM-P and C-IFACE rows |
| D23 | (c): `pred_change` for ABL-SA1b is the pair `{common, added}` | *Test P*; C.5a |
| safeguards | SG-1 to SG-4 below, each a frozen rule with its checkpoint | *Invariants and their checkpoints* |

**Feasibility under the decisions.**
- **B-P** (32 preparations, `d ≤ 18`) exceeds the copied caps as listed. Under D19 (0)(c) and (i)(a) its caps count
  extreme rays and are raised from ST-BP before `F`. Whether B-P is within them is not known before `F`. If it is not,
  B is VOID as a reported limitation and Levels 2 and 3 are not awarded; P's token and Level 1 stand (D21 (b)).
- **Construction A of B** (up to 256 outcomes against 200) and **the B-C fragments** (up to 91 preparations against
  16) can exceed the general caps (owner-approved R5 default). They are reported only (D19 (ii)(b),
  (iii)(c)), and their `out_of_scope` voids nothing.
- **The diagnostics** are bounded to 27,600 propagations (D20 (b)). A job-B timeout still halts the round (C.6).

### D19. The B fragments against the caps (items 1, 2 and 10)

**Facts.** These are computed from the definitions in this file. No B fragment is built.
- **B-P.** B-P has 32 preparations, and `Acc(B-P)` has 51 effects: the 50 outcomes of the nine settings and the unit
  effect. Its rank satisfies `d ≤ 18`, since the effects span at most 18 functions on the five read slots (*Test B*).
  Its number `n` of extreme rays is at most 32 and is not computed before `F`.
- **The copied caps** (C.1; counted under (0)(c)) are: at most 16 preparation generators; `d ≤ 16`;
  `C(n, d − 1) ≤ 10^5`; and at most 200 effects before reduction.
  - With `n = 32`, the binomial cap holds only for `d ≤ 5` (`C(32, 4) = 35,960`; `C(32, 5) = 201,376`).
  - The verifier's facet enumeration at `n = 32` and `d = 18` visits `C(32, 17) = 565,722,720` subsets.
- **Construction A of B** registers all eight slots jointly. That is one setting with up to 256 outcomes, above the
  effect cap unless at most 200 of them have positive probability.
- **A B-C fragment** has up to 91 preparations (7 QA laws × 13 orbit steps) and `d ≤ 4`. At `d = 4` the binomial cap
  holds for `n ≤ 85` (`C(85, 3) = 98,770`; `C(86, 3) = 102,340`).
- **Flagged instances.** Between 0 and 600 instances can be flagged. The number is not known before `F`.
- **The consequence.** Under the copied rules (C.1 step 6, C.4's C-BUDGET, C.6) a fragment over a cap or a budget
  would halt the round. Under D21 (b) it voids only its own test's token, and only B-P can do that (C.8 items 13
  and 14).

**Decision** (owner, c.6740078002): (0)(c), (i)(a), (ii)(b), (iii)(c) and (iv)(a).

- **(0)(c), how the caps count.** "Preparation generators" are the extreme rays of `cone{a_p}`, and `n` in
  `C(n, d − 1)` is their number. The facets of `cone{a_p}`, which are all that steps 2–4 and the verifier use, depend
  only on its extreme rays. Each removed row is certified by an exact nonnegative combination of retained rows, which
  the verifier checks (C.8 item 15). Removing non-extreme rows therefore changes no decision. "Effects before
  reduction" are the outcomes of the fragment's `Acc` settings that have positive probability under some preparation
  of the fragment, together with the unit effect. Under (0)(c) the cap `d ≤ 16` can still fail for B-P, since only
  `d ≤ 18` is known; B-P's caps are those of (i)(a).
- **(i)(a), B-P's caps from a stress test.** B-P keeps its 32 preparations and its whole `Acc`. Its caps and its
  budget are raised from the stress test ST-BP at 32 preparations (C.8 item 2), by the mechanical rule stated there,
  and are fixed before `F`. Their values are PENDING (C.8 item 1), to be fixed by an authorized design run before
  `F`. If no SF-1 instance of ST-BP qualifies as the reference within the maximum budget the owner fixes (`S_max` and
  C.1's timeout test; C.8 item 2), B-P's caps stay at the copied values. A B-P that exceeds its caps or its budget
  is `out_of_scope`, and B is VOID as a reported limitation (SG-2). B-P is not narrowed.
- **(ii)(b), construction A of B, reported only.** It is decided where it is within the general caps and budget
  (C.8 item 1; owner-approved R5 default). Otherwise its reported result is `out_of_scope` (or
  `undecided`), which voids neither B nor the round.
- **(iii)(c), B-C, reported only.** Every flagged instance has its B-C fragment built and reported, as in (ii)(b).
  The C texts print the instance's B status, "out_of_scope" or "undecided" where it applies. The timeout test's
  fragment count is that of C.8 item 2.
- **(iv)(a), which C instances are flagged** (item 10). An instance is flagged iff the conjunction of `decide-c`'s
  step 2, 3 or 4 holds: `HC(12) ∧ CONS(12) ∧ VAL(12) ∧ W-CL ∧ ABL ∧ EMB`; or the same at `K = 6`; or
  `HC(12) ∧ VAL(12) ∧ W-OCT(12) ∧ ABL ∧ EMB`. B-C and C-A are built for flagged instances only; flags are computed in
  job B from the decisive data.

**Not selected:** (0)(a), (0)(b); (i)(b), which narrows B-P; (i)(c); (i)(d), a covering by sub-fragments; (i)(e);
(ii)(a); (iii)(a), (iii)(b); (iv)(b), (iv)(c). D19 (i)(d) is not selected, so the owner's condition for it, a
separate, mechanically defined "not decided" outcome, does not arise. B's tokens are the three of *Test B*.

### D20. The extent of the diagnostics (item 17)

**Facts.**
- Under D1(a), the diagnostics of Appendix D.2 are computed in job B for all eight rules.
- `L_scope(g)` at depth 2 takes up to 8 × 23 × 150 × (1 + 150) ≈ 4.2 × 10⁶ one-round propagations in exact arithmetic,
  before deduplication.
- No token reads them.
- Their time is not measured. Measuring it on the test rules before `F` would evaluate those rules' reachable sets,
  which only job B may do.
- A job-B timeout is a checker outcome, and the round halts with VOID (C.6).

**Decision** (owner, c.6740078002): **(b)**. The diagnostics are bounded to depth 1: `S_0` and every one-round output
of an `S_0` law, 8 × 23 × 150 = 27,600 one-round propagations. They are labelled "depth 1". The diagnostic forms of
CC-DYAD, C-AFFB and C-XB, and C-SCOPE's diagnostic clause, read the same depth-1 sets (D.2, D.6). No diagnostics
benchmark is run. Not selected: (a), keeping them in full with a benchmark; (c), dropping them.

### D21. Test-level VOID (items 1 and 16)

**Facts.**
- Under the copied rules (C.1 step 6; C.4's C-CERT and C-BUDGET; C.5's exit rule; C.6), a red control, an
  `out_of_scope` fragment and an undecided fragment are each a checker outcome: the checker exits 3, the round halts
  with VOID, and no P, B or C token is read.
- Under a test-level reading, the same event voids only its own test's token. P's token and Level 1 then stand.

**Decision** (owner, c.6740078002): **(b), test level.**
- A red decisive-mode control voids the token of each test in its `for` column; a control whose `for` column reads
  "all" voids every token. An `out_of_scope` or undecided B-P voids B's token. An `out_of_scope` or undecided
  reported-only fragment voids nothing and is reported (D19 (ii)(b), (iii)(c)). Each is recorded with its code.
- The checker exits 0 when the output is otherwise complete. The other tests' tokens stand, and `decide-levels`
  computes the Levels from them; a Level whose conditions need a VOID token is not awarded.
- This decision's edits to the copied text are rows 72–90 of the edit log (C.2, C.3, C.4, C.5, C.6). C.1 stays
  verbatim, and C.8 item 14 governs its words.
- **The S1 binding** (re-review R13-B1). It is restored by the artifact-zip comparison, as ARP-1's verdict did: the
  frozen `gh api` template `actions/artifacts/{DEC}/zip`, `zipfile` and `io` in control B's import list (attributes
  `zipfile.ZipFile` and `io.BytesIO` only; the archive is read in memory and no file is written), and `verdict`'s
  canonical-JSON comparison of S1's `measurements.json` with the committed file without `parameters.dispatch_sha`
  (C.8 item 3). The alternative, an exact S1-versus-`E` comparison with its own control, is not selected.
- **Provenance and incomplete output.** The round halts, and every result of the run is void (SG-3), on any of
  these:
  - an incomplete-output halt: a crash or a timeout. The checker's output is then incomplete and no token exists,
    so a crash or a timeout in C's code also voids P's result, the one exception to SG-3's first clause;
  - a failed `check`;
  - a red fixture-mode control at S1 or `E` (C.8 item 14; owner-approved R2 default, precondition 2);
  - a replay mismatch, or a failed S1 binding;
  - a host VOID without a recorded retake;
  - an authorization violation;
  - a control-plane change after `F`.

Not selected: (a), round level.

### D22. The QM-P comparison on B-P's `p`-free settings (item 12)

**Facts.**
- `Acc(B-P)` reads slot 0 or slot 1 of a held cell. In this file slot 0 is `u` and slot 1 is `v` of the cell as it
  stands at registration, after `t = 3` (a naming; `Acc` is symmetric in the two slots, so the naming changes no
  setting). For a coupled arm cell supplied as `(u_a, v_a)`: slot 0 is `u_a`, the kick; slot 1 is `z + v_a`; the port
  follows `x + φ + u_a`. For the off arm, slot 0 is `u_a`, slot 1 is `v_a`, and the port follows `x + φ`. (P's model,
  read by hand.)
- Under the map fixed by the on arm (slot 0 ↔ the marker's `X` readout, slot 1 ↔ its `Z` readout), QM-P's present
  arms do not match SH-0 and SH-K: `X` on an uncoupled environment leaves a deterministic `Z` readout where SH-0 has a
  deterministic slot 0, and the classical-noise `Z^w` arm holds `w` in the `Z` readout where SH-K holds it in slot 0.
- With a CNOT marker prepared in `|0⟩` (on), `|+⟩` (SH-0) and the maximally mixed state (SH-K), and no coupling for
  off, the tables agree column by column for all four arms under that map (QM side exact: writer's probe
  `probes-r13/qmp_marker.py`, `efd583bd…`).

**Decision** (owner, c.6740078002): **(a)**.
- **The map:** slot 0 ↔ `X`, slot 1 ↔ `Z`.
- **QM-P's arms for its restricted fragment:** off, the marker in `|0⟩` with no coupling; on, a CNOT marker prepared
  in `|0⟩`; SH-0, a CNOT marker prepared in `|+⟩`; SH-K, a CNOT marker prepared in the maximally mixed state. The
  path is the control. QM-P's arms for P are unchanged (*The controls*).
- **Paper expectation:** equality, column by column, for all four arms.
- **Role:** a QM benchmark. `bp_equals_qmp` is reported per arm and gates nothing: no `decide-*`, no `decide-levels`
  and no ADA status rule reads it (SG-4; C-IFACE).

Not selected: (b), the same map with QM-P's present arms; (c), no comparison.

### D23. `pred_change` for the read-set ablation ABL-SA1b (item 13, in part)

**Facts.** `pred_change` reports "whether any observer-layer quantity of any admissible arm changes". ABL-SA1b changes
the read set itself: registering both slots of the held cell defines observer-layer quantities that do not exist under
SA-1(b) (`OLC`'s joint-subset conditionals). With registration modelled without meter cells, every quantity defined
under both read sets is unchanged. This field is part of the A/B report the owner required (c.6735014875).

**Decision** (owner, c.6740078002): **(c)**. For ABL-SA1b, `pred_change` is the pair `{common, added}`:
- `common`: a boolean, true iff some observer-layer quantity defined under both read sets changes for some admissible
  arm. Paper expectation: false.
- `added`: the sorted list of the observer-layer quantities defined only under the ablation's read set (`OLC`'s
  conditional `V` and `Pz` per joint subset, and `OLC.joint`). Paper expectation: non-empty.

Not selected: (a), `common` alone; (b), one boolean including the added quantities.

### The owner's safeguards, as frozen rules

Each safeguard is quoted verbatim from c.6740078002 and stated as a frozen rule. Its checkpoints are in *Invariants and
their checkpoints*.

- **SG-1. "no narrowing to manufacture success".**
  - B-P is decided whole: the 32 preparations and the nine settings of `Acc(B-P)` (51 effects) of *Test B*. No
    sub-fragment, reduced preparation set or restricted `Acc` replaces it, before or after `F`.
  - The only reductions of a fragment are step 1's copied effect deduplication and D19 (0)(c)'s removal of
    non-extreme rows. Each removal carries an exact certificate that the independent verifier checks, and neither
    changes a decision.
  - Construction A of B, B-P's completions and the B-C fragments are reported only. No token and no Level reads them,
    except UPR-BC's label, which can only reclassify a B-C result as a benchmark.
  - After `F`, no fragment, `Acc`, cap, budget, `S_max` or timeout changes (C.6).
  - **Checkpoint.** `decide-b`'s step 1 gives B-VOID unless B-P's record has 32 preparations and reads the nine
    settings of `Acc(B-P)`; C-CERT, B-RAY and M-RAY for the removals; C-IFACE's rule that `decide-b` reads only
    B-P's record and the B controls, with its mutation; C.6.
- **SG-2. "resource limits fixed before execution, with an over-limit B-P giving VOID/inconclusive under the frozen
  rules".**
  - `S_max`, B-P's caps and budget, the general caps and budget, `timeout-minutes` and the stress pin are entered in
    this file and in the pinned checker before `F`. Control P refuses `F` while any is `PENDING`. `check --freeze`
    recomputes the caps and budgets from the pinned `stress.json` by C.8 item 2's rule, and fails on any difference.
    It also requires the `S_max` entered in this file, the checker's `S_MAX` and the `S_max` recorded in
    `stress.json` to be equal (C.8 item 2).
  - A B-P that exceeds a cap or its budget, or whose certificate does not verify, is recorded `out_of_scope` or
    `undecided`. `decide-b` gives B-VOID, and the note prints the frozen limitation sentences (*Test B*). Levels 2 and 3
    are not awarded. There is no retake, re-run, narrowing or budget change (C.6).
  - A job timeout remains a checker outcome, an incomplete-output halt, which halts the round (SG-3).
  - **Checkpoint.** Control P; `check --freeze`'s recomputation; M-BUDGET; the self-test cases for an `out_of_scope`
    and an `undecided` B-P; C.6.
- **SG-3. "a failure in C doesn't erase P's result, but compromised provenance invalidates every affected result".**
  - VOID is test-level (D21 (b)). A red decisive-mode control, an `out_of_scope` B-P or an undecided B-P voids only its
    own test's token. The other tokens stand.
  - A provenance failure or an incomplete-output halt voids every result of the run: the round halts under `S12`,
    and no token, Level or ADA reading is reported as a result. Both are listed under D21. An incomplete-output halt
    (a crash or a timeout) is the one case in which a failure in C also voids P's result.
  - **Checkpoint.** The `decide-levels` self-test cases "C-VOID with P-COMPLEMENTARITY gives Level 1" and "B-VOID with
    P-COMPLEMENTARITY gives Level 1"; `verdict`'s self-test, which must print VOID on each provenance failure and
    incomplete-output halt; S1-BIND; C.6.
- **SG-4. "no imported quantum mechanism via representation choices, comparison maps or reductions".**
  - **Representation choices:** the representation ledger, REP-INV and the reclassification rule, unchanged.
  - **Comparison maps:** D22's slot-to-basis map and QM-P's CNOT-marker arms enter only `bp_equals_qmp`, a QM
    benchmark that no `decide-*`, `decide-levels` or ADA status rule reads.
  - **Reductions:** a row is removed under D19 (0)(c) only with an exact certificate that it is a nonnegative
    combination of retained rows, so the cone, its facets and every decision of steps 2–4 are unchanged. D20 (b)'s
    depth bound applies only to the diagnostics, which no token reads. D23 (c) reports the quantities that ABL-SA1b's
    read set adds apart from the quantities it changes.
  - **Checkpoint.** REP-INV and REP-PLANT; C-IFACE's rule that no `decide-*`, `decide-levels` or ADA status function
    (`ada_*`) references `bp_equals_qmp`, with its mutations; B-RAY, M-RAY and C-CERT; the diagnostics' label.

## The hazards, stated first

1. **P is not blind; its paper expectation is stated** (owner element 6; §A.23).
   - P's construction B is derived on paper (AP1 §4.5), and the writer's and the reviewer's probes evaluate it.
   - Expected token: P-COMPLEMENTARITY.
   - A/B, existence reading: both succeed. A/B, universality reading: A fails and B succeeds, carried by SA-1(c), which
     is posited, not derived.
   - P is a consistency-axis check.
   - **Level-1 presentation** (owner, c.6735014875: "Passing a consistency check must not be presented as a new
     derivation"). A Level 1 award here records that the run reproduces a known paper construction. It is not an
     independently generated mechanism, and every note that prints Level 1 prints that sentence with it.
   - `ATTR` reads "not attributable" in construction B, in QM and in classical waves. This is a known structural fact,
     disclosed in advance (*Test P*).
2. **P excludes no classical explanation.** Its table has noncontextual classical models: a classical wave with a
   polarization-type marker, and construction B itself, an epistemically restricted model (OICORE-1 §5(b); AP1 §0).
   P maps to Level 1 at most.
3. **No single suppression is attributable to recording, in any theory** (re-review R7-B1).
   - Screen statistics depend only on the arm's system-level channel. In construction B that channel is the kernel
     `K`. In QM and in classical waves it is the reduced channel on the path.
   - A record-free arm with the same channel suppresses identically. Dephasing is therefore an equally valid
     explanation of each suppression.
   - "Path-correlated record or not" is relative to access. QM's purified dephasing (environment `|+⟩`, CZ) carries a
     conjugate-basis record (`D = 1`). Construction B's dephasing arm has `D = 0` only because its second slot is unknown
     under N2.
   - What P can state is class-level: over construction B's admissible arms, every arm that records also disturbs and
     suppresses (complementarity).
   - The record is visible to an observer who reads the marker (M2 under `Z±`).
4. **No substratum-only P exists** (re-review R7-B2). Without N2 there are no probabilities. Without P3 arming and
   E-iso there is no detector switch, so under FIX the off arm does not exist. Without H-PREP there is no `X−` and no
   `φ = π`. Without L-PATH and L-PORT there is no path and no port. Construction A of P is therefore "B minus SA-1(c)",
   named `A_P`, and the scaffolding it shares with B is untested in this round (NR-16).
5. **B is relative to the fragment and its `Acc`.** Every OI table comes from a configuration model, so B-CONTEXTUAL is
   a degenerate pairing (Lemma NC-F). The LP reads the whole owner-typed `Acc`, so no artefact inside `Acc` remains.
6. **C's records are the U′ statistics** (L-UPRIME, used).
7. **Finite scope; rational reach.** A null result is a scoped finite search. **For instances with `STAB(K)`**, a W-CL
   positive can only be of R60 or `S_3` type (orders 3 or 6); without `STAB(K)` the spectrum is reported without that
   bound. This rests on the cone argument, which is proved only under STAB (*Proof reviews*).
8. **Heterogeneous rule in C** (L-HET; D5).

## The objects

- **`D`** = `cac5d26441dd33e9348151487e4df7b547195481`, the head of `main` on 2026-11-11 ("Merge pull request #1212:
  correct SM ring degree bounds"), by the owner's decision #1169 c.6789676675 (amaybaum, 2026-11-11T07:19:40Z): "Pin D
  to main as it stands when the round PR is opened (cac5d264 today, unless main moves)." When the round PR is opened,
  `D` is re-confirmed equal to `main`'s head; if `main` has moved, `D` is the then-current head of `main` by the same
  decision, and every pin read at `D` is re-checked there. At `cac5d264`, `.github/workflows/verify.yml` has blob
  `3a9dc8a97fd6f9d6d5f17cf390b5aabf37d65233` and every blob pinned under *Inputs* equals its pin.
- **`F`**: the owner-designated commit carrying this file.
- **S1**: single-parent child of `F` adding the scripts at their pinned blobs, the two STAB-FALSE certificates at their
  pinned sha256s (C.8 item 12), `evidence/design-run.json`,
  `evidence/f-run/results.json`, the gate-test records, and the frozen splice.
  - Its owner-approved dispatch (job B, attempt 1, on the round branch) computes every token. It is the decisive
    computation for B and C, the first evaluation of any test rule's orbit and of any B fragment built from OI data, and
    the first CI evaluation of P's construction B (paper-derived).
- **`E`**: single-parent child of S1 adding `evidence/measurements.json` (bound to the approved decisive computation by B6
  at `E`, and to S1's output by the S1 binding; D21 (b), C.8 item 3), `evidence/approvals.json` (C.8 item 9),
  `evidence/s1-run/results.json`,
  `evidence/order.json`, `evidence/order-s1.json` and `result.md`.
- **`W`, `Λ`, `Q`**: as §A.39 and `S12`.

**Branches** (frozen; the line below stands alone at column 0):

arp2-qc21 branches: round research/arp2-qc21-20261108; dev draft/arp2-qc21-dev

## Inputs (blobs at `D`; re-checked by DS)

The rows QA, FB, M2D, MI-R and SUB are in Appendix D.1. The rows below are added, and replace r5's AP1, RCH and M-ARC
rows:

| short | path | used for |
| --- | --- | --- |
| AP1 | `R/apparatus-1-20261107/DESIGN.md` (`51c24aeb…`) | SA-1 (AP1:282-309; "not derived", AP1:347); the coupled tick (AP1:464-530); the eraser words (AP1:628-668); C3 and C9 (AP1:670-682); Lemma 4′ (AP1:698-730); Lemma 5 (AP1:731-745) |
| M-ARC | at `fd539e15` (ARP-1's landing; the same blobs at `D`): `verification/receipts/ARP-1-MARC.json` (blob `f4f2b06b40f1dcb91d4c0f2f020688be422b7bc8`); `R/round-arp1-marc-20261108/preregistration.md` (`af7c4f228393ecaa9d334d50410e3c87d6faf80e`), `result.md` (`6fb623273c4db9aec5fd9ca0cfc80bd923076ece`), `evidence/measurements.json` (`f4a783aafcb44953231e6e4566a1e93bb71ba21f`), `marc_check.py` (`38d6f67559b6641590b3baf126b2247e97a4e28c`), `controls.py` (`5e6318896ffe274bf5cca7dbcb2cb537b1bad4a1`) | precondition 1; the relation section |
| QC22 | Q-C2-2's `preregistration.draft.md` r13, sha256 `15d90b24…` (scratch, not on `main`); its r14, sha256 `9e3ef0c9…`, and r14a, sha256 `d751a127…` (scratch, not on `main`) | the source of Appendix C (D10); r14 is the source of the wording of edit rows 92–99, 101, 105, 113 and 118, and r14a of rows 109–112, 114–117, 119 and 123, C.7's re-derivation and precondition 2's R10 (provenance: the wording used is stated here in full) |
| RCH | REACHABLE r3 (PENDING: path and blob on `main`) | Theorem C, for CC-NAT's paper expectation only |
| DSN | `DESIGN-DS.md`, the revision landed under D9(a) and pinned under precondition 3 (drafted as r13; PENDING: path and blob on `main`) | the model; the typing; the findings; Lemma CL; Lemma P (sketch) |
| OIC | OICORE-1 r6 (scratch, not on `main`; §A.42 item 8: provenance for the typing, not support) | the candidate-principle statuses |
| V3V | `tools/v3_verifier.py` at `D`: blob `681c673734427cb9f316feee09b7c5ffba348004`, sha256 `fc6545f581cd3282d43a65edbefea69722a2b3f006679a6ec9b1627845cede4a` (re-review r14b-N2) | control T (C.5 rule (h)); the governed-paths digest; precondition 1's `--verify-round` output |

None is a premise of a verdict (§A.46 item 7).

## The question

**Central** (owner, c.6733711272): "Can OI's own hidden dynamics generate quantum-specific operational behavior that an
observer detects indirectly, without importing the quantum mechanism being investigated?"

- **P (primary).** In construction B of *The model of P*, with the same source, phase settings, schedule, screen and
  cells in every arm:
  - Does activating the non-absorbing marker, whose held and unread record distinguishes the paths, suppress the
    two-setting screen interference?
  - Over construction B's admissible arm class, does every arm that records the path also disturb and suppress
    (complementarity)?
  - Reported beside these: the same two questions for `A_P` (existence and universality readings), and the decomposition
    by the two shams.
- **B (secondary).** Does P's detector-record table, read over its whole owner-typed `Acc`, admit a noncontextual model
  over the fragment's own equivalences? With complete access (construction A of B), what is measured?
- **C (secondary; obligation).** Does a non-affine bounded gadget on a two-cell encoded carrier, composed up to 12 times,
  act on its detector records as one fixed operation outside the Clifford class, valid on its orbit? Is the witness
  absent under the affine and idle ablations? Is it present with `reg = none`?

General questions stay open under every outcome.

## The two layers (frozen)

- **Observer layer.** Records of registered detector cells only:
  - the screen port;
  - the held cells' slot records, in the eraser and B;
  - C's records `S_Z`, `S_X` and `S_Y`;
  - gadget heralds;
  - coincidences among these, and conditioning on them.

  "Indirect" means through registered detector cells. Every OI detector is a meter that copies a functional of what it
  couples to. Marker-detector reads, coincidences and the eraser's conditioning are admitted under every option of D16
  (c.6733711272 item 3; c.6733796760 element 3; D8(a)); D16(a) (decided) admits C's end-of-run carrier meters as well.
  No carrier slot is registered. The comparator I1 and `R` are not read; C's detectors
  realize U′'s functionals (L-UPRIME, used).
- **Validation layer** (computed from the construction; not observer data): `D`, `K`, NONABS, SPI, COMP, TOMO, C-DET.
- **Diagnostics**: the direct-access quantities of Appendix D.2 (D1(a); bounded to depth 1, D20 (b)). No token reads them.

**C-IFACE.**
- *Static part.* P's screen inputs, B's tables and C's witness are functions of observer-layer tables. P's attribution
  conditions and B's eligibility read only validation fields.
- *Certificate exemption.* Certificate candidates are exempt. For example, step 2 of the LP method reads charged
  configuration laws to propose a model. A verified certificate is sound whatever its provenance, and the verifier
  checks it against the observer-layer table (review N7).
- *Mutation.* A carrier-slot read fed into P's screen input must turn the self-test red.

## The A/B typing (frozen at `F` as owner-typed; reviewer's proposal, `DESIGN-DS.md` §2)

Construction A (established native) is only the bijective symmetric second-order step: free tick, `q = 2`, the affine
rule choice, and retention (RET-w).

| ingredient | construction | three-way type | kind | `dynamics_credit` |
| --- | --- | --- | --- | --- |
| SA-1(c) half-known ready cells | B | candidate strengthened; posited, not derived | state restriction | none |
| N2 uniform law (apparatus cells and the hidden-sector cell) | B | candidate strengthened | state restriction | none |
| H-PREP (known value 1; QA family) | B | candidate strengthened; open hypothesis | state restriction | none |
| SA-1(b) terminal registration | B | candidate strengthened (RET-s) | access restriction | none |
| **P3 arming and E-iso** | B | candidate strengthened; in tension with FIX | **dynamics (control of couplings): it changes which step applies per tick, and the detector switch is a P3 switch** (re-review R7-B2) | a different mechanism |
| held, unread marker (L-HOLD) | retention A; isolation and non-reading B | established native; candidate strengthened | access restriction | none |
| observer interface restriction (L-ACC) | B | candidate strengthened (ACC-R2-type) | access restriction | none |
| forward conditioning, refills (C) | B | candidate strengthened | access restriction; supply | none |
| NNB (C's `Λ_{y,b}`; P under D4(b)) | B | supplied conditional premise | dynamics (an added coupling) | a different mechanism |
| L-PATH, L-PORT, L-CAL, L-UPRIME | neither | imported representation (D18) | — | — |
| Englert's bound, the Clifford class, QM-P, the supplied gates | — | imported quantum structure, in comparators and controls only | — | — |
| the non-affine `g` in C | — | a change of dynamics | dynamics | a different mechanism |

**Ablation report rule** (owner, c.6734374076: "test both whether the principle changes the reachable observable
predictions and whether it changes which mechanisms can be justified"; c.6735014875: "report separately whether
strengthened OI: changes the observable predictions; changes which mechanisms can be justified; merely restricts
observational access").
- Each ablation, and the overall comparison of `A_P` against B, reports **three separate fields**: `pred_change`,
  `mech_change` and `access_only`. `dynamics_credit` is kept beside them as the frozen kind label.
- `decide-*` reads none of them.
- **`access_only`** (computed): true iff the joint law of all cells at the end of the run, registered and unregistered,
  is identical between construction B and the ablation for every source and phase, so that the two differ only in which
  records are registered or held unread.
  - **Registration is modelled without meter cells** (re-review r10-N2): registering a slot is a read of the world
    law, not a coupling. A physical read by a meter would change the world laws. Under this model, ABL-SA1b's
    `access_only` is true.
  - **`A_P` against B** (r10-N3). Arms present in both classes are compared arm by arm. An arm present in only one
    class makes `access_only` false.
  - Expected true for ABL-SA1b. Expected false for ABL-SA1c, ABL-RECIP, ABL-ENV-u and ABL-ENV-v, and for `A_P` against
    B.
- **`pred_change`** (computed): whether any observer-layer quantity of any admissible arm changes.
- **`mech_change`** (computed; re-review R7-B2).
  - For the construction and for the ablation, the checker forms the map *validation cell → set of admissible
    mechanisms realizing it*.
  - A validation cell is `(V, D, K)`, with `K` the kernel. `V` comes from the observer layer; `D` and `K` from the
    validation layer.
  - **The mechanism grain is frozen** as supply × coupling type. A supply is the arm cell's supply over the frozen
    alphabet; the coupling type is one of reciprocal, copy-only or unarmed. Nothing finer is distinguished
    (re-review r8-N4).
  - `mech_change` is the list of cells whose mechanism set differs between the two maps.
- **`dynamics_credit`** (the frozen label of the row's kind): a state or access restriction is never credited with new
  dynamics, whatever `mech_change` shows. A dynamics row is credited with a different mechanism.

## The representation ledger (frozen; owner condition on D18(a))

Each identification below is a **representation choice**: a naming of native records. None is an OI principle, and each
is recorded here separately from the A/B typing. For each entry the table states what it identifies; why it supplies no
dynamics, probabilities or desired outcomes; and its admissible alternatives. Check REP-INV, below, varies each entry
over those alternatives.

| id | identifies | why it supplies no dynamics, probabilities or outcomes | admissible alternatives (frozen) |
| --- | --- | --- | --- |
| **L-PATH** | "path" with the value of the carrier cell's encoded `z`; "single-path sources" with `Z±`; "coherent source" with `X±` | It names which native functional is called the path. The step, the supplies and the N2 counting are unchanged; every probability is a configuration count. The marker's record and kick follow from the reciprocal step, whatever the functional is called | (α) relabel the path values, `z ↦ z + 1`. (β) the conjugate assignment, path = `x`: the frame is shifted by one free tick, so the marker is coupled at the odd tick and the screen at the even tick, with the sources exchanged accordingly |
| **L-PORT** | "port 0" with the registered screen value `u_s = 0` | It names an outcome of a native registration. `V` is an absolute difference, and `D` and `K` do not involve the port | (α) swap the port labels. (β) read the screen bit one free tick later, from the slot that then holds it |
| **L-CAL** | C's calibrated frame: `R_op` sends `ρ(Λ_0)`, `ρ(Λ_{a,0})` to `0`, `e_a` | It is an affine coordinate choice on record vectors. The records, herald, orbit and CONS are unchanged | every recalibration by one of the 48 signed permutations, that is, a relabelling of the axes and of the source values |
| **L-UPRIME** | C's detector set: `f_z`, `f_x`, `f_y` of U′ | It names which native meters are read. The meters are native single-edge or `XOR` couplings (L-HET), and the gadget's dynamics is unchanged | U′ relabelled by an affine symplectic carrier bijection that induces a map on all laws (the 48 classes of REACHABLE §2.3's reviewer control RC2: the 768 affine bijections in AGL(4,2) that induce a map on all laws give 48 signed permutations, each 16 times), with the detectors transported accordingly |

**REP-INV** (validation layer; computed in job B with the decisive data; frozen).
- **P.** For each L-PATH and L-PORT alternative, recompute P's token inputs (`V`, `D`, `K` for every arm of `Adm_B`),
  the class predicate, `ATTR`, the eraser fields and B-P's table up to relabelling.
- **C.** For each L-CAL and L-UPRIME alternative, recompute C's witnesses (W-CL in both frames, W-OCT, VAL, CONS) and
  B-C's table up to relabelling.
- **Frame transport** (re-review R10-B4). Under a recalibration `S` (L-CAL) or an RC2 relabelling (L-UPRIME), the
  encoded transposition is transported to `S P S⁻¹`, and `det_enc` is computed in the transported frame. W-CL's
  either-frame rule uses the transported transposition. Keeping `P` fixed would lose W-CL for C-R60-ODD's map in 8 of
  48 recalibrations (`review/probes-r10/repinv_frame.py`), and transporting it loses it in none. REP-FRAME holds this.
- **Output.** Per entry and alternative: `invariant`, or the list of changed inputs.
- **Readings (frozen; r13 item 13).**
  - **L-PATH (β)** is P's model with one free tick prepended. Every scheduled event moves from `t` to `t + 1`. The
    carrier and the phase cell are supplied at `t = 0` as *The model of P* states them, the arm cells and the screen at
    their coupling ticks, now `t = 3` and `t = 4`, and `u_s` is registered after `t = 4`. The source names exchange:
    "coherent" names `Z±` and "single-path" names `X±`.
  - **L-PORT (β)**: the screen stays unarmed for one more tick after `t = 3`, and its bit is read from `v_s` after
    `t = 4`.
  - **"Up to relabelling"** for B tables means equal after the alternative's own relabelling, and no other:
    L-PATH (α) exchanges `Z+` and `Z−`; L-PATH (β) exchanges the source names as above; L-PORT (α) exchanges the
    screen outcomes 0 and 1; L-PORT (β) relabels nothing; for B-C, L-CAL and L-UPRIME relabel the detector outcomes
    by the signed permutation they induce. Whether a fragment is contextual is invariant under every such
    relabelling; that is what the reclassification rule reads, and the table comparison is reported.
  - **A B table that differs beyond relabelling** (owner-approved R7 default, precondition 2) is not
    re-decided. It is recorded among the alternative's changed inputs, and the reclassification rule reads it as a
    change of whether the fragment is contextual, so the identification is reclassified as imported. No REP-INV
    re-decision enters the timeout test's count (C.8 item 2).
- **Scope** (re-review R10-B3). REP-INV tests **outcome-neutrality within each identification's symmetry class**. It
  catches implementation errors (REP-PLANT). It cannot show whether a class as a whole supplies a resource.
- **Paper confirmation for L-PATH, L-PORT and L-CAL** (the reviewer's check, r10 re-review): each names native
  registered records or affine coordinates, and supplies no dynamics, probability or contextuality.
- **The non-symmetric test for L-UPRIME, for B-C (UPR-BC; mechanical; frozen).** U′'s three functionals are B-C's whole
  access class. If a B-C fragment is B-CONTEXTUAL, and `decide-b`'s completion "every slot of every cell, registered
  jointly" restores a model, then L-UPRIME is reclassified as **imported for B-C**. That B-C result is then printed as a
  benchmark result, "contextuality supplied by U′'s read set". `decide-levels` and the note apply the rule. Under
  D17(a), B-C does not count toward Level 2, so no Level changes. The rule labels the printed result. When that
  completion is `out_of_scope` or `undecided`, no label is printed, L-UPRIME is not reclassified, and the result is
  printed as measured with the completion's status (owner-approved R9 default, precondition 2).

**Reclassification rule** (frozen). An identification is reclassified as **imported**, and every token that depends on
it is reported as a **benchmark result** with no Level awarded from it, if varying it among its admissible alternatives
changes any of the following:
- a token;
- whether W-CL or W-OCT fires;
- whether a B fragment is contextual;
- whether P's class predicate holds.

Such a change is the operational sign that the identification supplies a quantum-specific resource: coherent mixing,
quantum probabilities or contextuality. This rule is applied mechanically by `decide-levels`. It is not a VOID: the
measurements stand and are reported.

**Paper expectation** (disclosed; not a premise). Every alternative above is a symmetry of the native construction:
- relabellings and frame shifts commute with the reciprocal step;
- signed-permutation recalibrations preserve the unit-modulus spectra up to O_h compatibility, and ℓ1 and the ball;
- RC2's affine symplectic relabellings induce signed permutations.

REP-INV is therefore expected to read `invariant` for every entry.

## The model of P (frozen)

As in `DESIGN-DS.md` §3.
- **Cells.** Carrier `c`, phase cell `p`, arm cell(s) `a`, screen `s`, over `F_2`.
- **Step on armed edges.** `u_i' = Σ_{j armed with i} u_j + v_i`, `v_i' = u_i`. Unarmed cells swap their slots. Every
  supplied cell is stated at its coupling tick.
- **Schedule.**
  - `t = 0`: `c–p` armed.
  - `t = 1`: free.
  - `t = 2`: `c–a` armed (unarmed in arm off).
  - `t = 3`: `c–s` armed; `u_s` is registered (the port).
- **Held cells.** `p` and `a` are held, decoupled and unread in P.
- **Sources.** `X±` (`x` known, `z` unknown); `Z±` (`z` known, `x` unknown).
- **Phase.** `p = (φ, ·)`, `φ ∈ {0, 1}`: a known bit added to `x`, two settings.
- **The supply alphabet `Σ`** (frozen). Single fresh arm cells `(a, b)` with `a, b ∈ {0, 1, w}`, where distinct `w`
  symbols are independent unknowns. Added to these are the two cells whose known functional is `u + v`: `(w, w)` and
  `(w, w + 1)`, one unknown occupying both slots.
- **`Adm_B` is generated by rule** (re-review r8-N3): the off arm; every cell of `Σ` with exactly one slot known and the
  other slot an independent unknown; and the N2 environment cell `(w, w′)`. Each cell is coupled reciprocally at
  `t = 2`. The rule yields the four ready cells `(w, 0)`, `(w, 1)`, `(0, w′)`, `(1, w′)` and the hidden-sector cell.
  - The `u + v`-known cells are excluded from `Adm_B`, for two reasons: SA-1(c) as AP1 states it, "its other slot is
    unknown" (AP1:297-299); and AP1's type grading, which gives each fresh unknown one slot type (AP1 §4.2), whereas
    `(w, w)` puts one unknown in both slots.
  - The reviewer's probe (`review/probes-r8/adm_closure.py`) shows that these cells also record and suppress
    (`V = 0`, `D = 1`), so the exclusion does not affect the outcome.
- **Named arms** (all in `Adm_B`): on = `(w, 0)`; SH-0 = `(0, w′)` (coupling-matched, kernel identity); SH-K = dephasing
  = `(w, w′)` (kernel-matched to on, with no path-correlated record under N2).
- **`A_P`** (construction A of P as posable) = construction B minus SA-1(c). **`Adm_A` is generated by rule**: the off
  arm and every cell of `Σ` (nine slot-wise cells plus the two `u + v`-known cells), coupled reciprocally. Everything else is B's shared scaffolding, kept and untested
  in this round:
  - P3 arming and E-iso;
  - N2 and H-PREP;
  - the screen's terminal registration;
  - L-PATH and L-PORT.

  A substratum-only P cannot be posed (hazard 4; NR-16).
- **Eraser (required; D8).** For every arm in `Adm_B` and every slot of the held arm cell, the screen is sorted by that
  slot's value, over both phases.

## Test P: complementarity in a two-path experiment

**Observer-layer quantities** (exact):
- `s(arm, src, φ) = P(u_s = 0)`;
- `V(arm) = |s(arm, X+, 0) − s(arm, X+, 1)|`;
- `Δ(arm, φ)`, the departure from the single-path mixture;
- the eraser fields. For each arm, each held slot `σ` of `a` and each value `b`: the conditional `V` given `σ = b`, and
  the unsorted `V`.
  - **The `n/a` cells** (re-review r7-N2). If `σ = b` has probability 0 at some phase, the conditional `s` at that phase
    is recorded as JSON `null`. A conditional `V` with a `null` factor is `null`. The note prints "undefined: the value
    has probability 0".

**Validation-layer quantities.**
- **`D(arm)`.** Total variation over the joint law of all held, unregistered cells, given `Z+` against `Z−`, maximized
  over `φ`. `D_phase` is reported separately.
- **`K(arm)`, a kernel** (re-review R7-B4). The transition kernel of the encoded `x` across `t = 2`: the law of
  `x_after` given `x_before`, computed from `X+` and `X−` at both phases.
  - Values in construction B: identity for off and SH-0; the uniformizing kernel for on and SH-K.
  - A reset, which writes a known value into `x` (PL-SPI), gives the constant kernel and is distinguished from both.
- **NONABS(arm) and SPI(arm).** SPI is non-discriminating in construction B (`x` is uniform under `Z±`); PL-SPI gives
  it teeth.
- **`CPL(arm) = V² + D²`.** An imported comparator (Englert's bound applied to a classical total variation), reported
  per arm. No token reads it.

**Decision rule P** (`controls.py decide-p`; first match; §A.29-clean: no owner choice among D14's options changes which
token the measurements produce):
1. **P-VOID**: any P control red; any field missing; NONABS or SPI false for any arm in `Adm_B`.
2. **P-NO-FRINGES**: `V(off) = 0`.
3. **P-NO-RECORD**: `D(on) = 0`.
4. **P-RECORD-WITHOUT-SUPPRESSION**: some `a ∈ Adm_B` has `D(a) > 0` and `V(a) ≥ V(off)`. Every such arm is listed.
5. **P-COMPLEMENTARITY**: otherwise. The off arm shows two-setting interference; the on arm records the path and
   suppresses; and every arm of `Adm_B` that records the path also suppresses.

`Adm_B` contains only single fresh cells. The general statement for every SA-1 protocol (`D = 1 ⇒ V = 0`) is AP1 Lemma 3
[W], cited as the paper extension, labelled, not tested here (re-review r7-N6).

**The attribution field `ATTR`** (owner condition on D14(d); frozen; validation layer; printed beside the P token and
never folded into it). Computed mechanically:
- **"attributable to which-path recording"** iff all of the following hold:
  - `D(on) > 0` and `V(on) < V(off)`: the marker records and suppresses;
  - `D(SH-K) = 0` and `K(SH-K) = K(on)`: the kick-matched sham is valid;
  - `V(SH-K) = V(off)`: the sham retains the interference.
- **"not attributable"** iff the marker records and suppresses, the kick-matched sham is valid, and `V(SH-K) < V(off)`
  (the sham also suppresses).
- **"undefined"** otherwise (the marker does not record and suppress, or the sham is not valid), with the failing
  condition named.

The P token reads only the off/on interference contrast and the class-level predicate. It has no sham-specific gate:
SH-0 and SH-K enter it only as members of `Adm_B`, through the class predicate and step 1's NONABS and SPI (r10-N1).
`ATTR` never changes it. When `ATTR` reads "not attributable", no text reports a transition attributable to which-path
recording.

**Disclosed in advance, as a known structural fact, not a result** (re-review R7-B1). In every model where the screen
statistics are a function of the arm's system-level channel, `K(SH-K) = K(on)` implies `V(SH-K) = V(on)`. So `ATTR`
reads "not attributable" whenever the marker suppresses. This holds in QM, in classical waves and in construction B. The
value "attributable" is reachable only in a model in which the screen statistics depend on more than that channel. The
self-test fixture ATTR-FIX feeds synthetic field records to the function to show that it can return each of the three
values.

**Reported, gating nothing** (`decompose-p`).
- **The decomposition by the shams.** SH-0 has the coupling and no kick: `V(SH-0)` and `K(SH-0)`. SH-K has the kick and
  no path-correlated record under N2: `V(SH-K)`, `K(SH-K)`, `D(SH-K)`. The validity flags are `D(SH-0) = 0`,
  `D(SH-K) = 0` and `K(SH-K) = K(on)`. A failed flag is printed; it does not change the token.
- **The dephasing look-alike.** `V(SH-K) = V(on)` is reported.
- **`CPL` per arm.**
- **The eraser fields.**

**A/B report** (`ab-p`; not read by `decide-p`). For `X ∈ {A_P, B}`:
- **Existence:** `∃ a ∈ Adm_X` with `D(a) > 0 ∧ V(a) < V(off)`, given `V(off) > 0`.
- **Universality:** `V(off) > 0 ∧ ∃ a ∈ Adm_X` with `D(a) > 0`, `∧ ∀ a ∈ Adm_X: D(a) > 0 ⇒ V(a) < V(off)`.

For each reading the owner's case is reported: both succeed; A fails and B succeeds; or B fails. The arms that record
without suppressing are listed.

Paper expectation, disclosed: existence, both succeed (the same `(w, 0)` marker is in both classes). By the owner's case
logic, observational incompleteness is then not necessary for the transition's existence. Universality: A fails (the
four sharp supplies) and B succeeds, carried by SA-1(c).

**Per-principle ablations of construction B** (`ablate-p`). Each fixture is frozen exactly. Each reports the
observer-layer quantities, `D`, `K`, `pred_change`, the computed `mech_change`, `dynamics_credit`, and one of two
outcome fields:
- **Class ablations** (ABL-SA1c, ABL-RECIP, ABL-ENV-u, ABL-ENV-v): the token `decide-p` gives with `Adm_B` replaced by
  the ablation's class.
- **Read-set ablations** (ABL-SA1b; re-review R8-B2): the token is printed as "not applicable (access ablation)". In its
  place is the **observer-level complementarity field `OLC`**. For each joint-read subset (each value of the jointly
  registered held slots), `OLC` gives:
  - the conditional `V`;
  - the conditional path predictability `Pz = |2·P(z = 0 | subset) − 1|` under `X+`;
  - `OLC.joint := ∃ subset with Pz = 1 and conditional V = 1`, that is, joint path and phase knowledge at the observer
    level.

  Writer's probe `probes-r9/olc.py`: for ABL-SA1b, all four subsets have `(V, Pz) = (1, 1)`, so `OLC.joint` is true.

| id | removes | fixture (frozen) | kind / credit |
| --- | --- | --- | --- |
| ABL-SA1c | SA-1(c) | `Adm` = `Adm_A` (the whole alphabet `Σ`, reciprocal) | state restriction / none |
| ABL-SA1b | SA-1(b), one functional per cell | arm on. After `t = 3` the observer registers **both** slots of the held arm cell and the screen. Reported: `OLC` (the conditional `V` and `Pz` per joint subset, and `OLC.joint`); the token is "not applicable (access ablation)" | access restriction / none |
| ABL-RECIP | reciprocity of the coupling | `Adm_B`, plus each of its cells under a copy-only coupling at `t = 2` (the arm cell's `u` receives `z`; the carrier takes a free tick) | dynamics / a different mechanism |
| ABL-ENV-u | N2 on the environment cell's `u` slot | SH-K's cell with `u` known `= 0`: `(0, w′)` | state restriction / none |
| ABL-ENV-v | N2 on the environment cell's `v` slot | SH-K's cell with `v` known `= 0`: `(w, 0)` | state restriction / none |
| ABL-P3 | P3 arming (FIX) | not posable in this round: without arming no off arm exists (NR-16) | dynamics / — |

L-ACC's ablation is the eraser fields and B-P themselves; there is no separate fixture.

**Readings of the ablation fixtures (frozen; r13 item 13).**
- **ABL-RECIP's class** is `Adm_B` together with a copy-only variant of each of its five coupled cells (the off arm
  has no coupling to vary): eleven arms. A copy-only coupling at `t = 2` sends the arm cell `(u_a, v_a)` to
  `(u_c + v_a, u_a)` and gives the carrier a free tick, `(u_c, v_c) ↦ (v_c, u_c)`.
- **ABL-ENV-u's and ABL-ENV-v's classes** are `Adm_B` with the hidden-sector cell replaced by the stated cell. Since
  `(0, w′)` and `(w, 0)` are already in `Adm_B`, each class equals, as a set, `Adm_B` without the hidden-sector cell.
  The two ablations differ in the cell that takes SH-K's role in `decompose-p` and in the per-arm report: `(0, w′)`
  for ABL-ENV-u, `(w, 0)` for ABL-ENV-v.
- **`pred_change` for the read-set ablation ABL-SA1b** is the pair `{common, added}` (D23 (c)). `common` is true iff
  some observer-layer quantity defined under both read sets changes for some admissible arm (paper expectation:
  false). `added` lists the quantities defined only under the ablation's read set: `OLC`'s conditional `V` and `Pz`
  per joint subset, and `OLC.joint`. For a class ablation, `pred_change` is one boolean.

**Frozen P texts** (`note`; only measured values interpolated). **The freeze disclosure** (re-review r8-N2) is printed
verbatim as the first sentence of every P text below and in the first paragraph of `result.md`:

- "P's construction-B token, P-COMPLEMENTARITY, was derived on paper before the freeze (AP1 §4.5 with SA-1(c); AP1 Lemma
  3) and evaluated before the freeze by the writer's probe (`probes-r8/p_native.py`, `72c4db13…`) and the reviewer's
  probes (`review/probes-r6/p_arms_indep.py`, `1e351a74…`; `review/probes-r8/adm_closure.py`, `479a10c2…`). The CI
  evaluation reproduces that derivation under frozen controls. It is a consistency check (§A.23), not a novel
  confrontation, and under item L(i) Level 1's condition was known before the freeze."

- **P-COMPLEMENTARITY.** "In construction B of P (the OI substratum plus the observational-incompleteness principles
  named in the ledger, each identified and tested separately), with two phase settings, a known bit `φ ∈ {0, 1}` added
  to the read functional, the screen port follows `x + φ` with the marker off (`V = {V_off}`); with single-path sources
  it is uniform.
  With the marker on, the held, unread marker carries a validated path record (`D = {D_on}`) and `V = {V_on}`. Over the
  admissible arm class of construction B ({list}), every arm that records the path also disturbs the phase (kernel
  {K}) and suppresses the fringes: complementarity holds over that class.
  Each suppression is equally explained by the accompanying disturbance. The disturbance alone, with no path-correlated
  record, gives `V = {V_SHK}`; the coupling alone, with no disturbance, gives `V = {V_SH0}`. What the construction adds
  is that, in its admissible class, no record exists without that disturbance. This rests on SA-1(c), a posited
  principle.
  Whether an arm leaves a path-correlated record is relative to access: the dephasing arm's `D = 0` holds because its
  second slot is unknown under N2.
  Erasure: sorting by the marker's conjugate slot gives conditional `V = {…}`; sorting the dephasing arm by its noise
  value gives conditional `V = {…}`; unsorted, `V = {…}`.
  The table has noncontextual classical models, among them a classical wave with a polarization-type marker and
  construction B itself. This result excludes no classical explanation.
  A/B: existence, {case}; universality, {case}. Attribution (`ATTR`, a separate validated field, not part of the
  token): {ATTR}. In this model, as in QM and classical waves, the kick-matched sham suppresses in every case in
  which the marker does, so the suppression is not attributable to which-path recording. This was disclosed before the freeze. Level 1,
  where awarded, records that the run reproduces a known paper construction; it is not a new derivation or an
  independently generated mechanism."
- **P-RECORD-WITHOUT-SUPPRESSION.** "In construction B of P, the admissible arms {list} record the path (`D = {…}`) and
  leave the fringes (`V = {…}`). Complementarity fails over this class." Then the A/B sentence.
- **P-NO-FRINGES** and **P-NO-RECORD**: one sentence each, stating the failed condition with its measured values, and
  "No complementarity relation is reported in this model."
- **P-VOID**: "A required P control or validation check failed: {codes}. No reading is made."

## Test B: the fragment-relative classical-model test

**Fragments.**
- **B-P.** 32 preparations: sources `{X±, Z±}` × `φ ∈ {0, 1}` × arms {off, on, SH-0, SH-K}.
- **B-C.** For every flagged C instance (D19 (iv)(a); *Obligation C*), reported only (D19 (iii)(c)): the orbit laws
  `O_K(g, π)`, at the
  larger `K` whose conjunction flags the instance, with the measurements `S_Z`, `S_X`, `S_Y`.

**`Acc` as an explicit effect list** (frozen per fragment at `F`; owner-typed by D15; re-review R7-B3).

*`Acc(B-P)`* (D15(a), owner-typed **candidate strengthened** access principle, not established native; c.6735014875). SA-1(b) permits one functional per cell per run, and joint registrations across cells. AP1's type grading
(AP1 §4.2) excludes a `u + v` read, so no Y-type functional of a held cell is registered (re-review r8-N5). Every
measurement registers the screen's `u_s` together with at most one slot of `a` and at most one slot of `p`. That gives
nine measurement settings, written (`a`-slot, `p`-slot) ∈ {none, 0, 1}²:

| setting | screen | `a`-slot | `p`-slot | outcomes |
| --- | --- | --- | --- | --- |
| M00 | `u_s` | none | none | 2 |
| M10, M20 | `u_s` | slot 0 / slot 1 | none | 4 |
| M01, M02 | `u_s` | none | slot 0 / slot 1 | 4 |
| M11, M12, M21, M22 | `u_s` | slot 0 / slot 1 | slot 0 / slot 1 | 8 |

Slot 0 is `u` and slot 1 is `v` of the held cell as it stands at registration, after `t = 3` (r13 item 12). For the
on arm, slot 0 then holds the kick value `w` and slot 1 the path record `z`.

**The LP reads exactly `Acc`.** Its measurement set equals `Acc(fragment)`, checked as `lp_reads_equal_acc`. A
restriction inside `Acc` is not available to the round, so no B-REG-type artefact can arise inside `Acc`.
- D15(b) allows a restricted `Acc`. Then Level 2 additionally requires that the completion "add `Acc`'s remaining
  effects" does not restore a model.

*`Acc(B-C)`.* U′'s three functionals (L-UPRIME): imported, and so not Level-2-eligible unless D15 types it otherwise.

**TOMO's configuration space** (frozen; re-review R7-B3).
- `Ω_c` is the set of joint values of **the slots that `Acc`'s effects read**, restricted to values of positive
  probability under some preparation of the fragment (QC22's charged configurations). For B-P the slots are `u_s` and
  the two slots each of `a` and `p`: five bits. Unread slots are excluded.
- `r_S` is the rank of the preparations' laws on `Ω_c`. `r_E` is the rank of the effects as functions on `Ω_c`. `d` is
  the rank of the table.
- TOMO is green iff `d = r_S = r_E`. TOMO green with B-CONTEXTUAL is impossible (Lemma NC-F), and the checker asserts it.
- **Paper fact under D15(a)** (re-review r8-N6, stated in corrected form):
  - No setting reads both slots of one held cell, so `Acc`'s effects span at most `2 · 3 · 3 = 18` of the `2⁵ = 32`
    functions on the five read slots. `Acc` is therefore not tomographically complete for the read slots.
  - TOMO, as defined (`d = r_S = r_E`), is red whenever the preparations span more than the effects or the pairing is
    degenerate. Whether `r_S > r_E` holds for B-P is not computed before `F`, because it is a B-P quantity.
  - The review's "TOMO is necessarily red" holds when TOMO is read as tomographic completeness relative to `Ω_c` (given
    `|Ω_c| > 18`). Under
    the frozen definition it holds only in the cases just named.
  - In either reading, a B-CONTEXTUAL under D15(a) is relative to SA-1(b)'s one-functional-per-cell restriction, which is
    the principle D15's typing judges.

**Construction A of B** (`Acc_A`: every slot of every cell, carrier included, registered jointly). Its B result is
**reported as measured** (D19 (ii)(b)). It is decided where it is within the general caps and budget (C.8 item 1;
owner-approved R5 default), and is otherwise reported `out_of_scope` or `undecided`; it decides and
voids no token. Lemma NC-F's fast path applies only when `d = r_S = r_E`.
- On the preparation side, B-P's `r_S ≤ 32`, while `Ω_c` under `Acc_A` can have up to `2⁸` points (eight slots), so
  `r_S < r_E` is possible.
- No paper expectation is frozen for it. (r7 stated "imitable by Lemma NC-F"; that claim is withdrawn.)

**Method.** ARP-3-QC22 r13's *The exact method*, steps 1–6, with its independent verifier and caps, copied in
Appendix C.1 under the adaptation table there (D10(a)). The caps count extreme rays, each removal certified
(D19 (0)(c); C.8 item 15). B-P's caps and budget come from the stress test ST-BP; every other fragment takes the
general ones (D19 (i)(a); C.8 items 1 and 2).

**B-P against QM-P** (re-review R8-B1; **fix 2 chosen**, restriction).
- QM-P has a phase gate `Z^φ` and no phase register. So the settings that read the phase cell (M01, M02, M11–M22) have
  no QM counterpart in this round.
- QM-P's fragment, the paper equality and `bp_equals_qmp` are therefore restricted to the `p`-free settings M00, M10
  and M20.
- **The slot-to-basis map** is slot 0 ↔ `X`, slot 1 ↔ `Z`, and **QM-P's arms for the restricted fragment** are
  D22 (a)'s CNOT markers: off, the marker in `|0⟩` uncoupled; on, `|0⟩`; SH-0, `|+⟩`; SH-K, the maximally mixed
  state. Paper expectation: equality column by column for all four arms. `bp_equals_qmp` is reported per arm, a QM
  benchmark that gates nothing (SG-4). Neither token is predicted on paper.
- The full nine-setting B-P fragment has no QM-P counterpart, and no equality is claimed for it.
- Fix 1, a QM phase register mapped to B's phase cell, was not chosen. B's phase cell holds a masked path copy (`z +
  v_p`) and `φ`, and a QM register reproducing both would need a design of its own.

**Decision rule B** (`decide-b`; it reads B-P alone, with the B controls; C.8 item 13):
1. **B-VOID**: any B control red; B-P `undecided` or `out_of_scope`; B-P's record not the frozen fragment (32
   preparations, read by the nine settings of `Acc(B-P)`; SG-1); or `lp_reads_equal_acc` false for B-P.
2. **B-CONTEXTUAL**: B-P infeasible with a verified Farkas certificate. Reported: the `Acc` typing, TOMO, and the
   first restoring completion from the frozen list. The list is: `Acc`'s remaining effects (under D15(b)); then
   every slot of the held cells, **registered jointly (SA-1(b) dropped)**; then every slot of every cell, registered
   jointly (re-review r8-N7). Each completion is reported only, under the general caps and budget (C.8 items 1 and
   13; owner-approved R5 default). One that is `out_of_scope` or `undecided` is printed with that word,
   and the list goes on. The note names the first completion that restores a model with a verified certificate,
   or prints "No completion in the frozen list restored a model within this round's frozen caps and budget: {each
   completion with its result}."
3. **B-CLASSICALLY-IMITABLE**: B-P feasible with a verified model.

Construction A of B, B-P's completions and the B-C fragments are reported (D19 (ii)(b), (iii)(c)). Each B-C
fragment is reported with its own verdict, `Acc` typing, TOMO, completion and UPR-BC label. Under D21 (b), a B-VOID
voids B's token only; P's and C's tokens stand.

**B-VOID text** (frozen; `note`): "A required B control failed, or B-P has no verified verdict within this round's
frozen caps and budget: {codes}. No reading is made." When a code is B-P's `out_of_scope`, the note adds: "B-P
exceeded {the cap or budget}. This is a limitation of this round's frozen resources, not a result about B-P." When
it is B-P's `undecided`, the note adds: "B-P's certificate did not verify. This is a limitation of this round's
method, not a result about B-P." (SG-2)

**B1** (reported, not gated): `α = 0`, fixed by L-PORT.

**Frozen B scope sentence** (printed with B-CONTEXTUAL): "No preparation- and measurement-noncontextual model exists
over this fragment's own operational equivalences, read over the whole access class `{Acc}` ({typing}). Every OI table
is generated by a configuration model, so this is a degenerate pairing on the configurations: it is relative to an
access class whose reads do not span them. It does not exclude classical models in which those equivalences fail
ontically: classical registers with unread parities, classical fields with intensity-normalized single-event
detection, or OI's own configuration model."

## Obligation C: the non-Clifford operation through detector records

**Setup.** r5's *The model* (Appendix A) for the ring `Z_3` with U′ on cells 0–1, the rules `Φ_g` and the 150 rounds.
The source `Q` is the QA family (7 laws). Orbits are `O_K(g, π)` for `K ∈ {6, 12}`, with a fresh mediator per
application.
- C is not P's apparatus. It has no screen, phase cell or marker.
- The detectors `S_Z`, `S_X` and `S_Y` (native `XOR`, P3 arming, every arm and ablation; L-HET) realize U′'s
  functionals (L-UPRIME, used).
- The source, the orbit, the detectors, the record vector and the frame calibration L-CAL are in Appendix D.3.

**Quantities.** `HC(K)`, `CONS(K)`, `VAL(K)`, `W-OCT(K)`, ABL and EMB are defined in Appendix D.4. The changes:
- **`STAB(K)`** (reported; non-gating; frozen; cone review §6): `STAB(K) = [rank span O_{K−1} = rank span O_K]`,
  computed exactly from the orbit laws at each composition horizon `K ∈ {6, 12}`, for every instance where W-CL is
  reported. No token and no Level reads it. With every W-CL report the note prints `STAB(K)`, and it prints the bound
  "orders 3 or 6" only when `STAB(K)` is true.
- **W-CL** is computed on both `β` and `P^k β`, with `k` the round's tick count and `P` the transposition `x ↔ z`. It
  fires if either does, and both spectra and both determinants are reported. It is invariant under linear
  recalibration.
- **ABL** is labelled a dynamics ablation: affine `g`, and the zero-tick round.
- **C-A** (`reg = none`): for each flagged `(g, m, k)`, the same `m` and `k` with `reg = none`. The orbit, CONS, W-CL
  and W-OCT are reported, not gated. The C text states whether conditioning is part of the origin.
- **EMB**: NE-1, NE-2, NE-4 and NE-5.

**Decision rule C** (`decide-c`; first match, over test rules and rounds):
1. **C-VOID**: any C control red, or the enumeration incomplete, or flags disagree.
2. **C-EXPOSURE**: `HC(12) ∧ CONS(12) ∧ VAL(12) ∧ W-CL ∧ ABL ∧ EMB`.
3. **C-SIZE-DEPENDENT**: the same at `K = 6` and not at `K = 12`.
4. **C-NONSTABILIZER**: `HC(12) ∧ VAL(12) ∧ W-OCT(12) ∧ ABL ∧ EMB`.
5. **C-SURVIVAL**: otherwise.

**Flagged instances** (D19 (iv)(a)). An instance is flagged iff the conjunction of `decide-c`'s step 2, 3 or 4 holds.
B-C, reported only (D19 (iii)(c)), and C-A are built for flagged instances only; with none flagged, neither is built.

**Frozen C texts.** Appendix D.5 states them with these changes applied:
- "acts on the detector records" is followed by "(U′'s three functionals, read by native meters)".
- "The identical gadget with the rule made affine, or idle (a change of dynamics), shows no such operation. With
  `reg = none` on the same `(g, m, k)` the witness {is/is not} present; record-dependent conditioning {is/is not} part
  of the origin."
- The C-SURVIVAL text keeps "scoped finite search" and the witness principle verbatim.

**Common clause.** Appendix D.5 states it, with "construction B (the OI substratum plus the observational-incompleteness principles
named in the ledger, each identified and tested separately)" in place of each "native", and with "the imported
identifications of path, port and U′" added.

## Levels (mechanical; `decide-levels`)

- **Level 1** iff P-COMPLEMENTARITY (owner decision L(i): "Level 1 must require the detector-dependent interference
  transition, not fringes alone").
  - **Presentation** (frozen; owner, c.6735014875). Every note that prints Level 1 prints with it: "Level 1 here records
    that the run reproduces a known paper construction (AP1 §4.5 with SA-1(c); AP1 Lemma 3) under frozen controls. It is
    a consistency check, not a new derivation and not an independently generated mechanism."
  - `ATTR` is printed beside it. Level 1 does not depend on `ATTR`.
- **Level 2** iff all of the following hold:
  - Level 1;
  - B-CONTEXTUAL on B-P (D17(a): B-C does not count);
  - B-P's LP read exactly `Acc(B-P)`;
  - that `Acc` is owner-typed. It is typed **candidate strengthened** (D15(a)), so it is eligible, and every Level-2
    print names that typing.
- **Level 3** iff Level 2 and C-EXPOSURE. The note prints with Level 3: "Level 3 here joins B-P (P's two-path
  apparatus) with C-EXPOSURE (the U′ gadget), two unrelated instances" (D17(a)).
- **Level 4**: not tested.
- **VOID tokens** (D21 (b)). A VOID token fails only the Levels whose conditions read it. A C-VOID leaves Levels 1
  and 2 to be decided; a B-VOID leaves Level 1.
- **The representation rule.** If REP-INV reclassifies an identification as imported, every token that depends on it is
  a benchmark result. No Level is awarded from it: Levels 1 and 2 depend on L-PATH and L-PORT; Level 3 on L-CAL and
  L-UPRIME.

The level reported is the largest `n` whose own conditions and all lower ones hold, or "none". The owner's sentence is
printed: "… reaching Level 2 does not automatically establish Level 3, and even Level 3 does not establish full
equivalence."

**D14 disclosure** (kept from the decision sheet). Under the options not chosen, (a) and (c), which conflict with
§A.29, the gate would have fired whenever the marker suppresses, and with L(i) no Level could have been awarded. (b)
would never have fired. Under the chosen (d) the token is independent of the shams, and `ATTR` carries the attribution
separately.

## Proof reviews (owner, c.6735014875: independent review of Lemma P and the cone argument)

**Verdicts, quoted.**
- **Lemma P.** `review/proofs/REVIEW-LEMMA-P.md`, sha256
  `071704539148974eba77bc44ab6960d2809b7ec119e5686fe2f017d9e9dd740c`, verbatim: "**Verdict: PROVED.** The statement is
  true as stated." "The design's reliance on Lemma P survives. It remains conditional on Theorem C(ii), as the design
  already labels it, and on the link hypotheses L1–L3 in §4."
  - The link hypotheses are: records factor through `R` (L-UPRIME); `R(Q) = V₀`, which needs `Λ_{y,b}` (H-PREP, NNB);
    and CONS on all seven QA laws at the first step.
  - Wording fix LP-1 is applied in `DESIGN-DS.md` §6: the self-map property follows from `conv R(Q) = O` together with
    `R(πQ) ⊆ O`. "`O = conv R(L)`" is neither needed nor sufficient.
- **The cone argument.** `review/proofs/REVIEW-CONE.md`, sha256
  `07bc8fd75a3825e3604d3c032e68226c4f0f5cb071c756008443bef55decf267`, verbatim: "**Verdict: PROVED UNDER STATED EXTRA
  HYPOTHESES.** The conclusion holds once the window is required to be invariant". "The missing hypothesis is STAB:
  `span O_K = span O_{K−1}`, the orbit span is invariant within the window." "As the design uses the argument, with no
  STAB, it is a GAP."
  - Exact counterexamples exist in the abstract class of nonnegative branch matrices: at `K = 1` and `K = 2` with VAL,
    and at `K = 3` without VAL. Each has a `β` with an eigenvalue pair at angle `arccos(3/5)`.
  - "Not established: whether the gadget's own rounds at `K = 6` or `K = 12` can exploit the gap."

**What is withheld, and what is conditional** (the frozen table, now with its verdicts):

| sketch | verdict | withheld | conditional on `STAB(K)` per instance | unaffected |
| --- | --- | --- | --- | --- |
| **Lemma P** | PROVED (conditional on Theorem C(ii) and L1–L3) | nothing | — | CC-NAT keeps its paper expectation, labelled conditional on Theorem C(ii) and L1–L3, and its gating role |
| **the cone argument** | PROVED UNDER STATED EXTRA HYPOTHESES (STAB) | nothing else | "C's positives can only show orders 3 or 6" (hazard 7); "C cannot instantiate ENC-G"; remark R1's finite-order scope sentence (`DESIGN-DS.md` §6) | every C token; W-CL's computation; C-35; the arithmetic statement that every probability is rational and that nothing bears on irrational or approximate gates |

**Withdrawn.** r6's sentence "a rotation by `arccos(3/5)` is excluded on paper for this protocol class", which r7–r9
carried by reference, is withdrawn: the cone review refutes it in the abstract class. Whether gadget rounds at
`K = 6, 12` reach such a pair is open, and W-CL reports it if they do.

## The controls (frozen; each control's expectation is fixed before any decisive computation; its mode is in *Control modes*)

| code | for | fixture | green when | route to failure |
| --- | --- | --- | --- | --- |
| **CW-P** | P, B | classical two-beam field, exact. Admissible arms: off, polarization marker, the same rotation on both arms (SH-0 analogue), a recorded random `0/π` phase on one arm (SH-K analogue); diagonal-analyser eraser; two square-law detectors | `decide-p` returns P-COMPLEMENTARITY; `ATTR` reads "not attributable"; the decomposition and eraser references are reproduced; `α ≥ 1` | a P rule that credits classical waves beyond Level 1; a missing classical eraser |
| **QM-P** | P, B | stabilizer QM. Admissible arms: off, CNOT marker, `X` on the environment, recorded classical-noise `Z^w`, purified dephasing (environment `|+⟩`, CZ); for its restricted fragment, D22 (a)'s CNOT markers (off uncoupled; on `|0⟩`; SH-0 `|+⟩`; SH-K maximally mixed), under slot 0 ↔ `X`, slot 1 ↔ `Z`. `D` is the trace distance between the held registers' states given `Z+` and `Z−`, the counterpart of the total variation (r13 item 13) | P-COMPLEMENTARITY; `ATTR` reads "not attributable"; the purified-dephasing arm has `D = 1` and the classical-noise arm `D = 0` (access-relativity of `D`); its fragment on the `p`-free settings M00, M10, M20 decided with a verified certificate (R8-B1) | a P rule that treats QM differently from the classical wave; `D` taken as access-independent |
| **PL-CONFOUND** | P | in the on slot, a sharp `(0, 0)` cell (P2 departure) together with a hidden-sector cell | P-COMPLEMENTARITY; the note's decomposition reports the on arm's kernel as uniformizing and does not attribute the suppression to the record | a text that attributes a suppression to recording |
| **PL-NOREC** | P | the hidden-sector cell in the on slot | P-NO-RECORD | activation counted as recording |
| **PL-SHARP** | P | `Adm_B` plus the sharp `(0, 0)` cell (P2 departure) | P-RECORD-WITHOUT-SUPPRESSION, listing `(0, 0)`; `CPL = 2` reported | a record without suppression missed |
| **PL-ABSORB** | P | a blocking marker (runs with `z = 1` discarded) | NONABS red, so P-VOID | blocking counted as marking |
| **PL-SPI** | P | an exchange of the carrier's `x` with the known `u` slot of a sharp `(0, 0)` cell (a P2 departure; re-review r7-N4) at `t = 2` | SPI red, so P-VOID; its kernel `K` is the constant (reset) kernel, distinct from the identity and from the uniformizing kernel | SPI unable to fail; `K` blind to non-additive disturbance |
| **PL-NOFR** | P | the uniform source | P-NO-FRINGES | fringes without a known phase |
| **AB-P-FIX** | P | `ab-p` on `Adm_A` and `Adm_B` | existence: both succeed; universality: `A_P` fails (four sharp supplies listed), B succeeds | an A/B predicate that cannot fail, or one that reports only one reading |
| **MECH-FIX** | P | `mech_change` on ABL-SA1c and ABL-RECIP | ABL-SA1c adds the sharp mechanisms to two `(V = 1, D = 1)` cells; ABL-RECIP adds the copy-only mechanisms | `mech_change` that is a label, not a computation |
| **ATTR-FIX** | P | synthetic field records fed to the `ATTR` function: (i) the marker records and suppresses, the sham is valid and retains; (ii) the same with the sham suppressing; (iii) the sham invalid. Mutation: flipping the sham-specific fields in a synthetic `decide-p` record (r10-N1) | (i) "attributable to which-path recording"; (ii) "not attributable"; (iii) "undefined", with the failing condition named; under the mutation, the token is unchanged | an attribution function that cannot return a value, or that the token reads |
| **REP-PLANT** | P, all | an inadmissible "port" map that XORs the screen bit with the held marker's kick slot, an identification that inserts conditioning, run through REP-INV against the drafted L-PORT | REP-INV reports a change (`V(on)` changes); `decide-levels` reclassifies the planted identification as imported and withholds Levels 1–2 for the fixture | a representation check that cannot detect an identification that supplies a resource |
| **ACC-ONLY-FIX** | P | `access_only` on ABL-SA1b and on ABL-SA1c | ABL-SA1b: true; ABL-SA1c: false | an access-only field that is a label, not a computation |
| **B-POS** | B | rebit `±(3/5, 4/5)`, `±(3/5, −4/5)` with `Z`, `X` | infeasible, certificate verified | a test that cannot fire |
| **B-STAB**, **B-CLASS** | B | `Z±`, `X±` with `Z`, `X`; a two-bit classical register with spanning reads | feasible, model verified | a test that fires on stabilizer or classical spanning tables |
| **B-S4F** (step 4 feasible with `T > 0`; r13 item 15) | B | `Ω = F_2²`, the four point laws; effects: the unit, `ξ_1 = 3/8 + [ω_0 = 0]/4`, `ξ_2 = 3/8 + [ω_1 = 0]/4` and their complements. `d = 3`, `r_S = 4`, `r_E = 3`; `cone{a_p}` is a square cone with `m = 4` facets, so `T = (m − d)·d = 3` | feasible, decided by step 4's feasible branch (steps 2 and 3 inapplicable), model verified. A model exists on paper: three ontic states at `(−1/2, −1/2)`, `(5/2, −1/2)` and `(−1/2, 5/2)` in the affine plane of the point laws' coordinates `(ω_0, ω_1)`, with barycentric laws and affine responses in `[0, 1]` (writer's probe `probes-r13/s4f.py`, `d1e56566…`) | step 4's feasible branch untested at `T > 0` |
| **B-RAY** (D19 (0)(c); C.8 item 15) | B | B-RAY-S: B-STAB's `Z±`, `X±` with the mixture `½Z+ + ½Z−` added, read by `Z` and `X`. B-RAY-P: B-POS's four rebit preparations with the mixture of its first two added. B-RAY-F: B-S4F's four point laws with the mixture of its first two added, read by B-S4F's effects | in each, 5 distinct rows and 4 extreme rays; the mixture removed with a verified certificate; the verdict and deciding step equal to B-STAB's (feasible, step 2), to B-POS's (infeasible, step 4) and to B-S4F's (feasible, step 4, `T = 3`), the last two with facets enumerated over the retained rows; B-RAY-F's model reproduces `N` on all five preparations, the removed one included; under M-RAY, C-CERT fails | a removal taken on trust, or a reduction that changes a decision |
| **B-REG** | B | a two-bit classical register, reads bit 1 and bit 2 only | infeasible; TOMO red; completion "add parity" restores a model; with `Acc` = {bit 1, bit 2, parity} and the LP reading only bits 1 and 2, `lp_reads_equal_acc` is false and B is VOID; `decide-levels` awards no Level 2 under a design-chosen `Acc` | a Level 2 award from tomographic incompleteness, including from a subset of `Acc` |
| **B-WAVE** | B | CW-P's intensity-normalized table at B-POS's settings | infeasible (B's LP does not exclude classical fields); two-detector `α ≥ 1` | B read as excluding classical fields |
| **C-STAB**, **C-R60**, **C-35**, **C-S3**, **C-PLANT**, **C-CONSX**, **C-DET** | C | Appendix D.6 | Appendix D.6 | Appendix D.6 |
| **C-R60-ODD** | C | encoded R60 composed with one free tick. The fixed-slot spectrum `{−1, 1, 1}` is a signed-permutation spectrum; `P β` has `{1, e^{±iπ/3}}` | W-CL fires, through `P^k β` only | a frame blind spot for odd `k` |
| **CC-NAT** | C | the four affine rules, every round, the full orbit | no W-CL with CONS, and no W-OCT. Paper basis: Theorem C(ii) (conditional) and Lemma P (independently reviewed: PROVED, conditional on Theorem C(ii) and L1–L3) | a propagation error; a non-native supply; or a failure of Lemma P, Theorem C(ii) or the link hypotheses L1–L3 (records factor through `R`; `R(Q) = V₀`, with `Λ_{y,b}`; CONS on all seven QA laws at the first step) (r12-N2). Lemma P has passed its review, so CC-NAT keeps its gating role (*Proof reviews*). The gating path (r13 item 16): CC-NAT is a C control computed in decisive mode; red, it makes `decide-c` give C-VOID, and only C's token is VOID (D21 (b)); P's and B's tokens stand |
| **CC-DYAD**, **C-AFFB**, **C-XB**, **C-STEP**, **C-FRAME**, **C-SCOPE** | C | Appendix B, adapted to orbits as Appendix D.6 states (C-AFFB on the diagnostics only, under D1(a), at depth 1; D20 (b)) | Appendix B, as adapted | Appendix B |
| **C-EMB** | C | NE-1, NE-2, NE-4, NE-5; NE-3 through ABL (Appendix D.6) | all hold | Appendix D.6's C-EMB row |
| **C-IFACE** | all | static check with the certificate exemption, and the mutation; plus the rule that `decide-p` references neither `ATTR` nor the SH-0 and SH-K fields, except through the `Adm_B` loop (r10-N1); the rule that `decide-c` and `decide-levels` do not reference `STAB` (r12-N3); and the rules that `decide-b` reads only B-P's record and the B controls, and that no `decide-*`, `decide-levels` or ADA status function references `bp_equals_qmp`; the ADA status rules are computed only in functions named `ada_*` (SG-1, SG-4) | holds; each mutation turns the self-test red: the base mutation, one making `decide-b` read construction A of B, one making `decide-levels` read `bp_equals_qmp`, and one making an `ada_*` function read `bp_equals_qmp` | a direct read entering a token; a sham-specific gate; a reported-only fragment or a QM comparison entering a token |
| **STAB-FALSE** | C | the cone review's exact certificates, committed in `<record dir>/evidence/` in every tree from the design run onward, pinned by sha256, and read by `controls.py --self-test` (A9), which checks each file against its pin before use (C.8 item 12): `cone_k1_certificate.json` (`e67199472530e6753eed86e991636a4fadb930b2b9c56e0456ec6b884cfeb644`, `K = 1`) and `cone_window_K2_certificate.json` (`f24a68d902a423018d15c4d92440970e5f17b202cc8b8ea3407ad11269e6ebaf`, `K = 2`). **Orbit reconstruction** (outside `DECISIVE_BUILDERS`; supplied data only). `O_0` is the seven QA law vectors on U′'s 16 configurations (`Λ_0` uniform; `Λ_{a,b}` uniform on `{f_a = b}`). Then `O_{j+1} = {Bμ / 1ᵀBμ : μ ∈ O_j}`, and the herald is `1ᵀBμ`. For the `K = 1` certificate (fields `q`, `P`, `G`, `beta`), the branch matrix is rebuilt column by column: `B δ_x = w(x) ℓ_x`, with `v(x) = ((−1)^{f_x}, (−1)^{f_y}, (−1)^{f_z})(x)`, `w(x) = 8 q P(v(x))`, and `ℓ_x` the law with `χ_x`, `χ_y`, `χ_z` independent with biases `G(v)/P(v)` and the remaining configuration bit uniform (the column is zero where `P(v) = 0`). The fitted `β` is recomputed from `O_1`, and must equal the certificate's `beta`. For the `K = 2` certificate (fields `K`, `q`, `B`), the branch matrix is the field `B` (a 16×16 rational matrix). A9 re-verifies, from these data alone: `B ≥ 0`; column sums at most 1; HC(K); CONS(K); VAL(K); the factor `λ² − (6/5)λ + 1`; and `STAB(K)` | `STAB = false` in both. HC, CONS and VAL hold, and W-CL fires on the irrational pair (`λ² − (6/5)λ + 1`). The note does not print the "orders 3 or 6" bound | a STAB field that cannot be false, or a bound printed without STAB |
| **STAB-TRUE** | C | the **supplied identity map** on the seven QA law vectors (`O_1 = O_0`), computed outside `DECISIVE_BUILDERS` (r12-N1); it is not ABL's zero-tick ablation, which is a decisive family | `STAB = true` | a STAB field that cannot be true |
| **REP-FRAME** | C | C-R60-ODD's supplied map under all 48 signed-permutation recalibrations, with the transposition transported (`S P S⁻¹`) | W-CL fires in all 48 | a REP-INV that reclassifies a genuine witness through an untransported frame |
| **UPR-BC** | C | `decide-levels` on synthetic B-C records: contextual, with completion restoring a model; contextual, with completion not restoring it; contextual, with that completion `out_of_scope` | the first prints "imported for B-C" (benchmark); the second and third do not, and the third prints the completion's status (owner-approved R9 default) | an identification-supplied contextuality printed unlabelled |

For these fixed B fixtures and the QM-P restricted fragment, the effect-side C-SYM enumeration bound
is below `10^5` with the two-bit B-CLASS/B-REG registers declared above (r14c-N5): B-CLASS's bound is 286;
the conservative QM-P product-embedding bound is 50,388. C.1 already bounds this enumeration by
`C(effects cap, d cap − 1)`. This is a paper bound, not a report of an executed fixture or cap stress test.

**Decisive builders and the guard** (re-review R10-B2). Every decisive family is built only through the single gated
entry `s_decisive` in `qc21_check.py`. The families are:
- P's arm classes `Adm_A` and `Adm_B`, and the ablations;
- REP-INV on decisive data;
- B-P, construction A of B, and B-C;
- C's test-rule orbits, the affine and idle ablations (ABL), and the C-A runs.

The guard:
- **The refusal.** `s_decisive` carries QC22's refusal check as its first statement (Appendix C.5, read with the
  adaptation table). So does every registered builder, through the shared refusal `s_refusal()` (C.8 item 5). The frozen list
  `DECISIVE_BUILDERS` has four names, one per family above: `s_build_p`, `s_build_repinv`, `s_build_b` and `s_build_c`
  (C.8 item 6).
- **The name rules (control B).**
  - `s_decisive` is referenced only in the entry function `s_entry` and in `t_builder_refuses`.
  - Each registered builder's name is referenced only in its own `def`, in `DECISIVE_BUILDERS`, and inside
    `s_decisive`.
- **The counter.** The instrumented counter of M-GUARD counts calls to every registered builder. In every fixture-mode
  M-GUARD case it must read zero for each.

**Control modes (frozen; re-review R10-B2).** Every control runs either in **fixture** mode (job A, every event) or in
**decisive** mode only (job B, on the owner-approved dispatch). A fixture-mode control evaluates only one of the
following:
- supplied matrices or laws;
- synthetic fragments;
- the native-rule detector map on supplied laws;
- static code.

None of these is a decisive family, so a fixture-mode control exposes nothing decisive. Decisive-mode controls are
computed from the same builders as the tokens.

| mode | controls | why |
| --- | --- | --- |
| **fixture** (job A, every event) | B-POS, B-STAB, B-CLASS, B-REG, B-WAVE, B-S4F, B-RAY, QM-P, CW-P, ATTR-FIX, C-STAB, C-R60, C-R60-ODD, STAB-FALSE (in `controls.py`, A9), STAB-TRUE, REP-FRAME, UPR-BC (synthetic `decide-levels` records; r11-N1), C-35, C-S3, C-PLANT, C-CONSX, C-DET, C-STEP, C-IFACE, ZPT, F10, C-CERT and C-NCF and C-SYM on these fixtures, C-INDEP, C-EXACT, and every self-test and mutation | supplied QM or classical matrices and laws, synthetic classical fragments, synthetic field records, supplied rotations, and the native-rule detector and step maps on supplied laws. None builds a decisive family |
| **decisive** (job B, owner-approved dispatch only) | AB-P-FIX, MECH-FIX, ACC-ONLY-FIX, PL-SHARP, PL-CONFOUND, PL-NOREC, PL-ABSORB, PL-SPI, PL-NOFR, REP-PLANT, CC-NAT, CC-DYAD, C-XB, C-AFFB, C-FRAME, C-SCOPE, C-EMB, C-BUDGET, and C-CERT on decisive fragments | each evaluates P's construction-B arm classes or their variants, REP-INV on decisive data, a B fragment built from OI data, or the C orbit builder |

C-STATELESS is not a run-time control: `controls.py check --stage E` evaluates it on committed records. The self-test
drives the decisive-mode controls' `decide` paths with synthetic field records only.

Self-tests drive every `decide-*`, `ab-p`, `ablate-p`, `decompose-p`, `decide-levels` and the note generator through
every token and every VOID path. They include SG-1 to SG-3's cases: a 16-preparation B-P record gives B-VOID; an
`out_of_scope` and an `undecided` B-P each give B-VOID with the limitation sentences; C-VOID and B-VOID each leave
Level 1 with P-COMPLEMENTARITY; `verdict` prints VOID on each provenance failure and incomplete-output halt of D21;
and `ablate-p` gives `common` false and `added` non-empty on a synthetic ABL-SA1b record (D23 (c)).
`ab-p` enumerates all of `Σ`, the two `u + v`-known cells included. A self-test asserts
`|Adm_A| = 12` and `|Adm_B| = 6`, counting the off arm in both (r9-N3). No self-test evaluates P's construction B, a test rule's orbit, or a B fragment built
from them: those are decisive families (*Control modes*).

## What no outcome shows (frozen)

No outcome is a universal statement. None adopts a non-affine rule or a candidate strengthened principle, changes the
status of A5, P1, P2, N2, H-PREP, NNB or any manuscript claim, or establishes a mechanism that reproduces QM.
- **P-COMPLEMENTARITY** is at most Level 1, and P's table has noncontextual classical models, construction B among
  them.
- **No single suppression** is assigned to path recording rather than disturbance, in any theory: dephasing is an
  equally valid explanation of each.
- **Whether an arm leaves a path-correlated record** is relative to access.
- **Complementarity over construction B's class** rests on SA-1(c), which is posited, not derived. Its existence reading
  holds in `A_P` as well.
- **No substratum-only P** is posed.
- **B-CONTEXTUAL** is relative to the fragment's own equivalences and to its `Acc`.
- **C-EXPOSURE** is a finite witness on bounded orbits through U′'s functionals.
- **Every probability is rational.** Nothing bears on irrational or approximate gates.

**S4 phrase screen.** Appendix D.7 states the list. Owner quotations are exempted by exact match.

## Assumption-dependence analysis (ADA)

**Part 1, the ledger.** Appendix D.8's rows, with these changes.
- **P3 arming and E-iso** (L-ARM) are retyped as dynamics (control of couplings), credited with a different mechanism.
- **The shared scaffolding** that `A_P` keeps is listed as untested in this round: P3, E-iso, N2, H-PREP, the
  terminal screen, L-PATH and L-PORT.
- **`D`'s access-relativity** is recorded under L-N2: the dephasing arm's `D = 0` holds because its second slot is
  unknown.

**Part 2, the post-result template.** Appendix D.8's, with these changes:
- The status rules read `ab-p`'s two readings and `ablate-p`'s three fields: `pred_change`, `mech_change` and
  `access_only`. `dynamics_credit` is printed beside them.
- The representation ledger's REP-INV outcome is printed per identification, with any reclassification.
- **SA-1(c)** is **carrying the universality reading in this model** when the universality reading is "A fails, B
  succeeds" and ABL-SA1c has `pred_change` true. Its `mech_change` is printed. Its `dynamics_credit` is none (a state
  restriction).
- **The existence reading**, when both succeed, is printed with the owner's case sentence: "If both A and B reproduce
  quantum behavior, observational incompleteness may not be necessary for that result."
- **P3** is printed as a dynamics row that could not be ablated in this round (NR-16).
- **SA-1(b)** carries **observer-level complementarity in this model** when ABL-SA1b's `OLC.joint` is true, that is,
  when an observer reading the marker's two slots gains joint path and phase knowledge. Its `dynamics_credit` stays
  none (an access restriction). SA-1(c) carries the class-level, unread form; SA-1(b) carries the form seen by an
  observer who reads the marker (re-review R8-B2).

**Part 3, the renaming check.** Appendix D.8's, plus:
- an attribution made by choosing a sham (the shams gate nothing);
- a "no record" that holds only relative to access (`D`'s access-relativity, QM-P's purified arm);
- a restriction credited with no dynamics while it changes the step (P3 retyped).

**Candidate new rounds** (named, not run): NR-1 to NR-16, listed in Appendix D.8.

## Runtime (bounded, outcome-independent)

- **P**: `Adm_B` (6 arms), `Adm_A` (12 arms) and 5 posable ablations, × 4 sources × 2 phases, over at most 2¹⁰
  configurations.
- **B**: one B-P fragment (32 preparations; `d ≤ 18`) under its caps and budget from ST-BP; construction A of B,
  B-P's completions, and the B-C fragments of every flagged instance (at most 600) with their completion, reported
  only, under the general caps and budget (D19; C.8 items 1 and 2; owner-approved R5 default).
- **C**: ≈ 1.0 × 10⁵ propagations for the orbits; `reg = none` re-runs only for flagged instances. The diagnostics
  add 27,600 propagations (depth 1; D20 (b)).

Job B's time for P, REP-INV, C and the diagnostics has no term in the timeout test (C.8 item 2). Measuring it
before `F` would build decisive families, so it is bounded only by the counts above. A job-B timeout is an
incomplete-output halt, which voids every result, P's included (D21).

## The workflow edit, runs, approvals and evidence

ARP-3-QC22 r13's design, copied in Appendix C.2–C.6 with the D12 edit log and the adaptation table (D10(a);
c.6735159962):
- two jobs. Job B runs only on a first-attempt dispatch with the decisive input. **There is no Environment.**
- the decisive steps compute only on the round branch (the ref key), at the input commit, before the receipt;
- nothing is computed on `pull_request` or `push` runs;
- an enumeration of checker-bearing runs over every event, with VOID on any unapproved one;
- the activity check for ref moves;
- approval entries keyed on `(run_id, run_attempt)`, bound to the owner's quoted commit, with the edited-comment rule
  and the owner's ratification: of every entry in `approvals.json` at the designation of `E`, and of the `E`
  dispatch's own entry in the designation of `E` (approved R8 alternative);
- no re-run attestation;
- no deletion of runs, logs or artifacts until `Q` (owner commitment);
- verdicts read only structured data (§A.44).

The workflow anchors at `D`, the design and confirmation runs, the gate-test records and `T0` are filled at the design
run (PENDING).

## Scope of authorization and detection (owner, c.6735159962; re-review R10-B5)

**The decision.** The Environment gate is waived for Q-C2-1, and the existing V3 governance is retained. Owner approval
of each scientific dispatch stays. The workflow controls that tell authorized runs from ordinary CI, and that detect
unexpected executions, are kept. **Unauthorized computation is detected and rejected, not prevented.** For runs of the
frozen splice and the pinned checker, the in-tree keys still prevent decisive computation outside a first-attempt
dispatch with the decisive input, on the round branch, at the input commit, before the receipt (Appendix C.2). Whether
such a dispatch was authorized is detected.

**The owner's acceptance conditions, and how they are met.**
1. **Complete detection within the stated audit scope, re-runs and post-landing runs included.**
   - **Re-runs.** Every attempt is read, and job B is skipped at attempt 2 or later.
   - **Post-landing runs.** The ref key (decisive mode only on the round branch, whose head carries the receipt after
     `Q`) prevents them for the frozen splice, except through three routes that this round does not observe after the
     final capture:
     - (a) a fast-forward push to the round branch of a commit that deletes the receipt;
     - (b) a deletion of the round branch and its re-creation at a pre-`Q` commit;
     - (c) a force-move of the round branch to a pre-`Q` commit.

     Within the window, (b) and (c) are read from the activity API in every capture. A push such as (a) is enumerated
     through the runs it triggers.
   - Both hold within the limits below.
2. **Fail-closed on missing, incomplete or ambiguous evidence.** These count as failures, never as a pass:
   - a failed, rate-limited or truncated capture;
   - an unreadable tree;
   - a `total_count` mismatch;
   - an approval comment edited after its run;
   - an approval entry the owner has not ratified: an entry in `approvals.json` at the designation of `E`, or the `E`
     dispatch's own entry in the designation of `E` (approved R8 alternative, precondition 2).
3. **No residual dependencies.** Appendix C's D12 edit log removes every element E1–E13. No copied control, `verdict`
   condition, gate test, allowlist template or adaptation row refers to an Environment, `approvals` or `deployments`.

**Limits of detection (stated; this round claims no more).**
- **Deleted runs** cannot be enumerated. They are covered by the owner's commitment at the freeze (precondition 2), and
  the session's credential can break it.
- **Retention.**
  - Artifacts and logs expire after 90 days. One verdict condition reads an artifact: S1's measurements artifact, in
    the S1 binding (D21 (b); C.8 item 3). If it has expired or been deleted by `verdict`'s capture, `verdict` prints
    VOID (fail-closed; owner-approved R6 default, precondition 2), so `verdict`'s capture at `E` falls
    within 90 days of S1's run. No other verdict condition reads an artifact's content or existence (C.8 item 7).
    `order-s1.json` freezes the fixture-mode records at S1.
  - Logs are never evidence (§A.44). Run and job records persist until deleted.
- **Fork runs and local runs** are invisible to this repository's API. Pull-request runs from a fork run here and are
  enumerated, and job B is skipped in them.
- **Modified workflows** on other branches are detected only if they carry the pinned checker blob or the frozen names.
  A modified checker with renamed jobs is undetectable.
- **The session's credential** (`amaybaum`) can dispatch, post approval comments, re-run, push, force-move refs and
  delete runs. None of these is prevented.
- **The audit window** is `[T_repo, final capture]` for dispatches and `[T0, final capture]` for other events. After
  that, only the in-tree keys hold, the ref key included.
- **After the final capture,** routes (a)–(c) above reopen decisive mode on the round branch, and none of them is
  observed. The decisive output is public from `E`, so these routes threaten attestation hygiene, not blindness: a
  later decisive run could not show anything that was not already public. The owner's commitment at the freeze covers
  them (below).
- **The activity API's retention horizon.** On 2026-11-09, the oldest entry returned by
  `GET repos/amaybaum/incompleteness/activity?direction=asc` was the creation of `refs/heads/main` at
  2026-02-12T12:35:51Z. The repository was created at 2026-02-12T12:34:11Z. So the observed horizon reaches back to the
  repository's creation, which covers the round's window. The documented retention is not confirmed read-only
  (PENDING). GT-ACT checks that a force-push appears.

**Unauthorized executions, classified three ways.**

| execution | class | why |
| --- | --- | --- |
| an unapproved dispatch of the frozen splice or the pinned checker, on any branch of this repository, within the window | **detectable** (VOID) | the enumeration's rule (a)–(d): no matching entry. The checker is identified by blob or name, regardless of conclusions |
| a dispatch before the owner's comment, a reused comment, or a run whose `head_sha` differs from the quoted commit | **detectable** | the order rule and the binding re-anchored on the quoted commit |
| an approval comment edited after its run | **detectable** (VOID) | the edited-comment rule (`updated_at`) |
| a cancelled checker-bearing dispatch | **detectable** | identification ignores conclusions; the host-VOID rule (C.6) applies at S1 and `E` |
| a re-run attempt 2 or later | **prevented** for the frozen splice (job B's `if:`); **detectable** if job B ran | every attempt is read |
| a run at a commit outside the recorded branches, for example a branch cut from S1 | **detectable** within the window; **prevented** from computing by the ref key for the frozen splice | rule (d) and the closing violation clause; B3 and B4's ref key |
| a non-dispatch run in which B4 ran or A3b is not `success` | **detectable** | the no-unapproved-F1 rule |
| a force-move or deletion of a recorded branch | **detectable** within the window | the activity API, read in every capture |
| a dispatch after the final capture at a no-receipt ref | **prevented** for the frozen splice by the ref key, except after a force-move of the round branch | the round branch's head carries the receipt after `Q` |
| a force-move of the round branch after the final capture | **unobservable** to this round | no capture runs after the final one; it is barred by §A.43 without owner authorization |
| a fast-forward push to the round branch, after the final capture, of a commit that deletes the receipt | **unobservable** to this round | it is not a force-move, so the activity rule does not cover it; no capture runs after the final one; the owner's commitment covers it |
| a deletion of the round branch, after the final capture, and its re-creation at a pre-`Q` commit | **unobservable** to this round | no capture runs after the final one; the owner's commitment covers it |
| a deleted run | **unobservable** | it cannot be enumerated, and run ids are not contiguous per repository. It rests on the no-deletion commitment |
| a local run, or a run in a fork | **unobservable** | outside this repository's API |
| a modified checker with a different blob and renamed jobs and steps | **unobservable** | outside identification |
| a non-dispatch run before `T0` on an unrecorded branch carrying the checker | **unobservable** (residual; empty per the writer's record) | outside set (2)'s window |
| a capture that failed, was rate-limited or was truncated; an unreadable tree; a `total_count` mismatch | **evidence-incomplete**, fail-closed | retried, never a pass; a persistent failure halts the stage |
| a missing artifact (expired or deleted) | **not evidence**, except S1's measurements artifact, whose absence is **evidence-incomplete**, fail-closed (VOID; owner-approved R6 default) | no other condition reads one (C.8 items 3, 7) |
| an approval comment whose authorship (owner or session) cannot be told apart | **evidence-incomplete**, fail-closed | VOID unless the owner ratifies the entry: an entry in `approvals.json` at the designation of `E`; the `E` dispatch's own entry in the designation of `E` (approved R8 alternative) |

**What the session's credential can do, and whether each control is independent of the credential holder.**

| capability (as `amaybaum`) | the control that catches it | independent of the credential holder? |
| --- | --- | --- |
| dispatch | the enumeration, the entries and the order rule | **No at execution time:** the session runs the captures (`order`, `verdict`). **Yes after the fact:** the captures re-query host records. The independent results review re-runs the enumeration with its own read |
| re-run | job B's `if:` (in-tree); the enumeration of every attempt | the in-tree key is independent unless the workflow is edited (control W); the enumeration as above |
| cancel | identification ignores conclusions | as above |
| delete runs | none | **not independent**: unobservable; it rests on the no-deletion commitment |
| delete logs or artifacts | neither is evidence, except S1's measurements artifact, which the S1 binding reads; its deletion makes `verdict` VOID (owner-approved R6 default). A3b's conclusions and B6 at `E` carry the other facts (C.8 items 3, 7) | independent in effect; S1's artifact rests also on the no-deletion commitment |
| edit workflows | control W, and V3's governed paths on the round branch; on other branches, blob or name identification only | partial. A renamed, modified copy is unobservable |
| push to any branch, or create a branch from S1 | rule (d) within the window; the ref key | the in-tree key is independent; the detection as for dispatch |
| force-move or delete refs | the activity API in every capture | host-recorded, so independent within the window |
| after the final capture: push a receipt-deleting commit to the round branch, or delete and re-create the round branch | none: unobservable to this round | **not independent**. It rests on the owner's commitment; the decisive output is already public from `E` (attestation hygiene) |
| post or edit approval comments; record designations | the edited-comment rule; the owner's ratification of the run list and the entries in `approvals.json` at the designation of `E`, and of the `E` dispatch's own entry in the designation of `E` (approved R8 alternative) | **not independent** of the credential. The procedure requires the owner's designation with all entry digests (R8); R10 treats the host-time checks as conditions only, not an enduring claim they passed |

**Owner commitments, recorded at the freeze** (precondition 2):
- no workflow run, run log or artifact of this repository is deleted until `Q` (restating and extending c.6726548830
  item 1);
- the designation of `E` ratifies, by `order.json`'s sha256, the run list and every entry in `approvals.json`; the
  `E` dispatch's own entry and every retake entry require their sha256s in the owner's designation of `E`
  (approved R8 alternative). Under R10 these remain conditions of landing, not a claim that the unretained
  host-time approval and ratification checks passed;
- no force-move or deletion of a recorded branch without a recorded owner authorization (§A.43);
- after `Q`, no push to the round branch, and no deletion or re-creation of it, without a recorded owner
  authorization.

## Stop rule (halt-only)

The round halts under `S12`, with no preregistered rerun, on any of the following (C.6 states each in full):
- a failed `check` at S1 or `E`;
- at S1, any checker result other than exit 0 with complete output;
- at `E`, a red job, a replay mismatch or a `verdict` VOID;
- a host VOID, unless the owner records a retake decision after the void-run record and its sha256 are posted;
- any needed change to the control plane after `F`, or any parameter, rule, control or premise not frozen here;
- a checker outcome as C.6 defines it;
- a red fixture-mode control at S1 or `E` (owner-approved R2 default), or a failed S1 binding (C.8
  items 3 and 14).

Under D21 (b), a red decisive-mode control, an `out_of_scope` B-P or an undecided B-P voids only its own test's token,
and an `out_of_scope` or undecided reported-only fragment is reported. None of these halts the round. A substantive
token, or a P, B or C VOID token, is the measured outcome. A red control in P, B or C halts progression to ARP-3.
At a halt, `W` restores `verify.yml` to `F`'s state, keeps the record, and adds the evidence as produced and the
VOID note.

## Invariants and their checkpoints (§A.41)

Appendix D.9's rows, plus:

| invariant | checkpoint |
| --- | --- |
| no outcome depends on the choice of sham | the shams gate nothing (`decompose-p`); D14(d) drafted; the consequences of (a)–(c) stated |
| disturbance is measured as a kernel, including non-additive arms | `K` kernel; PL-SPI |
| P's claim is class-level complementarity, not attribution | `decide-p` step 4; frozen texts; S4 |
| both A/B readings are reported | `ab-p`; AB-P-FIX |
| A is named for what it is | `A_P` = B minus SA-1(c); the scaffolding listed |
| `mech_change` is computed at a frozen grain | `ablate-p`; MECH-FIX; grain supply × coupling type |
| read-set ablations report observer-level complementarity, not a misleading token | `OLC`; ABL-SA1b prints "not applicable" |
| `Adm_A` and `Adm_B` are generated by rule | the alphabet `Σ`; the rule; `adm_closure.py` |
| the freeze disclosure is printed | the frozen P texts; `result.md` |
| Level 1 is presented as a consistency check | the frozen Level-1 sentence; S4 |
| attribution is computed separately and never folded into the token | `ATTR`; ATTR-FIX; `decide-p` reads no sham field |
| representation choices supply no quantum-specific resource | the representation ledger; REP-INV; REP-PLANT; the reclassification rule |
| access-only restrictions are identified by computation | `access_only`; ACC-ONLY-FIX |
| a failed sketch review withholds only the dependent claims; the cone-dependent sentences are STAB-conditioned | *Proof reviews*; `STAB(K)`; STAB-FALSE, STAB-TRUE |
| every decisive family is built only through the gated entry | `s_decisive`; `DECISIVE_BUILDERS`; control B's name rules; the M-GUARD counter |
| each control's mode is frozen, and no fixture-mode control builds a decisive family | *Control modes* |
| REP-INV transports the frame, and its scope is stated | `S P S⁻¹`; REP-FRAME; the scope sentence |
| an identification-supplied contextuality in B-C is labelled (with an `out_of_scope` or `undecided` completion: owner-approved R9 default) | UPR-BC, its third case included |
| authorization checks fail closed within their stated scope; R10 host-time checks are landing conditions only | *Scope of authorization and detection*; the activity check; the edited-comment rule; ratification at `E` (the `E` dispatch's own entry: owner-approved R8 alternative) |
| decisive mode only on the round branch | the ref key in B3, B4, B6 and the checker; GT-REF. After the final capture, routes (a)–(c) are stated as unobservable and are covered by the owner's commitment; GT-ACT checks the activity read |
| P3 is credited as dynamics | the A/B typing; the ADA |
| B's LP reads its whole `Acc` | `lp_reads_equal_acc`; B-REG |
| TOMO's space is fixed | `Ω_c` definition |
| Level 2 is on P's setup with an owner-typed `Acc` | `decide-levels` |
| erasure is tested, with a classical eraser; `n/a` cells are recorded as `null` | the eraser fields; CW-P |
| W-CL has no frame blind spot | both frames; C-R60-ODD |
| record-dependent conditioning in C's origin is reported | C-A (`reg = none`) |
| the owner's terminology is used | S4 ("native OI") |
| B6 compares the decisive output without its dispatch field, and binds the committed measurements | `replay` (C.8 item 3); B6 at `E` |
| a non-dispatch run's fixture mode is read from a step conclusion | A3b; A3's conclusion when A3 never started; the no-unapproved-F1 rule (C.3; C.8 item 7); for an A3 that started and left no output, the executor precondition for pushes to recorded branches (C.3), whose breach is a violation (fail-closed) |
| STAB-FALSE reads pinned certificates in its own process | A9; the certificate pins (C.8 item 12) |
| every passage the file relies on is stated in it | Appendix D; the r5, r6 and r7 drafts cited as provenance only |
| scope choices and the level of a VOID are the owner's | D19 to D23 recorded (c.6740078002), quoted in *Owner decisions D19 to D23*; R1–R10 approved at c.6778994857 and applied in precondition 2; other pre-F pending items still block control P |
| SG-1: no narrowing to manufacture success | B-P decided whole: `decide-b`'s step 1 on B-P's 32 preparations and nine settings; removals only with verified certificates (C-CERT, B-RAY, M-RAY); C-IFACE's `decide-b` rule and its mutation; reported-only fragments read by no token; C.6 after `F` |
| SG-2: resource limits fixed before execution; an over-limit B-P gives VOID | `S_max`, caps, budgets, timeout and stress pin entered before `F` (control P); `check --freeze` recomputes them from the pinned `stress.json`, and requires the `S_max` of this file, of the checker and of `stress.json` to be equal and at least `10^5` (R1's floor: owner-approved R1 default; C.8 item 2); M-BUDGET; the self-test cases for an `out_of_scope` and an `undecided` B-P; the B-VOID limitation text; C.6 |
| SG-3: a failure in C does not erase P's result; compromised provenance voids every affected result | the `decide-levels` self-test cases (C-VOID or B-VOID with P-COMPLEMENTARITY gives Level 1); the provenance list of D21 and C.6; `verdict` VOID on each provenance failure and incomplete-output halt (self-test); S1-BIND |
| SG-4: no imported quantum mechanism via representation choices, comparison maps or reductions | the representation ledger, REP-INV, REP-PLANT; C-IFACE's `bp_equals_qmp` rule over `decide-*`, `decide-levels` and the ADA status functions `ada_*`, with its mutations; B-RAY, M-RAY and C-CERT for removals; the diagnostics' depth-1 label |
| B-P's caps and budget derive from ST-BP by a frozen rule and are fixed before `F` | C.8 item 2's rule; `check --freeze`; A7's stress pin at 6′, S1 and `E` |
| the caps count extreme rays, each removal certified | C.8 item 15; the verifier's removal check; B-RAY; M-RAY |
| the committed measurements are S1's output | the S1 binding in `verdict` (C.8 item 3); S1-BIND |
| `pred_change` for the read-set ablation separates changed from added quantities | the self-test case of `ablate-p` on a synthetic ABL-SA1b record, which must give `common` false and `added` non-empty (D23 (c); *The controls*, self-tests) |
| outputs do not depend on string-hash order, which `-I` leaves randomized | control B's no-`set` rule on `qc21_check.py`, with its M-GUARD variant; A7 at 6′ and the replay at `E` across processes |
| the design run and 6′ run the trees they name, not a synthetic merge | their pull requests' base is a branch held at `D`; `check --freeze` checks the run records' `pull_requests` base and head `sha`, and re-derives both records from the host by their run ids (C.7; ARP-3-QC22 r14a, R14-N4) |

## Preconditions of `F`

1. **ARP-1 landed and reviewed.**
   - Landed at `fd539e150759a6ea51ab279aeeac80fc06050ade` (#1208).
   - Receipt `verification/receipts/ARP-1-MARC.json`, with `Q` = `e064e766156e38ea2c307c4691bc43f98458e03d` and `E` =
     `c95e5c34e5a246046ab8ed420f26891fd18de565`.
   - Token `ARP1-MARC-SURVIVAL`.
   - Results review #1208 c.6732612066, CONFIRMED WITH QUALIFICATIONS. The three qualifications are findings 9–11, and
     finding 8 states SURVIVAL is "not a proof of inaccessibility".
   - `--verify-round` output.
     - Command: `python3 -I -B v3_verifier.py --verify-round e064e766156e38ea2c307c4691bc43f98458e03d`, with the
       verifier taken from `fd539e15:tools/v3_verifier.py` (sha256
       `fc6545f581cd3282d43a65edbefea69722a2b3f006679a6ec9b1627845cede4a`) and run read-only in the repository
       (`is-shallow-repository: false`), 2026-11-09.
     - Output: four `ATTESTATION … recorded, unverified` lines (the owner designations of `F` and `E`, and the check
       runs 42516831042 and 42564902307), then `VERDICT  HOLDS`, exit 0.
     - Blobs at `fd539e15`, unchanged at `D`, are listed under *Inputs*.
   - Effect: none on this round's question, controls or decision rule; the ledger row L-REG cites the SURVIVAL
     token.
2. **Owner decisions** recorded: #1169 c.6735014875 (*Owner decisions at the freeze*). Still to be met before `F`:
   - the D18 condition (the representation ledger, reviewed) (PENDING);
   - the D14 condition (`ATTR`, reviewed) (PENDING);
   - the verdicts of the two sketch reviews, quoted (PENDING). *Proof reviews* quotes both with their sha256s. The
     item is discharged only when both review files, `review/proofs/REVIEW-LEMMA-P.md` and
     `review/proofs/REVIEW-CONE.md`, are on `main`, with precondition 3's paper records or in the record
     directory: CC-NAT's gating rests on Lemma P's verdict, and the content a claim uses lands on `main` no later
     than the claim (§A.42 items 2 and 8; re-review r14a-N8);
   - the owner commitments of *Scope of authorization and detection*, recorded with author and time (PENDING);
   - D19 to D23: recorded with author and time (c.6740078002; *Owner decisions D19 to D23*);
   - **Owner rulings R1–R10: APPROVED**, #1169 c.6778994857, 2026-11-10; owner answer quoted in OWNER-DECISIONS.md.
     The selected rules are:
     - **R1.** Initial `S_max = 100000`. Its default form bounds visited `(d−1)`-subsets in solver and verifier;
       1200 s and timeout-minutes 60 remain separate limits. Initially the floor is 100000. After a red design
       run the owner may fix a positive value no larger than that run's; if that run used at most 100000, the
       same decision may remove the floor before another authorized design run. No measured cap is supplied.
     - **R2.** Default: a red fixture-mode control at S1 or `E` makes A3 exit 3 and halts the whole round,
       every result VOID. The test-level alternative and its conditional reader/guard changes are not selected.
     - **R3.** Default: the timeout test charges `1203 · W_max` for the full reported-only volume. SF-2 is
       decided without caps/budget in the authorized stress phase and contributes to the general maxima.
     - **R4.** Default: choose B-P's reference with that whole reported-only term in the timeout test; no
       B-P-first aggregate `W_RO` allocation is adopted. A failed test precludes an F request.
     - **R5.** Default: only B-P receives the raised caps/budget triple. All other B fragments retain general
       caps/budgets; fixtures and QM-P's restricted fragment retain their general treatment.
     - **R6.** Default: expired/deleted/unreadable S1 measurements evidence fails binding and halts the round
       VOID. Verdict capture at `E` must therefore be within its 90-day retention; missing data is not a pass.
     - **R7.** Default: a changed REP-INV B table beyond relabelling is recorded as changed input and the
       identification is reclassified imported. It is not re-decided; the volume 1203 is unchanged.
     - **R8.** Alternative: the owner's designation of `E` quotes `order.json`'s hash and the canonical-JSON
       sha256 of each E-stage approval entry, including every host-VOID retake. `verdict` reads the designation
       through the existing comment template and checks owner/OWNER identity and every required digest.
       No separate ratification comment is used. Credential independence is not claimed.
     - **R9.** Default: an `out_of_scope` or `undecided` UPR-BC completion yields no label and no L-UPRIME
       reclassification; print the B-C result with that completion status. B-C still changes no Level.
     - **R10.** Narrowing: final capture, E-stage approval and ratification checks remain operational
       conditions of landing. The enduring record says the round may land only if they pass; it does not state
       that the unretained host-time checks passed or establish their governance claims. Their records are
       provenance, not retained scientific support. No exception or waiver is granted. This applies to C.2
       Its record/Violations, C.3 Authorship and verdict conditions, C.8 item 9, the credential row, owner
       commitments and both invariant tables. Scientific tokens still require the separately authorized
       replay at `E`; neither this ruling nor implementation claims that any dispatch occurred.

   D12 is waived (c.6735159962), so no Environment setup step remains.
3. **REACHABLE r3 and DESIGN-DS r13** on `main` as separate paper records before `D` (D9(a)), pinned by blob.
4. **ARP-3-QC22's text**, copied in Appendix C with the D12 edit log (D10(a)). Done in r11; its review falls under
   precondition 5.
5. **Independent review** of this control plane with no open blocking finding. It covers in particular the
   representation ledger, `ATTR`, `access_only`, the control modes, and Appendix C as edited. It also checks that the
   owner's three acceptance conditions for removing D12 hold.
6. **No `PENDING`.**
7. **Design run, confirmation run and gate tests** as Appendix C.7, including ST-BP and the caps and budgets it fixes
   (C.8 items 1 and 2). c.6740078002 authorizes none of them.
8. **The `F` dispatch**, green.
9. **Designation request.**

## Appendix A. r5 *The model* (C's base, verbatim from r5)

**The model.**
- Ring `Z_3`, alphabet `F_2`. Cell `i` carries `(u_i, v_i)`. The rule `Φ_g`: `u_i' = g(u_{i−1}, u_{i+1}) + v_i`,
  `v_i' = u_i`, with `g` one of the eight symmetric Boolean functions of two arguments. Every `Φ_g` is a bijection of
  `F_2^6` (C-STEP).
  - **Test rules** (non-affine): `g ∈ {AND, NAND, OR, NOR}`.
  - **Countercontrol rules** (affine): `g ∈ {0, 1, XOR, XNOR}`. `XOR` is `N_1` on the triangle (`k_ij = 1`,
    `k_ii = 0`); all four are symplectic and center-free.
- **Carrier U′** = cells 0 and 1: `(z_1, x_1, z_2, x_2) = (u_0, v_0, u_1, v_1)`; `f_z = u_0`, `f_x = v_0`,
  `f_y = u_0 + v_0 + u_1 + v_1`. **Mediator** = cell 2.
- **R**: `r_a(μ) = μ(f_a = 0) − μ(f_a = 1)` for every carrier law μ, read in **fixed slots** (`f_z = u_0`,
  `f_x = v_0`) at every time.
- **Frame convention (frozen).** QA's U′ is defined in the common encoded frame, which is `(z, x) = (u, v)` at even
  ticks and `(v, u)` at odd ticks (AP1 §4.2; QA:445-448). In that frame a free tick is the identity; in fixed slots it
  is the transposition `x ↔ z`, with `f_y` unchanged and determinant −1. This round keeps fixed slots and corrects the
  determinant: for a round with `k` ticks, `det_enc β = (−1)^k det_fix β`. `outside_ball`, `nonstab_valid`,
  `offaxis_unit` and octahedrality are invariant under the transposition, so only the determinant needs the
  correction. Both determinants are reported for every induced map. (Fixed slots are kept, rather than carrying each
  law's tick parity, so that R stays one affine function of μ on all of `L_scope(g)`, which the affine-basis check
  needs.) The mediator supplies are closed under `u ↔ v` (both known-`u` and known-`v` ready cells are listed), so the
  supply set does not depend on the frame.
- **"Induced" is time-covariant (definition).** Induced means one fixed-slot affine map on all of `L_scope(g)`. With
  `P` the transposition `x ↔ z`, its encoded action is `P^k β` on even-parity inputs and its `P`-conjugate
  `P^{k+1} β P` on odd-parity inputs (parity of the law's total tick count); both have determinant `(−1)^k det β`. This
  is stricter than requiring an induced map on one parity class only, so it can only miss a CANDIDATE, never create
  one, and it does not affect NONSTAB or NO-VALID-ESCAPE. Diagnostic field `induced_parity0` (informational; `decide`
  does not read it): rounds that induce a map on the parity-0 subset of `L_scope(g)` (laws reached with an even total
  tick count; a law reached at both parities belongs to both) but not on all of `L_scope(g)`, with that map.
- **Start set `S_0`** (23 carrier laws, supplied preparations): the family `Λ_{a,b}`, `Λ_0` (7 laws; QA:580-601), and
  the 16 products of P2 ready cells, one per carrier cell, with known slot `u` or `v` and value 0 or 1, the other slot
  uniform (N2).
- **Mediator supplies `M`** (5 laws): ready with `u_2 = b` or `v_2 = b` known (`b ∈ {0,1}`), other slot uniform; or
  a source cell, both slots uniform.
- **One round** `π = (m, k, reg)`: attach `m ∈ M` in product with the carrier law; apply `Φ_g^k`, `k ∈ {1, …, 6}`;
  then `reg = none` (marginalize) or `reg = (s, r)` with `s ∈ {u_2, v_2}`, `r ∈ {0, 1}`: register slot `s` of the
  mediator and condition on the value `r` (kept only with positive probability); discard the mediator. 150 rounds,
  enumerated in the frozen order `m` (as listed), then `k`, then `reg` (`none`, `(u_2,0)`, `(u_2,1)`, `(v_2,0)`,
  `(v_2,1)`).
- **Forward conditioning, terminal registration.** The registered mediator slot is read after the round's last tick,
  the conditioned law is the carrier law at that time, and the mediator is discarded at once, so it is coupled to no
  cell afterwards (P1 terminal, NE-2). No carrier law is conditioned on a later record. After the discard no cell
  correlated with the carrier is retained, so the carrier-level description satisfies H-LIFT.
- **`L_scope(g)`**: `S_0`, every one-round output of an `S_0` law, and every one-round output of those, normalized,
  deduplicated by exact value. Depth 2.
- **Induced maps.** For a round `π` with herald `q_π(μ)` on `L_scope(g)`: `π` is *herald-constant* when `q_π` is
  positive and equal on all of `L_scope(g)`. Then `α = R(π Λ_0)`, `β e_a = R(π Λ_{a,0}) − α`, and `π` *induces*
  `(α, β)` when `R(π μ) = α + β R(μ)` for every `μ ∈ L_scope(g)`.
- **Affine basis (exact, bounds the cost).** `q_π(μ) = 1ᵀB_π μ` is linear in μ, so it is constant on `L_scope(g)` iff it
  is constant on an affine basis of `aff L_scope(g)`; when it is constant, both `μ ↦ R(B_π μ)/q` and
  `μ ↦ α + β R(μ)` are affine, so the identity holds on `L_scope(g)` iff it holds on that basis. The checker selects
  the basis exactly (`Fraction` row reduction of the law vectors, at most 16 laws, first in the frozen enumeration
  order, containing `Λ_0` and `Λ_{a,0}`) and checks herald and identity on it, plus positivity of `q_π` on all of
  `L_scope(g)`. Control C-AFFB confirms the equivalence on the four affine rules by the full check over `L_scope(g)`.
  `L_scope(g)` and the basis are the stated finite generating set of REACHABLE §1.4. An induced map is **unitary** when `α = 0`,
  `βᵀβ = I` and `det_enc β = (−1)^k det_fix β = 1`, with `k` the round's tick count (`k = 0` for PC-PLANT's planted
  map); **octahedral** when `β` is a signed permutation.

## Appendix B. r5 controls carried into C (verbatim from r5; adapted as stated in *The controls*)

| code | what | green when | route to failure |
| --- | --- | --- | --- |
| **CC-DYAD** (countercontrol) | all eight rules, rounds with `reg = none` only, their own depth-2 closure | every `V` entry has a power-of-2 denominator; `offaxis_unit = 0`; every induced map with `α = 0` and orthogonal `β` is octahedral (REACHABLE Lemma 5: dyadic descent, any dynamics) | conditioning leaking into the unconditioned class; a propagation or arithmetic error introducing other denominators; an induced-map routine that accepts a non-orthogonal fit |
| **C-AFFB** (affine-basis equivalence) | (a) on the four affine rules, every round's herald constancy and induced map computed both on the affine basis and over all of `L_scope(g)`; (b) on a fixed full-rank fixture set: `S_0`, PC-PLANT's seven laws, PC-NONSTAB's two laws and the 16 point laws (48 laws, linear rank 16), under every `k = 1` round of rules `0` and `XOR` and under PC-PLANT's `B_P`, extended as the identity on the four configurations its six planted supports do not cover | (a) and (b): identical results for every round; in (b) the selected basis has 16 laws | a basis that does not span `aff L_scope(g)`, a selection bug that shows only on large or full-rank sets, or a non-linear herald treated as linear |
| **C-XB** | independent propagation: for every rule, every `S_0` law and every round, the output recomputed by direct enumeration of the 64 joint configurations with integer weights over a common denominator, sharing no code with the permutation path | `mismatches = 0` over all `8 · 23 · 150` cases | a wrong permutation power, mask or marginal |
| **C-FRAME** (frame convention) | rule `0`, rounds with `k = 1`, on `L_scope(0)` | every herald-constant round induces `α = 0` and the transposition `x ↔ z` (`β e_x = e_z`, `β e_z = e_x`, `β e_y = e_y`), with `det_fix = −1`, `det_enc = +1` and encoded action `P^k β = I`, so it is classified unitary and octahedral | a frame or determinant convention that would report an encoded rotation as improper, and so turn a CANDIDATE into NONSTABILIZER |
| **C-STEP** | every `Φ_g` against an independently written inverse `(u, v) = (v', u' + g(v'_{i−1}, v'_{i+1}))`; `g` symmetric; reads neighbours only; affine classification by algebraic normal form; `XOR`'s matrix symplectic | all hold | a rule that is not the declared one |
| **C-SCOPE** | `|S_0| = 23`, `|M| = 5`, 150 rounds, depth 2 reached for every rule, `complete = true` | all hold | a truncated enumeration |

## Appendix C. ARP-3-QC22 r13's LP method, guard machinery and execution design, copied under D10(a), with D12's removals

**Source.** Q-C2-2's `preregistration.draft.md` r13, sha256
`15d90b24496a733d87079256f4a3efb06f426bfaba775aa77e7bc2adda2f4dd2`. This appendix is the copy this round freezes. The
source is a draft of a later round and is not on `main`. Nothing in this round rests on the scratch file (§A.42 item 8;
re-review R10-B1).

**Copied spans** (source lines), each with the five identifier renames only: `ARP-3-QC22` → `ARP-2-QC21`, `ARP3QC22` →
`ARP2QC21`, `arp3qc22` → `arp2qc21`, `arp3-qc22` → `arp2-qc21`, `qc22_check.py` → `qc21_check.py`. The spans are:
- C.1 *The exact method*, 297–486, verbatim;
- C.2 *The workflow edit*, 1099–1326, with the edits in the log below;
- C.3 *Runs, evidence, approvals*, 1328–1475, with the edits in the log;
- C.4 from *The controls*, the rows F10, ZPT, C-CERT, C-INDEP, C-STATELESS, C-BUDGET, C-NCF, C-SYM and C-EXACT, verbatim,
  and the self-test block, 525–628 (M-FACET, M-W, M-MODEL, M-SOLVER, M-FACTOR, M-INDEP, M-BUDGET, M-EVAL, M-SWAP,
  M-GUARD, M-MODE), with the edits in the log;
- C.5 *Scripts*, 849–1096, with the edits in the log;
- C.6 *Stop rule (halt-only)*, 1476–1513, with the edits in the log;
- C.7 the preconditions QC22 numbers 6, 6′ and 6″, **adapted** (rewritten for this round; not verbatim), with the
  Environment-only preconditions 2a and 2b, the gate tests GT-1, GT-2, GT-2b, GT-3, GT-6, GT-6b and GT-7, and A11 dropped
  (D12; c.6735159962).

**The D12 edit log** (re-review R10-B5, E1–E13; the owner's waiver c.6735159962), with row 45 (R11a-B1), the r13
rows 46–71 (C.8), the r14 rows 72–85 (D19 (0)(c), D21 (b)), the r14a rows 86–98 (re-review r14-N3, N11, N12;
rows 92–98 found via ARP-3-QC22 r14), the r14b rows 99–108 (re-review R14A-B1, r14a-N1 and N2) and the r14c
rows 109–126 (re-review R14B-B1, r14b-N1, N2, N6 and N9; rows 109–112, 114–117, 119 and 123 found via ARP-3-QC22
r14a, and row 126 via its r14a review's Rc1), with r14d rows 127–130 and r15 rows 131–134. Each row replaces copied text that starts as shown; for rows 99–134
that text is as the earlier rows leave it. `ref key` rows add the ref key; `downgrade` rows replace "prevented"
by "detected" claims.

| # | tag | section | copied text (start) | becomes (start) |
| --- | --- | --- | --- | --- |
| 1 | E12 | C.2 | **Two jobs (owner decision c.6726548830, item 4).** The splice adds two jobs. | **Two jobs.** The splice adds two jobs. |
| 2 | E1/E12 | C.2 | is the only job that can compute F1. It is gated by a GitHub Environment   whose required reviewer is the owne… | is the only job that can compute F1. With the Environment gate waived for this round   (c.6735159962), its exe… |
| 3 | E12 | C.2 | They are split because an Environment's protection applies to every run of a job that names it, so a single jo… | They are split so that job A's fixture mode runs on every event, while job B's decisive mode is reachable only… |
| 4 | E12 | C.2 | - Job B is skipped on every run that is not an owner-gated dispatch. | - Job B is skipped on every run that is not a first-attempt dispatch with the decisive input. |
| 5 | E13 | C.2 | **Its condition, `if:`** (job level, so it is evaluated before the Environment is consulted): | **Its condition, `if:`** (job level): |
| 6 | E1 | C.2 | **It names the Environment, `environment: arp2-qc21-decisive`** (frozen). GitHub holds the job before it start… | (removed) |
| 7 | ref key; E3 | C.2 | - B3. **"ARP-2-QC21 approved commit and receipt"**:   `test "$GITHUB_SHA" = "$ARP2QC21_SHA" && test ! -e verif… | - B3. **"ARP-2-QC21 approved commit and receipt"**:   `test "$GITHUB_SHA" = "$ARP2QC21_SHA" && test "$GITHUB_R… |
| 8 | E3 | C.2 | - B3b (**only if E-BIND is adopted**, precondition 2b; r11 N4). **"ARP-2-QC21 approval names this commit"**:  … | (removed) |
| 9 | ref key | C.2 | --event "${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && hashFiles('verification… | --event "${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && github.ref == 'refs/hea… |
| 10 | ref key; E2 | C.2 |   - **The in-tree keys are kept as defence in depth:** the event key, the attempt key, the receipt key, and th… |   - **The in-tree keys:** the event key, the attempt key, the ref key, the receipt key, and the checker's four… |
| 11 | ref key | C.2 |   `if: ${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && hashFiles('verification/r… |   `if: ${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && github.ref == 'refs/heads… |
| 12 | E4 | C.2 | (A3, A5, A7, A8, A9, A11, B3b, B4, B6) is `python3 -I -S -B`, so no `.pth` or other startup file runs in any s… | (A3, A5, A7, A8, A9, B4, B6) is `python3 -I -S -B`, so no `.pth` or other startup file runs in any step. Both … |
| 13 | E13 | C.2 | its job-level `if:` is false for them, so the job is `skipped` before the Environment is consulted, and no dep… | its job-level `if:` is false for them, so the job is `skipped` by the job-level `if:` (verified at the design … |
| 14 | E2 | C.2 | **Enforcement, in order (owner decision c.6726548830, item 4; r10 review, overall design).** 1. **Primary: the… | **Enforcement, in order (owner decision c.6735159962; re-review R10-B5).** The Environment gate is waived for … |
| 15 | E2 | C.2 |   - the Environment approved job B's deployment, on a ref the policy admits;  | (removed) |
| 16 | ref key | C.2 |   - B3: the run's commit equals the dispatch input, and the tree has no receipt; |   - B3: the run's commit equals the dispatch input, the ref is the round branch, and the tree has no receipt; |
| 17 | ref key; B2 | C.2 |   - the checker's three keys;   - the F1 builder's own refusal check passes. |   - the checker's four keys;   - the gated entry's and each decisive builder's own refusal checks pass. |
| 18 | downgrade | C.2 | - it is an owner-approved, first-attempt, gated dispatch whose commit is the approved one; - the tree carries … | - it is a first-attempt dispatch with the decisive input, on the round branch, whose commit equals the input; … |
| 19 | downgrade | C.2 | **After merging to `main` (owner's restated requirement 3; c.6726548830, items 2 and 4).** - **On `main`.** A … | **After merging to `main` (owner's restated requirement 3; c.6735159962).** - **On `main`.** A dispatch with `… |
| 20 | downgrade | C.2 | - **A gated dispatch on one** waits for the owner's approval, which is not given. B3 also requires the input t… | - **A dispatch on one** fails B3's ref key unless it is on the round branch. On the round branch it runs, and … |
| 21 | downgrade | C.2 | so it would be a route into decisive mode. The Environment would still gate that route, because it gates the j… | so it would be a route into decisive mode. That route is ungated. Any such change after landing is outside the… |
| 22 | E5 | C.3 | - **Approval entries, keyed on `(run_id, run_attempt)` (re-review r7 B1, r9 B4(a); c.6726548830, item 4).** Ea… | - **Approval entries, keyed on `(run_id, run_attempt)` (re-review r7 B1, r9 B4(a); c.6735159962).** Each decis… |
| 23 | E5/E6/E7 | C.3 |   - **The deployment review** (`review`). It is read from `GET actions/runs/{run_id}/approvals`. The entry hol… |   - **The edited-comment rule (re-review R10-B5).** `approval_updated_at` must equal `approval_created_at`, or… |
| 24 | E13 | C.3 |     - In attempt `≥ 2`, job B's job-level `if:` is false, so job B is `skipped` before the Environment is cons… |     - In attempt `≥ 2`, job B's job-level `if:` is false, so job B is `skipped` by the job-level `if:`. |
| 25 | E13 | C.3 |     - Whether the host would ask for approval again on a re-run of an Environment-gated job is not relied on a… | (removed) |
| 26 | E5 | C.3 |     - its frozen expectation;     - its review record, if any;  |     - its frozen expectation;  |
| 27 | E11 | C.3 |     - one trees call per distinct `head_sha` absent locally;     - a few calls for the Environment, approvals … |     - one trees call per distinct `head_sha` absent locally;     - the activity calls for the recorded branche… |
| 28 | activity; deletion | C.3 |   - **Residual (stated).** A deleted run cannot be enumerated. The owner's decision c.6726548830, item 1 ("No … |   - **Ref moves (re-review R10-B5).** Every capture reads `GET activity?ref=refs/heads/<branch>` for each reco… |
| 29 | E8; ratification | C.3 |   - every check at `E` passes, control N included; |   - every check at `E` passes;   - the owner's designation of `E` ratifies, by `order.json`'s sha256, the run … |
| 30 | E1; ref key | C.4 |     - the event key, the attempt key or the receipt key, from B4 or from B6;     - any key of job B's `if:`;  … |     - the event key, the attempt key, the ref key or the receipt key, from B4 or from B6;     - any key of job… |
| 31 | ref key | C.4 |     - `s_mode` must return `"fixture"` for each single-key failure: `--event workflow_dispatch` with       `GI… |     - `s_mode` must return `"fixture"` for each single-key failure: `--event workflow_dispatch` with       `GI… |
| 32 | ref key | C.5 |     - `--event <name>` is required for the default computation. **Three keys select decisive mode (re-review r… |     - `--event <name>` is required for the default computation. **Four keys select decisive mode (re-review r8… |
| 33 | E3/E4 | C.5 | `stress-check <stress.json>`,     `env-read` (E-READ (a) or (c) only), `approval-check <run_id> <sha>` (E-BIND… | `stress-check <stress.json>`,     `derive-run` |
| 34 | E8/E9 | C.5 |     - R: record files by stage (S1 includes `confirmation-run.json`, `confirmation-measurements.json`, `gate-t… |     - R: record files by stage (S1 includes `confirmation-run.json`, `confirmation-measurements.json` and     … |
| 35 | E5/E6/E8 | C.5 |             - `actions/runs/{DEC}/approvals`;             - `environments/arp2-qc21-decisive`;             - `… | (removed) |
| 36 | E2 | C.5 |         B claims nothing about routes it does not model, such as the interpreter, the runner or the host. It d… |         B claims nothing about routes it does not model, such as the interpreter, the runner or the host. With… |
| 37 | E2/E9 | C.5 |         - **Who approves.** The session acts under the owner's GitHub identity, `amaybaum`. It never calls the… |         - **The session's credential.** The session acts under the owner's GitHub identity, `amaybaum`. What t… |
| 38 | E1 | C.5 |       - job B's job-level `if:`, its `environment: arp2-qc21-decisive` line, its `env:` and B3; |       - job B's job-level `if:`, its `env:` and B3 (with the ref key); |
| 39 | ref key | C.5 |       - B4's compound `--event` expression and B6's `if:`; |       - B4's compound `--event` expression and B6's `if:`, each with the ref key; |
| 40 | E3/E4 | C.5 |       - the aggregate's lines;       - per precondition 2b: A11 and job A's `permissions:` (E-READ (a)), and B… |       - the aggregate's lines. |
| 41 | E1/E3/E4 | C.5 |       - any key of job B's `if:`;       - the `environment:` line;       - B3;       - A3's literal;       - t… |       - any key of job B's `if:`;       - B3, or its ref key;       - A3's literal;       - the marker A10; |
| 42 | E8 | C.5 |     - **N: the Environment** (owner decision c.6726548830, item 4; r11 B1). It compares a read of the Environm… | (removed) |
| 43 | E12 | C.6 | That covers a deployment the host rejected or let expire, a ref the policy refused, and a B3 failure. | That covers a B3 failure, the ref key included, and a job B that the host did not start. |
| 44 | round | C.6 | Progression to ARP-4 stops. | Progression to ARP-3 stops. |
| 45 | R11a-B1 | C.3 | branch and the gate-test branch, whose commits since `D` are listed in `order.json`. | … listed in `order.json`. The GT-ACT branch (C.7) is **not** a recorded branch (R11a-B1). … |
| 46 | r13 item 14 | C.2 |   `python3 -I -S -B <record dir>/qc21_check.py --event fixture > "$RUNNER_TEMP/arp2-qc21/fixtures.json"`. |   `mkdir -p "$RUNNER_TEMP/arp2-qc21" && python3 -I -S -B <record dir>/qc21_check.py --event fixture > "$RUNNER… |
| 47 | r13 item 14 | C.2 |   `python3 -I -S -B <record dir>/qc21_check.py --event "${{ |   `mkdir -p "$RUNNER_TEMP/arp2-qc21" && python3 -I -S -B <record dir>/qc21_check.py --event "${{ |
| 48 | r13 item 8 | C.2 | - A4. `actions/upload-artifact@v4` of `fixtures.json` | - A3b. **"ARP-2-QC21 fixture output is fixture mode"** (a marker; §A.44; r13 item 8):   `python3 -I -S -B <rec… |
| 49 | r13 item 8 | C.2 | Every interpreter the splice starts (A3, A5, A7, A8, A9, B4, B6) is `python3 -I -S -B` | Every interpreter the splice starts (A3, A3b, A5, A7, A8, A9, B4, B6) is `python3 -I -S -B` |
| 50 | r13 item 3 | C.2 | - B6. `python3 -I -S -B <record dir>/controls.py replay` against the committed measurements, with | - B6. `python3 -I -S -B <record dir>/controls.py replay "$RUNNER_TEMP/arp2-qc21/measurements.json"`, against t… |
| 51 | r13 item 3 | C.2 | - **B6** runs only under the same workflow keys, and compares bytes only. | - **B6** runs only under the same workflow keys, and compares canonical JSON only (C.8 item 3). |
| 52 | r13 item 8 | C.2 | - **A3** runs fixture mode by its literal `--event fixture`. | - **A3** runs fixture mode by its literal `--event fixture`, and A3b records that mode as a step conclusion. |
| 53 | r13 item 8 | C.2 | - **A7, A8, A9 and A10** compute nothing of F1. | - **A3b, A7, A8, A9 and A10** compute nothing of F1. |
| 54 | r13 item 3 | C.2 | and compares bytes (r7 N2). | and compares them as canonical JSON with `parameters.dispatch_sha`   removed from both (r7 N2; C.8 item 3). |
| 55 | r13 item 8 | C.3 |   `{run_id, run_attempt, head_sha, event, jobB_conclusion, B4_conclusion, A3_conclusion, fixtures_artifact_sha… |   `{run_id, run_attempt, head_sha, event, jobB_conclusion, B4_conclusion, A3_conclusion, A3b_conclusion, fixtu… |
| 56 | r13 item 8 | C.3 |   - At `E`, a run whose artifact is missing in the fresh capture counts as compliant only if `order-s1.json` h… |   - The no-unapproved-F1 rule reads no artifact, so a missing artifact is not a violation. `order-s1.json` kee… |
| 57 | r13 item 3/8 | C.3 |   - S1's `artifact_sha256` equals the committed measurements; |   - B6 at `E` is `success` and its replay result is a match, which binds the committed measurements to the app… |
| 58 | r13 item 6 | C.4 |     - `t_builder_refuses`, run under every synthetic environment above and under the real one, must record the… |     - `t_builder_refuses` runs once, under A8's real environment, and must record the refusal (r10 B2). The re… |
| 59 | r13 item 15 | C.4 | Q+RY with `T = 5` | B-S4F with `T = 3` |
| 60 | r13 item 8 | C.4 |     - A3's literal `--event fixture`;     - the marker A10. |     - A3's literal `--event fixture`;     - the marker A10;     - the marker A3b. |
| 61 | r13 items 4, 5 | C.5 | `os` is referenced at exactly two     sites, each `os.environ` passed whole to `s_mode`: the default entry, an… | `os` is referenced at exactly two     sites, each `os.environ` passed whole to `s_mode`: the `if __name__ == "… |
| 62 | r13 item 5 | C.5 | The F1 builder's first statement checks       `s_mode(sys.argv, os.environ) == "decisive"`, and raises otherwi… | The first statement of `s_decisive` and of       every registered builder is the call `s_refusal()`, whose bod… |
| 63 | r13 item 5 | C.5 |       - the default entry;       - the single self-test function |       - the entry function `s_entry` (the default computation);       - the single self-test function |
| 64 | r13 items 5, 7 | C.5 |         - the F1 builder's name is referenced only at the two sites named above (the default entry and        … |         - `s_decisive` is referenced only at the two sites named above (`s_entry` and `t_builder_refuses`, in … |
| 65 | r13 item 9 | C.5 |         - The string `"workflow_dispatch"` occurs only in the run-classification functions (`derive-run`, `ord… |         - The string `"workflow_dispatch"` occurs only inside the module-level string constants named `SPLICE_… |
| 66 | r13 item 3 | C.5 |         - `replay` compares files only: it reads two files in `"rb"` mode and compares their bytes. |         - `replay` compares files only: it reads two files in `"rb"` mode, parses each with `json.loads`, remo… |
| 67 | r13 item 8 | C.5 | `stress-check <stress.json>`,     `derive-run`, `order`, `verdict`, `--self-test`. | `stress-check <stress.json>`,     `fixture-mode-check <fixtures.json>`, `derive-run`, `order`, `verdict`, `--s… |
| 68 | r13 item 8 | C.5 |       - the marker A10;       - the aggregate's lines. |       - the markers A10 and A3b;       - the aggregate's lines. |
| 69 | r13 item 8 | C.5 |       - A3's literal;       - the marker A10; |       - A3's literal;       - the marker A10;       - the marker A3b; |
| 70 | r13 certificates | C.5 |     - R: record files by stage (S1 includes `confirmation-run.json`, `confirmation-measurements.json` and     … |     - R: record files by stage (S1 includes `confirmation-run.json`, `confirmation-measurements.json`,       `… |
| 71 | r13 certificates | C.5 | evidence pins, including `stress.json`'s sha256. | evidence pins, including `stress.json`'s sha256 and the two STAB-FALSE certificates' sha256s. |
| 72 | D21 (b) | C.3 |   - B6 at `E` is `success` and its replay result is a match, which binds the committed measurements to the app… |   - B6 at `E` is `success` … (C.8 items 3, 7);   - the S1 binding holds: S1's measurements artifact, read in memo… |
| 73 | D21 (b); D19 (0)(c); r14a N2 | C.4 | C-CERT: … and re-enumerates the facets; for every step (2, 3, 4) that decided \| `unverified = 0` | C-CERT: … and re-enumerates the facets (over the retained rows; C.8 item 15) … \| in fixture mode, `unverified = 0` …; in decisive mode … C-CERT is red … only if a fragment whose certificate fails is given a verdict |
| 74 | D21 (b) | C.4 | C-BUDGET: holds; otherwise C-BUDGET is red, the checker exits 3, and `decide` gives VOID | C-BUDGET: holds: every fragment over its budget is recorded `out_of_scope` and given no verdict. An `out_of_scope` B-P gives B-VOID … |
| 75 | D21 (b) | C.4 |   - The checker must record `out_of_scope`, set C-BUDGET red and exit 3, and `decide` must give VOID, with no… |   - The checker must record `out_of_scope`, give the fragment no verdict, and raise no exception. With the fragm… |
| 76 | D19 (0)(c) | C.4 | (none; added after M-FACTOR) | - **M-RAY** (D19 (0)(c); invalid by construction): in B-RAY-P's certificate, one removal multiplier altered; … |
| 77 | D21 (b) | C.4 | (none; added after M-MODE) | - **S1-BIND** (D21 (b); C.8 item 3). `verdict`'s S1 binding, on synthetic records built in memory. … |
| 78 | D21 (b) | C.4 |     - a `git` subcommand outside the frozen list. |     - a `git` subcommand outside the frozen list;     - **ZIP-1 to ZIP-3** (D21 (b)): `zipfile.ZipFile(io.BytesIO(b), "w")`; … |
| 79 | D21 (b) | C.5 |     - the default prints canonical-JSON `measurements.json`, exiting 0 when the output is complete and every cont… |     - the default prints canonical-JSON `measurements.json`, exiting 0 when the output is complete. A red decisive-… |
| 80 | D21 (b) | C.5 | **(a) Imports.** Only `import X`, with `X` in the frozen list `ast`, `fractions`, `hashlib`, `json`, `os.path`, … | **(a) Imports.** Only `import X`, with `X` in the frozen list `ast`, `fractions`, `hashlib`, `io`, `json`, … `zipfile` … |
| 81 | D21 (b) | C.5 |           - `tempfile.TemporaryDirectory`; |           - `tempfile.TemporaryDirectory`;           - `io.BytesIO` and `zipfile.ZipFile` (D21 (b)). A `ZipFile` is co… |
| 82 | D21 (b); r14b N11 | C.5 |             - `actions/runs/{DEC}/artifacts`; |             - `actions/runs/{DEC}/artifacts`;             - `actions/artifacts/{DEC}/zip` (D21 (b)), read by `verdict` and, for S1's measurements artifact, by `derive-run` run on S1's run before `E` is committed… |
| 83 | D21 (b) | C.6 | - any `out_of_scope`; | (removed) |
| 84 | D21 (b) | C.6 | - at `E`, a failed control, a checker outcome, a replay mismatch, or a `verdict` VOID arising from the checker; | - at `E`, a red fixture-mode control, a checker outcome, a replay mismatch, a failed S1 binding, or a `verdict` VOID… |
| 85 | D21 (b) | C.6 | Undecidable cases receive the preregistered VOID. | Undecidable cases receive the preregistered VOID of their own test (D21 (b)), or are reported (D19 (ii)(b), (iii)(c)). |
| 86 | r14a N11 | C.2 | - A4. `actions/upload-artifact@v4` of `fixtures.json`, on every event, with `if-no-files-found: error` and | - A4. `actions/upload-artifact@v4` of `fixtures.json` as the artifact `arp2-qc21-fixtures`, on every event, with… |
| 87 | r14a N11 | C.2 | - A6. `actions/upload-artifact@v4` of `stress.json`, on every event, with `if-no-files-found: error` and | - A6. `actions/upload-artifact@v4` of `stress.json` as the artifact `arp2-qc21-stress`, on every event, with… |
| 88 | r14a N11 | C.2 | - B5. `actions/upload-artifact@v4` of `measurements.json`, with `if-no-files-found: error` and `retention-days: 90`. | - B5. `actions/upload-artifact@v4` of `measurements.json` as the artifact `arp2-qc21-measurements`, with… |
| 89 | r14a N3; D21 (b) | C.3 | - **`verdict`.** It prints `VERDICT <token>` only when all of the following hold. Otherwise it prints `VERDICT VOID`… | - **`verdict`.** It prints the token line `VERDICT <P token> <B token> <C token> level <n>` (the three tokens, VOID… |
| 90 | r14a N3 | C.3 |   - the note's token line equals the token. |   - the note's token line equals this token line. |
| 91 | r14a N12; SG-1 | C.6 |   change to `P_max`, `B_max`, `W_max`, the caps, `timeout-minutes` or the stress pin, and any addition of a fragment, | … change to `P_max`, `B_max`, `W_max`, `P_max^BP`, `B_max^BP`, `W_max^BP`, `S_max`, the caps (B-P's included),… |
| 92 | r14a, via ARP-3-QC22 r14 (R13-N10) | C.4 | \| **C-SYM** \| on the fixtures, the effect-facet LP gives the same verdict \| | \| **C-SYM** \| on the fixtures, the effect-facet LP gives the same verdict. **The effect-facet LP** … is step 4 with the roles of `a_p` and `b_e` exchanged … |
| 93 | r14a, via ARP-3-QC22 r14 (R13-N17) | C.4 | C-INDEP: … `int`, `tuple`, `list`, `dict`, `set`, `isinstance`, and (iv) … | C-INDEP: … `int`, `tuple`, `list`, `dict`, `isinstance`, and (iv) … |
| 94 | r14a, via ARP-3-QC22 r14 (R13-N17) | C.4 |     - a `__*__` attribute walk. |     - a `__*__` attribute walk;     - a call to `set` or `frozenset`, a set display or a set comprehension. |
| 95 | r14a, via ARP-3-QC22 r14 (R13-N6) | C.4 |       `ZipFile`; `zipfile.ZipFile(<a path>)`. |       `ZipFile`; `zipfile.ZipFile(<a path>)`;     - a `gh` path f-string with a formatted value that is not an `a_ok(...)` call. |
| 96 | r14a, via ARP-3-QC22 r14 (R13-N17) | C.5 |   - The solver's functions are named `s_*` and the verifier's `v_*` (C-INDEP). | (inserted before it)   - **No sets.** `-I` leaves string-hash randomization on, … |
| 97 | r14a, via ARP-3-QC22 r14 (R13-N17) | C.5 |         - module-wide, it uses no `getattr`, … | (inserted before it)         - no call to `set` or `frozenset`, no set display and no set comprehension occurs; |
| 98 | r14a, via ARP-3-QC22 r14 (R13-N6) | C.5 |           - Every list element is a string literal, or a call to the frozen validator `a_ok(x)`. |           - Every list element is a string literal, a call to the frozen validator `a_ok(x)`, or, as `gh`'s path only (rule (g)), an f-string … |
| 99 | r14b R14A-B1, via ARP-3-QC22 r14 (R13-B4) | C.5 |             - `git/trees/{HEX40}?recursive=1`; | (inserted before it)             - `issues/comments/{DEC}` (ARP-3-QC22 r14, R13-B4; re-review R14A-B1), read by `verdict` and `e-entry` … |
| 100 | r14b R14A-B1, r14a-N3 | C.5 |   - **Modes:** `check <commit> --freeze F [--stage S1\|E\|W]`, … `derive-run`, `order`, `verdict`, `--self-test`. |   - **Modes:** … `derive-run`, `order`, `verdict`, `e-entry <E> <comment id>`     (C.8 item 9), `--self-test`. |
| 101 | r14b R14A-B1, via ARP-3-QC22 r14 (R13-B4) | C.3 |     - No comment is reused. | (inserted after it)     - The comment is read through `GET issues/comments/{DEC}` (ARP-3-QC22 r14, R13-B4; … |
| 102 | r14b r14a-N1; R8 | C.3 | … That ambiguity is closed only by the owner's     ratification at the designation of `E` (below). An entry not ratified there makes `verdict` print VOID. | … That ambiguity is closed only by the owner's     ratification: at the designation of `E` for the entries committed at `E`, and for the `E` dispatch's own entry as     precondition 2's R8 provides … |
| 103 | r14b r14a-N1; R8 | C.3 |   - the owner's designation of `E` ratifies, by `order.json`'s sha256, the run list and every approval entry, quoted … |   - the owner's designation of `E` ratifies, by `order.json`'s sha256, the run list and every approval entry     committed at `E` (C.8 item 9), quoted …; the `E` dispatch's own entry is ratified as precondition 2's R8 provides … |
| 104 | r14b r14a-N2; R2 | C.3 |     (B6 included at `E`), and every step of job A is `success` (A7 and A10 included). … |     (B6 included at `E`), and every step of job A is `success` (A7 and A10 included; A3 included, so that a red     fixture-mode control fails this condition: draft default, pending owner ruling R2 …). … |
| 105 | r14b R14A-B1, via ARP-3-QC22 r14 (R13-B4) | C.3 |   - in attempt 1 of the runs at S1 and `E`, … | (inserted before it)   - every approval entry holds, the `E` dispatch's included (ARP-3-QC22 r14, R13-B4; re-review     R14A-B1) … |
| 106 | r14b r14a-N2; R6 | C.3 |     JSON without `parameters.dispatch_sha` (D21 (b); C.8 item 3). A missing or unreadable artifact fails it; |     JSON without `parameters.dispatch_sha` (D21 (b); C.8 item 3). A missing or unreadable artifact fails it (an     expired or deleted one: draft default, pending owner ruling R6 …); |
| 107 | r14b r14a-N2; R2 | C.6 | - at S1, any checker outcome other than exit 0 with complete output; | - at S1, any checker outcome other than exit 0 with complete output (A3's exit 3 on a red fixture-mode   control included: draft default, pending owner ruling R2 …); |
| 108 | r14b r14a-N2; R2 | C.6 | - at `E`, a red fixture-mode control, a checker outcome, … | - at `E`, a red fixture-mode control (draft default, pending owner ruling R2, precondition 2), a checker outcome, … |
| 109 | r14c r14b-N1, via ARP-3-QC22 r14a (R14-N10) | C.2 | `python3 -I -S -B <record dir>/controls.py fixture-mode-check "$RUNNER_TEMP/arp2-qc21/fixtures.json"`. | … fixture-mode-check "$RUNNER_TEMP/arp2-qc21/fixtures.json"`, with   `if: ${{ always() }}` …   - It runs whether or not A3 succeeded. … |
| 110 | r14c r14b-N1 | C.2 | **Common.** No step continues on error, masks a status or installs a package. Every interpreter the splice starts | **Common.** No step continues on error, masks a status or installs a package. A3b's `if: ${{ always() }}` runs it after a failed A3 and masks nothing … |
| 111 | r14c r14b-N9, via ARP-3-QC22 r14a (R14-Rb2); R10 | C.2 | - **Its record.** The final capture's record (structured JSON with its sha256) is posted on the round PR. It is   provenance (§A.42 item 2). | - **Its record.** … is posted on the round PR. The claim   that no unapproved checker-bearing run occurred between `E`'s capture and landing uses it, … the owner's (precondition 2, R10, pending; … |
| 112 | r14c r14b-N9, via ARP-3-QC22 r14a (R14-N2) | C.3 | - **Binding the approval to the run (re-anchored on the owner's quoted commit; E5).** All of these must hold: … - the measurements' `parameters.dispatch_sha` equals the same commit; | - **Binding the approval to the run (re-anchored on the owner's quoted commit; E5).** For the run that attests at     each stage, all of these must hold … - at S1, the committed measurements' `parameters.dispatch_sha` equals S1 (at `E`, B3's `success` binds the       input); … - **The entry of a host-VOID run** that a retake replaces holds … |
| 113 | r14c R14B-B1, via ARP-3-QC22 r14 (R13-B4) | C.3 | - **`order.json`.** `F`'s designation precedes the first execution run. | - **`order.json`.** `F`'s designation precedes the first execution run. The owner's designation comment is read   through `GET issues/comments/{DEC}`, its id given as an argument; … |
| 114 | r14c r14b-N9, via ARP-3-QC22 r14a (R14-Rb2) | C.3 | The writer's record is that no draft of the scripts or the splice has been pushed anywhere (PLAN), so the       residual is empty unless that record is wrong. | The residual is empty if no such draft was pushed before `D`, which is the writer's statement and is not … |
| 115 | r14c r14b-N9, via ARP-3-QC22 r14a (R14-Rb2) | C.3 | That is about 770 calls for set (1) today (r10 review §3, H11–H15), … | An estimate, which no condition uses, is about 770 calls for set (1) (r10 review §3, H11–H15), … |
| 116 | r14c r14b-N9, via ARP-3-QC22 r14a (R14-N2) | C.3 |   - every approval entry holds, the `E` dispatch's included (ARP-3-QC22 r14, R13-B4; re-review R14A-B1): each … |   - every approval entry holds as stated for its run, the run that attests at its stage or a host-VOID run a retake     replaced, the entries `verdict` builds for the dispatches at `E` included … |
| 117 | r14c r14b-N1, via ARP-3-QC22 r14a (R14-N10) | C.4 |     - the marker A10;     - the marker A3b. |     - the marker A10;     - the marker A3b, or its `if:` … |
| 118 | r14c R14B-B1, via ARP-3-QC22 r14 (R13-B4) and r14a (R14-N2) | C.4 | (none; added after S1-BIND) | - **APPROVAL-ENTRIES** (ARP-3-QC22 r14, R13-B4, and r14a, R14-N2; re-review R14B-B1). `order`, `verdict` and   `e-entry` on synthetic records built in memory. … |
| 119 | r14c r14b-N9, via ARP-3-QC22 r14a (R14-Rb2) | C.5 | - **Why.** On git 2.43.0, `git rev-parse --end-of-options HEAD` without `--verify` exits 0 … | - **Why.** The rule ties each admitted form to one object name. … |
| 120 | r14c R14B-B1 | C.5 | read by `verdict` and `e-entry`               (C.3; C.8 item 9); | read by `order`, `verdict` and `e-entry`               (C.3; C.8 item 9; re-review R14B-B1); |
| 121 | r14c r14b-N6 | C.5 | `derive-run`, `order` and `verdict` call (C.8 item 8). | `derive-run`, `order`, `verdict` and `e-entry` call (C.8 item 8;           re-review r14b-N6). |
| 122 | r14c r14b-N2 | C.5 | - Its code imports only `tools/v3_verifier.py`, whose blob the inputs pin. | - Its code imports only `tools/v3_verifier.py`, whose blob the inputs pin (*Inputs*, row V3V). Before it … |
| 123 | r14c r14b-N9, via ARP-3-QC22 r14a (its §5) | C.5 | exercised by M-GUARD (BYP-1 to BYP-18).** | exercised by M-GUARD (BYP-1 to BYP-21, BYP-23 to BYP-26, ZIP-1         to ZIP-3 and the unnumbered variants; ARP-3-QC22 r14a).** |
| 124 | r14c r14b-N1 | C.5 |       - the markers A10 and A3b; |       - the markers A10 and A3b, with A3b's `if:` (re-review r14b-N1); |
| 125 | r14c r14b-N1 | C.5 |       - the marker A10;       - the marker A3b;     - DS: inputs and drift; |       - the marker A10;       - the marker A3b, or its `if:` (re-review r14b-N1);     - DS: inputs and drift; |
| 126 | r14c, via the ARP-3-QC22 r14a review (Rc1) | C.3 |   - A3b's conclusion is `success`, so A3's output had `mode: "fixture"` with the synthetic placeholders. |   - A3 is absent or `skipped`, so it never started … or A3b's conclusion is `success` … - **Residual (named; ARP-3-QC22 r14a review, Rc1).** An A3 that started and left no fixture-mode … |
| 127 | r14d R14C-B1 | C.3 | `order.json` records its id, author and times | owner/OWNER and full-F designation required; id, author, association, times and quoted words recorded |
| 128 | r14d r14c-N1 to N3 | C.3 | no-unapproved-F1 rule and its nested Residual | explicit attempt_status field from the attempt API; unfinished attempts fail capture for retry; completed-attempt rule; Residual outside conjunction; checker-bearing executor precondition and explicit local-run authorization boundary |
| 129 | r14d R14C-B1, r14c-N4 | C.4 | APPROVAL-ENTRIES designation and host-VOID cases | wrong/missing F, wrong owner/association, first-run selection across events, and false host-VOID cases must fail |
| 130 | r14d R14D-B1 | C.4; C.8 item 12 | equality shows no fixture perturbation; C-STATELESS detects shared state | comparison is with the supplied copy; inference about the actual confirmation output requires authenticity, which the procedure does not establish; C.7 limitation applies |
| 131 | r15 owner R8, c.6778994857 | C.3; C.4; C.8 item 9 | R8 default/separate ratification comment pending | approved alternative: E designation quotes order.json and every E-entry digest; no separate ratification comment |
| 132 | r15 owner R10, c.6778994857 | C.2; C.3; C.8; tables | host-time claims/disposition pending | checks remain mandatory landing conditions, with no enduring assertion that unretained host-time checks passed |
| 133 | r15 implementation read-only ZIP enforcement | C.5 control B | only namelist/read on an in-memory ZipFile | resource is locally with-bound; no alias/rebinding/escape; only namelist() and literal measurements.json read |
| 134 | r15 owner R1–R10, c.6778994857 | precondition 2; C.8 item 2 | owner choices and S_max pending | selected rules applied; initial S_max 100000; measured budgets, pins and other pre-F gates remain pending |
| 135 | r15 bounded implementation | C.5, malformed-data handling | callable whitelist only | unchanged callable whitelist; explicit non-call string type and exception-handler names |
| 136 | r15 bounded implementation | C.5, identity representation | pin locations and E note identity implicit | preregistration pin block and externally designated E identity avoid self-referential hashes; entry digest bytes explicit |
| 137 | r15 bounded implementation | C.5, provenance/CLI | implementation draft and capture-input format implicit | provenance-only SOURCE_BASE is bound before execution; validated UTC capture bound is an explicit CLI/config input |

**Typographic edits, also logged (r11-N2).**
- In C.2, the Job B bullet's first sentence is re-wrapped (whitespace only).
- In C.2, the headings "### Job A" and "### Job B" are demoted to "####".
- The copied headings "## Scripts" (C.5) and "## Stop rule (halt-only)" (C.6) are dropped; this appendix's own C.5
  and C.6 headings replace them.

**After the edits:**
- No copied control, `verdict` condition, gate test, allowlist template or adaptation row refers to an Environment,
  `approvals` or `deployments`.
- Three passages still mention the Environment only to state the waiver.
- `pending_deployments` remains in M-GUARD and control B as a **forbidden** `POST` route.

**Adaptation table (frozen).** In the copied text, each QC22-specific term reads as follows. "Not applicable" means the
passage has no force in this round.

| copied term | meaning in ARP-2-QC21 |
| --- | --- |
| F1, the F1 family, F1-family fragments, F1-dependent output, "computes F1" | this round's decisive families: P's construction-B arm classes `Adm_A`, `Adm_B` and the ablations; REP-INV on decisive data; B-P, construction A of B, B-C; C's test-rule orbits, ablations and C-A runs |
| "the F1 builder" (`qc21_check.py`'s name rules, refusal, instrumented counter, `t_builder_refuses`) | the single gated entry `s_decisive`, through which every decisive builder is called (preregistration, *Decisive builders and the guard*). Each name rule stated for "the builder" applies to `s_decisive`. Each registered builder carries the same refusal as its first statement, and the instrumented counter counts calls to every registered builder |
| `G_SM`, P★ | the dynamics of this round: P's class-N step with P3 arming; C's `Φ_g` |
| F1+R-G, F1+R-U′, F1+R-Uc, F1+R-Y, F1+R-S, R-S and its options (i)–(iii), SF-3, SF-3n, RS; INT, IS-SIZE, IS-PSTAR, IS-RULE, C-ISO-NAME, CC-OFF, the access fields, `blocks`, `lists_sha256`; M-EVAL, M-SWAP | not applicable: QC22's completions, instance and access machinery |
| SF-1, SF-2 (stress fixtures) | this round's stress fixtures: frozen synthetic classical fragments of B-P's size (32 preparations, the nine settings of `Acc(B-P)`) and of B-C's maximal size (at most 91 preparations, three binary settings). Generators and seeds: C.8 item 2. SF-1's three instances are the inputs of the stress test ST-BP (D19 (i)(a)) |
| CC-F0; "the frozen fixtures and their completions"; POS-1, POS-2, NEG-1, NEG-2, GBIT, DUAL, H3, G, X, Q, SW, SW−, X+RU′, Q+RY | this round's B controls B-POS (for POS-1 and the infeasible step-4 role of GBIT, DUAL and H3), B-S4F (for Q+RY's feasible step-4 role at `T > 0`), B-STAB (for NEG-1, POS-2), B-CLASS (for NEG-2), B-REG (for GBIT), B-WAVE, QM-P's restricted fragment, and the copied ZPT and F10. The mutations M-FACET, M-W, M-MODEL, M-SOLVER, M-FACTOR and M-BUDGET run on these, a QC22 fixture name being read as its mapped control. X+RU′'s step-3 role is ZPT's; Q+RY's step-4-feasible role at `T > 0` is B-S4F's (`T = 3`), and F10 carries `T = 0` (r13 item 15) |
| "the 14 terms are 7 fragments × 2 sizes" (timeout test) | B-P under its own budget, and the other decisive fragments under the general budget: B-P's two completions, construction A of B, at most 600 B-C fragments and at most 600 B-C completions. The test's left side is C.8 item 2's, `σ × (W_max^BP + 1203 · W_max + 2·W_fix + W_stress) + t_810` (B-P alone under its own caps and budget: owner-approved R5 default; the term `1203 · W_max`: owner-approved R3 default) |
| "Expected bounds on paper" for F1 and its completions | not applicable |
| schema `arp2-qc21-measurements` v3 (renamed from QC22's) | replaced by this round's schema (C.5a), version 1 |
| C-EVAL | this round's C-DET, and the B-P table builder's self-check against the definition |
| C-INDEP, C-EXACT, C-STATELESS, C-BUDGET, C-CERT, C-NCF, C-SYM, M-GUARD, M-MODE | carried as copied, for this round's checker and controls |
| preconditions 6, 6′, 6″ | C.7 below; this round's precondition 7 |
| A1–A10, B1–B6 | carried with this round's names. A11 and B3b are removed (D12) |
| `T0` | carried: the start of this round's enumeration window, fixed when the round PR is opened (PENDING) |
| fixture mode | builds none of this round's decisive families. It decides every self-test fixture and every fixture-mode control (preregistration, *Control modes*) with the full method and the independent verifier |
| ARP-4 | ARP-3 (the next round in this programme's order) |

### C.1 The exact method (copied verbatim)

**The accessible GPT.**
- Factor `N = A Bᵀ` by exact elimination: rows `a_p ∈ Q^d` and `b_e ∈ Q^d`, with the unit effect included.
- Operational equivalences are the linear relations among the rows. They are certified by the fragment's own reads
  and preparations and by nothing else.

**The decision procedure (frozen).** Each fragment is decided by the first step below that returns a verified
certificate. Every outcome carries a certificate, which the independent verifier checks against the definition.

1. **Effect reduction.** Remove every effect vector that duplicates, or is a positive multiple of, an earlier one in
   the frozen order. The unit effect is kept, and non-extreme effects are not pruned.
2. **Rank fast path (Lemma NC-F).** On the charged configurations `Ω_c`, compute `d`, `r_S` and `r_E` exactly. If
   `d = r_S = r_E`, the fragment is **feasible**, and the certificate is the configuration model: the charged laws
   `μ_p` and the response functions `ξ_e`.
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
   - The formulation was demonstrated by the reviewer (`review/probes2/fastnc2.py`, `fastnc3.py`). Its soundness and
     the completeness of both certificates were checked on paper in `review/REVIEW-ACCESS-r3.md` §4.
5. **Arithmetic and pivoting (frozen tie-breaks; re-review N6).**
   - The tableau is fraction-free: integer rows with a common denominator, and exact integer (Bareiss) pivot updates.
   - **Entering column:** Dantzig's rule, the most negative reduced cost, with ties going to the lowest column index.
   - **Leaving row:** the minimum ratio, with ties going to the lowest basic-variable index.
   - **Anti-cycling:** after 50 consecutive degenerate pivots, Bland's rule applies for the rest of that phase, with
     no return to Dantzig's rule.
   - Pivoting affects speed only. Soundness rests on the verified certificates.
6. **Deterministic budget (re-review B3).** Each fragment, across steps 3 and 4 and all phases, has three budgets:
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
     - every frozen fixture and each of its completions;
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
       a byte comparison) has no design-run record and counts 0 (r11 N6).
     - The test is `σ × (14·W_max + 2·W_fix + W_stress) + t_810 ≤ 1200`, evaluated exactly. 1200 s is ⅓ of
       `timeout-minutes: 60`. `W_fix` appears twice because the fixtures are decided in A3 (and in B4) and again in
       A5. The left side bounds each job separately:
       - job B's work, B4 and B6, is at most `σ × (14·W_max + W_fix) + t_B6`;
       - job A's work, A3 to A9, is at most `σ × (2·W_fix + W_stress) + t_A8 + t_A9`;
       - the sum covers both.
     - `check --freeze` evaluates the inequality from the pinned inputs and fails if it does not hold.
     - The 14 terms are 7 fragments (F1, R-G, R-U′, R-Uc, R-Y, R-S, F0) × 2 sizes. With R-S out of scope there are
       12.
     - `W_fix` is the fixtures' total work (with CC-F0), and `W_stress` the stress fixtures' total work. Both come
       from the design run's `stress.json`.
     - `σ` absorbs the uncounted operations of the stress step (facets, ranks, verifier) proportionally. It is an
       estimate, not a bound. A timeout remains a checker outcome: VOID, with no retake.
     - If the test fails with R-S kept, the R-S decision of precondition 2 is taken before `F`. If it fails without
       R-S, no `F` is requested.
   - **The job timeout is frozen.** `timeout-minutes: 60` on each of the jobs `probes_arp2qc21` and
     `probes_arp2qc21_decisive` (*The workflow edit*). Job B's limit counts from its start, after the approval.

**The independent verifier (re-review B2).** It is a separate function namespace in `qc21_check.py`: every function
whose name begins `v_`. C-INDEP checks it mechanically.
- **Its inputs** are only these:
  - the fragment's charged laws `μ_p`;
  - the read response tables `ξ_e`, as produced by the fragment builder (C-EVAL-checked), not by the solver;
  - the solver's reported `A`, `B` and certificate.
- **It re-derives the table from the definition.** It computes `N(p, e) = Σ_ω μ_p(ω) ξ_e(ω)` itself, checks
  `A Bᵀ = N` exactly, and checks `rank A = rank B = rank N = d` with its own elimination. A wrong factorization fails
  here.
- **Its own facet list.** It re-enumerates the facets of `cone{a_p}` by its own brute force over `(d − 1)`-subsets.
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

**Expected bounds on paper.**
- F1: `d ≤ 6`.
- F1+R-G: `≤ 7`.
- F1+R-U′ and F1+R-Uc: `≤ 8`.
- F1+R-Y: `≤ 10`.
- F1+R-S: at most 16 generators, on a larger `Ω`.

**Stress fixtures (frozen, synthetic, not `G_SM`).** These are classical fragments with F1's preparation structure.
The generator is frozen in `qc21_check.py`: stdlib only, with a 32-bit xorshift whose seeds are part of the pinned
blob.
- **SF-1** (seeds 20261108, 1 and 2). `Ω = F_2⁴`. The four inputs are `Z±, X±` on bits 0–1, with bits 2–3 uniform.
  The herald is `h = (ω_0 ∧ ω_2) ⊕ ω_1 ⊕ ω_3`. That gives 8 conditional preparations and 36 seeded boolean reads.
  This is F1's size.
- **SF-2.** SF-1 with `Y±` inputs added: 12 preparations, F1+R-Y's size.
- **SF-3.** `Ω = F_2⁶`, 8 inputs × herald, giving 16 preparations, and 36 seeded reads. This is F1+R-S's size.
- **SF-3n.** Defined only if R-S is narrowed before `F` (precondition 2).

**`--stress` and `stress.json` (§A.44).**
- `qc21_check.py --stress` decides every kept stress fixture, every frozen fixture with its completions, and CC-F0. It
  never builds the F1 family. It writes canonical-JSON `stress.json`, schema `arp2-qc21-stress` v2. For each
  fragment the schema records the verdict, the deciding step, the pivots, the maximum bits, the work and the
  certificate-verified flag. It also records the totals `W_fix` and `W_stress`. There is no timestamp. It is run with
  no budget, apart from the job timeout.
- The workflow runs it on every event and uploads `stress.json` as an artifact on every event, so the design run's
  figures are read through the artifacts API.
- **The marker step** "ARP-2-QC21 stress output equals the pinned sha256" runs `controls.py stress-check`.
  - It exits 0 iff `stress.json` meets schema v2, every fragment in it is certificate-verified, and its sha256 equals
    the frozen pin.
  - On the design tree the last condition is replaced by recording (no pin exists yet). The schema and
    certificate conditions are still enforced there (r4 N6).
  - At S1 and `E` its conclusion is a step conclusion read by `verdict`.
- **The pin is linked to the artifact.** `controls.py check --freeze` verifies that the pinned `stress.json` sha256
  equals the `artifact_sha256` of the stress artifact recorded in `design-run.json` for the design run named there
  (r4 N6).

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


### C.2 The workflow edit (copied; D12 edits applied)

**Two jobs.** The splice adds two jobs.
- **Job A** (key `probes_arp2qc21`) runs on every event and never computes F1.
- **Job B** (key `probes_arp2qc21_decisive`) is the only job that can compute F1. With the Environment gate waived for this
  round (c.6735159962), its execution is authorized by the owner's approval entry, and an unauthorized run is detected, not
  prevented.

They are split so that job A's fixture mode runs on every event, while job B's decisive mode is reachable only
through its job-level `if:` and the in-tree keys. Both jobs go after the last job before the `probes` aggregate at
`D` (anchor PENDING).

**`workflow_dispatch` inputs (frozen addition to `on:`).** Two inputs, both optional, so a dispatch without them
behaves as before:
- `arp2qc21_decisive`, a boolean, default `false`;
- `arp2qc21_sha`, a string, default empty, carrying the approved commit's full id.

**Aggregate.**
- Both jobs are added to the aggregate's `needs`, with `ARP2QC21_RESULT: ${{ needs.probes_arp2qc21.result }}` and
  `ARP2QC21D_RESULT: ${{ needs.probes_arp2qc21_decisive.result }}` in `env`.
- After the last round's lines (anchors PENDING), the aggregate gets:
  - `echo` lines for both results;
  - `test "${ARP2QC21_RESULT}" = success`;
  - `test "${ARP2QC21D_RESULT}" = success -o "${ARP2QC21D_RESULT}" = skipped`.
- Job B is skipped on every run that is not a first-attempt dispatch with the decisive input. That keeps every other run green, later
  rounds' `F` and `E` dispatches included. Whether job B succeeded at S1 and `E` is checked by `verdict` from the
  jobs API, not by the aggregate.

#### Job A — `probes_arp2qc21`, display name `Numerical probes / ARP-2-QC21 fixtures and stress` (frozen)

`timeout-minutes: 60`. No `environment:`. Its steps:
- A1. checkout with `fetch-depth: 0`.
- A2. `actions/setup-python@v5` with `python-version: '3.11'`.
- A3. **"ARP-2-QC21 fixture decision"**:
  `mkdir -p "$RUNNER_TEMP/arp2-qc21" && python3 -I -S -B <record dir>/qc21_check.py --event fixture > "$RUNNER_TEMP/arp2-qc21/fixtures.json"`.
  - The literal `--event fixture` means that job A runs fixture mode on every event, whatever the checker's other
    keys say.
  - This is the output used by 6′ and by C-STATELESS.
- A3b. **"ARP-2-QC21 fixture output is fixture mode"** (a marker; §A.44; r13 item 8):
  `python3 -I -S -B <record dir>/controls.py fixture-mode-check "$RUNNER_TEMP/arp2-qc21/fixtures.json"`, with
  `if: ${{ always() }}` (ARP-3-QC22 r14a, R14-N10; re-review r14b-N1).
  - It runs whether or not A3 succeeded. A red A3 whose output is complete fixture-mode output, a fixture mismatch
    for example, still gives A3b `success`; a missing or non-fixture output gives `failure`.
  - It exits 0 iff the file parses as schema `arp2-qc21-measurements` v1 with `mode: "fixture"`, `complete: false`
    and every decisive field the synthetic placeholder, and 3 otherwise.
  - Its conclusion is the structured record of A3's mode that the no-unapproved-F1 rule reads (*Runs, evidence,
    approvals*).
- A4. `actions/upload-artifact@v4` of `fixtures.json` as the artifact `arp2-qc21-fixtures`, on every event, with `if-no-files-found: error` and
  `retention-days: 90`.
- A5. **"ARP-2-QC21 stress"**: `python3 -I -S -B <record dir>/qc21_check.py --stress > "$RUNNER_TEMP/arp2-qc21/stress.json"`.
- A6. `actions/upload-artifact@v4` of `stress.json` as the artifact `arp2-qc21-stress`, on every event, with `if-no-files-found: error` and
  `retention-days: 90`.
- A7. **"ARP-2-QC21 stress output equals the pinned sha256"**:
  `python3 -I -S -B <record dir>/controls.py stress-check "$RUNNER_TEMP/arp2-qc21/stress.json"`.
- A8. `python3 -I -S -B <record dir>/qc21_check.py --self-test`.
- A9. `python3 -I -S -B <record dir>/controls.py --self-test`.
- A10. **"ARP-2-QC21 receipt absent"** (a marker; r9 N6): `true`, with `if: ${{ hashFiles('verification/receipts/ARP-2-QC21.json') == '' }}`.
  - It is `success` on the design run, at 6′, at S1 and at `E`.
  - It is `skipped` on any tree carrying the receipt.
  - It is recorded in `design-run.json` and `confirmation-run.json`, and `check --freeze` requires `success`.

#### Job B — `probes_arp2qc21_decisive`, display name `Numerical probes / ARP-2-QC21 exact decision (gated)` (frozen)

`timeout-minutes: 60`.

**Its condition, `if:`** (job level):

`${{ github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && inputs.arp2qc21_decisive == true }}`.

**Its `env:`** (job level): `ARP2QC21_SHA: ${{ inputs.arp2qc21_sha }}`. The input reaches the shell only as this
variable, never by interpolation into a `run:` line.

Its steps:
- B1. checkout with `fetch-depth: 0`.
- B2. `actions/setup-python@v5` with `python-version: '3.11'`.
- B3. **"ARP-2-QC21 approved commit and receipt"**:
  `test "$GITHUB_SHA" = "$ARP2QC21_SHA" && test "$GITHUB_REF" = refs/heads/research/arp2-qc21-20261108 && test ! -e verification/receipts/ARP-2-QC21.json`.
  - It fails unless the run's commit is exactly the commit named in the dispatch input, the run's ref is the round
    branch (the **ref key**; re-review R10-B5), and the tree carries no receipt.
  - B3 stops a run whose commit differs from the input, or whose ref is not the round branch. A run whose owner
    approval names a commit other than its own is not stopped by B3. It is detected afterwards by the approval binding
    (*Runs, evidence, approvals*), and the round halts VOID.
- B4. **"ARP-2-QC21 exact decision"**:
  `mkdir -p "$RUNNER_TEMP/arp2-qc21" && python3 -I -S -B <record dir>/qc21_check.py --event "${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && github.ref == 'refs/heads/research/arp2-qc21-20261108' && hashFiles('verification/receipts/ARP-2-QC21.json') == '') && 'workflow_dispatch' || 'closed-or-other' }}" --dispatch-sha "$ARP2QC21_SHA" > "$RUNNER_TEMP/arp2-qc21/measurements.json"`.
  - **The in-tree keys:** the event key, the attempt key, the ref key, the receipt key, and the checker's four keys
    (`--event`, `GITHUB_EVENT_NAME`, `GITHUB_RUN_ATTEMPT`, `GITHUB_REF`). The gated entry and every decisive builder
    also carry their own refusal check (Appendix C.5).
  - `--dispatch-sha` records the input, after the checker's own 40-hex check (exit 4 otherwise; r11 N3), as
    `parameters.dispatch_sha` in `measurements.json`. It selects nothing.
  - **Fixture mode evaluates nothing of the F1 family under `G_SM`:** no F1-family table, no access fields, no INT,
    no IS-SIZE, and no C-EVAL on F1's charged configurations. C-EVAL's self-test version uses P★ and frozen
    synthetic configurations.
  - A missing `--event` makes the checker refuse, with exit 4, and the output's `mode` is `"decisive"` or
    `"fixture"`.
- B5. `actions/upload-artifact@v4` of `measurements.json` as the artifact `arp2-qc21-measurements`, with `if-no-files-found: error` and `retention-days: 90`.
- B6. `python3 -I -S -B <record dir>/controls.py replay "$RUNNER_TEMP/arp2-qc21/measurements.json"`, against the
  committed `<record dir>/evidence/measurements.json` (the comparison of C.8 item 3), with
  `if: ${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && github.ref == 'refs/heads/research/arp2-qc21-20261108' && hashFiles('verification/receipts/ARP-2-QC21.json') == '') }}`.
  It replays exactly when B4 ran in decisive mode.

**Common.** No step continues on error, masks a status or installs a package. A3b's `if: ${{ always() }}` runs it
after a failed A3 and masks nothing: A3's conclusion, and job A's, stay `failure` (re-review r14b-N1). Every
interpreter the splice starts (A3, A3b, A5, A7, A8, A9, B4, B6) is `python3 -I -S -B`, so no `.pth` or other startup
file runs in any step. Both scripts are stdlib-only. `pull_request` and `push` runs never reach
job B: its job-level `if:` is false for them, so the job is `skipped` by the job-level `if:` (verified at the design run,
precondition 6).

**Enforcement, in order (owner decision c.6735159962; re-review R10-B5).** The Environment gate is waived for this
round. Unauthorized computation is **detected and rejected, not prevented**.
1. **The in-tree keys (prevention for runs of the frozen splice only).** These are:
   - job B's job-level `if:`;
   - B3, with the ref key;
   - the workflow keys in B4 and B6, with the ref key;
   - the checker's four keys, and the refusal checks of the gated entry and of every decisive builder;
   - controls W and B, with M-GUARD.

   They make a run of the frozen splice and the pinned checker compute nothing decisive unless it is a first-attempt
   dispatch with the decisive input, on the round branch, at the input commit, with no receipt in the tree. They do not
   establish that such a dispatch was authorized. Control B's claims are scoped to exactly what it checks (*Scripts*).
2. **Detection: the enumeration, the approval binding, the ref-move check and VOID.** The enumeration (*Runs,
   evidence, approvals*) catches, up to the final capture, every run that carries the pinned checker blob or the frozen
   job or step names, under **any** event:
   - a dispatch: whole history;
   - any other event: from `T0`.

   Any such run that is not an approved or gate-test entry, and is not a recorded fixture-mode run, is a violation, and
   the round halts VOID. This holds even if the run passed the in-tree keys. Whether a dispatch was owner-approved is
   detected by the approval binding; it is not prevented. The limits of detection are stated in the preregistration's
   *Scope of authorization and detection*.

**References to steps elsewhere in this file.**
- "Step 3" means B4 (the decisive decision) where a decisive run is meant, and A3 where fixture output is meant.
  "Step 8" means B6.
- "Steps 5, 7" mean A5 and A7; "steps 8–10" mean B6, A8 and A9, and `t_810` sums A8 and A9 (B6 counts 0); "step 11" means A10.
- The host-VOID rule and the run-at-a-stage rules concern job B.

**Which steps can compute the F1 family (re-review r6 B1, r9 B1, N7).**
- **B4**, only when all of these hold together:
  - job B's condition: a dispatch, attempt 1, `arp2qc21_decisive` true;
  - B3: the run's commit equals the dispatch input, the ref is the round branch, and the tree has no receipt;
  - the workflow keys in B4's expression;
  - the checker's four keys;
  - the gated entry's and each decisive builder's own refusal checks pass.
- **B6** runs only under the same workflow keys, and compares canonical JSON only (C.8 item 3).
- **A3** runs fixture mode by its literal `--event fixture`, and A3b records that mode as a step conclusion.
- **A5** (`--stress`) decides only the stress fixtures, the frozen fixtures and CC-F0.
- **A3b, A7, A8, A9 and A10** compute nothing of F1. Control B's name rule and the builder's refusal guard this.

**Scope of this guarantee (N7; r10 N2).** No run of the frozen splice and the pinned checker, at any commit, computes
F1 or any F1-dependent output unless both of these hold:
- it is a first-attempt dispatch with the decisive input, on the round branch, whose commit equals the input;
- the tree carries no receipt.

Whether such a dispatch was owner-approved is **detected** by the enumeration against the approval entries, within
the audit window; it is not prevented.

Two things are outside every in-tree mechanism:
- a modified workflow, or a modified checker, on another branch;
- a local run of the public code, which is public from S1's push.

For the first, the enumeration detects every run that carries the pinned blob or the frozen names, under any event,
up to the final capture (*Enforcement*, item 3). A modified checker with a different blob, renamed jobs and steps,
and a local run are not attributable from host records. The claim that F1 was computed once, under approval, is
scoped to the pinned checker accordingly.

**No automatic replay.**
- B6 runs only under the workflow keys. At `E` the only replay is the owner-approved `E` dispatch.
- `replay` recomputes nothing: it reads the fresh B4 output and the committed file, and compares them as canonical JSON with `parameters.dispatch_sha`
  removed from both (r7 N2; C.8 item 3).
- In a dispatch the decisive computation is B4's alone, which the timeout test's `14·W_max` term covers.

**After merging to `main` (owner's restated requirement 3; c.6735159962).**
- **On `main`.** A dispatch with `arp2qc21_decisive` true is refused by B3's ref key and receipt key, and B4's ref and
  receipt keys select fixture mode. A push or a dispatch without the input skips job B, and job A is green, so later
  rounds' `F` and `E` attestations are unaffected.
- **At pre-`Q` round commits** (S1, `E`, a `Λ`). An unapproved dispatch on the round branch before `Q` runs, and is
  **detected** by the enumeration (VOID). A dispatch on any other branch fails B3's ref key, and B4's ref key selects
  fixture mode, so it computes nothing decisive.
- **After `Q`.** The round branch's head carries the receipt, so B3's and B4's receipt keys refuse there too. The
  residual is a force-move of the round branch to a pre-`Q` commit, a destructive ref movement that §A.43 bars without
  owner authorization. It is visible in `GET repos/amaybaum/incompleteness/activity`, which every capture reads (*Runs,
  evidence, approvals*), but a force-move after the final capture is not read by this round.
- **Re-establishing the claim later (§A.42 item 7)** is a dispatch at `E`, made deliberately, with its own recorded
  owner approval. It lies outside this round and changes no token.
- **What remains.** After the final capture no enumeration runs. A modified workflow on another branch after that
  point is neither prevented nor detected by this round. This is the scope limit stated above. The decisive output is
  public from `E`, and the landed record is protected by the receipt's immutability (`G13`).

**The window between `E`'s capture and `Q`'s push.** Reconciliation commits (`Λ`) carry no receipt.
- **A dispatch on one** fails B3's ref key unless it is on the round branch. On the round branch it runs, and an
  unapproved one is **detected** by the final capture (VOID).
- **Final capture.** `verdict`'s capture, and a final capture `controls.py order --final` taken immediately before the
  round PR lands, both enumerate to their capture time.
- **Its record.** The final capture's structured record and sha256 are posted on the round PR as provenance.
  Under approved R10 narrowing, this is only a condition of landing: the round may land only if the final
  capture passes. The enduring record does not state it passed or claim no unapproved checker-bearing run
  occurred between `E`'s capture and landing. No unretained host-time content is used as scientific support.
- **Violations.** An unapproved checker-bearing run in either capture is a violation. The round does not land, and the
  owner is told that it is VOID. This is a mandatory operational landing condition; R10 does not waive it
  or turn it into an enduring claim that the unretained final-capture check passed.

**Cost after landing (r7 N3; r9 B1).**
- Every later pull request, push and ordinary dispatch on the repository runs job A, costing about the design run's
  measured job-A time.
- Job B is skipped and costs nothing.
- Any further change belongs to a successor change outside the round (§A.40).

**A latent route (r7 N4).** No `workflow_call` trigger exists in `verify.yml`. Adding one would let a caller's
`workflow_dispatch` reach job B's condition as `github.event_name`, so it would be a route into decisive mode. That
route is ungated. Any such change after landing is outside the round and must account for this guard.

**Design, confirmation, S1 and `E` trees.** Control W makes the workflow identical across all four.
- **The design run's tree** equals S1's apart from the record files. Its job B is `skipped`. Its step 7 records rather than compares, because
  the preregistration's stress pin is still an unbackticked `PENDING` field there. `stress-check` reads the pin from
  the tree and enforces the schema and certificates in either case.
- **The confirmation run (6′)** is the exact S1 tree, apart from the record files listed in precondition 6′. Its
  `verify.yml` is byte-equal to the frozen splice, and its step 7 compares against the final pin.
- **At S1 and `E`** the tree is exactly as frozen.


### C.3 Runs, evidence, approvals (copied; D12 edits applied)


- **The run at a stage.** The `workflow_dispatch` run of `verify.yml` whose `head_sha` is that stage's commit, dispatched
  with `arp2qc21_decisive` true and `arp2qc21_sha` equal to that commit, at attempt 1. It is read by `derive-run` from
  the runs and jobs APIs (every page). `artifact_sha256` comes from the artifacts API, never from a log (§A.44).
- **Approval entries, keyed on `(run_id, run_attempt)` (re-review r7 B1, r9 B4(a); c.6735159962).** Each decisive
  dispatch (S1, `E`, or a retake after a host VOID as defined below) has its own entry:
  `{run_id, run_attempt, head_sha, stage, approval_comment_id, approval_created_at, approval_updated_at, approval_author, quoted_words}`.
  - **The prior authorization.** `approval_comment_id`, `approval_created_at` and `quoted_words` are the owner's
    comment on the round PR authorizing the dispatch.
    - The quoted words name the full commit id and the stage.
    - The comment precedes the run's `created_at`.
    - No comment is reused.
    - The comment is read through `GET issues/comments/{DEC}` (ARP-3-QC22 r14, R13-B4; re-review R14A-B1).
  - **The edited-comment rule (re-review R10-B5).** `approval_updated_at` must equal `approval_created_at`, or precede
    the run's `created_at`. A comment edited after its run is a violation, and the round halts VOID.
  - **Authorship.** `approval_author` must be `amaybaum`, with author association `OWNER`. Host records cannot tell the
    owner's comment from one posted with the session's credential. That ambiguity is closed only by the owner's
    ratification: at the designation of `E` for the entries committed at `E`, and for the `E` dispatch's own entry as
    precondition 2's R8 provides (owner-approved R8 alternative; C.8 item 9). An entry not ratified makes
    `verdict` print VOID. These checks and ratification are operational conditions under R10; the enduring
    record does not assert that unretained E-stage approval/ratification checks passed. No credential
    independence is inferred.
  - **Binding the approval to the run (re-anchored on the owner's quoted commit; E5).** For the run that attests at
    each stage, all of these must hold (ARP-3-QC22 r14a, R14-N2):
    - the run's `head_sha` equals the full commit id in the owner's quoted words;
    - job B's B3 is `success`, so `github.sha` equals the `arp2qc21_sha` input and the ref is the round branch;
    - at S1, the committed measurements' `parameters.dispatch_sha` equals S1 (at `E`, B3's `success` binds the
      input);
    - job B ran, so the `arp2qc21_decisive` input was true;
    - the run's `run_attempt` is `1`.
  - **The entry of a host-VOID run** that a retake replaces holds when its prior authorization, the edited-comment
    rule and its authorship hold, and its run is a host VOID as the *Stop rule* (C.6) defines it; its B3 need not
    be `success` (ARP-3-QC22 r14a, R14-N2).
  - **Order.** The owner's approval comment precedes the run's `created_at`, and no comment is reused (*The prior
    authorization*).
  - **Re-runs (c.6726548830, item 3).** A re-run attempt never attests. "The run at a stage" is attempt 1 alone.
    - In attempt `≥ 2`, job B's job-level `if:` is false, so job B is `skipped` by the job-level `if:`.
    - `derive-run` reads every attempt.
    - An attempt `≥ 2` of an approved dispatch whose job B is anything but absent or `skipped` is a violation, and
      the round halts VOID.
    - A re-run that computes nothing is recorded and ignored. It cannot repair a red attempt 1, and the stop rule
      applies to attempt 1 as it stands.
  - **Gate-test entries** (precondition 6″) are the only other checker-bearing dispatches admitted. Each carries:
    - its frozen expectation;
    - the conclusions of job B and of B3 and B4;
    - in every gate-test entry, B4 must be absent or `skipped`. A gate-test run in which B4 ran is a violation.
- **`order.json`.** `F`'s designation precedes the first execution run. The owner's designation comment is read
  through `GET issues/comments/{DEC}`, its id given as an argument; its `created_at`, and its `updated_at` under the
  edited-comment rule, precede the first execution run's `created_at` (C.8 item 9). Its author must be
  `amaybaum` with association `OWNER`, and its quoted body must contain the phrase `Designate F <sha>`, with
  `<sha>` `F`'s full 40-hex commit id, exactly once. `order.json` records its id, author, association, times and
  quoted words (§A.42 item 7; ARP-3-QC22 r14, R13-B4; re-reviews R14B-B1 and R14C-B1).
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
      (2). The residual is empty if no such draft was pushed before `D`, which is the writer's statement and is not
      checked by this round (ARP-3-QC22 r14a, R14-Rb2).
  - **The queries.** Each is `GET actions/runs?<event filter>&created=<a>..<b>&per_page=100`, paginated to the end. Set
    (1) uses `event=workflow_dispatch`. Set (2) lists without an event filter, and drops `workflow_dispatch` runs,
    which set (1) holds.
    - The slices are disjoint at one-second granularity (`a..b`, then `b+1s..c`). Their union is recorded to equal the
      set's window, where `T_repo` is the repository's `created_at` from `GET` on the repository.
    - `total_count` is read from page 1 and must be the same on every page. The listed count must equal it, and it
      must be below 1,000 (r9 N2). A slice that fails this is split, and the split is recorded.
    - Runs are deduplicated by `id`.
    - `order.json` records every query, its window, its `total_count` and its listed count.
  - **Attempts and jobs (r10 N3).** For every listed run, every attempt from 1 to `run_attempt` is read through
    `GET actions/runs/{run_id}/attempts/{n}` and its jobs through `GET actions/runs/{run_id}/attempts/{n}/jobs?per_page=100`,
    every page. The `filter=all` endpoint (`/runs/{id}/jobs`) is not used.
  - **Identification, conservative (r9 B3(a)–(c)).** An attempt is **checker-bearing** if either of these holds. Its
    step and job conclusions are not consulted.
    - **(i) By name.** Any of its jobs has the display name `Numerical probes / ARP-2-QC21 exact decision (gated)` or
      `Numerical probes / ARP-2-QC21 fixtures and stress`, or contains a step named "ARP-2-QC21 exact decision".
    - **(ii) By blob.** Its `head_sha` tree carries the pinned blob of `qc21_check.py` at any path. The tree is a
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
      branch and the gate-test branch, whose commits since `D` are listed in `order.json`. The GT-ACT branch (C.7) is
      **not** a recorded branch (R11a-B1). It is created from `D`, so its tree carries neither the pinned checker
      blob nor the frozen job or step names. Its push runs are therefore not checker-bearing and cannot trip rule (d),
      and its own `force_push` entry is outside the ref-move rule, which reads recorded branches only.

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
    - the activity calls for the recorded branches.

    An estimate, which no condition uses, is about 770 calls for set (1) (r10 review §3, H11–H15), plus set (2)'s
    runs since `T0`, at about 100 runs a day on this repository (a read-only count, 2026-11-08; ARP-3-QC22 r14a,
    R14-Rb2). There are three captures (`check --stage S1`,
    `verdict` and `order --final`), each recording its own call count.
    - A rate-limit response (403 or 429 with an exhausted limit) or a 5xx makes the capture **failed**, to be retried
      after the reset. It is never a pass and never a VOID.
    - Set (2)'s size is measured at the first capture. If one capture would exceed one hour of the token's limit, the
      stage stops and the owner is told; no capture is shortened.
  - **Ref moves (re-review R10-B5).** Every capture reads `GET activity?ref=refs/heads/<branch>` for each recorded
    branch, every page. A `force_push` or `branch_deletion` entry on a recorded branch is a violation, and the round
    halts VOID.
  - **Residual (stated).** A deleted run cannot be enumerated. The owner's commitment at the freeze (no run, run log or
    artifact of this repository is deleted until `Q`; preregistration, precondition 2) covers this, together with
    c.6726548830, item 1. `T0` is also its anchor: `D`'s host time, the `timestamp` of the entry
    with `after = D` in `GET activity?ref=refs/heads/main` (`pr_merge` or `push`; r9 N4). Its value: PENDING.
- **The no-unapproved-F1 rule (re-review r6 B1; §A.44).** For every non-dispatch checker-bearing attempt at a
  recorded-branch commit, `order.json` records:
  `{run_id, run_attempt, head_sha, event, attempt_status, jobB_conclusion, B4_conclusion, A3_conclusion, A3b_conclusion, fixtures_artifact_digest}`.
  Run/attempt identity, event and `attempt_status` come from `GET actions/runs/{run_id}/attempts/{n}`;
  job/step conclusions come from its jobs API. `fixtures_artifact_digest` is the artifacts API's `digest` field, recorded as
  provenance and read by no condition; no artifact content is downloaded (C.8 item 7). A capture listing any
  checker-bearing attempt with status other than `completed` fails capture and is retried after completion;
  a queued or in-progress attempt's missing conclusions are not evaluated as completed outcomes (r14c-N1).
  The rule holds exactly when, for every such completed attempt:
  - job B is absent or `skipped`;
  - B4 is absent or `skipped`;
  - A3 is absent or `skipped`, so it never started (ARP-3-QC22 r14a review, Rc1), or A3b's conclusion is
    `success`, so A3's output had `mode: "fixture"` with the synthetic placeholders. When A3 is skipped, every
    later step of job A with a default `if:` is skipped too, and A3b, which runs `always()`, starts only
    `controls.py`, so no checker process runs in job A.

  **Residual (named; ARP-3-QC22 r14a review, Rc1).** An A3 that started and left no fixture-mode output (a
  timeout, a crash, a cancellation or a lost runner during A3) makes A3b fail, and the completed attempt is a
  violation (fail-closed). **Executor precondition (frozen; §A.41):** no checker-bearing commit is pushed to a
  recorded branch unless A3's command, run locally on that commit's tree with Python 3.11, completes within
  `timeout-minutes` with fixture-mode output and `controls.py fixture-mode-check` exits 0 on that output.
  The executor cancels no run on a recorded branch while its job A runs. This does not exclude a runner fault
  during A3, or an A3 that completes locally and times out on the runner. These local A3 runs require separate
  design-run authorization; the first such push is the design branch's, and no frozen-splice tree is pushed
  before that authorization.

  `verdict` re-checks the rule on a fresh capture. A violation is a failed check, and the round halts VOID.
- **Retention (r7 N1).** Every upload carries `retention-days: 90`. `controls.py check --stage S1`, run before the S1
  dispatch, also captures the rule's records for every run then existing: the enumeration and the non-dispatch
  records. It writes them to `evidence/order-s1.json`, which is committed at `E`.
  - The no-unapproved-F1 rule reads no artifact, so a missing artifact is not a violation. `order-s1.json` keeps each
    record's `fixtures_artifact_digest` as provenance (C.8 item 7).
- **`verdict`.** It prints the token line `VERDICT <P token> <B token> <C token> level <n>` (the three tokens, VOID
  ones included, and the Level awarded, `none` if none; D21 (b)) only when all of the following hold. Otherwise it
  prints `VERDICT VOID`, which is reserved for round-level failures, and exits 1.
  - every check at `E` passes;
  - the owner's designation of `E`, whose body contains the phrase `Designate E <sha>` with `<sha>` `E`'s full
    40-hex commit id exactly once, ratifies, by `order.json`'s sha256, the run list and every approval entry
    committed at `E` (C.8 item 9), quoted with author and time (fail-closed: without it, VOID); the `E` dispatch's
    own entry and each retake entry require their canonical-JSON sha256s in that same designation of `E`,
    read through `issues/comments/{DEC}` (approved R8 alternative); absent/wrong digests give VOID. Under R10
    these are required landing conditions; the enduring record does not assert the unretained checks passed;
  - every approval entry holds as stated for its run, the run that attests at its stage or a host-VOID run a retake
    replaced, the entries `verdict` builds for the dispatches at `E` included (ARP-3-QC22 r14, R13-B4; r14a,
    R14-N2; re-review R14A-B1): each is checked as *Approval entries* states, and each entry of a dispatch at `E`
    is built by `verdict` from that dispatch's approval comment id (C.8 item 9);
  - in attempt 1 of the runs at S1 and `E`, the job and step conclusions satisfy C.7's owner-approved B1
    conclusion table for `workflow_dispatch`: the 15 A42 exclusion shards and `ARP-1-MARC keep the measurements`
    are `success`; `KTRANS-SEP-2 axiom reports within the three axioms` is `success` and the KTRANS marker is
    `skipped`; every other job and step is `success`, every step of job B (B6 included at `E`) and every step of
    job A (A7 and A10 included; A3 included, so that a red fixture-mode control fails this condition:
    owner-approved R2 default, precondition 2) among them. The run's own conclusion is `success` (r10 N5).
  - B6 at `E` is `success` and its replay result is a match, which binds the committed measurements to the approved
    decisive computation (C.8 items 3, 7);
  - the S1 binding holds: S1's measurements artifact, read in memory, equals the committed measurements as canonical
    JSON without `parameters.dispatch_sha` (D21 (b); C.8 item 3). A missing or unreadable artifact fails it (an
    expired or deleted one: owner-approved R6 default, precondition 2);
  - the note's token line equals this token line.

  A red job elsewhere in attempt 1 is therefore a failed `verdict` condition. A re-run cannot repair it (c.6726548830,
  item 3), and the round halts VOID.


### C.4 Controls and self-tests used by the copied text (copied; edits applied)

| code | what | green when | route to failure |
| --- | --- | --- | --- |
| **F10** (step 4 feasible; re-review B2(e)) | four point laws, `Z` read only: `d = 2 < r_S = 4` | feasible, decided by step 4's feasible branch (steps 2 and 3 inapplicable); model verified | step 4's model construction untested |
| **ZPT** (step 3) | `Z±` with point reads: `r_S = d = 2 < r_E = 4` | feasible, decided by step 3 (a model `K` exists: `ξ = α[z = 0] + β[z = 1]`); model verified | step 3 untested |
| **C-CERT** | every verdict certificate-verified by the independent verifier, which re-derives `N`, checks `A Bᵀ = N` and the ranks, and re-enumerates the facets (over the retained rows; C.8 item 15); for every step (2, 3, 4) that decided | in fixture mode, `unverified = 0` (a failed fixture certificate makes fixture mode exit 3; C.1). In decisive mode, a fragment whose certificate fails is recorded `undecided` and given no verdict; `unverified` counts it, and that voids nothing by itself: an undecided B-P gives B-VOID through `decide-b`, and an undecided reported-only fragment is reported (D21 (b)). C-CERT is red, voiding B's token, only if a fragment whose certificate fails is given a verdict | a solver result taken on trust, a wrong factorization, or an incomplete facet list |
| **C-INDEP** (re-review B2; r4 N2; c.6724832474) | An AST check on `qc21_check.py` (rules below). The driver serializes the solver's output (`A`, `B`, the facet list, the certificate) to canonical JSON, whose sha256 is `cert_sha256`. The verifier receives that byte string, the charged laws and the read tables, and calls `json.loads` on it itself. So the certificate and the solver's facet list reach it only as plain data, never as solver objects. **Rules:** inside every `v_*` function, calls may target only (i) other `v_*` functions, (ii) `Fraction`, `json.loads` and `itertools.combinations`, (iii) the builtins `len`, `range`, `sum`, `min`, `max`, `abs`, `sorted`, `enumerate`, `zip`, `all`, `any`, `int`, `tuple`, `list`, `dict`, `isinstance`, and (iv) attribute calls on local variables (for example `.append`). `globals`, `locals`, `vars`, `getattr`, `setattr`, `eval`, `exec`, `compile` and `__import__` are forbidden. Every other module-level name referenced must be a `v_*` function or a whitelisted name. **Coverage (r5 N4):** the rules apply to the entire `FunctionDef`: its body, default argument values, decorators, and every nested function and lambda in it. **Runtime types:** the verifier's non-JSON inputs, the charged laws and the read tables, are checked on entry to be built only from plain `dict`, `list`, `tuple`, `Fraction` and `int`, recursively; anything else is `unverified` | holds | a verifier that reuses solver code or solver-internal state, by direct call or by alias |
| **C-STATELESS** (re-review r5 N1(d)) | at `E`, the `fixtures` section of S1's committed `measurements.json`, in canonical JSON (verdicts, deciding steps, derived fields, tokens, pivots, bits, work), is byte-equal to that of `evidence/confirmation-measurements.json`. S1 decides F1 too, while 6′ does not. This check compares S1 with the supplied committed copy. Any inference about 6′'s actual fixture decisions requires that copy to be authentic; no condition binds it to 6′'s archive (C.7). A matching supplied copy can pass vacuously, so equality alone does not establish that F1 left fixture decisions unchanged | byte-equal; evaluated by `controls.py check --stage E`; a mismatch is a failed check at `E`, so the round halts with VOID (r6 N1) | cross-fragment solver state, or nondeterminism |
| **C-BUDGET** | in the decisive run, every fragment decided within `P_max`, `B_max` and `W_max` (frozen at `F`); a fragment over budget is recorded `out_of_scope` | holds: every fragment over its budget is recorded `out_of_scope` and given no verdict. An `out_of_scope` B-P gives B-VOID through `decide-b`; an `out_of_scope` reported-only fragment is reported (D21 (b)); the checker exits 0. C-BUDGET is red, voiding B's token, only if an over-budget fragment is given a verdict | an over-budget fragment given a token, or a crash. M-BUDGET exercises the path. A wall-clock timeout is not prevented by the budget, only made unlikely by the timeout test, and is a checker outcome (*Stop rule*) |
| **C-NCF** | every nondegenerate fragment (`d = r_S = r_E`) is decided feasible by step 2 and its certificate verifies; on the fixtures, step 4 is also run where steps 2 or 3 decide, and must agree, with its own certificate verified (r4 N4) | holds | a rank, fast-path or LP error |
| **C-SYM** | on the fixtures, the effect-facet LP gives the same verdict. **The effect-facet LP** (ARP-3-QC22 r14, R13-N10) is step 4 with the roles of `a_p` and `b_e` exchanged: `{h_k}` are the facets of `cone{b_e}` (the effect set of *The accessible GPT*, unit included), and it decides `Σ_k h_k κ′_kᵀ = I_d` with `κ′_k · a_p ≥ 0` by the same Farkas route, step 5's rules and step 6's budgets. A noncontextual model regroups on the effect side as step 4's does on the preparation side, so the two verdicts agree on every fragment whose effect set holds the complements and the unit. The verifier checks its certificates with the roles exchanged: for infeasibility, `W` and `y ≥ 0` with `W h_k = Σ_p y_{kp} a_p` and `tr W < 0`; for feasibility, the model `μ_p(k) = (κ′_k · a_p)(h_k · b_u)`, `ξ_e(k) = (h_k · b_e)/(h_k · b_u)`, by definition. Each C-SYM decision counts as a fragment decision for the budgets: its counters enter the freeze rule's maxima, and its work is part of `W_fix`. The caps apply to the fixture as listed, not to its exchanged form | `mismatches = 0`; every C-SYM certificate verified | a formulation error |
| **C-EXACT** | AST scan: no float literal, no `float` call, no `math` import, and `/` only inside the one `Fraction` helper | no hit | floating point in a verdict |

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
  `T = 0`, B-S4F with `T = 3`);
- **M-SOLVER:** a solver returning its verdict with no certificate, or with the other verdict's certificate, must give
  `unverified > 0` and VOID;
- **M-FACTOR** (invalid by construction): add 1 to `A[0][0]`. Row 0 of `A Bᵀ` then changes by the first row of
  `Bᵀ`, which is nonzero because `B` has full column rank. It must fail the verifier's `A Bᵀ = N` check;
- **M-RAY** (D19 (0)(c); invalid by construction): in B-RAY-P's certificate, one removal multiplier altered; and,
  separately, the first row removed under a fabricated certificate. Each must fail C-CERT;
- **M-INDEP:** three variants must each fail C-INDEP (re-review r5 N4):
  - a `v_*` function edited to call a solver function directly;
  - a `v_*` function given a default argument bound to a solver function (`x=s_solve`);
  - a `v_*` function containing a nested function or lambda that closes over a solver function;
- **M-BUDGET:** with `P_max = 1`, and separately with `B_max = 1` and with `W_max = 1`, on a step-4 fixture (GBIT)
  and on a step-3 fixture (ZPT).
  - The checker must record `out_of_scope`, give the fragment no verdict, and raise no exception. With the fragment
    in B-P's role, `decide-b` must give B-VOID; in a reported-only role, the fragment must be reported and void
    nothing (D21 (b)).
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
      - A `--dispatch-sha` that is not 40 lowercase hex must exit 4. `qc21_check.py` checks it itself, as length 40
        over `0123456789abcdef`, because `a_ok` lives in `controls.py`.
      - This self-test runs as A8 in the design run, in 6′ and in every later run.
      - **Residual.** The host's evaluation of B4's `${{ … }}` expression and its redirect are first exercised at
        S1. A fault there is a checker outcome: VOID, with no retake.
    - `s_mode` must return `"fixture"` for each single-key failure: `--event workflow_dispatch` with
      `GITHUB_EVENT_NAME=pull_request`; the converse; both event keys with `GITHUB_RUN_ATTEMPT=2`; and all three with
      `GITHUB_REF` other than `refs/heads/research/arp2-qc21-20261108` (the ref key). Each, run
      through the entry with the synthetic environment, must produce `mode: "fixture"` with zero builder calls.
    - The self-test checks only that `s_mode` returns `"decisive"` when all three keys hold; it never runs that case
      through the entry, which would build F1.
    - `t_builder_refuses` runs once, under A8's real environment, and must record the refusal (r10 B2). The refusal
      reads only the real `os.environ`, so the synthetic environments above are exercised through `s_mode` and the
      entry function `s_entry(argv, environ)`, never through the refusal (C.8 item 5).
  - **Workflow keys (control W).** A splice with any of these removed or altered must fail W:
    - the event key, the attempt key, the ref key or the receipt key, from B4 or from B6;
    - any key of job B's `if:`;
    - B3, or its ref key;
    - A3's literal `--event fixture`;
    - the marker A10;
    - the marker A3b, or its `if:` (ARP-3-QC22 r14a, R14-N10; re-review r14b-N1).
  - **`qc21_check.py` name rules (control B).** Each of these must fail B:
    - a second occurrence of `"workflow_dispatch"`;
    - an alias `b = <builder>` in a self-test function;
    - a second self-test function that references the builder (r10 B2);
    - `t_builder_refuses` with a statement other than the stated `try` form;
    - `globals()[...]`;
    - `getattr(...)`;
    - a `__*__` attribute walk;
    - a call to `set` or `frozenset`, a set display or a set comprehension.
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
    - **ZIP-1 to ZIP-3** (D21 (b)): `zipfile.ZipFile(io.BytesIO(b), "w")`; an `extractall(…)` or `open(…)` call on a
      `ZipFile`; `zipfile.ZipFile(<a path>)`;
    - a `gh` path f-string with a formatted value that is not an `a_ok(...)` call.

- **M-MODE** (re-review r7 B2(b)): `decide` on a fixture-mode `measurements.json` must give VOID. It must do so
  independently on each of three conditions, testing each with the other two repaired: `mode` is not `"decisive"`;
  `complete` is `false`; an F1 `lp` field is `"placeholder"`.
- **S1-BIND** (D21 (b); C.8 item 3). `verdict`'s S1 binding, on synthetic records built in memory. An artifact list
  and an archive holding a `measurements.json` that differs from the committed file only in
  `parameters.dispatch_sha` must bind. Each of these must fail it: a changed token; a second member in the archive;
  a `digest` that differs from the archive's sha256; a `workflow_run.id` or `head_sha` of another run; no artifact;
  a fresh read whose `id`, `digest` or member list differs from the record in `evidence/s1-run/results.json`
  (C.8 item 3).
  No file is written.
- **APPROVAL-ENTRIES** (ARP-3-QC22 r14, R13-B4, and r14a, R14-N2; re-review R14B-B1). `order`, `verdict` and
  `e-entry` on synthetic records built in memory. Each of these must fail: an approval entry whose comment follows
  its run's `created_at`, whose `updated_at` follows it, whose author is not `amaybaum` or whose association is not
  `OWNER`, whose quoted words name another commit or stage, or whose comment is reused; an `F` designation comment
  whose `created_at` or `updated_at` follows the first execution run's `created_at`, whose body does not
  contain `Designate F <sha>` with `F`'s full 40-hex id exactly once, whose author is not `amaybaum`, or whose association is not `OWNER`.
  A push run at a strict descendant of `F`, created before the S1 dispatch, must be selected as the first
  execution run across events; an entry claimed as host VOID whose run fails C.6's host-VOID definition must
  fail. The same cases on an entry
  built for a dispatch at `E` must each make `verdict` print `VERDICT VOID`. An entry of a host-VOID run whose B3
  is not `success` must hold, and the same entry offered as the run that attests at its stage must fail. Two
  `E`-stage approval comment ids must give two built entries. `e-entry` and `verdict` must give byte-identical
  entries on the same records. Under the approved R8 alternative, a missing designation of `E`, a wrong
  entry digest, or failed owner/OWNER checks makes `verdict` print `VERDICT VOID`. No separate ratification
  comment is read. No file is written.


### C.5 Scripts (copied; D12 edits applied)

**Implementation representation (r15; editorial/engineering, no new scientific rule).** The exact script blob
and SHA-256 pins and the evidence-file SHA-256 pins are stored once in this preregistration's block below.
`controls.py` reads them; its `PINS` constant gives the required keys only. A script does not embed its own blob
identity. These fields remain unresolved until the separately authorized design/confirmation process supplies
them; null is never accepted by a freeze check.

```qc21-implementation-pins
{"schema":"arp2-qc21-pins","version":1,"blobs":{"qc21_check.py":null,"controls.py":null},"script_sha256":{"qc21_check.py":null,"controls.py":null},"sha256":{"stress.json":null,"design-run.json":null,"gate-tests.json":null,"confirmation-run.json":null}}
```

The checker additionally carries provenance-only `SOURCE_BASE`, unset in the implementation draft. Before a
separately authorized local A3 or design tree, it is bound to that round's approved `D`, and freeze checks require
the match. This preserves the distinction between a public implementation draft and the later pinned execution
blob; it adds no decisive-mode key or physical assumption. The result note identifies `E` as its containing
evidence commit; the owner's designation supplies the full hash externally, avoiding a self-referential file hash.
`e-entry` hashes exactly its entry's UTF-8 `json.dumps` serialization with the specified key/separator/ASCII
options, without the output wrapper or trailing newline. File pins continue to hash their preserved bytes.

The CLI supplies a validated UTC capture time through the capture JSON (`order`, `verdict`, and S1's
`--capture-config`) or `e-entry --capture-time UTC`. It is recorded as the inventory's upper bound; it is not a
scientific measurement. Executor clock provenance and a capture immediately before landing remain required.
The verifier's closed callable allowlist is unchanged. `str` is also admitted as a non-call type name, and the
builtin exception names ValueError, TypeError, KeyError, IndexError and ArithmeticError only as non-call names
for malformed-data handling. None admits a solver/shared-helper call or alias.


- **`qc21_check.py`** (blob PENDING; sha256 PENDING).
  - It imports `fractions`, `itertools`, `json`, `os` and `sys`, and reads no file. `os` is referenced at exactly two
    sites, each `os.environ` passed whole to `s_mode`: the `if __name__ == "__main__":` block, which calls
    `s_entry(sys.argv, os.environ)`, and the one shared refusal function `s_refusal()` (control B; C.8 item 5).
    `cert_sha256` is computed by the pure-Python `h_sha256` (C.8 item 4).
  - **No sets.** `-I` leaves string-hash randomization on, so the iteration order of a `set` of strings can differ
    between processes. `qc21_check.py` constructs no `set` or `frozenset` (control B). It uses lists and `dict`
    keys, whose order is insertion order, so its outputs are byte-identical across processes.
  - The solver's functions are named `s_*` and the verifier's `v_*` (C-INDEP).
  - **Modes:**
    - the default prints canonical-JSON `measurements.json`, exiting 0 when the output is complete. A red
      decisive-mode control, or an `out_of_scope` or `undecided` fragment, is recorded and voids only what C.8 item 14
      states (D21 (b)). Any other exit is incomplete;
    - `--stress` prints canonical-JSON `stress.json`;
    - `--self-test`;
    - `--event <name>` is required for the default computation. **Four keys select decisive mode (re-review r8
      B1(a), r9 B4(a); the ref key, R10-B5):**
      - `<name>` is `workflow_dispatch`;
      - the environment variable `GITHUB_EVENT_NAME` is `workflow_dispatch`;
      - `GITHUB_RUN_ATTEMPT` is `1`;
      - `GITHUB_REF` is `refs/heads/research/arp2-qc21-20261108`.

      If any key fails, the checker runs fixture mode, whose exit rule is in *Method*. Without `--event` it refuses,
      with exit 4. `--event fixture`, job A's literal, always fails the first key.
    - `--dispatch-sha <40-hex>` (job B only) is recorded as `parameters.dispatch_sha`. It selects no mode. A value
      that is not 40 lowercase hex makes it refuse, with exit 4.
      - The host sets both variables for every step, and child processes inherit them.
      - The decision is the pure function `s_mode(argv, environ) → "decisive" | "fixture" | "refuse"`. The entry calls
        it with `os.environ`; the self-test calls it with synthetic mappings.
    - **The builder refuses on its own (r9 B2(h)).** The first statement of `s_decisive` and of
      every registered builder is the call `s_refusal()`, whose body checks
      `s_mode(sys.argv, os.environ) == "decisive"` and raises otherwise (C.8 item 5), which is a crash and hence VOID. Even a
      call reached by an unforeseen route therefore cannot compute F1 outside a decisive run.
    - **The builder's name (r10 B2).** It is referenced, as a `Name` node, at exactly two sites (control B):
      - the entry function `s_entry` (the default computation);
      - the single self-test function `t_builder_refuses`. Its body is one `try` statement:
        - the `try` calls the builder with no argument;
        - the handler catches the refusal exception and records a pass;
        - an `else` clause records a failure.

      **Why the second site is safe.** The self-test runs only as A8, whose real `sys.argv` is
      `qc21_check.py --self-test`, with no `--event`. So `s_mode(sys.argv, os.environ)` returns `"refuse"`
      whatever the environment, and the builder raises at its first statement, before any work. That holds in a
      decisive dispatch too.
- **Schema `arp2-qc21-measurements` v3.**
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
  - `budget`: `P_max`, `B_max`, `W_max`, and per fragment `respected`: true exactly when the fragment was given a
    verdict and its typed budget and cap limits all held (C-BUDGET's per-fragment check), so a fragment withheld
    for any reason, a failed certificate included, reads false.
  - `is_rule`, `is_size`, `c_cert`, `c_indep`, `c_ncf`, `c_sym`, `c_iso_name`, `flags`.
  - There is no timestamp, host or duration field.
- **Schema `arp2-qc21-stress` v2** (`--stress`). Per fragment (stress fixtures, frozen fixtures and their
  completions, CC-F0): `verdict`, `decided_by`, `pivots`, `max_bits`, `work`, `certificate_verified`; the totals
  `W_fix` and `W_stress`. There is no timestamp.
- **`controls.py`** (blob PENDING; sha256 PENDING).
  - **Modes:** `check <commit> --freeze F [--stage S1|E|W]`, `decide`, `note`, `replay`, `stress-check <stress.json>`,
    `fixture-mode-check <fixtures.json>`, `derive-run`, `order`, `verdict`, `e-entry <E> <comment id>`
    (C.8 item 9), `--self-test`.
  - **Codes:**
    - T: chain and blocks;
    - G: paths;
    - R: record files by stage (S1 includes `confirmation-run.json`, `confirmation-measurements.json`,
      `gate-tests.json` and the two STAB-FALSE certificates; `E` includes `order-s1.json` and `approvals.json`);
    - B: blobs, allowlists, C-EXACT, C-INDEP, and **the guard's node-form rules** (re-review r7 B2(a), r8 B1(b), r9
      B2), checked by AST on every node of each script.
      - **In `qc21_check.py`:**
        - the string `"workflow_dispatch"` occurs exactly once, as the module constant `DISPATCH_EVENT`;
        - `DISPATCH_EVENT` is referenced only in `s_mode` and in M-GUARD's self-test functions;
        - `os` is referenced at exactly the two sites named above, each as the expression `os.environ`;
        - `s_decisive` is referenced only at the two sites named above (`s_entry` and `t_builder_refuses`, in the
          stated form); each name in `DECISIVE_BUILDERS` is referenced only in its own `def`, in `DECISIVE_BUILDERS`
          and inside `s_decisive`; and `s_decisive` and every registered builder begin with `s_refusal()` (C.8
          items 5, 6);
        - no call to `set` or `frozenset`, no set display and no set comprehension occurs;
        - module-wide, it uses no `getattr`, `setattr`, `delattr`, `globals`, `locals`, `vars`, `breakpoint`, `exec`,
          `eval`, `compile` or `__import__`, and no name or attribute of the form `__*__` other than the single
          statement `if __name__ == "__main__":`.
      - **In `controls.py`, a node-form allowlist:**
        - **(a) Imports.** Only `import X`, with `X` in the frozen list `ast`, `fractions`, `hashlib`, `io`, `json`,
          `os.path`, `re`, `subprocess`, `sys`, `tempfile`, `zipfile` (`io` and `zipfile` for the S1 binding; D21 (b)). No
          `as`, and no `from … import`.
        - **(b) Attributes.** An attribute of a module name must come from that module's frozen list:
          - `subprocess.run`, `subprocess.PIPE`;
          - `os.path.join`, `os.path.isfile`;
          - `json.loads`, `json.dumps`;
          - `hashlib.sha256`;
          - `re.fullmatch`;
          - `sys.argv`, `sys.exit`, `sys.stdout`, `sys.stderr`;
          - `fractions.Fraction`;
          - `tempfile.TemporaryDirectory`;
          - `io.BytesIO` and `zipfile.ZipFile` (D21 (b)). A `ZipFile` is constructed only as
            `zipfile.ZipFile(io.BytesIO(<bytes>))`, with one argument, and only `namelist()` and
            `read("measurements.json")` are called on it. The resource has one local with-binding, no alias,
            rebinding or escape; its only uses are those two method calls;
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
          `w_path` joins it under the temporary directory (r12 N1). Nothing else writes a file, so a `.pth` or other startup file cannot be planted.
        - **(e) Process starts.** Only as `subprocess.run(<list display>, ...)`.
          - No keyword other than `capture_output`, `check` and `text`. There is no `shell=`, `env=`, `executable=`
            or `cwd=` (r10 B1(b)).
            - Every process starts in the invoking shell's directory.
            - The entry refuses, with exit 2, unless `git rev-parse --show-prefix` prints an empty line, that is,
              unless it runs at the top of the repository's work tree.
            - The workflow runs it at the workspace root (control W).
          - Every list element is a string literal, a call to the frozen validator `a_ok(x)`, or, as `gh`'s path
            only (rule (g)), an f-string whose every formatted value is an `a_ok(...)` call and whose text, with
            those values replaced, is a frozen template.
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
              runner's git (ARP-3-QC22 r14a, R14-Rb2).
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
            - `actions/artifacts/{DEC}/zip` (D21 (b)), read by `verdict` and, for S1's measurements artifact, by
              `derive-run` run on S1's run before `E` is committed (C.8 item 3);
            - `issues/comments/{DEC}` (ARP-3-QC22 r14, R13-B4; re-review R14A-B1), read by `order`, `verdict` and
              `e-entry` (C.3; C.8 item 9; re-review R14B-B1);
            - `git/trees/{HEX40}?recursive=1`;
            - `git/trees/{HEX40}`;
            - `activity?ref=refs/heads/...`;
            - the repository itself.
          - Every further element comes from the frozen set `--paginate`, `--slurp`, `-H`,
            `"Accept: application/vnd.github+json"`. `--paginate --slurp` appears only on
            `activity?ref=refs/heads/...&per_page=100`: `gh` follows the host's cursor pagination (the `Link`
            header's `rel="next"`), never a numbered `page=` parameter, and returns one array of page arrays. The read
            fails closed unless that output is a non-empty array whose every element is an array, and every entry is
            an object with a decimal `id`, unique across all pages, and a string `activity_type`.
          - So there is no `--input`, `graphql`, `--hostname`, `-f`, `-F`, `--field` or `--raw-field`, and no other
            `-X` or `--method`, in any spelling.
        - **(h) Control T's exception.** The one process start that is not `git` or `gh` is
          `["python3", "-I", "-S", "-c", <the frozen string>, a_ok(D), a_ok(F)]`. It inherits the repository root as
          its directory, as rule (e) requires, and that is needed for `tools/`.
          - `-S` disables `site`, so no startup file runs.
          - Its code imports only `tools/v3_verifier.py`, whose blob the inputs pin (*Inputs*, row V3V). Before it
            starts that process, `check` compares the working-tree file's blob id with that pin, at `F`, S1 and
            `E`; a mismatch fails DS, and the process is not started (re-review r14b-N2).
        - The string `"workflow_dispatch"` occurs only inside the module-level string constants named `SPLICE_*`,
          which hold the frozen splice byte-exactly for control W, and inside functions named `run_class_*`, which
          `derive-run`, `order`, `verdict` and `e-entry` call (C.8 item 8; re-review r14b-N6).
        - `replay` compares files only: it reads two files in `"rb"` mode, parses each with `json.loads`, removes
          `parameters.dispatch_sha` from both, and compares their canonical serializations (C.8 item 3).
      - **What these rules give, as checked by B and exercised by M-GUARD (BYP-1 to BYP-21, BYP-23 to BYP-26, ZIP-1
        to ZIP-3 and the unnumbered variants; ARP-3-QC22 r14a).** This is all that B
        claims (r10 review, overall design). For the two frozen blobs that B checks, and for every route these rules
        admit:
        - `controls.py` starts no process other than read-only `git`, GET-only `gh api` and control T's frozen
          command;
        - it writes no file outside a self-test temporary directory;
        - so it cannot create, trigger, re-run or approve a workflow run (r8 N2). That covers
          `POST …/pending_deployments`, the deployment-review endpoint, which is excluded by the GET-only form and
          named as a variant in M-GUARD;
        - it cannot import or execute `qc22_check`.

        B claims nothing about routes it does not model, such as the interpreter, the runner or the host. With the
        Environment gate waived (c.6735159962), authorization is detected, not prevented (*The workflow edit*).
        - **The session's credential.** The session acts under the owner's GitHub identity, `amaybaum`. What that
          credential can do, and which control catches each act, is stated in the preregistration's *Scope of
          authorization and detection* (c.6735159962).
    - W: `verify.yml` as a whole file (re-review r9 N3). At the design run, at 6′, at S1 and at `E` it must be
      byte-equal to `D`'s `verify.yml` with the frozen splice. Hence no workflow-level `env:`, `defaults:` or shell
      override can reach either job. The splice includes:
      - the two `workflow_dispatch` inputs;
      - both jobs, with their display names and `timeout-minutes`;
      - A3's literal `--event fixture`;
      - job B's job-level `if:`, its `env:` and B3 (with the ref key);
      - B4's compound `--event` expression and B6's `if:`, each with the ref key;
      - the markers A10 and A3b, with A3b's `if:` (re-review r14b-N1);
      - the aggregate's lines.

      Its self-test shows that each of these removals fails W:
      - the event key, the attempt key or the receipt key, from B4 or from B6;
      - any key of job B's `if:`;
      - B3, or its ref key;
      - A3's literal;
      - the marker A10;
      - the marker A3b, or its `if:` (re-review r14b-N1);
    - DS: inputs and drift;
    - X: schema and flags;
    - V: note regeneration and S4;
    - P: no unbackticked `PENDING` under `--freeze`; evidence pins, including `stress.json`'s sha256 and the two STAB-FALSE certificates' sha256s.

### C.5a This round's measurement schema (adapted; replaces QC22's schema bullets in C.5)

Schema `arp2-qc21-measurements`, version 1. Canonical JSON, with no timestamp, host or duration field. Its fields:
- `parameters` (with `dispatch_sha`), `complete`, `mode` (`"decisive"` or `"fixture"`);
- **P:**
  - `Adm_B`, `Adm_A` (sizes, members);
  - per arm: `V`, `Δ`, `D`, `D_phase`, `K`, NONABS, SPI, `CPL`, the eraser fields (with `null` cells);
  - `decide_p` inputs; `ATTR`; `decompose_p`;
  - `ab_p` (existence and universality);
  - `ablate_p` (per fixture: `pred_change` (the pair `{common, added}` for ABL-SA1b), `mech_change`, `access_only`, `dynamics_credit`, token or "not applicable",
    `OLC`).
- **REP-INV:** per entry and alternative, `invariant` or the changed inputs; the transported frame; reclassifications.
- **B:** per fragment, `role` (`B-P`, `A-of-B`, `completion` or `B-C`), `preps`, `reads`, `effects_reduced`,
  `n_distinct`, `n_extreme`, `d`, `r_S`, `r_E`, `rank_added`, `lp`, `decided_by`, `pivots`, `max_bits`, `work`,
  `cert_sha256`, TOMO, `lp_reads_equal_acc`, completion, and the cap or budget exceeded where `out_of_scope`;
  `bp_equals_qmp` per arm (D22 (a)); B1; the B token with its codes (D21 (b)). Only B-P's record decides the token
  (D19 (ii)(b), (iii)(c)).
- **C:** per `(g, π)`, the orbits and `HC`, `CONS`, `VAL`, W-CL in both frames, W-OCT, ABL, EMB, C-A; `flagged`; the
  diagnostics of Appendix D.2 (D1(a); depth 1, D20 (b)), labelled "depth 1"; the C token with its codes.
- **Shared:** `fixtures` and `controls` (raw counts); `budget` (the general triple, B-P's triple and caps, and
  `S_max`; C.8 items 1 and 2); `flags`.

In fixture mode, every decisive field is a placeholder (`lp: "placeholder"`, `complete: false`).


### C.6 Stop rule (copied; edit applied)


**Host VOID, defined (re-review B3(d); by conclusions, r9 B3(b)).** A host VOID is an approved dispatch in which B4
never ran. In attempt 1's jobs records of the job named `Numerical probes / ARP-2-QC21 exact decision (gated)`, that
means one of:
- the job is absent;
- B4 is absent;
- B4's `conclusion` is `skipped`.

That covers a B3 failure, the ref key included, and a job B that the host did not start.

`started_at` is not used, because skipped steps carry one. A host VOID may be retaken only by a **fresh** dispatch: a
new `run_id`, at attempt 1, under a recorded owner decision made after the void-run record and its sha256 are posted,
with its own approval entry. A re-run attempt is never a retake.

**Checker outcome.** Any of the following is a checker outcome, not a host VOID:
- a timeout, cancellation or crash in a run whose B4 ran: a B4 conclusion other than `skipped`, or a missing
  conclusion on a job B that timed out;
- any exit status other than 0.

A checker outcome halts the round with VOID, with **no retake, no re-run and no budget change**.

The round halts under `S12` on any of the following:
- a failed `check` at S1 or `E`;
- at S1, any checker outcome other than exit 0 with complete output (A3's exit 3 on a red fixture-mode
  control included: owner-approved R2 default, precondition 2);
- at `E`, a red fixture-mode control (owner-approved R2 default, precondition 2), a checker outcome, a
  replay mismatch, a failed S1 binding, or a `verdict` VOID arising from the checker;
- a host VOID without a recorded retake decision;
- any need to change the control plane after `F`. This includes any narrowing of a fragment or completion, any
  change to `P_max`, `B_max`, `W_max`, `P_max^BP`, `B_max^BP`, `W_max^BP`, `S_max`, the caps (B-P's included),
  `timeout-minutes` or the stress pin, and any addition of a fragment, completion, control or premise.

**After `F` (c.6724832474).** No opportunistic narrowing and no additional computational budget is admissible.
Undecidable cases receive the preregistered VOID of their own test (D21 (b)), or are reported (D19 (ii)(b),
(iii)(c)). No checker rerun is preregistered. A substantive token is not a halt.

**At a halt.** `W` restores `verify.yml` to `F`'s state and keeps the record. It adds the S1 artifact when one exists,
preserved as produced, the run or void-run record, `order.json` and the VOID note. Progression to ARP-3 stops.

### C.7 Design run, confirmation run and gate tests (adapted from QC22 preconditions 6, 6′ and 6″; not verbatim)

**Owner-approved B1 conclusion rule (2026-11-11, #1169 c.6784808669; C.7 6/6′, and C.3 at S1 and `E`).**
Use the complete structured host job/step records (§A.44), with no log-derived statuses. D's `verify.yml` must
contain, byte for byte and exactly once, the A42 job's and the ARP-1 keep step's `if:` guards, the axiom-report
step's `id` and the KTRANS marker's `if:` guard below; its A42 matrix must be the 15 listed parts; and the host's
job names must equal D's job names plus jobs A and B, with the A42 job present as its placeholder on `pull_request`
and as its 15 shards on `workflow_dispatch`. Steps are matched by their exact names.
In a design/confirmation `pull_request` run:
- The exact job `Numerical probes / A42 exclusion (${{ matrix.part }})` is the **one skipped matrix placeholder**;
  on `workflow_dispatch` its 15 explicitly listed shards must all succeed. Guard:
  `if: ${{ github.event_name == 'workflow_dispatch' }}`.
- The exact step `ARP-1-MARC keep the measurements` is `skipped`; on dispatch it must succeed. Guard:
  `if: ${{ always() && github.event_name == 'workflow_dispatch' }}`.
- `KTRANS-SEP-2 axiom reports within the three axioms` must succeed, and the exact later step
  `KTRANS-SEP-2 marker complete reports with an axiom outside the three` must be **skipped** on **every event**.
  Its original guard is
  `if: ${{ !cancelled() && steps.ktrans_sep2_axioms.outputs.reports == 'complete-nonstandard' }}`.
  Marker `success` is a failure: it denotes an axiom outside the permitted three, not a positive test.
- Job B remains `skipped` for design/confirmation PR runs and is required to succeed on legitimate decisive dispatches;
  all other required jobs and steps must succeed. Missing/extra/duplicate jobs, any other skipped job or step,
  incomplete pages/attempts, guard drift or a different A42 matrix fail closed.
The exact permitted statuses must be mutation-tested in both directions: a wrongly successful PR-only step/job,
a failed A42 job, a skipped dispatch-required item, a successful KTRANS marker or skipped axiom-report step, an
additional skip, a missing matrix shard, a changed matrix, a renamed keyed step, a changed keyed guard or `id`,
or a missing or renamed job must each fail. This B1 amendment changes only the acceptance interpretation,
not the source or scope of any scientific operation. It does not approve a design run.

**6. The design run.**
- A disposable branch carries the predicted S1 tree, with fixture-mode output (the checker run with `--event fixture`; C.8 item 10). Its `pull_request`
  run satisfies the exact B1 job/step conclusion table above, with job B `skipped`. Its pull request's base is a branch held at `D` (*Synthetic merges*, below).
- `design-run.json` records:
  - every job and step conclusion;
  - each step's `started_at` and `completed_at` from the jobs API;
  - the artifact sha256s;
  - the base and head `sha` of the run's `pull_requests` entry.

  Its sha256 is pinned (PENDING).
- The self-tests, every mutation of C.4 included, pass.
- **A3 at the design run** (ARP-3-QC22 r14a review, Rc1). The design branch is a recorded branch, and the design
  run decides the fixtures under no budget, so a design run whose A3 starts and leaves no fixture-mode output (a
  timeout or a crash) violates the no-unapproved-F1 rule. It is found at S1's capture, after `F`, and voids the
  round. C.3's executor precondition (A3's command completed locally on the tree) therefore applies before the
  design branch is pushed. A design run that is red for another reason, A5's timeout included, is not a
  violation, and C.8 item 2's lowering rule applies to it.
- No decisive family has been built.
- The stress step's `stress.json` is retrieved by the executor from the run's artifact; its pin is bound by A7's
  `success` in the confirmation run (C.8 item 7). Every stress fixture that is decided is
  certificate-verified (an ST-BP instance over `S_max` is recorded `over_maximum`; C.8 item 2), and its sha256 is
  pinned (PENDING).
- ST-BP runs in A5 (C.8 item 2), under the owner's `S_max`, recorded before the design run (initial value 100000, owner-approved;
  precondition 2, R1).
- The general `P_max`, `B_max` and `W_max` (C.1's mechanical rule, the ST-BP instances excepted), and B-P's caps and
  `P_max^BP`, `B_max^BP`, `W_max^BP`, are set by C.8 item 2's rule (PENDING).
- The timeout test, with C.8 item 2's left side, is recomputed by `check --freeze` from the pinned records. If it
  fails, no `F` is requested.

**6′. The confirmation run.**
- It is a second disposable-branch `pull_request` run of the exact predicted S1 tree, under the final caps,
  budgets and pin. It satisfies the exact B1 job/step conclusion table above, with job B `skipped`.
- `confirmation-run.json` is checked by `check --freeze` as QC22 6′ states. That covers:
  - its pin;
  - every conclusion matches the owner-approved B1 table above, including the two PR-only expected skips, the required skipped KTRANS marker, and job B `skipped`;
  - the pinned blobs in its tree;
  - `verify.yml` byte-equal to the frozen splice;
  - A3's `mode: "fixture"`, through A3b's `success`;
  - the stress pin;
  - its pull request's base `sha` is `D` and its head `sha` is the run's `head_sha`;
  - **re-derived from the host** (ARP-3-QC22 r14a, R14-N4): `derive-run` on the run id in the pinned record gives
    the same job and step conclusions, `head_sha` and `pull_requests` entry as `confirmation-run.json`. The design
    run is re-derived the same way against `design-run.json`, so neither record rests on the supplied copy alone.
- **`confirmation-measurements.json`** is the `fixtures.json` file inside 6′'s `arp2-qc21-fixtures` archive,
  copied by the executor; no condition binds the copy to that archive (ARP-3-QC22 r14a, R14-N4). C-STATELESS
  compares it with S1's committed `fixtures` section, and any fixture-mode output of the S1 tree yields that same
  section. A copy equal to that section can make C-STATELESS pass vacuously. A wrong copy would be visible
  only by comparing it with 6′'s archive, which no condition does; this check supplies no such binding (r14c-N7).
- C-STATELESS compares it with S1 at `E`.
- **Synthetic merges** (ARP-3-QC22 r14, R13-N9). The design run and 6′ are `pull_request` runs, which execute the
  host's merge of the pull request's head into its base, not `head_sha` itself. Each of their pull requests therefore
  has as its base a branch held at `D`, and its head descends from `D`, so the merge's tree is `head_sha`'s tree.
  `check --freeze` verifies this from the run record (`derive-run`): its `pull_requests` entry has base `sha` equal
  to `D` and head `sha` equal to the run's `head_sha`. A record without that entry fails the check; whether the host
  fills it is first seen in the design run's record.

**6″. The gate tests (non-Environment; re-review E10, R10-B5).**
- **Where they run.** On a gate-test branch carrying 6′'s exact tree. Each dispatch and re-run has its own recorded
  owner authorization (§A.43 item 4).
- **What no gate test can do.** None can compute a decisive family. Every gate test is off the round branch, so the ref
  key fails B3 and selects fixture mode in B4 and in the checker. GT-B3 also uses the all-zero input.

| test | dispatch | frozen expectation |
| --- | --- | --- |
| **GT-B3** | gate-test branch, `arp2qc21_decisive: true`, `arp2qc21_sha` = forty zeros | job B starts; B3 `failure`; B4 and B6 `skipped`; job A `success` |
| **GT-REF** | gate-test branch, input true, `arp2qc21_sha` = the gate-test commit | B3 `failure` on the ref key alone; B4 `skipped`. Its safety rests on three ref keys (B3, B4's expression, the checker), each verified statically by W and M-GUARD before the test |
| **GT-RERUN** | the owner re-runs GT-B3's run | attempt 2: job B `skipped` by its `if:` |
| **GT-PLAIN** | gate-test branch, no inputs | job B `skipped`; job A and the aggregate `success` |
| **GT-PR** | the design run's own `pull_request` run, and one `push` run | job B `skipped` |
| **GT-ACT** | on a dedicated disposable branch created from `D` (not a recorded branch; it carries neither the pinned checker nor the frozen names): an owner-authorized force-push of a disposable commit, then one `GET activity?ref=refs/heads/<GT-ACT branch>` | the entry appears with `activity_type` `force_push`. The entry is recorded in `gate-tests.json` (r11-N3; R11a-B1) |
| **GT-LIST** | a read-only check that the repository runs API lists runs of a workflow whose file was later deleted (a fixture workflow deleted on the gate-test branch) | listed |

- **The record.** `derive-run` turns each run into a gate-test entry. Together they make `evidence/gate-tests.json`,
  committed at S1, whose sha256 is pinned (PENDING).
- **On failure.** Any expectation not met means no `F` is requested.
- **Retention.** The gate-test branch is kept until `E`'s receipt is captured.

### C.8 Readings of the copied and adapted text (frozen; r13, r14)

Each reading fixes the meaning of a copied or adapted passage that the implementation found ambiguous or
unimplementable (PLAN §20, items 1–19). Edits to the copied text itself are rows 46–137 of the edit log
(rows 72–85 at r14, 86–98 at r14a, 99–108 at r14b, 109–126 at r14c, 127–130 at r14d, 131–137 at r15). C.1 stays verbatim; where a reading below
concerns C.1, it governs C.1's words.

1. **The caps (C.1; item 1; D19 (0)(c), (i)(a)).** C.1's caps count as D19 (0)(c) states: "preparation generators"
   are the extreme rays of `cone{a_p}`, found by item 15, and `n` in `C(n, d − 1)` is their number; "effects before
   reduction" are as D19 (0)(c) states. There are two sets of caps and two budget triples, all fixed before `F`
   (SG-2):
   - **B-P's caps and budget**, set from ST-BP by item 2's rule: at most PENDING extreme rays; `d ≤` PENDING;
     `C(n, d − 1) ≤` PENDING; at most 200 effects before reduction; `P_max^BP`, `B_max^BP` and `W_max^BP`
     PENDING. They govern B-P alone (owner-approved R5 default, precondition 2).
   - **The general caps and budget**, for every other fragment (owner-approved R5 default): construction
     A of B, B-P's completions, the B-C fragments and their completion, QM-P's restricted fragment and every fixture.
     The caps are C.1's as listed (16, 16, `10^5`, 200), counted as above. The budget `P_max`, `B_max`, `W_max` is
     set by C.1's mechanical rule, with each maximum taken over every non-decisive fragment that the design run
     decides except the ST-BP instances.
   - The values entered for B-P's caps and for both budget triples, here and in C.7, are copies of
     `check --freeze`'s printed recomputation from the pinned `stress.json`. `check --freeze` does not parse them; it
     compares the checker's constants with that recomputation (item 2; SG-2), and the checker's constants govern
     (re-review r14a-N7).
   - A fragment over its caps or budget is `out_of_scope`. What that voids is item 14's reading of C.1 under
     D21 (b).
2. **The stress fixtures and the stress test ST-BP (C.1; items 1 and 2; D19 (i)(a)).** The generator is C.1's frozen
   32-bit xorshift. "One instance per seed" means that each of SF-1 and SF-2 is generated three times, once from a
   xorshift state seeded with each of 20261108, 1 and 2: SF-1/20261108, SF-1/1, SF-1/2, and likewise SF-2. A seeded
   coset is `c + span(g_1, …, g_k)` with `c` and the `g_i` drawn as bit vectors, redrawn until the `g_i` are
   independent.
   - **SF-1**, B-P's shape. `Ω = F_2⁵`, its bits named as B-P's read slots `(u_s, a_0, a_1, p_0, p_1)`. There are 32
     preparations, B-P's count (D19 (i)(a)). Preparation `j` is uniform on a seeded coset of seeded dimension
     `k_j ∈ {2, 3, 4}`, redrawn until it differs from every earlier coset of the instance, so the 32 laws are
     distinct. That is the shape of B-P's laws: P's step is affine over `F_2` and its unknowns are uniform, so each
     preparation's law on the read slots is uniform on a coset. The effects are the indicators of `Acc(B-P)`'s 50
     outcomes on these bits, and the unit effect.
   - **SF-2**, B-C's maximal shape. `Ω = F_2⁴`, U′'s configurations. There are 91 preparations, each uniform on a
     seeded coset of seeded dimension in `{1, 2, 3}`, and the effects are the indicators of `f_z`, `f_x` and `f_y`
     with values 0 and 1, and the unit effect. In `--stress` each SF-2 instance is decided under no cap and no
     budget, as C.1's stress fixtures are, and enters the general budget's maxima (item 1; owner-approved
     R3 default, precondition 2).
   - No stress fixture has a frozen verdict. `stress.json` records each verdict, its deciding step and its
     certificate.
   - No diagnostics benchmark is run (D20 (b)).
   - **ST-BP, the stress test of D19 (i)(a)** (frozen; synthetic; it builds no decisive family). It is part of
     `qc21_check.py --stress` (A5), so it runs in the design run, at 6′, at S1 and at `E`, and A7 compares its output
     with the pin.
     - **Inputs.** The three SF-1 instances above, at 32 preparations each. `S_max`, the owner's maximum budget: the
       largest number of `(d − 1)`-subsets that one facet enumeration may visit, in the solver and again in the
       verifier (its form and bound: owner-approved R1 default, precondition 2). It is fixed by a
       recorded owner decision before the design run, and entered on the line below and in the checker as `S_MAX`.
       C.1's frozen job limit `timeout-minutes: 60` and its timeout test, with the left side below.
       - **`S_max`** = 100000
     - **`S_max` checked** (`check --freeze`). The line above occurs once in this file, and its value is a decimal
       integer of at least `10^5`, R1's floor (owner-approved R1 default, precondition 2; R1's lowering
       rule can remove the floor from this check before a design run). It equals the checker's `S_MAX` and the
       `S_max` recorded once in the pinned `stress.json`. Otherwise `check --freeze` fails.
     - **Procedure, per instance** (exact; no wall clock): the factorization; step 1; the extreme-ray reduction of
       item 15 with each removal verified, under no budget; then `n` (the extreme rays), `d` and `c = C(n, d − 1)`
       are recorded, with `n_distinct`. If `c > S_max`, the instance is recorded `over_maximum` and is not decided.
       Otherwise it is decided by steps 2–4 under no budget and verified, and its verdict, deciding step, pivots,
       maximum bits and work are recorded, counted over the reduction and steps 3 and 4 as item 15 and C.1 step 6
       count them.
     - **Pass rule.** An instance passes iff `c ≤ S_max` and it is decided, feasible or infeasible, with its
       certificate verified. No verdict is expected.
     - **Its record.** In `stress.json` (schema v2), each ST-BP instance carries `n_distinct`, `n_extreme`, `d`, `c`
       and `over_maximum`, and, when decided, C.1's per-fragment fields; `S_max` is recorded once. Where C.1 says that
       every fragment in `stress.json` is certificate-verified (`--stress`, `stress-check`), it means every decided
       fragment: an instance recorded `over_maximum` carries no certificate and does not fail `stress-check`.
     - **The caps and budget for B-P** (mechanical; recomputed by `check --freeze`). The passing instances are taken
       in decreasing order of `c`, ties in seed order. The reference instance is the first of them for which the
       timeout test below holds when B-P's caps and budget are taken from it. The test's left side includes the
       reported-only term `1203 · W_max`, so the volume of reported-only fragments can move the reference to a
       smaller instance, or leave none (owner-approved R4 default, precondition 2). Then:
       - B-P's caps: at most `max(16, n_ref)` extreme rays, `d ≤ max(16, d_ref)`, `C(n, d − 1) ≤ max(10^5, c_ref)`,
         and at most 200 effects before reduction;
       - B-P's budget: `P_max^BP := max(P_max, 3 × pivots_ref)`, `B_max^BP := max(B_max, 3 × bits_ref)`,
         `W_max^BP := max(W_max, 3 × work_ref)`, with the general triple of item 1.
     - **Failure rule.** If no instance qualifies as the reference, no SF-1 instance was decided within `S_max` with
       the timeout test holding. SF-1's instances are seeded synthetic fragments of B-P's size and shape, not B-P's
       worst case, so this measures the method at that size and is not a result about B-P. B-P then takes the
       copied caps (counted under (0)(c)) and the general budget. A B-P that exceeds them is `out_of_scope`, and B is
       VOID as a reported limitation (D19 (i)(a); SG-2). B-P is not narrowed, and no cap, budget or `S_max` changes
       after `F`.
     - **The timeout test, this round's left side** (C.1's, read here):
       `σ × (W_max^BP + 1203 · W_max + 2·W_fix + W_stress) + t_810 ≤ 1200`. The count 1203 is the decisive
       fragments other than B-P: B-P's two completions, construction A of B, at most 600 B-C fragments and at most
       600 B-C completions. `σ`, `W_fix`, `W_stress` and `t_810` are C.1's, and `W_stress` includes the work of the
       decided ST-BP instances. If no instance qualifies as the reference, the test is evaluated with
       `W_max^BP = W_max`; if it then fails, no `F` is requested. The count 1203 and SF-2's treatment in `--stress`
       are owner-approved R3 defaults, and REP-INV re-decisions are excluded under approved R7 (precondition 2).
     - **C.1's per-job bounds** (the shared method's R13-N8, as ARP-3-QC22 r14 states it). C.1's "the sum covers
       both" reads: each per-job bound is at most the left side, and each job has its own 60-minute limit. With this
       left side, job B's bound is `σ × (W_max^BP + 1203 · W_max + W_fix)`; the sum of the two bounds,
       `σ × (W_max^BP + 1203 · W_max + 3·W_fix + W_stress) + t_810`, is not what the test bounds.
     - **Residuals of the timeout test.** B-P's facet enumeration is charged only through `σ`, calibrated on A5,
       where the reference instance enumerates `c_ref` subsets at rank `d_ref`. B-P's caps admit `d` up to
       `max(16, d_ref)`, and a subset's rank check costs more at a larger `d`, so a B-P with `d > d_ref` is
       under-charged by that per-subset excess. Job B's time for P, REP-INV, C and the diagnostics has no term
       (*Runtime*). A timeout from either is an incomplete-output halt (D21).
     - **Before the design run.** The design run's A5 must complete within job A's `timeout-minutes: 60`. A design
       run whose A5 times out is red. After a red design run, the owner may fix a positive `S_max` no larger than
       the red run's, by a recorded decision before another design run; it is at least `10^5` unless the red
       run's `S_max` was at most `10^5`, in which case the same decision removes the floor (R1's floor and
       lowering rule: owner-approved R1 default, precondition 2; re-review r14b-B2). `S_max` never
       depends on decisive data.
       `qc21_check.py --stress` refuses, with exit 4 and no output, while `S_MAX` is unset, so no ST-BP instance is
       decided before the owner's `S_max` is entered. No tree carrying the frozen splice is pushed before the design
       run is authorized, since a push runs `verify.yml` (§A.43 item 4). The scripts' self-tests of item 2's rule read
       synthetic `stress.json` records only, never an SF-1 instance.
3. **Replay (C.1, C.2, C.5; item 3).** `controls.py replay <run output>` compares the run's B4 output with
   `<record dir>/evidence/measurements.json`. Each is parsed with `json.loads`, `parameters.dispatch_sha` is removed
   from both, and the serializations `json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)`,
   encoded as UTF-8, are compared byte for byte. It exits 0 on equality and 3 otherwise. When the committed file is
   absent from the checked-out tree it prints `{"replay":"not-applicable"}` and exits 0.
   - At S1 the committed file is absent (it is added at `E`), so B6 is `success` with "not-applicable".
   - At `E`, control R requires the file, so "not-applicable" cannot arise there.
   - **The S1 binding (D21 (b); re-review R13-B1), as ARP-1's verdict did.** `verdict` at `E` reads S1's
     measurements artifact and compares it with the committed file:
     - `GET actions/runs/{DEC}/artifacts` for S1's run (every page) must list exactly one artifact with B5's frozen
       name, `arp2-qc21-measurements` (row 88), whose `workflow_run.id` is S1's run id and whose
       `workflow_run.head_sha` is S1;
     - `GET actions/artifacts/{DEC}/zip` (a frozen template) returns its archive as bytes, whose sha256 must equal
       the artifact's `digest` (`sha256:` followed by the hex digest);
     - the archive is opened in memory, `zipfile.ZipFile(io.BytesIO(<bytes>))`; its member list must be exactly
       `["measurements.json"]`, and that member is read;
     - it is compared with the committed `evidence/measurements.json` by the comparison above, `parameters.dispatch_sha`
       removed from both.

     A failed condition, including an artifact that is missing, expired or unreadable, makes `verdict` print VOID
     (fail-closed; for an expired or deleted artifact, owner-approved R6 default, precondition 2). A
     rate-limited or 5xx response is a failed capture, retried (C.3). No file is written.
   - **The binding's record at `E`** (§A.42 items 2, 7 and 8). `derive-run`, run on S1's run before `E` is committed,
     records in `evidence/s1-run/results.json` the binding's inputs: the artifact's `id`, `name`, `digest`,
     `workflow_run.id`, `workflow_run.head_sha` and `expires_at`, and the archive's member list, read in memory as
     above. `verdict`'s S1 binding also requires its own read to equal that record. S1's artifact is support for the
     binding when it is read, and provenance after it expires; the enduring support is `E`'s committed
     measurements, this record and a dispatch at `E` (§A.42 item 7).
   - The note states that the committed measurements are bound by B6 at `E`, and to S1's output by the S1 binding.
   - Wherever C.1 or C.2 says that B6 makes "a byte comparison" or "compares bytes", this comparison is meant.
4. **`cert_sha256` (C.4's C-INDEP, C.5; item 4).** `qc21_check.py` does not import `hashlib`. `cert_sha256` is computed
   by `h_sha256(data) → str`, a pure-Python SHA-256 (FIPS 180-4) in its own namespace `h_*`. C-INDEP's rules do not
   admit it among the calls a `v_*` function may make. The checker's self-test (A8) checks three FIPS 180-4 examples:
   - the empty message: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
   - `abc`: `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`;
   - `abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq`:
     `248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1`.
5. **The refusal, the entry and `os` (C.4, C.5; items 5 and 6).**
   - `qc21_check.py` has one refusal function, `s_refusal()`. Its body checks `s_mode(sys.argv, os.environ) ==
     "decisive"` and raises otherwise.
   - The first statement of `s_decisive` and of every registered builder is the expression statement `s_refusal()`.
     Apart from its `def`, `s_refusal` is referenced nowhere else.
   - The entry function is `s_entry(argv, environ)`. It calls `s_mode(argv, environ)`, refuses with exit 4, runs
     fixture mode, or calls `s_decisive()`. The block `if __name__ == "__main__":` calls
     `s_entry(sys.argv, os.environ)`.
   - `os` therefore occurs at exactly two sites, each the expression `os.environ`: inside `s_refusal`, and inside the
     `__main__` block.
   - M-GUARD's synthetic-environment cases call `s_entry` with synthetic mappings. None of them is a mapping on which
     all four keys hold, so none reaches `s_decisive`. `t_builder_refuses` runs once, under A8's real environment.
6. **The decisive builders (item 7).** `DECISIVE_BUILDERS` is the module-level tuple
   `(s_build_p, s_build_repinv, s_build_b, s_build_c)`:
   - `s_build_p`: P's arm classes `Adm_A` and `Adm_B`, and the ablations;
   - `s_build_repinv`: REP-INV on decisive data;
   - `s_build_b`: B-P, construction A of B and B-C;
   - `s_build_c`: C's test-rule orbits, ABL, the C-A runs, and, under D1(a), the diagnostics.

   The decisive-mode controls are computed from these builders' outputs.
7. **The fixture-mode marker (C.2, C.3; item 8).** The no-unapproved-F1 rule reads A3b's conclusion from the jobs API,
   and no artifact content. The one artifact a condition reads is S1's measurements artifact, by `verdict`'s S1
   binding (item 3; D21 (b)), through the frozen template `actions/artifacts/{DEC}/zip`, in memory. `derive-run`,
   run on S1's run before `E` is committed, reads the same archive only to record the binding's inputs (item 3).
   A non-dispatch checker-bearing attempt at a recorded-branch commit whose A3 started and whose A3b is not
   `success`, because A3's output is missing or not fixture mode, is therefore a violation (C.3's named
   residual). A red A3 whose output is complete fixture-mode output, a fixture mismatch for example, is not: A3b
   runs `always()` (C.2; ARP-3-QC22 r14a, R14-N10; re-review r14b-N1). Nor is an attempt whose A3 never started,
   absent or `skipped` (C.3; ARP-3-QC22 r14a review, Rc1).
   - **Artifact digests.** The artifacts API returns the `digest` of the uploaded archive, not the sha256 of the file
     inside it. Where the copied text names an `artifact_sha256` (C.1's link of the stress pin to the artifact, C.3's
     *The run at a stage*, C.7's design-run record), it is that `digest`, recorded as provenance; no condition compares
     it with a file's sha256. The S1 binding compares S1's measurements archive, not a file inside it, with its
     `digest` (item 3). The stress pin is bound instead by A7's `success` in the confirmation run (6′), and the
     committed measurements by B6 at `E` (edit row 57).
8. **`"workflow_dispatch"` in `controls.py` (C.5; item 9).** It occurs only inside the module-level string constants
   named `SPLICE_*`, which hold the frozen splice byte-exactly for control W, and inside functions named
   `run_class_*`, which `derive-run`, `order`, `verdict` and `e-entry` call (re-review r14b-N6).
9. **`order` and `verdict` (C.3, C.5; item 18).** Both are implemented and frozen at `F`. Their inputs that exist only
   after `F` are supplied at each capture:
   - the stage commits S1 and `E`, as `a_ok` HEX40 arguments;
   - the approval entries, in `evidence/approvals.json`, schema `arp2-qc21-approvals` v1, one entry per decisive
     dispatch made before `E` is committed (S1, and any retake), with the fields of C.3, written by the executor
     from the owner's comments and ratified at `E`. The entries of the dispatches at `E`, the `E` dispatch and any
     retake of it after a host VOID, cannot be in `E`'s tree: `verdict` builds one for each `E`-stage approval
     comment id given as an argument, verifies it as C.3 states, and prints it in its record (ARP-3-QC22 r14,
     R13-B4; r14a, R14-N2). Every comment `order` and `verdict` read is read through the frozen template
     `issues/comments/{DEC}` (rule (g); re-review R14A-B1, R14B-B1);
   - the ids of the owner's comments that `order` and `verdict` read besides the approval comments, as `a_ok` DEC
     arguments: `F`'s designation (C.3's `order.json` rule; re-review R14B-B1) and the designation of `E`.
     The approved R8 alternative uses that designation for each E-entry digest; no separate ratification id;
   - `T_repo`, read at each capture from `GET` on the repository.

   **The `E` dispatch's entry and its ratification** (re-review R14A-B1, r14a-N3). `order.json`, which the
   designation of `E` ratifies by sha256, is in `E`'s tree and so cannot hold that entry. The designation itself
   follows the `E` run, `E`'s exact-head run (§A.39), so it could quote the entry's sha256. Which owner act ratifies
   the entry is precondition 2's R8. Before `verdict`'s capture, `controls.py e-entry <E> <comment id>` builds the
   entry with the function `verdict` uses, checks it as C.3 states, and prints it as canonical JSON with its sha256;
   it prints no `VERDICT` line and decides nothing. Under the approved R8 alternative the owner's
   designation of `E` quotes that digest, beside `order.json`'s digest, for each E-stage entry. `verdict`
   prints `VERDICT VOID` unless the designation passes owner/OWNER checks and quotes every required digest.
   This is an operational landing condition under R10, not a permanent assertion that unretained checks passed.

   **Several dispatches at `E`** (ARP-3-QC22 r14a, R14-N2). Wherever this file says "the `E` dispatch's own entry"
   or "the `E` dispatch's entry", it means each entry `verdict` builds for a dispatch at `E`: the `E` dispatch's,
   and that of any retake at `E` after a host VOID. `e-entry` is run once for each such approval comment id, and
   R8's designation-based ratification covers each. Under approved R10 narrowing these are conditions of
   landing only; their unretained host-time content establishes no enduring approval/ratification claim.

   **The first execution run** (C.3's `order.json` rule; re-review R14B-B1) is the earliest-created run, of any
   event, whose `head_sha` is a strict descendant of `F` (other than `F`) on the round branch. `order` finds
   it in its enumeration; ancestry is checked with the admitted `merge-base --is-ancestor`.

   `T0` is a frozen constant of `controls.py`, entered when the round PR is opened and before `F`. Before `F` both modes
   run only in the self-test, on synthetic records. Their first real run is the capture of `check --stage S1`, where a
   fault is a failed capture.
10. **`--fixture-output` (C.7; item 19).** It is not a checker flag. It names the checker run with `--event fixture`,
    A3's literal.
11. **The output directory (C.2; item 14).** A3 and B4 each create `$RUNNER_TEMP/arp2-qc21` with `mkdir -p` before the
    redirect (rows 46 and 47). A3b, A5, A7 and B6 run after them in the same job.
12. **The STAB-FALSE certificates (the certificate location).** `evidence/cone_k1_certificate.json` and
    `evidence/cone_window_K2_certificate.json` are in the record directory in every tree the workflow runs on from the
    design run onward (design, confirmation, gate-test, S1 and `E`). `controls.py --self-test` (A9) reads them and
    checks each against its sha256 pin before use; control P pins both and control R requires both from S1 onward.
    They are inputs, not run records, so "the record files" by which the design tree differs from S1 (C.2) do not
    include them. `qc21_check.py` reads no file, and its checker-side STAB control is STAB-TRUE alone.
    - **Where STAB-FALSE's result is recorded.** STAB-FALSE runs in A9, in job A, in its own interpreter, which
      builds no decisive family. Its result is A9's step conclusion, which `verdict` requires to be `success` at S1
      and `E` (C.3). It is not in `measurements.json`, so C-STATELESS does not compare it. This placement is intended:
      C-STATELESS compares fixture decisions within its intended B4-process scope; interpreting it as evidence
      about shared state requires an authentic 6′ reference copy, which the procedure does not establish (C.7).
      STAB-FALSE never runs in B4's process; its inputs are pinned files, so its conclusion at the design run, at 6′,
      at S1 and at `E` re-checks the same computation. The note's control table prints STAB-FALSE as "A9: {conclusion}",
      from the derived run results.
13. **Which B fragments decide `decide-b` (item 13; D19 (ii)(b), (iii)(c)).** `decide-b`'s steps 1–3 read B-P alone,
    with the B controls. Construction A of B, B-P's completions and the B-C fragments are reported as measured: each
    is decided where it is within the general caps and budget (item 1; owner-approved R5 default), and
    otherwise reported `out_of_scope` or `undecided`. None of them decides or voids a B token or a Level. A B-C
    result enters `decide-levels` only through UPR-BC's label.
14. **Test-level VOID (D21 (b); C.1, C.4, C.5, C.6).**
    - Wherever C.1 says that a fragment over a cap or a budget, or one for which neither certificate verifies, makes
      the checker exit 3 or the round VOID (step 6; *Caps*; the verifier's "Neither verifies"), it reads: the fragment is
      recorded `out_of_scope` or `undecided`. If it is B-P, `decide-b` gives B-VOID. If it is a reported-only
      fragment, the record is reported. The checker exits 0 when the output is otherwise complete. C.1's statement
      that a timeout is a checker outcome stands.
    - A red decisive-mode control (*Control modes*) voids the token of each test in its `for` column. C.4's controls
      are B controls. A control whose `for` column reads "all" voids every token.
    - Fixture mode's exit rule (C.1) is unchanged. It governs A3, whose controls are fixed green at 6′ on the exact
      S1 tree. A red fixture-mode control at S1 or `E` is therefore a reproducibility failure: job A fails, `verdict`
      prints VOID, and the round halts with every result void (SG-3; owner-approved R2 default,
      precondition 2).
    - C.1's "The default exit rule (0 when complete and green, 3 otherwise) applies in decisive mode only" reads: in
      decisive mode the checker exits 0 when its output is complete, and a red control voids only what this item
      states.
    - `verdict`'s token line (C.3; rows 89 and 90) carries the P, B and C tokens, VOID ones included, and the Level.
      `VERDICT VOID` is printed only for a round-level failure: a failed `verdict` condition of C.3.
    - The edits to C.2, C.3, C.4, C.5 and C.6 for D21 (b) are rows 72–90 of the edit log.
15. **The extreme-ray reduction (D19 (0)(c); C.1 step 1 and the verifier).** It follows step 1. The cap on effects
    before reduction and the cap on `d` are applied before it; the caps on `n` and on `C(n, d − 1)` after it, with
    `n` the number of retained rows.
    - The rows `a_p` are taken in the frozen preparation order. A row is removed when it is a nonnegative combination
      of the rows still retained other than itself. That is decided by a phase-1 simplex on `Σ_q λ_q a_q = a_p`,
      `λ ≥ 0`, with step 5's arithmetic and pivot rules, drawing on the fragment's budget (step 6) as step 3 does. A
      feasible solution is the removal certificate `(p, {q: λ_q})`.
    - Every row satisfies `b_u · a_p = 1`, so `cone{a_p}` is pointed, and the retained rows are one row for each
      extreme ray. They generate the same cone, so its facets, and every decision of steps 2–4, are unchanged.
    - **The verifier.** The certificate carries the retained indices and the removal certificates, in their removal
      order, as plain data (C-INDEP). The verifier checks the removals in that order, each exactly: `λ ≥ 0`,
      `Σ_q λ_q a_q = a_p`, and every `q` a row other than `p` not removed before it. By induction every removed row
      then lies in the cone of the final retained rows. It then enumerates the facets over the retained rows only,
      which is sound for that reason. A failed removal check makes the fragment `undecided`.
    - **Models cover removed rows.** A feasible model is defined on every preparation, removed rows included: in
      steps 2 and 3 `μ_p` is the preparation's own charged law, and in step 4 `μ_p(j) = (g_j · a_p) s_j` is linear
      in `a_p`, so a removed row's law is `Σ_q λ_q μ_q`. The verifier checks reproduction of its own `N` on every
      preparation, removed ones included (C.1, *Feasibility*). B-RAY-F exercises this on step 4's feasible branch.
    - **Its controls.** The fixture-mode control B-RAY (B-RAY-S, B-RAY-P, B-RAY-F; *The controls*), and the mutation
      M-RAY (row 76): in B-RAY's certificate, one removal multiplier altered; and, separately, an extreme row removed
      under a fabricated certificate. Each must fail C-CERT.

## Appendix D. Passages carried from the round's r5, r6 and r7 drafts, stated here (r13 item 11)

The body refers to this appendix wherever it carries a passage of the round's r5, r6 or r7 draft. Each passage is
stated here in full. Where a later draft carried an earlier passage with changes, the changes are applied here, and the
earlier drafts' token names are replaced by this file's. Rows marked *verbatim* are copied unchanged from the named
draft. The drafts are scratch files and are not on `main`; they are cited as provenance only (§A.42 item 8), and no
claim of this round rests on them: `r5/preregistration-r5.draft.md`
(`d82af33cf3c4aeebdb240bc33ea4b75c7f30f439ba2045f5a745c9ac79eea115`), `r6/preregistration-r6.draft.md`
(`0120357a8b7d88ac7deed247656b3e1fde0255e3e11f175138df117df4efdb44`) and `r7/preregistration-r7.draft.md`
(`e75f0bc6a343cfb5942e0515d650b502ba1a75c3a1b0de69fdee97651f96e6b7`).

### D.1 Inputs carried from r5 (verbatim rows)

`R/` = `verification/programmes/oi-qm/reconstruction/`. These rows stand beside the rows of *Inputs*, which replace
r5's AP1, RCH and M-ARC rows.

| short | path | blob | used for |
| --- | --- | --- | --- |
| QA | `R/quarter-phase-native-20261107/DESIGN.md` | `fb21999b0d45750a465dda742589f0af11575326` | U′ (QA:448-450); the family `Λ_{a,b}, Λ_0` (QA:580-601); class N and posits (QA:128-152, ledger :770-790); C-ROT (QA:646-651) |
| FB | `R/quarter-phase-feedback-20261107/RESULT.md` | `a00b3b7f28992fd2c0010836d50e7c89ab158088` | the native read returns `f_a` (FB:43-44) |
| M2D | `R/mechanism-2-20261108/DESIGN.md` | `9352d9da7da6a55a52e6ada235034219638b34d2` | Lemma F's operation set (M2D:307-341); Lemma Qσ (M2D:593-625); P★ (M2D:630-703); the non-injective route (M2D:717-727) |
| MI-R | `R/minacc-1-20261108/RESULT.md` | `5adf76ebc8afa95cc51f45fb84c909b13876516c` | `G_σ` breaks AP1 Lemma 3's isotropy (MI-R:34-77); C-LIN and PROT-R (MI-R:394-442) |
| SUB | `papers/Substratum.md` | PENDING (at `D`) | A2, A4, A5 (the partly-derived status of affinity) |

### D.2 The diagnostics (D1(a); depth 1, D20 (b))

The diagnostics are r5's direct-access quantities: r5's classification of every rule on `L_scope(g)` (Appendix A),
computed in job B for all eight rules, labelled "diagnostic", and read by no token, no Level and no ADA status rule
except where D.8 says "for the diagnostics". Their categories CANDIDATE, NONSTAB, STAB and INVALID are diagnostic
labels, not tokens. Under D20 (b), `L_scope(g)` for the diagnostics is bounded to depth 1: `S_0` and every one-round
output of an `S_0` law, normalized and deduplicated (27,600 one-round propagations). Appendix A's "Depth 2" does not
apply to them, and each diagnostic is labelled "depth 1". The method (*verbatim*, r5 *The exact method*):

- **Representation.** A carrier law is a map from `F_2^4` to `Fraction`; a joint law from `F_2^6`. `Φ_g^k` is
  precomputed as a permutation of `F_2^6`. A round forms the product law, permutes, conditions by a 0/1 mask on the
  registered slot, marginalizes the mediator, and normalizes by the herald. Deduplication compares exact values.
- **Classification of a rule.** `V(g) = {R(μ) : μ ∈ L_scope(g)}`. Counts: `outside_ball` (`|r|² > 1`),
  `nonstab_valid` (`|r|² ≤ 1` and `ℓ1(r) > 1`), `offaxis_unit` (`|r|² = 1`, `r ∉ {±e_a}`). For every round: herald
  constancy, the induced map if any, and for induced maps: orthogonal or not, `α = 0`, determinant, octahedral or not.
  Category: **CANDIDATE** when some round induces a unitary non-octahedral map, `outside_ball = 0`, and C-EMB holds
  for `g`; else **NONSTAB** when `outside_ball = 0` and `nonstab_valid > 0`; else **STAB** when `outside_ball = 0`;
  else **INVALID**. A non-octahedral induced map in an INVALID rule is reported in its own field, and so is
  `nonstab_valid` for an INVALID rule (the P★-like pattern: valid non-stabilizer laws together with laws outside the
  ball).
- **Branch structure (reported, not decided on).** For every one-round conditioned output of an `S_0` law:
  `nonaffine_branches` (support not a coset, or law not uniform on it), `nonisotropic_branches` (uniform on a coset
  whose determined set is not `ω`-isotropic), `sharp_branches` (`f_z` and `f_x` both determined).
- **Arithmetic.** `fractions.Fraction` and integers only. No floating point.

**Fixture laws used by C-AFFB (b) and by C-PLANT** (*verbatim* rows of r5's controls; in this round they define
fixtures only, and neither row is run as a control):

| code | what | green when | route to failure |
| --- | --- | --- | --- |
| **PC-PLANT** (positive) | REACHABLE §3.3's planted set: six disjoint-support laws with images `±e_a`, their mixture, and a stochastic `B_P` on their supports sending them to laws with images `±β₀ e_a`, `β₀` the 60° rotation about `(1,1,1)`; run through the same induced-map routine, with the planted laws in the roles of `Λ_{a,0}` and `Λ_0` | the routine reports exactly one induced map, equal to `β₀`, unitary, non-octahedral | a detector that cannot report a non-octahedral map |
| **PC-NONSTAB** (positive, for the `nonstab_valid` counter and the INVALID-with-nonstab field) | two runs separate from CC-NAT's `L_scope(0)` (their planted laws never enter any countercontrol's or test rule's set): (a) rule `0` with `S_0` plus one planted N2-departing carrier law, `z_1, x_1 ~ Bern(1/5)` independent and cell 1 uniform, image `(3/5, 0, 3/5)`; (b) rule `0` with `S_0` plus two planted laws: one uniform on `{x_1 = 0, f_y = 0}` (image `(1, 1, 0)`, outside the ball) and the same `(3/5, 0, 3/5)` law | (a) `nonstab_valid > 0`, `outside_ball = 0`, category NONSTAB; (b) category INVALID with the invalid-rule `nonstab_valid` field positive; both planted laws fail NE-1 (C-EMB (a)) | a `nonstab_valid` counter that never fires (wrong `ℓ1`, a strict/non-strict slip, a mask error), which would let NO-VALID-ESCAPE stand over an untested detector; a missing INVALID-with-nonstab report |

### D.3 C's model, beyond Appendix A (*verbatim*, r6 *Obligation C*)

"Changes from r5" below means changes from Appendix A.

**The model.** r5's *The model* (Appendix A, verbatim) for the ring `Z_3`, U′ on cells 0–1, the rule family `Φ_g`
(four non-affine test rules AND, NAND, OR, NOR; four affine rules 0, 1, XOR, XNOR), the mediator supplies `M`, the
150 rounds `π = (m, k, reg)` in their frozen order, forward conditioning, terminal registration, and the frame
convention. Changes from r5:
- **Source** `Q` = the QA family `Λ_0`, `Λ_{a,b}` (7 laws; `Λ_{y,b}` under NNB). r5's 16 P2 products are dropped
  from C (they enter only r5's diagnostics).
- **Orbit** `O_K(g, π) = {π^j Λ : Λ ∈ Q, 0 ≤ j ≤ K}`, normalized, with a fresh mediator for every application;
  `K ∈ {6, 12}`.
- **Detectors** (observer layer; native rule `XOR` and P3 arming in every arm and ablation, L-HET): `S_Z` a ready meter
  `(w, 0)` armed to cell 0 for one tick, record `u_0`; `S_X` the same after one free tick, record `v_0`; `S_Y` the
  triangle round (ready `u_2 = 0`, two `XOR` ticks, register `u_2`). Each detector is applied to the orbit law and is
  terminal for its run. Record vector `ρ(μ) = (1, P_μ(S_X = 0), P_μ(S_Y = 0), P_μ(S_Z = 0))`.
- **Frame calibration** (L-CAL): `R_op` is the affine map on record vectors sending `ρ(Λ_0)`, `ρ(Λ_{a,0})` to `0`,
  `e_a`; consistency check `ρ(Λ_{a,0}) + ρ(Λ_{a,1}) = 2ρ(Λ_0)`. `R_op` is computed from records only.

### D.4 C's quantities (*verbatim*, r6 *Obligation C*; `STAB(K)`, W-CL's second frame, ABL's label, C-A and EMB as amended in *Obligation C*)

"r5's frame correction" is Appendix A's frame convention. "The eight spectra of `DESIGN-DS.md` §6" are the spectra of
the 3×3 signed permutation matrices, listed in `DESIGN-DS.md` §6 on `main` (precondition 3).

**Quantities** (exact).
- `HC(K)`: the gadget's herald (its mediator record) is positive and equal on every law of `O_{K−1}`.
- `CONS(K)`: with `Φ = (α, β)` fixed by `R_op(πΛ_0)` and `R_op(πΛ_{a,0})`,
  `R_op(π^{j+1}Λ) = α + β R_op(π^jΛ)` for every `Λ ∈ Q`, `j < K`. `β` is reported with `det_fix` and `det_enc` (r5's
  frame correction, per application).
- `VAL(K)`: `|R_op(μ)|² ≤ 1` for every `μ ∈ O_K`.
- `W-CL`: the unit-modulus eigenvalues of `β` with multiplicity (exact factorization of its rational characteristic
  polynomial; a quadratic factor `λ² + bλ + c` has unit roots iff `c = 1` and `|b| < 2`) form a multiset that is not a
  sub-multiset of the spectrum of any 3×3 signed permutation matrix (the eight spectra of `DESIGN-DS.md` §6).
- `W-OCT(K)`: some `μ ∈ O_K` has `ℓ1(R_op(μ)) > 1`.
- `ABL(g, π)`: the identical `π` with `g` replaced by each affine `g` and by the zero-tick round gives neither W-CL with
  `CONS(12) ∧ HC(12)` nor `W-OCT(12)`.
- `EMB`: NE-1, NE-2, NE-4, NE-5 of REACHABLE §3.3 (supplies in `N_sup`; forward conditioning on terminal records; frozen
  enumeration with one hash; `α, β` from outputs).

The C token is reported with B's result on the named instance (*verbatim*, r6): "classically imitable" when its B-C
fragment is feasible. Every flagged instance's B-C result is reported only (D19 (iii)(c)); where it is
`out_of_scope` or `undecided`, the note prints that word.

### D.5 C's frozen texts and the common clause (r6's, with *Obligation C*'s changes applied)

`{…}` marks a measured value interpolated by `note`.
- **C-EXPOSURE.** "For {g, π}, the gadget composed up to 12 times acts on the detector records (U′'s three
  functionals, read by native meters) as one fixed affine operation whose unit-modulus spectrum `{spectrum}` is not
  that of any Clifford-class map, with a constant herald, every orbit law inside the calibrated Bloch ball, native
  supplies and forward conditioning. `STAB(12)` is {true/false}." When `STAB(12)` is true, the next sentence is "With
  `STAB(12)` true, its rotations have order 3 or 6."; when it is false, no sentence about orders is printed. Then: "The
  identical gadget with the rule made affine, or idle (a change of dynamics), shows no such operation. With
  `reg = none` on the same `(g, m, k)` the witness {is/is not} present; record-dependent conditioning {is/is not} part
  of the origin. The detectors read the carrier linearly, so the records coincide with the R statistics; the frame is
  calibrated from the source labels. B's status of this instance: {B}. Composition alongside a second system, read and
  update statistics beyond the three detectors, and every branch's validity as a quantum instrument are not tested
  here."
- **C-SIZE-DEPENDENT.** The C-EXPOSURE text for `K = 6` (with `STAB(6)` in place of `STAB(12)`), followed by: "the
  operation is not a fixed operation on the records over 12 compositions: {which of HC, CONS, VAL fails}."
- **C-NONSTABILIZER** (*verbatim*). "No gadget acts as a non-Clifford fixed operation within scope. For {g, π}, orbit
  laws reach calibrated record coordinates inside the ball and outside the octahedron ({counts})."
- **C-SURVIVAL** (*verbatim*). "Within this scope no native non-affine gadget yields a non-Clifford fixed operation or
  a non-stabilizer valid orbit law on the detector records. This is a scoped finite search, exhaustive within its scope;
  it is not an impossibility statement." Then the witness principle, verbatim (D.8, Part 2).
- **C-VOID** (*verbatim*). "A required C control failed: {codes}. No reading is made."

**Common clause** (with every P, B and C text): "This concerns the finite models of this round: for P, one carrier
cell with phase, arm and screen cells under the class-N step of construction B (the OI substratum plus the
observational-incompleteness principles named in the ledger, each identified and tested separately), with supplied
arming; for B, the stated fragments; for C, the ring `Z_3` with the four non-affine symmetric rules in a gadget,
detectors of construction B, the seven QA sources, the 150 rounds and at most 12 compositions. It is conditional on
P2, N2, H-PREP, NNB (for `Λ_{y,b}`), P3 arming, E-iso, the supplied registration, the held unread cells, the refilled
mediators, and the imported identifications of path, port and U′. Nothing here concerns larger systems, other
alphabets, other identifications, a second system, or a physically sourced apparatus."

### D.6 C's controls carried from r5 and r6

**Rows carried from r6** (*verbatim*; "r5's PC-PLANT" is D.2's PC-PLANT row):

| code | for | fixture | green when | route to failure |
| --- | --- | --- | --- | --- |
| **C-STAB** | C | supplied Clifford maps (`H`, `S`, and their composite) as the gadget's action on `Q`, read through the detectors | no W-CL; no W-OCT; CONS holds | a stabilizer operation misclassified |
| **C-R60** | C | supplied 60° rotation about `(1,1,1)` | W-CL with spectrum `{1, e^{±iπ/3}}`; `VAL`; CONS | a witness that cannot fire |
| **C-35** | C | supplied rotation by `arccos(3/5)` about `z` | W-CL (non-root-of-unity pair); `VAL`; CONS | a witness that misses infinite-order rotations |
| **C-S3** | C | supplied rotoreflection `S_3` | W-CL with `{−1, ω, ω²}` | a witness that accepts an O_h-like spectrum by mistake |
| **C-PLANT** | C | r5's PC-PLANT stochastic map on six disjoint-support laws | W-CL fires; its laws fail NE-1 | a non-native supply passing EMB |
| **C-CONSX** | C | a supplied operation that is not one fixed map on the orbit (alternating between two Clifford maps) | CONS fails | composition consistency never failing |
| **C-DET** | C | the three detectors on all 16 point laws of U′ and on `Q`, under the native rule | `P(S_a = 0 | μ) = μ(f_a = 0)` exactly | a detector that does not read what it is said to |

**C-EMB** (*verbatim* r5 row; read on orbits as stated below):

| code | what | green when | route to failure |
| --- | --- | --- | --- |
| **C-EMB** (definitional embedding) | (a) PC-PLANT's and PC-NONSTAB's planted laws under NE-1; (b) every law of `S_0` and `M` (and every CC-MIX component) under NE-1, exactly the native class `N_sup`; (c) NE-3: for each test rule, the identical 150-round enumeration with `g` replaced by each of the four affine `g` (CC-NAT's computation) and by the zero-tick round (`k = 0`: attach, register, discard); (d) NE-2, NE-4, NE-5 statically: the round schema admits only `reg ∈ {none, (u_2, r), (v_2, r)}` read after the last tick, with the mediator discarded at once; the sha256 of the round enumeration is the same for every rule; `α, β` are computed only from outputs | (a) every planted law fails NE-1; (b) every supply passes; (c) the ablations reach only `O` and every induced map with `α = 0` and orthogonal `β` is octahedral; (d) holds | an NE-1 test that accepts any law; a supply outside the native class; an enumeration that differs by rule |

**Appendix B's controls and C-EMB, adapted to orbits.** Each reads as its Appendix B or D.6 row, with these
replacements:
- **CC-DYAD.** For every rule and every round with `reg = none`, on the orbit laws `O_12(g, π)` from `Q`: every
  coordinate of `R(μ)` has a power-of-2 denominator; no `μ` has `|R(μ)|² = 1` with `R(μ) ∉ {±e_a}`; and every fit
  `(α, β)` with `HC(12)`, `CONS(12)`, `α = 0` and `β` orthogonal is a signed permutation. Under D1(a) its Appendix B
  form also runs on the diagnostics, at depth 1 (D20 (b)).
- **C-AFFB.** On the diagnostics only, in its Appendix B form (D1(a)), over the depth-1 `L_scope(g)` (D20 (b)).
- **C-XB.** For every rule, every round and every law of `O_11(g, π)`, the one-application output is recomputed by
  direct enumeration of the 64 joint configurations with integer weights over a common denominator, sharing no code
  with the permutation path: `mismatches = 0`. Under D1(a), its Appendix B form also runs on the diagnostics' `S_0`.
- **C-FRAME.** Rule `0`, rounds with `k = 1`: every herald-constant such round has, on `O_12(0, π)`, the fit `α = 0`
  and `β` the transposition `x ↔ z` (`β e_x = e_z`, `β e_z = e_x`, `β e_y = e_y`), with `det_fix = −1`,
  `det_enc = +1` and `P^k β = I`.
- **C-STEP.** As Appendix B.
- **C-SCOPE.** `|Q| = 7`, `|M| = 5`, 150 rounds, the orbits reached to `K = 12` for every rule, `complete = true`.
  Under D1(a), also Appendix B's `|S_0| = 23` and depth 1 for the diagnostics (D20 (b)).
- **C-EMB.** (a) C-PLANT's laws fail NE-1; (b) every law of `Q` and of `M` passes NE-1; (c) NE-3 through ABL (each
  affine `g` and the zero-tick round, on the identical `π`); (d) NE-2, NE-4 and NE-5 statically, as in the row above.

### D.7 The S4 phrase screen (the lists of r5, r6, r7 and this file, joined)

A hit fails V. S4 is applied outside the frozen texts, and to them in the self-test. The owner's verbatim sentences
printed in the note, and the witness principle, are exempted by exact match. The phrases:
- "native protection", "is a theorem", "theorem-level", "proves", "proved", "never", "permanently", "in general",
  "for every observer", "physically justified", "establishes QM", "quantum mechanism", " iff ", "if and only if",
  "is equivalent to", "exactly when", "should not be read";
- "observed to be due", "quantum behaviour", "quantum behavior established", "proves quantum", "genuinely quantum";
- "native OI", "attributed to path recording", "excludes classical";
- "is due to recording", "caused by recording", "attributed to recording".

### D.8 The assumption-dependence analysis (ADA)

Separate from every token; no `decide-*` reads an ADA field. New variants are named as candidate rounds and not run.

**Part 1, the ledger.** The rows below, with the replacements listed after them, and the changes in the body's *ADA*.
Every row carries an A/B column: the construction and kind of its ingredient's row in *The A/B typing* where that
table lists the ingredient, and "—" otherwise.

*Rows carried from r5* (*verbatim*):

| id | assumption | type | source |
| --- | --- | --- | --- |
| L-BIJ | bijective second-order dynamics | native | SUB A2 |
| L-CF | center independence, both senses | native | SUB A4 |
| L-SYM | neighbour symmetry: `g` symmetric in its two arguments | native (E4-anchored) | SUB A4; SM form lemma |
| L-SYMP | symplecticity (symmetric, reciprocal couplings) | native; essential for Theorem C (RC1(c)); kept by the countercontrol rules, undefined for the test rules | QA:128-141; AP1:286-287 |
| L-ISOT | isotropy of determined sets | not assumed; reported (`nonisotropic_branches`); undefined for non-affine transport | AP1 Lemma 3; MI-R C-L3; M2D Lemma Qσ |
| L-P1 | terminal registration with the registered cell decoupled from every cell | imported (supplied). In this model it is implemented by removing the mediator at once after its slot is read, a supplied idealization; in the records it is enforced by P3/E-iso within a budget. Essential for Theorem C (RC1(b)) | AP1:292-296, :338-343 |
| L-NNB | armable symmetric center-free same-sublattice coupling | supplied conditional premise, not adopted; **used** only to supply `Λ_{y,b}` through H-PREP | QA:443-450; QA node 8 |
| L-FWD | forward conditioning: the time-`t` law conditioned only on records registered by `t` | access convention; essential for Theorem C (RC1(a); MI-R PROT-R) | REACHABLE §1.2; MI-R:435-442 |
| L-AFF | affine update | **uncertain**: affine part necessary given amplitude-scale gauge, whose derivation is an open step; carried both ways (native, then this round tests an extension; imported, then this round tests its removal) | SUB A5 |
| L-LIN | linear rather than affine | imported (imposed); not used by Theorem C | SUB A5 |
| L-Q2 | `q = 2` | **uncertain** (as in ARP-1's ledger); used essentially (characters ±1) | QA:460-464 |
| L-RING | the triangle, one mediator, depth 1 for the diagnostics (D20 (b)), `k ≤ 6`, single-round induced maps | imported (modelling reduction) | this file |
| L-P2 | ready cells with one known slot | imported (supplied) | AP1:297-299 |
| L-N2 | uniform unknown slots; H-INF-μ for infinite sectors | **uncertain** ("native measure, applied through H-PREP"; hypothesis on infinite sectors) | QA:777, :788 |
| L-HPREP | known value 1; the family `Λ_{a,b}` as preparations | imported (open hypothesis) | QA:782 |
| L-REG | registration of a mediator slot; mediator terminal | imported (SA-1(b), access part) | AP1:292-296 |
| L-REFILL | a fresh mediator each round | imported (supplied attach) | QA:142-144 |
| L-UPRIME | the linear identification U′ and R | imported (representation; R combines the native read with comparator I1's outcome rule) | QA:448-450, :116-117; FB:43-44 |
| L-I1 | comparator: single-qubit stabilizer, Lüders, CPTP; "unitary" as `α = 0`, `β ∈ SO(3)` | imported (comparator) | QA:108-117 |
| L-HCONST | herald constant on the reachable set | empirical (linearity of the induced operation on preparation mixtures, observable as consistency of statistics under mixing) | REACHABLE §1.4 |
| E-BALL | `r_x² + r_y² + r_z² ≤ 1` for every preparation | empirical | tomography of a qubit |
| E-NONCLIFF | QM predicts read statistics off the octahedron (e.g. spin reads at non-Clifford angles) | empirical (the target's observable anchor) | — |

*Rows carried from r6* (*verbatim*):

| id | assumption | type | where |
| --- | --- | --- | --- |
| L-PATH | the two "paths" are the two values of a carrier cell's encoded `z` | imported (representation) | P, B |
| L-SRC | coherent and single-path sources are supplied P2 ready cells | supplied (P2; H-PREP for value 1) | P, B |
| L-ARM | per-tick, per-edge arming (P3) and isolation (E-iso) select phase, arm and screen | supplied | P, B, C detectors |
| L-HOLD | the arm cell is held in the world, decoupled and never read in P. Link to OI's premise: the observer's description traces out everything it does not hold (Main:688-691), and Main:684 states that "A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms"; an unread record is part of what is traced out | supplied (isolation) on an OI premise | P |
| L-PORT | the screen's two ports are the two values of one registered bit; exclusivity of the two ports is therefore fixed | imported (detector model) | P, B1 |
| L-PHASE | the relative phase takes the native values `{0, π}`; no other value exists in the affine class without NNB (AP1 Lemma 5, type grading) | native (finding) | P |
| L-CAL | the record frame is calibrated by the source labels of the QA family | imported (calibration convention; no direct read) | C |
| L-HET | C's detectors use the native rule `XOR`; the test rule acts only in the gadget | imported (apparatus convention) | C |
| L-VALID | the validation layer is computed from the native construction and is not observer data | method | P |
| E-COMPL | `V² + D² ≤ 1` for a two-path system | empirical (Englert duality; also satisfied by classical waves) | P |
| E-NC | quantum prepare-and-measure tables violate noncontextuality inequalities | empirical | B |

*Replacements in the rows above* (from r6 and r7):
- **L-UPRIME**, type: "used in C and B-C: the detector set is U′'s functionals" (imported, representation; tied to
  D15 and to the representation ledger).
- **L-I1**: enters no token (a comparator only).
- **L-HOLD**, link to OI's premise: "Main:684 places the which-path detector's degrees of freedom in the visible
  sector, and Main:688-691 concerns partition trace-out for nested observers. The screen marginal is the same whether
  the unread marker is an unregistered visible cell or part of `H`."
- **L-N2** covers the hidden-sector environment cell (outside SA-1(c)).
- **L-ACC** (added): the observer interface restriction; ACC-R2-type; candidate strengthened; where: B.

**Which direction is the obstruction** (*verbatim*, r6). "For P, the obstruction would be an absence of the transition
in the native class; on paper it is absent (AP1 §4.5), so P tests reproduction, not removal. For B, the apparent
obstruction is that native tables are classically imitable; the toy-theory reading of the affine class (Spekkens;
Catani–Leifer–Schmid–Spekkens 2023, not read first-hand) predicts it. For C, it is octahedral confinement, attributed at
paper level to L-AFF, L-SYMP, L-P1, L-P2, L-N2, L-FWD, L-Q2 and L-UPRIME (REACHABLE §2.6); C removes L-AFF in the gadget
only."

**Part 2, the post-result template** (section `ADA` of `result.md`). It is generated from `measurements.json` and the
ledger with frozen sentences; every sentence broader than this model carries "outside this round's model, not
established".
- **Status rules.**
  - L-AFF: **essential in this model** when C is C-EXPOSURE or C-NONSTABILIZER with ABL, CC-NAT and C-EMB green;
    **not sufficient to remove in this model** when C is C-SURVIVAL.
  - L-HOLD: **the record that suppresses is unread**, printed with P-COMPLEMENTARITY.
  - L-PORT: **fixes B1**, always.
  - L-HET and L-CAL: **used, not varied**; REP-INV's outcome for L-CAL is printed beside it.
  - E-COMPL: **reported**: `CPL` per arm; no token reads it.
  - For the diagnostics (D1(a)), r5's rules, with its category names: L-HCONST is **binding** when some round
    induces a non-octahedral fit that fails herald constancy; E-BALL is **binding** when some test rule is INVALID,
    with whether that rule also has `nonstab_valid > 0`; L-ISOT is **reported** (`nonisotropic_branches`,
    `sharp_branches`).
  - The status rules read `ab-p`'s two readings and `ablate-p`'s fields, and every principle of kind "state
    restriction" or "access restriction" is printed with "not credited with new dynamics". The owner's case sentence
    is printed verbatim for the reported A/B case. The body's *ADA* adds the SA-1(c), SA-1(b), P3 and REP-INV rules.
  - Others: used, not varied.
- **The five questions**, printed per test and token:
  1. *Essential assumptions:* from the status rules.
  2. *Their types:* from the ledger; for L-AFF, L-Q2 and L-N2 both readings are printed.
  3. *Does removing an imported assumption eliminate the obstruction?* C-EXPOSURE: in this model, for the listed
     instances, on bounded orbits. C-NONSTABILIZER: partly (valid non-stabilizer orbit laws; no non-Clifford fixed
     operation found in scope). C-SURVIVAL: not in this model. For P, the A/B readings and ABL-SA1c's fields answer it.
     For B, the first restoring completion of `decide-b` answers it.
  4. *A counterexample satisfying the same observable requirements without it?* C-EXPOSURE: a finite candidate
     satisfying VAL on `O_K` only, HC, CONS and EMB; the comparator's further requirements are untested (NR-6).
     Otherwise none in scope.
  5. *All OI models, or only this one?* Only this model (the common clause). Exact maps on its rational reach can only
     be rational; irrational and approximate gates are outside every outcome.
- **Witness principle**, printed verbatim with C-SURVIVAL and with every P or B token that is a null (P-NO-FRINGES,
  P-NO-RECORD, B-CLASSICALLY-IMITABLE): "failure to construct a witness is not proof that no witness exists, unless a
  theorem establishes that impossibility within a clearly stated scope."
- **The owner's standard**, printed verbatim with every substantive token: "Conversely, relaxing an assumption is not
  sufficient by itself. The resulting model must still produce valid probabilities, observable quantum predictions and
  consistent behavior across repeated experiments."
- **Significance ladder:** the mechanical level of *Levels*.

**Part 3, the renaming check.** r5's table (*verbatim*), for C:

| imported or definitional item | form it could take | how it is excluded |
| --- | --- | --- |
| a non-stabilizer supply | a carrier or mediator law outside `N_sup`, or a mixture with an unrecorded label | C-EMB (b), NE-1 on every supply and component |
| access beyond P1 | retrodiction, two-slice reads, a registered cell left coupled | NE-2: the round schema (read after the last tick, mediator discarded at once) |
| invalid content hidden in valid mixtures | a valid observed law built from out-of-ball branches | NE-0 / E-BALL on every reachable law, fully conditioned outputs included |
| a conditioning predicate | conditioning on carrier values | C-EMB (d), the round schema |
| the target | a fitted rotation | NE-4: `α, β` from outputs only |
| a rule-dependent protocol set | protocols chosen per rule | C-EMB (d), one enumeration hash |
| the mechanism hidden in the supplies | non-O content present without the rule | C-EMB (c), the ablations |

Added for P and B:
- a marker that blocks or absorbs (NONABS, PL-ABSORB);
- activation counted as recording (`D(on)`, PL-NOREC);
- disturbance credited to path recording (the shams gate nothing; `ATTR`; PL-CONFOUND);
- the observer reading the marker (L-HOLD; the eraser fields are separate, labelled measurements);
- a preselected fringe picture (the phase comes from the phase cell; reference values are read only by controls and
  the note);
- the sham defined by design rather than measured (`K`; PL-CONFOUND);
- an access class chosen to make B fire (`Acc` owner-typed; TOMO; B-REG);
- U′'s functionals as the detector set (L-UPRIME, used).

The body's *ADA* adds three rows.

**Candidate new rounds** (named, not run):
- NR-1 larger rings and two mediators; NR-2 non-symmetric or non-translation-invariant `g` (A4 or neighbour symmetry
  relaxed as well); NR-3 multi-round induced maps and interleaved native Cliffords; NR-4 non-linear encodings with
  post-processed reads (L-UPRIME challenged); NR-5 the infinite-sector measure without H-INF-μ; NR-6 for any
  candidate, the full rung-3 test (all read directions, Lüders updates, CP of every branch, two carriers); NR-7
  in-world registration on U′, if ARP-1 returned EXPOSURE; NR-8 approximate induced maps (irrational gates); NR-9 the
  non-native supply tier `conv S_nat`, with membership decided by exact LP (*verbatim*, r5);
- NR-10 P-EXT, the which-path transition with non-affine marker couplings (the triangle site), and intermediate
  marker strengths off the line `V + D = 1`; NR-11 C's operation composed alongside a second system (spectator test);
  NR-12 P on U′ with NNB quarter phases; NR-13 the spatial `F_2` ring double slit (classical-wave form); NR-14 a native
  two-detector screen with a measured anticorrelation (*verbatim*, r6);
- NR-15 a native sham with the marker's coupling and a non-uniform kick, if a supply class admits one (*verbatim*,
  r7);
- NR-16 P under FIX, without P3 arming, the only route to a substratum-closer P.

### D.9 Invariants carried from r5 and r6

| invariant | checkpoint |
| --- | --- |
| indirect access is the only decisive interface | C-IFACE (static and mutation); *The two layers*; the diagnostics in their own section |
| attribution rests on validation fields, not observer data | `ATTR` reads `D` and `K` from the validation layer; C-IFACE |
| the marker records the path and does not absorb or block | `D(on)`; NONABS; SPI; PL-NOREC; PL-ABSORB |
| the shams are validated, not assumed | the validity flags of `decompose-p`; PL-CONFOUND |
| the dephasing look-alike is told apart | `D(SH-K)`; `V(SH-K) = V(on)` reported |
| the P rule cannot credit classical waves beyond Level 1 | CW-P; *Levels* |
| B fires and does not fire where it must | B-POS, B-STAB, B-CLASS, B-REG, B-WAVE; B-S4F for step 4's feasible branch |
| C detects non-Clifford operations through records only, and classifies Clifford ones correctly | C-R60, C-R60-ODD, C-35, C-S3, C-STAB, C-DET |
| composition is tested, not assumed | CONS at `K = 6, 12`; C-CONSX |
| the operation's origin is the non-affine rule | ABL; CC-NAT; C-EMB |
| no Level from a lower-level failure | `decide-levels` self-test |
| no number of the OI outcome is frozen | reference values read only by controls and the note |
| ARP-2 is frozen only after ARP-1 completed and was independently reviewed, and ARP-1's record is unchanged | precondition 1; `S7` (ARP-1's directory outside this round's governed paths); `--receipts` G13 |
| the reachable-law characterization precedes the executable test and is on `main` | precondition 3; DS pins its blob |
| rules, rounds, supplies, fragments and decision rules are fixed before any decisive computation | `F` designated before the first execution run: `order` reads `F`'s designation comment through `issues/comments/{DEC}` and checks its `created_at` and `updated_at` against that run's `created_at` (`order.json`; C.3; C.8 item 9), with the APPROVAL-ENTRIES self-test (re-review R14B-B1); the pinned blobs (B); the self-tests and the design run build no decisive family (the design run runs the checker only with `--event fixture`, `--stress` and `--self-test`) |
| conditioning is forward and registration terminal | NE-2 through the round schema; C-EMB (d) |
| no outcome is read as bearing on irrational or approximate gates | *What no outcome shows*; ADA question 5; S4 |
| a non-Clifford result is not embedded in the definitions | C-EMB (a)–(d); NE-1 to NE-5; C-PLANT's laws fail NE-1 |
| the encoded-frame determinant is used | C-FRAME; both determinants reported; W-CL in both frames |
| the round's runtime is bounded independently of the outcome | *Runtime*; the timeout test; `timeout-minutes: 60` |
| the dyadic, unconditioned case gives only signed permutations | CC-DYAD |
| the native affine case gives only the octahedron | CC-NAT |
| propagation is right | C-XB; C-STEP |
| exact arithmetic only | C-EXACT |
| no label over a red or missing control | the `decide-*` VOID clauses; `verdict`; the self-test VOID cases |
| verdicts read structured data only | exit statuses; the jobs API; the A3b marker; `replay`'s exit status; S1's measurements artifact through the artifacts API (D21 (b)) |
| the note says no more than the measurements; the ADA is separate and qualified | V; S4; the frozen texts; no `decide-*` reads an ADA field |
| each decisive dispatch requires owner approval; `F`/`E` require designation; R10 host-time checks are conditions only | approval entries, read through `issues/comments/{DEC}` and checked by `order` and `verdict`; designation quotes; ratification at `E` (the `E` dispatch's own entry: owner-approved R8 alternative); the APPROVAL-ENTRIES self-test (re-review R14B-B1) |
| execution changes only `verify.yml` and the record | `S7` through `--verify-round Q`; G, R, W |
| inputs as cited | DS |
| the receipt holds; legacy records are untouched | `--verify-round Q` prints `VERDICT  HOLDS`; `legacy_records_check.py` |
