# NOTES r1 for NLCAND-r1: what was read, what could not be checked

Working notes beside `NLCAND-r1.md`. Not a record; no result is stated here that is not in that file.

## 1. Provenance and compliance

- **Instruction.** The owner's instruction of 2026-11-14 is quoted in `NLCAND-r1.md` as it was relayed in the
  task brief. No Issue or comment id was supplied to the writer, and the host record was not read. A landing
  or citation of this work needs that id, quoted with author and time (§A.42 item 7).
- **Read-only.** No repository file was edited, nothing was committed, pushed or posted. The two files in
  `nlcand/` are the only outputs.
- **No computation on OI rules.** Every derivation in `NLCAND-r1.md` was done by hand. Two uses of a script
  occurred and neither computes on a rule: a short viewer printed fields of the stored file
  `stage2/runs/10/results.json` of the mixed-path unit (counts of verdict tokens, the headline, the sum of the
  field `nonlocal_among_nonsignalling`); and text substitutions were applied to the draft. No probe, checker or
  Lean build of the repository was run.
- **#1278.** The assessment was not present in any worktree named in the brief. It was read from the local
  object store at `d8b74527` (`native-apparatus-source-20261113/ASSESSMENT.md`); its `EVIDENCE.md` was not read.

## 2. Reading inventory

Pins as in `NLCAND-r1.md`. "Full" means read end to end; "part" lists what was read.

| Source | Extent |
|---|---|
| `papers/SM.md` | §3.1 full (:102–168); :14, :48, :96, :220–246, :290–296; Appendix A headings and setup only |
| `papers/Substratum.md` | :100, :104, :120–200, :220 |
| `papers/Main.md` | §3.3 full (:358–427); :588; :724 |
| `book/` | grep only: the explicit ring construction has no mirror in `book/ch*.md` (pattern: the right-neighbour assignment) |
| OA-3 r4 and its `STATUS.md` | :40–460, :498–560; status header |
| OA-2 r4 | :640–700, :776–830 |
| OA-1 r5 | :96–110, :145–200 |
| mechanism-2 `DESIGN.md` | :150–215, :540–590 |
| `prepared-pair-source.md` | full |
| `native-preparation-source-1` `PREPARATION-SCREEN.md` | full |
| `physical-interface.md` | :286–299 |
| TUNE-1 Step 2 sessions 3, 4 | S3:56–76; S4:86–101, :423–474 |
| Step 3A r3 (off `main`) | :154–222, :462–531, :712–960 |
| `STATUS-SOURCING.md`, `STATUS-STEP3A.md`, `LANDING-PLAN.md` §4 (off `main`) | full; :20–110; :236–266 |
| Bell ladder r3 (off `main`) | full |
| `STATUS-BS.md`, `STATUS-LADDER.md` (:1–120), `SB-L3.md` (off `main`) | as stated |
| Bell-scope r2 (off `main`) | :100–266 (claim table, §2, §3.1–3.4) |
| Mixed-path unit (off `main`) | :1–80, :300–345; `STAGE2-PREREG.md` only for its headline rule (:350–357); stored `results.json` top-level fields |
| #1278 `ASSESSMENT.md` (off `main`) | full |
| Lean: `ExecSource.lean` :1–40, :121–175; `StructuralClosure.lean` :336–356; `SecondOrderLayer.lean` :198–212; `SubstratumInterfaceAudit.lean` :60–71; `RegionTower.lean` :283–307; `SecondOrderDrive.lean` (declarations list) | statements read, not built |

Not read: `papers/GR.md`, `papers/Structure.md`, `papers/Methodology.md`; the book chapters; OA-1 and OA-2
outside the ranges above; `native-interaction-source-2`; apparatus-1 and mechanism-1; minacc-1; Q-868-H; REC-1;
SUBSTATE-BRIDGE-1 beyond the L3 extract; Bell-scope §§4–8; mixed-path §§1–3, §5–6 and its probe.

## 3. Searches behind the negative statements (§A.19), and their bounds

- *"No `d = 3` non-linear rule is written" (M1, F9).* Searched `papers/*.md` and `book/*.md` for the ring
  construction's wording and for its notation `R(i, x)`: one hit, SM:112. The reconstruction records read treat
  the ring only (`G_SM`, SMR). The rounded rule of SM:294 is a different non-linear rule, in `d = 3`, and is
  not a version of the ring rule. Bound: the corpus was not read end to end; `verification/` outside
  `programmes/oi-qm/reconstruction` was not searched.
- *"The manuscript does not list the reference class" (M2, F3).* Read SM:104–112, Main:362, :724. Bound: other
  papers and the book were not searched for a definition.
- *"The one-tick PR-type table is not recorded" (F5).* Searched the worktrees named in the brief for files
  mentioning the ring rule together with a PR box or CHSH 4. Hits: mechanism-2 (Proposition B's abstract
  example `a = h ⊕ xy`, `b = h`, not derived from the rule), OA-2 (a `ℤ₄` affine counterexample that signals)
  and Step 3A. None states that SM's update has this form. Bound: a search by phrase, not a reading.
- *"Directed speeds two and one; corridor lemma" (F2).* `physical-interface.md`:288–291 has the symmetric
  envelope and mechanism-2 :191 the non-reciprocity. No statement of the corridor copy was found by searching
  for "corridor", "leftward", "all-zero", "quiescent" in the three files `physical-interface.md`,
  `preparation-loading.md` and `SOURCE-SCREEN.md`. Bound: three files.

## 4. What could not be checked

1. **Every [H] derivation is unreviewed and has no machine check.** The ones a verdict rests on: the inverse
   (§1.2), the dependency sets (B1), the corridor induction (B3), the one-hop total variation `1/q` (B4 (ii)),
   the one-cell table and its no-signalling argument (B5), the erosion bound (C3).
2. **B4 (iii)** is undecided. The earliest tick `3 + ⌊g/2⌋` was derived twice (directly, and from Lemma S of
   the mixed-path unit, which is itself an unreviewed off-`main` argument). Whether the law depends on the
   remote setting at `(D, T) = (6, 5)` was not derived.
3. **B5 beyond `q = 2`.** `β − α = sel(y, x)` holds for every `q`; a CHSH value was computed only at `q = 2`.
   A hand value at `q = 4` with parity outputs (`y ∈ {0, 2}`, `x ∈ {1, 2}`) also gave 4 and was left out of the
   file as unneeded.
4. **A2.** Whether the label actions generate all reversible classical circuits was not examined.
5. **P13.** The boundary bound was argued for a boundary read in the union graph. The manuscript reads the
   boundary in the configuration's own graph (SM:150); that form was not re-derived.
6. **P12.** Taken from SM:112's assertion; the recurrence argument of Main §2.3 was not re-read.
7. **P16.** Appendix A of SM was identified by its setup (the linear ring) and not read.
8. **C4, C5.** Nothing is known here about the cycle structure of the ring rule; μ-R was not analysed.
9. **The kernel scope in A3** was read from the statement of `obs_not_layerFlowExecutable` and the header of
   `ExecSource.lean`. The definitions of `obsTheory`, `LayerFlowExecutable` and `substratumClass` were not
   traced, so the phrase "stated observer architecture" is the file header's, not an independent reading.
10. **Line citations** were checked against the files at the stated heads for every range that carries a
    quotation or a verdict; citations of whole sections (for example OA2:381–490) were taken from the records
    that cite them.

## 5. Points where the findings differ from the brief's framing

- The brief traces the control obligation to the linear rule. At kernel level the cited theorems hold for
  every substratum rule (A3), so only the TUNE-1 form of that obligation (translation-only labels, Lemma A-T)
  is specific to linearity.
- The brief asks whether the ring rule is a complete dynamical update. It is; what is absent is listed in
  §1.3 of the main file.
- The brief's "long edges" are not in the ring rule: its switched edge has length two. Verdict (b) is about
  that rule. A rule with a longer switched edge would be a different candidate, and its jump length is a free
  parameter of the kind §A.29 rejects (§7 of the main file).

## 6. Choices a reviewer may want to vary

- The observer block of three cells and its complete history (smaller blocks are the open case of OA-3 N5).
- Whether a wing's record region must contain its generator cell (decides B5's no-signalling).
- Which set of configurations is the reference class (decides P5–P7 and what "outside the reference cone"
  means in B3 and J1).
- The law: everything in §4 of the main file is under the uniform counting law at the setting slice.

## 7. Confidence (writer's estimate)

- High: §1.2; B1; B2 given Main's theorem; C1.
- Fairly high: B3; B4 (ii); B5's algebra and one-tick no-signalling; the erosion bound.
- Moderate: the multi-tick masking argument in B5; the preserved-results outcomes P5–P8, P10, P13.
- Low or none: anything about T1 (A5), B4 (iii), μ-O and μ-R.
