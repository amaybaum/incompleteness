# RR-1's two register forms: a brief, r1

**Status: paper-only brief; unreviewed.** It answers U3 owner question 5 as decided: "a short brief on
RR-1's two register forms comes before any reading is chosen" (#1169 c.6892563291, `amaybaum`,
2026-11-15T09:49:19Z). It chooses no reading, adopts no premise, changes no status and runs no
computation. Its recommendation is a recommendation only. Every [A-inf] is an author-side hand check.

**Inputs.** Branch `research/ro1-sector-c-1169-20261114` at
`11734ce3b2c88acf2b4b6949fdb5453d19012685`, in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, **off `main`**:
`S3-U3-r2.md` (blob `34ffe552`, owner-accepted, "L-2 and L-3 stay proposed lemmas that need a
dedicated review"; cited U3), `S3-U2-r4.md` (blob `1bcb9e17`; cited U2), `S3-PLAN-r9.md` (cited PLAN),
`S3-U1-r5.md` (cited U1). SEL-EXCL-1 at `0ecfddeb` and TSI on `main` as cited in U3.

## 1. The two forms

PLAN's RR-1 is "Same-seed reuse with retained records" (PLAN:355). U3 §2.2 writes each output of an
unchanged-source second use in one of two ways (SEL-EXCL-1 ll. 169–179):
- **Fresh-output form (F).** The second output goes into a fresh blank. Each wing's complete local
  history is the pair `(b₁, b₂)`, both held at `t_c`.
- **Same-register form (R).** The second output is XORed into the first use's register. The wing's
  complete local history is the one register `b₁ ⊕ b₂`, held at `t_c`; `b₁` is not held separately.

The record of (R) is a function of the record of (F).

## 2. What each requires of the substratum, under U1

| Requirement | (F) | (R) |
|---|---|---|
| Source | one source used twice, case (U) of U3 §2.2 | the same |
| Setting change between uses | `φ`-effected (C-SET); first missing step for both (U2:690) | the same; for `T`, Bob's change alone suffices (U2 AW-U2-3) |
| Budget | at least 2 below `ord(φ)` (AD-1(f)) | the same |
| Blanks | a second blank register reached by the second use | the initial blank `B₀ = 0` only (U2:459–470) |
| Retention | `b₁` retained to `t_c` (C-RET; U3 RQ-TC). Unsourced in general (O-RET, #1032) | none: the register itself is held at `t_c` (U2:470; U3 §3 RQ-TC) |
| Access | `b₁` and `b₂` readable by the wing at `t_c` | the register readable at `t_c` |
| Held capacity at `t_c` (U3 §6, reading (a), the owner's answer to U3 Q1) | two output bits per wing for two uses, plus settings | one output bit per wing, plus settings |

[A-inf] Under the owner's answer to U3 Q1 (one fixed finite observer family per model), both forms fit
any family that holds a few bits per wing; the capacity bound does not separate them at two uses.

## 3. Which results hold under each

| Result | (F) | (R) |
|---|---|---|
| SEL-EXCL-1 §7 witness for `T` [OFF] | `b₁ ⊕ b₂′ = x₂` (l. 179) | `b₂ = x₂` (ll. 169–177) |
| TSI's signal (10) [NP] | yes: its outcome slots are separate | not stated by TSI; [A-inf] from TSI (7) the register `b₁ ⊕ b₂ = x₁y₁ ⊕ x₂y₂` also signals |
| U2 F-3: not available in M-PR5 (budget 1) | yes | yes |
| U2 AW-U2-3: no retention, no clock | — | yes |
| L-2 (proposed; U3 §5.1) | yes, (k5) fresh-output case | yes, (k5) same-register case |
| L-3 (proposed; U3 §5.2) | yes, (k5′) | yes, with `Θ` identifying the register with `a₁ ⊕ a₂` |
| RQ-UPD-1, RQ-UPD-2 (U3 §3) | yes | yes, at the same conditions |
| C-RET against R2 differs (U3 §7) | yes: a parked `b₁` is executed under C-RET, not under R2 | no difference |
| RR-1 status (U3 §10.2) | undetermined | undetermined |

No result on record holds under one form and fails under the other. The forms differ in what they
require (retention, blanks, capacity) and in where C-RET and R2 diverge.

## 4. Performed experiments that bear on the choice (for the first-hand read)

[A-inf] The two forms are record formats of one program family, not rival physical hypotheses. For
any quantum two-use experiment, the (R) record is a function of the (F) record, so no performed
experiment can confirm one form against the other as a claim about nature. What the read can settle:
- **Record format.** For each performed experiment that uses one entangled source twice per wing
  with a setting change between uses, whether its raw records hold each outcome separately (an
  (F)-form experiment) or only an accumulated or parity record (an (R)-form experiment).
- **Strength of the test.** Raw (F)-form records also give the (R)-form record `b₁ ⊕ b₂`, so an
  (F)-form experiment checks the agreement half for both forms. An (R)-form experiment checks only the
  law of the register.
- **Instrument type.** Whether the first measurement is projective (Lüders, as in TSI (9), the case
  L-3 states) or unsharp. L-2's agreement use needs only setting-independence of the raw complete
  local-history records; L-3's needs repeatability at repeated settings.
- **Completeness.** Whether failures and all attempts are kept (K-6), and whether each wing's full
  local history, not only coincidence counts, is reported (§A.24 raw-direct level).

No specific experiment is identified here; identifying them is the read authorized under U3 Q4.

## 5. Consequences of each choice

- **(F) only.** RR-1 matches the record format of experiments that hold each outcome. It carries the
  retention requirement and the one C-RET/R2 difference. The (R)-form witness stays in `Γ_exe`
  wherever `φ` executes it (K-1; access closure, answer 4), but no case would assess it, although it
  is the route with fewer requirements.
- **(R) only.** RR-1 needs no retention and becomes the minimal exposure route of U2 AW-U2-3. It drops
  the retention question and the C-RET/R2 difference from RR-1. PLAN's "with retained records" would
  then mean persistence of the first record in the register up to the second use, not retention to
  `t_c`.
- **Both.** RR-1 is assessed as two sub-cases, RR-1(F) and RR-1(R), each with its own requirements
  row. This is the scope L-2 and L-3 are already stated for, so no proof changes. PLAN's wording is
  read as "the first record persists in a held region at least until the second use". No status
  changes under any choice.

## 6. Recommendation (for owner decision; not a choice made here)

**Read RR-1 as covering both forms, reported as RR-1(F) and RR-1(R).** Reasons:
1. Access closure and K-1: `Γ_exe` contains whichever form `φ` executes. Assessing one form leaves the
   other, which needs fewer resources, assessed nowhere.
2. The two forms test different parts of the frame: (F) needs retention to `t_c` and is where C-RET
   and R2 differ; (R) needs neither. Keeping both keeps both questions visible.
3. Nothing is lost. L-2, L-3, RQ-UPD and U2's results are already stated for both forms, and no
   status moves.
4. It matches the coming literature read: (F)-form raw records check both forms; (R)-form records
   check (R) only.

The cost is one more row in the requirements and status tables, and a stated reading of PLAN's
"retained records".
