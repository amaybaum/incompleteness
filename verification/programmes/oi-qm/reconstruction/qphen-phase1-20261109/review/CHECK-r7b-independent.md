# QPHEN Phase 1 r7b: independent housekeeping check (r7a → r7b)

## Standing

- Model-written, read-only on the repository, git and GitHub. It writes only this file. Two read-only GitHub API
  reads (`gh api repos/amaybaum/incompleteness/issues/comments/<id>`). One inline, file-less exact computation on a
  generic object (the reciprocal coupling over `F_2`, check 3); no computation on any OI mechanism.
- `review/CHECK-r7b-diff.md` (the writer's self-check) was not read or relied on.
- **Hashes verified before reading** (all match the brief):

  | file | sha256 |
  | --- | --- |
  | `r7a/QX3-ANTIBUNCHING.md` | `baf3de3cc5807a36a3ee265ddf178c3aa23b0028050de5ecaabbb75929e2f024` |
  | `r7a/QX4-INCOMPATIBILITY-LG.md` | `6b45c062bb5a6b1cbf7dabcaf15a8531d21e089f40b3bee9132a4b40ff7c1248` |
  | `r7a/QX6-BELL-CHSH.md` | `b77f0984a282603bb6ee2af3941d6bbe3f4fa696b220272329a241affbaa83fc` |
  | `r7a/SHARED-MECHANISM.md` | `ab69695e33e7e805d4cf49cb3704807ba77637f5feba9c257a0c57ce30dce3e5` |
  | `QX3-ANTIBUNCHING.md` (r7b) | `4a686c6deb9e051a5e04f01bc3f28484c663dcfee0b19794b807e291bcdcd8f9` |
  | `QX4-INCOMPATIBILITY-LG.md` (r7b) | `cafdd3210f3d295bc88aef252d503cc80b1e2492a5eaa40d86162534e375587e` |
  | `QX6-BELL-CHSH.md` (r7b) | `f915ab8892de5e2fd2e4016f3133af00d5aaa156958e4848fc7023fac653000c` |
  | `SHARED-MECHANISM.md` (r7b) | `4c26576a269ef38c73dd3ae3a8ec5a95f03ee5ca0bf531dbb4644dcfea21fc72` |
  | `DISPOSITIONS-r7b.md` | `0080ac328cb38085e99fa8f38ccbe1aec18f732298c8acaaea9b6a153abaddcf` |
  | `review/REVIEW-PHASE1-r7a.md` | `88fea7f348e17d5cf9407a4720db97956c2e1bf192fd72f647b62e110695bf5d` |
  | `review/probes/p14_r7rev_meter_supply.py` | `cd8be1e1f53f2e7571111e8f576c500f120481067ac18ce84d443ce4ccecb69d` |
  | `review/probes/p15_r7arev_stronger_conclusion.py` | `a598c0ed53ec32a0a1e57c27902a81ba5a00c655c9ba1e06197e2b446fe1da87` |
  | `review/probes/p15_r7arev_stronger_conclusion.out` | `fbe85c2d76902b58f9399c34d0a7020a830b29ee2325283956ec86e12edd08c7` |

- **Method.** `diff -u r7a/<f> <f>` for the four specifications (18 hunks: QX-3 3, QX-4 5, QX-6 1, SHARED 9), and a
  token-level `git diff --no-index --word-diff` listing every changed token. §8 entries were counted by ID. Q4-P20
  was extracted from both versions and diffed. p14 and p15 source was read for what each section computes.

## Summary

| # | check | result |
| --- | --- | --- |
| 1 | every change maps to H1–H4, O1–O3 or a declared extra | **PASS** |
| 2 | no claim, proof, hypothesis, ledger status or count changed; §8 = 81 (44/12/25); Q4-P20 body byte-identical | **PASS** |
| 3 | O3 at R4.9 neither strengthens nor weakens relative to the cited proofs | **FAIL** (first occurrence only) |
| 4 | O2's computation labels | **FAIL** (understatement only; no overclaim) |
| 5 | cited GitHub comments match | **PASS** |

Neither failure is an overclaim in the sense of a stronger proved result being asserted. Check 3's finding is a literal
scope extension of one sentence onto a case where it is false; check 4's is a support label that is weaker than the
evidence. Both are local, one-sentence fixes.

## 1. Mapping of every change — PASS

| site | change | item |
| --- | --- | --- |
| four titles | "(draft r7)" → "(draft r7b)" | H2 |
| four §0 "Revisions" | adds `r6/`, `r7/`, `r7a/`; record `DISPOSITIONS-r7b.md` (reflowed in QX-3/4/6) | H2 |
| QX-4 §0, QX-6 §0, SHARED §0 Conventions | "`QX3-ANTIBUNCHING.md` §0 (r7)" → "(r7b)" | declared extra (H2 tags) |
| SHARED §0 Inputs | "specifications (r7)" → "(r7b)" | declared extra (H2 tags) |
| QX-3 §0 owner-record list | adds c.6742225689 (Q4-O9 question) and c.6742554738 (kick note) | H1 fix 3; H1 fix 2 (separate attribution) |
| QX-3 §10 owner-records row | adds c.6742225689, c.6742554738 | H1 fix 3 |
| QX-4 R4.9 | "AP1:320-323" → ":320-325"; two occurrences of "meter's conjugate slot is unknown (SA-1(c))" → "meter is supplied under SA-1(c)" | H3; O3 |
| QX-4 A4.4 Consequence; QX-4 §10 AP1 row | ":320-323" → ":320-325" | H3 |
| SHARED §0 | "P1–P14" → "P1–P15" | O2 |
| SHARED T2; Q4-D8; §9 M15 row | ":320-323" → ":320-325" | H3 |
| SHARED §7 new row | r7a review + p15, cited in §8 Q4-P20 | declared extra (O2) |
| SHARED §7 owner-records row | adds c.6742225689, c.6742554738; cited-in adds "§8 Q4-O9" | H1 fix 3; declared extra (H1) |
| SHARED §7 AP1 row | cited-in "§9" → "§4 T2; §8 Q4-P20, Q4-D8; §9" | H4 |
| SHARED §8 X rule | "P12 and P14" → "P12, P14 and P15" | O2 |
| SHARED Q4-P20 label | support label rewritten (see check 4) | O2 |
| SHARED Q4-O9 | label re-cited to c.6742225689 with time; note sentence replaced by verbatim owner note cited to c.6742554738 | H1 fixes 1–2 |
| SHARED §9 null-result row | "… QM-independent support" → "… support (Q4-O9)" | O1 |

No token changed outside these sites. Stale strings ("320-323", "(draft r7)", "§0 (r7)", "specifications (r7)",
"session chat", "Per the same owner record", "conjugate slot is unknown", "P1–P14", "P14 by reviewers") occur 0 times
in the four r7b specifications. Register scan of the 40 added lines: four-plus capitals only in identifiers (SHARED,
ANTIBUNCHING, DISPOSITIONS-r7b, DECISIONS, DESIGN, MECH-OPEN, NCONS, QPHEN, CHSH, REVIEW-PHASE1-r7a); no history
phrase, reader instruction or self-assessment.

Note (not a failure): H1 fix 2 offered "remove, or attribute separately as an unrecorded session-chat remark". The
writer attributed it to a new record (c.6742554738) and replaced the paraphrase "may bear on the question" by the
verbatim "may be important for that investigation". This is within H1's intent and is declared under H1.

## 2. No content change; counts — PASS

- §8 entries by ID, r7a and r7b identical: proved 44 (Q3-P1–P11 with Q3-P6a = 12; Q4-P1–P20 = 20; Q6-P1–P12 = 12),
  disproved 12 (Q3-D1; Q4-D1–D8; Q6-D1–D3), open 25 (Q3-O1–O6; Q4-O1–O9; Q6-O1–O10); total 81. §8.4 is
  byte-identical.
- The only §8 hunks are the X rule, Q4-P20's label, Q4-D8's AP1 line range and Q4-O9's citation/note. No entry's
  claim, hypotheses, counterexample or status word changed.
- Q4-P20: from "Hypotheses:" to the entry's end the r7a and r7b texts have the same sha256
  (`b0e08cca03d471b282f98eea658bfc9322226ecb78314044bb78ea4b71c130f3`); only the bracketed label differs.

## 3. O3 at QX-4 R4.9 — FAIL (first occurrence); second occurrence PASS

- **SA-1(c) as the specifications use it.** AP1:297-299: "Every supplied ready cell has exactly one known linear
  functional. Its other slot is unknown and uniformly distributed, independently of everything else." Q4-P20's
  hypothesis instantiates this as a uniform law on `{ℓ = k}` for *any* nonzero `ℓ` of `(m, m′)`, and p14 (7b) treats
  "`m′` known, `m` unknown" as an SA-1(c) law. So "supplied under SA-1(c)" does not imply that `m′` is unknown.
- **Second occurrence** ("… when the meter is supplied under SA-1(c) every such coupling that records readably is
  null-result invasive (SHARED Q4-P20)"): this is now word-for-word Q4-P20's hypothesis, and Q4-P20 holds for every
  `ℓ`. Neither stronger nor weaker than the cited proof. PASS.
- **First occurrence** ("That kick acts on both branches, so the reciprocal coupling is null-result invasive (A4.4)
  when the meter is supplied under SA-1(c)"): the r7a condition "the meter's conjugate slot is unknown" excluded
  `ℓ = m′`; the r7b condition admits it. Exact check over `F_2`, reciprocal coupling
  `(c, x, m, m′) ↦ (c, x + m′, m + c, m′)` (symplectic), under each SA-1(c) law:

  | `ℓ` | `k` | `m′` unknown | readable | `K_null = id` |
  | --- | --- | --- | --- | --- |
  | `m` | 0, 1 | yes | yes | no |
  | `m + m′` | 0, 1 | yes | yes | no |
  | `m′` | 0 | no | no | **yes** |
  | `m′` | 1 | no | no | no (known displacement) |

  Under the SA-1(c) law `ℓ = m′, k = 0` the reciprocal coupling has `K_null = id`, so the r7b sentence is literally
  false there (the kick is zero and does not "act on both branches"). The coupling does not record readably under that
  law (p14 (7b) agrees), which limits the practical effect, but the sentence does not restrict to readable recording.
  The cited support, A4.4's Consequence, still says "with its kick from the meter's unknown slot (SA-1(c); …)", which
  the r7b first clause no longer requires. The rewording therefore narrows in one direction (uniform, independent) and
  extends in another (`m′` known), onto a case where the claim fails. DISPOSITIONS-r7b's "narrows wording to the proved
  scope and alters no claim" does not hold for this occurrence. The r7a review's O3 suggestion has the same gap.
- **Minimal fix.** At the first occurrence only: restore r7a's wording, or write "when the meter is supplied under
  SA-1(c) with its conjugate slot `m′` unknown".

## 4. O2's computation labels — FAIL (understatement; no overclaim)

- **Correct.** First sentence of Q4-P20's conclusion ("`x′ − x` is not constant on the `c = 0` support") at all
  11,520 affine-symplectic maps of `F_2⁴` (incl. the 384 LP) and the 17,496 LP maps of `F_3⁴`: p14 (2) computes
  constancy of `x′ − x` on explicit affine maps ("x'-x constant on silent support 0"), and p15 (2a)–(2c) and (2d)–(2f)
  compute it independently. X is earned. The new "X: p14 (3) and p15 (2g)–(2i) for all 51,840 × 81" (for
  `K_null ≠ id`) is also earned. §8's X rule (P15 by reviewers) and SHARED §0 "P1–P15" are correct. The new §7 row is
  accurate.
- **Not correct.** "computation-supported by `p15_r7arev_stronger_conclusion.py` (2g)–(2i) alone for the conclusion's
  first sentence there" (51,840 × 81). p14 (3) tests the same quantity:
  - p14 (3b) counts readable linear parts with `len(g_values(M, S, 3)) == 1`, where `g_values` is the set of values of
    `x∘M − x` on the `c = 0` support, over all 51,840 linear parts and 12 laws; `bad == 0`.
  - p14 (3a) verifies on explicit maps over all 81 translations (q = 3, first 200 LP parts) that `x′ − x` is
    non-constant exactly when `g` is non-constant (the `nc == gc` failure test).
  - Independently of the code: over a translation-closed class, "no map has `K_null = id`" is equivalent to "no map
    has `x′ − x` constant on the silent support", because a constant `g` is cancelled by choosing `b_x = −g`.
  So the first sentence at 51,840 × 81 is checked by both p14 (3) and p15 (2g)–(2i), with the same exact reduction,
  and qualifies for X. DISPOSITIONS-r7b's "p14 (3) tests only `K_null = id`, not the constancy of `x′ − x`" is
  incorrect about p14's code. The r7a label had attributed this scope to p14 (3).
- **Effect.** The label is weaker than the evidence; nothing is overstated and no claim changes. If the brief's
  expected form is retained, the DISPOSITIONS rationale should at least not misdescribe p14 (3). Minimal fix: "X:
  p14 (3) and p15 (2g)–(2i) for all 51,840 × 81 affine-symplectic maps of `F_3⁴`, including the conclusion's first
  sentence".

## 5. GitHub comments — PASS

| id | issue | user | created_at = updated_at | content |
| --- | --- | --- | --- | --- |
| 6742225689 | #1210 | amaybaum | 2026-11-09T14:14:59Z | contains "Can OI derive a physically meaningful null-result disturbance principle independently of QM, without simply introducing SA-1(c) or an equivalent assumption?" verbatim; Q4-O9's quoted text matches exactly |
| 6742554738 | #1210 | amaybaum | 2026-11-09T14:29:19Z | contains "The distinction between a predictable, correctable kick and an irreducible disturbance may be important for that investigation." verbatim; Q4-O9's quote matches exactly (across a line break) |

Both are Claude-Code-generated records, under the owner's account, of words the owner wrote in session chat; the
specifications cite them by the GitHub author field, as for the earlier owner records. c.6742554738 was posted after
the r7a review, to supply H1's record.

## Findings (one line each)

- F1 (check 3): R4.9's first O3 rewording admits the SA-1(c) law `ℓ = m′, k = 0`, under which the reciprocal coupling has `K_null = id`; restore "conjugate slot `m′` unknown" there.
- F2 (check 4): p14 (3b) tests constancy of `x′ − x` at 51,840 × 81, so "computation-supported by p15 alone" understates (X is earned) and DISPOSITIONS-r7b's O2 rationale misdescribes p14 (3).
- F3 (note): H1's note sentence is now the owner's verbatim words from a new record, a permitted variant of H1 fix 2.
- All other changes are housekeeping as declared; counts 81 = 44 + 12 + 25 and Q4-P20's body are unchanged.
