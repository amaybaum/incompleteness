# NP-AVG-1 Stage 0: changes r4 → r5

26 October 2026. `STAGE0-PLAN-r5.md` revises `STAGE0-PLAN-r4.md` (SHA-256
`1a9a28128a6b3a9059a5f3a36f94645e1c7d8ba00c2fdc8a176e26b938d40a12`) against the r4 re-check,
`review/STAGE0-RECHECK-r4.md`, committed at `926cb0d1`, with its probes in `review/toy-r4/`.
Under O-a the diff is self-contained: every change below is traced to an R4 item or nit.

The r5 design-evidence code is at `stage0/code-r5/` and its evidence at `stage0/design-r5/`.
The r4 files are unchanged.

## 1. Owner decisions

- **O-a (unchanged).** R4-1 to R4-7 are applied, followed by a diff-only re-check. Layer 1
  is then frozen.
- **Rule T's consequence: PENDING OWNER.**
  - The reviewer asks the owner to confirm that the L_A = L_G = 0 branch reports the
    geometric statement only.
  - A law statement for k > 2 would need a new proof obligation generalising PO8.
  - r5 adopts the conservative default: the geometric fact only. It says so in the header
    and in §12 ("Pending owner").

## 2. Map of changes

| Item | Plan section, code | Change |
|---|---|---|
| R4-1 | §6 C11 (ii) and non-vacuity, §7; `s0controls._planted_sets`, `s0geom.Rule`, `s0mutants.CASES` | The review's sentence is inserted verbatim. The G adjacent family is planted without its in-frame near-tip quantity ((n+2, 0, 0), 0), with assertions that the removed cell is that family's −x tip, is ineligible, and lies in a fixed or port cone. The reviewer's mutant becomes `decide_frame_ignore_minus_x` (field `decide_inelig_free_dir`, the reviewer's code), named at C11 (iii): "frame-adjacent G family eliminated". |
| R4-2 | §6 Refusal, §5b item 6, §7; `s0geom.Setup.key/guard`, `s0ref.ref_context`, `s0controls.refusal` | The refusal is keyed on (dim, n, port), using the review's sentence. The ports are compared as tuples. The refusal check adds the sources changed, the sources empty, ρ = 5, t_last = 24 and a list port (4 entry points each), for 36 attempts. |
| R4-3 | §4 P_G, C_A, C_G, PO6, PO7 | PO6 (G) uses the review's sentence. P_G and PO7 get the t ≥ 0 / slice −1 seed condition, with the review's PO7 sentence. C_A, C_G and PO6 (A, G) cite PO4. |
| R4-4 | §9 | The review's replacement sentence; the 173 → 24 change is reproduced in r5's own run. |
| R4-5 | §12 rule T, §5b item 5, §7 | Uses the review's consequence and invalid-S1a text, plus a §7 row (`result.json` records L_A, L_G and the outcome, §A.44). Layer-2 item 5 writes them. |
| R4-6 | §6 C8, §7, §9; `s0controls._reported_counts`, `_g_linked_per_record` | Adds G-linked and G-unlinked survivor counts. They are computed per record in the orbit-reduced path, never transferred, which brings the total to 54. The list is stated as closed against §3. |
| R4-7 | `s0controls.c11_props` (`pa_dir_violation_set_kinds`), `s0mutants.CASES` | `blind_B_minus_y` now requires a violation on an `A_B` or `adjPhi_A_B` set, and `blind_G_minus_y` one on a `G_F` or `adjFrame_G_F` set. |
| Nit: labels | header, §12 | "review R5", "review R8", "review R1–R9". |
| Nit: guards | §4 asymmetry, §7 | C11 (i) and (iii) are added to the over-elimination guards. |
| Nit: symcheck | `s0symcheck.py` | The docstring now reads "design evidence for C0". |
| Nit: §7 row | §7 | The complete-statement row is marked as a document property, checked by independent review. |

## 3. Departures from the review's text

1. **PO7's middle sentence.** R4-3 corrects PO7's last sentence. The middle sentence ("A
   quantity with |c| + t ≤ 8 has its whole cone inside the frame, and has no seed tip")
   has the same defect at slice −1: the even-class quantity (c, −1) with |c| = 9 has
   |c| + t = 8 and is a seed, since its tip is itself and lies outside B8. r5
   restricts it to t ≥ 0 as well. For t ≥ 0 it holds: the cone reaches |c| + t ≤ 8 on
   slice 0 and |c| + t − 1 ≤ 7 on slice −1.
2. **The PO6 (G) join.** The review's replacement ends "and with PO4 (G)", and r4's
   continuation "Law_G of the record equals Law_P …" follows after a comma. PO6 (A) cites
   PO4 inline, as "with PO4 (A), the record's law … is that of the collapsed record".
3. **Refusal hardening beyond R4-2.** Both guards compare against a literal, so rebinding
   `V8_KEY` (formerly `V8_PARAMS`) or `V8_REF` in the process no longer bypasses them. The
   reviewer listed that rebinding as tampering, noted only. The refusal check includes
   both rebindings. This changes no stated behaviour.
4. **The reviewer's probes as retained steps.** `review/toy-r4/guard_probe.py` is copied
   byte-identically to `stage0/design-r5/guard_probe.py`, and `frame_adjacent.py` with one
   renamed mutant and a provenance header. Both run against `stage0/code-r5/` as manifest
   steps.
5. **§A.44.** The review cites §A.44 in R4-5. It exists in `AGENTS.md` on `main`
   ("Structured evidence for computational verdicts"), so the citation is kept. This is
   not a departure; it is noted because the session's copy of `AGENTS.md` predates it.

6. **Item tags.** Where review text was inserted verbatim, an "(R4-#)" tag is appended
   before the closing full stop, as in r4. In the PO7 table cell the sentence has its `|`
   escaped and no final full stop. No wording changes.

## 4. Control results (r5 design evidence; toys, planted sets and small windows only)

`python3 -I -B`, Python 3.13.16. Every step exits 0. Nothing ran on v8's configuration
class: v8 setups were constructed only, to be refused.
`stage0/design-r5/RUN-MANIFEST.json` has SHA-256
`3f821cc564274652cbc41202845b79cabc1c4fd0ce3acbebbb1fa9247a76308f`.

| Step | Time | `-O` identical | stdout SHA-256 |
|---|---|---|---|
| controls_frozen_full | 134 s | yes | `124ca8960f0190161dea0ecbcc7588a8de95c76645178681e3e23c5cd80c18ee` |
| s6_po8_proofcheck | 18 s | yes | `0f0bca68f34aa498e5026952cda77637ca7cfe8cb69c3eec0e96768aaa939c5d` (= r4) |
| symcheck_v8_combinatorics | 20 s | yes | `76779524835103d032eda1d2170a6c1a4e57d5fb9cdb342835f5c03056c2d8b5` (= r4) |
| mutants_quick | 880 s | n/a | `85ddb4f14cf626e7077ff4ba6609f473634a41115f47655d9d058615903f15db` |
| toy_rerun_L4 | 9 s | yes | `cb843f0fdf42944041f12f19e904b9893b436db0f1e87cb0db9e8f4e739e825f` (= r4) |
| toy_planted | 0 s | yes | `8a4ebd8cd4c04b681a8515f79f197a093cabf90304570b785531cf5d4e7106d8` (= r4) |
| toy_radius_mutants | 0 s | yes | `5d826a8415a4a5ca7c51dd19c5abd8d237502225b9cc01a0d65b112a040b9ff7` (= r4) |
| toy_exact_small | 142 s | yes | `a0455a8889639109e5327feb40756c2acedf107bed78124ee9a31770d514cb6c` (= r4) |
| review_guard_probe | 0 s | yes | `31ffc4484153d3e7d2fdeb841e4ca2fa298d5704b63119122944b42bfff4fc3d` |
| review_frame_adjacent | 0 s | yes | `6e3ac33e3556e8470e7065088407491fc9ed63e829ad0d890495bd394a042bdf` |

**Controls.** No control fails.
- **C1:** 301,640 perturbations, none outside the cone.
- **C2:** 541 tips, 39 off-axis.
- **C3:** block 8 / 0.
- **C7:** 0 differences over 1,400 records.
- **C8:** 54 counts, 0 mismatches, 0 equivariance violations.
- **C10 (ii):** 2 port samples in-frame.
- **C11 (i):** 16,831 tables, 0 mismatches, 0 decision–table inconsistencies.
- **C11 (ii):** 24 retained planted sets, 0 violations.
- **C11 (iii):** 96 sets, 0 failures, including the 4 G frame-adjacent families without
  their in-frame tip quantity, all retained.
- **C15, C17, C18:** 0 violations.
- **Refusal:** 36 of 36 refused.
- **S6:** passes, "proof-check of PO8; not a result".

**The owner's checks against R4-1, R4-2 and R4-7.**
- **R4-1.** The reviewer's G mutant, `decide_frame_ignore_minus_x`, is killed at
  C11 (iii) "frame-adjacent G family eliminated". It also fails C7, C8, C11 (i) and C18,
  and changes the G observer-class counts from 173 to 24. The reviewer's probe, re-run on
  r5, gives: frozen 7/7 and 12/12 retained; the mutant 0/7 and 0/12; r4's family intact
  under the mutant (8/8, 13/13).
- **R4-2.** The reviewer's guard probe, re-run on r5, refuses all 15 attempts:
  - the five r4 bypasses: sources changed, sources empty, ρ = 5, t_last = 24, and
    `record_at` on ρ = 5;
  - both rebindings;
  - both list-port attempts, which were a TypeError in r4.

  The suite's own refusal check refuses 36 of 36.
- **R4-7.** `blind_B_minus_y` is killed with violations on `A_B` sets, and
  `blind_G_minus_y` on `G_F` sets.

**Quick mutant campaign.**
- The frozen suite is clean.
- All 17 mutants are killed at their named cases (plan §6 table).
- **Non-vacuity demo:** blind −y fails C11 (i)–(iii) only; ignore-fixed −y fails C11 (i)
  and (iii) only. The counts of both equal the frozen rule's.
- **Equivalent mutants:** parity-dropped fails nothing; symmetric-blind fails C1 only.
- **Demonstration context:** 0 toy survivors (A and G); 32 of the 54 counts identically
  zero (the two new G-linkage counts are survivor-conditioned).

**Observed failures that changed from r4.** The off-axis (all), wrong-far,
far-cone-deleted and radius −2 mutants no longer fail C11 (ii).
- **Cause, checked directly.** Under off-axis (all), r4 retained 9 planted sets and r5
  retains 6. Under wrong-far, r4 retained 4 and r5 retains none. The difference is
  exactly r4's `adjFrame_G_F` families. They kept their in-frame tip quantity, survived
  these mutants, and gave the aggregate-P_G hits. In r5 those families are eliminated,
  which C11 (iii) reports.
- **Kills unaffected.** None of these mutants is named at C11 (ii), so every kill stands.

**Not run.** The full mutant campaign is not run locally; under §A.40 it runs in CI, and
any dispatch needs owner approval (§A.43). The v8 enumeration is not authorized.
