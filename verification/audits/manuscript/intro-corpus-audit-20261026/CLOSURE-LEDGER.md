# Closure ledger for Issue #941

**Authority and standing.** This ledger was prepared read-only as Unit 1 of the #941 closure programme, under the owner
direction recorded in #941 c.6676652751 (amaybaum, 2026-11-06). It was independently reviewed: the review returned
ACCEPT WITH CHANGES and its findings 1–14 are applied (summary: #941 c.6677061224); a delta check of the revision
returned ACCEPT WITH CHANGES (minor), and its corrections D1–D3 are applied: SC-23 and SC-30 are "not #941"; SC-30 is
re-mapped at `721f35fb`; the row decisions match the list; and GR:260 and Main:147 are added to OD-15 (#941
c.6677206437). The review files themselves are not on `main` and are cited as provenance. The ledger is landed under
the owner rulings of #941 c.6677500012, quoted in "Owner rulings" below. It records planning dispositions (AGENTS.md
§A.45): no row establishes a scientific claim, and each row's scientific status rests on the evidence it cites. Every
"Proposed outcome" stays a proposal until the independent closure audit (Unit 6) confirms it. SC17-68, SC31-140, SC33-111
and README-28 are carried out by the change that lands this ledger, and O-17 and O-23 are confirmations for its
reviewer; their "Applies now?" entries describe `main` before that change, and their status is left as it was at review
and is confirmed in Unit 6. Where an owner ruling bears on a row, the "Owner decision" cell names the ruling item; the row's outcome is unchanged.
Wherever a ruling quoted in "Owner rulings" (c.6677500012) selects among, narrows or refuses an option offered elsewhere
in this ledger (in a row, the decision list or the execution package), the ruling governs.

Read-only checks added after the review:
- #946 c.6441584771;
- #1028's and #1029's register bodies;
- #1002 c.6597320954 (ancestry of `4759d27b`);
- Main:340 and :616;
- the book black-hole status sites, with their FULL mirrors;
- the round record at `44236326`;
- the 43 reference keys.

**Objects read.**
- `main` = `c95f2f9e6e3303dcce5bb46ff0fa02641240aaae` (fetched 2026-11-06). By the end of the work `main` was
  `721f35fb` (#1157). `git diff c95f2f9e 721f35fb` is empty for every path cited here: the Introduction, Main,
  Substratum, `introduction_repro/`, the audit record directory, `evidence-replay.yml` and the census. The Introduction
  there is the #1134 rewrite
  (head `64a84b12`, merged as `9f9dbc28`), 281 lines (the last is `\endgroup`), with no Appendix A and no Lean
  identifiers. "Intro Lnn" below means a line of this file. Between `721f35fb` and `424f28b1` (the `main` commit the
  change landing this ledger is based on) `git diff` is empty for the same paths, so every line reference holds at both.
- The #942 audit record at `16fc745d` (kept branch `audit/intro-corpus-20261026`, closed PR #942; not on `main`):
  `FINDINGS.md` (`F:n` = line n), `PLAN.md`, `CORRECTIONS-LEDGER.md`, `EVIDENCE.md`, `proofs/README.md`,
  `tracks/C-consistency/REPORT.md` and `REVIEW.md`, and `tracks/FINAL-AUDIT/slice2-book-explainer-intro.md`.
- All 45 #941 comments, the #941 body and planning block, the #942 PR and its 10 comments, #1134's body and claim map
  (`51eb9698`, an ancestor of `main`, not in its tree), #1118 (body; no comments), and targeted reads of #918
  (c.6650823924, c.6650329205, c.6643090231, c.6643385201, c.6649656506), #1124 c.6655788106 and #1028
  (c.6628572816, c.6657923668, c.6658178394).
- Files on `main` (at the commits above): `papers/introduction_repro/README.md`, the intro-corpus-audit tracks (SC17,
  SC31, SC33, SC42, SC44/SC45), `introduction-repro-ext/README.md`, `.github/workflows/evidence-replay.yml`,
  `verification/lean-manuscript-census.json`, `tools/lean_axiom_check.py`, `tools/release_gate.py`, the BH-01
  `REPORT.md`, and `papers/Substratum.md`.

**Off-`main` objects.** `16fc745d` and its files (`FINDINGS.md`, `PLAN.md`, `CORRECTIONS-LEDGER.md`, `EVIDENCE.md`,
`proofs/README.md`, the Track C and FA slice files), the pre-rewrite Introduction heads `4a260ca9` and `44236326`, the
draft commits `bace5ef8`, `72014a79` and `3e600003`, the commits `021850d9`, `a2be1e45`, `8f6ea594`, `2bc65ae9` and
`cb2029ce`, and the blobs `7c5f18b4` and `322f5321` are not reachable from `main`. They are cited as the origin of a row's
obligation (provenance). No row's disposition rests on their content: each "Applies now?" entry is checked against
`main`, except X-2's FINDINGS :660 citation, which is marked as provenance for a Unit 4 check; EV-L's rests on the
acceptance recorded in #942 c.6433846714 and on #1134's supersession. `c.N` is the id of a GitHub issue comment in this
repository; comments and Issues are the planning record (§A.45 rule 1), not evidence on `main`.

**Abbreviations.** H§n = the #942 handoff c.6628558706, section n. G1 = Group 1 record c.6657964075. G4 = Group 4
record c.6657984736. COV = coverage assessment c.6658270777. CR = #918 carrying record c.6666760529. T3 = Group 3
transfer record c.6658063924. Outcomes: (a) corrected and verified; (b) already satisfied, with a sourced no-change
disposition; (c) waived as outside the Introduction's scope; (d) transferred by owner approval to an open accountable
Issue. "Unit 6" means confirmation in the independent closure audit only, with no edit.

***

## 1. Planning-block rows and #918-retirement items

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| #1134 F-9 | #941 body, Rows; c.6661149176; #1134 claim map §3 | Main §3.4 lacks the Egri et al. credit the Introduction gives | No: landed by #1137 (`0da40cff`, an ancestor of `main`) | #941 | complete | (a) | none | none | 6 |
| #1134 F-10 | #941 body, Rows; c.6662268910; #1134 claim map §3 | Disposition of `papers/introduction_repro/` | No: #1138 (`a1f1cb0d`) corrected the README role; the JSON is unchanged | #941 | complete | (a) | none (but see EV-14) | none | 6 |
| EXPECTED_28 | #941 body, Rows; CR §1 | Workflow pin reachable only from a staging branch | No: `evidence-replay.yml`:62 pins `2714278a`, an ancestor of `main`; :98 reads the retained path | #941 | complete | (a) | none (the unreviewed status is EV-28) | none | 6 |
| EXPECTED_14 | G1 §2; c.6658483078 | Pin `4a260ca9` not reachable from `main` | No: :60 pins `f5efa7a0` (an ancestor), blob `61cfd6ea` (:61, :97) | #941 | complete (#1129, `8418ec34`) | (a) | none | none | 6 |
| ADM-W | c.6665390344 §3; c.6666781861 | writer-941 clause names #918's branch | No: re-pointed, then recorded complete (c.6676559595) | #941 | complete | (a) | none | none | — |
| ADM-B | #941 body, "Objects" and planning-block Readiness | The body names the object under audit as #918 at `4a260ca9` and the corpus at `b64919cd`. The Readiness entry still reads "Appendix A additions (OD-15): blocked: their axiom reports and registration independently checked", an edit that will not be made (c.6658287702 items 1 and 4) | Yes, both still in the body | #941 | open | needs work | one §A.45 maintenance edit at closure: the Objects line records the landed and rewritten text, and the Readiness entry describes OD-15 as an evidence confirmation, matching its Unit 5 outcome | approve the administrative edit, including the Readiness wording; ruled: item 18 (c.6677500012) | 6 |
| REPORT | G4; c.6657705110 Group 4 | PLAN.md step 12 `REPORT.md` and its criterion :203 | Waived by owner ruling, recorded in G4 | #941 | complete (waived) | (c) | none | none | — |
| PROOFS-204 | COV, Record item 1; c.6658142974 item 4 | PLAN.md :204, package-wide `proofs/` acceptance | Superseded for the historical landing (COV) | #941 | complete (superseded) | (b) | none | none | — |

## 2. R-01 – R-40 (FINDINGS (a); handoff H§1)

All R-rows target lines of the pre-rewrite Introduction (`4a260ca9`/`44236326`). The #1134 rewrite replaced that text.
For each row, "applies now" checks the substance against the current text, not the old line.

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | F:32; H§1 | Page value reported as a result; A.8 has no instance | Intro side no: L165 says the scrambling condition can never be met and A.8–A.9 establish no Page curve. Corpus side corrected (`3a73cf64`, OD-9) | #941 | superseded | (b) | cite L165 and `3a73cf64` | none | 6 |
| R-02 | F:55; H§1 | "no unconditional implication holds" is false | No: L113 says "no unconditional implication among them is asserted"; L95 states the full-support equivalence | #941 | superseded | (b) | cite L95, L113 | none | 6 |
| R-03 | F:79; H§1 | "exact probes" for floating-point work | Intro: no "exact probe" text (grep). Corpus: Main:176 reworded (`3a73cf64`); the other labels are #1029 orphan 39 (c.6658178394) | #941 (Intro) / #1029 (corpus) | superseded | (b) Intro; corpus (d) already recorded | cite the grep and `3a73cf64` | none | 6 |
| R-04 | F:101; H§1 | "minimal model … six hidden states" | No: the model moved to Main §2.4 (#1134 body); "minimal" and "six" absent | #941 | superseded | (b) | none | none | 6 |
| R-05 | F:125 | §6.1/§6.4 scope qualifiers dropped | No: L149 "over any finite stretch of time"; L119 "on a finite system" | #941 | superseded | (b) | none | none | 6 |
| R-06 | F:147; H§1 | Substratum-sourcing results unreported | Substantially no: L129 (see OD-2) | #941 | duplicate-of OD-2 | as OD-2 | as OD-2 | as OD-2 | 3 |
| R-07 | F:192; H§1 | ε-realization text | Intro: no text; L174 lists one-substratum approximation as open, consistent with F-19 | #945 (c.6657440520) | transferred | (d) already recorded | none | none | — |
| R-08 | F:220 | independent-prior realization for every law | No: L63 cites the Theorem "and its Extension" | #941 | superseded | (b) | none | none | 6 |
| R-09 | F:242 | open problem (3) exact gluing | No: L174 "recurrent multi-time patterns"; the census family "rooted classification" is `current` with the Main anchor "exact all-time gluing for recurrent families of multi-time laws" | #941 | superseded | (b) | none | none | 6 |
| R-10 | F:261 | kinematics and infinite-dimensional items missing | No: L119 "assumed, not derived from OI, and a derivation of it is open [GR §3.3]"; L171; CON-15 on `main` (`6e219231`) | #941 | superseded | (b) | none | none | 6 |
| R-11 | F:299 | where the proofs are | No: "Where the details are", L181–L185 | #941 | superseded | (b) | none | none | 6 |
| R-12 | F:318 | Theorem 3's source | No: L93 cites Main §2.3 Theorem (overlap and return); the census family "recurrence horizon" is `current` | #941 | superseded | (b) | none | none | 6 |
| R-13 | F:336 | routed-readback declaration | No: the Introduction cites no declaration | #941 | superseded | (b) | none | none | 6 |
| R-14 | F:354; H§1 | [Pag93] for the information problem | No: L161 cites [Pag93b] (PRL 71, 3743), added from owner-authorized first-hand arXiv reads (#918 c.6643090231, E11–E14) | #941 | open | (b) | cite c.6643090231 | none | 3 |
| R-15 | F:368; H§1 | Doukas attribution overstates Dou26 Prop. 1 | **Yes (regression).** The landed text (`f5efa7a0`:172) had "Doukas states the contraction argument concurrently, as a no-revival obstruction to Markovian realizers". L93 now says "Doukas states the same argument concurrently [Dou26, Prop. 1]", directly after the overlap-and-return argument. That is the very wording #918 round finding rF-10 corrected | #941 | open | needs work → (a) | restore the landed wording at L93 exactly (+7 words; it is also the round's rF-10 fix), with `.tex`/`.pdf` rebuilt | authorize one Introduction edit; ruled: item 4 (c.6677500012) | 3 |
| R-16 | F:387 | RHP14/BD16 directions and locators | Substantially no: L93 "uses the standard contraction criterion" claims no iff. The BD16 locator ("Prop. 1 and Cor. 1"), present at `f5efa7a0`, was dropped | #941 | open | (b), or (a) optional | (b) as worded; optionally restore "[BD16, Prop. 1 and Cor. 1]" in the same edit as R-15 | choose (b) or the locator; ruled: item 5 (c.6677500012) | 3 |
| R-17 | F:402 | Mon08 cited for explicit tasks | No: L133 cites "[HKLP24, Thm 4; GH03]" for unboundedness, with Mon08 only for reporting Hardy's result | #941 | open | (b) | none | none | 3 |
| R-18 | F:415; H§1 | Barandes/Schmidt dilation coincidence | No: the sentence and [Sch21] are gone (grep); the dilation moved to Main §3.1 (claim map I-20) | #941 | open | (b) | none (closes orphan 36 too) | none | 3 |
| R-19 | F:428 | [Sha79] unread | No: D5 (#918 c.6650823924) approved the agent's documented first-hand read; plan review c.6650329205 :19 | #941 | superseded | (b) | cite D5 (an agent read, not owner verification) | none | 3 |
| R-20 (prior leg) | F:443 | BHa endpoint sentence lacks its message prior | **Partly (regression).** Applied at `f5efa7a0`:302–304 (message "drawn uniformly"). L163 states the floor with no prior. See X-2 | #941 | duplicate-of X-2 | as X-2 | see X-2 | see X-2 | 4 |
| R-20b (population and sufficiency legs) | F:443 | BHa sentence: which population the counts cover, and "sufficient for what" | No: the counts moved to [BHa] (owner Q6, #1134 body), and L163 states sufficiency and non-necessity ("Reversibility does not guarantee recovery … Nor is reversibility necessary for recovery") | #941 | superseded | (b) | none | none | 6 |
| R-21 | F:460 | what the §5 results are | No: L163 "Unpublished finite-model research … none is derived from the substratum's dynamics"; L185 | #941 | superseded | (b) | none | none | 6 |
| R-22 | F:480 | I* undefined, no locator | No: L83 defines I with [Main §3.4, Theorem (C3 necessity)] | #941 | superseded | (b) | none | none | 6 |
| R-23 | F:493 | (C4) time index and positive probability | No: L85 states (C4) informally, with no M_t equivalence claimed | #941 | superseded | (b) | none | none | 6 |
| R-24 | F:506 | "deterministic completion" undefined | No: the phrase is absent; "completion" occurs only at L119, L139 (theorem name), L157 | #941 | superseded | (b) | none | none | 6 |
| R-25 | F:523 | "(each with one step not machine-checked)" | No: no machine-check claim in the text (grep "machine": 0) | #941 | superseded | (b) | none | none | 6 |
| R-26 | F:539 | (C2) necessity is conditional | No: L174 states the mixing assumption | #941 | superseded | (b) | none | none | 6 |
| R-27 | F:557 | which steps lack a machine check | No: no such list; L183 points to the formal papers | #941 | superseded | (b) | none | none | 6 |
| R-28 | F:570 | §3.3 heading | No: the heading is now "Recurrence…"; non-selection is in §4.1 L109 | #941 | superseded | (b) | none | none | 6 |
| R-29 | F:583 | "Level G3" labels | No: "G3" absent | #941 | superseded | (b) | none | none | 6 |
| R-30 | F:602; H§3 item 5 | "send it to different futures" read universally | Intro no: L30 "can differ … and so lead". Corpus Main:105 → #1028 (c.6657426485) | #941 / #1028 | superseded / transferred | (b) Intro; (d) corpus, recorded | none | none | 6 |
| R-31 | F:615 | "What the paper states are …" | No: sentence absent | #941 | superseded | (b) | none | none | 6 |
| R-32 | F:626 | card arrangement violates no Bell inequality | No: L139 states the card version with its conditions | #941 | superseded | (b) | none | none | 6 |
| R-33 | F:642 | "fixed-dimension form is false" | No: absent | #941 | superseded | (b) | none | none | 6 |
| R-34 | F:282 | "stop short of operational QM" omits ε-reach | Superseded by F-19 (c.6649268823: keep the exact regime); L12 and L24 state representation, not derivation | #941 → #945 | duplicate-of R-07/OD-3 | (d) already recorded | none | none | — |
| R-35 | F:660; H§1 | BHa counts and bound need conditions (S9-D5, S9-A2) | Counts: no (numbers moved to [BHa], owner Q6; see S9-D5). Bound: see X-2 | #941 | duplicate-of X-2 (bound) | as X-2 | see X-2 | see X-2 | 4 |
| R-36 | F:672 | positive-probability histories; source of (C3) | No: L76; L83 gives the capacity bound separately | #941 | superseded | (b) | none | none | 6 |
| R-37 | F:692 | rooted maps; what is specific to readback | No: L91, L95, L97 | #941 | superseded | (b) | none | none | 6 |
| R-38 | F:714; H§1 | Pinsker convention and hypotheses | Intro no: the Pinsker floor moved to Main (#1134 body). Corpus: #1028 orphan 44 (c.6658178394) | #941 / #1028 | superseded / transferred | (b) Intro; (d) recorded | none | none | 6 |
| R-39 | F:722 | Bell sentence's hypotheses | No: L139 lists all five, and L141 the branch OI takes | #941 | superseded | (b) | none | none | 6 |
| R-40 | F:730; H§1 | ε text on the exact regime only | As R-07 | #945 | duplicate-of R-07 | (d) recorded | none | none | — |

## 3. OD-1 – OD-15 (FINDINGS (c); H§2)

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| OD-1 | F:826; T3 3.9 | Main's title overclaims | No: Main:2 is "Finite-Observer Representations and Quantum Reconstruction" (#1130, `d9f0a845`); Intro L193 cites it | #1028 (c.6658060093) | transferred; corpus done | (d) recorded | none for #941 | none | — |
| OD-2 | F:832 | report the substratum-sourcing results | As R-06 | #941 | open | (b) | as R-06 | owner confirms (b) (decision 3); ruled: item 3 (c.6677500012) | 3 |
| OD-3 | F:838 | ε-realization addition | As R-07 | #945 | transferred | (d) recorded | none | none | — |
| OD-4 | F:842 | kernel-only results stated only in the Introduction; Introduction not a census manuscript | Intro side no: the text cites no Lean declaration. OD-4's families (recurrence horizon; physical C4 discharge and round 2, PhysicalC4Discharge/StorageReadback; rooted classification) are `current` with Main anchors (census). The four #1118 families (#1134 F-1–F-4: TrajectoryMemory, FullFutureMemory, RecordFibreIdentification, RootedRecurrenceBridge) are `kernel-only` and are not cited by the text. Census registration of the Introduction stays with #1118 under D10 | #941 / #1118 | open | (b) Intro; (d) census registration, recorded under D10 | none | none | 6 |
| OD-5 | F:858 | which routed-readback declaration | Moot: no declaration cited | #941 | superseded | (b) | none | none | 6 |
| OD-6 | F:863 | do not name the Characterization theorem | Satisfied: not named (L119's "characterization" is GR's operational-completion theorem) | #941 | complete | (b) | none | none | 6 |
| OD-7 | F:868 | exact-probe convention | As R-03 | #941 / #1029 | superseded | (b) / (d) | none | none | 6 |
| OD-8 | F:873; c.6561386879 | first-hand reads: Pag93, Sha79, CT06, Har04 (+Sch21) | Pag93b: read (c.6643090231). Sha79: D5. CT06: replaced by PW25 (D6), and since dropped (grep). Sch21: not cited. Har04: L133 "Montina reports Hardy's result [Mon08; Har04]"; the round lists a read (c.6643385201), but the landing gate marked it "not checked" (c.6649656506) | #941 | open | (b) | record (b): Har04's use is attributed through Montina, as OD-8 itself allows ("cited only as reported in [Mon08]") | confirm Har04 (b), or require a first-hand read; ruled: item 8 (c.6677500012) | 3 |
| OD-9 | F:878 | restate GR A.8 | Done on `main` (`3a73cf64`, D-8; H§2) | #941 | complete | (a) | none | none | 6 |
| OD-10 | F:887 | no minimality claim | Satisfied (R-04) | #941 | complete | (b) | none | none | 6 |
| OD-11 | F:891 | no established discriminating experiment | Satisfied: L24, L173 | #941 | complete | (b) | none | none | 6 |
| OD-12 | F:896 | leave out OI⁺; O-1 only if budget allows | OI⁺ absent; O-1 as below | #941 | complete (OI⁺) | (b) | none | none | 6 |
| OD-13 | F:899 | length budget | Superseded by F-26 (c.6649268823) and the #1134 rewrite (15 pages) | #941 | superseded | (b) | none | none | 6 |
| OD-14 | F:918 | CON-15 kinematics clause | Done on `main` (`6e219231`); L119 cites it | #941 | complete | (a) | none | none | 6 |
| OD-15 | F:922; G1 §1; c.6658287702 | axiom reports and census check for `PhaseSource` and `PhysicalC4StorageReadback` (Appendix A edit abandoned, ruling c.6658142974 item 6) | Edit moot: no Appendix A. Evidence: all three declarations have `#print axioms` in source (PhaseSource:203–204; PhysicalC4StorageReadback:709); both modules are imported by `OIBridge.lean` (:190, :254); release-gate step `lean-axioms` (`tools/release_gate.py`:148, `tools/lean_axiom_check.py`) fails on any non-standard axiom or missing report on every gated build. Both census families are `current`, with GR/Main anchors. The formal papers name the three declarations at GR:260 (`permClass_onesFixing`, `onesFixing_not_phasesAvailable`) and Main:147 (`routedAtStorage_forces_indivisible_somewhere`) | #941 | open | (b) | Unit 5: a reviewer confirms from `main` (recipe: `tools/lean_axiom_check.py` at a named `main` commit; expected pass; census step `lean-manuscript`) and records that the destination is the formal papers (GR §3.3, Main §2.3), not the Introduction | accept the release-gate checks as the "independently checked" axiom evidence, or require a separate reviewer re-run; ruled: item 11 (c.6677500012) | 5 |

## 4. Optional items O-1 – O-26 (FINDINGS (b); H§6; G1 §4)

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| O-1 | F:781 | coherent completions unique up to unitary/antiunitary | Not in text; GR §3.3 carries it | #941 | open | (c) | waive: the rewrite is a non-specialist guide with no theorem statements (owner Q1/Q2, #1134 body) | adopt or waive; ruled: item 6 (c.6677500012) | 3 |
| O-2 | F:782 | one-time freedom classified | L109 states the non-selection; the classification detail is in Main | #941 | open | (c) | waive, same reason | adopt or waive; ruled: item 6 (c.6677500012) | 3 |
| O-3 | F:783 | 0.031-bit measurement-dependence cost; PR-box | Not in text | #941 | open | (c) | waive | adopt or waive; ruled: item 6 (c.6677500012) | 3 |
| O-4 | F:784 | open problem (2) over the canonical quotient | Moot: open problem (2) was answered (Track C I-9) and L83 states the variational result | #941 | open | (b) | superseded by I-9 | none | 3 |
| O-5 | F:785 | canonical-measure "(machine-checked)" plus an Appendix A row | Moot: no Appendix A, no machine-check tags | #941 | superseded | (b) | none | none | 6 |
| O-6 | F:786 | rooted periodicity clause | Moot (R-09) | #941 | superseded | (b) | none | none | 6 |
| O-7 | F:787 | BHb C2 bound | Folded into R-01 | #941 | duplicate-of R-01 | (b) | none | none | 6 |
| O-8 | F:788 | Characterization sentence | = OD-6 | #941 | duplicate-of OD-6 | (b) | none | none | 6 |
| O-9 | F:789 | (iii)–(v) as OI⁺ | Not recommended; absent | #941 | complete | (b) | none | none | 6 |
| O-10 | F:790 | pointer to [SM] with H-link | L141 cites [SM] only for the cubic lattice and makes no SM-derivation claim, so H-link is not engaged | #941 | open | (c) | waive the SM-results pointer as outside scope | adopt or waive; ruled: item 6 (c.6677500012) | 3 |
| O-11 | F:791 | ROADMAP-only items | = OD-14 | #941 | duplicate-of OD-14 | (b) | none | none | 6 |
| O-12 | F:792 | abstract ε clause | = R-07 | #945 | duplicate-of R-07 | (d) recorded | none | none | — |
| O-13 | F:793 | advantage monotone under accumulation (BHa D1–D2) | Not in text; numbers moved to [BHa] (owner Q6) | #941 | open | (c) | waive | adopt or waive; ruled: item 6 (c.6677500012) | 3 |
| O-14 | F:794 | `continuous_extension_not_unique` | Not in text; no Lean identifiers by design (Q3) | #941 | open | (c) | waive | adopt or waive; ruled: item 6 (c.6677500012) | 3 |
| O-15 | F:795 | Bohr-frequency completeness | "Leave out"; absent | #941 | complete | (b) | none | none | 6 |
| O-16 | F:796 | CMP-13/15/16/19/20/21 | "Leave out"; absent | #941 | complete | (b) | none | none | 6 |
| O-17 | F:797; G1 §4 | "not adopted" on [BHa]/[BHb] | Superseded by D8; L203/L205 keep D8's descriptions | #941 | complete (supersession recorded in G1) | (b) | Unit 2 reviewer confirms G1 §4 against L203/L205 | none | 2 |
| O-18 | F:798 | \|C_V\|≥2 | No change | #941 | complete | (b) | none | none | 6 |
| O-19 | F:799 | H-Bell clauses | No change; L141 cites Substratum §3.2 | #941 | complete | (b) | none | none | 6 |
| O-20 | F:800 | Theorem 4 directions | No change; L119 | #941 | complete | (b) | none | none | 6 |
| O-21 | F:801 | label collisions | = CON-37 → #1029 (T3 3.5) | #1029 | transferred | (d) recorded | none | none | — |
| O-22 | F:802 | `levelOne_eq` | Moot | #941 | complete | (b) | none | none | 6 |
| O-23 | F:803; G1 §4 | recipe needs a clone holding the package | Discharged (G1 §4); the rewrite has no recipe | #941 | complete (discharge recorded) | (b) | Unit 2 reviewer confirms | none | 2 |
| O-24 | F:804 | define n | Folded into R-18 | #941 | duplicate-of R-18 | (b) | none | none | 6 |
| O-25 | F:805 | cuts C-1–C-8 | Superseded (OD-13) | #941 | superseded | (b) | none | none | 6 |
| O-26 | F:806; G1 §4; c.6657705110 Group 1 item 4 | cite version DOI 23608753 (release 3.1.4) beside the concept DOI | The ruling keeps it "until the relevant publication or archive identifier is verified". #942 c.6434035598 records that the concept DOI `10.5281/zenodo.19060318`, which L191 cites, resolves through doi.org to Zenodo record 23608753, the repository's own deposit. G1's "not resolved externally" referred only to that session. The current text cites only the concept DOI and has no version-specific reproduction claim | #941 | open | (b) | (b): the relevant identifier for the current text is the concept DOI, already verified (c.6434035598); plus one read-only re-resolution of it in Unit 3, since its target moves with each release | accept (b). A waiver (c) would vary c.6657705110 Group 1 item 4 and must be stated as a variation; ruled: item 7 (c.6677500012) | 3 |

## 5. Branch-only Introduction items: FA slice 2 §D and Track C (H§1)

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| D1 | slice2 :46; H§1 | abstract SC-3 wording | Satisfied: L12; L95 full-support equivalence | #941 | superseded | (b) | none | none | 6 |
| D2 | slice2 :47 | SC-2 rational class and Extension | Satisfied: L63 | #941 | superseded | (b) | none | none | 6 |
| D3 | slice2 :48 | C2-structural vs C2-slow | Satisfied: L85 states no C2-slow necessity; L174 | #941 | superseded | (b) | none | none | 6 |
| D4-FA | slice2 :49 | any non-permutation rooted map | Satisfied: L95, L97 | #941 | superseded | (b) | none | none | 6 |
| D5-FA | slice2 :50 | slow-bath form conditional | Satisfied: L174 | #941 | superseded | (b) | none | none | 6 |
| D6-FA | slice2 :51 | Bell hypotheses | Satisfied: L139, L141 | #941 | superseded | (b) | none | none | 6 |
| D7-FA | slice2 :52 | no change needed | — | #941 | complete | (b) | none | none | — |
| I-1 | Track C REPORT :191 | Extension label; probe | Satisfied: L63; no probe claim | #941 | superseded | (b) | none | none | 6 |
| I-2 | :195 | machine-check phrase | Moot | #941 | superseded | (b) | none | none | 6 |
| I-3 | :196 | positive-probability posteriors | Satisfied: L76 | #941 | superseded | (b) | none | none | 6 |
| I-4 | :197 | (C1)/(C3)/(C2) sources | Satisfied: L83, L85 | #941 | superseded | (b) | none | none | 6 |
| I-5 | :201 | abstract recurrence clause | Satisfied: L12 | #941 | superseded | (b) | none | none | 6 |
| I-6 | :202 | rows for every root | Satisfied: L91 | #941 | superseded | (b) | none | none | 6 |
| I-7 | :203 | shared prior | Satisfied: L91 | #941 | superseded | (b) | none | none | 6 |
| I-8 | :204 | full-support equivalence; non-deterministic step | Satisfied: L95, L97 | #941 | superseded | (b) | none | none | 6 |
| I-9 | :205 | open problem (2) answered | Satisfied: L83 | #941 | superseded | (b) | none | none | 6 |
| I-10 | :206 | readout-relevant memory iff | Satisfied: L79 | #941 | superseded | (b) | none | none | 6 |
| I-11 | :210–:211 | Bell either/or and hypotheses | Satisfied: L139, L141 | #941 | superseded | (b) | none | none | 6 |
| I-12 | :215 | ε text | As R-07 | #945 | duplicate-of R-07 | (d) recorded | none | none | — |

## 6. Step-9 findings (proofs/README.md at `16fc745d`, rows 30–77; COV)

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| S9-I2 (step-10 leg) | proofs/README :57; G4; COV | hidden memory of the past is forced by reversibility; readout-relevant memory is the witness re-described; (C3) holds unconditionally | Satisfied in the current text: L81 "A reversible world run from the start stores its whole visible past, even when the record has no memory at all; memory is the part of that store that changes what is seen next"; L79; L83 states the capacity bound independently of (C4) | #941 | open | (b) | a sourced no-change disposition, independently reviewed (ruling c.6658142974 item 4) | accept (b) after review; ruled: item 10 (c.6677500012) | 4 |
| S9-I7 (step-10 leg) | :62; G4; COV | "time-invariant" only through a hidden clock; (C4) met by a ledger; t ≪ t_R uncontrolled | Satisfied: L63 names the clock ("together with a clock"); "time-invariant" absent; L97 states that the recurrence window exceeds observable stretches; the corpus leg is in SC-2 (`9020bfa0`) | #941 | open | (b) | as above | accept (b) after review; ruled: item 10 (c.6677500012) | 4 |
| S9-I8 | :63; G4; COV | C1–C3 not OI-specific; C1's K=∅ never holds for an OI observer; 1/\|K\| classical, quantum analogue 1/d² | L163 frames the results as finite register toy models, "as in perfect secret sharing" (classical), and claims nothing about OI specificity or the quantum case. "Reading everything" there is a property of the model. No review has accepted S9-I8's interpretive claim, so adding it to the text would assert an unanchored claim | #941 | open | (b) | a sourced no-change disposition, independently reviewed in Unit 4 | accept (b) after review; ruled: item 10 (c.6677500012) | 4 |
| S9-M1, M2, A9, D4 | :30–31, :50, :72 | ε-realization at finite precision | Corpus SC-1 (`024a2126`); the finite-b repair is open | #945 | transferred | (d) recorded: #945 opened at the owner's request (2026-10-27, #945 body); owner decision 7 (#945 c.6561386277) | none | none | — |
| S9-I5 | :60 | ε interpretive overreach | #941 leg done: SC-1 (`024a2126`) narrowed the Kochen–Specker and ontology readings. #944 C5 is an input to that audit; **no owner transfer approval is recorded** | #941 | complete (#941 leg) | (a) | record the #944 input as input to an independent audit, not a transfer | accept the reclassification, or approve a transfer; ruled: item 16 (c.6677500012) | 6 |
| S9-M3, A6, D8 | :32, :47, :76 | independent-prior proof | SC-2 (`9020bfa0`) | — | complete | (a) | none | none | — |
| S9-M4, A4, A5, D7 | :33, :45–46, :75 | Theorem 2 and its Corollary | SC-3 (`6bc2c4af`, `a5168789`) | — | complete | (a) | none | none | — |
| S9-A1, D6 | :42, :74 | recurrence hypotheses | SC-3 | — | complete | (a) | none | none | — |
| S9-I1 | :56 | readback framing; indivisibility generic | #941 leg done: Intro side satisfied (L95, L97); corpus SC-3. #944 C1 is an input; **no owner transfer approval is recorded** | #941 | complete (#941 leg) | (b) | as S9-I5 | accept the reclassification, or approve a transfer; ruled: item 16 (c.6677500012) | 6 |
| S9-A8, D2 | :49, :70 | Bell hypotheses and "Certified" | SC-4 (`0585dd0d`) | — | complete | (a) | none | none | — |
| S9-I3 | :58 | cone speed vs c; (iv) posited | #941 leg done: SC-4 (`0585dd0d`); L141 states setting independence as an assumption. #944 C3 is an input; **no owner transfer approval is recorded** | #941 | complete (#941 leg) | (a) | as S9-I5 | accept the reclassification, or approve a transfer; ruled: item 16 (c.6677500012) | 6 |
| S9-A3 | :44 | Pinsker p₀, δ, TV convention | #1028 orphan 44 | #1028 | transferred | (d) recorded | none | none | — |
| S9-D1 | :69 | "certified exactly" at Main:176 | Reworded by #1019 (`3a73cf64`). #1029 c.6658171112 §3 records this as "a fact about the text, not a review verdict on the new wording" | #1029 orphan 39 | complete (corrected; verification pending) | (b) | Unit 6 reviewer confirms the Main:176 wording | none | 6 |
| S9-I4 | :59 | "backflow" senses | #941 leg done: SC-16 (`55e3217b`); the Introduction does not use "backflow" (grep). #944 C4 is an input; **no owner transfer approval is recorded** | #941 | complete (#941 leg) | (a) | as S9-I5 | accept the reclassification, or approve a transfer; ruled: item 16 (c.6677500012) | 6 |
| S9-A7, I6 | :48, :61 | CP-indivisibility hypotheses; "exact conditions" | #1028 (c.6657426485) | #1028 | transferred | (d) recorded | none | none | — |
| S9-D3 | :71 | "Certified exactly t=1..6" | #1029 orphan 39 | #1029 | transferred | (d) recorded | none | none | — |
| S9-M7 | :36 | three-notions implication | R-02 | #941 | complete | (b) | none | none | 6 |
| S9-M5, M6, A2 (record side) | :34, :35, :43 | BH-01 record errors | T3 3.1 → #1028 (c.6658037322) | #1028 | transferred | (d) recorded | none | none | — |
| S9-A2 (Intro side) | :43 | conditions on the BHa bound in the Introduction | See X-2 | #941 | duplicate-of X-2 | as X-2 | see X-2 | see X-2 | 4 |
| S9-D5 | :73 | the 1,376 count needs its record convention ("applied at every step with records accumulated") | No: the count is no longer in the Introduction (owner Q6; #1134 body). It stays in [BHa] | #941 | superseded | (b) | none | none | 6 |
| S9-D9 | :77 | matrix line citations | Audit-internal; the matrix is superseded (provenance only) | #941 | superseded | (b) | none | none | 6 |

## 7. SC and reference-trace items

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| SC17-68 | CR §2; `tracks/SC17-explainer-bell/README.md`:68 | side check states what the draft Introduction at `bace5ef8` says: support off `main` | Yes: the sentence is unchanged on `main`; blob `7c5f18b4` is not on `main` (CR §2) | #941 | open | needs work → (a) | narrow the sentence to provenance: "A side check of the then-draft Introduction (#918, `bace5ef8`, not on `main`) is recorded as provenance only; no claim of this record rests on it" | choose narrowing (recommended) or landing the blob; authorize a mutable-record edit; ruled: item 1 (c.6677500012) | 2 |
| SC31-140 | CR §2; `SC31-period-growth/README.md`:140 | as above, draft `72014a79` | Yes | #941 | open | needs work → (a) | as above | as above; ruled: item 1 (c.6677500012) | 2 |
| SC33-111 | CR §2; `SC33-bell-main-book/README.md`:111 | as above, draft `3e600003` | Yes | #941 | open | needs work → (a) | as above | as above; ruled: item 1 (c.6677500012) | 2 |
| SC42 | CR §2; SC42 README :13, :15 | draft-file references | Provenance: the track reads the kernel itself (CR §2) | — | complete | (b) | none | none | — |
| CC-10 | CR §2; `corpus-consistency-20261026/README.md`:10 | draft `AUDIT.md` reference | Provenance (CR §2) | — | complete | (b) | none | none | — |
| M6 | CR §3 | observer-relative-finiteness M6 uses draft text | A pointer to #1015's existing home (CR §3, under #1031 c.6666613671 item A), never a #941 obligation | #1015 | not #941 (pointer) | — | none | none | — |
| README-28 | G1 §3; c.6665390344 §3 | `papers/introduction_repro/README.md` says "28 baseline declarations" (:4) and "The 28 declarations of Appendix A" (:68) but omits `c3_necessity_via_hidden`, which `f5efa7a0`:356 lists | Yes: 28 table rows, 0 hits for `via_hidden`; root `README.md`:117 also says 28. The count of 29 was confirmed independently (Unit 1 review, finding 3; #941 c.6677061224), and is checkable from `main`: Appendix A at `f5efa7a0`, less its four additional-module bullets, names 29 declarations | #941 | open | needs work → (a) | add the missing row (its report is in the JSON, per G1 §3) and change the count to 29 at three sites (§A.25): `papers/introduction_repro/README.md`:4 and :68, and root `README.md`:117 ("for the 28 baseline declarations"). "28-module" (EXPECTED_28) counts modules and is not touched. The JSON is untouched | authorize the README edit and a separate merge; ruled: item 2 (c.6677500012) | 2 |
| SC-41 / NEW-2 | c.6558736061 §2.4; #1134 F-5 | Pauli-twirl citation split | Moot: the twirl remark is omitted; #972 closed | — | complete | (b) | none | none | — |
| SC-36 | c.6665390344 §3 | SC36 open items | Routed to #970 | #970 | transferred | (d) recorded: D1–D12 (#918 c.6650823924, "Add the unresolved SC36 items to #970"), recorded at #970 c.6650851636 | none | none | — |
| SC-43–45 | c.6558736061 §3, "not re-checked" | Introduction's citations of Substratum §24 | Checked now: L36 [Substratum, Theorem 24(iii)] matches Substratum:257 ("Finite decoupled ancillary enlargement … prepared independently"); L38 Prop. 24.5 matches Substratum:348. The corpus SC-44/45 work is #979 (open) | #941 (the corpus SC-44/45 work is on #979; not a transfer) | open | (b) | record the check | none | 6 |
| SC-6 | H§4 | CP-indivisibility hypotheses | #1028 | #1028 | transferred | (d) recorded | none | none | — |
| SC-7 | H§3 item 1 | BH-01 record | #1028 | #1028 | transferred | (d) recorded | none | none | — |
| SC-20 N3 | H§4 | τ_B reading at Main:76 | #1028 (T3 3.3) | #1028 | transferred | (d) recorded | none | none | — |
| H§3 items 2–8 | H§3 | CON-03, CON-21, CON-37, R-30 corpus, FA findings 5, 6b, 6c | T3 and c.6657440520 | #1028 / #1029 | transferred | (d) recorded | none | none | — |
| CON-04 | H§5 | GR §6 heading; other dissolution sites | No-change decision for the heading (H§5). The residue is #1028 orphan 41's PR-A row (c.6628572816), a pre-existing home, not a transfer from #941 | #1028 orphan 41 | transferred (pre-existing home) | (d) recorded | none | none | — |
| CON-10 | c.6657705110; c.6658142974 item 1 | Substratum:471 and fourth site | #1028 c.6657923668, c.6658178394 | #1028 | transferred | (d) recorded | none | none | — |
| Main:22/:176 | c.6657940473; c.6658142974 item 2 | four obligations | Recorded on #1028 c.6658178394 and on #1029 | #1028 / #1029 | transferred | (d) recorded | none | none | — |
| SC-23 | c.6558736061 §3 ("not re-checked"); CORRECTIONS-LEDGER :707 | #946 unit: fast-bath exact vanishing, one-step thermalization, and the τ claims at Main:439/:447 (now :445/:453) | Not a #941 obligation (a #946 unit; not in the handoff). Its surviving sites are #1028 orphan 35 ("Same chain, surviving #946 SC-21/SC-23"), under owner decision 5 of the 2026-11-01 disposition (#1028 body) | #1028 orphan 35 | not #941 (a #946 unit; existing home #1028 orphan 35) | — | none for #941 | none | — |
| SC-30 | c.6558736061 §3; #946 c.6441584771, c.6442678234 | #946 low-items batch (Main :20, :48/:62, :86, :109, :131, :242, :250/:246, :336, :584, :640, :716/GR:589; GR :276, :591; SM :112; Methodology :13; ch01 :123/:125, glossary :25, ch04 :36, ch05 :5; later ch01:265, ch19:248, Computation:138) | Not a #941 obligation (a #946 unit; not in the handoff). Its line numbers are at `55e3217b` (#946 c.6441584771); the FA finding IDs are in `tracks/FINAL-AUDIT/slice1-main-companions.md` and slice 2 at `16fc745d`. Re-mapped at `main` `721f35fb`: **homed:** A-5 (Main:20), D-13 (:109), D-14 (:86 + GR:20(ii)), D-21 (:48/:62), A-12 (:242–244 → :252–256), D-19 (:250 vs :246 → :252–256), D-23 (Methodology:13), ch01:123/:125 and ch04:36 → #1028 orphan 37 (its "Main:248–256 (A-12, D-19)" covers both); GR:276 → #1028 orphan 42; D-18 (:584), D-20 (:640 → :646), glossary:25 and ch05:5 → #1029 orphan 38; D-17 (Main:716/GR:589) → #1015 FA D-17; ch01:265 (now :271), ch19:248 and Computation:138, added by #946 c.6442678234 → #1029 orphan 34. **No recorded destination; the finding's quoted wording does not appear at `721f35fb`; not adjudicated under #941:** D-16 (Main:131 now "requires only bijective dynamics (Lemma 3) and a non-permutation one-step matrix $T$, under the uniform hidden prior that defines $T$"); D-22 (the frozen-bath sentence, now Main:342, says "(C2-slow)"); D-24 (SM:112 now exhibits the non-permutation one-step map and scopes the claim to the recurrence cycle, "not a statement about accessible windows"); D-25 (GR:591 now derives recurrence-cycle P-indivisibility on a finite representative; "would require decoupling the sectors entirely" is gone). | #1028 orphans 37, 42 / #1029 orphans 34, 38 / #1015 (D-17) | not #941 (a #946 unit) | — | none for #941 | owner: note that SC-30 is outside #941, and that D-16, D-22, D-24 and D-25 appear corrected on `main` and need no home (decision 15); ruled: item 15 (c.6677500012) | — |
| #1002 | c.6558736061 §3 ("Computation §4.5, deferred to #1015/#1017") | finite-S computational budget | Closed unmerged and reconciled in #1057 (merge `4759d27b`, an ancestor of `main`; owner decisions OD-1, OD-2, 2026-11-03; #1002 c.6597320954). The recovery question is recorded on #1015 (c.6597311610). #1017 is closed | #1015 (residue) | complete | (b) | none | none | 6 |
| CON-26 | F:640, :991 (PR-F; R-33's corpus side) | Main's prior-class count differs from B4's recheck | No: Main:616 now reads "sixteen distinct laws … $M_{\mathrm{det}} = M_t$ for two of them", which matches B4's 2 of 16, with an identity argument for every hidden prior | #941 (no other home located) | open | (b) | record the sourced no-change | owner accepts (b) (decision 14); ruled: item 14 (c.6677500012) | 6 |
| CON-42 | F:55 (R-02's corpus side); FINDINGS (d) PR-C | Main:340 "No unconditional implication among the three is asserted here", an underclaim (medium), since Markov ⇒ P-divisible gives one implication | Yes, the sentence is unchanged. It is true as stated (it scopes what is asserted), and Main's Remark (two notions of memory) states the Markov ⇒ P-divisible direction. The same paragraph's "the exact conditions" is S9-I6, homed on #1028 | #941 (no other home located) | open | (b), or (d) to #1028 | (b): true as stated, with the implication stated in Remark (two notions of memory), Main:628; or (d): place it beside S9-I6 on #1028, one writer for Main:340 | choose (b), or approve (d) to #1028 (decision 14); ruled: item 14 (c.6677500012) | 6 |
| CON-02 | FINDINGS (d) PR-E | book "resolved" black-hole status | No: ch07:110 "The framework does not resolve the paradox"; ch18:122 "the information paradox is not resolved"; ch19:22 "an unresolved entry", :72 "the paradox is not resolved", :334 "Not resolved". FULL:1985, :4935, :5176, :5226, :5488 mirror them. ch09 has no black-hole "resolved" site (grep) | #941 (no other home located) | open | (b) | record the sourced no-change | owner accepts (b) (decision 14); ruled: item 14 (c.6677500012) | 6 |
| D4 | c.6657440520 | Main:720–726 | #1015 c.6657431542 | #1015 | transferred | (d) recorded | none | none | — |
| D10 | #918 c.6650823924; #1118 | four kernel-only families; census registration of the Introduction | #1118 | #1118 | transferred | (d) recorded | none | none | 5 (coordination only) |

## 8. Evidence obligations

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| NEW-3 / orphan 26 / rF-15 | c.6561386879; c.6631126662 §1 | [CE]/[CR] pins `bdcbd32`, `2624d49` off `main` | No: both are ancestors of `main` (#1117, `53a3eb3d`); [CE]/[CR] are no longer cited (Q5) | #941 | complete | (a) | none | none | 6 |
| NEW-3b (other pins) | c.6558736061 §2.4 | pins `021850d9`, `a2be1e45`, `20ca05fe`, `55e3217b` in the draft text | Moot: the current Introduction cites no pins (F-17 check). `20ca05fe` and `55e3217b` are ancestors of `main` | #941 | superseded | (b) | none | none | 6 |
| #989 review | c.6631126662 §1 | companion `2624d49c` review | Homed on #970 | #970 | transferred | (d) recorded | none | none | — |
| Orphan 36 (Sch21) | c.6561386879 | read Sch21 before any use | Not cited (R-18) | #941 | open | (b) | none | none | 3 |
| EV-CI-1 | EVIDENCE.md :206; G1 §1; H§7 | fresh-build `introduction_repro` at `17b830bc` | Executed once under the #943 workflow (#942 c.6435469998, PASS; provenance only, §A.42 item 2). It supports no current claim (README :5–6) | #941 | open | (b) | record: no surviving claim needs a `main`-retained replay (§A.42 item 5) | accept (b); ruled: item 17 (c.6677500012) | 5 |
| EV-CI-2 | EVIDENCE.md :206 | extended (28-module) expected result | Retained by #1132; status is EV-28 | #941 | complete (retention) | (a) | none | none | — |
| EV-CI-3 | EVIDENCE.md :206 | BHa/BHb mutants and BHb `-O` replays | Executed once (#942 c.6435105802, PASS; provenance). BH-01's `mutants-output.json`, `checks.py` and `result.json` are on `main`; the Introduction's [BHa]/[BHb] claims are qualitative (L163–L165) | #941 | open | (b) | record: the claims rest on the records' committed recipes and outputs on `main`; re-running is optional | accept (b), or authorize one `bh-mutants` dispatch; ruled: item 17 (c.6677500012) | 5 |
| EV-L | EVIDENCE.md (E1 122, E2 20, E3 36 items; 3 failed rows); #942 c.6433846714 | step-7 evidence levels for the 409 matrix rows of `4a260ca9` | Recorded as accepted: #942 c.6433846714 records "step 7 accepted" (a diff-only re-review of `8f6ea594..2bc65ae9` returned ACCEPT, `review/EVIDENCE-RECHECK-2bc65ae9.md`, checkpoint `cb2029ce`; not on `main`, provenance). That met the evidence gate of c.6428100988. Its rows map the pre-rewrite text and are superseded for the current Introduction by #1134. The three failed rows are evidence tags (R-03/OD-7) | #941 | open | (b) | record (b), citing c.6433846714 and #1134. No new supersession ruling is needed | none | 5 |
| EV-28 | `introduction-repro-ext/README.md`:3–6; `evidence-replay.yml`:20–24 | the 28-module result is not independently verified on `main`; "The accountable Issue is #941" | Yes. §A.46 item 4 requires "a stated status, an accountable Issue and a remediation plan"; the closure criterion (d) and §A.45 rule 6 require an open home. **Hard closure blocker:** #941 cannot close while EV-28 names it | #941 | open | needs work | one of: (d) transfer accountability to an open Issue (e.g. #1029, evidence records), with the README :6 pointer edited and a separately approved comment-only edit of workflow :24 (trigger check under §A.43 item 4); (a) an independent review on `main` re-deriving the 14 added entries; or a §A.46 item 6 disposition | choose the route (decide before Unit 6); ruled: item 12 (c.6677500012) | 5 |
| EV-14 | `papers/introduction_repro/README.md`:9; `evidence-replay.yml`:7 | "The accountable Issue is #941" for the historical 14-module evidence | Yes, as a pointer. The result supports no current claim (README :5–6), and the release gate's `lean-axioms` step re-checks the current sources. Not a blocker unless a verification obligation is kept | #941 | open | (b) plus a pointer correction | record (b) (no verification obligation kept); correct the stale pointer under §A.27/§A.30 in the same edit as EV-28's route (README :9; workflow :7 in the same approved comment-only change). If the owner keeps a verification obligation, it becomes a blocker like EV-28 | decide whether a verification obligation is kept; ruled: item 13 (c.6677500012) | 5 |

## 9. Re-baseline NEW-1 – NEW-6 and the #918 round F-series

**Two F-series, kept apart.**
- **The #918 round series, labelled `rF-nn` here.** It comes from the round record `44236326:verification/audits/manuscript/intro-corpus-audit-20261026/round-20261104/README.md` and the owner decisions c.6643474520 and c.6649268823. Most of its members map onto existing rows:
  - rF-01 to rF-06 are R-03, R-04, R-05, R-09, R-27 and R-28;
  - rF-08 is SC-41/NEW-2, rF-09 is orphan 36 (Sch21) and rF-10 is **R-15**;
  - rF-11, rF-12 and rF-13 are R-16, R-17 and R-14;
  - rF-15 is NEW-3/orphan 26, rF-24 is NEW-5 and rF-22 does not exist.

  Only rF-07, rF-14, rF-16 to rF-21, rF-23, rF-25 to rF-28 have rows of their own.
- **#1134's claim-map series, F-1 to F-10.** Its F-9 and F-10 are the planning-block rows in §1. Its F-1 to F-4 are the four kernel-only families (D10 → #1118), F-5 is SC-41, F-6 needs no action, F-7 is owner Q6 (the [BHa] qualitative statement) and F-8 is owner Q5 ([CE]/[CR] omitted; reviews on #970). None of F-1 to F-8 is a #941 obligation.

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| NEW-1 | c.6558736061 §2.3 | kernel-only families cited | = OD-4 / D10 | #1118 | duplicate-of OD-4 | (d) recorded | none | none | — |
| NEW-2 | §2.4 | twirl citation | = SC-41 | — | duplicate-of SC-41 | (b) | none | none | — |
| NEW-3 | §2.4 | pins off `main` | = orphan 26 | #941 | duplicate-of orphan 26 | (a) | none | none | — |
| NEW-4 | §2.1 | finite-S scope | Satisfied: L32, L34 (observer-relative finiteness; total finiteness an assumption of the models); D4 → #1015 | #941 / #1015 | complete | (b) | none | none | 6 |
| NEW-5 | §2.6 | Contributions sentence omits CE/CR | Moot: no Contributions sentence; CE/CR omitted (Q5) | #941 | superseded | (b) | none | none | 6 |
| NEW-6 | §2.6 | #918 behind `main` | Moot: #918 closed (c.6670854475) | — | complete | (b) | none | none | — |
| rF-14 | c.6643474520 | four Lean families | Omitted by the rewrite (#1134 F-1–F-4) → #1118 | #1118 | transferred | (d) recorded | none | none | — |
| rF-16 | c.6643474520 | [CR] unreviewed | Omitted; review is on #970 | #970 | transferred | (d) recorded | none | none | — |
| rF-17 | c.6643474520 | corpus pin | Moot: no pin in the text | — | complete | (b) | none | none | — |
| rF-18 | c.6643474520 | condition (iv) scope | L127, L129 stated for the qubit theory and access model | #941 | complete | (b) | none | none | 6 |
| rF-19 | c.6649268823 | ε expansion | = OD-3 | #945 | transferred | (d) recorded | none | none | — |
| rF-20 (Appendix A half) | c.6649268823 F-20 | "Defer additional Appendix A Lean entries until their axiom reports and registration are independently checked" | = OD-15 | #941 | duplicate-of OD-15 | as OD-15 | — | — | 5 |
| rF-20b (routed-readback statement) | c.6649268823 F-20 | "Preserve the reading-neutral routed-readback statement" | Superseded: the rewrite omits the routed-readback statement (grep "routed": 0) under owner Q3 (#1134 body). Main §2.3 (Main:147) carries both readings | #941 | superseded | (b) | none | none | 6 |
| rF-21 | c.6649268823 | Sha79 and CT06 | = R-19 / OD-8 | #941 | duplicate-of OD-8 | (b) | none | none | 3 |
| rF-23 | c.6649268823 | BH-01 enumeration vs unadopted conclusions | Satisfied: L163 ("Unpublished finite-model research"; maps "not derived"), L203, L205, L185 | #941 | complete | (b) | none | none | 6 |
| rF-25 | c.6649268823 F-25 | unused references ([HLW06], [PSW06] at the round) | Satisfied: all 43 reference keys ([Main] to [Wei89]) are cited in the text | #941 | complete | (b) | none | none | 6 |
| rF-26 | c.6649268823 | 25 pages accepted | No action (G1 §4) | — | complete | (b) | none | none | — |
| rF-27 | c.6649268823 | optional items kept in their homes | Rows O-1–O-26 | #941 | duplicate-of §4 | — | — | — | — |
| rF-28 | c.6643474520 | L41 provenance | Satisfied: L133 "this is an imported result"; L181 | #941 | complete | (b) | none | none | 6 |
| rF-07 | round record `44236326:…/round-20261104/README.md`:79 | H-Bell's continuum-limit clause cited to [Main §3.3]; the clause is at Substratum:133 (§3.2) | No: L141 cites "[Main §3.3; Substratum §3.2]"; Substratum:133 carries clause (iii) | #941 | complete | (b) | none | none | 6 |

## 10. Findings not in the owner's unit list (new)

| ID | Exact source | Claim / obligation | Applies now? (evidence) | Home | Status | Proposed outcome | Smallest supported resolution | Owner decision | Unit |
|---|---|---|---|---|---|---|---|---|---|
| X-1 | Intro L93 vs `f5efa7a0`:172 | R-15 regression: "the same argument" again attributes the overlap-and-return argument to Dou26 Prop. 1 | Yes | #941 (as R-15) | duplicate-of R-15 | needs work → (a) | see R-15 | authorize the edit; ruled: item 4 (c.6677500012) | 3 |
| X-2 | Intro L163 vs `f5efa7a0`:302–304; BH-01 `REPORT.md`:42–47; FINDINGS :660 | the floor sentence dropped the message-prior condition that R-35 applied | Yes: L163 states "hiding it completely requires the unread registers to have at least as many joint values as there are possible messages" with no prior. BHa's C2 states the zero-advantage form (`P_succ = 1/\|M\|`), which assumes a uniform prior. The floor $P_{\rm succ}\ge1/\|\mathcal U\|$ itself holds for every prior (FINDINGS :660, at `16fc745d`, not on `main`: provenance; to be checked in Unit 4 against BH-01 `REPORT.md` on `main`). **Unit 4 check, not a result:** whether "hiding completely", read as independence ("learn nothing"), needs no prior condition | #941 | open | (b), or (a) | (b) if the Unit 4 reviewer accepts the independence reading and finds the [BHa] attribution adequate; otherwise (a) with R-35's own wording, "for a uniformly distributed message" (about +5 words), and nothing more | choose after the Unit 4 check; authorize the edit if (a); ruled: item 9 (c.6677500012) | 4 |
| X-3 | #1118 body | #1118's premise ("The Introduction (#918) cites four Lean module families") and readiness ("blocked: #918 landing") are stale after #1134 (F-1–F-4: "nothing to relabel") | Yes, but outside #941 | #1118 | not #941 (another Issue's upkeep) | — | a §A.45 maintenance note on #1118, for its owner. It does not block #941 | #1118's owner | — |
| X-4 | EV-28, EV-14 | three files on `main` name #941 as the accountable Issue | Yes | #941 | duplicate-of EV-28 | as EV-28 | as EV-28 | as EV-28 | 5 |
| X-5 | #941 body | stale Objects/Scope lines | = ADM-B | #941 | duplicate-of ADM-B | as ADM-B | as ADM-B | as ADM-B | 6 |

***

## Count summary

Ledger rows: **190**.
- That is the 179 rows of the reviewed first draft (#941 c.6677061224), plus the 7 missing rows the review found (SC-23, SC-30, #1002, CON-26, CON-42, CON-02, rF-07), giving the review's 186;
- plus 4 rows split out so that no sub-claim is lost: R-20b, S9-D5, NEW-3b, rF-20b.
- Grouped rows (for example "S9-M3, A6, D8") count once.

| Section | Rows |
|---|---:|
| 1 Planning and retirement | 8 |
| 2 R-01–R-40 (+R-20b) | 41 |
| 3 OD-1–OD-15 | 15 |
| 4 O-1–O-26 | 26 |
| 5 FA D1–D7, Track C I-1–I-12 | 19 |
| 6 Step-9 (grouped; +S9-D5) | 21 |
| 7 SC, trace and corpus rows (+SC-23, SC-30, #1002, CON-26, CON-42, CON-02) | 25 |
| 8 Evidence (+NEW-3b) | 10 |
| 9 NEW and #918 round F-series (+rF-07, rF-20b) | 20 |
| 10 New findings | 5 |
| **Total** | **190** |

| Current status | Rows |
|---|---:|
| complete | 48 |
| superseded (includes R-30 and R-38, superseded on the Introduction side with the corpus side transferred) | 58 |
| transferred (an owner approval or pre-existing home is cited in each row) | 23 |
| duplicate-of | 21 |
| not a #941 obligation (M6, X-3, SC-23, SC-30) | 4 |
| **open, #941-accountable** | **36** |

**Changes from the review's expected count of about 40.**
- The four #944 legs (S9-I1, I3, I4, I5) are reclassified as complete on their #941 legs. Each has an owner decision attached: accept the reclassification, or approve a transfer.
- SC-23 and SC-30 are #946 units and are not #941 obligations. SC-23's home is #1028 orphan 35. SC-30 was re-mapped at `721f35fb`: every sub-item is homed (#1028 orphans 37 and 42, #1029 orphans 34 and 38, #1015 D-17) except D-16, D-22, D-24 and D-25, which have no recorded destination and are not adjudicated under #941.
- #1002 is complete (#1057).

**The 36 open rows by proposed outcome**
- **(b), sourced no-change awaiting review (22):** R-14, R-16, R-17, R-18, OD-2, OD-4, OD-8, OD-15, O-4, O-26, S9-I2, S9-I7, S9-I8, SC-43–45, CON-26, CON-42, CON-02, orphan 36, EV-CI-1, EV-CI-3, EV-L, EV-14 (with a pointer correction).
- **(c), waiver proposed (6):** O-1, O-2, O-3, O-10, O-13, O-14.
- **Needs work or an owner choice (8):** ADM-B, R-15, SC17-68, SC31-140, SC33-111, README-28, EV-28, X-2.
- **Hard closure blocker (1, within the 8):** EV-28 (§A.46 item 4; §A.45 rule 6; closure criterion (d)).

**Baseline for Unit 6.** N_unaccounted = 36 now. Rows awaiting only Unit 6 confirmation count as accounted.

**Distinct edits once duplicates are merged: 5 changes.**
1. **One Introduction edit:** R-15 (+7 words), optionally R-16's locator, and X-2 if (a).
2. **Three mutable-record narrowings:** SC17, SC31 and SC33, in one PR.
3. **One count correction:** README-28, at three sites.
4. **One accountability change** for EV-28, if (d), together with EV-14's pointer correction. It touches two READMEs and one comment-only workflow edit.
5. **One body maintenance edit:** ADM-B (the Objects line and the Readiness entry).

Two confirmation records come with no edit: OD-15, and the bundle of (b) records (EV-L, EV-CI-1, EV-CI-3, CON-26, CON-02, and others).

## Duplicates found

- **ε-realization:** R-07 = R-40 = R-34 = O-12 = OD-3 = rF-19 = I-12 → #945.
- **Exact-probe tag:** R-03 = OD-7 = rF-01 = E2-10/E2-11 = CON-25 = S9-D1, with the corpus side on #1029 orphan 39.
- **Kernel-only and census:** OD-4 = NEW-1 = D10 = rF-14 = #1134 F-1–F-4 → #1118. The PR-G parts are done on `main`: R-09 = rF-04 = O-6 = CON-28; R-12 = CON-41; R-13 = OD-5 = CON-43.
- **First-hand reads:** OD-8 ⊇ R-14 = rF-13 and R-19 = rF-21 (Sha79). R-18 (Sch21) = orphan 36 = rF-09. CT06 → PW25 (D6).
- **Doukas:** R-15 = rF-10 = X-1. The rewrite reintroduced rF-10's exact pre-correction wording.
- **Other attributions:** R-16 = rF-11; R-17 = rF-12.
- **Pinsker:** R-38 = S9-A3 = #1028 orphan 44.
- **BH floor:** R-20 (prior leg) = R-35 (bound) = S9-A2 (Introduction side) = X-2. R-20b and S9-D5 are separate supersessions.
- **Recurrence and readback:** R-37 = S9-A1/I1/D6 = D1 = D4-FA = I-5–I-8.
- **Bell:** R-39 = S9-A8/I3 = D6-FA = I-11.
- **Independent prior:** R-08 = D2 = I-1 = CON-20.
- **C2:** R-26 = D5-FA, and D3 = SC-20.
- **Kinematics:** R-10 = OD-14 = CON-15 = O-11.
- **Substratum sourcing:** R-06 = OD-2.
- **Minimality:** R-04 = rF-02 = OD-10 = CON-24.
- **Machine-check phrasing:** R-24 ⊂ I-10; R-25 ⊂ R-36 (L12) ⊂ I-2.
- **Other text items:** R-05 = rF-03; R-27 = rF-05; R-28 = rF-06.
- **Page curve:** OD-9 = CON-01 = R-01 (corpus side); O-7 ⊂ R-01.
- **OD-15:** OD-15 = rF-20 (Appendix A half) = E3-14 = EV-CI-2. rF-20b, the routed-readback half, is a separate supersession.
- **Pins:** NEW-3 = orphan 26 = rF-15. NEW-3b, the other pins, is separate.
- **Twirl:** NEW-2 = SC-41 = rF-08 = #1134 F-5.
- **Contributions sentence:** NEW-5 = rF-24.
- **Finite-S:** NEW-4 = D4 (#1015).
- **Main's title:** OD-1 = CON-16 = T3 3.9.
- **Folded optional items:** O-8 = OD-6; O-21 = CON-37; O-24 ⊂ R-18; O-25 ⊂ OD-13; O-4 superseded by I-9.
- **Accountability:** EV-28 and EV-14 share one edit (X-4); ADM-B = X-5.
- **Main:340:** CON-42 and S9-I6 sit on the same paragraph, so one writer should hold it if (d).

## Findings the owner's unit list missed

1. **R-15 (rF-10) came back in the rewrite.** L93 reads "the same argument", rF-10's pre-correction wording, which entered with #1134's first head and is absent from its fidelity review. It is a text regression, not a literature item.
2. **X-2: the BH floor's message-prior condition is missing at L163.** This is the Introduction side of R-20, R-35 and S9-A2. Whether it is needed under the independence reading is a Unit 4 check.
3. **EV-28 is a hard closure blocker.** EV-14 needs a pointer correction. Four lines in three files on `main` name #941 as the accountable Issue (`evidence-replay.yml`:7 and :24; `introduction-repro-ext/README.md`:6; `papers/introduction_repro/README.md`:9).
4. **Seven rows were missing from the first version.** SC-23 and SC-30 (#946 units), #1002, and CON-26, CON-42 and CON-02 (FINDINGS (d) corpus rows with no located home), and rF-07.
5. **README-28 has a third site,** root `README.md`:117.
6. **Four #944 legs (S9-I1, I3, I4, I5) carry no owner transfer approval.** They are reclassified on their #941 legs, pending the owner's choice.
7. **The ~130 (b), (c) and (d) rows in the review baseline need independent confirmation in Unit 6.** No unit in the owner's list covers them.
8. **Smaller items:**
   - SC-43–45 was not re-checked in the re-baseline; it is checked now: (b).
   - ADM-B covers the stale Objects line and the Readiness entry.
   - R-16's BD16 locator was dropped (optional).
   - SC-30's unlocated sub-items should be flagged to #1028/#1029.
9. **Not counted, for the owner:**
   - #1134 asked reviewers to confirm the `unattached` coverage-ledger record it added for the Corollary. No record carries that request to #941; give it a row only if the owner regards it as #941's.
   - X-3 (#1118's stale premise and readiness) is #1118's upkeep.

## Owner decisions requested (final list)

1. **SC17, SC31, SC33** (Unit 2): narrow each sentence to a provenance note (recommended), or land the draft blobs `7c5f18b4` and `322f5321`.
2. **README-28** (Unit 2): authorize the 28 → 29 declaration-count fix and the missing `c3_necessity_via_hidden` row, at `papers/introduction_repro/README.md`:4 and :68 and root `README.md`:117.
3. **OD-2/R-06** (Unit 3): confirm (b). L129 reports the substratum-sourcing result in plain words and cites GR §3.3.
4. **R-15** (Unit 3): authorize restoring the landed Doukas wording at L93 (+7 words).
5. **R-16** (Unit 3): keep (b) as worded, or restore the locator "[BD16, Prop. 1 and Cor. 1]".
6. **O-1, O-2, O-3, O-10, O-13, O-14** (Unit 3): adopt or waive each (proposed: waive all six).
7. **O-26** (Unit 3): accept (b), citing the concept-DOI resolution in #942 c.6434035598, plus one read-only re-resolution. A waiver would vary c.6657705110.
8. **Har04, under OD-8** (Unit 3): accept attribution through Montina (proposed), or require a first-hand read.
9. **X-2** (Unit 4): after the read-only check, (b) no change, or (a) add "for a uniformly distributed message".
10. **S9-I2, S9-I7, S9-I8** (Unit 4): accept (b) after the independent review.
11. **OD-15** (Unit 5): accept the release gate's `lean-axioms` step, the current census families and the citations at GR:260 and Main:147 as the evidence, or require a separate reviewer re-run.
12. **EV-28** (Unit 5; a hard blocker, to settle before Unit 6): choose (d) transfer, for example to #1029, with the pointer edits; (a) an independent review of the 14 added entries; or §A.46 item 6.
13. **EV-14** (Unit 5): confirm that no verification obligation is kept (proposed), making it (b) plus a pointer correction.
14. **CON-26 and CON-02:** accept (b). **CON-42:** (b), or (d) to #1028 beside S9-I6 at Main:340.
15. **SC-30** (outside #941; for the record): every sub-item is homed (#1028 orphans 37 and 42, #1029 orphans 34 and 38, #1015 D-17) except D-16, D-22, D-24 and D-25. Those four have no recorded destination; the findings' quoted wording does not appear at `main` (Main:131, Main:342, SM:112, GR:591), and they are not adjudicated under #941.
16. **The four #944 legs (S9-I1, I3, I4, I5):** accept their reclassification as complete on their #941 legs, with #944 as an audit input, or approve transfers.
17. **EV-CI-1 and EV-CI-3** (Unit 5): accept (b) (proposed), or authorize one `bh-mutants` dispatch.
18. **ADM-B** (closure): approve the maintenance edit of the #941 Objects line and the OD-15 Readiness entry.
19. **Optional:** whether #1134's `unattached` coverage-ledger record needs a #941 row (proposed: no).

EV-L needs no owner decision: its recorded acceptance is #942 c.6433846714, which records step 7 as accepted. Its checkpoint `cb2029ce` is not on `main` and is provenance only.

## Owner rulings (#941 c.6677500012)

Ruling by amaybaum in the Claude Code session chat on 2026-11-06, posted verbatim on #941 as c.6677500012
(2026-11-06T05:11:33Z); the summary record is #1031 c.6677496553. Quoted:

> Approve the proposed execution sequence, Units 2–5, with separate review and merge gates. Unit 6 remains the final independent closure audit; closing #941 itself still requires an explicit decision.
>
> | Items | Decision |
> |---|---|
> | 1. SC17, SC31, SC33 | Approve three separately justified provenance narrowings. Do not land superseded Introduction blobs merely to cure historical references. |
> | 2. README-28 | Approve correcting the inventory to 29 declarations, including c3_necessity_via_hidden, in both identified READMEs. Preserve evidence bytes. |
> | 3. OD-2/R-06 | Accept the proposed no-change route, subject to exact-source confirmation of Introduction L129 and GR §3.3. |
> | 4. R-15 | Approve restoring the previously reviewed, narrower Doukas wording. |
> | 5. R-16 | Keep the current wording unless a first-hand source check establishes a material citation defect. |
> | 6. Six optional items | Waive O-1, O-2, O-3, O-10, O-13 and O-14 individually as optional additions outside the chosen expository scope. This does not waive their underlying scientific questions. |
> | 7. O-26 | Favor a sourced no-change disposition. #942 c.6434035598 records the concept and version DOIs, but require one fresh read-only resolution before closing the item. Do not waive the verification requirement. |
> | 8. Har04 | Require a first-hand source check for any substantive claim attributed directly to Har04. Otherwise, explicitly qualify the attribution as secondary. |
> | 9. X-2 | Approve the narrow correction, but first independently verify the prior conditions. If missing, add only the supported uniform-message qualifier. |
> | 10. S9-I2/I7/I8 | Authorize focused independent review of each interpretation. Accept the no-change outcome individually only if supported; do not promote interpretive premises. |
> | 11. OD-15 | Require independent checks of the three declarations' axiom reports and census registration. Existing CI evidence alone does not automatically settle the obligation. |
> | 12. EV-28 | Choose independent verification of the 14 additional module entries. Keep #941 accountable until reviewed. Do not transfer or waive the evidence obligation merely to permit closure. |
> | 13. EV-14 | Accept the proposed no-new-verification disposition, retaining historical provenance and correcting the pointer where needed. |
> | 14. CON-26/02/42 | Accept no-change for CON-26 and CON-02 after source confirmation. For CON-42, check whether its full finding is already addressed; otherwise return a scoped #1028 transfer proposal. |
> | 15. SC-30 | Record its existing destinations; do not reopen it under #941. |
> | 16. Four #944 legs | Approve classification as complete on the #941 Introduction-audit side where the existing record supports that. Preserve #944's independent scientific responsibilities. |
> | 17. EV-CI-1/3 | Accept documented no-change dispositions if the existing evidence passes review. No bh-mutants dispatch is authorized. |
> | 18. ADM-B | Approve narrow planning-block maintenance at closure, including the obsolete OD-15 Readiness wording. |
> | 19. #1134 unattached | No separate #941 row is needed if the final ledger reviewer confirms full coverage. |
>
> Unit 2 may prepare its documentary PR containing the three SC narrowings, README corrections and retained ledger. Require independent review of the actual 190-row artifact before merging it. Units 3–4 may prepare one narrowly scoped Introduction correction PR, followed by the canonical rebuild under the existing PDF conditions. The R-15 and X-2 changes must be individually traceable to reviewed evidence. Unit 5 may perform the approved evidence review, including OD-15 and EV-28. Any new scientific execution or workflow dispatch beyond that scoped review requires a separate authorization. Do not merge any of these PRs automatically. Each needs exact-head review, green CI and an owner merge decision. The 22 proposed no-change rows must be checked individually, not accepted through a blanket status change. The hard closure condition remains EV-28. Until its independent verification is resolved, #941 stays open.

Rows each item bears on (marked "ruled: item N" in their "Owner decision" cell): 1 SC17-68, SC31-140, SC33-111;
2 README-28; 3 OD-2 (R-06 follows OD-2); 4 R-15, X-1; 5 R-16; 6 O-1, O-2, O-3, O-10, O-13, O-14; 7 O-26; 8 OD-8;
9 X-2 (R-20, R-35 and S9-A2 follow X-2); 10 S9-I2, S9-I7, S9-I8; 11 OD-15 (rF-20 follows OD-15); 12 EV-28 (X-4 follows
EV-28); 13 EV-14; 14 CON-26, CON-42, CON-02; 15 SC-30; 16 S9-I1, S9-I3, S9-I4, S9-I5; 17 EV-CI-1, EV-CI-3; 18 ADM-B
(X-5 follows ADM-B); 19 no row. No row's status or proposed outcome is changed by recording a ruling.

## Prioritized execution package

None of these units is authorized by this ledger.

**Unit 2: documentary gaps** (priority 1; mechanical)
- **Authorization:** paper-only edits to mutable records; one draft PR; independent review; exact-head CI; then a separate merge decision.
- **Changes:**
  - narrow SC17:68, SC31:140 and SC33:111 to provenance notes. These are mutable records, not in `legacy-records.json`.
  - add the `c3_necessity_via_hidden` row to `papers/introduction_repro/README.md`, and change the count from 28 to 29 at :4, :68 and root `README.md`:117. "28-module" stays, and the JSON is byte-identical.
- **Confirmation only:** the reviewer confirms O-17 and O-23 (G1 §4) against L203 and L205.

**Units 3 and 4: one Introduction PR and one rebuild** (priority 2)
- **Authorization:**
  - paper-only edit of `papers/Introduction.md`, with `.tex` and `.pdf` regenerated by `sh ./build.sh Introduction`;
  - the owner's PDF conditions (c.6643207092): `.md`, `.tex` and `.pdf` committed together from one source revision; the TeX toolchain version and build command recorded; reviewers examine the exact committed PDF;
  - §A.25 propagation check (no mirror is expected);
  - independent review, then a separate merge.
- **Unit 3:**
  - R-15: restore "Doukas states the contraction argument concurrently, as a no-revival obstruction to Markovian realizers [Dou26, Prop. 1]" (+7 words).
  - Optional: R-16's BD16 locator.
  - (b) records for R-14, R-17, R-18, OD-2/R-06, OD-8, O-4 and orphan 36.
  - O-26: (b) plus one read-only re-resolution of the concept DOI.
  - O-1, O-2, O-3, O-10, O-13, O-14 as the owner rules.
- **Unit 4:**
  - a read-only check of X-2 against BH-01 `REPORT.md` C2, `PLAN.md` and S9-A2, with no computation; then (b), or the (a) phrase "for a uniformly distributed message" in the same PR;
  - an independent review of the (b) dispositions for S9-I2, S9-I7 and S9-I8.

**Unit 5: evidence and accountability** (priority 3; EV-28 must be settled before Unit 6)
- **Authorization:**
  - read-only confirmation of OD-15 from `main`: the recipe is `tools/lean_axiom_check.py` at a named `main` commit, with the census step `lean-manuscript`, and no dispatch;
  - administrative (b) records for EV-L (citing c.6433846714), EV-CI-1, EV-CI-3 and EV-14;
  - the owner's EV-28 route. If (d), a paper-only edit of `introduction-repro-ext/README.md`:6 and `papers/introduction_repro/README.md`:9, and a separately approved, comment-only edit of `evidence-replay.yml`:7 and :24 after a §A.43 item 4 trigger check.
- **Records for the new rows:** SC-23, SC-30, #1002, CON-26, CON-42 and CON-02 go in the same administrative records, or in Unit 6.

**Unit 6: independent closure audit** (last; read-only)
- The reviewer:
  - confirms every (b), (c) and (d) row against `main` and the cited records;
  - confirms that Units 2–5 landed;
  - recomputes N_unaccounted from this ledger's baseline of 36.
- The owner then decides closure, with the ADM-B maintenance edit.
