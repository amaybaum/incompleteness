# QPHEN Phase 1 r7c: independent check of the r7b → r7c edits

## Standing

- Model-written, read-only on the repository, git and GitHub; no git or GitHub calls made. It writes only this file
  and `review/c7_check.py` (sha256 `a66b4987ac593c1b605d920f709800964d88f1805d43ad8764a5442a14d58417`), a
  standard-library exact script on a generic object (the reciprocal coupling over `F_2`) that imports no earlier
  probe. No computation on any OI mechanism. p14 was read, not re-run.
- `review/CHECK-r7b-diff.md` was not read.
- **Hashes verified before reading** (all match the brief):

  | file | sha256 |
  | --- | --- |
  | `r7b/QX3-ANTIBUNCHING.md` | `4a686c6deb9e051a5e04f01bc3f28484c663dcfee0b19794b807e291bcdcd8f9` |
  | `r7b/QX4-INCOMPATIBILITY-LG.md` | `cafdd3210f3d295bc88aef252d503cc80b1e2492a5eaa40d86162534e375587e` |
  | `r7b/QX6-BELL-CHSH.md` | `f915ab8892de5e2fd2e4016f3133af00d5aaa156958e4848fc7023fac653000c` |
  | `r7b/SHARED-MECHANISM.md` | `4c26576a269ef38c73dd3ae3a8ec5a95f03ee5ca0bf531dbb4644dcfea21fc72` |
  | `QX3-ANTIBUNCHING.md` (r7c) | `d50fc89790783ff79e2b8409fdd792b2b297613db6c005f3bf9c9b7900622d8f` |
  | `QX4-INCOMPATIBILITY-LG.md` (r7c) | `32213901791f8af0e470b1e87d0ee3c9e5091767849efc0cf835b35d32dd6a27` |
  | `QX6-BELL-CHSH.md` (r7c) | `df910657409981fefd8a27d9a545b761809956a9bce652da2a15f44d5b7a2e7d` |
  | `SHARED-MECHANISM.md` (r7c) | `fdaee64f0fb114492be70f0bcca1e80c3594c7c5b7686248f76b2963dae085d4` |
  | `DISPOSITIONS-r7c.md` | `856fa01d7010855a2f6dad75ce41b5c4adbf81d6f8d917b2cd20314253c1b0ba` |
  | `review/CHECK-r7b-independent.md` | `2e355f095a4a9175a2565c05df3fe010cd2b29a24129e60bf2d5e85172141203` |
  | `review/probes/p14_r7rev_meter_supply.py` | `cd8be1e1f53f2e7571111e8f576c500f120481067ac18ce84d443ce4ccecb69d` (as in the r7b check) |
  | `DISPOSITIONS-r7b.md` and `r7b/DISPOSITIONS-r7b.md` | both `0080ac328cb38085e99fa8f38ccbe1aec18f732298c8acaaea9b6a153abaddcf` (unchanged) |

- **Method.** `diff r7b/<f> <f>` and `git diff --no-index --word-diff=porcelain` for the four specifications, every
  changed token listed; §8 IDs extracted from both versions and compared; p14 source read for (3a)/(3b).

## Summary

| # | check | result |
| --- | --- | --- |
| 1 | every change is F1, F2 or housekeeping (title, §0 tags, revision pointers), nothing else | **PASS** |
| 2 | F1 is correct (exact, `c7_check.py`) | **PASS** |
| 3 | F2's evidence is real (p14 (3a)/(3b) read) | **PASS** (one precision note, N1) |
| 4 | nothing else changed; §8 = 81 (44/12/25); no claim, proof or hypothesis changed | **PASS** |

## 1. Change mapping — PASS

12 changed lines (QX-3 2 hunks, QX-4 4, QX-6 3, SHARED 5). Every changed token:

| site | change | item |
| --- | --- | --- |
| four titles | "(draft r7b)" → "(draft r7c)" | housekeeping |
| four §0 "Revisions" | list adds `r7b/` (`… r7/`, `r7a/` and `r7b/`); record `DISPOSITIONS-r7b.md` → `DISPOSITIONS-r7c.md` | housekeeping |
| QX-4 §0, QX-6 §0, SHARED §0 Conventions | "`QX3-ANTIBUNCHING.md` §0 (r7b)" → "(r7c)" | housekeeping (§0 tag) |
| SHARED §0 Inputs | "The three Phase 1 specifications (r7b)" → "(r7c)" | housekeeping (§0 tag) |
| QX-4 R4.9, first occurrence | "…null-result invasive (A4.4) when the meter is supplied under SA-1(c);" → "…supplied under SA-1(c) with its conjugate slot `m′` unknown;" | F1 |
| SHARED §8 Q4-P20 label | "computation-supported by `p15_r7arev_stronger_conclusion.py` (2g)–(2i) alone for the conclusion's first sentence there;" → "including the conclusion's first sentence there (p14 (3b) counts constancy of `x∘M − x` on the `c = 0` support, and p14 (3a) matches it to constancy of `x′ − x` over all 81 translations);" | F2 |

- **R4.9 second occurrence unchanged**: "…when the meter is supplied under SA-1(c) every such coupling that records
  readably is null-result invasive (SHARED Q4-P20)" is byte-identical to r7b; it remains word-for-word Q4-P20's
  hypothesis.
- No `r7b` self-tag survives in the four specifications other than the revision-list entry `r7b/` (one per file).
- Register scan of the added text: no capitals beyond identifiers, no history phrase, reader instruction or
  self-assessment.
- Propagation: the other SA-1(c) sites (SHARED M16 row, Q4-P20 hypothesis, Q4-D8 restatement) state Q4-P20's
  readable-recorder claim, which holds for every `ℓ`, and QX-4 A4.4's Consequence already reads "kick from the meter's
  unknown slot (SA-1(c); …)". None carries F1's defect, so none needed the qualifier.
- Cosmetic only: the changed lines in the three QX revision lists and SHARED Q4-P20 label line 523 were not reflowed
  (overlong source lines); rendering is unaffected.

## 2. F1 — PASS

`review/c7_check.py`, exact (`Fraction`) over `F_2`, reciprocal coupling `T(c, x, m, m′) = (c, x + m′, m + c, m′)`,
carrier `x` uniform on each branch, meter uniform on `{ℓ = k}` independently of the carrier. `K_null` is the exact
channel `P(x′ | x, c = 0)` with the meter marginalized. All 12 checks pass (exit 0):

| `ℓ` | `k` | `m′` unknown and uniform | `K_null` |
| --- | --- | --- | --- |
| `m` | 0, 1 | yes | `[[½, ½], [½, ½]]` ≠ id |
| `m + m′` | 0, 1 | yes | `[[½, ½], [½, ½]]` ≠ id |
| `m′` | 0 | no | **id** |
| `m′` | 1 | no | `[[0, 1], [1, 0]]` ≠ id (known displacement) |

- `T` is a bijection, linear, symplectic on all basis pairs, and location-preserving (0a–0c).
- `ℓ = m′`, `k = 0`: `K_null = id` (1a). So "supplied under SA-1(c)" alone does not give null-result invasiveness;
  the r7b wording was false on this law, as F1 states.
- Every SA-1(c) law with `m′` unknown and uniform (`ℓ ∈ {m, m + m′}`, `k ∈ {0, 1}`; exactly the laws with `ℓ ≠ m′`):
  `K_null ≠ id`, indeed fully randomizing (1c–1e). The r7c qualifier selects exactly these laws, so the sentence is
  now true on its whole scope and matches A4.4's Consequence.
- Controls: the identity map gives `K_null = id` under every law, the unconditional flip gives `K_null ≠ id` under
  every law (2a–2b).
- Minor, in `DISPOSITIONS-r7c.md` only (not a manuscript defect): its F1 row says that under the law `ℓ = m′` the
  reciprocal coupling has `K_null = id`; that holds for `k = 0`, while `k = 1` gives the known displacement `x ↦ x + 1`
  (1b). The r7b check's table states this correctly.

## 3. F2's evidence — PASS (note N1)

p14 read at the hash above:

- `g_values(M, S, q)` (lines 131–133) is the set of values of `(x∘M − x)(y)` over support states with `c = 0`.
- **(3b)** (lines 259–271): for each of the 12 SA-1(c) laws at `q = 3` and every one of the 51,840 symplectic linear
  parts `M`, it counts the readable parts (`readable_lin`) whose `g_values` is a single value, and requires
  `bad == 0`. This is a count of constancy of `x∘M − x` on the `c = 0` support, as the label says.
- **(3a)** (lines 247–258): for each tested `M`, law and every translation `b` (`q⁴` of them: 81 at `q = 3`), it
  builds the explicit affine map and fails on `nc == gc`, i.e. unless "`x′ − x` non-constant on the silent support"
  is exactly "`g` not constant"; it also checks that readability is `b`-independent and that `K_null = id` implies
  `g` constant. This is the match the label describes.
- The reduction (3a) controls is exact algebra for every map: on each support state
  `x′ − x = (My + b)_x − y_x = (x∘M − x)(y) + b_x`, so `x′ − x` is constant on the `c = 0` support iff `g` is, for
  every `b`; and `f(My + b) = f(My) + f(b)`, so readability does not depend on `b`. With (3b) this gives the first
  sentence of Q4-P20's conclusion at all 51,840 × 81 maps of `F_3⁴`, independently of p15 (2g)–(2i). The X mark is
  earned, and the r7c label is not stronger than the evidence.
- **N1 (precision, non-blocking).** (3a) runs over every translation, but only for all 720 linear parts at `q = 2`
  and the first 200 of the 648 location-preserving parts at `q = 3`, each with the first four laws (`lines(q)[:4]`).
  The label's "p14 (3a) matches it to constancy of `x′ − x` over all 81 translations" is literally accurate but can
  be read as covering all 51,840 parts. The 51,840 × 81 scope rests on (3b) plus the exact identity above, of which
  (3a) is a sampled explicit-map control. An optional tightening: "p14 (3a) checks that match on explicit maps over
  all 81 translations (200 location-preserving parts, four laws)".

## 4. Nothing else changed — PASS

- §8 IDs extracted from both versions are identical (81): proved 44 (Q3-P 12 incl. Q3-P6a; Q4-P 20; Q6-P 12),
  disproved 12 (Q3-D 1; Q4-D 8; Q6-D 3), open 25 (Q3-O 6; Q4-O 9; Q6-O 10).
- The only §8 difference between r7b and r7c is Q4-P20's bracketed label (two source lines). Its hypotheses,
  conclusion, proof and exhaustive counts are unchanged. Outside §8 the only content change is F1's qualifier, which
  narrows one sentence to the scope on which it holds; no claim, proof, hypothesis, status word or count changed.

## Findings (one line each)

- Check 1 PASS: every change is F1, F2 or the declared title/§0-tag/revision-pointer housekeeping; R4.9's second occurrence is unchanged.
- Check 2 PASS: exact over `F_2`, the reciprocal coupling has `K_null = id` under SA-1(c) with `ℓ = m′, k = 0`, and `K_null ≠ id` (fully randomizing) under every SA-1(c) law with `m′` unknown.
- Check 3 PASS: p14 (3b) counts constancy of `x∘M − x` on the `c = 0` support over 51,840 parts × 12 laws, and (3a) checks its match to `x′ − x` on explicit maps over all translations; N1: (3a) is a sampled control (200 LP parts, four laws at `q = 3`), the full scope resting on (3b) and an exact identity.
- Check 4 PASS: §8 = 81 (44/12/25), IDs identical, no claim, proof or hypothesis changed.
- Note: DISPOSITIONS-r7c's F1 row says `K_null = id` under `ℓ = m′` without "`k = 0`"; the manuscript text is unaffected.
