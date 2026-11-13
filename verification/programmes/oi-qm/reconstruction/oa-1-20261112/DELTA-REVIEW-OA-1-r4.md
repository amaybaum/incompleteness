# Focused delta review of OA-1 r4 (r3 → r4)

**Reviewer standing.** Independent, read-only, paper-only. No computation on any OI rule. No commits, pushes or
GitHub writes. Under the owner's decision of 2026-11-13 (#1169 c.6841795465, "Run all three (Recommended)"), the
r3 reviewer's waiver of a further round does not cover the r3 → r4 edits. This review covers those edits only.

**Text reviewed.**
- `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r4.md` on branch
  `research/oa1-w1-1-20261112` at `5fec096645b5a201af3ce37c0a60538e8407a365`.
- Blob `41a1fb79cc640f3b5347ce5071d43d089e967e24`, SHA-256
  `87e60622480fa3c35a01e38714bb0b6d965134308d059b036817926ce196d291`, 699 lines. This is the same blob at
  `066be3b1d` and as recorded in `OBJECTS.md:17`.
- Baseline: r3, blob `dd7ed08d780c20dbdc6f68ec175b1c6067f6d671`, which is unchanged. The diff has 11 hunks
  (+66/−16).
- Requests: `REVIEW-OA-1-r3.md`, blob `adfa30cd…`.

**Sources checked at `main@fb733b4a`.**
- `papers/Main.md:724`, ledger items (iv), (vii), (xiii) and (xiv); `Main.md:582`.
- `OIBridge/FrozenSourcing.lean:65–113` and `:290–330`.
- `apparatus-1-20261107/DESIGN.md:275–306`.
- `mechanism-2-20261108/DESIGN.md:40–125` and its P★ references.
- `minacc-1-20261108/RESULT.md:1–70`.
- `operational-quotient-v3/REPORT.md:1–30` and `:215–232`.
- r2 §4.2 and §9.
- #1169 comments 6829742537, 6829898892, 6831588323 and 6841795465, read through the GitHub MCP.

## Verdict: ACCEPT WITH CHANGES

- Nits 4 and 6 are applied correctly. Nit 6 needs one small change to a quantifier.
- Nits 1, 2 and 3 are applied as the r3 reviewer worded them, but each leaves a defect:
  - **Nit 1:** the new R-lin text overreaches. It turns a sufficient condition into a necessary one, and its
    unscoped "always needs a blank" contradicts r4's own status "N1-S under μ-O and μ-R: open". This is a hidden
    verdict move.
  - **Nit 2:** it cites P★ and `G_σ` as ingredients without the qualifiers their sources and r4's own tables
    carry.
  - **Nit 3:** the fix reached the §2A table but not the body or §6.
- Nit 5 is now stale (§10A).
- The Standing block does not say that r4 is unreviewed.

All the required edits are wording and scope changes. None needs a new derivation. Once they are applied, a
focused re-check of the edited lines is required, because a waiver does not count.

Recommendation: apply the edits as a new file, `OA-1-REPORT-r5.md`, and leave r4 byte-identical. OA-2 r1–r3 cite
`OA1r4:n` line numbers at `066be3b1` (:172–204, :421, :439–441, :515). Editing in place would shift every line
after :268. None of the edits below changes the content at those cited lines.

***

## 1. Accounting for every delta hunk

| # | r4 lines | Hunk | Disposition |
|---|---|---|---|
| H1 | :1–13 | Title "r4"; new "Standing (r4)"; "Standing (r3, retained)" | **F6**: no "unreviewed" status; the retained r3 block and the Disclosure (:49) are stale |
| H2 | :267–268 | §2A: N3 split into fixed read and backaction (nit 3) | Table correct. **F3**: not propagated to body :382 or §6 :596; citation :298–303 should be :297–299 |
| H3 | :331–341 | N1-S, R-lin refinement (nit 1) | Algebra correct. **F1**: necessity overreach and an unscoped "always" |
| H4 | :473 | §4.1 `FrozenSourcing.lean:74` → :79, :84, :99, :327 (nit 4) | **Verified**: :79 `permTheory_nonnegBounded`, :84 `obsTheory_nonnegBounded`, :99 `nonnegBounded_not_phasesAvailable`, :327 `nonnegBounded_verdict` |
| H5 | :489–505 | §4.2 claimed-supply table restated (nit 6) | Matches r2 row by row, except: "Main:582" added (verified); "(R1)" → "(relative to R1)"; "all" → "everything"; "error ≥ 1/15" → "error ≥ 1/15 non-Clifford" (**F5**) |
| H6 | :513 | Gap-1 row (nit 1) | **F1** (same overreach) |
| H7 | :563–572 | MP-1 "not by itself a route" (nit 2) | The wording change is correct, and the ledger (vii) gauge-step bullet is verified at Main:724. **F2**: P★ and `G_σ` qualifiers missing; 5c listed against U2 |
| H8 | :592 | §6 row (nit 1) | **F1** |
| H9 | :616–619 | §7 pressure test (nit 1) | **F1** ("always a blank requirement") |
| H10 | :657–665 | §10A heading and provenance (nit 5) | **F4**: stale. Recorded on #1169 c.6831588323 and authorized there as OA-2 |
| H11 | :689–699 | §12 change table | **F6**: "no verdict moved" is inaccurate for §2A's N3 backaction cell and, until F1 is fixed, for N1-S under μ-O and μ-R |

***

## 2. Findings

### F1 (substantive). The R-lin selection condition: necessity overreach and an unscoped "always"

**The hand derivation holds.**
- Main:724 (xiii) gives `(x(t−1), x(t)) ↦ (x(t), F(x(t)) − x(t−1))`, and §3.2 instantiates it with `F` the
  nearest-neighbour sum. So for carrier `i` with the setting at neighbour `j₀`:
  `x_i′ = s + m`, where `m := Σ_{j∈N(i)∖{j₀}} x_j − y_i`.
- E-iso (apparatus-1 :305–306) restricts which edges couple. It leaves the second-order term, so an isolated, armed
  cell gives `k s − y_i`. "Isolation does not remove `−y_i`" is correct.

**Overreach 1: sufficient presented as necessary.** At :338 r4 says "R-lin therefore selects **only if** the
carrier's previous slot is known **and** the other neighbours are known or isolated."
- What is necessary is a condition on the combination `m`, not on each term:
  - an exact write, up to a known shift, needs `m` to be known;
  - N1-S's own infrastructure tier (:128: the laws differ for two values of `s`) needs only that `m` is not
    uniform given what is held.
- A known `y_i` together with known or isolated neighbours is one sufficient route. A held record of the combination
  `m` would also do.
- This is a necessary/sufficient boundary violation (Code Review Rules, claim/evidence boundary).

**Overreach 2: "The first condition always needs a blank cell (MP-0a)" (:339).** The same claim appears as "a
blank, MP-0a" at :513, "(blank)" at :592 and "always a blank requirement" at :618. It is unscoped.
- **Under μ-G, for a hidden carrier, it holds.** By D2, `y_i ∈ H_t` is uniform and independent of everything
  held, so `m` is uniform and `x_i′` is uniform for every `s`.
- **Under μ-O and μ-R it is not established.** r4's own N1-K result (:317–320, the swap) shows that a hidden value
  can be fixed by the present configuration with no blank.
- So "always" makes N1-S for R-lin not native under every measure. That contradicts r4's own statements that N1-S
  under μ-O and μ-R is **open**: §2A :265, :348, §6 :591 and §10 :644. It is a verdict move that §12 and the
  Standing block deny.
- **For visible carriers** (:350, "Native"), the previous slot is held whenever the visible cell's configuration
  includes it, so "always" also conflicts there.
- **Other ready-cell supplies.** A half-known ready cell (SA-1(c), P2) whose known functional is `y_i` would also
  supply the first condition. "MP-0a" is therefore one ready-cell supply among others, not the only one.

This entered through the r3 reviewer's own nit 1 ("a blank (MP-0a) in every case"), and r4 applied it faithfully.
The waiver gate exists for exactly this case.

### F2. MP-1's ingredient bullet drops source qualifiers (:568–570)

- **P★.** "MECH-2's nonlinear conditioning gives the non-stabilizer state P★" leaves out what the source says:
  "A non-stabilizer state appears only in a C-CP-failing instrument" (MECH-2 :96–98, relative to R1, :61–64). r4's
  own §4.2 row (:498) and R5 row 5c (:420) carry that qualifier. P★ is also the name of the instance or protocol
  (MECH-2 :630–632, :763), not of the state.
- **5c.** Listing 5c as ground where the rule's form "stays a possible ingredient" needs U2's scope stated. Under R1
  every encoded unitary channel that a fixed bijection induces lies in `A_4 ≀ S_n` (MECH-2 :55–64), whatever the
  rule. The rule's form is therefore a possible ingredient only for other frames, or at record level.
- **`G_σ`.** The bullet says M-INACC "was tested on the nonlinear `G_σ`" but not the outcome, which is negative.
  `RESULT.md:41–53` shows Lemma Q(iii)'s protection failing and `u + v` determined in every record branch. r4's
  own R5 row 5d (:421) says "M-INACC not supplied by … `G_σ`". Cited without its outcome, a failed test reads as
  support for a positive "possible ingredient". The source is WIP/UNVERIFIED, so it needs the label [R] (§A.46
  item 7).
- **Verified.** "Under NC's hypotheses no dynamics escapes" (MECH-2 :109–110) and the gauge-step bullet (Main:724
  (vii): affine from amplitude-scale gauge invariance, with A5 stronger).

### F3. Nit 3 was not propagated (§A.25)

- **Body :382.** It still reads "Backaction: native, given half-known meters." By r4's own trichotomy (:114–117),
  a capability that needs a named posit (SA-1(c), P2) is "supplied under a named premise", not native. The §2A
  table (:268) now says this, so the body and the table disagree.
- **§6 :596.** It groups "N3 fixed read; N4 under P1, E-iso, MP-0a" as **conditional**, while §2A :267 and body
  :381 call the fixed read **native**, and backaction has no §6 row. The split in the table makes this
  inconsistency visible.
- **Citation.** SA-1(c) is apparatus-1 `DESIGN.md:297–299`. The cited range :298–303 starts mid-clause and runs
  into commentary.

### F4. Stale provenance and authorization in §10A (:657–669)

- **What r4 says.** :663–665 says the words are "not yet recorded on #1169; the coordinator will record them
  there". The heading and :667 say "not authorized".
- **What #1169 records.** c.6831588323 (amaybaum, 2026-11-12T17:55:41Z) records the question verbatim. The text
  matches :659–661 exactly. The same comment records the owner's answer, "Authorize paper-only unit", which made it
  unit **OA-2**.
- **Still true.** "Not part of OA-1."
- **Now false.** "Not yet recorded", "the coordinator will record" (a future promise in a record) and "not
  authorized".

### F5. Quantifier in the restated §4.2 table (:501)

"error ≥ 1/15 non-Clifford" can be read as a bound for every non-Clifford rotation. The source states it for **one
rational non-Clifford rotation** (op-quotient v3 REPORT :21–24, :218–227). r2 had "error ≥ 1/15", so the
qualifier r4 added widens the quantifier (witness → general).

### F6. Status text (Standing, Disclosure, §12)

- **No unreviewed status for r4.** "Standing (r4)" (:3–5) does not say that r4 is unreviewed or WIP/UNVERIFIED. The
  only WIP label is in the retained r3 block.
- **Retained r3 block.** :12, "unadopted until the r3 re-check", reads as current Standing, but the r3 re-check has
  happened.
- **Disclosure.** :49, "Nothing was committed, pushed or posted", is false for the committed blob
  (`066be3b1d`, draft PR #1265).
- **§12.** The heading says "no verdict moved" (also :4). The §2A N3 backaction cell did move, from native to
  premise-dependent. No gap verdict moved.
- **Outside the file.** #1169 c.6831588323 heads OA-1 "(reviewed, paper-only, not adopted)" with r4 as the full
  text and "the nits are applied in r4". That presents the r4 delta as covered by review. It cannot be fixed in r4;
  see §4.

Nothing in the r4 file calls r4 reviewed.

***

## 3. Required edits

Apply these to a new file, `OA-1-REPORT-r5.md`. Line numbers are r4's.

**E1 (F1), N1-S, :338–341.** Replace from "R-lin therefore selects only if …" to "… It is not affinity." with:

> R-lin writes `s` exactly, up to a known shift, when the mask `m = Σ_{j∈N(i)∖{s}} x_j − y_i` is known at the
> write. The carrier's held conditional law depends on `s` (N1-S) only if `m` is not uniform given what is held. A
> known previous slot together with known or isolated other neighbours is a sufficient way to fix `m`. Isolation
> (E-iso, a posit) removes only the neighbour terms. Under μ-G, for a hidden carrier, `y_i` is uniform and
> independent of everything held (D2), so `m` is uniform unless a ready-cell supply fixes `y_i`: MP-0a, or a
> half-known ready cell whose known functional is `y_i` (SA-1(c)). Under μ-O and μ-R, whether `m` can be known
> natively is open (N1-S open). The obstacle is ready cells, with isolation as an alternative only for the
> neighbours. It is not affinity.

**E2 (F1), gap-1 row, :513.** Replace "R-lin itself needs the carrier's previous slot known (a blank, MP-0a) and the
neighbours known or isolated" with:

> under R-lin the write is masked by the carrier's previous slot and the other neighbours; under μ-G, for a hidden
> carrier, unmasking the previous slot needs a ready cell (MP-0a), with the neighbours known or isolated

**E3 (F1), §6, :592.** Item cell:

> Selection writable in the affine class; under R-lin the write is masked by `Σ_{j≠s} x_j − y_i`. A known previous
> slot with known or isolated neighbours suffices. Under μ-G, for a hidden carrier, the previous slot needs a ready
> cell

**E4 (F1), §7, :618.** Replace "(always a blank requirement)" with:

> (under μ-G, for a hidden carrier, a ready-cell requirement)

**E5 (F2), MP-1, :568–570.** Replace the "In a changed identification (5c, 5d) …" bullet with:

> In a changed identification the rule's form is a possible ingredient only where the frame-relative results do not
> reach. Under R1 (5c), U2 places every encoded unitary channel that a fixed bijection induces in `A_4 ≀ S_n`,
> whatever the rule. MECH-2's nonlinear conditioning gives a non-stabilizer state (instance P★) only in a
> C-CP-failing instrument, relative to R1 (MECH-2 :55–64, :96–98) [R]. At record level (5d), M-INACC (a functional
> the fixed rule uses) was tested on the nonlinear `G_σ`, and the protection fails there: `u + v` is determined in
> every record branch (`minacc-1-20261108/RESULT.md:36–53`) [R].

**E6 (F3).**
- Body :382: "Backaction: supplied under a named premise, half-known meters (apparatus-1 SA-1(c), P2); under μ-G
  their heralds cost D3."
- §2A :268: change the citation to "apparatus-1 `DESIGN.md:297–299`".
- §6 :596: replace with two rows, "N3 fixed read | native (§2A) | [W]" and "N3 backaction (half-known meters,
  SA-1(c)); N4 under P1, E-iso, MP-0a | conditional | [R] / [W]". If the fixed read is meant to be conditional,
  change §2A :267 and body :381 to match instead. Either way the three sites must agree.

**E7 (F5), §4.2, :501.** Replace "24 Clifford; error ≥ 1/15 non-Clifford" with:

> 24 Clifford; error ≥ 1/15 for one rational non-Clifford rotation

**E8 (F4), §10A, :657–669.**
- Heading: "## 10A. Next question (owner's words; recorded on #1169; a separate unit, OA-2; not part of OA-1)".
- Provenance paragraph:

  > These are the owner's words, given in the coordinating session chat on 2026-11-12 and recorded verbatim on
  > #1169 in comment 6831588323 (amaybaum, 2026-11-12T17:55:41Z). That comment also records the owner's
  > authorization of a paper-only unit on this question, OA-2.

- :667: replace "It is recorded as the recommended next question. It is not authorized and is not part of OA-1."
  with "It is not part of OA-1." Keep "It sits at the open ground …". Replace "Any unit on it would need its own
  owner scope." with "It is scoped separately as OA-2."

**E9 (F6), Standing and §12.**
- New Standing (r5): "WIP / UNVERIFIED. r5 applies the required edits of `DELTA-REVIEW-OA-1-r4.md`. r4 was not
  covered by the r3 reviewer's waiver (owner, #1169 c.6841795465, 2026-11-13). Paper-only and unadopted. r1–r4 are
  unchanged."
- Remove "until the r3 re-check" from the retained r3 text, or drop that sentence.
- Disclosure :49: "Committed on draft PR #1265 (branch `research/oa1-w1-1-20261112`); nothing is landed on `main`
  or adopted."
- §12/§13: "no gap verdict moved. §2A's N3 backaction cell moved from native to 'given half-known meters (posit)';
  the R-lin condition is stated for `m` and scoped to μ-G (N1-S under μ-O and μ-R stays open)."
- Add `DESIGN.md:297–303`, `RESULT.md:36–60`, `FrozenSourcing.lean:79–113` and op-quotient v3 REPORT :1–30 to the
  §9 reading inventory as r4/r5 reads.

**Optional.** §11 R1 row :675, "(refined for R-lin: known or isolated neighbours)", describes r3's change and is
accurate as history. Adding "; further refined in r4/r5, §12" would stop it being read as current.

***

## 4. Outside the file (not an r4 edit; for the coordinator and owner)

- #1169 c.6831588323 calls OA-1 "(reviewed …)" with r4 as the full text. Once r5 and its re-check are done, a
  follow-up comment should record that the r3 → r4 delta was reviewed separately (this review), with its verdict
  and the re-check outcome. Posting it is a GitHub write and outside this review's authority.
- OA-2 r1–r3 cite OA-1 at `066be3b1` (`OA1r4:n`). Those citations stay valid if r4 is left unchanged. E1–E9 do not
  change the content at OA1r4:172–204, :421, :439–441 or :515.
- Edit E1 changes how R-lin selection is stated, and any downstream text that relies on "R-lin selection always
  needs a blank" inherits F1. `git grep` at `5fec0966` for "previous slot", "own previous" and "N1-S" over
  `reconstruction/` outside `oa-1-20261112/` found no such reliance in OA-2 or OA-3. The OA-2 delta review should
  still check this.

***

## 5. Checks performed

- Each hunk was compared with `REVIEW-OA-1-r3.md` nits 1–6.
- R-lin algebra re-derived by hand from Main:724 (xiii). Under μ-G with a hidden carrier, `y_i` uniform and
  independent of everything held gives `m` uniform, so `x_i′` is uniform for every `s` (D2).
- Kernel lines read directly: FrozenSourcing :74, :79, :84, :99, :327.
- The restated §4.2 table was compared cell by cell with r2 §4.2.
- Quotations checked: Main:582, MECH-2 :96–98 and :109–117, minacc-1 RESULT :36–53, op-quotient v3 :21–24.
- #1169 comments read for provenance (F4, F6).
- No computation on any OI rule.

***

## Recheck of r5

**Text rechecked.**
- `scratchpad/oa1/OA-1-REPORT-r5.md`: blob `29af14191b6f4707225e321db0aa387e4a78c8e5` (verified by
  `git hash-object`), 731 lines, uncommitted.
- Against r4: `scratchpad/oa1/OA-1-REPORT-r4.md`, blob `41a1fb79…` (verified unchanged).
- With the writer's record `OA-1-r5-APPLY.md`.
- Read-only and paper-only, as before.

### Verdict: ACCEPT WITH CHANGES

E1–E5, E7, E8 and E9 are applied verbatim and in the right places. E6 is applied verbatim too, but **the E6 option
the writer took was my error**: §6's fixed-read status went from conditional to native without support (R-a below).
The remaining edits are a stale title, one stale Standing phrase and an ambiguous inventory line. Apply R1–R7 to r5
in place, since r5 is uncommitted and nothing cites it. Then re-check only the edited lines.

### (1)–(2) The diff, r4 → r5

`diff` shows 17 change blocks. Each maps to E1–E9, except the appended §13 (:716–731) and the coordinator's sentence
"Its edits await a focused re-check." (:5). Nothing else changed. The writer's claim that OA-2's cited r4 content is
byte-identical in r5 is consistent with the diff: no block touches r4 :172–204, :421, :439–441 or :515.

| Edit | r5 lines | Exact text? |
|---|---|---|
| E1 | :342–349 | yes |
| E2 | :522 | yes |
| E3 | :604 | yes |
| E4 | :631 | yes |
| E5 | :577–582 | yes |
| E6 | :390–391, :272, :608–609 | yes, but see R-a |
| E7 | :510 | yes |
| E8 | :673, :679–685 | yes |
| E9 | :3–5, :16, :53, :651–652, :705, :716–719 | yes |

### (3) Rulings on the writer's judgement calls

- **R-a. E6, two-row option ("N3 fixed read | native (§2A)"): not accepted; correct it (R3–R5).**
  - My E6 offered "native" as the default without checking it. That was wrong.
  - Under R-lin, a meter's new slot is the carrier's value plus the meter's other neighbours, minus the meter's own
    previous slot. This is the same second-order form as E1.
  - Under μ-G, a meter slot that is not known when the record is held is uniform and independent. It pads the
    record, which is then independent of the carrier. This is the one-time pad of r5 :326 ("a CNOT into a uniform
    cell gives a one-time pad").
  - Apparatus-1 obtains reads only from supplied half-known ready cells: SA-1(c) (`DESIGN.md:297–299`), P2 (:420),
    and the conjugate-slot statement at :321–325.
  - So the fixed read under μ-G is native only given a ready meter slot, at D3 cost. Under μ-O and μ-R, no
    derivation in the report establishes "native".
  - r4's §6 "conditional" was the supported status. The unsupported sites are §2A :271 and body :389, inherited
    from r3. They are corrected downward, and §13 records the change.
- **E6, §2A citation replaced wholesale, dropping "SA-1(c)": restore the label.** R3 does this in passing.
- **E8, italic lead-in kept: accepted.** It labels where the paragraph came from and is true.
- **E9, whole Disclosure line :53 replaced, bold label included: accepted.** The condition is that r5 is committed
  on #1265, as stated. If it is not committed there, the line must be revised.
- **E9, "§12/§13" read as both places: accepted.** §12's "no gap verdict moved" is accurate for r3 → r4.
- **E9, §9 inventory with bare file names: correct it (R7).** Three files in the corpus are named `DESIGN.md`, and
  the inventory is what bounds the report's negative claims. The bare names were my wording.
- **E1 line breaks: accepted.**

### (4) Rulings on what was not applied

- **Optional §11 R1 row:** may stay unchanged. It is accurate as r3 history.
- **"Standing (r4)", r5:8, "No verdict changes": correct it (R2).** It now contradicts §12's corrected heading
  "no gap verdict moved". F6 flagged it, and my E9 omitted it.
- **Title "OA-1 (r4)": correct it (R1).** It misidentifies the revision.

### (5) The writer's other points

- **Mask notation:** acceptable. E1 (`Σ_{j∈N(i)∖{s}}`) and E3 (`Σ_{j≠s}`) both index the setting cell as `s`.
  `j₀` appears only in this review. Harmonizing E3 to E1's form is optional.
- **r5:340, "s − y_i":** acceptable. R-lin's native coupling coefficient is 1, so `s − y_i` is correct for R-lin.
  F1's `k s − y_i` was the P3-armed form. No edit.
- **E5's `RESULT.md:36–53` against r4's :37–60:** acceptable.
  - :36–53 covers the `G_σ` construction and the (B-D) outcomes (`u + v` determined, :46–47 and :52–53).
  - The §9 read range :36–60 contains it.

### Required edits (r5 line numbers)

- **R1. :1.** Replace "# OA-1 (r4):" with "# OA-1 (r5):".
- **R2. :8.** Replace "No verdict changes;" with "No gap verdict changes;".
- **R3. §2A :271–272.** Replace the two rows with:

  > | N3 fixed read | only given a known meter slot (half-known ready meters, a posit: apparatus-1 SA-1(c), `DESIGN.md:297–299`; P2), at D3 cost; a meter slot not known when the record is held masks the record, as `y_i` masks the write in N1-S | not established | not established |
  > | N3 backaction | only given half-known meters, a posit (apparatus-1 SA-1(c), `DESIGN.md:297–299`) that costs D3 under μ-G | only given half-known meters (posit) | only given half-known meters (posit) |

- **R4. Body :389.** Replace "- Fixed read: native." with:

  > - Fixed read: under μ-G, only given a known meter slot (half-known ready meters, SA-1(c), P2), at D3 cost; a meter slot not known when the record is held masks the record, as `y_i` masks the write in N1-S. Not established under μ-O or μ-R.

- **R5. §6 :608–609.** Replace the two rows with one:

  > | N3 fixed read and backaction (half-known meters, SA-1(c), P2); N4 under P1, E-iso, MP-0a | conditional | [R] / [W] |

- **R6. §13 :718–719.** Append to the sentence:

  > N3's fixed read is stated as conditional on half-known meters in §2A, the N3 body and §6.

  Add a change-map row:

  > | Recheck R1–R7 | recheck of r5 | title :1; Standing (r4) :8; §2A N3 rows :271–272; N3 body :389; §6 N3/N4 row :608; §9 :651–652; this section |

- **R7. §9 :651–652.** Replace with:

  > Read for r4/r5: apparatus-1 `DESIGN.md:297–303`, minacc-1 `RESULT.md:36–60`, `OB/FrozenSourcing.lean:79–113` and op-quotient v3 `REPORT.md:1–30`.

**After the re-check.** Once R1–R7 are re-checked, replace ":5 'Its edits await a focused re-check.'" with a
statement of the re-check's outcome before r5 is committed.

***

## Re-check of R1–R7

**Text re-checked.**
- `scratchpad/oa1/OA-1-REPORT-r5.md`: blob `602fe3af4d340da613985c22281445964950e0ab`, 730 lines.
- Pre-R copy: `scratchpad/oa1/.r5-pre-R.md`, blob `29af14191b6f4707225e321db0aa387e4a78c8e5`.
- r4: `scratchpad/oa1/OA-1-REPORT-r4.md`, blob `41a1fb79…`, still unchanged.
- All blobs verified with `git hash-object`. Read-only.

### Verdict: ACCEPT, after two mechanical edits

R1–R7 are applied verbatim, in the right places, and nothing else changed. `diff .r5-pre-R.md OA-1-REPORT-r5.md`
has nine blocks:

| Block | Lines | Content | Exact? |
|---|---|---|---|
| R1 | :1 | Title "(r5)" | yes |
| R2 | :8 | "No gap verdict changes" | yes |
| R3 | :271–272 | Fixed-read row (μ-G: only given a known meter slot…, D3 cost, masking clause; μ-R and μ-O "not established"); backaction row with SA-1(c) restored | yes |
| R4 | :389 | Body "Fixed read: under μ-G, only given a known meter slot … Not established under μ-O or μ-R." | yes |
| R5 | :608 | One §6 row, "N3 fixed read and backaction (half-known meters, SA-1(c), P2); N4 under P1, E-iso, MP-0a \| conditional \| [R] / [W]" | yes |
| R6 | :717 | Sentence appended to the §13 summary | yes |
| R6 | :730 | Change-map row appended | yes |
| R7 | :650 | Inventory joined into one line with qualified names | yes |

**Lowered statuses (R3–R5).** The fixed read is now conditional at all three sites:
- §2A :271;
- N3 body :389;
- §6 :608.

No site still says it is native. The only remaining "fixed read (native)" is in §12's nit-3 row (:709), which
records the r3 → r4 change and is accurate as history. The backaction statements (:272, :390–391) are unchanged
apart from the restored label.

**Mechanical defect from my own R5–R7.**
- R5 removed one line and R7 joined two, so every r5 line cited in §13's change map from :608 onward is off by one
  or two.
- My R6 row repeated the old §9 range.
- Required: replace digits only, in the §13 table (:719–730):

| Row | Was | Now |
|---|---|---|
| E4 | :631 | :630 |
| E6 | "§6 N3 rows, :608–609" | "§6 N3 row, :608" |
| E8 | ":673", ":679–681", ":683–685" | ":671", ":677–679", ":681–683" |
| E9 | "§9 inventory, :651–652", "§12 heading, :705" | "§9 inventory, :650", "§12 heading, :703" |
| Recheck R1–R7 | "§9 :651–652" | "§9 :650" |

All other cited r5 lines in §13 (:3–5, :16, :53, :272, :342–349, :390–391, :510, :522, :577–582, :604, :271–272,
:389, :608) were verified as current.

These are digit-only edits to a change-map table. A `diff` confirming that only those cells changed is a sufficient
check, and no further review round is needed.

**Replacement for :5.** Replace "Its edits await a focused re-check." with:

> Its edits were re-checked in `DELTA-REVIEW-OA-1-r4.md` ("Recheck of r5", ACCEPT WITH CHANGES; "Re-check of
> R1–R7", ACCEPT once the §13 line numbers were corrected). The re-check lowered N3's fixed read to conditional on
> half-known meters. No gap verdict moved.
