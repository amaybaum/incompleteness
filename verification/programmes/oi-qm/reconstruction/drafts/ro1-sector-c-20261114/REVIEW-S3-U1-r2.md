# Focused review of S3-U1-r2 against the review of r1

**Objects.** `S3-U1-r2.md` (SHA-256 `985f681e…9783`) and `RESPONSE-S3-U1-r1.md` in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at PR #1294 head
`134dcc970c199b62bb3f76db55b5c360a62b127f`. Cited below as `r2:§`.
- `S3-U1-r1.md` is unchanged from `e7f4db9d` (byte comparison).
- `REVIEW-S3-U1-r1.md` is retained byte-identical to the reviewer's file. Its SHA-256 matches the
  README row.

**Corpus.** `origin/main` `dfeec843`; SEL-EXCL-1 at `0ecfddeb`; the GitHub records named below,
read through the API.
**Reviewer.** The same separate non-author reviewer as for r1. Read-only.

## Verdict: ACCEPT WITH CHANGES

r2 resolves B2 and most of B1, and it resolves R1–R3, R5–R7 and all ten optional findings, the
correction of the "bare model" placement included. The response's dispositions match the text.

One problem is new, introduced by the B1/R4 fix. The Q1 working definition is quoted faithfully, but
it is applied to C-INT's I-sel. I-sel is an operational class that C-COMP, AD-1(e) and the first
missing step for intervention use as a **requirement**. Under r2's formalization the Q1 test is
satisfied trivially whenever the carrier is held, so it withholds I-sel from every operation on a
held carrier, not only for `T`. My r1 R4 asked for Q1 to enter C-INT in loose terms ("for example,
I-sel is withheld when …"), and r2 followed that suggestion. The defect is therefore partly the
review's.

The fix is bounded and has three parts:
- separate the operational class from the informational label to which Q1 applies;
- correct the two places that depend on the conflation (N1 and N2);
- correct one overstatement about adaptivity that r1 carried and my r1 review missed (N3).

A focused check of r3 is sufficient.

***

## 1. Disposition of the r1 findings

| Finding | Status | Note |
|---|---|---|
| B1 | **Partly resolved** | The unsourced carrier clause is dropped, following S-C1(a)'s quantifier (MR★:501–503). The flag is applied to `T` with the correct averaging. The three-row table of alternatives (r2 §5.1(iv)) is correct row by row. AW-3 is reclassified BORDERLINE and is author-side and off `main`. The frozen row rests on the Q1 application of N1 |
| B2 | **Resolved** | The comparison tick `t_c` is in §2.1, G4, S-A7, C-PREP, C-SET, C-REC (R5) and C-RET. AW-4 and K-4 are updated. See §3 below |
| R1 | **Resolved**, one residue (N5) | Four outcomes (r2 §2.3); K-1(iii) is consistent with SNR-1 (PLAN:784–797) |
| R2 | **Resolved** | The divergence is stated where it is made; "every record meeting R2 meets C-RET" holds for `t_c ≤ T`. AW-6 is added and owner question (3) is added |
| R3 | **Resolved** | "Not excluded … undecided on K1 … not sourced". Q-b1 is [NP], and the citation now runs to :917 |
| R4 | **Partly resolved** | Q1 is applied and quoted verbatim, but it is over-applied (N1) |
| R5 | **Resolved**, one residue (N2) | "Bare model" is defined, and Interfaces A and B match DEPS:275–282. D-iv is moved out. The two halves are reported, with the soundness reason |
| R6 | **Resolved** | "a named source", with both verdicts |
| R7 | **Resolved**, residues (N4, N6) | Nine choices are tabled. D7 is quoted with its antecedent (OA1:204–205), and AD-1(e) is re-grounded on G1 |
| O1–O9 | **Resolved** | O1: matches `git diff --stat d8b74527 7086bd30`. O3: OA1:328 is "Visible carriers. Native, by a visible herald, at the D3 cost" (N1-K). O6: SPEC:205–208 is correctly used |
| O10 | **Resolved** | See §4 below; an optional addition is N8 |

## 2. Q1: faithful in wording, over-applied in use

**The source.**
- The quotation matches the owner's text at #1007 c.6719788955 (`amaybaum`, 2026-11-08T09:25:24Z):
  "A common refinement that is genuinely available through the declared native access interface,
  under the same preparation, should withhold the setting-controlled-interaction label. Do not award
  the label merely with a qualification flag. This is a working definition, not a proof that such a
  refinement physically exists."
- That decision adopts "the proposed conservative rule, subject to the stated access assumptions".
- The proposal answered is quoted in the retirement packet (#1007 c.6719401889, §4, from #1009
  c.6559049909 §6): "**Garbling under some π, and (A6)(b).** Should a common refinement supplied by
  Acc (a continuation re-read, or an in-window operation) withhold, as proposed? The alternative is to
  award with a flag, which would mean 'garbling under every π'."
- So Q1 governs NC-1's *setting-controlled-interaction label*. That label concerns whether the
  readout experiments under different settings are garblings of one experiment that the access
  supplies. It is an informational label.

**N1 (required). Q1 is applied to an operational requirement, and the test is degenerate on held
carriers.**
- *How r2 states the test.* r2 §4.3 states the Q1 test on "a common refinement of the partitions"
  that I-sel compares. These are partitions of the carrier's own content, with every other region
  fixed. A record of the carrier itself refines every partition of the carrier's content.
- *Consequence.* Whenever the carrier is held at the tick of use, I-sel is withheld, whatever the
  gate does. C-SET requires every setting to be held, so no setting–setting operation is ever I-sel;
  r2 states this itself ("a setting acting on another setting never earns I-sel under Q1"). The same
  holds for every operation on a visible or otherwise held carrier, for example a controlled swap of
  two held cells. Only operations on carriers not held, such as a quantum reference's setting acting
  on an unknown system, can earn I-sel.
- *Why the label's use matters.* For NC-1's informational label this is close to Q1's intent:
  nothing is learned about a system whose state is already held. But r2 uses I-sel as an operational
  requirement in three places:
  - C-COMP's timing clause ("A schedule that depends on records needs I-sel") and its adaptivity
    clause ("that is, I-sel");
  - AD-1(e), where a setting-dependent read is "classified under C-INT";
  - the first missing step for intervention ("a rule with I-sel, passing the Q1 test").

  With Q1 in place, a record-selected operation on held data cannot satisfy those requirements,
  however `φ` acts. That is a coverage effect produced by the definition. It falls on the classical
  fragment too (SEL-EXCL-1 l. 83 requires that fragment to be kept).
- *K-1.* Q1 does not make PR vanish: it classifies, and it removes no PR program directly.
- *K-2.* As frozen, the definition exempts setting–setting coupling by construction, and that is the
  class DEPS X5 identifies as the PR mechanism ("remote-setting dependence"; compare Main:412's
  "one wing's response depends on the remote setting"). Settings acting on carriers that are not
  held, the quantum measurement pattern, remain exposed. Any later restriction stated on I-sel would
  then reach the quantum references and miss `T` by definition. That asymmetry comes from a
  formalization choice, not from a source.
- *Fix.*
  - Keep **operational I-sel** without Q1, and use it in C-COMP, AD-1(e) and the first missing step.
  - Apply Q1 only to a separately named **informational label**, in the sense of NC-1/O-SET, which
    is where the corpus applies it.
  - State that label on readout experiments, as Q1's source does: garbling under the declared
    access and the same preparation, with the access-supplied refinement of Q1's question (a
    continuation re-read or an in-window operation). Do not state it on fixed-rest partitions of the
    carrier's content, which a held carrier refines by itself.
  - Cite c.6719401889 / c.6559049909 for the question Q1 answers.
  - Move the formalization into §5.2's table of U1's own choices (N6).
- *Effect on the PR gate.* The frozen row of the §5.1(iv) table becomes: `T` is operationally I-sel
  (carrier `y`, `x` selecting), and its informational label is withheld by Q1. A restriction on
  setting-selected operations then reaches `T`. Whether it also reaches the ontic parameter
  dependence of Main:412, and so fails AC-1, stays open, as r2 already says for its second row.
  AW-3 should be restated to match. BORDERLINE remains the right class.

**N2 (required, follows from N1).** r2 §5.3's table says "C-INT with Q1: Classifies only; it places no
program outside `Γ_exe`". That is contradicted by C-COMP's I-sel requirements under the frozen
definition. It becomes true once N1 separates the operational class (a requirement) from the
informational label (a classification only).

## 3. B2: the comparison-tick rule

- **Natural, and a requirement rather than an assumption.**
  - The rule asks that records compared jointly be held together, in present configurations, at one
    declared tick. The program must source the retention (C-RET) or the carrying (S-A6); nothing is
    assumed to be retained.
  - Where retention is unsourced, as on K1 (C-3 blocks C-4), the outcome is *unsourced*. That is not
    a negative under SNR-1.
  - It is target-neutral. It binds SEL-EXCL-1's `H_A^(i)` exactly as it binds a quantum reference's
    record sequence.
- **It does not exclude ordinary quantum sequential experiments.**
  - The quantum references enter AC-1 as target laws under `Θ` (PLAN SNR-1, "Target laws"). `Θ` (e)
    maps complete records, failures included, to complete outcome records (SPEC:379).
  - A laboratory sequential experiment is compared from retained records, so the rule asks of an OI
    model what the reference presupposes.
  - Records that a protocol erases by design, such as an eraser's marker, are not entries of the
    complete record, so the rule does not touch them.
  - The rule removes no program that a model executes with retention.
- **No new hidden assumption found.** The single global `t_c` presupposes global ticks, which the
  programs already use for schedules (C-COMP "timing"). That is not a new premise.

## 4. The S7(a) narrowing and the `Γ` outcome

- **Correct under both readings of S7(b).**
  - Derived reading: `Γ := Γ_exe`. An operation "typed into `Γ`" without execution through
    `(φ, Obs)` is supplied outside `(φ, μ, AD-1)`, which gives *requires assumed apparatus*.
  - Component reading: K-acc requires `Γ = Γ_exe` (SPEC:242). The same program outcome follows.
- **The `φ` branch.** "Criterion unchanged; P-L3 a model question (DEPS X3)" is right.
- **The `Obs` branch.** This is the one branch that needs AD-1 itself to change, so stopping there and
  only there is correct. Which typing applies is not chosen.
- **N8 (optional).** Add the second consequence under the component reading. A model whose `Γ` lists
  such an operation, not in `Γ_exe`, fails K-acc and so is outside C. This holds in addition to the
  program's outcome.

## 5. Other new points

**N3 (required; present in r1, missed by my r1 review). Adaptivity is equated with I-sel.**
- S-A2 is "Later settings may depend on the observer's own retained records and on private seeds"
  (SPEC:299–300). That is a record-conditioned write of a setting *value*.
- By U1's own partition test, the write `(h, z) ↦ (h, z ⊕ f(h))` (SEL-EXCL-1 l. 99) is a translation
  of the target `z`, so it is I-off.
- So the following overstate:
  - C-COMP's "adaptivity (S-A2): a record-conditioned write, that is, I-sel" (r2 §4.7);
  - "Not available at scope: adaptivity on R-lin" (r2 §4.7(iv));
  - §9's "adaptivity not available on R-lin [M-r]".
- OA-1 D5 (OA1:176–183) and S-C1(c) (MR★:508–509) concern *record-selected operations on a carrier*.
  They do not concern record-dependent setting values: a value written by an affine function of held
  records is not excluded by D5, and a value written by a non-affine function needs a non-affine
  write.
- Fix: split S-A2 into adaptive setting values (C-SET with a record-conditioned write) and adaptive
  operations (I-sel). Scope the R-lin negative to the second.
- Under SNR-1 this matters: as written, a negative would count at a wider scope than its source
  proves.

**N4 (optional).** r2 §5.3's coverage cell grounds "a laboratory record is held where it is read" on
"§A.24". That is the repository rule on external comparison, not a source for the statement. Ground it
on `Θ` (e) and K-rec (SPEC:379, :243), or mark it [A-inf].

**N5 (required, minor).** r2 §5.3: the criterion "places outside `Γ_exe` … programs whose outcome is
*unsourced*". An unsourced program is not shown to be in `Γ_exe`; it is not shown to be outside it.
Write "does not place in `Γ_exe`" or "leaves undetermined". This keeps R1's distinction.

**N6 (required, minor).** r2 §5.2 lists "the Q1 test (owner working definition)" among the clauses
taken from sources. Q1's wording is sourced. Its formalization in C-INT is U1's [P] and belongs in the
table of choices: the refinement taken over fixed-rest partitions, held at the tick of use, and
applied to I-sel. N1's fix changes it in any case.

**N7 (optional).** The r2 §4.3 G_SM row says "I-sel present in `φ` … Q1 not yet applied to it". After
N1 this becomes "operational I-sel present in `φ`". Until then it states a class that the frozen test
might withhold.

**Premises, status and references.**
- No new physical premise.
- No conditional result is stated as established. AW-3 is BORDERLINE, author-side and off `main`. Its
  frozen row is stated as relative to Q1, "not a proof".
- No hidden authorization. The closing line of §9 now disclaims it.
- §A.42 item 8: #1007 c.6719788955 is classified (within the #866 row, as governance). With N1's
  added citations, c.6719401889 and c.6559049909 should join that row as provenance. Main:412 is on
  `main`. No unclassified off-`main` reference was found.

## 6. Checked and not checked

- **Checked.**
  - The whole of r2 and of the response.
  - r1 unchanged; the retained review identical.
  - The Q1 owner comment, the proposal it answers and the original question.
  - OA1:320–352 (O3).
  - DEPS:273–285 (R5).
  - SPEC:203–209 and :378–380.
  - Main:411–412.
  - The `T` algebra under the three definitions in r2's table, re-derived by hand. All three rows are
    correct as stated.
- **Not re-checked.** Citations unchanged from r1, which were verified in the r1 review; Lean
  statements; the internal proofs of the records cited.
