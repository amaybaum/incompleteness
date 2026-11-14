# REVIEW-OICORE-1-r6: confirmation check of OICORE-1 r6

- **Reviewed file.** `OICORE-1.md` (r6), sha256 `ec7966c955a17043c85f85be3f2bbe178049ed3a0f4286e0b61e3bd1c4aa078b`
  (re-hashed). It was diffed in full against `OICORE-1-r5.md` (`9c273525…`, re-hashed).
- **Scope.** Paper-only and read-only at `2cd49dc0`. No Lean was run, nothing was computed, and no repository or GitHub writes were made.

## Verdict: **ACCEPT**

There is one optional labelling nit (R6-n1). It does not affect any count, verdict or classification.

## Checks

**1. Only R5-n1 and R5-n2 are applied.** Confirmed. The diff has exactly these hunks:

| Hunk | Content |
|---|---|
| title | r6 |
| revisions table | ll. 20-21 |
| l. 259 | the CERT cell in §3.2 |
| ll. 385-387 | §5(f) |
| l. 541 | the CERT cell in §8.6 |
| ll. 598-599 | §8.7(e) row 2 split into two rows |
| ll. 603-612 | the §8.7(e) headline, including "these five rows" at l. 612 |
| ll. 621-622 | the gap-table rows |
| ll. 644-645 | §8.8 |
| ll. 678-680, 683-686 | §8.10 |
| §9.4 | dispositions |

No other line changed.

- **R5-n1 is applied in substance.** Both CERT cells now read "excluded within NC's scope, **conditionally** on W". The wording matches the
  RET-s and U2 cells. A grep finds no bare "CX" left on a W-layer result. The only remaining CX outside class confinement is l. 543's
  "within finite bijective read-write dynamics", which is a kernel class-confinement result and correct.
- **R5-n2 is applied in substance.** §8.7(e) row 2 is now two rows:
  - the infinite world / open supplies route: a shift;
  - a separate row, labelled "*not an ε-route*", for a non-linear identification in one fixed finite world.

**2. The count of three shifts and two open cases is supported by the body.** The §8.7(e) table has exactly five rows (ll. 597-601):

| Row | Verdict | Level |
|---|---|---|
| growing systems / ε-indexed rules | shift | ε |
| infinite world / open supplies | shift | exact infinite-order gate |
| non-linear identification in a finite world | open | dense |
| free ε | shift | ε |
| horizon-limited finite-order gate | open | ε |

That is three shifts and two open cases.

- The non-linear identification case is correctly a dense case and not an ε-route. Its target is an *exact infinite-order* gate, which feeds
  the existing dense theorem. Its openness traces to §8.7(c) row 5 ("non-linear identifications … **open**"). The spectral exclusion in row 2
  needs a linear identification.
- A "two shift" count is not supported. All three shift rows assume something outside OI:
  - more than one `φ` or a growing `S`;
  - an infinite world, against total finiteness;
  - a tunable ε that fails §A.29.
- The count is repeated consistently in four places: the headline (ll. 605-610), the gap table (ll. 613-622), §8.8 (ll. 644-645) and §8.10
  (ll. 683-686).

**3. No new overstatement.**

- Each open case is "not excluded; not a candidate mechanism" at every site.
- ENC-G-2 remains "an open conjecture, typed as a new hypothesis".
- The new §5(f) sentence (ll. 385-387) names the two cases "within" the owner's question. That is accurate: dense control yields
  approximately quantum operations (`DenseFiniteQM` is a density statement). The sentence asserts neither feasibility nor a mechanism.
- The headline is neutral: "Over the five rows above, the approximate-versus-exact distinction does not show any route to be OI-native"
  (l. 603).
- The finite-coverage caveat remains: "It is not shown that every route falls into one of these five rows" (l. 612).
- A grep finds none of "consistent with OI", "nothing beyond OI's axioms" or "exposes" in the audit's own voice.

## Nit (optional)

**R6-n1. Two labels are inconsistent at the table and §8.10 level.**

- The table's column header still reads "ε-route" (l. 595).
- §8.10 (l. 683) says "Three ε-routes shift".
- But the infinite-world / open-supplies row also targets an *exact infinite-order* gate. Like the non-linear row, it is a dense case, not an
  ε-route.
- *Fix.* Rename the header "Route", and change "Three ε-routes" to "Three routes". The headline at l. 605 already says "Three routes".
- The count, the verdicts and the classifications are unaffected.
