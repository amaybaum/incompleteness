# ASSESS-1049 r3: dispositions of REVIEW-1049-r2

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).**

This file maps each finding of `review/REVIEW-1049-r2.md` to its change in `ASSESS-1049.md` r3.
- **Review.** sha256 `22da4c924a08222c883553f8861ee3c6ea0520809066db739d1109ff10cadab3`; verdict
  REVISE.
- **From.** r2, kept unchanged at `r2/ASSESS-1049.md`, sha256
  `1628cc7850979632da93879f5188c6df5ce5d6d55849fce5e30feac94a43a893`.
- **To.** r3, `ASSESS-1049.md`, sha256
  `75d6af06fcac7750dcdd7677abf42fbbbeb50caa0acbb8db619e42fb39b82fa9`.
- **Verification.** Each finding was checked against its source with
  `git show fd539e15:<path>`, after `git fetch origin main`; `origin/main` = `fd539e15`, unchanged.
- **Reviewer's checks.** `review/rv2_gauge_audit.py` was re-run with `python3 -I` into
  `reassess/rerun-1049-r3/`: exit 0, output byte-identical (`372a2c17…16ab2`).
- **Writes.** No git or GitHub write was made, and no manuscript was edited.

## Blockers

### R2-B1 — one reading for "amplitude-(in)dependent dispersion"; Sub:270; F-8

**Verified against.**
- Sub:270: "the linearity equivalence of [SM §4.1] (amplitude-independent dispersion $\iff$ affine
  dynamics)".
- Sub:272: "a non-affine $F$ induces amplitude-dependent emergent dispersion, which *is* observable),
  so "absolute amplitude is unobservable" already presupposes an affine rule".
- SM:240 and Sub:274: the lemma, stated in base-point form.
- rv2 R6 and r2 G1: P1's response does not depend on the absolute level.

**Decision.** The sources support reading (b), the base-point reading, for both phrases: Sub:270
attaches the phrase to the [SM §4.1] lemma, and that lemma is stated in base-point form.
- Under (b), Sub:270's ⟺ is the lemma, so Sub:270 is **not** an overstating site.
- Under (b), F-8's "false" for the Sub:272 parenthetical was wrong. F-8 is restated as **"Sub:272's
  inference fails under either reading"**, as the sources support.
  - Under (b), the parenthetical is true, and the conclusion is false for d = 2, 3 when its
    antecedent is read as (R-uni), or as (R-rel) at every d.
  - Under (a), the parenthetical is also false, and so is Sub:270's ⟹.
- Per the owner direction, a narrowly scoped correction is given for each false clause.

**Changes in r3.**
- New §2.3.1.
  - The two readings, plus a third (dependence on the perturbation's own amplitude), which splits
    into (a)'s scale part and (b)'s superposition part.
  - The source-support paragraph.
  - Truth table for Sub:270, the Sub:272 parenthetical, the Sub:272 conclusion and the inference,
    under (a) and (b).
  - "What is false, stated narrowly": F3, plus the two reading-(a) falsities.
  - Corrections for Sub:272's second sentence. V1 uses a definitional premise ("a rule for which
    uniform rescalings and shifts are not exact symmetries of the dynamics distinguishes, in its
    evolution, states that differ only in absolute amplitude"), so the inference is valid. V2 adds
    the d = 2, 3 limitation.
  - The r2 parenthetical is withdrawn, with the reviewer's reason.
- §2.3 per-site table: new row for Sub:270. No correction under (b); a qualifier-only correction if
  the owner reads (a).
- §2.3 GA3 row: "One reading serves both phrases"; R6's unit homogeneity added.
- §2.1 (R-site) bullet: F-8 sentence restated.
- §2.1 *Consequence*: Sub:270 bullet.
- §7 F-8 restated.
- §0 item 3.
- §6 Q3: confirm reading (b).

**Partly adopted.** The reviewer's suggested premise was "makes the absolute amplitude dynamically
observable". It is replaced by the literal "distinguishes, in its evolution, states that differ only
in absolute amplitude". The literal form restates "not an exact symmetry" and asserts nothing about
what the embedded observer resolves; the Status note already flags that question.

### R2-B2 — contradicted clauses left standing in the same passages

**Verified against.**
- Sub:100: "pending it, non-affine alternatives are excluded precisely to the extent amplitude-scale
  gauge is assumed".
- ch02:84 = FULL:718, byte-identical: "excluded exactly to the extent that input is assumed".
- Sub:274: "The principled object that delivers the affine restriction without overshooting is the
  **additive-automorphism** group".
- Sub:272: "the input (absolute amplitude is unobservable) is strictly weaker than the output (affine
  dynamics)".

**Changes in r3.**
- **Sub:272, first sentence.** New table: both clauses under (R-rel), (R-uni) and (R-site).
  - The pair is false under every reading.
  - In the link-sum class the comparative still fails: the input is stronger than the output, not
    weaker.
  - F1 and F2 are stated.
  - V1 deletes the false comparative and qualifies "excludes" with the base-point form; no new
    negative claim. V2 also states the uniform-form limitation.
  - This also removes the conflict the reviewer found between r2's base-point replacement and the
    surviving "strictly weaker".
- **Sub:274.** F4 ("principled object that delivers") and F5 ("certified theorem") are stated as
  false for the uniform group.
  - V1 corrects both clauses inside the claim: (i) adds "taken in the base-point form …"; (ii)
    "yields, in that base-point form, …". V2 adds the limitation.
  - Note added that only the shifts enter the base-point form.
- **Sub:100 and ch02:84 = FULL:718.** The narrowings are withdrawn (R2-B3), so the surviving clause is
  given an explicit disposition in the per-site table.
  - Under GA7-α it holds in both directions. The witness is Σ_j x_j², which is not affine, and is a
    link sum excluded exactly by uniform gauge.
  - Under the interface as typed it holds in one direction only (§2.4 G1).
  - Under GA7-β both clauses would need the qualifier. The contingent text in §2.4 item 4 covers
    every clause of Sub:100 (three), ch02:84 = FULL:718 (two), Sub:104 (one) and Sub:220 (two).

**Partly refused.** The reviewer offered the owner a choice between a "base-point form" correction
and a "link-sum form" correction. No link-sum wording is proposed for paper prose. It would write
into the manuscript a premise the corpus does not state for non-additive rules (§A.29), and this
unit is not authorized to introduce new assumptions. The link-sum option is instead put to the owner
as a question about A6's interface (§6 Q2; O-G).

### R2-B3 — A6 is reading-dependent; recovery note; inventory; Q-NEXT

**Verified against.**
- `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`:1–135 at `fd539e15`.
  - It defines four readings: A6-inv, A6-cov, A6-glob, and A6-sd (named, with no predicate).
  - `A6Cov` is defined on `linkF N M c i = ∑ j ∈ N i, M i j (c j)` with `M i j : V →+ V`.
  - D3-a: "its content is the interface, not a constraint".
  - The module states that it "adopts no reading".
- `OIBridge/A6Instantiation.lean`: `linkSubstratum_A5` ("each `M i j` is additive and the neighbour
  sum is finite"), and the bounded reading at :317–321.
- A5 D14, N9 and E2; Q3 A4 ("Corpus: none"; "The corpus links are matrices (SM:116, SM:523)").
- Sub:102, ch02:86 = FULL:720 (byte-identical); Main:726 (xii); SM:114–118; SM:314.

**Changes in r3.**
- **Theorem-recovery note: new §2.4**, written before any narrowing. It gives:
  - the strongest existing results: E1, the lemma [P; A]; E2, the kernel results [K]; E3, the
    link-sum recovery [A]. E3 is the reviewer's one-line proof, stated without κ = 2: any
    state-independent shift effect, λ = 1 only. It comes with a corollary (the base-point form, so
    the Sub:100/Sub:104 route holds) and a converse (every affine rule is a link sum, so on the
    covariant class link-separability is equivalent to affinity);
  - the verification: rv2 R4, and the new r3 K1 and K2;
  - the corpus reading, with sources quoted:
    - the written interface is the link sum, with additive links;
    - no source writes a non-additive or joint-insertion interface;
    - "restricts no rule" is scoped in the kernel to link-coupled rules;
  - the assessment: P1 is excluded by A6, or outside its domain, under either status of the
    interface;
  - the precise gap: G1 (additive typing: gauge idle, A5 redundant, one-direction clauses); G2
    (warrant: separability equivalent to affinity on the covariant class); G3 (sites not
    recovered); G4 (scope).
- **The corpus's A6 is link-sum in its written form**, so the affine claim is recoverable at the
  A1–A6 sites, as the coordinator anticipated. The narrowings at Sub:104 and Sub:220 are
  **withdrawn**, and so are those at Sub:100 and ch02:84 = FULL:718: they sit in the same A1–A6 list
  (Sub:90 "restrictions on the class of candidate substrates"; ch02:74 "six properties"). Structure:259
  is also recovered (A1–A6 in the same paragraph).
- **GA7 split by reading:** GA7-inv, -cov, -glob, -sd, -α, -β, each with a P1 verdict and support.
- **A6 column added to the per-site table for every site.** The test text now defines when a site
  states A6.
- **Inventory additions:**
  - the four kernel readings (GA7);
  - SM:96's gauge-group statement, as GA9, with verdict **yes, exactly**. It has a paper argument
    (σ(w − y) + σ(y) = σ(w) + σ(0) and f onto, so σ − σ(0) is additive), rv2 R3, and the new
    r3 K4 for d = 2, q = 7 and d = 3, q = 2;
  - Theorem 24 (i), (iii) and (iv), listed as placing no condition on F;
  - the master principle;
  - SM:585 and :811;
  - ch05:45 = FULL:1363, as a GA1 and GA2 source.
- **Q-NEXT (§5)** now leads with link-separability, "the one candidate already known to close the
  implication". Its sufficiency is settled, and on the covariant class it is equivalent to
  affinity, so the question is its warrant.
- **New O-G (§4)** and owner question §6 Q2.
- §0 items 1, 2, 4 and 8. §7 F-1 is scoped to non-link-sum rules. New F-9 (POSITIVE, with an
  assumption-watch marker) and F-10 (ELABORATING). New pressure-test item 7, on the recovery as a
  favourable branch.

## Nits

| Finding | Verified against | Disposition | Change in r3 |
|---|---|---|---|
| N1: F-7 should cite H-D D6, H-D-SR SR-1/SR-3 and A5 C8; only Structure:301 is new | H-D result D6; H-D-SR `SR-1` table, "Four in the open form, one resolved in the negative — the distribution H-D's D6 records", and `SR-3`, "The disagreement stands on the record unadjudicated"; A5 C8 (cites `SR-3`); blob `84a7ede4` has no "does not entail" (`git show 84a7ede4 \| grep -c` = 0) | Accepted | §7 F-7: prior record cited; Structure:301 named as the only addition; coordinate drift noted (H-D-SR's coordinates are at its own base) |
| N2: "Two further statements" lists one | r2 §2.3 | Accepted | Replaced by the numbered list "Gauge statements that place no condition on the rule" (five items) |
| N3: Structure:301 is "no overstatement", not a GA8 hold | Structure:301; SM:240 | Accepted | Per-site row: "None: no overstatement"; §4 O-F |
| N4: "defined uniformly in q" reads as favourable to P1 | §2.1 construction (P^{q−2}) | Accepted | §2.1 alphabet-size disposition and GA8 row: the degree of the nonlinearity grows with q; "undetermined" rests on the unconstructed correspondence |
| N5: owner Q1 should offer the clause-wise reading | Structure:219 (GA2 clause and GA8 in separate sentences) | Accepted | §2.3 test text; Structure:219 row gives the clause-wise V1 text; §6 Q1(b) |
| N6: `.tex` ranges | `git show fd539e15:papers/Substratum.tex`: Sub:100 clause :745–751; Sub:272 :1729–1732 and :1736–1739; Sub:270 :1719–1720; Sub:274 :1768–1772 and :1776–1778; Sub:104 :783–784 | Accepted | §2.1 mirror list and per-site table. Sub:104's range is corrected from :783 to :783–784; Sub:274 :1768–1772 is added for the "principled object" clause |
| N7: proposals add an off-`main` negative claim to paper prose | §A.42 item 2; §A.46 item 1 | Accepted | Every correction has a V1 variant (qualifier or deletion only; no new negative claim) and a V2 variant (adds the limitation; P1's proof must land with it). The r2 proposals that carried the claim at Sub:100 and :220 are withdrawn (R2-B3) |
| N8: complete the GA sources and the non-rule-constraining rows; SM:96 gauge group, P1 yes, exactly | SM:96; Sub:251–266; Sub:270; ch05:45 = FULL:1363 (byte-identical); SM:585, :811 | Accepted | GA1 and GA2 sources extended; GA9 row; non-condition list items 2–5. The r3 sweep also found Stage 2(d) uses of amplitude-scale gauge (Sub:163; SM:344, :374; ch02:102; ch03:74; ch05:17, :125, :129, :143, :190, :192; ch06:8; appendix-c:289), listed as item 5 |

## "What re-review needs" (REVIEW-1049-r2 §7)

- R2-B1 to R2-B3 are applied; see above.
- The GA7 row is split by reading, and there is an A6 column for every site.
- The recovery note for the link-sum result is §2.4.
- The diff check of the changed passages is left to the re-reviewer. The `diff r2/ASSESS-1049.md
  ASSESS-1049.md` hunks map to the items here and below.

## Untraced changes (not from a review finding)

- **U1. Header and authorization.** Revision line; the r2 copy and `DISPOSITIONS-r3.md` are named;
  the owner direction on narrowly scoped corrections is quoted; the reviewer's citation
  #1169 c.6740778880 is recorded.
- **U2. §0 restructured** into eight items. Old items 3–5 become 5–7, with their text unchanged
  except old item 5's internal "item 4" reference, which becomes "item 6". Old items 1, 2 and 6 are
  rewritten as new items 1, 4 and 8. New items 2 and 3 are added.
- **U3. §1 rows** for the kernel A6 modules and the rv2 checks.
- **U4. §2.4 G1, one-direction clauses.** Found while checking R2-B2. Under the interface as typed,
  with additive links, dropping gauge admits no non-affine rule either. So "excluded precisely to
  the extent" (Sub:100; ch02:84 = FULL:718) and "exactly when … dropped" (Sub:220) hold in one
  direction only. Recorded as part of O-G. No correction is proposed, since it is not a P1
  counterexample.
- **U5. §2.4 E3 generalization and converse.** E3 drops the κ = 2 restriction of the reviewer's R4
  argument. The converse (affine ⇒ link sum) makes link-separability equivalent to affinity on the
  covariant class. This drives G2, the Q-NEXT framing and pressure-test item 7.
- **U6. Sub:220 context.** It is described as a bullet of the *Remark (Hypothesis dependencies)*
  (Sub:214–221), verified at `fd539e15`, not of Theorem 23's dependency list.
- **U7. §2.1 *Consequence*.** The overstating sites are regrouped into "among A1–A6" and "gauge
  principle alone". A book-mirror check found no book passage restating the Sub:272 and Sub:274
  clauses. The search-scope terms are extended to r3's sweep.
- **U8. §4 O-A and O-D.** O-A is restated for the recovery. O-D's SA-1(a) wording adds "or a link-sum
  interface".
- **U9. §6** is restructured: Q1(a)–(d); new Q2 (A6's interface) and Q3 (Sub:270 reading). Old
  Q2 and Q3 become Q4 and Q5.
- **U10. §7 pressure test.** Item 5 is updated for the r3 inventory, and the lead-in mentions the
  seventh item.
- **U11. §8.** r3 paper items; the r3 probe; the rv2 re-run; the r3 reading coverage, split into
  "in full" and "at the quoted passages only". "Not done" notes that the kernel was read, not
  rebuilt.

## Probe added

`probes/r3_link_recovery.py`, sha256
`349032103f7f8bbc8eba2e58eb2cad43eb85214f3fbc51090bc61db3d789d5e4`. Output
`probes/r3_link_recovery.out`, `ab2b278651d89de8cacfd71c1e565118ee8287911d7ca69c40106f1b87a90b44`.
ALL PASS, exit 0, about 1 s.

It uses exact modular arithmetic on generic local functions and one-step identities. It iterates no
dynamics, computes no observable, instantiates no OI mechanism, and imports nothing from `probes/` or
`review/`.

- **K1.** None of the four P1 constructions is a link sum. Controls: the linear rule, and Σ x_j²
  (separable, not affine).
- **K2.** Link-sum rules with a state-independent shift effect are exactly the affine ones.
  Countercontrol: a non-separable, shift-covariant, non-affine rule.
- **K3.** Affine rules with b ≠ 0 fail (R-uni) for every κ. Control: the linear rule.
- **K4.** The uniform permutation symmetry group is AddAut for d = 2, q = 7 and for d = 3, q = 2.
  Countercontrol: a smaller group.
