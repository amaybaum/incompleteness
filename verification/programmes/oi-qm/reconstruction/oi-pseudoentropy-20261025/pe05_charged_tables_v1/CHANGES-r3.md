# PE-05 plan: changes from revision 2 to revision 3

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

## Re-check nits P1–P3 (`review/RECHECK-r3.md`, ACCEPT WITH NITS)

Applied in place, on `7a283d39`, as part of revision 3.

| Item | Re-check's requirement | Edit |
|---|---|---|
| P1 | Put the body content that depends on O1, O10 and O5 under TH's `assumes` check | **New `dependent` entries,** each tagged `["O1:i", "O10:full"]`: `CH_IFF_boundary_records` (the eight records), `PL_E_boundary`, `INC_RE_checkpoint`, `E_void_rule` and `search_range_R_contains_E`. Also new: `EN_meaning`, tagged `["O10:full"]`, and `secondary_comparisons`, tagged O5, O7 and O9. **O5 tag added** to `secondary_n`, `secondary_population` and `sim_reporting`. **Body pointers:** each item in §1.3 (PL), §3.4, §5 (CH-IFF, EN, INC-RE) and §6 item 4 now names its block entry and the decisions it holds under. **§9 table:** the O1 (ii), O5 and O10 rows name the entries that must be restated. The block parses as JSON with 22 `dependent` entries, every one carrying `assumes`. |
| P2 | Remove the stale "(this file, uncommitted)" from PLAN's header | The header now says "Revision 3 (this file)", notes that commit identifiers for the file live in the CHANGES files and the branch history, and adds `7a283d39` as the base of the P1–P3 edits. |
| P3 | Schema ids and the block tag survive O8 | **§5:** a "Fixed identifiers" bullet. `pe02-shard/1`, `pe02-measurements/1`, `pe02-verdict/1`, `pe02-rp01/1` and `pe02-parameters` are fixed identifiers, not stage labels or ordinals. They stay unchanged whatever O8 decides and are never reused. **§9:** the O8 row says so. |

NOTES §1 and §10 now record the re-check, so that they no longer say revision 3 is unchecked. The design scripts were
replayed after these edits, and all four outputs are byte-identical (`cmp`).

## Owner decisions recorded (2026-10-26); the O8 rename held

**The approval.** The owner (amaybaum, 2026-10-26, 18:54 UTC): "I approve all eleven PE-02 decisions (O1–O10, including O4b) as recommended, subject to the final nit confirmation and exact-version checks before freezing the plan."

**Decisions recorded.**
- **PLAN status:** "decisions recorded; frozen pending independent confirmation". The coordinator records the freeze.
- **Placeholders:** each `[OWNER: Ox]` is replaced by "Decided (Ox) (owner, amaybaum, 2026-10-26)" with the ruling, in
  §1.2 (O5), §2.1 (O10), §2.2 (O3), §2.3 (O1), §3.3 (O9), §3.4 (O4, O4b, O6) and §4.3 (O7).
- **§9:** the approval is quoted, and the last column is now the owner's ruling, quoted.
- **The block:**
  - `decisions` holds the rulings in the tags' `Ox:value` form, with `decided_by`;
  - `amendment` reads "none: decisions recorded in PLAN.md before freeze";
  - two entries close gaps in option-dependent coverage: `reported_models` (O2) and `ablation_controls` (CA-EQ and
    ACT-SIM on the clock-ablated generators, O5).
- **TH check, emulated on the block** (scratch script, not committed): it parses, has no `OPEN` value, and every one of
  the 24 `dependent` entries carries `assumes`, each item equal to a recorded `Ox:value`. Result: PASS.
- **Wording:** the TH row, the no-extension clause, the shard `params` field and the not-chosen option texts are reworded
  for decisions recorded in the plan rather than in a later amendment.

**O8 not applied, and why.**
- "PE-04" is already the thread README's stage "implications for quantum reconstruction" (`../README.md:199`). It is
  also cited as PE-04 in the retained thread review (`../review/REVIEW.md:51, :83`).
- The review's "next unused identifier, PE-04" overlooked the README's PE-03 and PE-04.
- Applying the ruling as written would give one identifier to two stages. That is the collision O8 was meant to remove,
  and it would fail the owner's freeze condition that the rename be consistent across the PR, plan, references and
  retained records.
- The directory is not moved, and "PE-02" still means the stage of #934 in this package.
- **Proposed instead, for the owner:** the next unused identifier, PE-05, with the same mechanics: `git mv` to
  `pe05_charged_tables_v1/`, update references, add `review/README.md` mapping old to new paths, and keep the schema ids
  and `pe02-parameters` as fixed identifiers.

## O8 applied: the stage is PE-05 (2026-10-26)

**The ruling.** The owner (amaybaum, 2026-10-26), later the same day: "Approved: rename the new stage to PE-05." / "PE-04
remains reserved for quantum reconstruction. Apply the rename consistently to #934, its plan, citations, and retained
records. Freeze after the three reviewer nits and independent confirmation pass." / "This authorizes the specification freeze, not experimental execution." It superseded the approval
table's "O8 — Rename to PE-04 and retitle #934 before freeze".

**What changed.**
- **Directory:** `git mv pe02_charged_tables_v1 pe05_charged_tables_v1`.
- **Renamed references:** every reference to this stage changes from "PE-02" to "PE-05", and every old path changes to
  the new one, in `PLAN.md`, `NOTES.md`, both CHANGES files and the four design scripts' header docstrings. The scripts'
  outputs are unchanged.
- **Kept as written:**
  - the other stage named PE-02 (computational versus physical);
  - verbatim owner quotations;
  - places that discuss the name itself as it then stood. These are records.
- **PLAN:** the header and §9's O8 row now record PE-05 with the owner's words. The parameters block reads
  `"O8": "PE-05"`. One line records that PE-04 was found taken. The "application held" text is removed.
- **Fixed identifiers (P3):** `pe02-shard/1`, `pe02-measurements/1`, `pe02-verdict/1`, `pe02-rp01/1` and
  `pe02-parameters` are unchanged.
- **Thread README:** a PE-05 entry is added after PE-04. Nothing is renumbered, and the README's own PE-02 is
  untouched.
- **`review/`:** the retained files are byte-unchanged. A new `review/README.md` records the working name and maps the
  old paths to the new ones.
- **Issue #934:** retitled to PE-05 on GitHub, with its body updated and a rename comment posted
  (issuecomment-6425664988), outside this working tree.

## Independent confirmation nits C1–C5 (`review-confirm-PE05`, ACCEPT WITH NITS)

Applied on `7b469183`, in the commit proposed as the freeze commit.

| Item | Edit |
|---|---|
| C1 | **Thread README.** The PE-05 entry moves from after PE-04 to the end of the file, under "Stages added after the first milestone". Lines 1–277 are byte-identical to `a611f943` (`cmp`), so PE-01's frozen citations `README.md:265`, `:268–277` and `:252–261` resolve at the current head as well. |
| C2 | **Timeless status lines.** PLAN and NOTES now read "Specification; frozen at the commit named in the freeze record on #923", and the README entry says the same. NOTES §10's "Freeze still needs …" becomes a statement of how each freeze condition is met. No freeze commit or digest is written into the files. |
| C3 | **(a)** `fixed.PE05_env` is added (Python 3.12, numpy 2.2.6, GitHub-hosted ubuntu-24.04, x86_64), with an ENV checkpoint row, TH refusal on a mismatch, and a §10 line. **(b)** The freeze record names the exact commit and the sha256 of PLAN, NOTES and the parameters block. NOTES §10 records that both readings are applied. |
| C4 | **Verbatim quotes.** The 18:54 UTC approval is quoted verbatim, without the paraphrased "authorizes specification freeze". The authorization sentence is quoted as the owner wrote it later the same day, "This authorizes the specification freeze, not experimental execution.". The rename ruling is quoted in its separate parts. The §9 ruling cells are marked as summaries of the approval table, not quotations. The table's O8 entry is quoted, together with its supersession by PE-05. |
| C5 | The #934 retitle is recorded above. |
| C6 | Left as it is. |
