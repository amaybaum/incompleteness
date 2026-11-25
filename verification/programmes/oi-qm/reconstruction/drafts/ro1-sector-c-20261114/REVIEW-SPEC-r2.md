**Verdict: ACCEPT WITH CHANGES** — `RO1-SPEC-r2.md` at `551b2f180b5372bc2d00134b4afbceac8d106c82` (PR #1294; file SHA-256 `5ea19f79…3528`, matching the directory README). All three r1 blocking findings are resolved, and all 22 dispositions are applied. Three new major findings must be fixed before acceptance: two prejudge open stops (S5, S9) and one overstates the O11 analysis. Six minor findings follow.

# Independent re-review of RO1-SPEC-r2

**Reviewer:** the same independent agent as for r1, not the writer. **Method:** reading only: no computation, no Lean, no edit, no post.
**Read:** `RO1-SPEC-r2.md` and `RESPONSE-SPEC-r1.md` at `551b2f18`. Sources checked again at the same pins as r1: `main` `dfeec843` (`papers/Main.md`, `book/ch18-beyond.md`, `B4PRIME.md`), SEL-ACCESS-1 `1b966a03`, SEL-EXCL-1 `0ecfddeb`, SEL-DISC-1 `445b17f7`, LEDGER `9ff3b8d9`, and PR #1294's review list.

**Integrity checks:**
- `REVIEW-SPEC-r1.md` as preserved in the PR is byte-identical to the review as written, and its SHA-256 is `f3e19cf8…58cd`, matching the README.
- r1 is unchanged (`d7f4380d…a4341`).
- The commits since `7156d761` touch only this directory.

Line numbers refer to `RO1-SPEC-r2.md` at `551b2f18`.

## 1. Dispositions of the r1 findings

### Blocking

- **B1: resolved.**
  - §7.1 (ll. 404–406) states that §7 is a conditional check, not a verdict, and that the rule applies only to a complete, frozen C.
  - §7.2 marks K-acc **Open**, citing SEL-EXCL-1 ll. 46, 129 and 150, all verified.
  - The control is UNSOURCED (l. 438), and "REFUTED" and "cannot yet be sound" are removed.
  - The single-use test's setting actuation is now an availability row in §5.1 (l. 297).
  - §8 step 3 requires the classical control to be exhibited before it is green (ll. 509–513).
  - The class reading and reading (i) are stated (l. 405), and the sector caveat is given (ll. 444–445).
  - Residual: N4.
- **B2: resolved.**
  - `Θ` (ll. 344–355) is labelled [P]. It preserves wings and local instruments, composition, sequence and adaptivity, the message budget, records and exogenous settings.
  - Its support at source is correct: SEL-EXCL-1 l. 81; SEL-DISC-1 ll. 129 and 190; SEL-ACCESS-1 §1 item 4.
  - `Θ` constrains only the comparison class, so §6.1 is untouched (l. 366).
  - S8 (l. 578) is a genuine owner decision, since without `Θ` soundness excludes nothing.
  - The re-derivations are correct at their cited scope:
    - single use (ll. 424–428): the Tsirelson bound for the bipartite image;
    - same-seed reuse (ll. 429–432): SEL-DISC-1 l. 149 proves complete local-history no-signalling for local adaptive instruments;
    - one-bit message (ll. 433–435): D7.
  - §8 steps 4–7 now read through `Θ`. Residual: m2.
- **B3: resolved.**
  - §7.4 states its search (ll. 476–477) and restricts its claim to that search (ll. 479, 491).
  - Rows are added for (C1)–(C4) (untested; Main:78 verified), for the OI⁺ principles and both refinements (Main:584–588 quotes verified), and for candidate E (marked outside the repository).
  - The H-Bell row now reads "No, as stated" (l. 488). The writer's refinement, that clause (iii) is unapplied rather than shown inapplicable, is correct.
  - The l. 174 ban of r1 is withdrawn, and the question becomes S9.
  - Residual: N1.

### Major and minor

- **M1–M7: applied and verified.**
  - M1 is reworded as notation (ll. 124–126).
  - M2 is now S7. J7 reads "§A.29 judgement: not met" with reasons (a)–(c) (l. 262).
  - M3: LEDGER and r3 are moved to §9 as off-main records, with the gap stated (ll. 547–564), and the main-line citations use Main:724 directly. All verified, including "part-empirical rather than a pure lemma" and (xiv) at Main:724.
  - M4: C0 is dropped, and the swap/flip control is cited instead (SEL-ACCESS-1 ll. 53–69).
  - M5: the K-X row is corrected (l. 224). Residual: m1.
  - M6: §4 is restated (ll. 241–249).
  - M7: the constraint is moved under S1 (ll. 203–209).
- **m1–m12: applied.**
  - The §5 heading is labelled "(proposed)".
  - §5.1 adds the four rows and is retitled "In `Γ`?".
  - S-A5 covers banks prepared in `μ`.
  - The finiteness hypotheses are restored: Main:758 and :362, and the theorem's (i)–(iv) at Main:366–376.
  - K-dyn is now [P] and adopts posits.
  - S4 is withdrawn.
  - O4 is named as scientific.
  - The labels are fixed, the O12 attribution is corrected, coverage now maps every experiment, the outcome wording is fixed, and the measurement-dependent row is corrected.

## 2. Major findings, new in r2

**N1. §6.1 (l. 318) prejudges S9 and contradicts §7.4.** "C is not repaired by adding quantum-set membership, *or any equivalent condition*, as a clause or an assumption."
- **The conflict.** The OI⁺ principles are, by the kernel theorem the spec cites, equivalent to exact finite operational QM on every nonempty finite carrier (Main:584–588; l. 485). Read literally, l. 318 bars them as a clause. Yet §7.4 says they "come nearest" (l. 493), and S9 (l. 579) leaves their admissibility to the owner.
- **The records bar a choice, not a logical equivalence.** #1060 forbids choosing C "by testing whether the resulting correlations match quantum predictions". #914 item 1 forbids introducing "a premise merely to reproduce quantum predictions". Neither bars a physically justified principle that turns out to be equivalent to QM.
- **Safe path:** restate l. 318 as a bar on clauses adopted *because* they are, or are equivalent to, quantum-set membership, with justification judged under §6.1 and §A.29. Note that whether a principle proved equivalent to QM can be a clause is part of S9. Make "come nearest" (l. 493) neutral: state the row's status and dependencies only.

**N2. §7.3 assumes measurement independence (xiv), which is open as S5.**
- **(b) (ll. 455–457)** requires the model reaching CHSH = 2√2 to have "a setting-independent common source". For an OI model that is (xiv) on its hidden source. The setting-independence in SEL-DISC-1 §6.3 belongs to the quantum reference state, that is, to the `Θ`-image under (b), not to the OI model.
- **l. 460** derives local response functions from "pointwise parameter independence together with K-src's common source and determinism". K-src deliberately excludes (xiv) (l. 220). The Bell ceiling needs hypothesis (iv), `p(Ω|a,b) = p(Ω)` (Main:372–374).
- **The consequence.** "`R*` cannot be pointwise parameter independence" (l. 462) holds only under (xiv). Without it, parameter independence with measurement dependence can reach the quantum value at `I_ont ≥ 0.0309` bits (Main:416–423).
- **An internal contradiction.** l. 463 then allows "a source that depends on it", which (b) has excluded.
- **Safe path:** in (b), require the CHSH value of the record law and leave the OI source unconstrained. State the parameter-independence paragraph as conditional on (xiv) (S5). Note that without (xiv) the measurement-dependent route remains open.

**N3. The O11 answers "yes" under (i) and (ii) are stronger than the argument (ll. 183–193; S1 l. 572).** The question is whether physically equivalent descriptions *can get different* membership decisions.
- **Under (i).** The text shows only that relabelled or enlarged descriptions are separate models, and it then expects their decisions to agree ("agreement is expected, but it is not proved"). No case of differing decisions is given. The supported answer is "not excluded by the relation; it rests on each clause's invariance, unchecked for K-acc and K-X".
- **Under (ii).** The argument uses record-equivalent but not gauge-related lifts (M-1, Q2A). But l. 181 took "physically equivalent" to mean relabelling, decoupled enlargement and change of alphabet. l. 192 itself says it is not stated whether those fall under `G`. So "yes in general" applies to a different notion of equivalence than the one fixed.
- **Safe path:** answer "not excluded" for (i) and (ii), with the reasons as given. Keep record-equivalent lifts as a separate, labelled case. Make S1's "Why" column agree.

## 3. Minor findings, new in r2

- **N4. The conditional in §7.2 (ll. 440–442) has an antecedent the stated tuple cannot meet.** `T` writes no setting, so "its single-use test is in `Γ`" refers to an enlargement with setting sources and controllers. That enlargement is not constructed, and its K-dyn, K-obs and K-src are unchecked. Constructing it would be a new countermodel, which is #1143's work (r3 §4.5.2). Say "an enlargement of the PR model that executes these programs, if one exists", and route its construction to #1143 and #866.
- **m1. `R*` is defined by its tests.** "the following restriction `R*` … the condition K-X must state … such that (a) … (b) …" (ll. 449–458) defines `R*` by the outcomes that l. 224 says "do not define it". Present (a)–(b) as necessary tests on any K-X, with (c) and §A.29 as the justification requirement. This is not a quantum-set assumption, and no H-Bell or IC₂ choice is made, both as the coordinator required.
- **m2. `Θ` (f) "exogenous settings map to exogenous settings" (l. 355) has no OI-side criterion.** Under K-acc, settings are executed by the model's dynamics, so which OI variables count as exogenous settings needs stating. This ties to S5 and S7.
- **m3. Two OI⁺ row overreaches (l. 485).**
  - The [A-inf] "excludes PR tables on that carrier" needs `Θ` (a)–(b). On one carrier a PR table is an ordinary classical channel.
  - The E row cites SEL-ACCESS-1 l. 81 for the CHSH statement, which is at ll. 83 and 90. "fails CHSH > 2" should read "obeys CHSH ≤ 2".
- **m4. Citations in §2.3 and §2.1.**
  - "G ⇒ O also fails for C2-ch and C2-sel" (ll. 168–169) is at B4PRIME §3.5, l. 367 (witness WE, in `PPer`), not l. 19.
  - Relation (iii) (records over the whole `Γ`) is not B4′'s `O_C` (records of one record class), so "differ at B4′'s scope" needs that step stated.
  - l. 129: the Main:588 quotation supports "OI⁺ is not entailed by bare OI", not "no E is adopted", which is a record (#914).
- **m5. Wording in §7.2.** "Verdict of the check" (l. 437) conflicts with §7.1's "not a verdict", and l. 438 cites §8 step 2 although §7 "is not an application of this rule" (l. 532). Use "Outcome of the check", and say UNSOURCED "in the sense of step 2".

## 4. The three added checks

- **The PR countermodel, clause by clause (§7.2).** The table is correct at source:
  - K-dyn: SEL-DISC-1 l. 65.
  - K-obs: SEL-EXCL-1 l. 44.
  - K-src: l. 67.
  - K-acc is open: ll. 46, 129 and 150.
  - K-rec and K-res are met conditionally: ll. 67, 87 and 91.

  The closure consequences for single use, same-seed reuse and the one-bit message are right under `Θ`. One gap remains: N4.
- **The missing restriction `R*` (§7.3).** It is named and not chosen. Neither H-Bell nor IC₂ is selected, and no quantum-set assumption is made on C. But (b) and the parameter-independence step silently assume (xiv) (N2), and the "such that" form defines it by tests (m1).
- **The O11 analysis (§2.3).** The method is sound: it takes Main:724's representatives as the equivalent descriptions, and the quotations are verified. The verdicts under (i) and (ii) overstate the argument (N3). The answer under (iii) is correct, including the caveat that K-dyn can fail invariance (Main:598).

## 5. Stops

| Stop | Assessment |
|---|---|
| S1 | **Genuine.** O11 is open by owner item 1. Fix its "Why" column per N3 |
| S2 | **Genuine.** `R*` has no justified candidate within the search. Q7 is the owner's, O4 is #1143's, and the conditional variants follow r3 question 6 |
| S3 | **Genuine.** K-acc has no criterion and the controls are UNSOURCED |
| S5 | **Genuine,** but prejudged in §7.3 (N2) |
| S6 | **Genuine.** It changes soundness, confinement and the PR check |
| S7 | **Genuine.** Owner item 1 leaves typing open; K-dyn and K-acc depend on it |
| S8 | **Genuine.** `Θ` fixes the target's comparison class, which only the owner can adopt |
| S9 | **Genuine,** but prejudged by l. 318 (N1) |
| S4 withdrawn | **Justified.** K-obs quantifies over each observer (l. 219), so it holds under either answer to ledger Q1. Q1 bears on coverage's "one stated `Obs`" (ll. 377–378) |

## 6. New errors

No claim of a refutation or a theorem remains.
- "REFUTED" and "FAILS" appear only as possible outputs of the proposed rule (§8).
- The [A-inf] conclusions of §7.2 are conditional on availability (S3), on `Θ` (S8) and on the class reading (S6).
- The off-`main` statements carry the §A.42 item 8 gap (ll. 561–564).

N1 and N2 are the only places where an open question is prejudged.
