# PE-02 plan revision 3: diff-only re-check

- **Range:** `5b2ae247..b339c4b2` on `research/oi-pseudoentropy-20261025`, one commit.
- **Files touched:**
  - changed: `PLAN.md`, `NOTES.md`, `CHANGES-r2.md`;
  - added: `CHANGES-r3.md`, `design/charge_ranges.{py,out}`, `design/linear_class_code.{py,out}`.
- **Reviewer:** the same independent reviewer as `REVIEW.md` and `RECHECK-r2.md`.
- **Method:** read-only, design checks only.
  - Fetched into the existing clone and read with `git show` snapshots.
  - Scripts run with `python3 -I`.
  - No experiment was run and nothing was committed.

## Verdict: **ACCEPT WITH NITS**

- **N1–N7 are applied as specified.**
- **The drafter's three additions are correct:**
  - the `G_clkfix_u` `emb_m3_passive` caps;
  - the `plin_m1` consequence under a class-specific code;
  - O10's alternative ranges.
- **The new design scripts replay byte for byte** and agree with `r2_checks.out`.
- **No new exclusion favours the claim.**
- **One gap remains in N3's mechanism (P1).** A few values outside the parameters block depend on O1 and O10 and are
  not under TH's `assumes` check. They matter only if the owner chooses a non-recommended option, where they would
  void the stage or quietly weaken two controls. The fix is mechanical. It should be made before freeze and confirmed
  by a glance at the diff; no further full re-check is needed.

## 1. N1–N7

| Item | Status | Check |
|---|---|---|
| N1 | applied | Details below. |
| N2 | applied | Details below. |
| N3 | applied, with one residual | See §4 and P1. |
| N4 | applied | `rp01_env.json` (`pe02-rp01/1`) carries the versions, head, sha256 and comparison. The replayed shard is untouched, and the RP-01 row is updated. |
| N5 | applied in NOTES and CHANGES-r2 | The PLAN header still says "Revision 3 (this file, uncommitted)" with no time qualifier, and it is committed at `b339c4b2` (P2). |
| N6 | applied | "no window with K ≤ 15 (the sweep's range)". |
| N7 | applied | $F_C^{\rm TA}$ is labelled a component sum. Under E it omits γ(m+1), χ and γ(K+1), and is not a code length. `charge_ranges.py` uses the same definition. |

**N1 in detail.**
- §1.2 "Search range": `G_clkfix_u` is searched over its θ = n+2 region whichever value governs.
- §3.4 searches Part B up to $K^R_{\max}(n,1;\theta_{\max})$.
- The block's per-n values at n+2 match `r2_checks.out`:
  - R: n = 12 → 1, 14 → 3, 16 → 7, 18 → 15, 20 → 31, 22 → 63, 24 → 127;
  - E: n = 13 → 1, 14 → 2, 16 → 3, 17 → 6, 19 → 7, 20 → 14, 22 → 15, 23 → 30, 24 → 30.
- §2.4 is qualified to θ = n+1, and the `G_clkfix_u`, n = 8, m = 0, R cell (K = 4..7) has status `NONE` (proved
  zero, computed by M0). `charge_ranges.out` confirms it is the only non-empty full-description cell at n ≤ 8.
- AR-C now compares at each generator's θ values and derives cell status from the recomputed region.
- The onsets are added: n ≥ 16 (R) and 17 (E) at n+2.

**N2 in detail.**
- The new status `NOT_IN_SEARCH_RANGE` applies to U cells whose region is non-empty but outside the search range by
  design.
- M0 cells are `NONE` tagged `proved-zero`, and never count as searched.
- `NO_WITNESS_IN_SCOPE` and `NEITHER` both need a searched non-empty cell for each model or activity level compared.
  Otherwise the outcome is `REGION_EMPTY_ALL`, with no factor verdict, printed as a property of the model.
- At Part B n = 9..16, U is `NOT_IN_SEARCH_RANGE`, C is `REGION_EMPTY` and m = 0 is `proved-zero`. The factor outcome
  is therefore `REGION_EMPTY_ALL`, not the favourable `NO_WITNESS_IN_SCOPE`. This is correct.

## 2. The drafter's additions

**Part A `emb_m3_passive` caps for `G_clkfix_u`: correct.**
- The U region at θ = n+2 for m = 3 is $c(K) \le n - 2$: K ≤ 31 at n = 7 and K ≤ 63 at n = 8.
- `G_clkfix` keeps PE-01's A1 caps (15, 31), which are the θ = n+1 values.
- The change widens the search; it never narrows it.

**`plin_m1` under a class-specific code from n = 16: correct.**
- $|\mathrm{GL}(1,2)| = 1$, so the code is 7 + γ(K+1) bits, and $F = c + 2 + 7 + |\gamma(K+1)| = 17$ at K = 4..6. That
  needs n ≥ 16.
- At n = 16 the universal R range for m = 1 is K ≤ 3, which is empty, so this is a genuinely new cell under that
  model.
- `linear_class_code.out` also gives:
  - `plin_m2` at n = 22, 23 (K ≤ 6) and n = 24 (K ≤ 7);
  - at θ = n+2, `plin_m1` from n = 15 and `plin_m2` from n = 21;
  - `plin_m3` and `plin_m4` empty for n ≤ 24;
  - $|\mathrm{GL}(m,2)|$ = 1, 6, 168, 20160, matching the product formula.
- The O3 row states this search consequence.

**O10's computed alternative: correct.** These are transition-and-action component sums at θ = n+1.

| m | R | E |
|---|---|---|
| 1 | charge 6, $F = c + 8$: from n = 10 | charge 4, $F = c + 6$: from n = 8 |
| 2 | empty for n ≤ 24 | charge 14, $F = c + 17$: from n = 19 |

- INC-RE fails under this option, because E's sum for m = 1 (4) is below R's (6).
- Part A gets non-empty charged cells: m = 0 at n = 4..8 (M0 zeros), and m = 1 under E at n = 8, K = 4..7.
- At θ = n+2, m = 2 starts at n = 18 (E) and 24 (R).
- All of this matches `charge_ranges.out`.

## 3. Replay

| Script | Result |
|---|---|
| `design/charge_ranges.py` | Byte-identical on rerun (`cmp`), about 47 s. Its θ = n+2 full-description rows equal `r2_checks.out` cell for cell (R and E, m = 0 and 1, n = 3..24). |
| `design/linear_class_code.py` | Byte-identical on rerun. |

The sha256 values match NOTES §4:
- `charge_ranges.py`: `8c63311f…`
- `charge_ranges.out`: `e2359f73…`
- `linear_class_code.py`: `08840902…`
- `linear_class_code.out`: `895da4bc…`

## 4. The parameters block

- **Structure.** The block parses as JSON with top-level keys `amendment`, `decisions`, `dependent` and `fixed`.
- **`decisions`:** O1–O10 and O4b, each `OPEN` with the review's recommendation. TH refuses `OPEN`.
- **`dependent`:** 15 entries, each carrying `assumes`. The tags are correct and, where they over-tag, they err toward
  forcing a restatement (for example, the n+2 ranges also assume O5):

  | Entry | Assumes |
  |---|---|
  | `theta`, `theta_by_n` | O1, O5 |
  | the four m = 1 K-range families | O1, O10, and O5 at n+2 |
  | `partB_n` | O4 |
  | `partB_search_classes` | O3, O4b, O10 |
  | `partA_charged_nonempty` | O1, O10, O5 |
  | `m3_passive_K_cap` | O1, O5 |
  | `M0_K_max_partB` | O4b |
  | `K0_n_max` | O6 |
  | `secondary_n`, `secondary_population` | O7 |
  | `sim_reporting` | O9 |

- **`fixed`:** nothing in it depends on a decision. `partB_K_min` = 4 rests only on the proved K′ = 0 zero; the rest
  are the PL/PL-mut ranges, n_ctl, the ACT-SIM and Z cross-check limits, δ, w, the d rules and the RP-01 environment.
- **TH** refuses any `assumes` mismatch unless the amendment restates the entry.
- **Residual (P1).** Some decision-dependent content lives in the body, not in the block, so TH's `assumes` check
  cannot see it. If the owner chose O10 "transition and action only", or O1 (ii):
  - **CH-IFF's eight synthetic boundary records** (n = 9/8, 13/12, 17/16, 20/19) would no longer sit at θ and θ+1. The
    control would still pass, but it would no longer test the boundary.
  - **PL's E-boundary property** ($F_E = \theta = 14$ at n_ctl = 13) would be lost in the same way.
  - **The INC-RE checkpoint and §6 item 4's E-void rule** would fail under O10's alternative, which the plan itself
    says breaks INC-RE. That would void the stage.
  - **§3.4's rule "search at $K^R_{\max}$, which contains $K^E_{\max}$"** would be false under that alternative.
  - **E would stop being a prefix code** under that alternative, because the E component sum is not a code. That
    changes what EN certifies.
  - **§4.3's comparisons on `G_clkfix`** depend on O5 ("uniform only" removes `G_clkfix`), but `secondary_*` and
    `sim_reporting` are tagged with O7 and O9 only.

  None of these defaults silently under the recommended options. Under the alternatives, two controls lose their
  boundary role without notice and one rule voids the stage.

## 5. Coverage

- **Widened:**
  - `G_clkfix_u` searched over its θ = n+2 region in Parts A and B;
  - its `emb_m3_passive` caps raised.
- **Unchanged and reviewed:**
  - m = 0 in Part B is the M0 control to K ≤ 63, with coverage beyond by proof, now as O4b (a) with the required
    verdict sentence;
  - transition-and-action and class-code regions are not searched under the recommended O10 and O3, and the O10 and
    O3 rows state what choosing them would add.
- **Nothing newly excluded favours the claim.**

## 6. Nits (P1 to fix before freeze; the rest in the same pass)

1. **P1.** Bring the decision-dependent body content into the TH mechanism:
   - add `dependent` entries for the CH-IFF boundary table, the PL E-boundary flag, the INC-RE checkpoint, §6 item 4's
     E-void rule and the §3.4 range rule, each with `assumes: ["O1:i", "O10:full"]`;
   - add O5 to the tags of the §4.3 comparison entries;
   - alternatively, state in the O1 and O10 rows that the resolving amendment must restate exactly these items.
2. **P2.** PLAN line 10 says "Revision 3 (this file, uncommitted)", but it is committed at `b339c4b2`. A commit-status
   claim inside the file goes stale by construction. Record SHAs only in the following CHANGES file, or use the "at
   the time of writing" qualifier as NOTES does.
3. **P3.** The schema ids (`pe02-shard/1`, `pe02-measurements/1`, `pe02-verdict/1`, `pe02-rp01/1`) and the
   `pe02-parameters` block tag embed the stage name, which O8 may change. Either declare them fixed identifiers
   independent of O8 (identifiers, not ordinals, so they survive a rename), or add them to `dependent` with
   `assumes: ["O8:…"]`.

## 7. Final owner-decision list, ready to put to the owner

| Id | Decision | Recommendation | If not the recommendation |
|---|---|---|---|
| O1 | θ under charged models | **(i) θ = n+1 for U, R, E** (`G_clkfix_u` per O5). It is the most stringent rule considered; every witness reports $F_C$ components, and every cell its minimum $F_C$, so another θ can be read off. | (ii) needs a generator encoding $D_C$ that the plan does not define; every θ, range, cap and the P1 items must be restated. |
| O2 | Governing charged models | **R and E, reported separately.** INC-RE: within the scope, every E-witness is an R-witness. | R only or E only: same search, different labels. |
| O3 | Description-complexity proxy | **Information only** (the reduced-form E length per witness). The class-code arithmetic is now a checked design fact. | A class-code model must search `plin_m1` at n = 16 (K 4..6) and `plin_m2` at n = 22..24 (K 4..7), with more for `G_clkfix_u` at n+2. |
| O4 | N_max | **24**, with the no-extension clause. | 22 drops n = 23, 24. 8 means no Part B, and every charged answer then comes from arithmetic. |
| O4b | m = 0 in Part B | **(a) the M0 control only, 1 ≤ K ≤ 63.** Coverage beyond rests on the M0 proof, and the verdict prints "m = 0 at K > 63: zero by M0 (proof); computed for K ≤ 63". | (b) a full search to $K^R_{\max}$ (≤ 1023; ≤ 2047 for `_u`), at about $10^{11}$–$10^{12}$ updates; it cannot change an outcome. |
| O5 | Clock-ablated prior; θ for `G_clkfix_u` | **Matched prior primary, uniform variant reported.** For `_u`, θ = n+2 governs (PE-01's $\log_2|\mathcal{C}|$) and n+1 is also reported. The search runs at n+2 either way. | Matched only drops `_u`. Uniform only drops `G_clkfix`, and with it the matched basis of CA-EQ, SIM-P1 and the backaction comparison. |
| O6 | K0 status at n > 8 | **Not computed.** | A fixed subfamily adds K0 runs; no witness range changes. |
| O7 | Secondary population | **All active members meeting (a′)–(e):** m = 2 on `G_clk`, n ∈ {4, 5}, as PE-01's data already fix. | Admissible-only reduces it to the n = 5, K = 7 cell (36 pairs). |
| O8 | Stage name | **Rename to PE-04 and retitle #934 before freeze**, because PE-01's frozen plan binds "PE-02" to the computational-versus-physical stage. Keep the schema ids as fixed identifiers (P3). | Keeping "PE-02" leaves two stages with one name in frozen records. |
| O9 | Lemma A-SIM | **Adopt**, as revised: one-step hypothesis, bijectivity step, $m' \le m+1$ upper-bound wording. Checked by proof and by exhaustive toy checks. | Dropping it removes SIM-P1 and the twin-footprint reporting; ACT-SIM stays, uninterpreted. |
| O10 | Charge scope | **The full description (ρ, a, readout, K) governs**, because an interpreter needs all of it. The transition-and-action component sum $F^{\rm TA}$ is reported per witness. | Transition and action only: m = 1 from n = 8 (E sum) and 10 (R); m = 2 from n = 19 (E sum); charged cells in Part A; `emb_m2_all` in Part B; INC-RE fails. Every dependent value and the P1 items must be restated. |

## Files

In this directory: `RECHECK-r3.md`. No new scripts were needed. The checks used the drafter's two design scripts,
replayed above, and the existing `r2_checks.out` for comparison.
