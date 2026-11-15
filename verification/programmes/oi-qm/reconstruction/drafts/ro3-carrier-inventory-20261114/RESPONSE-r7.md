# RO-3: response to the focused review of inventory r7

**UNREVIEWED.** This file gives the writer's disposition of each item of the focused review of r7
(delivered as `REVIEW-1303-INVENTORY-r7.md`, REVISE, the map not yet complete, no label refuted;
SHA-256 `8e153d8d66bd9743797ec7cc61f081fda9fb4e032e9cd23a97be1c77ad0b1402`). r7 is left unchanged.
The changes are in `RO3-INVENTORY-r8.md`. Everything was checked at `main`
`7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac` by reading only, with `git show` and `git grep`, and the
census. Nothing was built or computed, and no repository, Issue or PR was written.

Section numbers below refer to r8.

## M1. The phrase family "finite deterministic"

**Disposition: accepted, extended.** §7.0 adds step 3b over `papers/*.md` and `book/*.md`. It
combines the review's patterns with "finite configuration (space|set)", "finite (energy )?shell",
"finite total", "finite set $S$" and "finite universe". Over `papers/` it gives 85 lines, 59 of them
not cited in r7. Each was read in context.

**The review's items.**
- **GR:613 (AM-36), recorded as a finding.**
  - (U1)–(U3) were traced through GR:613–669.
  - The claim's hypothesis names "any finite deterministic substratum" (GR:613).
  - GR:669 says S1–S4 suffice and are weaker than A1. But S4 is the §3.2 Stinespring structure
    (GR:667), and that is under A1 as Main states it (Main:266).
  - (U1)'s identification rests on GR:58's finite counting under H-count.
  - The A1-freedom of (U1)–(U3) is therefore not established at source. r7's §7.2 entry is
    withdrawn.
- **GR:70 and GR:28: added to AM-22.** GR:28 also frames AM-36.
- **SM:1225–1227: added to AM-4,** with SM:292.
- **SM:1388: added to AM-31.**
- **Complexity:374: added to AM-20**, as a mirror and as a propagation finding.
  - r8 paraphrases its first clause and quotes its parenthetical.
- **The framing lines: added to AM-10**, and listed in §7.5.
  - Main:710; GR:20, :705; SM:1592.
  - Sub:14, :16, :22, :367, :429, :465.
  - Struct:21, :45, :108, :377, :528, :741; Meth:517.
  - Introduction:36; Complexity:21, :27; Computation:21, :180.
  - Also Main:14, :706, SM:250 and Meth:337.
  - The review's Introduction:53 is class D, constructed (§7.2). Its Introduction:129 is a mirror of
    AM-27.
- **Eventual-image mirrors.** Sub:94 is added to AM-3, and GR:861 to AM-33.
- **Main:578: in §7.2.** Juno:261 is recorded there as a false hit.

**Found beyond the review's list.** The second group was not on the review's list.
- **Mirrors and extensions of existing rows.**
  - GR:224 and Introduction:129: AM-27.
  - GR:605 and the Appendix A setup GR:709–715: AM-33.
  - SM:90 ("assumes only finite configuration sets"): AM-1.
  - SM:292: AM-4.
  - Complexity:212: AM-8.
  - Meth:146: AM-3.
- **A new consumer.** Struct:1255 (AM-37): the visible factor of a finite deterministic bijection has
  zero asymptotic entropy rate. [IR]: on an infinite carrier with a normalized measure, the rate can
  be positive.
- **In §7.2, not consumers.**
  - Constructed finite carriers: Main:214, :433, :480, :524, :552, :578; GR:278; Introduction:53;
    Sub:533; Struct:1273.
  - A classification: Struct:339.
  - False hits on "definite": Meth:397, :401, and appendix-c:230 (FULL:6460).

**The "finite deterministic" sites (§7.5).** Every site in `papers/` and `book/` is listed with its
line:
- `papers/`: 26 lines;
- book chapters: 30 lines;
- FULL: 29 lines.

§7.5 also records a framing finding for the owner under #1169 comment 6893456888. These sites state
results for a "finite deterministic system/universe/substratum". For the law-level equivalence that
narrows a statement Main:60 makes for every finite-horizon law. For the physical reading it states A1
as the setting. No manuscript is edited.

## M2. The nine modules flagged by the discriminator

**Disposition: accepted.**
- **Checked.** The discriminator `Equiv\.Perm S|orderOf|φ\^\[|vis ` over the 42 hits exactly the nine
  the review names. Each was read: its header, its `variable` lines and its declarations.
- **Census 3, now AM-38.** These work on a finite microstate set with a permutation and a visible
  map, so they are statements on finite realizations. The census note says they underwrite no
  manuscript statement. Their placement is the one the review gives: about the substratum only
  through A1.
  - `ObservabilityQuotient`: `itiRelK` at :79, `itiRelInf_iff_orderOf` at :304.
  - `DomainGlue`: :75.
  - `ControlledQuotient`: :51; each menu action has finite order.
  - `CoherentExtension`: :251. It is a finite-dimensional CPTP-extension classification on the
    carrier the controlled quotient determines.
- **Census 4 and 5, in §7.2.** `MonoidalCompletion` and `BranchSelector` (census 4), and
  `LieRankSource`, `SpectatorBridge` and `DiagonalTheory` (census 5). Each uses `Equiv.Perm S` as a
  relabelling or primitive intervention on a finite operational carrier. None states a property of a
  substratum's microstate dynamics.
- **The other 33.** §7.4 names them and states them as unread, a scope limit only. They are not
  classified.

## M3. `verification/lean/`

**Disposition: accepted.**
- **Checked.** The six `.lean` files under `verification/lean/` give no hits for
  `Fintype|Finite |orderOf|recurren`.
- **Applied.** §7.0 states this, so the Lean step covers all of `verification/lean*`.

## Completeness

**Disposition: not claimed.**
- **The review's condition.** M1–M3 applied, and no new hit found.
- **What happened.** M1–M3 are applied, but the extended recipe found hits beyond the review's
  list. Each is placed, but the condition is not met as stated.
- **What r8 says.** The Standing, §7.0, §7.1 and §7.4 no longer say "complete". §7.4 leaves to the
  next review whether the map meets the owner's condition.
- **Remaining limit.** The 33 unread modules.

## Not changed

- **Status.** No cell's status changes, no result is withdrawn and no premise is adopted.
- **AM-3.** It stays proposed, not chosen.
- **The findings.** GR:613, Complexity:374 and the framing list are recorded, not settled.
