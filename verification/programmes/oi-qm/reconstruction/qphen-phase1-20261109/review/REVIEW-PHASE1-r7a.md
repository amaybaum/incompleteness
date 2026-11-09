# QPHEN Phase 1 r7a: confirming review

## Standing

- **Reviewer.** This is a fresh, independent, model-written confirming review. It is read-only on the repository, git
  and GitHub. It writes three files: this review, `review/probes/p15_r7arev_stronger_conclusion.py` and its output
  `p15_r7arev_stronger_conclusion.out`. The p14 re-run output went to a separate scratch directory, `review/rerun/`.
- **Files reviewed.** Each sha256 was verified before reading, and each matches the brief.

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `baf3de3cc5807a36…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `6b45c062bb5a6b1c…` |
  | `QX6-BELL-CHSH.md` | `b77f0984a282603b…` |
  | `SHARED-MECHANISM.md` | `ab69695e33e7e805…` |
  | `DISPOSITIONS-r7a.md` | `417932eed82889e5…` |

  The texts under `r7/` match the hashes listed in DISPOSITIONS-r7a. `REVIEW-PHASE1-r7.md` is `42edbb6c…`, and
  `p14_r7rev_meter_supply.py` is `cd8be1e1…`.
- **Corpus.** The sources were read with `git show fd539e15:<path>`, with no fetch, depth, gc or prune.
  - AP1 (`verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`):
    - :290-291 says per-edge arming "is not native";
    - :297-299 is SA-1(c), "… unknown and uniformly distributed, independently of everything else";
    - :322-323 is "Given (c) and N2, that slot is unknown and uniform, so the shift is a disturbance";
    - :323-325 is "With a known meter slot the shift would be a known displacement and no disturbance."
  - Main:726 is the posit ledger: (vi) is isotropy, (vii) is linearity, and there is no per-edge arming.
  - The owner record #1210 c.6742225689 was read through the GitHub API (read-only). It is by user amaybaum, created
    2026-11-09T14:14:59Z.
- **Method.**
  - All four specifications and DISPOSITIONS-r7a were read, and `diff -u r7/ .` was read for every hunk.
  - p14 was re-run with `python3 -I`.
  - Q4-P20 was re-derived by hand.
  - p15 is a new exact probe. It imports nothing earlier and uses only `itertools` and `random`. It builds
    `Sp(4, F_q)` a fourth way: by enumerating ordered symplectic bases. It evaluates readability and `K_null` by brute
    force on explicit support states.
  - No computation was run on any OI mechanism.

## Verdict: **ACCEPT WITH NITS** (housekeeping only)

All four of the owner's criteria (#1210 c.6742225689) are met. Nothing in r7a changes a claim, proof or hypothesis
that I find wrong, and no scientific nit remains. The nits below are provenance and identification items (H1–H4). None
of them touches a claim's content. H1 corrects a citation that the brief describes as already applied. It is not
applied in the file.

## The owner's criteria

| criterion | status | basis |
| --- | --- | --- |
| **N1.** The false sharp-meter statement is corrected everywhere it matters, without introducing a necessity claim about SA-1(c) | **met** | See below |
| **N2.** Meter–carrier independence is in the new proof's hypotheses and reflected in its stated scope | **met** | See below |
| The 12 disproved entries, 64/64 checks and other previously accepted findings remain valid | **met** | See below |
| No new hypotheses or conclusions have been silently introduced | **met**, with the provenance item H1 | See below |

**N1.**
- **The grep.** `sharp|known displacement|K_null|known meter slot` was run over the four specifications: 61 matching lines.
  "Known displacement and `K_null = id`" occurs nowhere.
- **The three corrected sites**, QX-4 R4.9, QX-4 A4.4's Consequence and SHARED T2, now read: "with a sharp meter that
  kick is a known displacement: the identity when the meter's conjugate slot is sharp at 0 (Q4-D8), and in no case a
  disturbance in AP1's sense". Each clause is true:
  - the reciprocal coupling's silent action is `x ↦ x ± m′`;
  - it is the identity iff `m′ = 0`;
  - with a known slot it is never a disturbance, by AP1:323-325.

  p15 (5b) checks every sharp state at `q = 2` and at `q = 3`, where the coupling `x ← x − m′` is symplectic.
- **The other sharp-meter sites** are existential or scoped, and none is universal:
  - Q4-P19 (ii), §1 M16 and the §9 null-result row say "need not";
  - Q4-D8 and its count line;
  - the §9 M15 row;
  - the Q4-P20 remark;
  - T9 and the `A_4`/ABL rows concern sharp mediators and supplies, and are unchanged.
- **No necessity claim about SA-1(c).**
  - Every SA-1(c) site added or kept is sufficient-direction: "when …", "for example by keeping …", "from a meter
    supplied under SA-1(c)".
  - The only necessity words on added lines are pre-existing reflowed text, quoted owner words, and "not a necessary
    one".
  - Two sites state non-necessity explicitly, and both are correct: the Q4-P20 remark, and Q4-O9's "a sufficient route
    … not a necessary one (Q4-P20; Q4-D8)". The witness is the 144 of 288 sharp-meter readable LP recorders at `F_2`,
    and 10,368 of 15,552 at `F_3`, that have `K_null ≠ id` by a nonzero known displacement (p14 (5a); p15 (4a)–(4c)).
  - The M15 row's "rests on" concerns a *disturbance* in AP1's sense, not `K_null ≠ id`. It is supported within its
    affine-symplectic, location-preserving scope by the coefficient-1 argument (p15 (4b), (4d)).

**N2.**
- **The hypothesis.** Q4-P20's second hypothesis now reads: "… independently of the carrier (SA-1(c), AP1:297-299),
  so that on each branch the support is the product of the carrier's `x`-values and that line".
- **The proof** cites it at the readability step ("(second hypothesis)"). The `K_null` step's "varying `x` and then
  the meter along the line" uses the same product.
- **The scope.** The remark lists "the product support" among what the proof uses, beside "Location preservation is
  not used". So the stated scope is now the scope proved.
- **Downstream sites.** Every downstream statement of Q4-P20 carries SA-1(c), which contains the independence clause:
  - §1 M16;
  - §2 M16 × QX-4;
  - §3;
  - §9's null-result and SA-1(c) rows;
  - Q4-D8's restatement;
  - QX-4 R4.9 and A4.4.
- **Independence is load-bearing.** p15 (6a) uses a correlated family different from p14 (5e): `m′` known, and
  `m = s·x + t·c`.
  - Readable symplectic parts with constant `x′ − x` on the `c = 0` support exist: 216 per family at `q = 2`, and
    12,096 at `q = 3`.
  - None of them is location-preserving.
  - Under the product law on the same line there are none (p15 (6b), control).

**Previously accepted findings.**
- **p14.** It was re-run with `python3 -I`. It exits with 0, passes 64 of 64, and its output is byte-identical to
  `p14_r7rev_meter_supply.out`.
- **The 12 disproved entries.** Q3-D1, Q4-D1–Q4-D7 and Q6-D1–Q6-D3 are byte-identical to r7, compared entry by entry.
  Q4-D8's claim, counterexample and membership are byte-identical to r7. It gains only the count clause "the other 144
  have `K_null ≠ id` only by a nonzero known displacement", which p14 (5a) and p15 (4c) reproduce. All 12 remain valid.
- **The other r7-accepted items** are unchanged outside the 21 hunks: B1 items 1–7, r6 N1–N11, Q6-P12 and §9's
  three-column rows.

**The hunks.** `diff -u r7/ .` has 21 hunks: QX-3 2, QX-4 3, QX-6 2 and SHARED 14. Each traces to an item.

| item | hunks |
| --- | --- |
| N1 | QX-4 R4.9; QX-4 A4.4; SHARED T2 (§4); QX-4 §10's AP1 row (the citation consequence) |
| N2 | SHARED §8 Q4-P20, hypothesis and proof step |
| N3 | SHARED §9 SA-1(a) row |
| N4 | SHARED Q4-O3 |
| N5 | Q4-P20's conclusion, step 3 and remark; Q4-D8's count line |
| O1 | SHARED §0 "P1–P14"; Q4-P20's label; §7's r7-review row; §8's X rule |
| O2 | §9 M15 row |
| O3 | QX-6 A6.2 and §8 item 2; SHARED §3 "Counting", §5 QX-6 and §8.4 |
| O4 | QX-3 §0 and its references row; SHARED §7's owner-records row |
| Q4-O9 | the new entry; its cross-references in §1 M16 and the Q4-P20 remark |

No hunk falls outside these items.

## Q4-P20's stronger conclusion: independent check

**The conclusion.** "`x′ − x` is not constant on the states of the support with `c = 0`. In particular `T` changes
`x` on some such state, so `K_null ≠ id` on its silent branch, and its action on `x` there is not a known
displacement."

**The proof, re-derived.**
1. *Bracket preservation.* `MᵀJM = J` gives `{φ∘M, ψ∘M} = {φ, ψ}`. The functionals `x` and `f` lie in different
   symplectic pairs, so `{x, f} = 0`.
2. *Readability.* Under the product support, the differences on each branch span `e_x` and the line's direction `d`,
   with `ℓ(d) = 0`. The annihilator of `span{e_x, d}` is `span{c, ℓ}`. Constancy of `f∘T` on each branch gives
   `f∘M = αc + λℓ`. Because `ℓ = k` on both branches, the branch difference is `α`, so `α ≠ 0`. The translation `b`
   adds the same constant to every value and cancels.
3. *The constant case.* "`x′ − x` constant on the `c = 0` support" means `x∘M − x` kills `e_x` and `d`, again with
   `b_x` cancelling. So `x∘M = rc + x + ρℓ`. This is the same step as the weaker r7 hypothesis, so the stronger
   conclusion costs nothing.
4. *Contradiction.* `0 = {x, f} = {rc + x + ρℓ, αc + λℓ} = α{x, c}`, and `{x, c} = ±1`. So `α = 0`, a contradiction.
5. *"In particular".* A non-constant `x′ − x` is nonzero somewhere on the support, so `K_null ≠ id`. Every support
   state has positive weight under the uniform law. Being non-constant, it is not a translation by a known amount.

The proof is correct as stated, over any field. Its scope matches its hypotheses.

**The sharp-meter remark.**
- `c∘M = c` for a location-preserving map. Bracket preservation then gives `{c, x∘M} = {c, x}`. Since
  `{c, φ} = φ_x·{c, x}`, `x∘M` has coefficient 1 on `x`. With `c`, `m` and `m′` known on each branch, `x′ − x` is a
  known constant there. This is correct.
- "Zero on the silent branch for some readable recorders (Q4-D8) and nonzero for others" is correct (p15 (4a)–(4c)).
- "The conclusion fails" is correctly scoped by the colon clause to location-preserving maps.

**p15 results.** It passes 33 of 33 and exits with 0, in 69 s. Everything is exact, apart from the b-independence
spot check (2g), which is a seeded sample.

| section | what it checks | result |
| --- | --- | --- |
| (1) | `Sp(4, F_q)` by symplectic-basis enumeration | orders 720 and 51,840. At `q = 2` it equals a brute-force filter of all 65,536 matrices |
| (2a)–(2c) | `F_2`, all 11,520 affine-symplectic maps and the 384 location-preserving ones, 6 SA-1(c) laws | 4,608 and 192 readable per law. **No readable map has `x′ − x` constant on the `c = 0` support** |
| (2d)–(2f) | `F_3`, the 17,496 location-preserving maps, 12 laws; `x` restricted to each pair of values | 11,664 per law; no constant `x′ − x` |
| (2g)–(2i) | `F_3`, all 51,840 linear parts, 12 laws; b-independence verified on a sample | 15,552 per law; no constant `x′ − x` |
| (3a) | every readable `(M, f)`: `F_2`, all maps; `F_3`, location-preserving | 6,912 cases: `f∘M = αc + λℓ` with `α ≠ 0`, and `{x∘M, f∘M} = 0` |
| (4) | sharp meters | per sharp state, (288, 144) at `F_2` and (15,552, 5,184) at `F_3`. Every readable LP recorder is a known displacement on each branch, and `(x∘M)_x = 1` for every LP symplectic part |
| (5) | N1 | as above. Meter `(0, 1)`: readable, `x ↦ x + 1` (the r7 sentence was false) |
| (6) | N2 | as above |
| (7) | the copy coupling (not symplectic) under SA-1(c) | readable, `K_null = id` |

**Assumption-watch (§A.31; POSITIVE for the text as written, NEW as a scope fact; no change required).** "Not a known
displacement" does not entail a disturbance in AP1's sense outside the location-preserving class.
- **Non-location-preserving maps.** Among readable SA-1(c) recorders that are not location-preserving, `x′ − x` can
  vary only through the carrier's own `x`. That is, `(x∘M)_x ≠ 1` with no dependence on the meter's unknown slot. For
  the first law this holds for 96 of 288 readable linear parts at `F_2`, and 3,888 of 15,552 at `F_3` (p15 (8)).
- **Location-preserving maps.** `(x∘M)_x = 1`, so non-constancy means dependence on the unknown meter slot. That is
  AP1's disturbance.
- **Effect on the text.** The specification says only "not a known displacement", which is true, and never says that
  Q4-P20 yields a disturbance. So nothing is overstated. The fact bears on Q4-O9's predictable-versus-irreducible
  distinction, and the writer may record it there.

## Housekeeping (apply before the freeze decision; no content change)

- **H1. Q4-O9's provenance.**
  - **As written.** Q4-O9 cites "(owner question, amaybaum, session chat, 2026-11-09)". The brief says it is cited to
    c.6742225689. It is not, and no specification cites c.6742225689.
  - **The record.** #1210 c.6742225689 (amaybaum, 2026-11-09T14:14:59Z) quotes the question verbatim. The text in
    Q4-O9 matches it exactly.
  - **Fix 1.** Re-cite the label to that record, with author and time (§A.42 item 7).
  - **Fix 2.** That record does **not** contain the note "the distinction between a predictable, correctable kick and
    an irreducible disturbance may bear on the question". So "Per the same owner record" would become a
    misattribution. Remove the sentence, or attribute it separately as an unrecorded session-chat remark. Removing it
    is cleaner, since nothing relies on it.
  - **Fix 3.** Add c.6742225689 to QX-3 §0's list of owner records, to QX-3's references row and to SHARED §7's
    owner-records row.
  - **DISPOSITIONS-r7a.** Its "no GitHub record of this direction was read" is accurate for its own time. The record
    now exists.
- **H2. Self-identification.** All four titles say "(draft r7)". The §0 "Revisions" pointers name `r1/`–`r6/` and
  `DISPOSITIONS-r7.md`. The r7 text is now under `r7/`, and the record is `DISPOSITIONS-r7a.md`. A freeze decision
  needs the frozen scope to name itself exactly, so update these in all four files.
- **H3. The AP1 line range.**
  - **As written.** Six sites cite "AP1:320-323" for the known-displacement sentence:
    - QX-4 R4.9;
    - QX-4 A4.4's Consequence;
    - QX-4 §10's AP1 row;
    - SHARED T2;
    - Q4-D8;
    - the §9 M15 row.
  - **What the range holds.** At `fd539e15` that sentence is at :323-325. :320-323 holds only the disturbance sentence
    and the first two words of the quote.
  - **Fix.** Use :320-325. The Q4-D8 and M15 instances predate r7a, and r7a's N1 text copied the range from the r7
    review's suggested wording.
- **H4. SHARED §7's AP1 row.**
  - **As written.** The row is "Substratum…; AP1:282-350, :415-421 | §9". Its range covers :297-299 and :320-325, but
    its cited-in column lists §9 only.
  - **Where AP1 is cited.** §4 T2 (new in r7a), and §8 Q4-P20 (:297-299, new in r7a) and Q4-D8.
  - **Fix.** Add "§4 T2; §8 Q4-P20, Q4-D8" to the cited-in column (§A.42 item 8 completeness).

## Optional

- **O1.** §9's null-result row could add "(Q4-O9)" after "this route gives no QM-independent support", matching §1
  M16. This is not a scope error: the row already states the open status.
- **O2.** p15 independently reproduces the stronger form, `x′ − x` non-constant, at every scope that p14 (2) and (3)
  cover. With p15 cited, the label's "computation-supported by p14 (2) alone for the conclusion's first sentence" and
  "p14 (3) alone" could become X. That would also mean adding P15 to §8's reviewer list and SHARED §0's range.
- **O3.** QX-4 R4.9 says "when the meter's conjugate slot is unknown (SA-1(c))". This is a paraphrase narrower than
  SA-1(c), which requires the slot to be unknown, uniform and independent. The tag makes it adequate. "When the meter
  is supplied under SA-1(c)" would be literal. This text predates r7a.

## The writer's "not changed" list: assessment

| item | matters for freeze? |
| --- | --- |
| Titles "(draft r7)" | **yes**, H2 |
| §0 revision pointers name `r6/` | **yes**, H2 |
| SHARED §7's AP1 row | **yes**, minor, H4 |
| §9 null-result row without a Q4-O9 cross-reference | no, O1 |
| Q4-O9's record id c.6742225689 | **yes**, H1. Re-cite it, and drop or re-attribute the note sentence |

## Scope, register and authorization

**Scope.**
- Every changed summary and table site was checked against its proof's scope: §1 M16, §2, §3, T2, §5, §8.4, §9's
  SA-1(a), null-result and M15 rows, QX-4 R4.9, A4.4 and §10, and QX-6 A6.2 and §8. Each matches.
- §9 SA-1(a) (N3) now ends Main:726's list at (vii). P3 is typed as a design posit, not an OI principle, and the
  standing carries the P3 condition. This matches Main:726 and AP1:290-291.
- Q4-O3's addition states the open forms of Q4-D8's claim. They are non-affine couplings, and supplies outside
  Q4-P20's hypotheses other than sharp meters, where Q4-D8 refutes the claim.

**Register (§A.32, §A.33).**
- All 67 added lines were scanned.
- Capitals of four or more letters occur only in identifiers: SHARED, MECH-OPEN, REVIEW, ANTIBUNCHING, DESIGN.
- There is no history phrase, reader instruction or self-assessment.
- "Independently reviewed" in Q4-P20's label is a status label, in the idiom of §8.

**Authorization.**
- No added line mentions a freeze, a dispatch, a construction or D19–D23.
- The §0 blocks keep "no criterion is frozen".
- DISPOSITIONS-r7a keeps Q-C2-1's D19–D23 separate.
- The owner record c.6742225689 authorizes no freeze, and this review implies none.

## Probes

| probe | sha256 | result |
| --- | --- | --- |
| `p14_r7rev_meter_supply.py` (re-run) | `cd8be1e1f53f2e75…` | 64 of 64; exit 0; byte-identical to `p14_r7rev_meter_supply.out` (`d4064e3afb1ebe72…`) |
| `p15_r7arev_stronger_conclusion.py` (this review; imports nothing earlier; standard library; generic objects only) | `a598c0ed53ec32a0a1e57c27902a81ba5a00c655c9ba1e06197e2b446fe1da87` | 33 of 33; exit 0; output `p15_r7arev_stronger_conclusion.out` (`fbe85c2d76902b58f9399c34d0a7020a830b29ee2325283956ec86e12edd08c7`) |

## Readiness

- **The content is ready** for the owner's freeze decision. The four criteria are met, and no claim, proof, hypothesis
  or disproved entry needs change.
- **Before freeze,** apply H1–H4. They are mechanical and change no content.
- **Confirming them** needs only a diff check that the changes are confined to those sites, not a further full review.
- O1–O3 are at the writer's discretion.
