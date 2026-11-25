# Review of S3-U2-r1 (independent, non-author)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U2-r1.md`
at PR #1294 head `ad83ee33cabfc966f18b0a67368112ba7ef9941d`. Cited `U2:N` below.

**Governing.** `S3-U1-r5.md` (blob `68983f86`, identical at `3ec1e465` and at the head; cited
`U1:N`), `S3-PLAN-r9.md` (`46ebc72d`), `RO1-SPEC-r3.md` (`76910fcf`), `RO1-DEPS-r4.md` (`a6326cbf`),
all unchanged between `3ec1e465` and the head (`git diff --stat` touches only README, U2, U4-SOURCES
and the VERIFY-SL3-CC pair). Corpus at `origin/main` `75cc5100`. Owner records #1169 c.6890079967,
c.6891241282, c.6891338304, read in full via the GitHub API (author `amaybaum`; times 06:02:00Z,
07:45:04Z, 07:54:33Z on 2026-11-15); U2's quotations of them are verbatim.

**Reviewer.** Claude, non-author. Read-only. No computation, Lean, commit, push or Issue change.
All checks below are by hand or by text read at the stated objects.

## Verdict: ACCEPT WITH CHANGES

No blocking finding. The per-program classification applies U1 as frozen. The gate algebra, the
μ-G herald argument, the CP-4 witness and Lemma L-1 check out by hand within stated hypotheses. Nine
required changes, all textual, narrow statements to what the argument reaches. None moves a verdict
from available to not available or the reverse. The most important ones: R1 on F-1's status, R3 on
L-1's hypothesis, R5/R6 on the AC-1 verdicts, and R4 on the unlisted outcome state "not in `Γ_exe`".

## Findings

### Required

**R1. F-1 is stated one level too strongly. It does not overturn SPEC:468 for "the stated tuple".**
- U1 does allow a setting's content to be "a datum of `μ`", with verdict *assumed* under a declared
  datum (U1:310–313, quoting OA1:111–112 "either an initial condition or written by `φ`"). A
  `μ`-assumed input "is not a producer" (U1:201–202). So U2 applies U1 correctly when it calls CP-1
  *available relative to `μ_PR`*. U1 is not silently changed (check 1 passes on this point).
- But `μ_PR` is U2's completion. SEL-EXCL-1 states no law for `(x, y)`: its settings are "freely
  chosen local setting labels" (SEL-EXCL-1 l. 17), "Alice chooses/records x" (l. 44). U2 says so
  itself (U2:110–113). SPEC:468 concerns "the stated tuple", which has no setting law. For that
  tuple SPEC:468's conclusion stands. What U1 changes is that the enlargement SPEC:469–473 asks for
  can be a **`μ`-level completion alone**: a booked setting law in `μ`, with `S` and `φ` unchanged and
  no setting writer. It does not make the enlargement unnecessary (U2:177 says "not needed").
- Status: CP-1 is in `Γ_exe` only relative to an assumed initial law that books the settings, the
  blanks and `r`. At U1's *derived* level CP-1 is not available in this tuple (§2.1, μ-G row), and the
  reason is the blanks/herald, not the setting. Under μ-G the settings are derived (U1:390–391). So
  SPEC:468's stated *reason* ("`T` writes no setting") fails at both levels, while its *conclusion*
  holds at the derived level and for the uncompleted tuple. SPEC:446's "executes no setting program"
  stays true: no setting is executed, it is sampled.
- Change: restate F-1 (U2:172–179 and the F-1 row, U2:472) along those lines. Reclassify it, or
  justify NEW. SPEC:318 states the written-setting requirement explicitly ("iff `M` executes the
  setting writes"), so it is not hidden. The finding is a U1-vs-SPEC inconsistency that U1's
  C-SET creates and that must be propagated to SPEC's next revision. ELABORATING (or CONFIRMING of
  U1:310–313) fits better than NEW.

**R2. `μ_PR` is not of MP-0a form as specified.** MP-0a is "fixed known values on designated cells,
independent of settings and carrier, **uniform elsewhere**" (OA1:359–361). U2 gives `(x, y)` "a
full-support law" (U2:110), which need not be uniform. Either fix the setting law as uniform, which
satisfies U1:308–309 and makes the MP-0a claim and its [M-r] non-import label hold, or drop the
MP-0a claim and book the setting law as a separate `μ`-datum with its own admissibility question
(ledger Q8).

**R3. L-1's hypothesis "or written from such a factor" is not covered by the proof.**
- *Re-derivation.* Binary setting factors `x, y`, binary output factors, `λ` the other factors with
  a law independent of `(x, y)`, deterministic `φ`. For a binary carrier `y`, the partition of
  `{0,1}` induced by `y ↦ b(x, y, λ)` is either trivial or discrete. Equal partitions for `x = 0, 1`
  give `b(1,·,λ) = b(0,·,λ) ⊕ c(λ)` in both cases. The symmetric step gives `a`, so
  `a⊕b = α(x,λ) ⊕ β(y,λ)`. CHSH depends only on `E_xy = E[(−1)^{a⊕b}]`, so it equals a local
  deterministic model's value under a setting-independent `λ` law, and Main:386–389's pointwise
  bound gives `≤ 2`. Correct. No counterexample is found within these hypotheses. The flagged case
  (outcome a non-injective function of a readable region, U1:441–445) is correctly excluded.
- *Gap.* If a setting is *written* at a later tick from a seed factor `u`, the I-sel test's selector
  and carrier are the seed factors (U1:414–419). Two problems follow. (a) If the seed is not binary,
  the "trivial or discrete" step fails. The step can be repaired: with a binary output, equal
  partitions still give `b(u_A,·) = b(u_A⁰,·) ⊕ c(u_A, λ)`. (b) The seeds belong to "every other
  factor", so `λ` as defined is then *not* independent of `(x, y)`. The bound then needs the
  independence condition at seed level: the non-seed factors independent of `(u_A, u_B)`, and
  `u_A ⟂ u_B`, so that `P(u_A | x, y) = P(u_A | x)` and likewise for `u_B`.
- Change: either restrict L-1 to settings that are binary factors of the initial configuration
  (unchanged to use, or copied injectively), or add the seed-level argument with the S5-type
  condition stated as a named condition. Hypotheses already explicit and correct: determinism,
  outcomes as contents of binary output factors, S5. Main:389 is the right anchor.

**R4. "Not in `Γ_exe`" is an outcome state U1 does not define.** U1 has four outcomes (U1:205–213),
and U2 adds two reporting states, *stop* and *target law* (U2:69–72). The verdict "not in
`Γ_exe(M-PR5)`" for CP-3 (`m ≥ 2`), CP-4, CP-5, CP-7 and CP-8 (U2:186–189, §11.1) is neither. U2 then
counts these as negatives under SNR-1 (U2:191–192), and under U1 only *not available* counts
(U1:213, :715–717). Change: declare the state and map it onto U1. The natural mapping is *not
available* at the scope of this tuple, with a stated disproved input. For the budget-limited rows
that input is AD-1(f) applied to `T`'s order. For CP-6 it is the declared `Obs` (R5). Its
[A-inf]/[OFF] standing should be stated in the table, not only in the footer.

**R5. F-3: two statements to correct.**
- (a) U2:187 and the CP-6 row (U2:291) say "a probe of `r` by Bob that does not depend on `x` is not
  in `Γ_exe`". At `y = 0`, Bob's own record is `B₁ = r`, which does not depend on `x`. So the sentence
  as written is false. Presumably the intended program is a read of `r` *in addition to* a `y = 1`
  use, which M-PR5 cannot host (one register `B`, `r` hidden). Restate it, and add Bob's `b = r` at
  `y = 0` to the sub-reads.
- (b) "The reasons are native facts of the tuple … None of them is a declaration (K-1)" (U2:188–189)
  overstates. The budget bound is AD-1(f), a criterion clause applied to the native order 2. It is
  target-neutral and also removes QR-2's separated rereads (U2:338). The exclusion of an extra
  `r`-probe rests on M-PR5's declared `Obs` (`r` hidden, SEL-EXCL-1 l. 44), which the source itself
  labels "**assumed** rather than OI-derived" (SEL-EXCL-1 l. 150). U2 applies K-1 to that same
  declaration for the §3 family (U2:291) but not for M-PR5. Change: say which negatives rest on
  `T`'s algebra, which on AD-1(f), and which on the declared `Obs`, under reading (i) of O11. Also note
  that M-PR5's `φ = T` at every tick is U2's reading of the tuple: SEL-EXCL-1 applies `T` "**once**"
  per "clocked use" (l. 44), with the clock supplied.

**R6. AC-1: the verdicts for "removing setting–setting I-sel" need the same scope in both halves.**
- Coverage (U2:371): "fails AC-1 … open for flagged realizations". This is acceptable as a scoped
  statement, conditional on S5 and on R3. It should also name the other realizations L-1 does not
  reach: those without S5 (Main:416–423), and extension operations typed into `φ` or `Γ`.
- Performed-experiment half (U2:393): "in conflict with E2. **Fails**" is stated flatly. L-1 reaches
  only output-factor realizations under S5. So the conflict holds only if the performed Bell tests
  must be realized by such programs. The same flagged, non-S5 and extension caveats apply. Change:
  scope it as in the coverage row.
- §11.2 (U2:524–527) should repeat both scopes. Attribution is otherwise right: "coverage holds on no
  model" is stated as "shown on no model … a property of the models, not of the criterion"
  (U2:378–379), which follows U1:796–805. That is correct as "not shown". Unsourced rows (QR-2 on
  R-lin) are not presented as disproofs.

**R7. The `Θ` condition is applied to M-PR5 but not to R-lin.** U2:391 makes M-PR5's CHSH 4 a
raw-direct miss "**only if** `Θ` identifies CP-1 with a performed test". This is correct under §A.24
and under c.6891338304, which makes stronger-than-quantum behaviour in experiments not yet performed
a prediction, not a defect. But U2:392 states R-lin's "conflict with E2" with no corresponding
condition. Both need an identification of performed Bell tests with model programs: for R-lin, of
the experiment's spacelike separation with "wings outside each other's cone", which is S8/`Θ` (a)
material, and S5. The asymmetry can be justified, since R-lin is OI's candidate native class and
M-PR5 is a designed tuple, but the justification must be stated. Optionally, note that the M-PR5
miss also needs the datum "no observed excess above `2√2`". The corpus carries that datum only as a
falsification condition (Substratum:481), and U2 takes no measured value from outside the corpus
(U2:387).

**R8. Evidence labels in §11.1 and one citation.**
- §11.1 marks the M-PR5 availability verdicts (CP-1, CP-2, CP-3(g)) and QR-1's R-lin negative
  without their [A-inf]/[OFF] standing. QR-1's R-lin "not available, output-factor case (L-1, D5)"
  rests on L-1 [A-inf] and on U1's [A-inf] extension of D5 to factor-set carriers (U1:435–440). The
  footer's "D5 [M-r] counts at its scope" (U2:518) could be read as making that negative count.
  Label each cell.
- U2:134 cites "no ready region under μ-G (D2, OA1:145–154) [M-r]" for R-lin's blanks. D2 is
  equal-time blindness. It does not state that no ready region exists, and visible blanks are
  "Native, by a visible herald, at the D3 cost" (OA1:328). The correct grounds: heralded visible
  blanks at D3 cost, whose herald must then be retained to `t_c` (C-RET, unsourced); and on K1,
  MR★:642 [NP]. The verdict *unsourced* is unchanged.

**R9. L-1 against U2's stop rule.** PLAN:871 stops a U2 row when "a verdict would need a new
derivation or candidate". L-1 is a new hand derivation that carries two AC-1 verdicts and decides
U1's open AW-3 point (U1:738–739, :896). U2 calls it "the standard fact … restated in U1's
operational classes" (U2:327–328), which matches Main:404–412: the framework gives up parameter
independence, and response dependence on the remote setting is the option taken. That defence is
plausible, but it must be stated *as* the reason the row is not stopped. Otherwise, route L-1 to
#914 O-INS / #1060 as a proposed lemma and keep the AC-1 verdicts that depend on it conditional on
its review.

### Optional

- **O1.** AW-U2-3 (U2:479) says CP-4's witness "needs only a `φ`-effected setting change". The
  algebra (U2:250–253; re-derived: `B₂ = B₀ ⊕ x₁y₁ ⊕ x₂y₂ = x₂` at `y₁=0`, `y₂=1`, `B₀=0`) also uses
  the blank `B₀ = 0` and a budget of at least 2. Only Bob's setting change is needed: with
  `y: 0 → 1`, `B₂ = x`. Add these to the summary row.
- **O2.** §8.1's "no flag" is correct (R2 "every later accessible time up to `T`", PREREG:163–164,
  and C-RET coincide at budget 1, `t_c = 1`), and it is vacuous because no coverage result is
  positive. For CP-3(g) it holds because reading (g) folds the inter-use retention into one tick.
  Say so, so that U3 does not read it as evidence on retention.
- **O3.** U2:335's "a response-table tuple … would meet the same steps as M-PR5": write "may meet;
  not constructed or checked", in line with the stop at U2:458.
- **O4.** CP-5's "not absorbable" argument (U2:278–281) reads better grounded in S-A6's requirement
  that the channel carry a held record *between* ticks, and in SEL-DISC-1 l. 97, where `T`'s
  coupling is already global, than in "the budget could not be stated".

## Answers to the brief's checks

1. **U1 applied as frozen?** Yes on the criterion, with one undeclared outcome state (R4). Allowing a
   setting as an initial-law datum is U1's own text (U1:310–313), not a U2 change. The `μ_PR`
   completion is a modelling step U2 declares (R1, R2).
2. **F-1.** SPEC:468's reason is overturned and its conclusion is not. CP-1 is available only
   relative to an assumed initial law (R1).
3. **F-3, L-1.** F-3's core holds: `T² = id`, so AD-1(f) gives budget ≤ 1. Its wording on Bob's probe
   and on "no declaration" needs correction (R5). L-1 is correct for binary initial setting factors,
   with determinism, output factors and S5 explicit. The "written from" clause needs a fix (R3). No
   counterexample was found within the hypotheses.
4. **AC-1.** Both "fail" restrictions are correctly shown to exclude QR-1 at their scopes. The
   performed-experiment verdict for I-sel removal is unscoped (R6). "Coverage on no model" is
   correctly attributed to the models. The raw-direct conditional on `Θ` is correct under §A.24 and
   c.6891338304, but it is applied asymmetrically (R7).
5. **Retention flag.** Correct, and vacuous (O2).
6. **Labels and citations.** 40+ spot-checked (list below). All accurate except R2 (MP-0a), R8 (D2)
   and the §11.1 labels (R8).
7. **Off-`main`.** §10 classifies U1/PLAN/SPEC/DEPS, SEL-EXCL-1, SEL-DISC-1, NAS and #912 as
   **support off `main` (gap)** and states that F-1, F-2 and F-3 are not established (U2:497–498).
   That is correct under §A.42 item 8 and §A.46 item 1. Owner comments are classed as governance, and
   routing Issues as accountability only. Correct.
8. **New premises, readings.** No new physical premise. `μ_PR` is a declared model completion
   (R2). Conditionals carry their conditions (S1, S5, S6, S8, U1, off-`main` `T`). "Meets the
   criterion" is explicitly not "OI realizes it" (U2:124–125). Soundness is read as a finding, not a
   requirement (U2:22–25, §7), as c.6891338304 requires. The text of BELL-QSET is correctly left to
   the owner.

## Checked

- Blob identity of U1 at `3ec1e465` and the head (`68983f86`); PLAN, DEPS, SPEC blobs; no change
  to the governing files between `3ec1e465` and the head.
- Owner comments c.6890079967, c.6891241282, c.6891338304: quotes, authors, times.
- SEL-EXCL-1 at `0ecfddeb` (blob `1e8892ff`): ll. 17, 33, 36, 38–40, 44, 46, 67, 69–81, 83, 87, 89,
  91, 93–95, 97, 99, 101, 129, 150, 165–181.
- SEL-DISC-1 at `445b17f7` (blob `ccf2d46d`): ll. 53, 65, 71, 85, 95, 97, 101–107, 113, 129, 143,
  147, 149.
- NAS at `d8b74527` (blob `a6661de9`): ll. 14, 38, 65, 70–76, 82, 155; diff to head `7086bd30`
  (status lines and retention files only).
- `main`: Main:42, 54, 58, 74, 326–328, 360, 364–389 (bound at 389), 404–412, 414, 416–423, 724
  ((xiv)); Substratum:123, 481; OA1:111–113, 131–134, 145–160, 176–194, 202–206, 326–328, 356–364;
  MR★:508–509, 595–601, 637–642; REPORT.md:34–36, 57–69; THEOREM-N.md:3–9; MR-1
  preregistration:163–164.
- PLAN:268–272, 344, 412–420, 784–800, 866–888; DEPS:295–298, 370–374, 590–594; SPEC:232–245,
  316–328, 370–400, 435–500, 540–569; U1 at all lines U2 cites.
- Hand re-derivations: `T² = id`; CP-1 table and CHSH 4; `x = 0` fragment; μ-G herald (`V_A(t₁)`
  independent of `A₀`; `a⊕b = A₀⊕B₀⊕xy`, CHSH 0); CP-4 witness; CP-5 affine writes; L-1 (above).

## Not checked

- SEL-EXCL-1 §3's lemma proof and REPORT's freshness proof beyond the lines quoted. Reading (g)'s
  availability relies on them and is [OFF]/[M-r] as labelled.
- #912 `composition_flag_v6/` at `2af1d5d5` (U2 marks it context only).
- Theorem N's family against C-RET (U2 does not use it as a negative).
- DEPS C-1's full derivation, and Main:414's corollary hypotheses applied to R-lin beyond their
  statement.
- The ChatGPT exact-head review, which remains a separate gate (c.6890079967 C1).
