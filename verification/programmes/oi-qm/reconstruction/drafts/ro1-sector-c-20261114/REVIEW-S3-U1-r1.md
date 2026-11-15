# Review of S3-U1-r1 (RO-1 S3, unit U1): independent non-author review

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U1-r1.md`
at PR #1294 head `e7f4db9d4d830e89263e72e6c26edaa953333654` (branch
`research/ro1-sector-c-1169-20261114`). Cited below as `U1:N`.
**Governing plan.** `S3-PLAN-r9.md` at `bfad27312ae48deba40926badf67c3afc1b9e504` (blob `46ebc72d`,
verified identical at `e7f4db9d`). Cited as `PLAN:N`. `RO1-SPEC-r3.md` (blob `76910fcf`) and
`RO1-DEPS-r4.md` (blob `a6326cbf`) at the same commit, cited as `SPEC:N` and `DEPS:N`; blobs match
U1's input list.
**Corpus.** `origin/main` at `dfeec843bec08443b25cffe34d33dc8401c3b604`. `Main:N`, `SM:N`, `GR:N` are
lines of `papers/*.md` there. `MR★` = `.../measurement-record-formation/amendments/MR-star.md` (blob
`45af1678`), `PREREG` = `.../measurement-record-formation/preregistration.md` (blob `c36fb14b`),
`OA1` = `.../oa-1-20261112/OA-1-REPORT-r5.md`, all at `dfeec843`.
**Off-main objects read.** SEL-EXCL-1 at `0ecfddeb`
(`verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md`);
SEL-DISC-1 at `445b17f7`; NAS (`native-apparatus-source-20261113/ASSESSMENT.md`) at `d8b74527` (blob
`a6661de9`, verified) and the branch head `7086bd30` (fetched by name).
**Reviewer.** Separate non-author Claude reviewer. Read-only; no computation, Lean, edit, commit or
Issue change.

## Verdict: REVISE

The architecture is sound and close to acceptable: the availability test G1–G7, the two-axis report
(levels × source verdicts), the three input kinds, AD-1 carrying both slice forms, and the S7(a) stop
are well grounded, and the large majority of citations are accurate and correctly labelled. Both
plan corrections are verified. Two defects, however, sit in the frozen definition or in the new
finding that is routed to U3/U4, and both must be fixed before the criterion is frozen for U2:
- the PR-gate finding (§5.1(iv), AW-3) contradicts U1's own I-off flag and turns on an unsourced
  definitional clause (B1);
- the composition clause S-A7, with a multi-tick read schedule, readmits R-seq, which G4 and AD-1(d)
  are meant to exclude (B2).

The remaining findings are local corrections of wording, labels and scope.

***

## Findings

### Blocking

**B1. The PR-gate finding is definition-relative, and §5.1(iv) contradicts U1's own I-off flag.**
- *Arithmetic: correct.* At SEL-EXCL-1 l. 33 (at `0ecfddeb`),
  `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))`. For fixed `(x,y)`, `T` restricted to `(r,A,B)` is the
  setting-free linear map `(r,A,B) ↦ (r, A⊕r, B⊕r)` followed by the translation `(0,0,x∧y)`. A
  translation does not change the level sets of a map, so for every non-setting carrier and every
  output register the induced partition is the same for all `(x,y)`. Under the I-sel definition as
  written (U1:266–270), `T` is not I-sel. The DEPS citation (DEPS:204, X-PR) matches the source.
- *The flag applies to `T`, and §5.1(iv) omits it.* U1's own flag (U1:274–278) covers "an offset that
  is not additive in the setting and another cell (for example `z·n`)", and says such cases "are
  recorded as I-off with this flag". `T`'s offset `x∧y = x·y` is exactly of that form, with `n` the
  other wing's setting. Averaging over `y`: for `x = 0`, `B = r` and `r` is legible in `B`; for
  `x = 1`, `B = r⊕y` and it is masked. §5.1(iv) (U1:489–497) nevertheless states "So `T` is I-off
  under C-INT" without the flag.
- *The classification turns on an unsourced clause.* "The carrier is any non-setting region"
  (U1:269–270) has no source. S-C1(a), which I-sel generalizes, quantifies over "every value of every
  other region" (MR★:501–503), and that includes other settings. If a setting region may be the
  carrier, take `y` as carrier, `x` as setting and `Y = B`. Then `y ↦ B⊕r⊕(x∧y)` is constant for
  `x = 0` and injective for `x = 1`. The partitions differ, so `T` is I-sel: `x` selects whether `y`
  is transferred into `B`.
- *Consequence.* The stated consequence, "a restriction placed on setting-selected operations does
  not reach this implementation of PR, so it cannot be the fact that excludes it" (U1:496–497), holds
  only for I-sel with setting regions excluded as carriers. Under the flag class, or with settings
  admitted as carriers, a restriction on setting-selected operations does reach `T`. AW-3 (U1:577)
  says it was "pressure-tested against every output register and every non-setting region as
  carrier". That is precisely the test that leaves out the decisive case.
- *Required fix.*
  - Either justify the non-setting-carrier clause from a source that makes no reference to outcomes
    (K-2), or drop it.
  - Restate §5.1(iv) as "`T` is I-off with the flag: its only setting dependence is the offset `x∧y`,
    non-additive jointly in the two wings' settings, acting on no non-setting carrier".
  - Restate the consequence as relative to the I-sel definition.
  - Reclassify AW-3. The sound content may still be a gem: the PR gate's setting dependence lies
    entirely in a setting–setting product and acts on no carrier, whereas a quantum reference's
    settings select operations on a carrier. But that must be stated as a property of `T` under
    the stated definitions, not as "restrictions at the intervention action do not reach it".
    AW-3 already lists "the cross-wing offset" as a locus, so the fix is consistent with AW-3's own
    guidance.
- *Author-side status.* The finding is correctly marked [A-inf] and "author-side, scoped to `T`", and
  §8 classifies SEL-EXCL-1 as support off `main`. That part is in order.

**B2. S-A7 with a multi-tick read schedule readmits R-seq.**
- *The clauses.*
  - A program declares a read schedule, "which `V_k` at which ticks" (U1:87–88).
  - Execution requires each record to be "held (G4) at its read tick" (U1:91–93).
  - S-A7 says "the comparison of records held at their final read ticks defines the joint law and is
    not an operation" (U1:448–449).
- *The leak.* A program that reads one `V` at ticks `t₁ < t₂` and compares the two records under S-A7
  obtains the joint law of `V`'s projected sequence with no retention process at all. That is the law
  of R-seq. G4 (U1:104) calls R-seq "a representation, not a held record". AD-1(d) (U1:142) requires a
  retention process for a history to count as held. AW-4 (U1:578) claims these clauses exclude R-seq
  from `Γ_exe`. As written they do not, because the line between "a history" and "several records,
  each held at its own tick" is nominal.
- *Why it matters.* It bears directly on K-rec's "complete accessible histories" (SPEC:243), on
  SEL-EXCL-1's complete local histories `H_A^(i)` (l. 91), and on same-seed reuse (RR-1), all of which
  U2–U4 will classify.
- *Required fix.* State in S-A7, or in §2.1's execution clause, that records entering a joint
  comparison must all be held at the comparison tick. Records from earlier ticks must be retained
  there under C-RET, or moved under S-A6. Otherwise the joint law is a representation (K-4). The same
  applies to the setting records K-rec requires.

### Required

**R1. The "not available" vocabulary is inconsistent.**
- K-1(iii) (U1:487–488): "A program is reported *not available* only where an input is disproved at
  verified scope … otherwise it is *unsourced*."
- §2.3 (U1:125–126): an apparatus-assumed input "fails G1, and the program is not available".
- §5.3 (U1:511–512): the criterion removes "programs with an apparatus-assumed or disproved input".
- These conflict. Fix: separate the outcomes as available (derived, or relative to `μ`) / unsourced /
  requires assumed apparatus / not available (disproved, at scope and status). State that only the
  last counts as a negative under SNR-1 (PLAN:784–797, which itself separates *unsourced or assumed*
  from *disproved*).

**R2. C-RET is weaker than MR-1's R2, but C-REC says "R2 holds by C-RET".**
- PREREG:163–164: R2 requires `r` to be "recoverable at every later accessible time up to `T`".
- C-RET (U1:356–364) requires recoverability at the readback `t₂` only. It explicitly admits a record
  whose support passes through `H` between `t₁` and `t₂` (the parked-record case).
- C-REC (U1:315–316) says "R2 holds by C-RET". That is inaccurate.
- The readback form has a source, C2-structural, "persists to the readback that uses it" (Main:74,
  and PLAN:293). Its adoption is therefore defensible, but it is a [P] choice that differs from R2.
- Fix:
  - State the divergence where it is made.
  - Replace "R2 holds by C-RET" with "R2 is replaced by C-RET (readback form)".
  - Note that MR-1 results stated with R2 transfer to C-RET only after a check.
  - Owner decision A assigns the parked-record case to U4 as a named hypothesis
    (#1169 c.6890079967). U1 should say that the clause defines what would count, and assumes no
    mechanism.

**R3. §4.4(iv): "not excluded" is presented as "sourced", and one citation has no status label.**
- U1:342–345 begins "Sourced: R1 for records of past properties is not excluded under μ-G". In U1's
  own vocabulary (§2.3), *sourced* means verdict *derived*. "Not excluded" is not derived. The same
  section records that on K1 the offsets can mask R1 at later ticks, "not decided here"
  (MR★:1349–1352), and that the trace route is undecided (MR★:1373–1380).
- The cited O-OBSMU Lemma Q-b1 (`observer-interface-obsmu-20261104/ANALYSIS.md`:907–913 at
  `dfeec843`) carries no status label. Its own following lines (:914–917) say that a preparation
  through the record history needs retention, which is "all open".
- The O-OBSMU reviews are #1110 comments, not review files on `main` (the directory holds only
  `ANALYSIS.md` and `README.md`). Under U1's definitions (U1:47–50) the lemma is therefore [NP], not
  [M-r].
- Fix: "Not excluded under μ-G (D2 is equal-time only); undecided on K1 (C-3, C-4)", with Q-b1
  labelled [NP].

**R4. The Q1 working definition is required by the plan but not applied.**
- PLAN:870 (U1's row) requires U1 to "Reuse MR-1's levels, #866's source-matrix vocabulary and the Q1
  working definition". PLAN:283–285 lists Q1 among the owner rules that apply.
- U1 lists #866 c.6719811801 as an input (U1:38) and as governance (U1:600), but never applies it.
  The definition reads: "A common refinement that is genuinely available through the declared native
  access interface, under the same preparation, should withhold the setting-controlled-interaction
  label".
- It bears directly on C-INT's I-sel/I-off split. S-C1(b) and OA-1 D7 both say that reads are
  coarse-grainings of one joint record.
- Fix: state how Q1 enters C-INT (for example, I-sel is withheld when an available common refinement
  exists under AD-1), or state why it does not.

**R5. AC-1's two halves are not reported as two halves, and "bare model" is undefined and
inconsistently placed.**
- *Soundness half.* AC-1 (PLAN:417; PLAN:878–888) requires both halves to be reported, and a unit
  that cannot test both "reports why, and stops". U1 reports the coverage half for bare models and
  says "U1 reports no soundness result" (U1:519–520), without the reason. The reason is available
  and adequate: U1 proposes no restriction aimed at soundness, and K-1(i)–(ii) show that the criterion
  treats PR and the quantum references alike. It should be stated as the AC-1 soundness-half report.
  §9 (U1:608–609, "AC-1 run on the criterion") should then match.
- *Coverage half.* On bare models the target's coverage operations are absent for reasons of the model
  (the ceiling, D-A8). The coverage half is therefore "criterion-neutral, coverage absent by model".
  It should say so, so that it is not read as positive coverage.
- *Bare model.* The term is not defined. P-phase is placed in two ways:
  - "apparatus-assumed for a bare model" (U1:280–282);
  - an extension operation under S7(a) (U1:533–535).
- Yet §5.3 (U1:514) counts D-iv as a bare-model coverage loss. D-iv is stated for `substratumClass`,
  which includes the phase operators: interface A (DEPS:178; DEPS §7.2 "Interface" row). Only
  D-nonneg (`permTheory`, without phases) is bare in U1's sense.
- Fix: define "bare model" (no extension E; `Obs` read-only; no stated intervention principle) and
  place D-iv and D-nonneg accordingly.

**R6. C-SET's "named producer" contradicts §2.3.**
- U1:217–219: "a named producer: `Z`'s content is a `μ`-datum".
- U1:123–124: a `μ`-assumed input "is not a producer (#866 rule above), so its verdict is *assumed*".
- Fix: "a named source", with verdict *derived* under the derived `μ` and *assumed* under a declared
  datum.

**R7. K-2 overstates the sourcing of the clauses.**
- §5.2 (U1:504) says "Every clause is justified by a source predating this unit". Several clauses are
  U1's own [P] choices:
  - the I-sel generalization of S-C1(a), with its non-setting-carrier clause (B1) and the flag;
  - AD-1(e)'s extension of OA-1 D7. D7's statement is conditional, "If the setting does not change
    `φ`'s action" (OA1:204–205), and AD-1(e) quotes it without that antecedent (U1:143);
  - C-RET's readback form (R2);
  - the parked-record clause.
- Fix: list these as [P] choices, each with its target-neutral ground. That is what K-2 actually
  requires (PLAN:415).

### Optional

- **O1. The Codex branch head.** U1:33–34 says `7086bd30` "changes ASSESSMENT lines 3 and 167 only and
  adds retention and status files". `git diff d8b74527 7086bd30` also modifies `EVIDENCE.md`
  (documentary status lines and a new §7) and adds `support/` and `reviews/` copies. ASSESSMENT's
  scientific content is unchanged; only the description is incomplete.
- **O2. SEL-DISC-1 l. 79.** At `445b17f7` that line supports the entropy needed for fair outputs. It
  does not support "blanks for records" (U1:424–425). Cite l. 53 or the PR-blank source
  (SEL-EXCL-1 l. 87) for the blank half.
- **O3. Preparation scope.** Gap 1 concerns *selected hidden* carriers (OA-1 STATUS:52–57). Visible
  carriers are native (OA1:358), and under U1's own C-PREP a heralded preparation of visible cells is
  available at the D3 cost (OA1:156–160). The preparation row of §9 (U1:619) and the first missing
  step (U1:209–211) should be scoped to hidden carriers, and to preparations whose herald later steps
  must hold (which brings in C-RET).
- **O4. S5 at R-fresh.** The freshness condition's `X_relevant` includes every non-seed variable used
  by the stage (REPORT.md:59–63), and therefore the settings. Independence of a seed from the settings
  at later use boundaries is S5-type content. U1 derives it only at the initial slice under μ-G
  (U1:419–421, correctly). Carry S5 as a named condition at later boundaries, as C-SET does.
- **O5. G3's last sentence.** "A `μ` chosen for one program makes that program representable only"
  (U1:103) is not testable inside one fixed model, where `μ` is common to every program by
  definition. Restate it as a statement about refitting `μ` across programs: that is a different
  model, and G6 forbids combining verdicts across models.
- **O6. O11.** §6.2 addresses readings (i) and (iii) only. Reading (ii), the gauge relation `G`, needs
  the same one-line treatment. G6's rule that the two slice forms are "a different model"
  (U1:155–156) presupposes reading (i). Say so.
- **O7. §A.42 item 8 table.** Add the Issues cited as homes (#1234, #1032, #913, #914, #1143) as
  provenance.
- **O8. For U2.** SPEC:318's single-use row presupposes "setting sources independent of the unused
  source". U1's C-SET correctly does not. A pointer for U2 to carry S5 on that row would prevent
  reintroduction.
- **O9. "Frozen here."** AD-1 is frozen on acceptance of this unit. U1 is unreviewed at this head.
- **O10. The S7(a) stop can be narrowed.** U1 already gives the verdicts for two of the three typings
  (U1:538–542):
  - typed into `φ`: a native step, with the P-L3 conflict a model question;
  - typed into `Γ`: not available, under either reading of S7(b).

  Only the `Obs` typing needs a re-frozen AD-1. Stating this narrows the stop without choosing.

***

## Answers to the brief's checks

**1. Citations.** I checked more than 60 citations against their sources, covering all seven actions,
every row the §9 verdicts and first missing steps rest on, AD-1, G1–G7 and the authorization quotes.
- *Accurate as quoted:*
  - Main:42, :48–52, :54, :58, :74, :80, :84, :326–328, :360, :405–410, :406–407, :482, :556, :572,
    :582, :588, :598 (via SPEC), :724;
  - SM:252, Lemma 1c (i)–(iii); GR:823;
  - MR★:455–460, :464–483, :487, :498–509, :511–513, :517–527, :564, :573, :595–601, :613–618,
    :634–643, :657–659, :667, :672–673, :857–861, :876–878, :910–916, :919–923, :1065–1069,
    :1297–1300, :1322–1331 (C-2), :1344–1366, :1373–1380, :1493–1494;
  - PREREG:36–43, :104–108, :112–117, :134–140, :162–170, :177–187, :191–200, :262–264, :288–297,
    :421–424, :461–462, :512;
  - OA1:105–114, :145–193, :202–208, :352–363;
  - OA-1 STATUS:48–59, :65;
  - NATIVE-INT-SRC-2 SOURCE-SCREEN:91 and STATUS:25–33;
  - NATIVE-PREP-SRC-1 STATUS:25–34;
  - composition-access REPORT:29–31, :34–55, :57–69;
  - THEOREM-N:3–9 and README:15–16;
  - O-OBSMU ANALYSIS:485–489, :907–913;
  - NAS:12–14, :33, :38, :67–77, :82, :155;
  - SEL-EXCL-1 ll. 33, 44, 46, 87;
  - SEL-DISC-1 l. 53;
  - SPEC:110–120, :142–151, :169–173, :215–218, :238–245, :295–310, :318–320, :332–350, :380–382,
    :613, :616;
  - DEPS:178–179, X1, X3, X4, §7.2;
  - #866 c.6763916830 items 3 and 5; #1169 c.6890079967 (author `amaybaum`, 2026-11-15T06:02:00Z,
    every quoted phrase present);
  - PR #1278 reviews 5897621232 and 5898054706, both at `d8b74527` as stated.
- *Status labels.* These are correct as U1 defines them. MR-1 has no review file on `main`, only
  MR★'s relayed summary (MR★:1297–1300), so [NP] is right for S-L2, S-L3, S-L6, S-L7, S-C1 and S-C4b.
  Composition-access, Theorem N, OA-1, NATIVE-INT-SRC-2 and NATIVE-PREP-SRC-1 carry review files on
  `main`, so [M-r] is right. F-3 is correct: S-C1, S-L2 and S-L5 are absent from MR★:1297–1300.
- *Exceptions.*
  - Q-b1 is unlabelled and should be [NP] (R3).
  - OA-1 D7 is quoted without its antecedent (R7).
  - SEL-DISC-1 l. 79 is over-attributed (O2).
  - The Codex head description is incomplete (O1).

**2. Native or imported.**
- Every per-action criterion is native in form. Each requires that `φ` effect every change (G1),
  traces every input to `μ` and `φ` (G2), and books assumed data in `Res` rather than letting them in
  as producers.
- The first missing steps are genuinely first on the record for C-REC (C-3), C-RET (O-RET; C-4 blocked
  by C-3) and C-REN.
- For C-PREP the step should be scoped (O3).
- For C-INT the ordering is right: a rule with I-sel admissible under P-vii, then G_SM's request and
  precursor. But it depends on B1's definition.
- "No first missing step specific to setting choice" (AW-5) follows from the criterion as stated.

**3. Countercontrols.**
- The criterion cannot make PR vanish by declaration. No clause reads a record law (K-1(i)). PR's
  inputs (setting registers, a fresh `r`, blanks) are booked as `μ`-assumed exactly as the quantum
  references' are. No clause is selected for quantum outcomes.
- Two caveats remain:
  - K-1(iii) is internally inconsistent (R1);
  - K-2's sourcing claim is overstated (R7).
- AC-1: "bare models only" is the correct scoping of the coverage half, given S7(a). The report
  should be explicit that on bare models the coverage half is criterion-neutral, with coverage absent
  for reasons of the model, and that the soundness half is not reported because no restriction is
  proposed (R5).

**4. The S7(a) stop.** The stop is real and correctly placed.
- Completing a verdict for an extension's operation requires choosing its typing (SPEC:142–151).
- The `Obs` typing contradicts AD-1(c), so AD-1 itself would have to change.
- It can be narrowed (O10). U1 could not have completed the extension case without choosing.
- S7(b) is correctly not reached: membership is decided by the same clauses under both readings, and
  the `Γ`-typed branch is "not available" under either.
- O11 is correctly not reached for stating the criterion on tuples. The note on reading (ii) is
  missing (O6).

**5. S5.**
- No setting criterion assumes measurement independence. C-SET requires the joint law to be stated as
  a property of `μ` and `φ`, "never assumed" (PREREG:512). It carries S5 as a named condition wherever
  independence is used (U1:221–224). G3, AD-1(e) and the program declaration are not independence
  assumptions.
- Note that OA-1's own operation definitions N1-S and N2 embed ledger (xiv) (OA1:132–133). U1 cites
  OA-1 only for D5 (measure-free) and D2 (μ-G), and does not import those definitions. That is
  correct.
- Residual S5 exposure lies at R-fresh, not at settings (O4), and in SPEC's single-use row (O8).

**6. The PR-gate finding.** The source was verified at `0ecfddeb` l. 33 and agrees with DEPS:204. The
arithmetic is correct. The classification and its consequence are not robust to U1's own flag, or to
admitting settings as carriers (B1). It is correctly stated with author-side status and classified as
support off `main`.

**7. The plan corrections.**
- *F-1, verified.* `git show 5914c17c:papers/SM.md` and `dfeec843` give byte-identical line 252.
  Lemma 1c (iii) reads "current field visible, retarded register hidden". MR★'s S-L7 (MR★:616–618)
  cites SM:252 for exactly that assignment. PLAN:302–303's "has drifted" is inaccurate.
- *F-2, verified.* NATIVE-INT-SRC-2 landed by merge `7fc6e0fc` ("Merge pull request #1223"), and
  NATIVE-PREP-SRC-1 by merge `bc7f817d` ("Merge pull request #1225"), both 2026-11-13, first-parent on
  `main`. Their records, review files and status notes are present at `dfeec843`. PLAN:208–209 and
  PLAN:432 ("reviewed, not merged") are stale.

**8. Status discipline.**
- Conditional and established, defined and executable, and first missing step and ultimate goal are
  kept apart throughout.
- There is no new physical premise. P-super and non-functional records are correctly named as
  premises that would be new and are not used.
- There is no hidden authorization. U2's wait for decision C4 is stated. "No other decision is needed
  for U2–U4 to start" (U1:643) should not be read as authorizing them; their starts are governed by
  #1169 c.6890079967's order.
- New [P] definitional choices should be listed as such (R7).
- §A.42 item 8: every off-`main` reference I found is classified, except the Issue homes (O7). The
  classifications are correct: NAS, SEL-EXCL-1, SEL-DISC-1, #912 and PLAN/DEPS/SPEC are each support
  off `main`, a gap. §8's claim that no verdict of U1 rests on an [OFF] row alone holds for the §9
  verdicts. AW-3 does rest on an off-`main` object, and §8 says so.

## Not checked

- The Lean statements cited (`substratumGen_not_control`, `frozen_sourcing_verdict`,
  `obs_not_layerFlowExecutable`): read through Main and DEPS only, not opened or built.
- The proofs inside MR★, OA-1, Theorem N and the composition REPORT: read at the cited lines for what
  they state, not re-derived. The exception is the one-line Lemma R and the PR-gate algebra, both
  re-derived by hand.
- MR★ S-L4/S-C4a's slice count (C-10), and the content of #912 `composition_flag_v6/` at `2af1d5d5`.
- The other PLAN line citations, beyond spot checks of PLAN:157–160, :169–179, :267–303, :410–420,
  :784–797, :864–891 and :902–920.
- SEL-ACCESS-1, and the Codex `support/` copies added at `7086bd30`.
