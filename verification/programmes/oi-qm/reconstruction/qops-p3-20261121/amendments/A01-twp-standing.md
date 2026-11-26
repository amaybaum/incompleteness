# A01: amendment to `PREREG.md` (T-WP's standing, and its sanity checks)

**Standing. Plan only. Nothing has been run.** This amendment is append-only; `PREREG.md` is
unchanged. Where they differ, this file governs, for every item it names. It answers the review of
`826cb00d` ([#1518 c.7066768898](https://github.com/amaybaum/incompleteness/pull/1518#issuecomment-7066768898),
R4 and n2).

1. **T-WP is a paper protocol, not a decisive computation.** This replaces the "Standing" and
   "What an outcome would mean" sections of `PREREG.md` wherever they imply that a run decides
   anything.
   - FF's values are derived in `NOTE.md` §3.2.
   - Each readout arm becomes a finite hand calculation once the amendment that instantiates `R`
     fixes its instrument form.
   - Running T-WP would therefore replay hand calculations under either R-READ answer. The
     hypotheses that matter (FLOW₁ executable; `R` native and of a given form) are inputs, not
     outputs.
   - The unit's productivity is **NON-GEM as a computation** (`PLAN.md`, criterion (ii)) on both
     branches. The previous text, "INCONCLUSIVE pending READOUT-ALG", is withdrawn.
2. **What T-WP still defines.**
   - The operational witness: the classification WP-NC / WP-C / WP-X / WP-D against CC-Δ and
     CC-M.
   - The RES count of the protocol.
   - The geometry and the native copy (Lemma P6, with at least one catalyst and one sufficing).

   If a later unit names a native instrument of unknown classification at level 2 (`NOTE.md`
   §2.3), T-WP is the protocol that classifies it operationally. That would be a hand calculation,
   or a computation preregistered in that unit.
3. **Sanity checks, not controls (n2).** K4 (discarding `r` leaves `W` unchanged) and K5 (CC-Δ has
   no gap) cannot fail by construction. They are reclassified as sanity checks. K1, K2, K3, K6 and
   K7 remain controls.
4. **No run is planned.** Executing T-WP needs separate owner authorization. Under item 1 it is not
   proposed.
