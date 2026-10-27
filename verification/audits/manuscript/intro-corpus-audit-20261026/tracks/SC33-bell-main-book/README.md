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
added as well.

| Site | Was | Anchor | Now |
|---|---|---|---|
| Main :700 | 't Hooft comparison: "Bell placement (outcome independence violation vs. superdeterminism)" | §3.3 either/or; theorem proof (determinism makes the conditionals point masses) | "Bell placement (ontic parameter dependence with measurement independence retained vs. superdeterminism)" |
| Main :766 | ceiling from "genuine local interventions" and pointwise separation, no ±1; "Reproducing quantum correlations therefore requires ontic parameter dependence, which … the specific SM/GR target implements through preparation-indexed state-dependent adjacency" | §3.3 (i)–(iv), ±1 in every run, either/or; Corollary (H-Bell open) | Ceiling states one-step own-wing interventions and a ±1 outcome in every run read outside the other wing's cone. Reproduction requires giving up ontic parameter independence or measurement independence, and §3.3 gives up the first. Preparation-indexed adjacency is the proposed SM/GR implementation, and its compatibility with no-signaling and the continuum-curvature limit is the open hypothesis H-Bell. |
| Main :558 | "The Bell side is now separate rather than analogous"; "a measurement-independent deterministic completion with that pointwise cone is Bell-local" | §A.33; §3.3 (ii), (iii), ±1 | "The Bell side is a separate question rather than an analogous one"; the completion has own-wing setting interventions, readouts outside the other wing's cone and a ±1 outcome in every run. "The framework's adopted Bell branch therefore requires ontic parameter dependence" is kept, since it is scoped to the branch that retains measurement independence. |
| Main :22 | "keeps the pointwise cone and a setting-independent pre-setting ensemble"; parameter dependence "realized in the specific SM/GR branch through preparation-indexed … adjacency" | §3.3 (ii)–(iv), ±1; Corollary | Own-wing interventions, readouts outside the other wing's cone recording a ±1 outcome in every run. "realized" becomes "targeted"; the abstract's later sentence names H-Bell as open. |
| Main :646 | "if that pointwise cone is kept at the wings' separation and the pre-setting ensemble is measurement-independent" | §3.3 (ii), ±1 | Adds own-wing setting interventions and a ±1 outcome in every run. |
| ch00 :55 (+FULL :291) | graph-cone separation and a setting-independent ensemble give the ceiling; parameter dependence "realized in the SM/GR target through preparation-indexed structure" | §3.3; Corollary | Adds own-region interventions and ±1 in every run. The SM/GR target proposes preparation-indexed structure, and whether it keeps no-signaling and the continuum-curvature limit is the open hypothesis H-Bell. |
| ch01 :16 (+FULL :360) | "pointwise finite-range cone together with local interventions and one setting-independent pre-setting ensemble is Bell-local" | §3.3 | Own-wing interventions and a ±1 outcome in every run. |
| ch01 :169 (+FULL :513) | the book's own statement of the ceiling: coupling-range separation plus a setting-independent ensemble | §3.3 | Adds own-wing interventions and a ±1 outcome at each wing in every run. |
| ch01 :183 (+FULL :527) | MI plus parameter independence "would imply" the ceiling | §3.3 | Adds a ±1 outcome in every run. |
| ch02 :188 (+FULL :831) | MI plus parameter independence "would obey" the ceiling; the reference sector "cannot itself supply Bell parameter dependence for wings outside each other's graph cone" | §3.3; Corollary (one-step own-region interventions) | Adds ±1 in every run, and own-wing setting interventions to the Corollary clause. |
| ch03 :162 (+FULL :1038) | coupling-range separation plus a setting-independent ensemble "factorizes" | §3.3 | Adds own-wing interventions and ±1 in every run. |
| ch03 :164 (+FULL :1040) | "A finite-range Bell graph plus a setting-independent response-complete ensemble would force" the local class | §3.3 | Adds own-wing interventions and ±1 in every run. |
| ch03 :180 (+FULL :1056) | graph separation plus a setting-independent ensemble give Bell factorization | §3.3 | Adds own-wing interventions and ±1 in every run. |
| ch04 :90 (+FULL :1209) | "finite-range Bell couplings plus a setting-independent pre-setting ensemble imply Bell factorization" | §3.3 | Adds own-wing interventions and ±1 in every run. |
| ch04 :92 (+FULL :1211) | finite-range graph plus setting-independent ensemble cap CHSH; reference graph Corollary clause; "with H-Bell now the open …" | §3.3; Corollary; §A.30 | Adds own-wing interventions and ±1 in every run, own-wing interventions in the Corollary clause, and drops "now". |
| ch18 :110 (+FULL :4928) | Bell "rules out" an MI and PI completion; "Chapter 1 proves the corresponding Bell ceiling" from coupling-range separation and one ensemble | §3.3 | Adds ±1 in every run to the first, and own-wing interventions and ±1 in every run to the second. |
| appendix-c :32 (+FULL :6278) | finite range, "local interventions" before the cones meet, one ensemble; "OI therefore cannot combine deterministic response completeness, measurement independence, and ontic parameter independence" | §3.3 | Own-wing interventions and ±1 in every run, in both sentences. |
| appendix-c :34 (+FULL :6280) | pointwise cone on one ensemble "is a local hidden-variable model"; parameter dependence "implemented in the SM/GR branch through preparation-indexed structure" | §3.3; Corollary | Adds own-wing interventions and ±1 in every run. "implemented" becomes "targeted … under the open hypothesis H-Bell". |
| glossary :19 (+FULL :6619) | MI plus ontic PI "gives Bell factorization" | §3.3 | Adds a ±1 outcome in every run. |

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
- **Main :82, the Theorem statement.** "measurement independence plus ontic parameter independence would force $|S|\le2$" omits
  ±1 in every run. It is a canonical statement and not on this unit's list, so it is left for #946.
- **glossary :49 (+FULL :6649), appendix-c :42 (+FULL :6288), ch03 :40 (+FULL :916).** These are compressed ceilings of the same
  kind, outside this unit's list, and are left for #946.
- **ch01 :171, ch03 :180, Main §3.3 (Corollary).** "That condition is now downstream of a harder one" also stands in Explainer
  :340 and Methodology :339. It is one sentence across five sources, so it is left for a corpus-wide unit.
- **ch02 :188.** H-Bell is glossed as "the compatibility of the local lattice sector with the ontically parameter-dependent
  Bell completion", which is looser than §3.3's no-signaling-plus-curvature condition. The text is left as it is.
- **ch03 :186, ch05 :95** (SC-17), **Main :176, :706** (SC-28) and **Main :268, :510, :584, :608, :610** (SC-29) are not
  touched.

## Re-grep (`papers/*.md`, `book/*.md`; line counts)

| Phrase | Count | Where |
|---|---|---|
| "outcome independence violation" | 0 | |
| "is now separate" | 0 | |
| "H-Bell now" | 0 | |
| "implements through preparation", "realized in the SM/GR", "realized in the specific SM/GR", "implemented in the SM/GR" | 0 each | |
| "outcome-independence failure" | 2 | ch04 :90 and FULL; correct use |
| "outcome dependence" | 4 | ch03 :162, ch04 :98 and FULL; correct uses |
| "therefore requires ontic parameter dependence" | 2 | Main :558, scoped to the adopted branch; Explainer, SC-17's |
| "\pm1$ outcome" | 35 | Main 7 (3 in §3.3, 4 added), chapters, appendix-c and glossary 14, FULL 14 |
| "open hypothesis H-Bell" | 5 | Main :766, ch00 :55, appendix-c :34 and the two FULL mirrors |

Each chapter line changed here appears verbatim in FULL (`mirror_check`: 0 chapter lines absent).

The Introduction (`papers/Introduction.md` on `draft/oi-introductory-paper-20261025` at `3e600003`, read only) states the
ceiling with all four hypotheses and ±1 in every run (L254). It states the either/or and the adopted branch (L258), and H-Bell as
no-signaling plus the gravitational continuum limit (L258, L260). It makes no outcome-independence placement. The L306 entry
"the Bell ceiling" is proved on paper.

Regenerated: Main and the book (`.tex` and `.pdf`). The page counts are unchanged at 96 and 558, and no glyph was dropped.
