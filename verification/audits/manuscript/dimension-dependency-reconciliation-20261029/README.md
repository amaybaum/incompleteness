# Dimension/dependency source reconciliation

Guiding PR: #997. Review requirements: [comment6497986035](https://github.com/amaybaum/incompleteness/pull/997#issuecomment-6497986035). Parent source: `9e2673820ae0c02d6c8ab7e10cf9470753d00ad8`; main baseline: `ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf`.

## Source dispositions

1. Complexity §2.8: all five starting `derived` arrows become conditional (including the independent-gauge-groups arrow omitted from the review's four-site list). The abstract carries A4, E5–E7, continuum and carrier/matter hypotheses; the first chemical conclusions and closing whole-chain summaries retain their downstream assumptions. CP-phase availability is separated from its actual value, and Higgs-field availability from actual mass hierarchy.
2. Explainer's physics-to-life summary carries A4/E5–E7/continuum, spin/statistics/atomic/matter assumptions and H-link/H-spin′/H-χ′. Chemical/biological model claims are not certified by finite-law representation alone.
3. Chapter11's combinatorial-productivity statement is conditional on the selected branch, carbon's electronic/bonding structure and the autocatalytic model's realization assumptions. Its dimension-selection reference is Chapter5§5.3. Chapter10's observer-supporting theorem conclusion is removed. Both edits are mirrored in FULL.
4. The three-logically-independent-filters claim is corrected at SM Tier1 and Tier2 summaries, Substratum E5/Stage2(a), GR's boundary-filter summary, chapters2/5, bookREADME and FULL. Propagating gravity plus stable matter already select3 in A4's assumed integer-lattice/continuum branch; concordance, with its horizon assumptions, is redundant for the selection once those two hold but not logically dependent on them, since it independently excludes $d\geq4$ (SM§3.2). Independent-literature and alternative-filter arguments retain their actual scope.
5. The continuum reference at SM§4.10 is §3.1–§3.2. The prior scope correction is retained; no unrelated background-independence sentence is restored.

## AF-1: SU(2) counterexample and source-correction assignment

Assigned to #997 for the direct false Tier3 claim, with downstream selector reasoning retained under #996/#946 (and #963's non-Bell selector/chirality/Higgs reconciliation). SM's own stated coefficient b2=-19/6 in §6.2 is an SU(2) asymptotic-freedom counterexample to the claimed necessity Nc≥3. Tier3 now explicitly separates this matter-dependent beta-function fact from color-group selection and dimensionless coupling. A targeted corpus search located the direct Nc≥3 necessity assertion only in this Tier3 sentence; this does not certify every downstream gauge-selection argument. No independent gauge-group selection from asymptotic freedom is claimed.

## Remaining audit boundary

This revision does not certify the existing quantitative viable-fraction measure or complete biological extensions. Specific remaining source questions stay assigned to the whole-framework audit #944 and source gate #946: the chosen weighting/ranges and independence assumptions in Complexity§3, chemistry/observer inevitability in chapters10–13, the template/evolution claim at chapter11:130, and the biological inevitability clause at chapter13:8. The selected-branch scope corrections above are not acceptance of those chains. #918 remains unchanged and held. No original correction unit is closed.

## Validation status

Current build, check and review results are recorded in the correction-round section below and in the PR checkpoint. Mathematical theorem bodies, Lean sources, proof grades and workflows are not modified. Final independent scientific/editorial review, fresh candidate CI, and separate owner exact-SHA approval remain required. No merge, release, special dispatch or native designation is authorized.

## Minimum-change cleanup (2026-10-29)

Restored the eleven pre-existing Markdown horizontal-rule spellings in `papers/Complexity.md` (`***` back to `---`), with no scientific prose or derivation changes. This cleanup neither promotes the science grade nor closes #946.

## Forward integration after #1000

Source reconcile candidate incorporates #997's exact correction hunks against main merge `6e219231483bb404c0d055ab9a447278422a597e` (which includes #998/#999/#1000), together with the existing, independently reviewed #997 source corrections. The branch carries both parent histories. The integration commit `bd8fa74d` did not preserve main's content exactly: it changed 15 display-math lines from `$$…$$` to `$…$` (Complexity 11, ch05 1, ch10 1, FULL 2). The correction round below restores them. The Introduction #918 remains on hold. No merge or scientific-grade promotion is authorized by this checkpoint.

## Canonical publication regeneration after #1000

The affected paper and book TeX/PDF were generated from this post-#1000 source on the canonical repository `build.sh` workflow in [GitHub Actions run 40971794313](https://github.com/amaybaum/incompleteness/actions/runs/40971794313), artifact commit `dae6883cdefb2999368d5353a07e9445d5918e24`. The temporary build workflow was removed in that same commit. `staleness_check: OK (13 matched, 0 unstamped)`; no missing-character warnings; `mirror_check: 0 chapter line(s) absent from FULL.md`. Page/text-density QA: Complexity 35/2758 median chars, SM 150/3170, GR 88/3208.5, Substratum 54/3239.5, Explainer 71/2921, book 557/3052. These QA results do not replace independent rendered-page inspection or scientific/editorial review. The SC-42 successor produces 494 PASS predicates after this integration, 23 more exact chapter/FULL mirrors than the 471 on #1000. Old SC-42 records and negative controls are preserved; the retained source JSON is replayed at this head. Fresh ordinary CI including the release gate and independent exact-head review are still required; #997 remains draft and #918 held.

## Correction round (2026-10-30)

Owner-bounded correction of the independent final-head review of `613632e4`, from that head. Each manuscript edit maps to one finding; book edits are mirrored in FULL.

| Finding | Change |
|---|---|
| Blocker: 15 display-math lines collapsed by `bd8fa74d` | Complexity:45, :95–109 (odd lines), :329–330, ch05:60, ch10:69, FULL:1387 and :2887 restored to `$$…$$`, byte-identical to the reviewed pre-integration head `a6d7f417`. Display-line counts equal main (Complexity 22, ch05 12, ch10 3, FULL 135). |
| Complexity contradicts §3.4 (:154) | :121 holds the structure fixed on the selected branch (§3.4) instead of "the framework fixes the structure"; :198 removes structural variation on the selected branch and states that embedded observation alone does not exclude it; :204 scopes the removed ensemble to the stated inputs and drops "nothing that could have been otherwise"; §6.4 arrows at :323 and :324 read "conditional". Same scope at :27 ("under the hypotheses stated there"), :212 and :270 ("selected" for "derived" structure). |
| E7 logical status | SM Tier1 (:30), SM §3.2 (:178) and GR (:446): concordance is redundant for the selection once E5 and E6 hold, but not logically dependent on them, since it independently excludes $d\geq4$ (SM:180). |
| Propagation | Computation:13 and ch00:21 (+FULL): "forced consequence of a cubic-lattice commitment" becomes conditional, with E5–E7 within A4's class on the continuum branch. "Derived structure" becomes "selected structure" at Computation:39/:41/:47/:92 and ch12:22/:162 (+FULL). |
| Voice | Complexity:332 "one of the contingent steps"; Complexity:340 "open hypotheses", self-assessment sentence removed; Explainer:806 bridges are open hypotheses and parameter values empirical inputs. |
| Citations | Complexity:47, :93 and SM:1257 cite §3.1–§3.2. |
| Deletions | Explainer:880 restores, in conditional form, Complexity's $\sim10^{56}$ autocatalytic estimate and C1–C4 origin-of-life identification. SM Tier1's deleted sentence is not restored: it called the defining object a theorem; its self-consistency status is kept in the retained sentence citing §3.2 and §8.3; and its clause that the selection does not depend on the specific dynamics omits the continuum conditions of §3.1–§3.2, which constrain the dynamics. |
| Stale audit notes | This README's validation, cleanup and forward-integration notes; SC-42 README predicate count and provenance. |
| Final-acceptance review of `baf13720` | Explainer:806 states that most Standard Model parameter values are properties of the specific bijection φ (consistent with :858/:862); Explainer:974, Complexity:200, ch10:190 and preface:7 (+FULL) carry the same branch scope as the corrections above; Complexity:204 keeps one qualifier; ch00:21 names the dimensional filters of Chapter 5 instead of labels defined later; Computation:39 keeps "derived periodic table", as at :27 and :53. |

Rebuilt with `sh ./build.sh Complexity SM GR Computation Explainer` and `sh ./build.sh --book`, then, after the final-acceptance fixes, `sh ./build.sh Complexity Computation Explainer` and `sh ./build.sh --book`: Complexity 35, SM 150, GR 88, Computation 22, Explainer 71 and book 558 pages (the book's 557 at `613632e4` came from the collapsed displays), no dropped glyphs, `staleness_check: OK (13 matched)`. Rendered Complexity pp. 6 and 18 and book p. 258 show the restored displays as display math; the ch10 chain at book p. 258 runs as close to the right margin as on main. SC-42: 498 predicates pass (338 non-mirror, identical to `613632e4`, and 160 chapter/FULL mirror predicates, which now record the restored `$$` lines), and the controls and optimized run are unchanged.

**Left to #944/#946 (not changed here):** Complexity §5 and §6.4 biological claims (:15 RNA "structural prediction", :327 "inevitable" Darwinian evolution, §5.3–§5.6 inevitability), the §3 viable-fraction weighting, chapters 10–13 chemistry/observer inevitability (ch10:10/:16/:134, ch11:130, ch13:8).

## Formatting-safety closure (2026-10-30; #997)

Authorized minimum-change correction: commit `2901421b9b9f56f03cb68c6492e7e8d28e4490d9` replaces exactly 11 standalone `---` horizontal-rule delimiters with `***` in `papers/Complexity.md` to comply with AGENTS.md's Pandoc safety rule. All 22 display-math lines (44 `$$` delimiters) and all scientific prose are unchanged. GitHub Actions [run 41002473848](https://github.com/amaybaum/incompleteness/actions/runs/41002473848) canonically rebuilt **only** `papers/Complexity.tex` and `.pdf`, committed at `4124b3bf9fab23d070d619abb394e0c16f496594`, and deleted its temporary workflow within the same commit. Post-build checks passed: Complexity 35 pages, median 2,791 visible characters per page, no dropped glyphs, `staleness_check: OK (13 matched, 0 unstamped)`, and `mirror_check: 0 chapter line(s) absent from FULL.md`. Rendered pp. 6 and 18 retain centered display equations and show no clipping in the inspected samples. The PR's effective diff contains no temporary workflow. The prior independent scientific/editorial reviewer accepted source head `7bd7a353`; optional nits were applied by `d07f6e65`. This formatting-only delta requires independent exact-head confirmation and fresh ordinary green CI before merge. The Introduction #918 remains held.
