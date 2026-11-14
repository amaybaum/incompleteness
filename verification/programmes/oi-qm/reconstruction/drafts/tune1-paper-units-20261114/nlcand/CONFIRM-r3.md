# CONFIRM r3 of NLCAND: exact-head confirmation after CONFIRM-r2 (ACCEPT WITH CHANGES)

**Verdict: ACCEPT WITH CHANGES.**

r3 applies N1–N5 exactly as `CONFIRM-r2.md` gives them. All 13 hunks of `diff NLCAND-r2.md NLCAND-r3.md` are
accounted for below. No verdict, node, derivation or scope changes. Every verdict is stated at the strength
its nodes support, for the one member of §1.4. Four minor required changes remain (R1–R4, exact text in §7).
They concern how r3, the summary and the README state the review status and the name H-nl, plus one hypothesis
that the summary drops.

- **Exact head.** Draft PR #1288, branch `research/tune1-paper-units-1236-20261114` at
  `485f9a2d8537c30fb0e5291e50e49722345cb908`. `git rev-parse HEAD` returned that SHA and the working tree was
  clean. Directory: `verification/programmes/oi-qm/reconstruction/drafts/tune1-paper-units-20261114/`, files
  `nlcand/*` and `README.md`.
- **Other sources read.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (`papers/SM.md`, `papers/Main.md`,
  `TUNE-1-STEP2-SESSION4.md`, `OA-1-REPORT-r5.md`, the Lean files cited in A3). TUNE-1 Step 3A r3 on
  `research/tune1-step3a-1236-20261113` at `8228b3c24e17a17f324b6779b53b04ad296b4308` (off `main`).
- **Reviewer.** A non-author model reviewer. It wrote none of `NLCAND-r1/r2/r3.md`, `REVIEW-r1.md`,
  `CONFIRM-r2.md`, `RESPONSE-r1.md`, `SUMMARY-r3.md` or the README.
- **Method.** Source reading and hand checking only. No computation on any OI rule or model, and no Lean build.
  Lean statements were read, not rebuilt. Read-only: nothing in the checkout was edited, and nothing was
  committed, pushed or posted.
- **Scope.** The non-linear candidate unit only. `l54/` was not reviewed.
- **Citation form.** `r2:n` and `r3:n` are lines of `NLCAND-r2.md` and `NLCAND-r3.md`. `S4:n`, `OA1:n`, `SM:n`
  and `Main:n` are as in r3's pins.

***

## 1. Q1: does r3 implement N1–N5 exactly? **Yes. No verdict or scope changes.**

| Hunk | r2 → r3 | What it is | Check |
|---|---|---|---|
| 1 | 1 → 1 | Title `r2` → `r3` | editorial |
| 2 | 3–4 → 3–6 | Status paragraph | see the note below the table; R1 |
| 3 | 68 → 70–71 | §0.6 | N2 (first place), text exact |
| 4 | 216 → 219–220 | A3, "`rfl` and `Iff.rfl` respectively" | N3 (first edit), exact. `sourcing_rule_independent` ends in `Iff.rfl` (`FrozenSourcing.lean`:299) |
| 5 | 232 → 236–237 | A3, "stated on the two-valued carrier" | N3 (second edit), exact. `DenseUnitaryControl` takes a `FiniteOperationalTheory (Fin 2)` (`DiscreteCompletion.lean`:45), and `permTheory_dense_ceiling` is on `permTheory (Fin 2)` (`FrozenSourcing.lean`:187) |
| 6 | 414 → 419–420 | C1 | N2 (second place), exact, including "with equality when it reads those slots directly". OA1:158–160 has "`P(E) ≤ q^{−M}`, with equality for a visible herald on visible cells" |
| 7 | 438–439 → 444–446 | Verdict (c) | N2 (third place), exact. The line break inside "O-RDY (Gap P, LP:243–248)" is cosmetic |
| 8 | 452–453 → 459–461 | §6 "Order" | N1, exact: r3:457–461 matches the N1 bullet word for word |
| 9 | 514 → 522 | §8 fixed-point sentence: "r3 adds wording edits only" | editorial. True in the sense that no analysis pass was added |
| 10 | 522 → 530–531 | §9, second "Shows" bullet | N4, exact |
| 11 | after 530 → 540–541 | §9, "Does not show", new second bullet | N5, exact, placed after r2:530 as specified |
| 12 | 554 → 565 | §10 review row: adds `CONFIRM-r2.md` and "the wording edits N1–N5" | editorial; provenance only |
| 13 | after 559 → 571–574 | Closing "Not included" note on O1 | accurate. O1's own text says it "does not cover the member, whose `r_O` fixes slots … nor convention H"; r3 does not use O1 |

The README's list of the changes beyond N1–N5 matches hunks 1, 2, 9, 12 and 13, and its count of 13 hunks is
right.

**Note on hunk 2.** r2's header said "r2 itself is unreviewed". r3's header drops the corresponding sentence for
r3 and writes "r3 is r2 with those five wording edits and no change of verdict". Read alone, that can be taken to
mean `CONFIRM-r2.md` covers r3. It also leaves out hunks 9, 12 and 13. Neither point alters a verdict or a
scope, but the header no longer states r3's own review status (R1). The header also keeps r2's "independent
non-author review" a few words before "not independent verification". R1 drops "independent" there; the README
already says "Non-author review".

***

## 2. Q2: verdict strength. **Exact, for the one member.**

| Verdict in r3 | Nodes | Exact? |
|---|---|---|
| (a) A label action that is not a translation: supplied, pointwise, under both conventions | A1. Under S, `v_{a+1}(0) = 0` by `r_O` and `u_a(0)` is in the tick-1 state | Yes |
| (a) Kernel sourcing results not scored | A3, P17. The negatives are on `Fin 2` with no substratum and no rule. `obsTheory_rule_independent` holds by `rfl` and `sourcing_rule_independent` by `Iff.rfl`. Checked at the Lean lines | Yes. "They do not see the rule" (Verdict (a)) is the right phrasing |
| (a) Single-qubit target: undecided | A5. T1 is not restated for a ring and the T1 family is unspecified | Yes |
| (b) Member: not supplied at lattice scale | B7, with B2 and B4 (0). For every `c_L`, either no record outside the physical cone depends on the remote generator, or the record at `{a, a+1}` signals at distance 2 > `c_L` | Yes, for the member with its declared `r_O` (needed under S) and label `0` in its menu. The defect is a signalling instance at `g = 0`, and that placement is allowed because `g` is free in §1.4 |
| (b) Rule: not established | B5 (dependence without signalling for one-cell records under H); B4 (iii) undecided | Yes |
| (b) Distant wings: undecided | B4 (iii); B7 limit (1) | Yes, "under μ-G with no declared cells between" |
| (b) Dependence on the record convention | Header (H, S kept apart); B4 (0) both; B4 (i) both; B4 (ii) H `1/q`, S `0`; B4 (iii) both undecided, with S bounded by H; B5 H PR-type table, S product table; B4 table; F11 | Yes. Every in-cone effect is labelled with its convention, and N1 fixes the one place in r2 that was not |
| (c) None unconditionally under the uniform law | C1. Invariance of μ-G under a bijection | Yes. The "for any bijective rule" form is rule-free and is marked as such in §9 |
| (c) Heralded supply: accepted with probability at most `q^{−M}` | C1; OA1 D3 | Yes, now a bound (N2) |
| (c) Undecided under μ-O and μ-R | C4, C5 | Yes |
| Joint: "not shown to meet the three requirements; for (b) a derived defect at lattice scale; not shown that no completion of the ring rule can meet them" | §6, with N1 | Yes. The "Order" bullet now matches B4 under S |

I found no statement in r3 stronger than its nodes. The defect claim is stated for the member, and the
ring-rule-level claim is "not established" in both directions.

***

## 3. Q3: hypothesis naming. **The distinction is right. One wording is imprecise (R2).**

- On the source: S4:30–39 (on `main`) defines **R-nl** as "the rounded bijection of SM:294", the six-neighbour
  `d = 3` rule `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q`. It defines **H-nl** as "the named hypothesis
  'the world's rule is R-nl'", which is not adopted. Step 3A r3 uses H-nl in the same sense (3A:715, :1013).
  SM:294 itself names no hypothesis. SM:112 is the one-dimensional ring rule, a different rule.
- r3's H-ring, "the world's rule is this ring rule", is therefore a different hypothesis from H-nl. r3 says so
  and never uses H-nl for its own candidate. r3's M1 and §9 keep the rounded rule out of scope.
- **Imprecision.** r3:8–9 and README:16–17 say "H-nl, which names the rounded rule". SUMMARY-r3:44 says "H-nl
  (TUNE-1's name for the rounded rule)". In the source the rule is named R-nl. H-nl names the hypothesis that
  the world's rule is R-nl. R2 fixes all three places.
- Minor: r3 says "written H-ring below", but H-ring does not occur below the header (optional S2).

***

## 4. Q4: `SUMMARY-r3.md` and the README.

**README. Correct on review status. No generalization.** It says r3 applies all five edits as written, that
r2's verdicts are unchanged, and that "r3 itself has not been reviewed". It lists the changes beyond N1–N5
correctly and says "Neither review is independent verification, a human review or an owner decision". The
scope paragraph limits every verdict to the one candidate and excludes the class, H-ring, H-nl and H-Bell. It
states the dependence on the record convention, citing Main:369–372. The `nlcand` section does not use any
L5.4 result. The `l54` section mentions the ring rule once, in the `CHECK-RULEFREE.md` table ("no bearing on the
linear or ring rule beyond …"), and that is a scope exclusion, not a conflation. Only remaining change: the H-nl
wording (R2). Optional: S4, S6.

**SUMMARY-r3. Nothing stronger than r3 on the verdicts. Three changes.**
- Status (lines 43–44). It reads "one non-author model review and its confirmation; not independently verified".
  It does not say that the confirmation was of r2, or that r3 is unreviewed (R3).
- H-nl wording (line 44): R2.
- Line 24–25, "no dependence outside the rule's own cone …, and Bell-local there". r3 states this "under (xiv)"
  (§0.5, B2, Verdict (b)), that is, under the ledger's measurement independence (Main:724). The summary drops
  that hypothesis (R4).
- The rest matches r3: control; the Bell bullets with their conventions; the dichotomy; distant wings
  undecided; cell supply with the bound; the joint verdict; the exclusion of the rounded rule, longer edges,
  `d = 3`, H-Bell and the class. "Under the uniform law no bijective rule supplies known cells unconditionally"
  is r3's rule-free C1, not a generalization from the candidate. "Under S both effects are absent at one tick"
  is right for the one-cell variant as specified, which has no declared record cell (optional S5).

***

## 5. Q5: new claims in r3 not in r2. **None of substance.**

The new statements are listed here, with their checks.
- The equality case of the herald bound (N2), checked at OA1:158–160.
- "Stated on the two-valued carrier" (N3), checked at `DiscreteCompletion.lean`:45 and
  `FrozenSourcing.lean`:186–188.
- "Under S the `g = 1` instance is decided and does not signal" (N1). This restates r2's B4 (ii) under S
  (r3:324–327).
- "Both reviews are model reviews, not independent verification (§A.46 item 7)". This is accurate.
- "r2 received the same reviewer's confirmation". This matches `CONFIRM-r2.md`'s reviewer line.
- The §8 and "Not included" sentences. They are accurate, as in §1.

N4 restates B1 and B2. N5 adds an item marked "not examined". None of these adds a result or moves a verdict.

***

## 6. Findings outside N1–N5 (none changes a verdict)

- r3:219 cites `sourcing_rule_independent` at `FrozenSourcing.lean`:295–298. The proof term `Iff.rfl` is at line
  299, and `RESPONSE-r1.md` cites :295–299. This was carried over from r2 (optional S1).
- B4 (0) (r3:306–307) says the label is "known by declaration (or read from the block's tick-1 state)". Reading
  it from cell `a+2` would enlarge the readout region to include a cell at nearest-neighbour distance one from
  the generator. B7 uses only the declared label with region `{a, a+1}`, so no verdict is affected. This was
  carried over from r2 (optional S3).

***

## 7. Required changes (all minor), with exact replacement text

**R1. r3:3–6, status paragraph.** Replace "r1 received an independent non-author review (`REVIEW-r1.md`,
REVISE); r2 received the same reviewer's confirmation (`CONFIRM-r2.md`, ACCEPT WITH CHANGES, N1–N5); r3 is r2
with those five wording edits and no change of verdict." with:

> r1 received a non-author review (`REVIEW-r1.md`, REVISE); r2 received the same reviewer's confirmation
> (`CONFIRM-r2.md`, ACCEPT WITH CHANGES, N1–N5); r3 is r2 with those five wording edits, this paragraph, one
> sentence of §8, the review row of §10 and a closing note, and no change of verdict. r3 itself is unreviewed.

If the edit is made after this confirmation is placed beside the file, replace the last sentence with
"r3's only review is an exact-head confirmation (`CONFIRM-r3.md`)."

**R2. The name H-nl, three places.**
- r3:8–9: replace "H-ring is not TUNE-1's H-nl, which names the rounded rule of SM:294 (S4:37–39)." with
  "H-ring is not TUNE-1's H-nl, the hypothesis that the world's rule is R-nl, the rounded rule of SM:294
  (S4:30–39)."
- README:16–17: replace "It is not TUNE-1's H-nl, which names the rounded rule of `papers/SM.md`:294." with "It
  is not TUNE-1's H-nl, the hypothesis that the world's rule is R-nl, the rounded rule of
  `papers/SM.md`:294."
- SUMMARY-r3:44–45: replace "H-nl (TUNE-1's name for the rounded rule) and the ring-rule hypothesis of r3 are
  named and unadopted." with "H-nl (TUNE-1's hypothesis that the world's rule is the rounded rule of
  `papers/SM.md`:294) and H-ring (r3's hypothesis that the world's rule is this ring rule) are different
  hypotheses, both named and unadopted."

**R3. SUMMARY-r3:43–44, review status.** Replace "one non-author model review and its confirmation; not
independently verified." with "a non-author model review of r1 and its confirmation of r2; r3 itself is
unreviewed; not independently verified." The alternative ending in R1 applies here too.

**R4. SUMMARY-r3:24–25, the dropped hypothesis.** Replace "and Bell-local there." with "and Bell-local there
under measurement independence (ledger item (xiv))."

***

## 8. Optional suggestions (not required)

- **S1.** r3:219: change "`FrozenSourcing.lean`:295–298" to "`FrozenSourcing.lean`:295–299".
- **S2.** r3:8: change "written H-ring below" to "written H-ring". The name is used only in the header and in
  the README.
- **S3.** r3:306–307: delete "(or read from the block's tick-1 state)", or add "; B7 uses the declared label".
- **S4.** README:45: replace "Nothing here is a statement about the non-linear class" with "Apart from the
  rule-free statements r3 §9 lists, which hold for every rule by their own proofs, nothing here is a statement
  about the non-linear class". C1 holds for every bijection.
- **S5.** r3:68 and SUMMARY-r3:29: add "with no declared record cell" after "under S". B5 (r3:359–360) says the
  table returns under S when the record cell's pre-setting slot is declared.
- **S6.** README file table: "`NLCAND-r3.md` | The final text" could read "The current text", because r3 has no
  review of its own.
- **S7.** r3:522 is one overlong source line, and r3:446–447 break inside a parenthesis. Both are cosmetic.

***

## 9. Status of this confirmation

This is a model review of the text at `485f9a2d8537c30fb0e5291e50e49722345cb908`. It checked that the edits
were applied, checked verdict strength against the file's own nodes, and checked citations against their
sources. It is not independent verification of the mathematics (AGENTS.md §A.46 item 7). It is not a human
review and not an owner decision. It authorizes nothing and changes no scientific status.
