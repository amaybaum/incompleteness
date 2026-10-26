# PE-02 plan: changes from revision 2 to revision 3

**Status: WIP / UNREVIEWED; planning only; no execution authorized.**

- **From:** revision 2, committed at `58441eb2`.
- **Re-review:** `review/RECHECK-r2.md`, committed at `5b2ae247`. Verdict: REVISE, narrowly. N1–N3 are required and
  N4–N7 are nits; the O3 arithmetic is recommended.
- **To:** revision 3, drafted on `5b2ae247`, uncommitted at the time of writing.
- **Files changed:** `PLAN.md`, `NOTES.md` and `CHANGES-r2.md` (the N5 correction only).
- **Files added:** this file; `design/charge_ranges.py` and `.out`; `design/linear_class_code.py` and `.out`.

Section references are to revision 3's `PLAN.md` unless marked otherwise.

| Item | Re-review's requirement | Edit in revision 3 |
|---|---|---|
| N1 | Search `G_clkfix_u` over its θ = n+2 region; per-n values at n+2; qualify "every charged region empty at n ≤ 8"; the n = 8 m = 0 R cell is `NONE`, not `REGION_EMPTY`; AR-C must not halt | **§1.2:** a new "Search range" bullet. `G_clkfix_u` is searched at the larger reported θ whichever value governs. **§3.4:** Part B's K range is $K^R_{\max}$ at $\theta_{\max}(\varphi)$, which is n+2 for `G_clkfix_u`. Part A's `emb_m3_passive` caps for `G_clkfix_u` are raised to the n+2 region (31 at n = 7, 63 at n = 8); the drafter found this gap in the same pass. **§2.4:** the n ≤ 8 statement is qualified to θ = n+1, with the `G_clkfix_u` exception stated (n = 8, m = 0, R, K = 4..7, status `NONE`, proved zero, computed by M0). The onset adds n ≥ 16 (R) and 17 (E) at θ = n+2. **§9:** `K_R_max_m1_theta_n+2` and `K_E_max_m1_theta_n+2` per n, `theta_by_n` at n+2, and `partA_charged_nonempty`. **AR-C** now compares at each generator's θ values, including the exception, and derives cell status from the recomputed region. **§10:** Part B cost row updated. **Design:** `design/charge_ranges.py` computes every value; its n+2 values agree with `review/r2_checks.out`. |
| N2 | U cells outside the search range get their own status; `NO_WITNESS_IN_SCOPE` only with a searched non-empty cell per model | **§6 item 3:** new status `NOT_IN_SEARCH_RANGE`, and M0 control cells are tagged `proved-zero` and never count as searched. **§6 item 4:** `NO_WITNESS_IN_SCOPE` requires, for each of U and C, at least one searched non-empty cell of a search class at that n. Otherwise the new `REGION_EMPTY_ALL` applies, with no factor verdict. **§6 item 5:** `NEITHER` has the same requirement. **§6 item 9:** `REGION_EMPTY_ALL` is printed as a property of the model. **§3.4:** U cells at n with an empty charged range are `NOT_IN_SEARCH_RANGE`. |
| N3 | Tag dependent values with the decisions they assume; TH refuses a mismatch; state each option's effect on ranges (O10's TA option needs a recomputed range); split out O4b | **§9 block** restructured into `decisions`, `dependent` and `fixed`. Every dependent value carries `assumes`: θ, `theta_by_n`, the four K-range families, `partB_n`, `partB_search_classes`, `partA_charged_nonempty`, `m3_passive_K_cap`, `M0_K_max_partB`, `K0_n_max`, `secondary_n`, `secondary_population` and `sim_reporting`. **TH row:** refuses any `assumes` mismatch unless the amendment restates the entry. **§9 table:** a column gives each option's effect on ranges and dependent values. O10's TA option is computed in `design/charge_ranges.out`: m = 1 from n = 8 (E sum) and 10 (R), m = 2 from n = 19 (E sum), non-empty Part A cells, and INC-RE broken. **§2.1** states this under O10. **O4b** is a new `OPEN` placeholder (§3.4, §9). "Done in revision 2" is removed from NOTES. The verdict text "m = 0 at K > 63: zero by M0 (proof); computed for K ≤ 63" is required under O4b (a) (§3.4, §6 item 9). |
| O3 arithmetic | Commit the class-code arithmetic as a design fact; state its consequence in O3's option text | `design/linear_class_code.py` counts $|\mathrm{GL}(m,2)|$ by enumeration and evaluates the code. **§2.2:** `plin_m2` at n = 22, 23 (K = 4..6) and n = 24 (K = 4..7); `plin_m1` from n = 16. **§9 O3 row** states the search consequence. The `plin_m1` at n = 16 consequence is the drafter's addition from the same script. |
| N4 | RP-01 versions: the replayed shard must stay byte-identical | **§5 control 1:** the RP-01 job writes its own `rp01_env.json` (`pe02-rp01/1`) with the versions, the head, the shard's sha256 and the comparison; the replayed shard is not modified. The RP-01 table row is updated. |
| N5 | Correct the "uncommitted" statements (R15 regression) | NOTES §1 now records revision 2 at `58441eb2` and the re-review at `5b2ae247`, and says revision 3 is uncommitted at the time of writing. `CHANGES-r2.md`: "To" now reads committed at `58441eb2`, the R15 row says revision 2 was not yet committed when drafted, and the closing line says the drafter committed nothing. |
| N6 | PL: K ≤ 15 | §5 control 3: "no window with K ≤ 15 (the sweep's range)". |
| N7 | Label $F_E^{\rm TA}$ as a component sum | §2.1: $F_C^{\rm TA}$ is a component sum reported for information. Under E it omits γ(m+1), the readout and γ(K+1), and is not the length of any code. The design script uses the same definition. |

## Owner placeholders

All remain `OPEN`, each with the review's recommendation: O1–O10, plus the new O4b. The stage name (O8) stays "PE-02"
with the header placeholder.

## Replay of the design scripts

All four scripts in `design/` were run with `python3 -I`, and each output compares byte-identical (`cmp`) with the
file beside it:
- `least_primitive.out` and `charge_arith.out`, committed at `902c4c0d`;
- `charge_ranges.out` and `linear_class_code.out`, new in this revision.

The sha256 values are in NOTES §4.

## Not done

- No experiment was run, no PE-01 cell was recomputed, and the drafter committed nothing.
- No owner choice was made.
