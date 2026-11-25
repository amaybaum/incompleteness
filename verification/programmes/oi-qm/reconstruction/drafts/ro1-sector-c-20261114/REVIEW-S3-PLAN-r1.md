REVISE — `S3-PLAN-r1.md` at `38b5a4604e7934c90cd579bb267c1eb086b6ea5c` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Independent review of the S3 plan, r1

## Scope and method

- **Reviewer.** Independent reviewer; not the writer.
- **Constraints.** Read-only and paper-only: no computation, no Lean build, no edit, no commit, no
  post.
- **File.** SHA-256 `582cb141…9ac4`. The supplied copy is identical to the committed file.
- **Read through the REST API:**
  - #866: body and all 71 comments;
  - #913: body and all 3 comments;
  - #1169 c.6884568026 and c.6880239486;
  - #1023 c.6555169983.
- **Checked at source on `main`:**
  - MR-1: `preregistration.md`, `README.md` and `amendments/MR-star.md`;
  - `composition-access-20261024/REPORT.md` and commit `86cd47e5`;
  - Main:326–328, :482 and :682;
  - Substratum:463;
  - GR:350.
- **Line numbers** are the plan's.

## Summary

The plan covers most of the owner's terms well. Specifically:
- #866 and #913 are represented accurately.
- No authorization is changed.
- Representable, available and derived are kept apart (MR-1 §1).
- The countercontrols K-1 to K-6 are sound.
- Requirements B1–B3 and the tiers of C are built in.

Three major findings block acceptance:
1. Route M's negative closure is mis-specified. Its condition (a) holds by definition, and its
   condition (c) is false on the record. No decisive test is named, although the corpus supplies one
   (F1).
2. Requirement A(iv) asks for fully specified negative controls. As planned, meeting it would need
   construction, or MR-1's unauthorized stage 2 (F2).
3. U2 and U3 overlap a #866 allocation in flight, and loci that #913 holds for #914. The plan does
   not demarcate the overlap (F3).

## Findings

### Major

**F1. Route M's negative closure would close the route prematurely, and its decisive test is
missing (§8.6, ll. 410–420; §8.3, ll. 334–336; §8.4).**
- **(a) Condition (a) holds by definition.**
  - MR-1's *available* level is "a composition of native steps" (preregistration §1). P-L3 makes
    every native step a bijection of configurations.
  - So "every natively executable recording operation is a permutation of configurations" follows
    from the definitions. It is not a finding U4 could fail to confirm.
  - The open route the corpus records lies elsewhere. Main:588 says "the observer-level lift … derives
    neither a non-monomial admissible operator nor the layer flow, **the site-space wave-operator
    formulation being unresolved rather than excluded**".
  - SM:224 states the rule "at either the substratum-symbolic level or an observer-level linear lift".
    On that lift, the native linear step acts on field amplitudes by a non-monomial matrix.
  - Condition (a) must be scoped to the configuration-level representation, and §8.6 must say that the
    wave-operator / observer-level-lift route is not closed by it.
- **(b) Condition (c) is false on the record.**
  - On K1, native superposition (S-L1, MR-star) gives class-(i) interference of the additive field.
  - A classical eraser (CC5) and the Catani et al. model (AW-MR5, CC4) reproduce returned
    interference without any class-(ii) import.
  - So "every account of returned interference needs class (ii), or a U or P that is not available"
    cannot be confirmed, and route M could never close negatively, even though that interference is
    classical.
  - Restate (c): class-(i) interference that a generalized-noncontextual model (M-1, M-2) reproduces
    supplies no quantum coherent operation. Only interference beyond such models needs class (ii) or
    an unavailable U or P.
- **(c) A decisive test is on record and is not used.**
  - S-L5 (MR-star, ll. 584–594) is a class-(i) result derived without reference to QM: on K1, "A record
    (R1) never causes (ii): marking is non-invasive". In #1023 c.6555169983's words, "Marking cannot
    destroy interference".
  - This conflicts on its face with observed which-path complementarity. That is a raw/direct
    observable under §A.24.
  - The plan files S-L5 only as a class-(i) item (ll. 314, 375) and as a way information can become
    inaccessible (l. 348).
  - It should be U4's first check, as a candidate class-(iii) confrontation. It is conditional on two
    things: the K1 reading of the step, and identifying MR-1's marker region with a which-path
    detector. Both conditions must be stated.
  - Either outcome is decisive at its scope:
    - if the identification holds, native K1 recording misses observed complementarity (a raw-direct
      miss);
    - if it fails, the K1 marker is not a which-path detector, and route M on K1 is empty.
- **(d) MR-1's GAP has a scope the plan does not carry.**
  - The GAP is for `K★ = {K1}`, sources σ1–σ13, and a budget below recurrence.
  - σ12 is not screened: the non-additive native-type rules, including native-Y and the state-varying
    coupling graph of SM:104–106. MR-star states: "These are the rules on which conditional dynamics,
    and so pointers and settings, are not excluded by S-C1".
  - The state-varying coupling graph is track (b)'s Bell route.
  - "Under the existing premises" in (a) must therefore be indexed by the reading of P-vii (C-1,
    #1234; X2). Under the scoped reading, MR-1's K1 results do not cover the non-additive dynamics
    the reading admits.
  - The GAP's own caveats should be carried, from #1023 c.6555169983: "This is not a no-go, and it
    makes no claim against classical explanations", and "the absence of a proved ready supply is an
    open sourcing problem, not a proof that no ready supply can exist".

**F2. Requirement A(iv) cannot be met as planned without a stop condition or unauthorized work
(§8.4 item 5, l. 384; §8.5; §9 stops, l. 445).**
- §8.4 item 5 asks U4 to specify "the four negative controls of §8.5, class (iv) … completely". Those
  are M-1, M-2, M-3 and M-7.
- Specifying M-1 to M-3 completely, with full branch masses and residual state, is construction. §9
  makes construction a stop.
- It is also the content of MR-1's controls-only stage 2. Stage 2 must return the CC reference
  results (README: "a controls-only stage 2 … returns every reference result"). Stage 2 is not
  authorized, and O-REC is #866's.
- On the record, the fully specified negative controls are:
  - **M-7.** The reversible PR model with complete records (SEL-EXCL-1 §§2–3, reviewed, not merged).
    It also fails coherent operations, since `T` is a permutation.
  - **PC-1's rules on `main`.** "classical measurable bijections with function-valued records"
    (#866 c.6627392555).
- **Fix.**
  - Name these as the class-(iv) controls available without construction.
  - Mark M-1 to M-3 as specified at class level in MR-1 and executed only under an MR-1 stage-2
    authorization.
  - Do not make their complete specification a U4 deliverable.

**F3. Duplication is not excluded (§§2.1–2.3, ll. 107–108, 433–434; owner question 4).**
- **The #866 allocation.** #866 c.6863601327 (2026-11-13) allocates a paper-only "native apparatus
  source screen" to Codex. Its step 2 is: "For each ingredient mark **derived / assumed / absent**".
  The ingredients are "(i) a ready configuration, (ii) a selected setting/intervention, (iii) a held
  readout and failure history, and (iv) resources for repeated runs".
  - That is U2's per-action ledger and part of U3's renewal question.
  - Under the ownership reset (#1169 c.6880239486), work in flight "keeps its existing writer".
  - Owner question 4 limits the overlap to "candidate selection" (l. 456). The overlap is in the
    classification itself.
  - U2 and U3 should start only after the owner answers question 4. If the screen is running, U2
    should be scoped to the actions and records the screen does not classify.
- **The #913 loci.**
  - #913's gates "Native preparation, settings and clock" and "Observer-access closure — Define
    allowed composed probes, including workspace and delayed reads" overlap U1's criterion for
    preparation and settings, and U3's closure (§5).
  - Those gates are the work loci of #885 obligations 5 and 6. Their accountable home stays #914, row
    O-INS (c.6628909432).
  - §2.2 lists the loci (ll. 117–121), but §2.3 omits #914 O-INS, and nothing says how U1 and U3
    avoid restating them.
  - State the demarcation, for example: U1 fixes a criterion used by RO-1 as a definition only, and
    routes any closure finding to #913/#914 without discharging it. Add #914 O-INS to §2.3.

### Medium

**F4. The setting criterion builds in an open posit (l. 167).**
- "A native process that writes a setting value whose law is independent of the unused source"
  builds measurement-independence-type freedom into the definition of executability.
- That posit is open at S5 (ledger Q8). MR-1 AW-MR7 says: "Free choice is decided as a property of
  `μ`", and :512 says "never assumed".
- Drop the independence clause from the criterion, and record setting-law independence as a property
  each classified record must decide.

**F5. The declared access is a free choice that can decide outcomes (§3; K-2).**
- S-L7 (MR-star) shows that whether the native access is an epistemic restriction depends on which
  slices it reads: "Which slices the access reads is not fixed by the sources". S-L7 cites SM:252 for
  this; at today's `main`, SM:252 is Lemma 1c, so the line reference has drifted and needs
  re-pinning.
- MR-1's *available* level is relative to "the declared access".
- U1 must freeze the access declaration, with its source, before any classification, and K-2 must
  cover it explicitly. Otherwise the criterion can be tuned through the access.

**F6. AW-MR8 is quoted in superseded wording (l. 294).**
- MR-star C-6 (ll. 1401–1410) rescoped it: "The K1 step is additive and supplies no conditional
  dynamics (S-C1) … Operation-selecting settings, adaptive operations and subsystem undo therefore need
  a non-additive step, or structure beyond the K1 step. Whether the K1 step supplies records, through
  wakes, is undecided (C-4)".
- C-6 also withdraws the substratum-level reading. Cite the scoped text.

**F7. Route-M tiers are applied to units they were not defined for (§9 table, ll. 432–434).**
- The tiers of §8.6 are defined for route M. U2 and U3 are said to reach the "weaker tier", which is
  route M's "recording explains memory" tier.
- Either define a tier scale for U1–U3, or mark their column as not applicable, with the output type
  instead.

### Minor

- **F8 (l. 168).** State whether additive, setting-dependent offsets count as setting-dependent
  interventions. MR-1 records: "Setting-dependent outputs remain possible as offsets" (#1023
  c.6555169983), while S-C1(a) gives no selection of operations.
- **F9 (l. 336).** Point 1's inference is correctly marked [A-inf]. Its premises carry stronger
  labels and should say so: the diagonal-preservation lemma is a paper proof on `main` (Main:326–328),
  and P-L3 is a premise. The conclusion is then exact at configuration level and scoped by F1(a).

## Checks requested by the coordinator

1. **#866 and #913.**
   - *Status.* Accurate. I checked the following against the body and comments:
     - CP-PREP-1 "NOT PASSED" (c.6719027303);
     - the controller lead (c.6713088252);
     - NATIVE-INT-SRC-2 "STOPPED / UNSOURCED";
     - NATIVE-PREP-SRC-1 completed, "not permission for another source screen" (c.6765674746);
     - O-REC blocked, with MR-1 stage 2 not authorized;
     - O-SET "ready" under PO-1102;
     - P0 "not authorized";
     - the 2026-11-14 writer reset;
     - O-REUSE "blocked: O-INS", "not authorized";
     - the REPORT landing at `86cd47e5`, which is on `main`.
   - *Authorizations.* None is changed.
   - *Duplication.* Not excluded (F3).
2. **The criterion.**
   - Native in form, except setting independence (F4) and the access declaration (F5).
   - K-1 stops PR from vanishing by declaration, and K-2 and M-6 stop the criterion from being chosen
     for its quantum outcomes. F5 is the one gap.
   - Coverage is preserved, or its loss reported (K-3).
3. **Route M.**
   - A(i)–A(iii): met as definitions.
   - A(iv): not met as planned (F2).
   - B1: met (Point 1).
   - B2: met (R, U, I and P, with the preparation included).
   - B3: met (Point 3 with K-3).
   - C: tiers present; the negative closure is mis-specified (F1).
   - *The working analysis* ("a native record write is a configuration permutation, so it supplies
     neither coherent operations nor PR exclusion"):
     - it is correct at configuration level, and properly [A-inf];
     - it is true by definition there (F1(a));
     - it does not reach the observer-level linear lift, which Main:588 records as open.
   - *The MR-1 GAP.* The quoted phrases match #1023 c.6555169983 and MR-star. The scope and caveats
     are not carried (F1(d)), and AW-MR8's wording is superseded (F6).
   - *Closure.* Premature as written; no decisive test is named (F1(c)).
4. **Units.**
   - The dependency order U1 → U2 → U3, with U4 after U1, is genuine.
   - The units are bounded and paper-only, and their stops are real.
   - The tier column is misapplied (F7).
   - U4's item 5 hits the construction stop (F2).
   - No hidden authorization request: owner questions 1–6 ask openly. No new premise and no
     computation.
5. **General.**
   - Off-`main` citations are labelled.
   - Defined, available and derived are kept apart.
   - Conditional and established are kept apart, except F1(a)–(c).
   - The first step (U1) is kept separate from the ultimate goal (§1).

## Verdict

**REVISE.**
- **Required:** F1, F2 and F3.
- **Also to apply:** F4–F7.
- **Optional:** F8 and F9.
- **Re-review:** a focused re-review of §§2.3, 3, 8.1, 8.4–8.6 and 9 suffices.
