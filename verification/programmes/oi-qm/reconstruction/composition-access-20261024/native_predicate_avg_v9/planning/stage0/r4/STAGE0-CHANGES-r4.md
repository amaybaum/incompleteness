# NP-AVG-1 Stage 0: changes r3 → r4

26 October 2026. `STAGE0-PLAN-r4.md` revises `STAGE0-PLAN-r3.md` (SHA-256
`683acdf46c28af943799f6fa053c0952eb557f6b6b8babd3a775f89bb1cbe32c`) against the r3
re-check `review/STAGE0-RECHECK-r3.md`, committed at `6f35cc59`. Owner decision O-a
asks for a self-contained diff, so every change below is traced to one RC item, nit or
owner decision. Departures from the review's text are listed separately in §3.

The r4 design-evidence code is at `stage0/code-r4/` and its evidence at
`stage0/design-r4/`. The r3 code and evidence are unchanged.

## 1. Owner decisions (2026-10-26), in the owner's wording

- **O-a, approved.** The r3→r4 diff, together with its new tests and results, is
  independently reviewed. The freeze happens only after a clean independent acceptance.
  The diff is kept self-contained, with every change traceable to an RC item or nit.
- **O-b, approved in principle.** "Define and preregister the S1b/S1c trigger before
  examining S1 results. The trigger must depend on objective outcomes, not whether the
  result is desirable."
  - The trigger is rule T in §12.
  - It reads two S1a counts, L_A and L_G, and states what happens in every case.
  - It does not read the label, whether survivors exist, or the direction of any
    result.
  - The alternative the review offered was to declare any such search a new
    preregistration. Rule T keeps that in part: S1b is put to the owner as a new
    preregistration whenever the rule calls for it.
- **O-c, approved.** RESIDUE_UNLINKED keeps its G clause, with PO6 complete ("independent
  of G given the frame"). PO3 and PO5–PO8 are written as complete, checkable statements,
  and every rule that depends on one cites it.
- **O-d, approved.** The new planted families and mutants are run now, on toys only. The
  v8 enumeration is not authorized.

## 2. Map of changes

| Item | Plan section | Change |
|---|---|---|
| RC1 | §5 | VOID bullet replaced verbatim. COLLAPSE_ALL now requires "every required control of §6 (C0–C3, C6–C18, the refusal check, the native self-test and S6) green". The MISMATCH bullets cite their PO and corollary, and include C10 (ii) (see §3). |
| RC2 | §2, §4 | Tip, reach, M_T(e), aligned directions and ρ(q) inserted before P_A. "Each of its aligned near tips" in P_A and P_G. P_G-dir added verbatim. B8 defined in §2. PO3, PO5, PO6, PO7 and PO8 restored from r1 as complete statements; PO4 carries the G conditioning; every proposition and corollary cites its POs. |
| RC3 | §2 | Eligibility sentence replaced verbatim. "L3 is L3′ with the far tips removed; cones are unchanged." added. |
| RC4 | §1 | E3 replaced verbatim. |
| RC5 | §3 | (b) replaced verbatim. |
| RC6 | §6 C11 (i), §7 | Decision–table consistency appended verbatim, failure VOID. Implemented in `c11_dir_tables`. |
| RC7 | §6 C11, §7, §9 | Planted set list and non-vacuity pass condition replaced. Φ-adjacent families added for A F and A B; G gets a frame-adjacent analogue. Two mutants fixed before the run. Survivor counts of the class are stated. §7 rows updated. |
| RC8 | §3 | The single item (q9, 9) written out verbatim after the base derivation. |
| RC9 | §5b, §10 | (a) certificate item 6 appended: content-keyed refusal including a freshly constructed v8 copy. (b) item 2's control list replaced. (c) item 3 appended. (d) §10's local-run sentence replaced. |
| RC10 | §6 C8, §9 | The closed list of reported counts: r3's 44 plus the observer classes among collapsed records (A and G), the counts of (b), and the A survivor linkage classes of N1. 52 in all on the toy class. Count preservation covers every item, and the design evidence is extended to all 52. |
| N1 | §3, C8 | Three classes: J-linked; Φ-linked but not J-linked; unlinked. |
| N2 | header, §3, §6, §12 | "review R#" (r1), "re-check R#" (r2), "RC#" (r3). |
| N3 | §5b, §9, manifest | Repository paths `stage0/code-r4/` and `stage0/design-r4/` throughout; the manifest commands use them. No scratch paths remain. |
| N4 | `s0symcheck.py`, §6 C1 | Docstring corrected. C1 states 1,000 interior cells per depth on both slices, 2,000 interior perturbations per depth (beyond depth 8). |
| N5 | §12 | S1a lines are every axis-parallel line meeting Reg (41 per axis, 123 in all), reported only, not a C9 bound. |
| N6 | §6 C7, C8, §5b | The 1-in-1,000 and 1-in-100 sampling rules are Layer-2 configuration constants under certificate item 1. |
| N7 | §9 | The toy region ball(1) does not contain the toy port site (0, 0, −2), so the port-site degeneracy count is vacuous in the design evidence. It is not vacuous on v8. |
| N8 | `s0ref.py` | `pa_aligned_violations` no longer accepts ineligible or Φ-covered exits, so the checker matches P_A. |
| N9 | `s0mutants.py`, §6 | `CASES` maps each mutant to its control, named case and predicate. The §6 mutant table is generated from it. |

Supporting code changes (design evidence, not frozen):
- **`s0geom.py`.** The guard is keyed on content: `Setup.params()` is compared with
  `V8_PARAMS` at every entry point. It adds the mutant fields `ignore_fixed_dir`,
  `decide_blind_dir`, `decide_ignore_fixed_dir`, `blind_only_type` and `blind_only_G`,
  and logs the final tables.
- **`s0ref.py`.** `ref_context` refuses v8 by content. It adds the reference
  per-direction table and the P_A-dir checker.
- **`s0controls.py`.**
  - `_planted_sets`, with the families and the Φ- and frame-adjacent families.
  - The three C11 parts.
  - Refusal: 13 attempts.
  - The 52-count list, with per-record source cells and group-transformed private sets.
- **`s0mutants.py`.** Rewritten for named-case kills, a frozen-clean precondition and
  the two-mutant demo with its context.
- **`s0run.py`.** No local full campaign; `-O` identity checks; repository paths.

## 3. Departures from the review's text

1. **Where Φ-adjacent retention is checked.** RC7 says "The frozen rule must retain the
   Φ-adjacent families (C3)". r4 checks this in a new part, C11 (iii), "planted
   directional retention", and leaves it out of C3.
   - The reason: RC7 also requires the over-elimination mutant to "fail C11 and leave
     every other control green".
   - That mutant eliminates exactly the Φ-adjacent families. If their retention sat in
     C3, it would fail C3 as well.
   - C11 (iii) is required, and its failure is VOID (§5, §5b item 2), so the requirement
     binds just as hard.
2. **G's adjacent family.** Under G no quantity of the fixed set is a cover outside the
   frame, and frame tips are ineligible. A literal "Φ-adjacent" G family therefore tests
   nothing. r4 uses a frame-adjacent family: its −x near tip lies in the frame, so the
   tip is ineligible and the family must be retained.
3. **The A B adjacent family.** It is placed at c = (1, d, 0), so that its −y near tip is
   the Φ cell (1, 0, 0) on slice 7. The natural choice c = (0, d − 1, 0) at d = 1 gives
   q = p, which is fixed, so the planted set would be degenerate. An assertion that each
   planted q is even and not fixed was added.
4. **MISMATCH and C10.** RC1 lists C10 (ii) among the MISMATCH conditions. §5's
   MISMATCH bullets therefore gain a C10 (ii) bullet citing its PO, which r3 lacked.
   r3's bullet "a fixed quantity is eliminated" is kept, citing PO5. It states that
   C10 (i) is a code invariant that cannot fail by construction (§7), and so is not
   among RC1's controls. This keeps RC1's precedence unambiguous without deleting r3
   text that the review did not ask to delete.
5. **PO6.** RC2 asks for r1's PO6. r4 states it for A and for G, keeping the G clause
   "independent of G given the frame" (O-c). RESIDUE_UNLINKED cites both.
6. **RC10's list.** The review lists r3's 44 counts plus the observer classes and the
   counts of (b). r4 also adds the A survivor linkage classes of N1, so that every count
   §3 defines is on the list. That gives 52 on the toy class. The design evidence covers
   all 52, so the alternative "state that the r3 evidence covers 44" is not needed.
7. **RC tags.** Where the review's text was inserted verbatim, r4 appends an "(RC#)" tag
   for traceability. This follows the "(review R#)" convention of r2–r3 and changes no
   wording.
8. **The native evaluator.** `s0native.py` has no configuration entry point that could
   reach v8; it evaluates only the toy, planted and S6 instances passed to it. The
   content-keyed refusal of RC9 (a) is therefore enforced at the production
   (`s0geom`) and reference (`s0ref`) entry points. The refusal check exercises both.
9. **Rule T** (O-b) is new text, not review text. Its inputs are L_A and L_G, defined
   over the S1a global bound. It states the action for L_A = L_G = 0, for either > 0,
   and for a cost overrun, and it is independent of the k ≤ 2 label.

## 4. Control results (r4 design evidence; toys, planted sets and small windows only)

Everything ran with `python3 -I -B` on Python 3.13.16. Every step exits 0. Nothing ran
on v8's configuration class.

| Step | Time | `-O` identical | stdout SHA-256 |
|---|---|---|---|
| controls_frozen_full | 133 s | yes | `a556e3247f559fa7b4665ae92716127ed10ebc82c833fc33859faec047b8e589` |
| s6_po8_proofcheck | 19 s | yes | `0f0bca68f34aa498e5026952cda77637ca7cfe8cb69c3eec0e96768aaa939c5d` |
| symcheck_v8_combinatorics | 19 s | yes | `76779524835103d032eda1d2170a6c1a4e57d5fb9cdb342835f5c03056c2d8b5` |
| mutants_quick | 845 s | n/a | `8971d628bd3d026e9f5860054a1b27fd87e77cb64776b8e01c57e18cd31b66ca` |
| toy_rerun_L4 | 10 s | yes | `cb843f0fdf42944041f12f19e904b9893b436db0f1e87cb0db9e8f4e739e825f` |
| toy_planted | 0 s | yes | `8a4ebd8cd4c04b681a8515f79f197a093cabf90304570b785531cf5d4e7106d8` |
| toy_radius_mutants | 0 s | yes | `5d826a8415a4a5ca7c51dd19c5abd8d237502225b9cc01a0d65b112a040b9ff7` |
| toy_exact_small | 141 s | yes | `a0455a8889639109e5327feb40756c2acedf107bed78124ee9a31770d514cb6c` |

The full values are in `stage0/design-r4/RUN-MANIFEST.json`.

**Controls.** No control fails.
- **C1:** 301,640 perturbations, none outside the cone.
- **C2:** 541 tips, 39 off-axis.
- **C7:** 0 differences.
- **C8:** 52 counts, 0 mismatches, 0 equivariance violations.
- **C10 (ii):** 2 port samples, 0 failures.
- **C11 (i):** 16,835 tables, 0 mismatches, 0 decision–table inconsistencies.
- **C11 (ii):** 24 retained planted sets, 0 violations.
- **C11 (iii):** 96 planted sets, 0 failures.
- **C15, C17 and C18:** 0 violations.
- **Refusal:** 13 of 13 attempts refused: v8 ×5, a freshly constructed v8 setup ×5, the
  flipped flag, and `ref_context` under A and under G.
- **S6:** passes, labelled "proof-check of PO8; not a result".

**Quick mutant campaign.** The frozen suite is clean (exit 0, nothing failed). All 16
mutants are killed at their named cases:

| Mutant | Named case |
|---|---|
| `blind_dir_minus_y` | C11 (i): table mismatch |
| `ignore_fixed_minus_y` | C11 (iii): Φ-adjacent family eliminated |
| `decide_blind_minus_y` | C11 (i): decision inconsistent with table |
| `decide_ignore_fixed_minus_y` | C11 (i): decision inconsistent with table |
| `blind_B_minus_y` | C11 (ii): P_A-dir violation on a B planted set |
| `blind_G_minus_y` | C11 (ii): P_G-dir violation on a G planted set |
| `far_cone_deleted` | C1: dependence outside the cone |
| `radius_minus2` | C1: dependence outside the cone |
| `radius_plus2` | C1: claimed radius not attained |
| `swapped` | C1: cone mismatch |
| `offaxis_all` | C2: an emitted tip is not bijective |
| `offaxis_B` | C2: an emitted B-type tip is not bijective |
| `near_only` | C3: block minus centre retained |
| `keep_odd` | C0: context differs from the reference |
| `unapplied_elimination` | C17: retained quantity with a free tip |
| `wrong_far` | C15: exactness violation |

- **Non-vacuity demo.** `blind_dir_minus_y` fails the three parts of C11 and nothing
  else. `ignore_fixed_minus_y` fails C11 (i) and (iii) and nothing else. The reported
  counts of both are identical to the frozen rule's.
- **Equivalent mutants.** Parity-dropped fails nothing. Symmetric-blind fails only C1.

**Owner's r4 requirements against the evidence.**
- **The planted families are detected.**
  - B type: `blind_B_minus_y`, caught by C11 (ii).
  - G: `blind_G_minus_y`, caught by C11 (ii).
  - Φ-adjacent: `ignore_fixed_minus_y`, caught by C11 (iii).
- **Decision-level mutants are caught** at C11 (i)'s decision–table check:
  `decide_blind_minus_y` and `decide_ignore_fixed_minus_y`. The latter is the analogue of
  the re-check's `rv_decide_ignore_fixed_y`, which escaped r3.
- **The v8 refusal is keyed on content.** A fresh object, `ref_context` and a flipped
  flag are all refused.
- **Every proof-dependent rule references a complete statement:** §4's PO table and the
  PO citations in §5.
- **Limits of the demonstrations disclosed (§9).**
  - The toy class has 0 survivors under A and G.
  - 30 of the 52 counts are identically zero on it.
  - The port-site count is vacuous there (N7).
  - r3's demonstration was over-retention only. Its part (i) was near-tautological and
    its part (ii) rested on one planted set. 24 of its 44 counts were zero, and it missed
    `rv_decide_ignore_fixed_y`.

**Not run.** The full mutant campaign is not run locally; under §A.40 it runs in CI, and
any dispatch needs owner approval (§A.43). The v8 enumeration is not authorized.
