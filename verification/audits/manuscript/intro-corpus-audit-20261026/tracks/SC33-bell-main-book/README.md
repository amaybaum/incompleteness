# SC-33: Bell placement in Main and the book (#942 / #946)

Base: `main` at `0d917665`. This unit carries the Main and book part of the SC-17 claim class; SC-17 corrects the Explainer.
Each site is restated at the strength of its anchor, and no claim is strengthened. The anchor is Main §3.3, Theorem (Bell
ceiling for a screened local completion). Its hypotheses are (i) determinism, (ii) own-wing read/write setting interventions
applied at one step, (iii) a ±1 readout region outside the other wing's cone, and (iv) one common pre-setting ensemble. It
applies when the protocol records a ±1 outcome in every run. The either/or follows the theorem: a completion reproducing
quantum Bell correlations gives up (ii) and (iii), which with the cone lemma secure ontic parameter independence, or (iv),
measurement independence. The framework gives up the first, so the adopted branch is ontic parameter dependence. H-Bell is the
open compatibility condition on preparation-indexed adjacency: operational no-signaling and the continuum-curvature
(Ollivier–Ricci) limit (§3.3, Corollary).

A deterministic completion satisfies ontic outcome independence automatically, since each outcome is a point mass given the
pre-setting variable and the settings. Outcome dependence is therefore not available as OI's Bell route.

Where a site assumes ontic parameter independence directly, (ii) and (iii) are already inside that assumption, and only the
±1-every-run hypothesis is added. Where it states the ceiling from graph separation, the own-wing intervention hypothesis is
added as well, applied at one step. On a finite vertex set "finite-range" is not a separation hypothesis, so (iii) is
stated as each wing's readout lying outside the other wing's graph cone, or as couplings that do not connect the wings before
readout.

| Site | Was | Anchor | Now |
|---|---|---|---|
| Main :700 | 't Hooft comparison: "Bell placement (outcome independence violation vs. superdeterminism)" | §3.3 either/or; theorem proof (determinism makes the conditionals point masses) | "Bell placement (ontic parameter dependence with measurement independence retained vs. superdeterminism)" |
| Main :766 | ceiling from "genuine local interventions" and pointwise separation, no ±1; "Reproducing quantum correlations therefore requires ontic parameter dependence, which … the specific SM/GR target implements through preparation-indexed state-dependent adjacency" | §3.3 (i)–(iv), ±1 in every run, either/or; Corollary (H-Bell open) | Ceiling states one-step own-wing interventions and a ±1 outcome in every run read outside the other wing's cone. Reproduction requires giving up ontic parameter independence or measurement independence, and §3.3 gives up the first. Preparation-indexed adjacency is the proposed SM/GR implementation, and its compatibility with no-signaling and the continuum-curvature limit is the open hypothesis H-Bell. |
| Main :558 | "is now separate rather than analogous"; "with that pointwise cone is Bell-local"; "should not be turned into a new 'selection' paper"; "is settled as a characterization" | §A.32/§A.33; §3.3 (ii), (iii), ±1 | "is a separate question rather than an analogous one"; one-step own-wing interventions, readouts outside the other wing's cone and ±1 in every run; the 'selection' clause is deleted; "is a characterization". The adopted-branch "therefore requires ontic parameter dependence" is kept. |
| Main :22 | "keeps the pointwise cone and a setting-independent pre-setting ensemble"; parameter dependence "realized in the specific SM/GR branch" | §3.3 (ii)–(iv), ±1; Corollary | Setting interventions applied at one step, each reading and writing only their own wing; readouts outside the other wing's cone recording ±1 in every run. "realized" becomes "targeted"; the abstract's later sentence names H-Bell as open. |
| Main :82 (Theorem statement, canonical) | "measurement independence plus ontic parameter independence would force $\|S\|\le2$" | §3.3 theorem ("If the protocol records a ±1 outcome in every run") | Adds "that records a ±1 outcome in every run". Ledger `MAIN:T-statement` re-affirmed: fingerprint 70572f0b3e1aa833 → 2748dd752bdd9f03, level SUM and empty delta unchanged (it summarizes the constituent rows), same ID. |
| Main :646 | "that pointwise cone is kept at the wings' separation and the pre-setting ensemble is measurement-independent" | §3.3 (ii), (iii), ±1 | Interventions applied at one step, each wing's readout outside the other wing's graph cone, ±1 in every run. |
| ch00 :41 (+FULL :277) | "a measurement-independent response-complete completion with finite-range Bell couplings is classical, so quantum violation requires ontic parameter dependence" | §3.3; either/or | One-step own-wing interventions, couplings that do not connect the wings before readout, ±1 in every run; "is Bell-local, so quantum violation under measurement independence requires ontic parameter dependence". |
| ch00 :55 (+FULL :291) | ceiling from graph-cone separation and a setting-independent ensemble; "realized in the SM/GR target"; "What is not yet claimed" | §3.3; Corollary; §A.30 | One-step own-region interventions and ±1 in every run. The SM/GR target proposes preparation-indexed structure, and whether it keeps no-signaling and the continuum-curvature limit is the open hypothesis H-Bell. "What is not claimed". |
| ch01 :16 (+FULL :360) | "a pointwise finite-range cone together with local interventions and one setting-independent pre-setting ensemble is Bell-local" | §3.3 (iii): on a finite vertex set "finite-range" is no separation hypothesis | One-step own-wing interventions, readouts outside the other wing's graph cone, ±1 in every run and one setting-independent ensemble "give a Bell-local model". |
| ch01 :169 (+FULL :513) | the book's own statement of the ceiling: coupling-range separation plus a setting-independent ensemble | §3.3 | Adds one-step own-wing interventions and ±1 at each wing in every run. |
| ch01 :171 (+FULL :515) | "The averaged operational distribution remains no-signaling. H-Bell is the open metric/Ollivier--Ricci stability condition …. That condition is now downstream of a harder one." | Main §3.3 Corollary (H-Bell requires no-signaling and the curvature/metric limit); §A.30 | "H-Bell is the open requirement that those prepared graphs preserve operational no-signaling and the metric/Ollivier--Ricci continuum limit. The curvature condition is downstream of a harder one." |
| ch01 :183 (+FULL :527) | MI plus parameter independence "would imply" the ceiling | §3.3 | Adds ±1 in every run. |
| ch02 :188 (+FULL :831) | MI plus parameter independence "would obey" the ceiling; reference sector "cannot itself supply Bell parameter dependence for wings outside each other's graph cone" | §3.3; Corollary | Adds ±1 in every run, and one-step own-wing interventions to the Corollary clause. |
| ch03 :40 (+FULL :916) | "The reference cubic graph is Bell-local under measurement independence; the adopted branch uses preparation-indexed state-dependent adjacency, with H-Bell conditioning its metric/Ollivier--Ricci compatibility" | Corollary; H-Bell | Bell-locality scoped by one-step own-wing interventions, readouts outside the other wing's graph cone and ±1 in every run; the branch "proposes … under the open hypothesis H-Bell (operational no-signaling and the metric/Ollivier--Ricci continuum limit)". |
| ch03 :162 (+FULL :1038) | coupling-range separation plus a setting-independent ensemble "factorizes" | §3.3 | Adds one-step own-wing interventions and ±1 in every run. |
| ch03 :164 (+FULL :1040) | "A finite-range Bell graph plus a setting-independent response-complete ensemble would force" the local class | §3.3 (iii) | "A Bell graph that does not connect the wings before readout, with one-step own-wing setting interventions and a ±1 outcome in every run, plus …". |
| ch03 :180 (+FULL :1056) | graph separation plus a setting-independent ensemble; "The averaged operational statistics remain no-signaling. H-Bell is the remaining metric/Ollivier--Ricci stability condition …. That condition is now downstream of a harder one." | §3.3; Corollary; §A.30 | Adds one-step own-wing interventions and ±1 in every run; H-Bell sentence as at ch01 :171. |
| ch03 :182 (+FULL :1058) | "that nonlocality is represented by preparation-indexed state-dependent adjacency" | Corollary (H-Bell open) | "is targeted through … under H-Bell". |
| ch04 :90 (+FULL :1209) | "finite-range Bell couplings plus a setting-independent pre-setting ensemble imply Bell factorization" | §3.3 (iii) | "Bell couplings that do not connect the wings before readout, one-step own-wing setting interventions and a ±1 outcome in every run, plus …". |
| ch04 :92 (+FULL :1211) | "its Bell-relevant graph is finite-range at the wings"; reference-graph clause; "with H-Bell now the open metric/Ollivier--Ricci stability condition for the prepared graph family" | §3.3; Corollary; §A.30 | Graph "does not connect the wings before readout", interventions applied at one step, ±1 in every run; one-step own-wing interventions in the Corollary clause; "with H-Bell the open requirement that the prepared graph family preserve operational no-signaling and the metric/Ollivier--Ricci continuum limit". |
| ch04 :124 (+FULL :1243) | "reaches quantum Bell violation only on the ontically parameter-dependent branch" | either/or | "under measurement independence, only on the ontically parameter-dependent branch". |
| ch18 :110 (+FULL :4928) | Bell "rules out" an MI and PI completion; "Chapter 1 proves the corresponding Bell ceiling" from coupling-range separation; "The operational distribution remains no-signaling." | §3.3; Corollary | Adds ±1 in every run, and one-step own-wing interventions; "Whether those prepared graphs keep the operational distribution no-signaling and preserve the continuum-curvature limit is the open hypothesis H-Bell." |
| appendix-c :32 (+FULL :6278) | "local interventions occur before the corresponding cones meet"; "OI therefore cannot combine deterministic response completeness, measurement independence, and ontic parameter independence" | §3.3 (ii), (iii) | Interventions applied at one step, each reading and writing only its own wing, "and each wing's readout lies outside the other wing's graph cone"; ±1 in every run in both sentences. |
| appendix-c :34 (+FULL :6280) | "keeps a pointwise finite-range cone on one setting-independent pre-setting ensemble is a local hidden-variable model"; "implemented in the SM/GR branch" | §3.3 (iii); Corollary | "with one-step own-wing setting interventions, each wing's readout outside the other wing's graph cone, a ±1 outcome in every run, and one setting-independent pre-setting ensemble"; "targeted … under the open hypothesis H-Bell". |
| appendix-c :42 (+FULL :6288) | "a parameter-independent deterministic completion would still satisfy CHSH ≤2" | §3.3 (iv), ±1 | "a measurement-independent, parameter-independent deterministic completion recording a ±1 outcome in every run". |
| glossary :19 (+FULL :6619) | MI plus ontic PI "gives Bell factorization" | §3.3 | Adds ±1 in every run. |
| glossary :49 (+FULL :6649) | MI plus PI "gives the bound 2; quantum violation therefore uses ontic parameter dependence" | §3.3; either/or | Adds ±1 in every run; "quantum violation under measurement independence therefore uses …". |
| glossary :147 (+FULL :6747) | "a measurement-independent, parameter-independent deterministic completion, whose Bell bound is 2" | §3.3 | Adds "recording a ±1 outcome in every run". |
| book/README.md :15 (no FULL mirror) | "H-Bell is the open metric/Ollivier--Ricci stability condition for those prepared graphs" | Corollary | "H-Bell is the open requirement that those prepared graphs preserve operational no-signaling and the metric/Ollivier--Ricci continuum limit." |

## Audit for the outcome-independence error

Every use of "outcome independence", "outcome-independence", "outcome dependence" and "outcome-dependent" in `papers/*.md` and
`book/*.md` was read in context.

- **Main :700.** The only instance of the error. Corrected above.
- **ch04 :90 (+FULL :1209).** "does not obtain quantum Bell violation from outcome-independence failure in an indivisible
  stochastic law". This is correct and is kept.
- **ch03 :162 (+FULL :1038).** "cannot use graph locality, screening, outcome dependence, or indivisibility to explain the quantum
  violation". This is correct and is kept.
- **ch04 :98 (+FULL :1217).** "in the adopted branch it is ontic parameter dependence, not mere stochastic outcome dependence".
  This is correct and is kept.
- **Main :714, Substratum :483, ch04 :146 (+FULL :1265), GR :599.** These use "outcome-independent rule" for identifying
  fundamental open-system processes. That is unrelated to Bell.
- **GR :248.** This uses "outcome-dependent continuation" in an operational protocol. That is unrelated to Bell.
- **Explainer.** It has no outcome-independence placement. Its Bell sites are SC-17's.

## Sites checked and left unchanged

- **Main :770.** It names the adopted branch, measurement independence retained and ontic parameter dependence, and states no
  ceiling.
- **Main §3.3 (:356–:425).** This is the anchor.
- **Main :352.** "the intervention side is settled as a characterization" is outside this unit's Bell lines and is left as it is.
- **ch03 :186, ch05 :95** (SC-17), **Main :176, :706** (SC-28) and **Main :268, :510, :584, :608, :610** (SC-29) are not
  touched.
- **ch02 :188.** The H-Bell gloss, "the compatibility of the local lattice sector with the ontically parameter-dependent Bell
  completion", names no wrong condition, and the text is left as it is.

Deferred to a companion unit (not touched here):

- "That condition is now downstream of a harder one" at Main :410 (the Corollary paragraph), Explainer :340 and Methodology :339.
- Explainer, Methodology, Structure and Substratum Bell wording of the same class: "finite-range Bell" (Methodology, Substratum),
  "remain(s) no-signaling" (Explainer, Methodology, Substratum) and the H-Bell "stability condition" glosses (Explainer, SM,
  Substratum).

## Re-grep (`papers/Main.md`, `book/*.md`; line counts)

| Phrase | Count | Where |
|---|---|---|
| "outcome independence violation" | 0 | |
| "is now separate", "H-Bell now", "not yet claimed", "should not be turned" | 0 each | |
| "implements through preparation", "realized in the SM/GR", "realized in the specific SM/GR", "implemented in the SM/GR", "represented by preparation-indexed" | 0 each | |
| "finite-range Bell", "pointwise finite-range", "finite-range at the wings" | 0 each | |
| "remains no-signaling", "stability condition for" | 0 each | |
| "now downstream of a harder one" | 1 | Main :410, deferred |
| "is downstream of a harder one" | 4 | ch01 :171, ch03 :180 and FULL |
| "outcome-independence failure" | 2 | ch04 :90 and FULL; correct use |
| "outcome dependence" | 4 | ch03 :162, ch04 :98 and FULL; correct uses |
| "therefore requires ontic parameter dependence" | 1 | Main :558, scoped to the adopted branch |
| "\pm1$ outcome" | 46 | Main 8, chapters, appendix-c and glossary 19, FULL 19 |
| "applied at one step" | 20 | Main 4, chapters and appendix-c 8, FULL 8 |
| "one-step own-wing" | 15 | Main 1, chapters and appendix-c 7, FULL 7 |
| "open hypothesis H-Bell" | 9 | Main 1, chapters and appendix-c 4, FULL 4 |
| "open requirement that" | 7 | book/README, ch01, ch03, ch04, FULL 3 |

Each chapter line changed here appears verbatim in FULL (`mirror_check`: 0 chapter lines absent).

The Introduction (`papers/Introduction.md` on `draft/oi-introductory-paper-20261025` at `3e600003`, read only) states the
ceiling with all four hypotheses and ±1 in every run (L254). It states the either/or and the adopted branch (L258), and H-Bell as
no-signaling plus the gravitational continuum limit (L258, L260). It makes no outcome-independence placement. The L306 entry
"the Bell ceiling" is proved on paper.

Regenerated: Main and the book (`.tex` and `.pdf`). Main stays at 96 pages and the book goes from 558 to 559, from the added text; no glyph was dropped.
