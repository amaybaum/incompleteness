# PE-02 plan revision 2: diff-only re-review

- **Range:** `2bb45e0b..58441eb2` on `research/oi-pseudoentropy-20261025`, one commit, `58441eb2`. It changes
  `PLAN.md`, `NOTES.md` and adds `CHANGES-r2.md`; nothing outside the stage directory.
- **Reviewer:** the same independent reviewer as `review/REVIEW.md`.
- **Method:** read-only.
  - `git fetch` into the existing clone, then `git show` snapshots.
  - Design checks on toy instances only, in `r2_checks.py` / `r2_checks.out` beside this file.
  - No experiment was run and nothing was committed.

## Verdict: **REVISE**, narrowly

Every R item is applied correctly. Three new findings must be fixed before freeze:
- **N1:** a coverage gap that favours the claim;
- **N2:** a label that would print a favourable reading where nothing was searched;
- **N3:** placeholders whose dependent parameters silently assume the recommended options.

The fixes are small and need no redesign. N4–N7 are nits.

***

## 1. The R items

| Item | Status | Notes |
|---|---|---|
| R1 | correct | §1.3, control 3 and `PL_mut_K_range` [1, 13]. Z(`G_weak_mut`) = n holds, because $c_0 = 1$ brings $h_0$ into $Y_{n-1}$. Nit N6. |
| R2 | correct | The restatement in (1) and (2) is right, and only the reported witness falls under (1), as I found. **The eight synthetic records check** at K = 7, c = 3: m = 0 R gives $F_R = 10$, at n = 9 (θ) and n = 8 (θ+1); m = 0 E gives $F_E = 14$, at n = 13 and 12; m = 1 R gives 18, at n = 17 and 16; m = 1 E gives 21, at n = 20 and 19. Every pair is exactly at θ and θ+1. |
| R3 | correct | Detail below. |
| R4 | correct | The M0 proof in §2.4 is right. The round satisfies $x' \oplus q' = x \oplus q \oplus a$, so it maps $S_t$ onto $S_{t+1}$ of equal size, and $S_t$ is balanced in x. The class table and rationale are fixed. The scope change is discussed in §2. |
| R5 | correct | INC-RE is in §2.4 with the right differences. Part B uses $K^R_{\max}$. §6 item 4 has the void rule. |
| R6, reporting | correct | Components, $F_C^{\rm TA}$, per-cell minima, NOTES O1 corrected. Nit N7. |
| R7 | correct in §1.2, but incomplete in the search ranges | see N1 |
| R8 | correct | Every outcome is per n, with matched K ranges in Part B. See N2 for a consequence. |
| R9 | correct | The §4.3 statements match the retained `windows` I read: n = 4, K = 7–9 (K_cx = 9); n = 5, K = 7 and 10 (K_cx = 20); `emb_m1_all` and `emb_m2_passive` have no window. **SIM-P1** gives a falsifiable prediction: no active m = 1 window on `G_clkfix` at n ≤ 8. The generated sentence is narrowed. |
| R10 | correct | Schemas and keys are stated. Exit statuses are host step conclusions, with marker steps, and `host_conclusions.json` comes from the API. |
| R11 | correct | All the rows asked for are present. The ACT-SIM non-vacuity ranges match the toy evidence: `G_clk` at n = 3 fails in 39 of 130 cases, and the mutants fail at n = 3. Nit N4. |
| R12 | correct | Step 1 is exactly the missing argument: the same hidden image for both x, injectivity, so the map on x is the identity or the flip. T2 is stated as an upper bound. |
| R13 | correct | No-extension clause. The block's per-n values equal `design/charge_arith.out`: R, m = 1 at n = 13..24 and E, m = 1 at n = 14..24 match. TH refuses `OPEN`. See N3. |
| R14 | correct | MSB-first throughout, PE-01's labelling, γ checked MSB-first. |
| R15 | **regressed** | see N5 |
| UX | correct | Full-subclass and passive-subclass counts, K by K, K ≤ K_cx, `abs` and `signed`, n = 3..8. A-pop computes all members. |

**R3 in detail. The zero argument:**
- Range 1 ≤ K′ ≤ Z, with K′ = 0 only for uniform $x_0$: correct.
- The conditional proof sketch is right. With $c_{K'-1}$ a function of $x_0$ and $Y_{0:K'-2}$, joint uniformity given $x_0$ makes $Y_{K'-1}$ uniform given the guess and the control.

**Per-generator methods:**
- `G_lin`, `G_clk`: rank over all $2^k$ sequences, with exhaustive agreement at n ≤ 12. Correct.
- `G_filt`: enumeration over h, valid since $\sigma_0 = \sigma_1$.
- `G_clkfix`, `G_clkfix_u`: enumeration over the conditional support, with no rank method.

**The new bound $Z(\texttt{G\_clkfix}),\ Z(\texttt{G\_clkfix\_u}) \ge Z(\texttt{G\_clk})$: the proof is correct.**
- $q_{t+1} = q_t \oplus \ell(h_{t+1}) = q_t \oplus Y_t$, so given $(x_0, q_0)$ the clock schedule is
  $c_t(z) = q_0 \oplus z_0 \oplus \dots \oplus z_{t-1}$.
- For each fixed z, the event $\{Y_{0:k-1} = z\}$ equals "`G_clk`'s increments under the fixed sequence $c(z)$ equal
  z", and h is uniform given $(x_0, q_0)$ under both priors.
- That probability is $2^{-k}$ for $k \le Z(\texttt{G\_clk})$. Averaging over $q_0$ covers `_u`.
- **Toy check (`r2_checks.out`),** exhaustive over the conditional support. Z(`G_clk`) is 2, 3, 3, 4 at n = 3..6,
  reproducing PE-01's drafting values. The matched and uniform `G_clkfix` give equal values at n = 3..6, and 4 and 4
  at n = 7. The bound holds, with equality in every toy case.

**Coverage no longer depends on Z:** Part A uses 1 ≤ K, and Part B uses K ≥ 4 from the K′ = 0 zero alone.

## 2. The two items not applied as written

**O3 arithmetic.** Leaving the linear-filter code arithmetic out of `design/` is acceptable for the plan text: §2.2
records the limit plainly and makes no claim from it.
- Revision 2 makes the arithmetic more relevant than before, because Z no longer bounds any search.
- Under a class-specific code (selector, γ(m+1), GL(2,2) index, b, c, e, γ(K+1)), `plin_m2` has $F = c + 15 + |\gamma(K+1)|$.
  That is 23 at K = 4..6, needing n ≥ 22, and 25 at K = 7, needing n ≥ 24.
- So if the owner chose a third, class-code model under O3, `plin_m2` would have to be **searched** at n = 22..24,
  K = 4..7. It could no longer be dismissed through Z.
- **Recommendation (not blocking):** commit the arithmetic as a small `design/` script before the owner decides O3, and
  state this search consequence in O3's option text. The owner then decides on a checked fact.

**Dropping the m = 0 search in Part B beyond M0 (K ≤ 63).**
- **Sound.** M0 is a proof, which I checked again above: m = 0 has advantage exactly 0 at every K on every (a′)
  generator. Dropping the search therefore excludes no candidate that could become a witness, and the claim is not
  made easier to sustain.
- Coverage for m = 0 at 63 < K ≤ $K^R_{\max}(n, 0)$ rests on the written proof, with the computation checking only
  K ≤ 63. That is a different verification layer.
- §6 items 8 and 9 already print M0 zeros as proved zeros. The verdict should also say "m = 0 at K > 63: zero by M0
  (proof); computed for K ≤ 63" wherever Part B coverage is stated.
- **Owner confirmation is needed.** It is a scope change to the computation, and the review offered it as an option
  under O4, not as an edit to apply. Revision 2 applies it in the body (§3.4 table, §10, the `M0_K_max_partB` block
  value), while O4 is still `OPEN` and labelled "done in revision 2".
- Make it its own placeholder, O4b, as part of N3.
- **Recommendation:** accept the cut. A full m = 0 search to $K^R_{\max}$ would cost about $10^{11}$–$10^{12}$
  updates at n = 24 and could not change any outcome.

## 3. New findings

**N1 (required; coverage in the favourable direction): `G_clkfix_u` at θ = n+2 is not searched over its region.**
- R7 reports `G_clkfix_u` at θ = n+1 and n+2, but Part B's K range and the block's `K_R_max_m1_by_n` and
  `K_E_max_m1_by_n` are computed at θ = n+1 only. At θ = n+2 the m = 1 region is larger (`r2_checks.out`):

  | | R | E |
  |---|---|---|
  | n = 16 | K ≤ 7, versus empty at n+1 | |
  | n = 17 | K ≤ 7 | K ≤ 6 |
  | n = 23 | K ≤ 63 | K ≤ 30 |
  | n = 24 | K ≤ 127, versus 63 | K ≤ 30 |

- As drafted, those cells would be either unsearched, which makes them INCOMPLETE and voids that factor, or, if the
  implementation trusts the n+1 range, silently narrower than the region they are reported against.
- **Fix:** for `G_clkfix_u`, the search range is $K^R_{\max}$ at the largest θ reported, and the block carries per-n
  values at θ = n+2.
- Relatedly, §2.4's "at n ≤ 8 every charged region is empty" and §3.4 Part A's "R and E structurally empty" hold only
  at θ = n+1.
  - For `G_clkfix_u` at θ = n+2 = 10 (n = 8), the m = 0 R region is K = 4..7. It is covered by M0, but its cell status
    is `NONE` (proved zero), not `REGION_EMPTY`.
  - Qualify both statements. Otherwise AR-C will disagree with §2.4 and halt the stage.

**N2 (required; labels): a favourable label where nothing is searched.**
- At Part B n = 9..16, every charged m = 1 region is empty at θ = n+1, m = 0 is a proved zero, and the U cells exist
  only "within the charged search range", which is also empty.
- Under §6 item 4 these n receive `NO_WITNESS_IN_SCOPE`, a label §6 item 9 lists as favourable, although no observer
  was searched at any K there.
- `REGION_EMPTY` is also the wrong status for those U cells. The U region at θ is non-empty; only the search was
  truncated, by design.
- **Fix:**
  - give U cells outside the searched range their own status (for example `NOT_IN_SEARCH_RANGE`);
  - require `NO_WITNESS_IN_SCOPE` to rest on at least one searched non-empty cell per model compared;
  - otherwise print `REGION_EMPTY_ALL` (no factor verdict) for that n.

**N3 (required; placeholders): dependent parameters silently assume the recommended options.**
- O1–O10 are each `OPEN` in the block and in §9, and TH refuses `OPEN`. That part is right.
- But several concrete block values and body ranges are computed under the recommended options and would be wrong
  under the others, with nothing forcing their revision:
  - `theta` / `theta_by_n` assume O1 (i);
  - `K_R_max_m1*` and `K_E_max_m1*` assume O1 (i), O10 (full description), and θ = n+1 for every generator (see N1);
  - `M0_K_max_partB` and §3.4's m = 0 handling assume the O4 cut (§2 above);
  - §4.3 and `secondary_n` assume O7 "all";
  - §3.4's "not computed at n > 8" assumes O6.
- O10's alternative, transition and action tables only, would open m = 1 from about n ≈ 10–13 and need a different
  Part B range. O10's option text does not say so.
- **Fix:**
  - tag each dependent value with the decisions it assumes (`"assumes": ["O1:i", "O10:full", …]`);
  - have TH refuse if the resolving amendment's decisions differ from those assumptions, unless the amendment restates
    the dependent values;
  - state each option's consequence for the search ranges in the §9 table;
  - split O4b (m = 0 in Part B) out of O4.

**N4 (nit): RP-01 versions.** "The shard records `sys.version` and `numpy.__version__`" cannot refer to the replayed
PE-01 shard. Its bytes must equal the original, which has no such keys (top-level keys: commit, controls,
measurements, mode, pending, preflight, recipe, schema, shard, tree). Say that the RP-01 job writes its own
`pe02`-schema record carrying the versions, alongside the byte-identical replay.

**N5 (nit, a regression of R15).** NOTES §1 (line 21) says revision 2 "is not committed", and CHANGES-r2 says "To:
revision 2, uncommitted". Both are committed at `58441eb2`. Correct them.

**N6 (nit).** PL forbids a `G_weak_mut` window "with K ≤ 16", but the sweep runs only to K ≤ 15 (`PL_K_max`). Use 15.
The statement holds at 16 as well, but a check cannot assert over K it does not compute.

**N7 (nit).** Under E, $F_E^{\rm TA}$ omits γ(m+1) and γ(K+1), so it is not a code length. Label it as a component sum
for information.

## 4. Owner placeholders

| | Status |
|---|---|
| O1–O10 | Each is present in §9 and the block as `OPEN` with the review's recommendation. No `OPEN` value can reach a run (TH). |
| Silent defaults | Only those listed in N3: the dependent values, and the O4 m = 0 cut applied in the body. |
| O8 | Correctly held as a header placeholder; the name stays "PE-02" until decided. |
| O9 | The lemma is "relied on only after the owner's decision". Correct. |

## 5. Coverage

| Change | Effect on the claim |
|---|---|
| Part A from K = 1 and Part B from K = 4, with Z off the search path | Coverage widened. |
| m = 0 in Part B: control to K ≤ 63, otherwise covered by proof | Nothing that could be a witness is excluded. Owner confirmation needed (O4b). |
| `G_clkfix_u` at θ = n+2 | Excluded over the region it is reported against (N1). This is the one exclusion in the favourable direction. |
| Transition-and-action-only regions (n ≈ 10–16, m = 1) | Not searched. This is legitimate only while O10 is undecided and stated as a scope limit, which §7 now does ("… and charge scope"). It must not survive an O10 choice of transition and action only (N3). |

## 6. Final owner-decision list, with recommendations

| Id | Decision | Recommendation |
|---|---|---|
| O1 | θ under charged models | (i) θ = n+1, the most stringent rule considered; $F_C$ components and per-cell minima reported. |
| O2 | Governing charged models | R and E, reported separately. INC-RE: in scope, E ⊆ R. |
| O3 | Description-complexity proxy | Information only. First commit the class-code arithmetic as a design fact, with its consequence: a class-code model would require searching `plin_m2` at n = 22..24, K = 4..7. |
| O4 | N_max | 24, with the no-extension clause. |
| O4b (new) | m = 0 in Part B | M0 control only, K ≤ 63, with coverage beyond by proof; the verdict states that layer. |
| O5 | Clock-ablated prior and θ for `G_clkfix_u` | Matched primary, uniform variant reported. θ for `_u`: n+2 governing, n+1 reported, with the search range at n+2 (N1). |
| O6 | K0 status at n > 8 | Not computed. |
| O7 | Secondary population | All (a′)–(e) members, with the known extent (m = 2, n ∈ {4, 5}) stated. |
| O8 | Stage name | Rename to PE-04 and retitle #934 before freeze. PE-01's frozen plan binds "PE-02" elsewhere. |
| O9 | Lemma A-SIM | Adopt, as revised: step 1 added, upper-bound wording. |
| O10 | Charge scope | The full description (ρ, a, readout, K) governs, with the reason stated; $F^{\rm TA}$ reported. If the owner instead chooses transition and action only, Part B's ranges must be recomputed under it (N3). |

**Required before freeze:** N1, N2, N3, then a diff-only recheck. N4–N7 can be fixed in the same pass.
