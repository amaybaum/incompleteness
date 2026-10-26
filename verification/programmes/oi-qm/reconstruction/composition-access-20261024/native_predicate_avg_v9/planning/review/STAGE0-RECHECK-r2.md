# Re-check: NP-AVG-1 Stage 0 r2, with its code and evidence

**Reviewed.**
- `draft/STAGE0-PLAN-r2.md` (660 lines), `STAGE0-CHANGES-r2.md` and `STAGE0-NOTES-r2.md`;
- `stage0-code/`: `s0geom`, `s0ref`, `s0native`, `s0controls`, `s0mutants`, `s0s6` and `s0run`,
  read in full;
- `stage0-design-r2/` and its `RUN-MANIFEST`.

**Read-only.** Nothing ran on v8's class. My re-runs are in `review/rerun-s0r2/`, run with
`python3 -I -B` on Python 3.13.16.

## Verdict: ACCEPT WITH CHANGES (not a clean ACCEPT FOR FREEZE)

**What is ready.**
- The rule, the masking engine, the three safeguards and the toy evidence are sound.
- They are reproducible byte for byte.
- R1–R9 are substantively applied.
- Every non-equivalent mutant is caught by a named control.

**What blocks a clean freeze, as written:**
- the plan freezes "every file in `stage0-code/`", but the enumeration program the decision rule
  depends on is not in it (finding 1);
- several stated control ranges are not what the code does (finding 3);
- seven of the eight recorded runs are retained only as hashes (finding 6).

All of these are bounded edits. None changes the rule or the question.

## Reproduction

| step | my result | against the record |
| --- | --- | --- |
| `s0controls.py` (full), normal and `-O` | exit 0, nothing failed | **byte-identical** to `runs/controls_frozen_full.out` (SHA-256 `cc01c766…`); `-O` identical |
| `s0s6.py`, normal and `-O` | exit 0 | SHA-256 `ebecfa96…`, equal to the manifest; `-O` identical |
| `s0mutants.py` (quick) | pass; frozen rule clean | `c4f79d5d…`, equal to the manifest |
| `s0mutants.py --full` | pass | `895f17e6…`, equal to the manifest |
| `planted.py`, `radius_mutants.py`, `exact_small.py` | exit 0 | equal to the manifest |
| `rerun.py` | exit 0 | differs **only** in its timing line, so its manifest hash can never be reproduced (finding 6) |

**Refusal (v8-class guard).** Without the flag, `s0geom.Context(V8, …)` raises PermissionError
under A and under G; I confirmed this directly. Only `Context` is guarded.
`num_records(V8)` and `record_samples(V8, …)` run unguarded. That is harmless, since they are
combinatorics and no closure is involved, but the docstring's "every entry point refuses it" is
inaccurate.

## Findings

### 1. The enumeration program is absent from the code that would be frozen

There is no code anywhere in the package for:
- C11 (the P_A, P_G or P_A-dir checks);
- MISMATCH and minimal-witness selection on real records;
- the label generator: COLLAPSE_ALL, RESIDUE, BASE_RESIDUE, INCOMPLETE;
- the shard runner, the schema, the merge, the coverage check and the `result.json` and
  `expected-controls.json` writers;
- the dry run;
- the v8 S1a global bound driver;
- the orbit-representative enumeration with C8 count preservation on v8;
- the classification and degeneracy cross-tabulations.

`grep` finds none of them. The controls exercise only the engine (`closure`, `analyse`) on toys.
§12's freeze ("SHA-256 of every file in `stage0-code/`") would therefore freeze a plan whose
decision rule has no frozen implementation.

The two-layer remedy is R1.

### 2. Are the three safeguards independent?

**Code.** `s0ref` imports only `itertools`, and `s0native` only `collections`. Neither imports or
copies `s0geom`.
- `s0ref` re-derives contexts, cones (explicit cell sets), tips and frame from the plan text. It
  uses a different algorithm: brute-force greatest self-supporting subset up to 8 non-fixed
  quantities, and synchronous deletion above that.
- `s0native` re-implements the rule (the scalar and bit-sliced forms agree in the self-test).

**What they share, by design.** The plan-text rule (radii, tips, frame), and v8's H table,
retyped. So C7, C17 and C18 test implementation against the plan. Rule against dynamics is tested
by C1, C2 and C15, against `s0native`. This is the right split. `s0ref` itself is never compared
with native code, but its agreement with production, plus production's agreement with native,
covers it transitively. C7 draws its records from `s0geom.record_at`, which C13's independent
recount then checks.

**Is C15 exhaustive and exact? Yes, within its windows.**
- `Sliced` enumerates all 8^|W| assignments of the window.
- `value()` raises KeyError for any dependence outside W, so every pooled quantity provably
  depends only on window variables.
- `exact_independent` is integer counting of the full joint law.
- The G variant conditions on the frame variables (`ret | frame`), which is the right statement.

**Limits, which are stated or should be:**
- 1D covers F depth ≤ 3 and B depth ≤ 2. The 2D pool is a single depth-1 quantity plus window
  variables, in effect the constraint block.
- Depth-2 in 2D needs 13 triples (39 bits), so the plan's statement that off-axis is "beyond the
  windows" is correct.
- 3D soundness at v8's depths therefore rests on the uniform-in-d proof, on C2 and on C18's
  conformance audit. That makes finding 3's depth gap load-bearing.

### 3. Control ranges as stated against as coded

| control | plan says | code does |
| --- | --- | --- |
| C1 | A: F 0–15, B 0–8; G: 0–23; "forward and backward from both pairs" | depths 0–4, pair (0, 1) only (`s0controls.py:51`) |
| C2 | every depth used | depths 0–4 (`:82`) |
| C3 | A: F 1–15, B 1–8; G: F 1–23 | depths 1–6 (`:126`) |

C1 and C2 at v8's depths involve no v8 configuration (generic random backgrounds), so they are
permitted. Required: R2.

**Other control points:**
- C10 does not check "N in-frame under G", although the plan asserts it. Its fixed-quantity check
  cannot fail by construction, since `closure` iterates only non-fixed quantities. Call it a code
  invariant.
- C8's count-preservation check covers survivor counts only (`:239-241`). The owner asked that
  the reduction preserve the *relevant* counts. Required: R3.

### 4. Mutants and the drafter's non-adoptions

**Every non-equivalent mutant is caught by a named control**, in my quick and full re-runs. The
caught sets match §6's bracketed observations.

**The non-adoptions are all accepted:**
- **The symmetric-radius countercontrol is equivalent.** The parity argument is confirmed below.
  My r1 acceptance of C5 as "able to fail" was wrong for even-class contexts. Replacing it with
  radius ±2 and "far cone deleted" is right; all three are caught.
- **The B-only off-axis mutant has nothing to act on under G.** In the pair (−1, 0), every
  quantity at depth ≥ 1 is F type, and the slice −1 samples are B type at depth 0, which has no
  off-axis tips. It is caught under A.
- **Off-axis mutants are not in C15**, correctly: they need depth ≥ 2 in two or more dimensions,
  which exceeds the windows. C2, C3 and C18 catch them.
- **Near-only is caught only by C3's block on the toy class.** That is acceptable. Near-only is an
  over-retention error, the direction unfavourable to collapse, and L3 is reported beside L3′ on
  every record anyway.

**The owner's question: the parity argument holds.** Take an even-class quantity (c, t) and an
even-class cell (u, s) on its far slice. Since |u−c| ≡ |u| − |c| ≡ t − s (mod 2):
- for F type, t = L + d and s = L − 1, so |u−c| ≡ d + 1 ≡ d − 1;
- for B type, the mirror case gives the same;
- under G, t − (−1) = d + 1 also gives the same.

So every even-class far cell within distance d is at distance ≤ d − 1, and radii d and d − 1
select the same even cells. Two conditions are needed:
- E2: odd samples dropped, so tips and covers are even-class only. The `keep_odd` mutant breaks
  this and is caught.
- Φ, p and the port samples all even, which holds for v8 and for the r2 toys.

Measured: the parity-blind radius gives 0 of 400 differences (`rerun.out`). It fails only C1's
definitional radius check. My own r1 toy at the correct parity gave the same.

### 5. S6 and the classification

**S6 is correct and correctly scoped.**
- It works on the 21-bit structure only: J = (q8.B, q10.D, q10.B) and K as in v8
  (`checks.py:314-317`), with p = V ⊕ H(⊕ six).
- All 22 subsets have 0 target-law classes.
- The positive control (v6's flag) makes every class target-law. The negative control (permuted
  thresholds) leaves 64 non-target classes.
- It is labelled in the plan, but its JSON carries no label. Nit: add `"label": "proof-check of
  PO8; not a result"`.

**The three-way classification is correctly defined.** It covers: (a) the post-closure
public-set classes; (b) the private Φ cells, J cells and source cells; (c) the stated limit. It is
implemented in `analyse`. Under A the J-cell selection hard-codes the ±z neighbours, which are
q8 and q10, so it is correct for v8.

### 6. Evidence retention (§A.42, C13)

`runs/` holds one of the eight outputs. The manifest has hashes for the other seven, but not the
outputs themselves. Retain all eight.

Move timing lines out of `rerun.py`'s deterministic output, or mark that step non-reproducible.
As it stands, its recorded hash cannot be regenerated.

### 7. The §A.41 table

Rows that need correcting:
- "propositions agree with the computation | C11, MISMATCH": there is no implementation yet
  (finding 1).
- C1, C2 and C3 depth claims (finding 3).
- "orbit representatives … C8": survivor counts only (finding 3).
- C10's "N in-frame".
- "the evidence is … retained | C13": seven outputs are missing (finding 6).

All other rows are satisfied by code I re-ran.

### 8. Open items

| item | recommendation |
| --- | --- |
| S2 | Accept. |
| S3 | Accept. |
| S5 | Accept. Note that on v8 contexts (up to about 29 non-fixed quantities) `s0ref` runs in synchronous mode, so C7 there compares two fixed-point algorithms, not brute force. |
| S7 | Accept. |
| S8 | Accept. |
| S10 | Accept. |
| S11 | Adopt P_A-dir. It needs the C11 code of finding 1. |

## Required changes before freeze

- **R1. Two-layer freeze (owner decision O1).** State explicitly that this freeze covers:
  - the plan;
  - the engine and the reference code (`s0geom`, `s0ref`, `s0native`);
  - the control suite and the mutants;
  - S6;
  - `stage0-design/sym_check.py`, which carries C0's v8 combinatorics (counts, orbits, Burnside):
    either add it to the frozen set or fold it into `s0controls`.

  The enumeration program in finding 1 is then a second artifact. It is written to this plan,
  independently reviewed and hash-frozen before any launch authorization, and nothing executes
  without it. The alternative is to complete it now and re-review.
- **R2. Align C1, C2 and C3 with their stated depths.** Either run them at A F 0–15, B 0–8 and G
  0–23 (the planted families at those depths, in CI if heavy), or restate the plan's ranges. The
  first is recommended, because 3D soundness beyond depth 4 otherwise rests on proof alone.
- **R3. C8 count preservation over every reported count.** That means survivor counts, Φ-, J- and
  L3/L3′ disagreement counts, the degeneracy cross-tabulations, and observer-class counts
  (computed with class orbits). G-linkage stays per record.
- **R4. Small fixes:**
  - make C10 check that N is in-frame under G, and label its fixed-quantity check a code
    invariant;
  - correct the guard docstring;
  - add S6's label to its JSON.
- **R5. Retain all eight run outputs** in `runs/`, and make `rerun.py`'s retained output
  deterministic.
- **R6. Correct the §A.41 rows** listed in finding 7.

## Remaining owner decisions

- **O1.** Two-layer freeze (recommended) or a complete program before freeze (R1).
- **S11.** Adopt P_A-dir (recommended).
- **S2, S3, S5, S7, S8, S10:** accept as proposed.
- **Pre-execution certificate:** see below.

## For information: fail-closed behaviour today, and the certificate

**(a) A configuration that differs from a frozen configuration or hash set: no.**
- Nothing in `stage0-code/` checks its own hashes or the configuration constants (V8 setup,
  `Rule` fields, toy setups, sampling parameters).
- `s0run.py` records hashes but compares them against nothing.
- `Rule()` defaults to the frozen rule. Any mutant is reachable through `--rule`, or by editing,
  without refusal.

**(b) A soundness, completeness or non-vacuity control fails: partly.**
- `s0controls.py` exits 2 and lists the failures, and `s0mutants.py` exits 1 if a mutant escapes.
- But no production runner exists that is gated on them. The engine computes closures whether or
  not the controls ran or passed.

**What the pre-execution certificate would need to add:**
1. **A frozen manifest** of code SHA-256 values and configuration constants: V8 setup, `Rule`
   fields, k, the depth ranges, sampling rates, S_max, the budget and the shard plan. The runner
   verifies it at start-up, and on any mismatch prints VOID and exits 2 before computing anything.
2. **Pre-flight controls in the same job at the exact commit:** C0–C3, C6, C12–C18, the refusal
   check, the native self-test and S6. The runner reads their structured results (§A.44). Any
   failure means VOID, with no enumeration.
3. **A mutant-campaign result** for the same code hashes, present and passing. Otherwise refuse.
4. **In-run gates:**
   - C7 on its sample;
   - C8 equivariance and full count preservation on its sampled and survivor orbits;
   - C9 against the computed v8 S1a bound;
   - C11 on every survivor;
   - C17 and C18 on a sample of v8 records.

   Any failure gives VOID or MISMATCH under §5, never a label.
5. **A merge that refuses** shards whose code or configuration digests differ from the manifest or
   from each other, or whose coverage is not exact (INCOMPLETE).
6. **The v8 authorization** passed only through an owner-designated input bound to the exact
   commit, and echoed into `result.json`. The `authorized_v8` flag is otherwise unreachable.
7. **Determinism:** `-O` identity per shard and merged. The dry run is mandatory before the real
   run.
8. **Labels** generated only by the merge, from structured files; no label from logs.
