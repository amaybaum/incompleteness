# Independent review of the #1169 synthesis r1 (missing-mechanism list)

**Verdict: ACCEPT WITH CHANGES.** The list's structure, its nine entries and the interface ties in
§2 are sound. Every pin and blob checks out, and so does the authority record. The proposed routes
are not presented as adopted. #1060 is used as context only. The register is neutral. Five
statements, however, carry a no-go or necessity beyond the class it was proved for, and those are
blockers under the Code Review Rules ("Claim/evidence boundary"; "Bridge and no-go scope"):

- the ranking reason for MM-1 (F1);
- MM-1's (1b) and (1c) labels (F2);
- "every ceiling" for MM-6 (F3);
- MM-2's §A.31 inference (F4);
- cross-unit agreement A4 (F5).

Four further findings concern label precision, kernel citations, the ranking's dependency reasoning
and §A.42 item 8 (F6–F10, F13). Each fix below is a text edit and needs no new research. An r2 with
a focused confirmation is enough.

**Object.** Branch `research/synthesis-1169-20261113`, fetched by name with full history. Exact head
`4940e8d681caeaca37960400c6685101e633b389`, a single-parent child of `main` at `c3b5f37a`. The diff
adds exactly two files, `SYNTHESIS-r1.md` (581 lines) and `NOTES-r1.md` (131 lines), under
`verification/programmes/oi-qm/reconstruction/drafts/synthesis-1169-20261113/`. Line numbers below
are of those files at that head. "S:n" is `SYNTHESIS-r1.md` and "N:n" is `NOTES-r1.md`. Every other
short name is the synthesis's own, from its §0.

**What was read.**
- Authority: #1169 c.6860584645 (`amaybaum`, 2026-11-13T17:47:40Z). Owner decisions #1273
  c.6860580909, #1268 c.6860582570 and #1169 c.6854774010.
- ChatGPT reviews 5892912253, 5892912758, 5892919040 and 5895564670, plus r7's ChatGPT review
  5891524305. Each review's `commit_id` equals its unit's pinned head.
- Unit records, read in full at their exact heads: TS r2 at `c539a60c`; P0 r3 at `cd38655c`; R7 at
  `cd38655c`; BL r3 and NOTES-r3 at `d8e4f80e`; OC `NEW-RESULTS.md` and `DEPENDENCIES.md` at
  `d015131d`. Also the r7→r8 diff at `2a9f10ba` and REVIEW-r8.
- On `main` at `c3b5f37a`, at every cited line: OA1, OA2, OA3, W11, OBS, PPS, M1D, M2D, Main, S4 and
  P. The OIBridge statements cited in MM-3a and MM-8, with the definitions they depend on.
- Every blob in §0 was recomputed and matches (TS `35c5c116`, CONFIRM `558ddc77`, P0 `611a4d9a`,
  P0-CONFIRM `8b440f2d`, R7 `f1ffac0e`, BL `0298088d`, NOTES-r3 `963d7352`, CONFIRM-r3 `c968776a`,
  OC `1859e8c5`, DEP `6c127b0a`, OA1 `5a16b213`, OA2 `8f8ddf73`, OA3 `0a36fd05`, W11 `8bf64629`, OBS
  `e657732b`, M1D `7f8a142b`, M2D `9352d9da`, PPS `9123157c`, Main `0db17597`).
- About 120 file:line citations were checked against their sources. All except those named below
  say what the synthesis attributes to them.

**Tools run** (paper-only, as authorized):
- `tools/voice_check.py`, `tools/claims_check.py`, `tools/staleness_check.py` and
  `tools/artifact_placement_check.py`: all OK. The first three scan manuscripts only, so they do not
  reach the draft. A manual scan of the draft for the §A.32/§A.33 phrase families found no hit in
  `SYNTHESIS-r1.md`.
- `tools/legacy_records_check.py 4940e8d6…`: self-test OK, 303 records intact.

Nothing was committed, pushed or posted.

***

## Findings

### F1 (High; blocker). MM-1's ranking reason generalizes a scoped stop to every embedded protocol

- **Where.** S:349–352: "MM-1 blocks every embedded protocol. Preparation comes first in operation
  order. … blocks its parts (b)–(f) (TS:380–382)."
- **Evidence.**
  - OA1:526–529 qualifies the operation-order claim: "N1 (as N1-S) comes first in operation order,
    but only under the posited global selection μ-G and the held-equals-present-`V` convention."
  - OA1:522 states the measure scope: "Under μ-O (derived) and μ-R: N1-K can be native (swap); N1-S
    is open."
  - TS:380 says part (e) "rests on the same ingredient, **or on the convention MP-0b**", so MM-1
    does not by itself block (e).
  - ChatGPT 5892912253: "a sourcing stop, not an OI-wide no-go." The synthesis's own S:90 and S:408
    say the same.
- **Fix.** Replace S:349–352 with: "**MM-1 blocks every protocol of TUNE-1's initial-condition schema
  (1a) and, under μ-G with C5, selectable preparation of hidden carriers (OA-1 gap 1; OA1:522,
  :526–529).** It is TUNE-1's first stop and blocks part (b); parts (c) content, (d) held outcomes
  and (f) inherit it, and (e) rests on it or on MP-0b (TS:380–382). Under μ-O and μ-R it is not
  shown to block (N1-K can be native; N1-S open, OA1:522). O-RDY is a listed prerequisite of #1143."

### F2 (High; blocker). MM-1 (1b) is a non-supply result, and (1c) shows a disjunction

- **Where.** S:68 ("shown necessary (3 scoped forms)"), S:99–109, S:129–130, S:28 (R7 "context").
- **Evidence.**
  - **(1b).** Lemma P-1 (OBS:529–545) and OA-1 D3 (OA1:156–160) show that μ-G supplies no
    unconditionally ready region, and that a heralded substitute has probability at most `q^{−M}`.
    That says the ingredient is *absent*. It is not a proof that a target fails *without* it, which
    is the synthesis's own definition of "shown necessary" (S:58–60). ChatGPT 5892912253 words it
    "ruled out as an unconditional ready source under uniform μ-G". The sentence at S:101–102, "no
    ready region exists at any time", drops "unconditional".
  - **(1c).** R7 §3.2 concludes that "A φ-dependent held statistic needs **either** an initial or
    boundary law other than μ-G (MP-0a …; any structured realization law …) **or** a typing other
    than held-at-use (the retention convention MP-0b, or heralds read as ensemble conditionings, C7)"
    (R7:196–200). OA1:522 says gap 1 is "resolved classically by MP-0a **or** MP-0b". So what (1c)
    shows necessary is a disjunction, and one of its disjuncts belongs to MM-2. The synthesis applies
    exactly this distinction to MM-4c (S:235–238) but not here.
  - (1c) also rests on R7 §3.2, which its own heading marks "[W, REC-1; unreviewed]" (R7:185, :206).
    Yet §0 (S:28) classes R7 as "context".
  - A necessity form under μ-G does exist on `main`: "under μ-G, for a hidden carrier, unmasking the
    previous slot needs a ready cell (MP-0a), with the neighbours known or isolated" (OA1:522, R-lin,
    selectable preparation).
- **Fix.**
  - S:68, label cell: "shown necessary in TUNE-1's schema (1a) and for writing a selected value
    under R-lin and μ-G (1b′); one disjunct under μ-G with C5 (1c); not supplied under μ-G (1b);
    producer: proposed route".
  - Rewrite (1b) as "**Not supplied under μ-G.** … so no *unconditionally* ready region exists at
    any time under μ-G, no bijection produces one, and a heralded substitute costs `P(E) ≤ q^{−M}`.
    This is the absence of the ingredient, not its necessity."
  - Add (1b′): "**Writing a selected value under R-lin and μ-G.** For a hidden carrier, unmasking the
    previous slot needs a ready cell (MP-0a), with the neighbours known or isolated (OA1:522).
    Observer class: selectable preparation (N1-S) of hidden carriers under R-lin and μ-G."
  - Rewrite (1c)'s label line as "**(1c) One disjunct under μ-G with C5.** … a φ-dependent held
    statistic needs a law other than μ-G (the ready-resource form, MP-0a, or any structured
    realization law) **or** a typing other than C5 (MP-0b or C7, which are MM-2). Here the ready
    resource is one disjunct, not a necessary condition on its own. The R7 reading is marked
    unreviewed in its own text (R7:185, :206)."
  - Change S:28 "(context)" to "(context; support for MM-1c and MM-2, see §8)".

### F3 (High; blocker). MM-6 is not "a hypothesis of every ceiling"

- **Where.** S:73 ("load-bearing role in every ceiling shown"), S:273–281, S:371, S:385; and the BL
  bullet of MM-2 at S:158–159 ("Inside (vii) with a coset law and MI\*").
- **Evidence.**
  - Proposition AL has no MI hypothesis: "No separation, generator isolation or
    measurement-independence hypothesis is made" (BL:205). ChatGPT 5892919040 agrees: "It does not
    need (Sep) or MI as additional hypotheses." NOTES-r3:69 adds: "in AL the coset hypothesis does
    the work MI does elsewhere."
  - OA-3 Theorem S "uses no invariance and no (xiv)" (OA3:349–351).
  - MI\* holds in the law μ₀ of the selected-read witness (NOTES-r3:54). It is not a hypothesis of
    AL.
- **Fix.**
  - S:73: "proposed route; load-bearing role shown for E(b), OBL-SP and the Bell stage-5 ceiling;
    not a hypothesis of AL or Theorem S".
  - S:371: "**MM-6 is a hypothesis of E(b), OBL-SP and the Bell stage-5 ceiling** (OA2:528; R7:257;
    BL:102). AL and Theorem S do not use it (BL:205; OA3:349–351); in AL the coset law (MM-5) plays
    its role (NOTES-r3:69)."
  - Apply the same scoping at S:277 ("the ceilings" → "these ceilings") and S:385.
  - S:158–159: replace "with a coset law and MI\*" by "with a coset law (no MI hypothesis, BL:205)".

### F4 (High; blocker). MM-2's §A.31 check overstates, and its inference is asymmetric

- **Where.** S:166–172.
- **Evidence.**
  - "Every non-classical pattern found in or next to the affine class … appears at a
    record-convention boundary" is false on the corpus:
    - OA-2's N2.1 dual route is measurement-contextual with full reads and non-spanning reachable
      laws (OA2:296–315). OA2:604 lists "non-spanning reachable laws" as an open exit *within* the
      affine class. That is a preparation-span boundary, not a record convention.
    - A setting-dependent non-coset law with an affine readout gives the PR box (NOTES-r3:67–69;
      BL:243–245). That is a run-law boundary.
    - OA-2's `Z₄` CHSH-4 counterexample is an H-AR (observer-class) boundary (OA2:612–613).
  - "A convention that is chosen rather than derived from the Definition therefore cannot carry a
    non-classical result" is not derived anywhere. It is also asymmetric. The classical verdicts rest
    on conventions that are equally chosen: (LF) for P0, (AL4) for AL and (H4) for E(b). The
    synthesis's own MM-2 item list says none of them is fixed by the Definition. The owner fixed AL's
    convention "to AL only" (#1273 c.6860580909, Q4).
  - This is the obstruction-favourable reading that §A.31 asks to pressure-test, and the checks at
    S:162–163 and S:170–172 already contain the material for a symmetric statement.
- **Fix.** Replace S:166–169 with: "**§A.31 check.** Three of the non-classical patterns found in or
  next to the affine class sit at record-convention boundaries: P0 N8.2(b), BL's selected read and
  OA-3's (V-ii-U) shift, the last of which OA-3 N4 classes as a convention artefact. Others sit at
  other boundaries: non-spanning reachable laws (N2.1, OA2:296–315, :604), non-coset laws
  (NOTES-r3:67–69) and non-H-AR coarse-grainings (OA2:612–613). The classical verdicts also rest on
  conventions not fixed by the Definition ((LF), (AL4), (H4)). Neither side's convention is derived,
  so neither verdict is a result about the Definition alone." Keep S:169–172 from "P0's N8.2(b) gbit
  is outside …" onward.

### F5 (High; blocker). A4 merges distinct hypotheses and misstates the open cases

- **Where.** S:440–447; NOTES R-c (N:95–100).
- **Evidence.**
  - E(b) is classical under (H1), H-AR, (H3), (H4), (xiv) **and (SP)** (OA2:528–537, :552–560). It
    assumes no coset-uniform law.
  - With (H1) and (H3) kept, E(b) has three open exits: non-additive observers, non-nested reads and
    **non-spanning reachable laws** (OA2:600–604). OA3:494 adds: "The affine class at E3 without (SP)
    stays open."
  - AL's open cases include non-coset laws, non-cell settings and postselection (BL:242–248), as
    well as setting-selected reads.
  - So "the observer has full, label-free or fixed-region access to a coset-uniform record" is not
    E(b)'s condition, and "In each, the open case is a restricted record region" is false for both
    E(b) and AL.
- **Fix.** Replace S:440–445 with:
  > **A4. Three affine-class classicality results, each under its own full hypothesis set.**
  > - P0, the scoped pass under (LF): (H3), the r7 record class, held-at-use typing, C-PM, H-xiv,
  >   `D_0` (P0:454–459).
  > - AL: (AL1)–(AL4) and (NS) (BL:189–203).
  > - E(b): (H1), H-AR, (H3), (H4), (xiv), (SP) (OA2:528–537).
  >
  > Each has a record-access clause ((LF), (AL4), (H4)), and for each, dropping that clause leaves
  > the case open. Each also has other open exits: for E(b), non-additive observers and non-spanning
  > reachable laws (OA2:600–604); for AL, non-coset laws, non-cell settings and postselection
  > (BL:242–248).

  Keep S:446–447.

### F6 (Medium). MM-3a: two clauses are not what the cited [K] identifiers state, and one link is [W]

- **Where.** S:193.
- **Evidence.** The three identifiers are at the cited lines:
  - `obsTheory_rule_independent` (SubstratumInterfaceAudit.lean:780) is the `rfl` equality of
    `obsTheory` across `Rule ι V`, for finite abelian `ι`, `V`.
  - `phase_ceiling_rule_independent` (FrozenSourcing.lean:302) gives `¬ PhasesAvailable (obsTheory
    …)` for every rule.
  - `nonnegBounded_verdict` (FrozenSourcing.lean:327) applies only to `T : FiniteOperationalTheory
    (Fin 2)`.

  However:
  - "Not `DerivedOI` on any carrier" for `obsTheory` needs `nonnegBounded_not_derivedOI`
    (FrozenSourcing.lean:111) together with `obsTheory_nonnegBounded` (:84). Neither is cited.
  - `DenseUnitaryControl` is defined only for Fin-2 theories (DiscreteCompletion.lean:45), while
    `obsTheory 𝒮` lives on `𝒮.Conf` (SubstratumInterfaceAudit.lean:770–771). The kernel's
    dense-control statement is therefore about NonnegBounded Fin-2 theories, not about `obsTheory`.
    It transfers only through the invariant.
  - "Rule-derived configuration interfaces stay inside (D6)" is [W] on [K] (OA1:196–200, :598). The
    row's layer cell says "[K] on `main`".
- **Fix.**
  - Interface cell: "Configuration identification `obsTheory 𝒮 = permTheory 𝒮.Conf` (`Substratum`
    with finite abelian sites and alphabet), every rule: no phases, not `DerivedOI`. Every
    NonnegBounded theory on `Fin 2` has no dense control. Rule-derived configuration interfaces stay
    inside (D6)."
  - Proof cell: add `obsTheory_nonnegBounded` OB/FrozenSourcing.lean:84 and
    `nonnegBounded_not_derivedOI` :111.
  - Layer cell: "[K] on `main` (identifiers); D6 [A] on `main` on [K]".

### F7 (Medium). MM-4 names (vii) where each necessity result is proved for the affine class

- **Where.** S:71, S:220–224, S:230–238, S:241–244, S:508–510.
- **Evidence.**
  - Ledger (vii) is "linearity of the substratum update (A5), stronger than the affine restriction
    that amplitude-scale gauge invariance yields" (Main:724).
  - D5 (OA1:176–189), L4 ("L4 needs only the affine form", OC:441–444) and AL (AL1, BL:190) are
    each proved for the **affine** class.
  - "Dropping A5 alone, keeping the affine form, does not restore control" (OA1:523), and dropping
    the affine form "also means modifying the amplitude-scale gauge-invariance step" (OA1:583–584).
  - So an affine, non-linear update is outside (vii) and still inside all three obstructions. The
    necessary ingredient is a non-affine update.
  - BL:81 and :261 and OC route B say "an update outside (vii)", which is imprecise against AL1 and
    L4. This tension is missing from §6.
  - Owner Q1's "conditional ledger posit" applies to (vii), not to the gauge-derived affine form.
  - In addition, "Hard to vary? No in bare form" (OA1:570) is stated of MP-1 only, but S:241–242
    applies it to every candidate. S:242–243 lists two of §A.29's three requirements and omits
    non-adjustability (OC:502–504; AGENTS §A.29).
- **Fix.**
  - Title and S:71: "Setting-selective coupling: a non-affine update (outside the affine class that
    amplitude-scale gauge invariance yields; a fortiori outside (vii))".
  - S:224: "…, that is, a non-affine update. Leaving (vii) alone does not suffice (OA1:523), and
    leaving the affine form modifies the gauge-invariance step (OA1:583–584; Main:724)."
  - S:241–242: "MP-1 is 'Hard to vary? No in bare form' (OA1:570). Every candidate (`G_SM`, `G_σ`,
    R-nl, MP-1, M1) is a Layer-0 revision under §A.29 and would have to state the preserved results
    in advance, give an independent prediction, and not be adjustable to fit any outcome (OC:502–504;
    BL:280–284)."
  - Add a tension to §6: "**T6. 'Outside (vii)' versus 'non-affine'.** BL:81, :261 and OC route B
    (OC:479) name the exit 'an update outside (vii)'. AL (AL1), L4 and D5 hold for every affine
    update, so the exit each proves is a non-affine update."
  - Replace S:508–510 as in F14(b).

### F8 (Medium). "MM-3 is independent of MM-4" conflates insufficiency with independence

- **Where.** S:363–364, S:368, S:383; N:69–73.
- **Evidence.**
  - OA-1 states insufficiency only: the gap-2 repair "does not by itself bear on gap 3" (OA1:524,
    :574).
  - OA-2 Corollary E1 is a necessity statement. With (H4), (SP) and (xiv) kept, a G3 escape requires
    settings that do not merely translate the joint held record. Under H-AR, (H1) and (H3), that
    means leaving (H1) ∧ (H3): MP-1 (a non-affine rule) or supplied P3/E-iso (OA2:587–592). OA2:596–
    599 states this compatibility explicitly.
  - So MM-4 is one disjunct of what MM-3d's G3 escape requires. The other exits are non-additive
    observers, non-nested reads and non-spanning laws (OA2:600–604).
- **Fix.**
  - S:363–364: "MM-4 is not sufficient for MM-3 (OA1:524). Within Corollary E1's scope, it is one
    disjunct of a G3 escape, alongside supplied control, non-additive observers, non-nested reads and
    non-spanning laws (OA2:587–604)."
  - S:383: add "MM-3d (with (H4), (SP), (xiv), H-AR) → MM-4 ∨ supplied control ∨ the OA2:600–604
    exits".
  - N:72–73: "it unblocks no MM-3 route by itself".

### F9 (Medium). MM-2 introduces a third label

- **Where.** S:69, S:151 ("shown necessary as a decision input").
- **Evidence.**
  - The owner's plan admits two labels (#1169 c.6860584645). What S:151–165 shows is that the
    verdict *depends* on the convention: paired results, with "What is shown is the dependence, not
    which convention is physical" (S:165).
  - MM-5 and MM-6 have the same epistemic shape and are labelled "proposed route; load-bearing role
    shown". N:74–77 explains why that is the right label for MM-6, and the reason applies equally to
    MM-2.
- **Fix.** S:69 and S:151: "proposed route (a derivation of the four interface items from the
  Definition and inclusion); load-bearing role shown by paired results". Keep the bullets under it.

### F10 (Medium). MM-5's reach is overstated, and a BL-internal tension is missed

- **Where.** S:255–256 ("Theorem E(b) with heralds … all assume such laws"), S:369–370 ("Every
  affine-class negative result extends beyond coset laws only through MM-5"), S:382 ("MM-5 → the
  scope of every MM-2 result").
- **Evidence.**
  - E(b) assumes (xiv) and (SP), not a coset-uniform law (OA2:528–537).
  - OA-2 Corollary E2 "covers every law satisfying (xiv), coset-uniform or not" (BL:236–237).
  - Theorem S uses the law only through supports at handoff (OA3:349–352).
  - The coset reading comes from the NOTES-r3:76–78 marker ("the hidden premise behind every
    affine-class classicality result (Lemma A-T, E(b), E2, AL)"). That marker conflicts with BL:237
    in the same unit.
- **Fix.**
  - S:256: "Lemma A-T (c), Proposition AL (AL2), P0 (`D_0`, through R2's coset conditioning,
    P0:163–166) and the coset form of heralded preparations assume such laws".
  - S:369–370: "The coset-dependent negative results (Lemma A-T (c), AL, P0) extend beyond coset
    laws only through MM-5. E(b) and Corollary E2 need (xiv) instead (OA2:528, :752; BL:237)."
  - S:382: "MM-5 → MM-1 (μ-R) and MM-5 → the scope of AL and P0".
  - Add to §6: "**T7. Coset premise.** NOTES-r3:76–78 lists E(b) and E2 among results that rest on a
    coset-uniform run law. BL:236–237 and OA2:528 state that E2 and E(b) need (xiv), not a coset
    law."

### F11 (Low–Medium). Theorem S is listed as an affine-class classification

- **Where.** S:353–354.
- **Evidence.** Theorem S is for `G_SM`, which breaks A5 through the term `u_{i+1}u_{i+2}`
  (OA3:132–145; R7 row 28, R7:142). MM-4 itself lists `G_SM` as a Layer-0 candidate (S:241). MM-2
  does bear on Theorem S, through AW-OA3-2 (OA3:660–666), but not as an affine-class result.
- **Fix.** "MM-2 decides the scope of every classification in the affine class (OBL-SP, AL, E(b),
  OA-1 D4), and of Theorem S for `G_SM` through its record and herald conventions (AW-OA3-2)."

### F12 (Low–Medium). The second axis is stated for three entries and argued by definition

- **Where.** S:361–366; N:57–62.
- **Evidence.**
  - The claim is right for MM-1, MM-4 and MM-2 (OA1:534–552). It is not argued for MM-5 to MM-9.
    Their targets are realized by designed classical bijections when locality is not imposed:
    `φ_×` and `φ_0` with `μ_MD` (BL §2), S ⇒ D for every finite trajectory law including Tsirelson
    tables (BL:108–109), and Main:360.
  - MM-3 separates quantum from classical only through its definition, whose target is the qubit
    tier beyond the configuration ceiling. Each of its necessary conditions is met by a classical
    system:
    - 3b: "G2 tests carrier growth, not quantumness" (OA2:372–374);
    - 3c and 3d: 𝔊_K (OA2 N2.3).
  - OA1:548–550 adds that the qubit-tier failure is not established for every observer-relative
    representation.
  - The ranking metric ("how many downstream results each blocks", S:347) is not counted, and items
    6–7 use different criteria: S:372–373 for MM-6, and Bell-specificity for MM-7 to MM-9.
- **Fix.** Replace S:361–364 with: "**MM-3 is the only entry whose target separates quantum from
  classical.** That is its definition, the qubit tier beyond the configuration ceiling (OA1:524).
  Its necessary conditions 3b–3d are each met by classical systems (OA2:372–374; 𝔊_K). MM-1, MM-4
  and, under a fixed convention, MM-2 are met by a classical reversible computer (`𝔖_F` with MP-0a,
  OA1:534–552). The targets of MM-5 to MM-9 are met by designed classical bijections when locality
  is not imposed (BL §2; BL:108–109; Main:360)." At S:347 add: "'Blocks' means that the entry is a
  premise of a construction target. A premise of an obstruction (MM-6) blocks no construction and is
  ranked by its role in the ceilings."

### F13 (Medium). §8 gives a group "provenance" label to references the synthesis uses

- **Where.** S:570, S:108–109.
- **Evidence.** §A.42 item 8 says: "'Provenance only' is a finding about each reference, never a
  label applied to a group of them." The grouped row hides several uses:
  - QH's result is stated at S:323–324: support off `main`.
  - BS Theorem N/N′ carries "Bell stage 5" at S:371 and MM-6. BL itself classes it as "support off
    `main`: gap" (BL:298).
  - SB L3 carries MM-9's N2 necessity (S:335–336; `DEPENDENCIES.md` row D2: gap).
  - APPROX r4a (#1221) defines the E_f classical class, which S:197 and S:209–211 use
    (`DEPENDENCIES.md` row A2: gap).
  - 3A (#1267) defines TC-A, which MM-1a and A1 use through TS (TS:100–101 [R-off]).
  - OICORE-1 (#1214) is cited nowhere in the synthesis text.
  - S:108–109 relies on r7 having been "ChatGPT-reviewed", but review 5891524305 (at `9f7d2612`) is
    not cited.
- **Fix.** Replace the S:570 row with one row per reference:
  - QH: MM-8 Context, support off `main` (gap); or delete the sentence at S:323–324, since no
    verdict rests on it.
  - BS Theorem N/N′: §3 item 6 and MM-6, support off `main` (gap); the exogenous form, Main:364–389,
    is on `main`.
  - SB L3: MM-9, support off `main` (gap), as OC row D2.
  - APPROX r4a: MM-3e and the MM-3 §A.31 check, support off `main` (gap), as OC row A2.
  - 3A: MM-1a through TC-A, support off `main` through TS (gap, as TS's own table).
  - OICORE-1: delete, or "not used".

  Add 5891524305 to the ChatGPT row and to S:108–109.

### F14 (Low–Medium). Name collisions and one identification are missed

- **Where.** S:482–529.
- **Evidence.**
  - (a) The synthesis uses each of these names for two or more different objects:
    - "H4": OC's "records are coordinates" (OC:65), used at S:197, versus OA-2's (H4) nested
      records (S:145, :196).
    - "H3": OC's "laws, no amplitudes" (OC:64) versus OA-2/P0's (H3), no supplied control (S:156).
    - "E1" and "E2": OA-2 Corollaries E1 and E2 (OA2:577, :606; S:196) versus OC's E1 (kernel
      measurability) and Lemma E2 (S:197, :417).
    - "G1": OC's finding (S:209) versus criterion G1 of OA-2's G0–G3 (S:207).
    - "N…": P0 nodes N1–N8, TS nodes N0–N5 and OA-3 N1–N5, beyond the pair listed.
    - "Q1–Q8": the synthesis's own §7 questions, cited as "§7, Q2" at S:114 and :475 next to "Owner
      Q2" (BL) at S:287.
    - "D4" and "D5": OA-1 facts versus P's interface clauses D4/D5 (TS:121, :142).
    - "B": r7's broad reading (P0:442) versus OC route B.
    - "C3": P0's check versus R7's C3 (FIX, R7:214) versus OA-3's C3/C4 rows (OA3:529–530).
  - (b) S:508–510 calls MP-1, M1, H-nl/R-nl, C2, "an update outside (vii)" and `G_SM`/`G_σ` "the
    same lever under different names". They are different objects:
    - MP-1 adds setting control, recorded independence and sourced timing (OA1:566–567);
    - M1 adds a diagonal-confinement clause (M1D:125–128);
    - R-nl is a rule class;
    - `G_SM` and `G_σ` are instances.

    They share one necessary ingredient. No formal map identifies them (Code Review Rules, "Bridge
    and no-go scope"). The synthesis handles the analogous case correctly for the ready resource
    (S:488–489).
- **Fix.**
  - (a) Add the collisions above to S:521–529. Rename §7's questions "SQ1–SQ8", and use "SQ2" at
    S:114 and :475.
  - (b) Replace S:508–510 with: "**Non-affine-update proposals.** MP-1 (OA-1), M1 (MECH-1), H-nl /
    R-nl (TUNE-1), C2 (R7), and `G_SM` / `G_σ` as instances share one necessary ingredient, a
    non-affine update (MM-4). They are not one object: MP-1 adds setting control, independence and
    sourced timing, and M1 adds diagonal confinement."

### F15 (Low). T1's dating is wrong, and it omits AL's standing for the mixed-path unit

- **Where.** S:456–461.
- **Evidence.**
  - Proposition AL first enters at `b8096c79` (2026-11-13 14:21:45 UTC). That is before the
    option-(c) package commit `bac44eeb` (14:25:47) and its head `d015131d` (14:55:32). What predates
    AL is the draft S at `86a413c8`, from which OC copies route C (OC:482–488).
  - BL:258–259 calls the route-C closure "a stated expectation for the separately authorized
    mixed-path computation …, not a substitute for it". Owner Q3 says AL's expected answer is not
    written into that test.
- **Fix.** Replace "OC carries no cross-reference to AL, which postdates it" with "OC copies route C
  from the draft S @`86a413c8`, which predates AL, and carries no cross-reference to AL. AL's
  closure is [A], off `main`, and a stated expectation, not a substitute for the mixed-path
  computation (BL:258–259; owner Q3)."

### F16 (Low). The #1268 pin is stale, and A6 refers to r8 as future

- **Where.** S:21–22, S:28, S:450.
- **Evidence.**
  - At the synthesis commit (18:03:33 UTC), `research/rec-1-1169-20261113` was at `2a9f10ba`
    (17:59:41), not `cd38655c`. So "its remote head equals the pinned commit" is false for #1268.
  - r8 exists as `4b81298f`, and its independent review at `2a9f10ba` is ACCEPT. Against r7 the diff
    touches only the header (r7:1, :14) and the three passages (r7:289–290, :293a, :299–300,
    :320–321; checked here).
  - A6's conclusion therefore holds, but the R7 line numbers the synthesis cites are r7's, and r8
    shifts them by +4 after line 14.
- **Fix.**
  - S:21–22: "…equals the pinned commit, except #1268, whose head is `2a9f10ba` (REC-1-r8, the
    owner's forward fix, independently reviewed ACCEPT; ChatGPT review pending). P0 and r7 are
    unchanged there."
  - S:450: "that r8 (`4b81298f`; review at `2a9f10ba`) corrects".
  - Add: "R7 line numbers are r7's at `cd38655c`."

### F17 (Low–Medium). A5 maps TC-A into P0's class without showing that it belongs

- **Where.** S:448–449.
- **Evidence.**
  - P0's class requires H-AR, held-at-use typing with records formed inside `S`, and (H4) or
    (V-ii-H) (R7:254–256; P0:457–458).
  - TC-A's memory (e) is MP-0b, with records held outside `V` (TS:143), and no member's observer
    layout is exhibited (TS:141).
  - TS:296–297 states only a conditional: if a member met E(b)'s hypotheses with (SP).
- **Fix.** "**A5. TC-A and P0.** If a TC-A member were specified and fell in P0's class (H-AR,
  held-at-use records inside `S`, (H4) or (V-ii-H)), its prepare–measure fragment would carry P0's
  O-U. TC-A's (e) rests on MP-0b, which places records outside `V`, so membership is not shown, and
  TC-A has no classical pass from E(b) either (TS:296–297)."

### F18 (Low). T5 is escalated beyond P0's record-only marker

- **Where.** S:454–455 (each tension "is a finding to propagate when its record is next revised")
  and S:476–480.
- **Evidence.**
  - AW-P0-2 is "record-only … The presumption is recorded here only" (P0:488–492).
  - P0's scoped result "may not serve as a premise until independently reviewed" (P0:479).
  - Treating it as a propagation finding against OA-2 r4 and OA-3 r4 on `main` goes beyond P0 and
    beyond §A.46 item 7. §7 Q4 already frames it correctly.
- **Fix.** Append to S:454–455: "T5 is carried as P0's record-only marker; any propagation waits on
  the read-only check of §7 Q4."

### F19 (Low). MM-7 and MM-8: what is shown necessary is narrower than the entry text

- **Where.** S:297–305, S:318–320.
- **Evidence.**
  - MM-7: PPS:136–145 shows that restricted affine span is necessary. "Physically preparable" and
    "a reason independent of the target table" are §A.29 and non-import requirements (OC:494), not
    part of the necessity.
  - MM-8: the necessity follows from the definition of a selector plus Main:360 and :427, as
    N:78–80 says. The entry does not say so. The PR control is generic and not sourced by OI
    (ChatGPT 5895564670).
- **Fix.**
  - S:303–304 → "needs `𝒫` of restricted affine span. That the restriction be physically sourced,
    for a reason independent of the target table, is a §A.29 and non-import requirement (OC:494),
    not part of the diagnostic."
  - S:320, add: "This necessity follows from the definition of a selector. The PR control (OC:497–
    500) is generic, not sourced by OI."

### F20 (Low). Labels used as support are undefined, and NL-C′'s range conditions are missing

- **Where.** S:94–95, :127, :131, :194, :276, :575–577; N:47.
- **Evidence.**
  - S3, S4, P, AF, NPS1 and NIS2 are not defined in §0 and are not in §8's list of records on
    `main`. MM-1a and MM-3b(iii) rest on S4:464–474 and P:143 and :184–199, which N:47 says were not
    re-read.
  - Checked here: S4 (`drafts/tune-1-20261111/TUNE-1-STEP2-SESSION4.md`, blob `17ca08f8` per TS:69)
    lines 464–474 state NL-C′ with `ε < 1/8`, `K ≥ L+1` and `O ⊇ C`. P (blob `84f71030`) lines 143
    and 184–199 give a fixed `r_O` and program blocks that are translates of `C` outside `O`. The
    support holds.
- **Fix.**
  - Add S3, S4, P, AF, NPS1 and NIS2 with their paths and blobs (from TS:66–75) to §0 and to S:575.
  - In MM-1a's assumptions (S:95–97), add "`ε < 1/8`, `K ≥ L + 1`".

### F21 (Low). MM-3c and MM-3e omit stated hypotheses

- **Where.** S:195, S:197.
- **Evidence.**
  - Proposition B is stated for "`R` injective on `W`" (OA2:244). "Always preparation-noncontextual"
    drops that condition, and Corollary B′'s "preparation equivalences coarser" disjunct is exactly
    the case where `R` is not injective.
  - The direction is right: only (⇐) is used, and (CVX) is correctly left aside (§A.34; N:117–118
    asks for this check, and it passes).
  - E2's consequence names "a pair of incompatible sharp measurements **with their update rule**"
    (OC:373–374).
- **Fix.**
  - S:195: "For `R` injective on `W`, the configuration model is preparation-noncontextual (B(i)),
    and measurement-noncontextual when the restriction map is injective (B(ii)(⇐)). Target: G3 on
    the prepare–measure fragment."
  - S:197: add "with their update rule".

***

## Checks that pass (recorded so the confirmation need not repeat them)

- **Authority and scope.** S:10–15 quotes c.6860584645 verbatim. Nothing is merged, run or adopted.
  The ranking is not presented as a planning change (S:5–6, :422, :556–557).
- **Proposed routes.** None is presented as found or adopted:
  - MM-1's five producer routes are marked "none tested", MP-0a as "a new §A.29 premise once
    selected".
  - MM-3's routes are marked "none constructed".
  - MM-4 carries the §A.29 framing, which F7 completes.
  - MM-5, MM-6 and MM-9 are marked open.
  - §5 (S:418–420) lists every unadopted premise.
- **Faithfulness.**
  - TUNE-1's stop is scoped by measure in MM-1's "Not shown" bullet (S:110–114), and MP-0a is
    admitted data, not a producer. F1 fixes the one place that drops this.
  - P0 stays O-U, with the scoped pass under (LF) stated as one-directional (S:416–417).
  - N2.1 and 𝔊_K are kept distinct (S:513–520).
  - AL's two safeguards are carried: MI\* is distinct (S:287–288, :501), and the full-history
    convention applies to AL only, with the selected read kept separate (S:173–175, :496).
  - Q3 is respected at S:310–311 (and needs adding to T1, F15).
  - Option (c)'s E2 class boundaries are carried in full (S:197).
  - The PAD/S7 distinction is right (S:280–281).
  - #1274's integration gates are not crossed.
- **#1060.** Used only at S:323 and S:573, as context.
- **§A.46.** S:7, S:422–424 and S:575 state that no unit result is established. The support layers
  (S:53–56) are applied consistently, except at MM-3a (F6).
- **Register.** Neutral. No self-assessment, reader instruction, history narration or caps emphasis
  in `SYNTHESIS-r1.md`. "The strongest shown-necessary statement" (N:70) and "a clean
  classification" (N:106) appear only in the working notes.
- **A1–A3 and A6.** Accurate as cited, with the pin note of F16 for A6.
- **T2 and T3.** Real. T2's four quotations check: OA1:569, TS:139, R7:212 and Q1. T3's planning
  edge is in the #1147 body ("Prerequisites: native retention (O-RET, #1032)"). T4 reads TS:140,
  :247–251 and OA1:141–143 correctly; NOTES open point 1 is answered: TS's "open" refers to the
  held-record route (OA1:522: N1-K native under swap, N1-S open), which T4 states.
- **Placement.** The drafts directory is correct under §A.36. No forbidden path strings appear in
  either file.
