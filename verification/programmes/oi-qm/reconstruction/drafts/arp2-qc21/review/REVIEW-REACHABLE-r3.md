# Changed-lines check: ARP-2 r3 drafts, against REVIEW-REACHABLE-r2.md

**Objects (sha256).**
- `qc21/REACHABLE.md` r3: `718e7dbcf0c8f632709c94cb63865cf84c55d8f3d60d3dfac583a5087ef25b47`
- `qc21/preregistration.draft.md` r3: `7f0d5983f146d3e6f901804b478f013827ef71a9a422f597579ca47686a9decf`
- `qc21/PLAN.md` r3: `74afe74e24be93d6e57b90867fadd76a4333aa4ae64d626f408f95c3af792a5b`
- r2 baselines for the diff: `REACHABLE-r2.md` `5429c7e4…`, `preregistration-r2.draft.md` `3864215c…`, `PLAN-r2.md`
  `c18eae0a…`.
- Measured against `review/REVIEW-REACHABLE-r2.md` (`899721d8…`).

**Standing.** Independent model check, read-only, 2026-11-08. Not human verification. **Scope:** the r2 → r3 diff only,
plus one defect found outside it (R3-B2), reported because it bears on the decision rule.

**Reviewer control** (`review/controls_r3.py`, sha256 `317a4abe…`, exact, `python3 -I -B`). It computes only static
algebra: the PC-NONSTAB planted laws and their images under rule `0`'s free swap. Rule `0` is affine and is not a test
rule. **No reachable set was computed under any rule.**

## Verdicts

- **REACHABLE r3: ACCEPT.** RN1–RN5 are closed, and the changed lines open no new hole.
- **Preregistration r3: REVISE.** PB1–PB4 and PN1–PN4 are closed as findings. Two blocking items remain, and each needs
  a one-line fix:
  - **R3-B1** completes PB4's propagation into the frozen common clause.
  - **R3-B2** is new and predates r3: a frame/determinant convention can turn a CANDIDATE into NONSTABILIZER. Both
    of my earlier reviews missed it.

## 1. REACHABLE r3 (RN1–RN5)

| finding | closed? | check |
| --- | --- | --- |
| RN1 `α = 0` | **yes** | R:211-213. The sum gives `α_c = 0` for `c ≠ b`, since `|α_b+1|+|α_b−1| ≥ 2`. Each inequality taken alone then gives `|α_b ± 1| ≤ 1`, so `α_b = 0`. The proof is now complete. |
| RN2 `Q* = 0` scope; label | **yes** | R:176, R:181-183. `Q* = 0` is stated only without centre terms. The extension of the isotropy half to general affine symplectic steps is labelled paper here. |
| RN3 `Λ_{y,b}` needs NNB | **yes** | R:116-117 (`N_sup`), R:368-369 (NE-1). |
| RN4 P★ not a bound on U′ | **yes** | R:282. |
| RN5 status line | **yes** | R:3-7 cites both reviews, both verdicts and their model-review standing. |
| §4 bounded instance | **yes** | R:430-435 states the decidable instance and leaves the general O-1 question open under every outcome. |

No new hole was found in these lines.

## 2. Preregistration r3 (PB1–PB4, PN1–PN4)

**PB1 → PC-NONSTAB.** Closed.
- The planted laws really do fail NE-1, so they cannot count as native:

  | law | image `(r_x, r_y, r_z)` | ℓ1 | \|r\|² | NE-1 | why it fails NE-1 |
  | --- | --- | --- | --- | --- | --- |
  | (a) `z_1, x_1 ~ Bern(1/5)` independent, cell 1 (`z_2, x_2`) uniform | `(3/5, 0, 3/5)` | 6/5 | 18/25 | **fails** | not uniform on its support |
  | (b) uniform on `{x_1 = 0, f_y = 0}` | `(1, 1, 0)` | 2 | 2 | **fails** | determined set ⊇ `{f_x, f_y}`, `ω(f_x, f_y) = 1`, so not isotropic |

- Neither law can enter even through the non-native NR-9 tier. Both images have `ℓ1 > 1`, and `conv S_nat` has images in
  `O` (Theorem C(ii) with Prop E). So no LP can place either law in `conv S_nat`.
- Under rule `0`'s free swap, (a) keeps its image and (b) maps to `(0, 1, 1)`. Both statuses persist, so the expected
  categories hold:
  - (a) gives NONSTAB, because the `S_0` laws stay in `V₀` under rule `0` and the mediator is decoupled;
  - (b) gives INVALID, with the invalid-rule `nonstab_valid` positive;
  - C-EMB (a) now covers both planted laws (P:286).

  These expectations are paper here; the control was not run on reachable sets.
- **N.** State that PC-NONSTAB's runs are separate from CC-NAT's `L_scope(0)`, so that planted laws never enter the
  countercontrol's set. The text implies this but does not say it.

**PB2 → CC-MIX.** Closed (P:284).
- The non-vacuity clause is now quantified over the union of the four affine rules, and the per-rule clauses stay per
  rule.
- Non-vacuity is attainable, by paper argument on an affine rule. Take XOR with `k = 1` and `reg = none`, carrier
  `(u_0, v_0) = (?, 0)` and `u_1 = 0` known, and the CC-MIX mediator with `P(u_2 = 1) = 2/3`. Then `f_z' = u_0' = u_2`,
  so `r_z = −1/3`.

**PB3 → CANDIDATE text and ADA question 4.** Closed (P:322-323, P:415).

**PB4 → L-NNB.** Closed in the ledger (P:366) and in the kept/removed table (P:252). The propagation is incomplete:
see R3-B1.

**PN1 → phrase screen.** Closed. A scripted S4 screen of the frozen texts (common clause through *What no outcome
shows*, and ADA Part 2) finds no hit.

**PN2 → affine basis, C-AFFB, timeout.** Closed. The equivalence argument (P:229-235) is correct:
- `q_π` is linear in `μ`, so it is constant on `L_scope(g)` iff it is constant on an affine basis of its affine hull.
- With `q` constant, both sides of the identity are affine in `μ`, so they agree on the hull iff they agree on the
  basis.
- `Λ_0, Λ_{x,0}, Λ_{y,0}, Λ_{z,0}` are affinely independent, because their images `0, e_x, e_y, e_z` are, so the
  basis can start from them.
- The positivity check on all of `L_scope` is redundant but harmless.
- The design bound (P:520-529) is outcome-independent. Non-blocking points:
  - **N.** Basis selection over up to about 5 × 10⁵ laws is missing from the estimate. Stop early once 16
    affinely independent laws are found, since the hull is then the full simplex plane, and run the elimination on the
    integer tuples.
  - **N.** C-AFFB exercises the equivalence only on the affine rules, whose sets are small and low-dimensional. A
    basis-selection bug that shows only on large or full-rank sets would pass it. Also run C-AFFB on a fixture set,
    for example PC-PLANT's and PC-NONSTAB's laws together with their rule-`0` closure, chosen so that the affine hull
    has full rank 16.

**PN3, PN4.** Closed (P:387-388, P:365).

**Bounded instance.** Stated at P:193-199 and PL:145-151, consistent with R:430-435 and with the categories at P:262-270.

## 3. Blocking

**R3-B1. The frozen common clause omits NNB (P:317-318).**
- The clause is printed with every outcome. It reads "conditional on P2, N2, H-PREP, the supplied registration and the
  refilled mediator". NNB is now a used supplied premise (P:252, P:366; R:430): it supplies `Λ_{y,b}` in `S_0`.
- The outcome text would therefore state fewer conditions than the round uses (conditional → less conditional; §A.25
  propagation of PB4).
- *Fix:* "conditional on P2, N2, H-PREP, NNB (for the supplied `Λ_{y,b}`), the supplied registration and the refilled
  mediator."

**R3-B2. A frame convention can hide a CANDIDATE (P:207-236, P:262-266; this predates r3 and I missed it in r1 and r2).**
- The model's R reads fixed slots: `f_z = u_0`, `f_x = v_0`.
- QA's U′, whose encoding the round imports, is defined in the common encoded frame. In AP1 §4.2 that frame is
  `(z, x) = (u, v)` at even `t` and `(v, u)` at odd `t`; QA:445-448 uses "the common encoded frame".
- A free tick is the identity in that frame. In fixed slots it is the swap `x ↔ z`, with `f_y` unchanged and
  determinant −1. RC-r3 shows this: law (b) maps `(1,1,0) ↦ (0,1,1)`.
- So for a round with `k` ticks, `det β_encoded = (−1)^k det β_fixed`.
- The counts `outside_ball`, `nonstab_valid` and `offaxis_unit` are invariant under the swap, and so is octahedrality.
  The CANDIDATE rule's `det β = 1`, however, is not.
- Suppose the encoded action of a round with odd `k` is a non-octahedral rotation. The round then reports an improper
  map, and the rule falls to NONSTAB: its off-axis unit columns make `nonstab_valid > 0`. A CANDIDATE is thus
  mislabelled NONSTABILIZER.
- *Fix (either):*
  - freeze the encoded frame: evaluate R on `(v, u)` when the law's total tick count is odd, carry the parity with
    each law in `L_scope`, and keep `det β = 1`;
  - or keep fixed slots, define unitary as `(−1)^k det β = 1` for the round's `k`, and report the determinant in
    both conventions.

  Either way, add a self-test fixture that checks the swap. On rule `0`, `k = 1` must induce the `x ↔ z` transposition,
  with fixed determinant −1 and encoded determinant +1.

## 4. Summary

| item | status |
| --- | --- |
| RN1–RN5 | closed |
| PB1 (PC-NONSTAB (a), (b)) | closed; both planted laws fail NE-1 and lie outside `conv S_nat` |
| PB2 (CC-MIX union) | closed; non-vacuity attainable (XOR, `k = 1`) |
| PB3, PB4 (ledger), PN1–PN4 | closed |
| affine-basis argument | correct; two non-blocking robustness notes |
| bounded decidable instance | stated consistently in all three files |
| new blocking | R3-B1 (NNB missing from the common clause); R3-B2 (frame/determinant convention) |
| REACHABLE r3 | **ACCEPT** |
| preregistration r3 | **REVISE** (R3-B1, R3-B2; each a one-line fix plus one fixture) |
