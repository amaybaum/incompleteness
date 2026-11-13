# QPHEN Phase 1 r7a: dispositions of `review/REVIEW-PHASE1-r7.md` (`42edbb6c…`)

## Scope and standing

- This record is paper-only and model-written. It made no repository, git or GitHub writes. It made two read-only
  GitHub API reads: the two owner records quoted under O4.
- No computation was run on any OI mechanism. No new probe was written. The reviewer's
  `p14_r7rev_meter_supply.py` (`cd8be1e1f53f2e75…`) was re-run with `python3 -I` from a separate directory. It exited
  with 0, and its output is byte-identical to `p14_r7rev_meter_supply.out`
  (`d4064e3afb1ebe72ab69efebf6aec8a50c5b94a0621ffcc7cbe73c73db84767f`), 64 of 64.
- Q-C2-1's D19–D23 stay separate. This revision implies no freeze, dispatch, construction or implementation approval.
- **Inputs.**
  - The r7 review, `42edbb6c70aeac15cf447657bd8376b64e1d90631173f73d64f954731ff07efa`, verified before reading. Its
    verdict is ACCEPT WITH NITS: must-fix N1 and N2, precision N3–N5, optional O1–O4.
  - One owner addition, relayed by the coordinating session (below, "Owner-directed").
- **Corpus check.**
  - The commit `fd539e150759a6ea51ab279aeeac80fc06050ade` was read with `git show`, with no fetch, depth, gc or prune.
  - `papers/Main.md` at that commit equals `main_fd.md` (`6144cd4a…`).
  - AP1 (`verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`) was read at that commit, at
    :278-330:
    - :290-291: "per-tick, per-edge arming is not native";
    - :297-299: SA-1(c), "Every supplied ready cell has exactly one known linear functional. Its other slot is unknown
      and uniformly distributed, independently of everything else";
    - :320-325: "Given (c) and N2, that slot is unknown and uniform, so the shift is a disturbance. With a known
      meter slot the shift would be a known displacement and no disturbance."
  - Main:726 lists isotropy as posit (vi). It contains no per-edge arming and no P3.
- **The r7 texts** were copied unchanged into `r7/`:

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `b6effd8a8a7364648c70250cc7258e2531a1317913eb109870837af1ee059b90` |
  | `QX4-INCOMPATIBILITY-LG.md` | `6497d64efae0cedacd2ebc7e316c22c6797d0f798dd326dc34a5d47b295a0627` |
  | `QX6-BELL-CHSH.md` | `33b01deb08aec45f6f3da18a6005ff86f9c244fe87fcd8bc265b562bdaeaaa3c` |
  | `SHARED-MECHANISM.md` | `1aad26d1c5db83962c918ba76106d8548cc815c3fa66dfa982b589615131331a` |
  | `DISPOSITIONS-r7.md` | `98e17956d0dc7bfe0f98d0bccc59225d29c380de2773d91a51a9882dff854458` |

  `DISPOSITIONS-r7.md` is a record. It is not edited, and it is also kept unchanged at the top level.

## Items

| item | verified against | exact change (r7a) |
| --- | --- | --- |
| **N1** (the sharp-meter sentence) | AP1:320-325. The reciprocal coupling's silent action with a sharp meter `(m, m′)` is `x ↦ x + m′`, which is the identity iff `m′ = 0`. p14 (7a): with the meter `(0, 1)` it records readably and `K_null ≠ id` | **QX-4 R4.9**: "; with a sharp meter the kick is a known displacement and `K_null = id` (SHARED Q4-D8)." becomes "; with a sharp meter that kick is a known displacement: the identity when the meter's conjugate slot is sharp at 0 (SHARED Q4-D8), and in no case a disturbance in AP1's sense (AP1:320-323)." **QX-4 A4.4 Consequence** and **SHARED T2**: "With a sharp meter that kick is a known displacement and `K_null = id` (…Q4-D8)" becomes the review's sentence, "With a sharp meter that kick is a known displacement: the identity when the meter's conjugate slot is sharp at 0 (…Q4-D8), and in no case a disturbance in AP1's sense (AP1:320-323)". The wording is the review's, with two adaptations: the file's `SHARED` prefix in QX-4, and a lowercase "with" after R4.9's semicolon. **Consequence (§A.42 item 8)**: QX-4 §10's AP1 row reads "AP1 §0 and :320-323 … \| R4.3; §2; R4.9 and A4.4's Consequence (the sharp-meter case)" |
| **N2** (independence from the carrier) | AP1:297-299, verbatim. The proof's readability and `K_null` steps vary `x` and the meter separately on each branch | **SHARED Q4-P20**, second hypothesis: adds ", independently of the carrier (SA-1(c), AP1:297-299), so that on each branch the support is the product of the carrier's `x`-values and that line". **Proof step 2** (readability) now opens "on each branch the support is the product of the carrier's `x`-values and the line (second hypothesis), so …". **The remark** lists what the proof uses as "symplecticity, the product support, and that the meter's known functionals commute" |
| **N3** (§9 SA-1(a) row) | Main:726: (vi) is isotropy, and the posit list contains no P3. AP1:290-291 | The P3 clause is removed from the Main:726 list, which now ends with (vii). After it the row adds: "For detector couplings on armed edges the coefficient symmetry rests instead on per-edge arming, one coefficient per undirected edge (SA-1(a′), P3), a design posit, not an OI principle." The standing gains "; for detector couplings on armed edges, conditional also on the design posit P3" |
| **N4** (Q4-D8's open forms) | Q4-O3's text, against Q4-D8's restatement | **Q4-O3** adds: "Also open: Q4-D8's claim for non-affine couplings, and for meter supplies outside Q4-P20's hypotheses other than a sharp meter, under which Q4-D8 refutes it." No new open ID is used for N4 |
| **N5** (stronger conclusion; SA-1(c) sufficient, not necessary) | The proof was re-derived by hand. "`x′ − x` constant on the silent support" puts `x∘M − x` in the annihilator of `span{e_x, d}`, which is `span{c, ℓ}`. Under the product support that is the same step as the original `K_null = id` case, so the proof gives the stronger form unchanged. The sharp-meter argument: `c∘M = c` and bracket preservation give `{c, x∘M} = {c, x}`, so `x`'s coefficient in `x∘M` is 1. p14 (2): no SA-1(c) recorder has `x′ − x` constant. p14 (5a): every sharp-meter readable location-preserving recorder is a known displacement, with 144 of 288 having `K_null = id` | **Q4-P20 conclusion**: "`x′ − x` is not constant on the states of the support with `c = 0`. In particular `T` changes `x` on some such state, so `K_null ≠ id` on its silent branch, and its action on `x` there is not a known displacement." **Proof step 3**: "Suppose `x′ − x` is constant on the states of the support with `c = 0`." **Remark**: the sharp-meter sentence becomes "the conclusion fails: on each branch every location-preserving affine-symplectic map acts on `x` by a known displacement, since `c∘M = c` and bracket preservation give `{c, x∘M} = {c, x}`, so `x∘M` has coefficient 1 on `x` and its other terms are known (p14 (5a)). That displacement is zero on the silent branch for some readable recorders (Q4-D8) and nonzero for others, which then have `K_null ≠ id`. So in the affine-symplectic class SA-1(c) is a sufficient route to M16, not a necessary one; a route independent of QM is open (Q4-O9)." In the copy-coupling sentence, "it fails" becomes "the conclusion fails", because the inserted sentences changed the antecedent of "it". **Q4-D8's count line** (the review's suggested addition) adds: "; the other 144 have `K_null ≠ id` only by a nonzero known displacement (Q4-P20; p14 (5a))" |
| **O1** (label; p14 as X) | p14 (2) reproduces the writer-only p13 counts: `m + m′` laws, 11,520 maps of `F_2⁴`, and 17,496 location-preserving maps of `F_3⁴`. p14 (3) is exhaustive over `F_3⁴` but single-probe. p14 (4) is a sample. p13 does not test whether `x′ − x` is constant, so the stronger form has p14 alone | **Q4-P20's label**: "[A: the proof below, independently reviewed in `review/REVIEW-PHASE1-r7.md`; X: p12 (2e)–(2f), p13 (2) and p14 (2), exhaustive over the 384 location-preserving … maps of `F_2⁴` with a known meter slot; X: p13 (2) and p14 (2) for the known functional `m + m′`, for all 11,520 affine-symplectic maps of `F_2⁴`, and for the 17,496 location-preserving affine-symplectic maps of `F_3⁴`; computation-supported by p14 (2) alone for the conclusion's first sentence at those scopes, and by p14 (3) alone for all 51,840 × 81 affine-symplectic maps of `F_3⁴`; a random sample at `q = 5, 7` in p14 (4), not a proof]". **§8 X rule**: "P10, P12 and P14 by reviewers". **Consequences**: SHARED §0 "probes P1–P14"; a new SHARED §7 row for the r7 review (`42edbb6c…`) and p14 (`cd8be1e1…`), listing the sites that cite them |
| **O2** (M15 clause's wider support) | The paper argument under N5, and p14 (5a) | §9's M15 row appends ", and with a sharp meter every location-preserving affine-symplectic recorder acts on `x` by a known displacement on both branches (Q4-P20; p14 (5a))" |
| **O3** ("and (R)'s readout clause") | Q6-P12's second bullet names "(R)'s readout clause" as a hypothesis | "given (L′) and separation in the designed reference graph" becomes "given (L′), separation in the designed reference graph and (R)'s readout clause" at five sites: QX-6 A6.2 "For #1210"; QX-6 §8 item 2; SHARED §3 "Counting"; SHARED §5 QX-6; SHARED §8.4. The affected lines are reflowed |
| **O4** (later owner records) | Read through the GitHub API (read-only). #1169 c.6740778880, user amaybaum, created 2026-11-09T13:05:46Z: the three distinctions. #1210 c.6741117489, user amaybaum, created 2026-11-09T13:22:24Z: "preserve the distinction between necessary physical conditions and assumptions built into the design" | **QX-3 §0's list** appends both records in time order, with author and time. **QX-3's references row** and the **SHARED §7 owner-records row** add "c.6741117489; #1169 c.6740778880" |

## Owner-directed

- **The direction.** In session chat on 2026-11-09, the owner (amaybaum) asked that N5 be kept as an explicit open
  question. The coordinating session relayed it to this revision. The owner also noted that the distinction between a
  predictable, correctable kick and an irreducible disturbance may matter for the investigation.
- **The record.** No GitHub record of this direction was read. Its time of day is not available.
- **Change: new open entry Q4-O9**, after Q4-O8 (SHARED §8.2):
  - **Label.** "(MECH-OPEN; M16, R4.10; owner question, amaybaum, session chat, 2026-11-09)".
  - **The question.** It is quoted verbatim: "Can OI derive a physically meaningful null-result disturbance
    principle independently of QM, without simply introducing SA-1(c) or an equivalent assumption?"
  - **Its context.** "SA-1(c) is a sufficient route to M16 for affine-symplectic location detectors (Q4-P20), not a
    necessary one (Q4-P20; Q4-D8), and has no identified support other than agreement with QM (§9)."
  - **The owner's note.** It is attributed to the same record.
- **Cross-references.**
  - In SHARED §1's M16 row: "Whether OI derives a null-result disturbance principle independently of QM, without
    SA-1(c) or an equivalent assumption, is open (Q4-O9)".
  - In Q4-P20's remark: "(Q4-O9)", under N5.
- **No new content.** No hypothesis or conclusion is introduced. Each statement in the entry restates Q4-P20, Q4-D8
  or §9.
- **Not changed.** §9's null-result row (also M16) is not changed, because the direction named the M16 row.

## Not changed

- Titles ("draft r7") and the §0 "Revisions" pointers (`r6/`, `DISPOSITIONS-r7.md`) are not changed. The r7 round
  updated them as housekeeping, but the instruction for r7a limits changes to the listed items.
- SHARED §7's row for Substratum, Main, SM and AP1 is not changed:
  - its AP1 range :282-350 already covers :297-299 and :320-323;
  - its "cited in" column lists §9 only, although §8 (Q4-D8) already cited AP1 in r7.
- QX-4 and QX-6 do not cite p14 or the r7 review, so their §0 probe ranges are not changed.
- **Everything else** is byte-identical to r7. This includes Q4-P20's "Exhaustively" bullet, every other §8 entry,
  and §§1–2's M16 cells other than the Q4-O9 cross-reference.

## Checks

- **Exact matching.** Each edit was applied by exact-string replacement, and each old string occurred exactly once.
- **Hunk count.** `diff -u r7/ .` over the four specifications gives 21 hunks:
  - QX-3: 2;
  - QX-4: 3;
  - QX-6: 2;
  - SHARED: 14.
- **Stale text.** A grep of the four specifications for "known displacement and `K_null = id`" finds no site. "P1–P13"
  remains in QX-4 §0 only, which does not cite p14. Q4-P20 is not labelled "unreviewed" at any specification site.
- **Register (§A.32, §A.33).** The 67 added lines were scanned:
  - Four-letter capitals occur only in identifiers (`SHARED`, `REVIEW`, `MECH-OPEN`, `DESIGN`, `ANTIBUNCHING`).
  - No history phrase, reader instruction or self-assessment occurs.
- **Necessity words.** Every necessity word on an added line is one of the following:
  - pre-existing text on a reflowed or extended line;
  - the owner's quoted words (O4);
  - "not a necessary one", stating N5's non-necessity.

## r7a file hashes (sha256)

| file | sha256 |
| --- | --- |
| `QX3-ANTIBUNCHING.md` | `baf3de3cc5807a36a3ee265ddf178c3aa23b0028050de5ecaabbb75929e2f024` |
| `QX4-INCOMPATIBILITY-LG.md` | `6b45c062bb5a6b1cbf7dabcaf15a8531d21e089f40b3bee9132a4b40ff7c1248` |
| `QX6-BELL-CHSH.md` | `b77f0984a282603bb6ee2af3941d6bbe3f4fa696b220272329a241affbaa83fc` |
| `SHARED-MECHANISM.md` | `ab69695e33e7e805d4cf49cb3704807ba77637f5feba9c257a0c57ce30dce3e5` |
