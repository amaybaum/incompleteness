# REVIEW-OICORE-1-r5: independent re-review of OICORE-1 r5

- **Reviewed file.** `OICORE-1.md` (r5), sha256 `9c273525600aef5cbf40fa8a110080750cd18e1f2629cabb95bc6ce781d3738a`.
  I re-hashed it before the review. It has 745 lines.
- **Method.** r5 was diffed in full against `OICORE-1-r4.md` (`e090309c…`, re-hashed). The diff covers 20 hunks, plus the new §9.3. I also
  grepped the whole file for the R4 phrases: "consistent with OI", "exposes", "nothing beyond OI's axioms", "candidate mechanism", and
  every remaining bare `CX`.
- **Scope.** Paper-only and read-only at `2cd49dc0`. No Lean was run and nothing was computed. No repository or GitHub writes were made.

## Verdict: **ACCEPT-WITH-NITS**

R4-1 to R4-6 are fixed in substance, and the edits introduce no new overstatement. The §5 and §8 summaries match the body. The two
remaining nits are consistency items. Neither changes a conclusion.

## R4 findings: status

| Item | Status | Evidence (r5 lines) |
|---|---|---|
| R4-1 | **fixed** | The legend adds **CX†**: "excluded *if* the candidate is consistent with the core; that consistency is open, so the exclusion may be vacuous" (l. 84). ACC_op is CX† in §3.2 (l. 252) and §8.6 (l. 534). The §3.2 RET-s cell now reads "excluded within those scopes, **conditionally**" (l. 256). §5(b) keeps ACC_op out of the "proved unable" bullet (ll. 332-334) |
| R4-2 | **fixed** | No occurrence of "consistent with OI", "nothing beyond OI's axioms" or "exposes" remains in the audit's own voice. The only "exposes" left are the owner's verbatim question (l. 39) and MI-R's "`G_σ` exposes" (l. 253). The horizon-limited route now reads "not excluded by any result found; open conjecture (ENC-G-2); not a candidate mechanism" at ll. 597, 603, 613, 634 and 673-675. The §8.7(e) headline (l. 599) is now "does not show any ε-route to be OI-native" |
| R4-3 | **fixed** | §8.7(e) row 2 (l. 595) and §8.8 (ll. 635-637) state the exclusion of an exact infinite-order gate as conditional on §8.7(c) row 2's hypotheses, with non-linear identifications open (row 5). An infinite world or open supplies is typed as a new hypothesis against total finiteness |
| R4-4 | **fixed** | §8.4 (l. 513) moves the horizon-limited route to a separate ε clause: "not excluded … needs OICORE-F6; open conjecture" |
| R4-5 | **fixed** | §7 (l. 411) lists all eight Theorem C use sites. The §3.2 ACC-U cell (l. 254) uses §5(c)'s draft-conditional wording |
| R4-6 | **fixed** | §5(d) (l. 360) names `FiniteOperationalTheory (Fin 2)` |

## Summaries against the body

All of the following agree:

- **§5(b)** (ll. 330-346):
  - FIX_op and FIN_op are proved unable;
  - ACC_op's exclusion is definitional and may be vacuous;
  - Lemma M is stated on `Fin 2`;
  - dense control is excluded for FIX_op, carrier-labelled, and not shown for ACC_op;
  - CTRL is the stated exception.
- **§5(c)** is draft-conditional for F0.
- **§5(d)** carries the `Fin 2` scope.
- **§5(f)** keeps the r4 neutral locating list.
- **§8.4** separates the dense and ε levels.
- **§8.6** uses CX† and NI-W.
- **§8.7(e)** and its gap table, **§8.8** and **§8.10** describe the horizon-limited route the same way.
- **§9.3** dispositions match the diff.

## Nits

**R5-n1. The CERT cells still carry a bare CX label on a W-layer result.**

- The CERT cells are §3.2, l. 258 ("**CX** within Theorem NC's hypotheses … [W]"), and §8.6, l. 538 ("CX in scope (both)").
- The RET-s cell got the R4-1 fix, but CERT did not. Both cells rest on M2D Theorem NC, a W record. Under §A.46 item 7 they should read
  "excluded within NC's scope, **conditionally** on W", as RET-s and the U2 row (l. 568) do.
- I listed CERT among the legitimate CX results in R3-B2. That conflicted with my own R3-B4 point that W records cannot ground "proved
  unable", and this nit corrects it.

**R5-n2. §8.7(e)'s route count is ambiguous after the R4-3 fix.**

- Row 2's verdict is now split (l. 595): "shift" via an infinite world or open supplies, and "open" via a non-linear identification in a
  finite world.
- The headline (ll. 601-603) still says "three routes shift".
- *Fix.* Either rename row 2 "infinite world / open supplies" so the count stays exact, or say: "three routes shift; a non-linear
  identification in a finite world is a separate, open dense (not ε) case, covered by §8.7(c) row 5".

Neither nit affects a verdict, a classification boundary or a summary.
