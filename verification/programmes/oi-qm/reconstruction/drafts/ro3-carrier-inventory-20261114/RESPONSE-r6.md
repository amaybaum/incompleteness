# RO-3: response to the focused review of inventory r6

**UNREVIEWED.** This file gives the writer's disposition of each item of the focused review of r6
(delivered as `REVIEW-1303-INVENTORY-r6.md`, REVISE for map completion only, no label refuted;
SHA-256 `dfaaab898368ad8a9a661cbb54d2581f25e494173155759e2a56c5c0555ca672`). r6 is left unchanged.
The changes are in `RO3-INVENTORY-r7.md`. Everything was checked at `main`
`7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`, by reading only, with `git show` and `git grep`, and the
census. #1169 comment 6894115930 was read first-hand through the GitHub API. Nothing was built or
computed, and no repository, Issue or PR was written.

Dispositions:
- **accepted**: applied as the review proposes;
- **accepted, modified**: applied with a stated difference;
- **noted**: no change needed.

Section numbers below refer to r7.

## K1. The authority record

**Disposition: accepted.**
- **Checked.** #1169 comment 6894115930 (`amaybaum`, 2026-11-15T12:11:24Z): "Confirmed, proceed as
  suggested". Its #1303 row presupposes the r6 review. The row's goal link is "Priority item 2, A1
  dependence of the main equivalence".
- **Applied.**
  - Standing cites the comment as the authority for r6 and r7, quoting the #1303 row and the "Not
    authorized" line verbatim. r6's "no owner comment ... was found" is removed.
  - The goal link cites the comment.
  - §3's AM-3 entry is restated in the owner's terms. It names a weaker, independently justified
    premise, a complete proof with at least one independent consequence, and a negative that names
    the class it excludes.
  - The entry stays a proposal. It is not chosen.

## K2. Missing consumers

**Disposition: accepted.** Each was read at the base.
- **(a) Main:588 and GR:266: new row AM-27.**
  - The row covers census 21 and 22. It adds census 6, 14, 19 and 20 (current), which carry the
    same finite-configuration context and are anchored at Main:588 and GR:256–274. It also adds the
    kernel-only sourcing families 18, 23–27 and 29.
  - Cited: `obs_not_layerFlowExecutable` (`ExecSource.lean:129`, context at :125) and
    `coherentLiftClass_eq_substratumClass` (`LiftSource.lean:164`; substratum sections at :196 and
    :296).
  - Status: established (K) on finite configuration spaces; open without A1. The row records that
    these results bear on EXACT.
- **(b) Main:145: new row AM-28.** It covers census 35 and 36, with the line numbers of the Return
  section (:101, :109, :122). The conclusion's periodicity step is traced to `rootedMap_periodic`
  (`RootedClassification.lean:135`). AM-1 points to AM-28.
- **(c) SM.**
  - Theorem 19 is AM-30, with `theorem_19` at `Reciprocity.lean:129` and `[Fintype H]` at :40. It
    adds that Theorem 19 is a dependency of Theorem 23 (Sub:116).
  - Theorem 22 is AM-31: SM:1376–1384, :52 and :92, and the `Cut` section at
    `PhysicalC4Discharge.lean:574`.
  - SM:44, :112, :22 and :1654, with SM:236, :308 and :336 found by the recipe, are AM-32. They are
    classified as G-fam members or as mirrors of AM-1, AM-3 and AM-4.
  - AM-16's "not traced" sentence now points to these rows.
- **(d) Census 32: new row AM-29.** The finiteness is used: `EnsembleDetermined` is defined through
  `IsProb`, a finite sum, and the positive route uses the uniform law on a finite orbit.
  - The review cites :111. That is the section's substratum `variable` line; the theorem
    `ensemble_underdetermined` is at :118. `stochastic_interface_gap` is at :182.
  - [IR], the writer's reading: on the OBL class the zero configuration is fixed. So `δ_0` and `μ`
    are distinct invariant probabilities, and the underdetermination carries over. This is not
    stated on `main`.
- **(e) Posit (ix): added to AM-7**, quoted from Main:724.

## K3. A structural recipe that can be rerun

**Disposition: accepted, modified.** §7.0 adopts the reviewer's three steps:
- Lean contexts that put finiteness on a substratum, its configuration space or its hidden carrier;
- the manuscript lines citing them;
- hidden and total finiteness in prose.

§7.0 states each step as a `git grep` pattern at the base, with its result.

**Modifications.**
- Step 1 is split into five patterns, L1–L5.
- For L5, `[Fintype S]` across 79 modules, the 37 modules whose text mentions the substratum were
  classified by census family. The other 42 were classified by that absence and were not read one by
  one. r7 states this as a limit of the run, and does not claim to have read them.
- Step 3 runs over every `papers/*.md`, not only the seven papers already covered.

**What else the recipe found**, besides K2:
- A.8 and A.9 (GR:791–839). They were in §1.5 but missing from the map; now AM-33.
- Substratum Proposition 24.4 (Sub:331–333), and Lemmas 24.1 and 24.1A in the kernel (census 61 and
  62); now AM-34.
- The kernel-only sourcing families listed under (a).
- AM-1 mirrors in the application papers: `Introduction.md:12`, :93; `Medicine.md:13`, :25;
  `Bioinformatics.md:14`; `Complexity.md:430`, :474. The review reported no hits outside the seven
  papers, but these restate the recurrence-scale result.
- C3 mirrors in `Medicine.md:31`, :98.
- Two records that use the posit as a premise: `MR-star.md:296` and `TUNE-1-SOURCING-r2.md:139`; now
  AM-35.
- Several groups that do not consume A1, each listed in §7.2 with its reason:
  - constructed finite realizations;
  - the C3 bound;
  - exhaustive enumerations;
  - finite operational carriers;
  - census 2 and 13;
  - the Definition's "total system";
  - Axiom 2's recurrence;
  - records that restate the posit.

**Result.** The map is now complete relative to the recipe at `7ac74a4b`. §7.4 states the boundary:
- a consumer that no pattern reaches would be missed;
- items still marked "not traced here" concern the inside of rows already listed.

## AM-3: first missing step, observations and controls

**Disposition: accepted, as a recommendation.** §3 records:
- **The first missing step.** Before any proof, preregister three things:
  - the observational inputs: Lemma 1, the record prong and Axiom 2;
  - the candidate class `P_w` of weaker premises, each with its independent justification;
  - the target: bijectivity of a full-measure invariant set, and hidden-sector injectivity.
- **O1 [IR].** Conservativity of a σ-finite measure gives surjectivity up to a null set, with no
  normalized measure. It is labelled the reviewer's own check and not on `main`. Conservativity is
  sufficient, not necessary (the `Z` shift).
- **O2 [IR].** The expected negative: a measure-preserving, conservative 2-to-1 map whose merges lie
  in the hidden sector only. It shows that neither member of `P_w` gives hidden-sector injectivity.
  It replaces the doubling map as the cleaner countercontrol.
- **The review's protocol.** Its controls, preservation checks, countercontrols, independent
  consequence, decision rule and skepticism, as the review states them.

**Checked on paper.** O2's map `T(v, h) = (v ⊕ h_2, σh)`:
- each point has exactly two preimages, which differ only in `h_1`;
- the one-step visible matrix has every entry 1/2.

Neither observation is used as a premise.

**Not chosen.** AM-3 is proposed, not chosen as a unit. That is the owner's decision after this
review.

## Not applied

- **Promoting O1 or O2 to a status.** Both stay [IR] until a reviewed record on `main` carries them.
- **Status changes.** No cell's status changes, no result is withdrawn and no premise is adopted.
