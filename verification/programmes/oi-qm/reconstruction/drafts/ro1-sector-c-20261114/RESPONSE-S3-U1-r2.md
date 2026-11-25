# Response to the focused review of S3-U1-r2

**Review.** `REVIEW-S3-U1-r2.md`, on PR #1294 at `12447eb1`. Same separate non-author reviewer.
Verdict ACCEPT WITH CHANGES. It reviewed `S3-U1-r2.md` at `134dcc97`.

**Revision.** `S3-U1-r3.md`. r2 is left unchanged. Each finding was checked at its source before it
was applied. Status: unreviewed, and paper-only, under #1169 c.6890079967.

What does not change:
- No new premise is adopted.
- The S7 stop and the O11 stop stand.
- S5 stays separate, and H-RR stays a hypothesis.
- AC-1 and SNR-1 apply.

## Required

**N1. Scope of Q1. Accepted.** In r3: §4.3, §5.1(iv), §5.2, §5.3, §7 (AW-3), §8 and the inputs list.

- *What I checked.*
  - #1007 c.6719788955 (`amaybaum`, 2026-11-08T09:25:24Z) is the owner's Q1 text; r2 quoted it
    exactly.
  - #1007 c.6719401889 §4 (`amaybaum`, 2026-11-08T08:42:56Z) quotes the question it answers, from
    PR #1009 c.6559049909 §6: "Garbling under some π, and (A6)(b). Should a common refinement
    supplied by Acc (a continuation re-read, or an in-window operation) withhold, as proposed?"
  - In c.6559049909, that question governs NC-1's "setting-controlled interaction relative to
    Acc". NC-1's (A4) and (A6) are stated on the readout experiments `Φ_s^a`, and its owner rule
    reads "A garbling withholds the label at a; finding no garbling never awards it".
- *The defect.* The reviewer is right. r2 tested refinement of the carrier's own fixed-rest
  partitions. Any held carrier refines its own partitions, so I-sel was withheld from every operation
  on a held carrier. Yet C-COMP's timing and adaptivity clauses, AD-1(e) and the intervention action's
  first missing step all use I-sel as a requirement. The result exempted the setting–setting
  coupling that DEPS X5 names as the PR mechanism, while settings acting on unheld carriers stayed
  exposed. That asymmetry came from a formalization choice, not from a source.
- *The fix.*
  - C-INT now has two operational classes, I-sel and I-off. No refinement test applies to them.
  - Their selector is a setting or a held record.
  - Their carrier is any region other than the selector, as S-C1(a) has it.
  - Q1 applies only to a separately named informational label, INC, stated on readout experiments
    as in NC-1. INC is a classification only: no requirement uses it, and it places no program in or
    out of `Γ_exe`.
- *Consequence for `T`.*
  - `T` is operationally I-sel: with `y` as carrier, `x` selects whether `y` reaches `B`.
  - Its INC label is withheld by Q1. Bob holds `y`, and his readout experiments on `(B, y)` under
    `x = 0` and `x = 1` are garblings of each other.
  - A restriction on operational I-sel therefore reaches `T`.
  - Whether such a restriction also reaches Main:412's ontic parameter dependence, and so fails
    AC-1, is stated as **open**.
- *The §5.1(iv) table.* The frozen row now reads "I-sel; INC withheld by Q1 | Yes; AC-1 consequence
  open". r2's row is kept, marked withdrawn, with the reason.
- *AW-3.* Restated: to reach `T`, a restriction must cover selections whose carrier is a setting,
  which is X5's remote-setting dependence. It stays BORDERLINE, close to X5, and author-side and off
  `main`.
- *Provenance.* c.6719401889 and c.6559049909 are added to the inputs and to §8 as provenance. NC-1
  is classified as a proposal, off `main`.

**N2. §5.3's C-INT row. Accepted.** In r3: §5.3. The row now distinguishes operational I-sel, a
requirement, from INC with Q1, a classification only.
- Operational I-sel is used where C-COMP, AD-1(e) and the intervention action need it.
- It places outside `Γ_exe` nothing a model executes. Whether `φ` effects I-sel is a property of the
  rule (for example, D5 on R-lin), not of the definition.
- The soundness cell now states that a restriction on I-sel reaches `T`, and that the AC-1
  consequence is open.

**N3. Adaptivity overstated. Accepted.** In r3: §4.2, §4.3, §4.7, §7 (AW-7), §9.
- *What I checked.*
  - SPEC:299–300 defines S-A2 as settings that depend on retained records.
  - SEL-EXCL-1 l. 99's write `(h, z) ↦ (h, z ⊕ f(h))` is a translation of the target, so it is I-off
    under the partition test.
  - OA1:176–183 (D5) and MR★:508–509 (S-C1(c)) concern operations on a carrier.
- *The split.* S-A2 is now split:
  - *adaptive setting values*: a record-conditioned value write, I-off, under C-SET;
  - *adaptive operations*: a record-selected operation on a carrier, operational I-sel.
- *Scope of the R-lin negative.* It is restricted to adaptive operations, in the evidence rows and in
  §9. The text says that D5 does not exclude a value written by an affine function of held records,
  and that a value written by a function that is not affine needs a rule that is not affine.
- *First missing step.* C-SET's now names the blank target the value write needs.
- *AW-7.* Added, recording that a negative for "adaptivity" counts under SNR-1 only at the second
  scope.

**N5 (residue of R1). Accepted.** In r3: §5.3. The coverage sentence now separates three cases:
- the criterion places in `Γ_exe` only programs whose outcome is *available*;
- it places outside `Γ_exe` programs that *require assumed apparatus*, programs that are *not
  available*, and representable-only programs;
- it leaves *unsourced* programs undetermined: not shown to be in `Γ_exe`, and not shown to be
  outside it.

**N2 (residue of R5).** This is the same item as N2 above. The review numbers it once; it is
answered there.

**N6 (residue of R7). Accepted.** In r3: §5.2.
- Among the clauses taken from sources, the entry now reads "the wording of Q1 … and of NC-1's
  question".
- The table of U1's own choices gains three rows:
  - the formalization of operational I-sel, by fixed-rest partitions, with its selector and carrier;
  - the formalization of INC and of Q1's application to INC only;
  - the split of S-A2.

  Each row states its ground, and each is marked "No" for reference to an outcome.

## Optional

| # | Disposition | Reason |
|---|---|---|
| N4 | Applied (§5.3) | §A.24 is a repository rule, not a source for the statement. The cell is now grounded on `Θ` (e) and K-rec (SPEC:379, :243) and marked [A-inf] |
| N7 | Applied (§4.3) | The G_SM row now reads "operational I-sel present in `φ`, inputs unsourced; INC not assessed" |
| N8 | Applied (§6.1) | I agree: under the component reading of S7(b), a model whose `Γ` lists an operation not in `Γ_exe` fails K-acc (SPEC:242), and so is outside C, in addition to the program's outcome |

## Kept, as instructed

- **The comparison-tick rule from B2.** Unchanged. The reviewer's §3 finds that it adds no hidden
  assumption and does not exclude ordinary quantum sequential experiments.
- **The S7(a) narrowing.** Kept. r3 §6.1 now opens with a paragraph that states the narrowing so that
  it can be reverted:
  - r1 stopped for every typing; r2 narrowed the stop to the typing into `Obs`; the review of r2
    confirmed the narrowing;
  - the owner has an open question on whether to keep it;
  - if it is reverted, the stop covers all three typings again, and the verdicts for the `φ` and `Γ`
    typings are kept only as conditional statements.

  The question is added to owner question (1), and §9's verdict notes that the narrowing can be
  reverted.

## Not changed

- The verdict: criterion delivered with one named stop.
- AD-1.
- The four outcomes.
- C-PREP, C-REC, C-RET and C-REN, apart from cross-references to the S-A2 split.

## Not checked in this revision

As in r1 and r2, not re-checked here: the Lean statements; the internal proofs of MR★, OA-1, Theorem
N and REPORT.md; and whether Theorem N's criteria are at least as weak as C-RET's.

Also not checked: NC-1's remaining clauses (A1)–(A3) and (A5). INC records only the Q1 component and
NC-1's owner rule, and makes no claim under the other clauses.
