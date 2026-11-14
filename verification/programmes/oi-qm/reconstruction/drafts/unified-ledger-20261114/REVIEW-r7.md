ACCEPT WITH CHANGES

# Independent review of LEDGER-r7 and RESPONSE-LC-2

This review is read-only, paper-only and non-author. It covers `diff LEDGER-r6.md LEDGER-r7.md` and
`RESPONSE-LC-2.md`. `origin/main` was re-fetched and is `dfeec843`. No file was edited, nothing was
run on OI rules and nothing was posted.

## 1. Part A: REVIEW-r6

**S1 (§H.4 homes): applied.** Each home was checked at its source:
- **D4:** the #1234 body, open item 2: "Companions and book … The book has not been swept for
  this".
- **M2:** §2.4, "#1169, #1236".
- **M5:** the #1055 row of §H.3.
- **M6:** §4.1, "#873".
- **U-3:** #914 comment 6877908458.

The added note that `QUEUE-PROPOSAL-r4.md`:867 proposed U-3 as RO-10 is accurate. It is
correctly marked as a proposal, not an assignment.

**N1 to N5: applied.**
- **N1.** C-STR-8 is DM only as part of B-QM-1; the Main:18 quotation is exact.
- **N2.** The four observations are placed as follows:
  - :168 and :178 go to F-17 as DA;
  - :198 goes to F-17 as DC;
  - :903–904 against :926 becomes D14;
  - :913 becomes D15.
- **N3.** Introduction:179 cites "[Main §3.3; Substratum §3.2]", and it is added to D2 in §11 and
  in §F.1.
- **N4.** The #914 row for M1 now names its record.
- **N5.** "any QB5(a) execution" and "any merge" are added.

## 2. LC-2: the Structure re-audit

**Every T-1 to T-17 entry has a row.** §R.1's mapping matches the audit's §4.5 table
(`COVERAGE-AUDIT-r4.md`:906–925) entry by entry:
- T-2 (:361–389) falls within B-STR-1's sources.
- T-12, T-13, T-16 and T-17 keep the audit's own rows.

**B-STR-6** is correct. Structure:886 says the features "are forced by the structure of
observation", and :888 says they are derived "from 'observation occurs' alone". UO as stated is
right, against two sources:
- Structure:120 and :166 place the same features under observer admission (C1–C4).
- Main:18 shows the Born form is definitional and that representability does not single out
  memory.

**The four candidates read as the sources do:**

| Candidate | Structure | Checked against |
|---|---|---|
| D12 | :872, :886–890 | — |
| D13 | :775, :783 | SM:865, "This is a hypothesis, not a derivation"; SM:936–944 |
| D14 | :896, :904 at Level 1; :926 at Level 3 | — |
| D15 | :908, :913, "Three chiral generations \| Confirmed" | — |

## 3. LC-3: the Main-independence trace

**The rule.** The rule I apply is the one in `AGENTS.md` at `origin/main` (`dfeec843`, Code Review
Rules, "Whole-framework scope"), merged by PR #1240 (`612252621`). It reads:

> `papers/Main.md` must be independent of downstream companion papers. Main may mention downstream
> results but must not depend on them, including through indirect labels or unnamed references.
> Permitted mentions include forward pointers to later work, descriptions explicitly labelled as
> conditional or proposed, and references identifying further applications; each mentioned result
> is identifiable as downstream and carries its own status where it has one. Main must not use a
> downstream result to prove its claims, present a downstream conclusion as established by Main, or
> require a downstream theorem for its argument to be valid. Test: removing every downstream
> reference must leave Main's proofs, assumptions and conclusions intact; if removal changes what
> Main establishes, the passage contains a dependency, not merely a pointer.

The writer is right that the copy loaded in these sessions is older ("must not reference or cite
downstream results"). `git log -S` on `main` shows the change in `aefc239c3`, merged by #1240.

**The four passages.** Under that rule I agree that none is a dependency.

| Passage | Assessment |
|---|---|
| Main:20 | Labels its Bell route as a target and its open part as "part of H-Bell", with status. It is a permitted forward pointer. |
| Main:660–674 | The lemma's horizon and foliation are stated hypotheses, and the proof is the little-group classification. The SM and gravity mentions are applications. |
| Main:76 (D18) | Its realization numbers are mentions without downstream identification or status. The removal test leaves C3's necessity, the data-processing bound "for any realization", intact. |
| Main:704 (M-33) | "This framework provides … quantitative predictions" presents downstream content as Main's. That fits the clause "present a downstream conclusion as established by Main". |

For Main:76 and Main:704, MC-candidate is the right kind of work.

### Should-fix S1. The reconciliation with T2 can go further on `main` than §R.2 says.

The sources are #1238 comment 6800989329, PR #1241 on `main`, and the #1234 body.

- **T2's four other dependences are named in the comment.** They are:
  - the wave-speed comparison using [SM §4.1];
  - the `K_eff` grading identity;
  - "the 10^-32/10^-64 figures from `GR.md:48`";
  - the transfer across representatives.

  The wording PR that corrected them, #1241, is on `main` (`1257617a9`, an ancestor of `dfeec843`;
  commit `e806e52cb`). After it, Main:216, :340 and :352 give the figures "for the horizon ratio of
  (C2)'s realization clause".
- **T2's two Bell items can be located.** #1234's body names them, as item 3: "Main.md:414 and :416
  rest the [graph that varies with the state] on a downstream citation ([SM §3.1], G(x))" (bracketed
  words paraphrased). Main:20 is not one of
  them.
- **The re-anchoring brings D18's pattern to a second clause.** (C2)'s realization clause, Main:74,
  reads "Realization — τ_S/τ_B ~ 10⁻³² at the horizon", which is GR:48's ratio. It is not identified
  as GR's and carries no status. It is a mention, not a dependency: the figures at :216, :340 and
  :352 are magnitudes, not proof steps.

Replace §R.2's reconciliation bullets with:

"T2 (#1238 comment 6800989329) classed 6 of 37 items as dependences.
- Its four named non-Bell dependences were corrected by PR #1241 (`1257617a9`, on `main`). After it,
  Main:216, :340 and :352 cite 'the horizon ratio of (C2)'s realization clause' (Main:74).
- Its two Bell items are #1234 item 3, Main:414 and :416, which remain with #1234. Main:20 is not
  among them.
- Main:74's realization clause ('τ_S/τ_B ~ 10⁻³² at the horizon', GR:48) shows D18's pattern and is
  recorded with it as an MC-5 candidate."

Then extend D18 and its §F row to cite `papers/Main.md`:74 and `papers/GR.md`:48.

## 4. LC-4: the R ≈ ε record

**Confirmed by my own search.** This is a negative claim (§A.19), so I searched `main` myself, in
three ways:
- `grep` of `verification/` and `papers/oi_lattice_code/` for "kernel width", "kernel-width",
  "position-space width", "R ≈ ε" and `R \approx \varepsilon`;
- `git grep` at `origin/main` for "smear", "G_oo" and "kernel_width";
- a listing of `papers/oi_lattice_code/trace_out_fractional/`.

What the search found:
- **The only `verification/` hit** is a string guard in `verification/lean/edge_rigidity_probe.py`
  (:9823). It notes that the kernel width in SM §3.1 is "not a kernel claim". It is not a
  computation.
- **The nearest computation** is `grr_spectral_measure.py`. It computes the spectral measure; SM:130
  calls that "the spectral-measure counterpart of the R ≈ ε kernel-width result".
- **No file computes the position-space width R.** That includes `operator_conditioning.c`, whose
  "width" is a histogram width.
- **The claim stands** at SM:134 ("a direct computation of its position-space width gives R ≈ ε")
  and at ch19:244 / FULL:5391. Neither cites a record.

D17, with its MC candidate and RO, is correctly scoped to "not found on `main`".

## 5. LC-5: the reduced-depth passes

**Stated precisely.**
- **ch13 §13.6 (:110–131).** Read; D16 holds at source:
  - appendix-a:28 defines S as fixing "the prediction's value";
  - ch13:118 says the waiting-time forms vary by enzyme;
  - ch13:124 gives a "structural reading";
  - ch13:128 says the operational prediction requires "its own derivation" and that the memory
    test "alone does not separate" the reading from classical memory.
  - The FULL mirrors at :3605, :3611, :3615 and :5671 match.
- **What remains.** The remainder matches LC-5's scope (`QUEUE-PROPOSAL-r4.md`:596) less what was
  done:
  - ch13 §13.4 (B4), §13.5 (B5) and §13.7;
  - the ch14–ch17 derivations behind B1, B2, B6–B14, F1–F4 and F9–F12;
  - the proof bodies of Main §3.4 (:429–658) and GR §3.3 (:164–298).

## 6. LC-6: census spot-check

**Confirmed, with one count corrected.** A script looked up each of the 22 identifiers in the
OIBridge declarations and the census registry. Each is declared, and each lies in a "current"
family, except `frozen_sourcing_verdict`, which is "kernel-only". Some examples:
- `complete_passive_iff_commutative` and `central_classification` are in CentralObservation,
  family "OI-N passive observation".
- `fullClass` is in ImplementationLocality.
- `ruleDynamics` is in SecondOrderDrive, family "continuous time (CT2)".

None of the 22 appears as a superseded key in the census `supersessions` map. The witnesses listed
for the equivalence displays agree with the census and the module declarations.

**Nit N1. There are three superseded citations, not two.** The manuscripts cite three superseded
identifiers beside their successors:
- `oiPlusPos_iff_qm` and `carrier_general_oiPlusPos`, both at GR:242 (and the latter also at
  Main:588);
- `derivedOI_qm_iff_layerFlowExecutable`, beside its primed successor, at GR:266.

Change "Two superseded identifiers" to "Three", and add GR:266. The census rule is met in each case.

## 7. Unchanged

- **Identifiers.** A script comparison of r6 and r7 shows no identifier removed and B-STR-6 the
  only one added. C-BIO/B3 is a sub-row, and D12–D18 are new D entries.
- **Unresolved findings.** There are still ten U rows. U-1, U-9 and U-10 carry r7 outcomes marked
  unreviewed, and none is marked resolved.
- **Candidates.** D12–D18 are labelled candidates, and no manuscript is changed.
- **New errors.** No new conditional-to-unconditional, witness-to-theorem or fit-to-prediction
  error was found.
