# Q-868-H unit 1: dispositions of the r2 review findings (r2 → r3)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-13).** This is a change note, not a review. Nothing is
adopted. No git or GitHub write was made, and no probe was run.

- **r2:** `Q868H-UNIT1.md` at `82f592db3a0a36f118bf693805be5d1322e32b1e` (branch `research/q868h-868-20261113`),
  sha256 `1e128f286b14be3294cb8411e21f0b4b4516cbc9985fc2589fb6362a752179e6` (verified).
- **r3:** `Q868H-UNIT1.md`, sha256 `2d900ccc87101b540ceaf80269884d1b85d6a8fd1f44cab6b77318e404a53932`. The change is the diff of
  `r2/Q868H-UNIT1.md` against `Q868H-UNIT1.md`.
- **Review:** the fresh independent review of r2 at `82f592db` (model-written, 2026-11-13; `review/REVIEW-Q868H-UNIT1-r2.md`, sha256
  `651612e89c964c05bbc31d7b47c67cbb855456622b8eaee98bf3c79d9865268e`). Verdict ACCEPT WITH CHANGES; required changes
  RC1–RC5; optional suggestions O1–O7. Line numbers below are r2's, as the review cites them.
- **Owner decision:** amaybaum, 2026-11-13, #868 c.6853568040 (posted 2026-11-13T12:55:08Z): "r3; ratify the probes",
  recorded there as "This session writes r3 with RC1–RC5. The owner retroactively ratifies the unit's generic
  linear-algebra probe scripts as covered, and r3 records that decision." The same record states "Not authorized:
  any other computation, new premise, execution or merge."
- **Sources re-read:** Main §3.3 (`fd539e15:papers/Main.md`, :400-410); AP1 ledger rows P1–P3 (:419-421) and checks
  C1, C4–C9 (:674-682); #868 c.6742050189, #1210 c.6739250392 and #1211 c.6739843458 (`gh api`). Each RC was checked
  against these and against r2 before it was applied.

The verdicts are unchanged: **(V) PASS, (C) PASS conditional, QC FAIL**, now with (iv) listed for (C) and NNB carried
in the QC headline. No premise, witness or computation is added.

***

## Required changes

### RC1. What QC FAIL rests on (§0, :68-70). **Applied as specified.**

Verified: under the stated access E2 is type 2 with `pp` undetermined (§4; QC-1, −1/4), and E4 without `τ_Y` is
SWAP/2 with `pp = 0` determined (§4; QC-3, −1/2). Either alone fails QC by the §6.1 map, so r2's "does not carry the
verdict on its own" was false for the stated class, and "rests on QC-2" was not exclusive, since QC-4 also holds on
every native state (§6.2). The review's new text replaces r2's three sentences verbatim. The paragraph was reflowed
together with O2.

### RC2. (C) uses (iv) (§0 :55-56; §5.2 :319). **Applied as specified.**

Verified: K1's uniform law within a branch conditions on settings (§1, "A *branch* is the conditional law given every
record, supply herald and setting"), which needs the configuration law to be independent of the settings: Main §3.3
(iv), retained there as a posit (Main:406-407). The review's counterexample without (iv) (A's read choice tied to
`f_z^A(s)` on E4) puts B at `(±1, 0, ±1)`. §0 now reads "E-iso, WL, H-PREP and (iv) via P3"; the §5.2 heading reads
"E-iso, WL, H-PREP, (iv) via P3; NNB for the Y read". No other change: QC FAIL is existential and needs no such
condition.

### RC3. QC FAIL carries NNB (§0 :65; §11 :657). **Applied as specified.**

Verified: QC-1 and QC-2 need NNB for `H`/`S`, QC-3 and QC-4 need it to read Y or to conjugate across wings (§6.2), and
tier N is a non-selective pass (§6.5). §0's headline now reads "FAIL** (with NNB carried)"; owner question 3 now reads
"QC fails for U′ composites with NNB carried (including under premise I)". §0's K2-route sentence and §6.4 already
carried NNB and are unchanged.

### RC4. "No native witness" scoped to class level (§0 :90-91; §7 :520-521). **Applied as specified.**

Verified: §7's argument is class-level (each class considered contains E4 without `τ_Y`, i.e. SWAP/2, so no class has
QC). Both sentences now say "No native class-level witness exists"; §0 adds "since each contains SWAP/2". The native
property-level witness the review sketches is not added (O5).

### RC5. The generic-check permission (header :17-18). **Applied, modified as the owner decided.**

Verified: c.6742050189 says "No computation" with no carve-out; the #1210 and #1211 rulings name other units and
predate the Q-868-H question. The review's proposed text attributed the unit's reading to those rulings and added
owner question 4. The owner has since answered (c.6853568040). r3 therefore:
- states that the authorization says "No computation";
- quotes the owner decision "r3; ratify the probes" with author, date and comment id, and the record's sentence that
  the owner retroactively ratifies the unit's generic linear-algebra probe scripts as covered;
- identifies those scripts as the two probes of §10, and states that the same record authorizes no other
  computation;
- drops the citations of #1210 c.6739250392 and #1211 c.6739843458;
- does not add owner question 4.

The rest of the header bullet (probes encode no OI rule; preparations enumerated by hand) is unchanged.

## Optional suggestions

### O1. QC-2 eigenvalue for mixtures (§0 :77). **Applied.**

Checked by hand: for `(I + XX + ZZ + vYY)/4` the Bell-basis eigenvalues are `(3 − v)/4`, `(1 + v)/4` (twice) and
`−(1 + v)/4`; the two paths give `v = ±u`, so the worse one has `−(1 + |u|)/4 ∈ [−1/2, −1/4]`. §0 now reads
"eigenvalue −1/2 or −1/4 per branch, and at most −1/4 for mixtures".

### O2. Φ⁺ reachable as a product-test table only (§0 :66-68). **Applied, modified (placement).**

Checked against QC-4 and QC-3: E3/E4's Φ⁺ table has `pp = 1`, so the Mermin–Peres row sum is 1 with certainty where QM
gives 0, and `τ_Y` (the partial transpose on A) takes the Φ⁺ table to SWAP/2. "as a product-test table only" follows
"natively reachable on some branches", as suggested; the qualifying clause is a separate sentence after the E3/E4
clause, so that the Lemma P sentence stays whole.

### O3. (iv) is a posit; P3 only carries the settings (§0 :50; §2.4 :208). **Applied.**

AP1:421 states that P3 loads coefficients from a classical controller and that "the setting selection rests on it";
Main:406-407 retains (iv) as a posit. "supplied here through P3's external controller" is replaced at both sites by
"carried (here) as a posit; the settings enter through P3's external controller". The shorthand "P3 with (iv)" and
RC2's "(iv) via P3" are kept, as the review specifies them.

### O4. Unpreserved second run of the r2 probe (§10 :603). **Not applied.**

Outside the optionals this revision was instructed to consider. The clause "a second run is byte-identical" has no
preserved output (`OBJECTS.md` lists runs 1–3). Resolving it means either preserving that output, which would need a
run, or dropping the clause; that choice is left to the owner or the focused confirmation.

### O5. Native property-level witness of QC ⇏ (C). **Not applied.**

It is a new hand construction (a sharp carrier from AP1 C9 or SA-1(c) removal, mixed with `Λ_0` at weight 5/8) and,
as the review notes, would need its own review. RC4 scopes the existing sentence instead.

### O6. `GENERIC` in the preserved probe docstrings. **Not applied.**

The probe files are byte-preserved; their bytes are not changed. The suggested record of an accepted substitution
belongs to a landing-time SC-42 run, not to the unit text.

### O7. Heralds by non-Pauli native reads on A (§6.0). **Applied.**

§0 already states that every remote herald lies in the cube cone; §6.0 derived it from product tests only. A bullet
now gives the argument for raw parity-cell, ancilla, mediator and multi-record reads on A: their kicks change only A's
slots (E-iso, WL), so B's later read records `f_b^B(s)`, and conditioning on A's records reweights the law of `s`. The
r1 review confirmed the same point. It uses no premise beyond those (V) already lists.

## Unchanged

- The preserved files (`r1/`, `probes/`, `DISPOSITIONS-r2.md`) are not touched. The review of r2 is added under `review/`, r2 moves to `r2/` with its bytes unchanged, and `OBJECTS.md` gains the r3 rows.
- §A.42 item 8: the two off-`main` support gaps the review lists (ASSESS-868 r3a; the [D] framing behind §8's last
  bullet) are unchanged by this revision. r3 adds one reference, #868 c.6853568040, an authority record.
