# Re-check of fee98794 (PE-01 plan, revision 3)

## What was read

- Commit `fee98794049dd12e28c30d163dc9dd981af65a68`, tree `a4abe9036232f9bb65e8a4d2c1d7e2056dfb8850`, parent `67a5cbe1`.
  It changes only `pe01_bounded_tests_v1/PLAN.md` (+76/−32).
- **PLAN.md read here:** blob `8389f1f45febd2bb6ffa3b2ad14785586fdbb59a`, sha256
  `85169310cad10144a4958bb7970cf8b467c169a3bff73dadf2ac8c4be91acf24`. It matches the coordinator's values. I extracted
  it read-only with `git show` to `revpe01/PLAN-fee98794.md`; line numbers below refer to that file.
- **Design check:** `revpe01/checks4.py`, output in `revpe01/checks4.out`. It parses both plan tables and compares
  them cell by cell with my independent recomputation from `revpe01/checks3.py`. It computes no PE-01 measurement.
- **Reviewer:** independent, read-only. No commits, no pushes.

## Verdict: ACCEPT WITH NITS

Both required items from the 67a5cbe1 re-check are resolved, and all five nits are applied. Nothing new is required.
Four nits remain (N1–N4), and one scope question should be listed in §10 as an owner decision (N5).

## 1. Required items from 67a5cbe1

- **The window floor and the tables: resolved.**
  - Z(φ) is defined at :385–387 exactly as in my design check.
  - The every-observer argument at :388–397 is correct: an adaptive control is a function of x₀ and earlier
    increments only; the window has probability 2^{−k}; x_{K′} = c_{K′−1} ⊕ Y_{K′−1}; and K′ = 0 is trivial.
  - The floor is K ≥ Z(φ)+4 for every generator (:398–399).
  - The Z table at :402–406 matches mine.
  - Both region tables match my recomputation in all 48 cells, with 0 mismatches (`checks4.out`).
  - The AR row (§5) derives Z exhaustively, cross-checks Z(G_lin) = n against PC, recomputes the region and requires
    cell-for-cell equality with the tables.
  - The verdict prints the recomputed region, not the table (§6: "recomputed (AR) from the measured Z(φ) and
    K_cx(φ)").
  - :407–411 labels the values as drafting values, not results, and says that a cell inside the region is not a claim
    that a witness exists. Both are correct.
  - The old overclaim at :379, "design-checked … reprints", has been removed.
- **The attribution rule: resolved.**
  - §6 item 4 (:332–335): resource-attributed if and only if some witness meets (a)–(e) but fails (f). Otherwise
    the verdict says "no witness within the enumerated scope at any footprint". It never says the record is
    unpredictable because of the observations available on the strength of a finite enumeration.
  - The Purpose paragraph (:12–15) points to the rule.

## 2. Nits from 67a5cbe1

| Nit | Status |
|---|---|
| CX reads the EX1, EX7, EX8 and IM3 flags and the global control flag | applied (CX row) |
| VG self-test covers the limitation sentence | applied (VG row: "a verdict text lacking … must fail") |
| Runs gated on θ and K_LP | applied: TH row (JSON records θ, K_LP and the amendment blob; ancestor check as for PIN; the run refuses to start without it), §6 :308, §10 last line |
| θ consequences restated | applied (§7 :437–447, §10). All consequence statements match the recomputed tables. |

## 3. The author's new assumption: the product prior

The Z argument needs x₀ independent of h and h uniform. Conditioning on x₀ removes any dependence on x₀'s own law.
The plan's prior meets both conditions at every place Z is used:
- **The primary generators:** μ is uniform on C_V × C_H (:56), which is uniform x₀ times uniform h.
- **The embedded composite:**
  - the joint prior is μ ⊗ δ_{v₀}, with v₀ = 0^m fixed (:108, :164, EX7);
  - the output bit starts at 0;
  - named larger observers are also given as explicit tables with a prepared state.
- **G_tape** is not in Z's scope, and G_dec is a control only.

No admissible configuration has a non-product prior, so the floor holds wherever Z is used. The assumption also does
not narrow PE-01's scope:
- the product prior is posit (iv), uniform invariant μ, which PE-01 adopts throughout;
- the same factorisation is what makes the settings measurement-independent (:108, EX7);
- a non-product prior would be outside PE-01, and Z would have to be recomputed for it. That belongs to a later stage,
  not here.

Two gaps in what is stated:
- **N1 (nit): the clock's initial value is unstated.** :173 does not say where the clock starts. A clock register
  started anywhere other than a fixed value would break both the product form and the trigger at K. *Fix:* "the clock
  starts at 0".
- **N2 (nit): the assumption has no checkpoint.** :397 states the assumption, but AR does not check it, and §A.41
  asks for a cheap mitigation once an assumption is named. *Fix:* add to AR "μ factorises as uniform x₀ ⊗ uniform h,
  and the observer, clock and output registers start deterministic".

## 4. K_cx

- The plan defines K_cx(φ) = ⌊ℓ_med(φ)/2⌋, with ℓ_med the μ-median orbit length.
- My orbit enumeration at the first review (`revpe01/checks.out`) gives:
  - G_lin and G_filt: ℓ_med = 7, 15, 31, 63, 127, 255, so K_cx = 3, 7, 15, 31, 63, 127;
  - G_clk: ℓ_med = 10, 19, 40, 85, 169, 337, so K_cx = 5, 9, 20, 42, 84, 168.
- These agree with the author's values. In every orbit census the lower and upper medians coincide, so the median is
  unambiguous.
- In the tables, the clock bound binds before K_cx in every non-empty cell. For example, at n = 8, m = 1, θ = n+1 the
  G_clk cell ends at 127, below its K_cx of 168.

## 5. The passive m = 3 sweep, and other owner decisions

- **The plan's text is accurate.** "The passive m = 3 sweep (n ≤ 6) can yield no admissible witness at either θ" is
  right:
  - at θ = n, m = 3 is non-empty only at n = 8;
  - at θ = n+1, m = 3 is non-empty only from n = 7.
- The linear-filter m = 4 claim is also right: admissible only at n = 8 with θ = n+1.
- **N3 (nit):** the n range of the linear-filter sweep is not stated (:78, :193). The claim assumes it includes n = 8.
  *Fix:* state "n = 3..8".
- **N5 (owner decision, to list in §10).** As planned, the passive m = 3 sweep is comparison-only. The owner should
  choose one of two options:
  - **(i)** Keep it at n ≤ 6, as unrestricted-footprint comparison data only.
  - **(ii)** Extend it to n = 7, 8, capped at the top of the admissible region for the chosen θ:
    - θ = n: n = 8, K ≤ 15;
    - θ = n+1: n = 7, K ≤ 15, and n = 8, K ≤ 31.

    With the cap the cost is moderate. A K cap of 31 instead of K_max = 1020 cuts the per-observer simulation by about
    30×. It needs its own §8 row.

  *Recommendation:* (ii) if θ = n+1, since that is the only way an m = 3 passive observer can bear on (f). Under
  θ = n, (i) loses only n = 8. The owner decides.
- **Other owner decisions.** I found none beyond θ, K_LP and the m = 3 sweep scope. Two related points can be decided
  by the author:
  - **The attribution granularity (N4).**
  - **The linear-filter n range (N3).** If the owner prefers to restrict it, the same capping applies.

## 6. New defects

- **N4 (nit): the attribution rule needs a stated granularity (:332).** "Some witness meets (a)–(e) but fails (f)" is
  read globally. Then a single large-footprint witness on one (φ, n) would attribute unpredictability to resources
  everywhere. *Fix:* apply the rule per (generator, n, observer subclass), and report each cell's attribution.
- **Wording:** :437 is headed "Consequences, the same for all three generators", but its second bullet is specific to
  G_filt and G_clk. Fold this into N4's edit, or reword it as "Consequences".
- **Checked and found sound:**
  - Vacuous or prejudging controls: none found. AR halts the stage on any difference with the drafting tables, which
    is a control on the plan text and not on an outcome.
  - Invariants without a checkpoint: none beyond N2.
  - Claims stronger than their evidence: none found.
  - :410–411 states correctly what a region cell does and does not mean.

## Summary

| # | Item | Class |
|---|---|---|
| — | Window floor, tables, AR, recomputed region | resolved |
| — | Attribution rule, Purpose pointer | resolved |
| — | CX flags, VG sentence, TH gating, §10 restated | applied |
| N1 | Clock starts at 0 | nit |
| N2 | AR checks that the prior is a product | nit |
| N3 | State n = 3..8 for the linear-filter sweep | nit |
| N4 | Attribution per (generator, n, subclass); the :437 heading | nit |
| N5 | List the passive m = 3 sweep scope as an owner decision in §10 | nit (owner decision) |

***

## Addendum: confirmation of 1cbfba61 (parent fee98794, PLAN.md only, +27/−12)

PLAN.md at `1cbfba61` has blob `ce12a5f1` and sha256
`0163b21c0bf4152a81519ef90d7358ea9899a5c92ca6ed26f3eed468cddb81b4`. I recomputed it from `git show`, and it matches. Only
the `fee98794..1cbfba61` diff was read.

### Verdict: ACCEPT WITH NITS

The diff applies every nit as specified and changes nothing else of substance. One stale sentence remains, and is a nit.

| Nit | Applied as specified? |
|---|---|
| N1 clock starts at 0 | yes: "starts at 0, ticks as a cyclic permutation" (§3) |
| N2 AR checks the product prior | yes. AR checks that μ factorises with h uniform and independent of x₀, and that the memory, clock and output registers start at fixed values. |
| N3 linear-filter n range | yes, n = 3..8, in the §1 range table and the §3 subclass list |
| N4 attribution granularity; :437 heading | yes. The rule is applied per (generator, n, observer subclass) and never pooled. The heading now reads "Consequences:". |
| N5 m = 3 scope as an owner decision | yes. §10 lists options (i) and (ii). TH records the decision. Runs are gated on θ, K_LP and the m = 3 scope, in §6, §10 and TH. A new §8 row covers option (ii). |

**Option (ii) caps against my tables.** They match:
- **θ = n:** m = 3 is non-empty only at n = 8, where the top is 15 for all three generators. The cap is K ≤ 15 at n = 8.
- **θ = n+1:** m = 3 is non-empty at n = 7 (top 15) and n = 8 (top 31). The caps are K ≤ 15 and K ≤ 31.
- Option (i)'s statement, "no admissible region exists there under either θ", is correct for m = 3 at n ≤ 6.
- §10 states neutrally that (ii) is the only way an m = 3 observer can bear on condition (f), and that the plan does not
  make the decision. My recommendation, (ii) if θ = n+1, was conditional. It is not restated, which is acceptable,
  because the owner decides.

**Nothing else of substance changed.** The rest of the diff is wording only:
- the rewrapped §6.4 sentence;
- the attribution bullets.

**N6 (nit): stale count of open decisions.** §6 item 4 still says "The threshold θ is the one open owner decision
(§10)". After this diff, §10 has two open decisions, θ and the m = 3 scope, and K_LP awaits confirmation.
*Fix:* "θ and the m = 3 scope are the open owner decisions (§10); K_LP awaits confirmation".

The remaining cosmetic items need no re-review:
- the §6.4 rewrap leaves one line over the wrap width;
- the attribution bullet's last line is a lazy continuation.
