# BH manuscript-consistency correction — change note (record of the change)

- **Worktree:** `bhfix/wt`, branch `fix/bh-consistency-20261026`, base `main` 687e885b.
- **Inputs:** `paper/r11/FINDINGS.md`, plus `paper/r11/REVIEW.md`, which governs wherever the two differ.
- **Edit script:** `bhfix/apply_edits.py`. It makes 47 exact-match replacements, and each `old` string must
  occur exactly once in every target. Chapter edits are applied identically to FULL.md.

Files changed (`git diff --stat`):
- **Manuscript:** papers/GR.md; book/ch07, ch09, ch18, ch19, glossary, appendix-a, bibliography, README;
  book/The-Incompleteness-of-Observation-FULL.md.
- **Regenerated:** papers/GR.tex and papers/GR.pdf; book/…FULL.tex and book/…FULL.pdf.
- **Bookkeeping:**
  - tools/dependency_label_check.py: `decouple` is added to `CONDITION_TOKENS`, as the tool's comment requires
    whenever a new H-name is introduced.
  - verification/coverage/LEDGER.json: two fingerprints are re-affirmed (see Checks).

## 1. Site table

Line numbers are those at main 687e885b (GR lines after :815 shift by +2 to +4 in the edited file). Abbreviations: F = FINDINGS item, R = REVIEW item. "+FULL" means the identical line is changed in FULL.md; every
changed chapter line was confirmed present once in FULL with `grep -cxF`, and mirror_check reports 0 absent lines.

| Site | Old (short) | New (short) | Source |
|---|---|---|---|
| ch07:12 +FULL | "§7.6 resolves the BH information paradox … Page curve is derived from cycle typicality, cond. on H-scramble … mass-independent Page time" | "treats … a cycle-averaged Page curve follows under H-scramble and H-decouple … Page time that, for a mass-independent emission coefficient, is a fixed fraction …" | F D.1, D.2, D.6; O-1 |
| ch07:110 +FULL | "resolves the paradox at the structural level: … because φ is bijective." | "…at the level of information preservation: …; how much an observer can recover from the radiation is a separate question, which bijectivity alone does not settle and which the Page-curve derivation below addresses under its own conditions." Sentence 3 is kept. | F1 / R1 (FINDINGS wording, accepted by the review) |
| ch07:116 +FULL | "conditional on H-scramble … Under that condition the two derivations give a Page curve of the same form" | "…H-scramble and the decoupling condition H-decouple … Under those conditions … same form, the framework's as an average over the cycles of the dynamics" | R M4; O-1; §C.4 |
| ch07:118 +FULL | heading "The framework's resolution: nested trace-out." | "The observer's description: nested trace-out." | F D.1 |
| ch07:126 s1 +FULL | "runs through the *combinatorial* structure … rather than through the gravitational path integral" | "does not use the gravitational path integral: the cycle structure … supplies exact time averages, and the Page value enters through a typicality condition on the substratum orbit" | F2 / R2a |
| ch07:126 s2 +FULL | "PSW typicality theorem: … generic pure state … approximately maximal, corrections vanish exponentially in the dimension of the larger subsystem" | "Page's mean entropy (Page 1993) and measure concentration (Popescu, Short & Winter 2006): … Haar-random … close to Page's mean ≈ ln d_min − d_min/(2d_max), within half a nat of ln d_min at equal dimensions … deviations exponentially unlikely in the dimension of the smaller subsystem" | R2b (wording) + R M8 |
| ch07:126 s3 +FULL | "a finite bijection *can* count its cycles uniformly while visiting only product states" | "every finite bijection acting on a definite configuration, with the bipartition aligned to the configuration coordinates, visits only product states, however uniformly it counts its energy-shell cycles" | O-2 default (BH-02 C1) |
| ch07:130–132 +FULL | "For the typical state … PSW … applied to the bijection's cycle structure, which is what H-scramble supplies — S_rad(t) = min·ln q … corrections are exponentially small" | "Under H-scramble, which carries PSW concentration from the Haar ensemble to the orbit, and under H-decouple …, the entropy averaged over full cycles at the bipartition of time t is \overline{S}_rad(t) = min·ln q … correction of at most about half a nat, reached at the turnover and exponentially small in \|n_R−n_B\| away from it. Whether the entropy along a single trajectory … follows the same curve is open." | R M10; F C.1 / D.3; R §2 ch07:132 wording; §C.4 |
| ch07:143 +FULL | "conditional on β = 1 as well as on H-scramble" | "… on H-scramble and H-decouple" | O-1 (F D.5) |
| ch07:149 +FULL | "under H-scramble, a Page curve … is reproducible …; the scrambling condition and the radiation's entropy per boundary mode lost are the open steps" | "under H-scramble and H-decouple, a cycle-averaged Page curve …; the open steps include the scrambling condition, the decoupling condition, whether the entropy along a single trajectory follows the cycle-averaged curve, and the radiation's entropy per boundary mode lost" | R M3; O-1; §C.4 |
| ch07:157 +FULL | "the black hole's reduced entropy is approximately min(n_R,n_B) ln q" | "…equals the radiation's and is at most n_R ln q" | §C.4 propagation (it quoted A.9 pointwise) |
| ch07:159 +FULL | "The framework's resolution of the information paradox" | "The framework's account …" | F3 / R3 |
| ch07:161 s1–2 +FULL | falsifier: "radiation carries less information … in a way that cannot be reproduced by the nested trace-out. No such evidence …" | "Bijective dynamics is compatible with radiation that carries less information …, the remainder being held in sectors the observer does not read, and the nested trace-out is consistent for every dynamics; a measurement of the radiation alone therefore does not test the conservation claim, which rests on bijectivity as a premise (Chapter 1). The QES + islands computations … support unitary evaporation without depending on the framework." The rest is unchanged. | R3 wording; O-4 |
| ch07:288 +FULL | "the Page curve requires H-scramble" | "… requires H-scramble and H-decouple" | O-1 |
| ch09:108 +FULL | "(resolving the BH information paradox in Chapter 7 §7.6)" | "(the information-preservation half of Chapter 7 §7.6)" | F D.1 |
| ch09:127 +FULL | "Page curve conditional on H-scramble" | "… on H-scramble and H-decouple" | O-1 |
| ch18:146 +FULL | "resolution …; … preserves unitarity at the substratum level while reproducing the Page curve at the emergent level" | "account …; …φ is bijective; whether the radiation carries it is a separate question, which bijectivity alone does not settle. … self-consistent emergent quantum description when the two boundaries coexist; the Page curve at the emergent level is a conditional result (Chapter 7 §7.6)" | R5, verbatim |
| ch18:148 +FULL | "Its Page time is a mass-independent fraction" | "For a mass-independent emission coefficient (Chapter 7 §7.6), its Page time is a fixed fraction" | F9 / R10 (R12) |
| ch18:150 +FULL | "inaccessible at the emergent level (the radiation looks thermal" | "inaccessible at the emergent level while it resides in the sectors the emergent description traces out (…" | O-3, minimal scoping (R §4) |
| ch18:156 +FULL | "as the two-level description does for the cosmological constant and information paradox problems" | "… for the cosmological constant problem and, at the level of information preservation, for the information paradox" | R M9 |
| ch18:158 +FULL | "(which it does, through the nested partition)" | "(the substratum preserves it, by bijectivity; whether the radiation carries it is the separate question of Chapter 7 §7.6)" | R6, verbatim |
| ch19:72 +FULL | "The Page curve follows from cycle typicality …, applying PSW … under H-scramble …, which is not established. … independent of mass" | "The Page curve follows, as an average over the cycles of the dynamics, under H-scramble and H-decouple …, neither of which is established: H-scramble carries PSW concentration to the orbit …, whose cycle structure supplies exact time averages. … independent of mass for a mass-independent emission coefficient" | O-1; F D.2, D.6; §C.4 |
| ch19:334 +FULL | "Resolved (Page curve from typicality)" | "Preserved; Page curve conditional" | F7 / R7; O-6 default |
| ch19:370 | "ten disparate hard problems" | **unchanged.** The ten are those listed at ch19:366 (CC, measurement, Bell, KS, PBR, FR, dark sector, hierarchy, Higgs criticality, GUT absence); BH information is not among them. ch18:347's "ten problems" list does include BH, under "resolution, dissolution, conditional construction or partial treatment", which the new cell satisfies. | R M11 |
| glossary:113 +FULL | "derives the Page curve from cycle typicality, conditional on H-scramble, … a mass-independent fraction" | "obtains a cycle-averaged Page curve under H-scramble and H-decouple, with a Page time that, for a mass-independent emission coefficient, is a fixed fraction" | F D.2, D.6; O-1 |
| appendix-a:103 +FULL | "The Page curve requires H-scramble." | "… requires H-scramble and H-decouple." | O-1 |
| appendix-a:116 (G11) +FULL | "Nested trace-out and H-scramble \| C \| 1 \| Scrambling condition open" | "Nested trace-out, H-scramble, H-decouple \| C \| 1 \| Scrambling, decoupling open". Class C is unchanged, so no count moves. | O-1 |
| book/README.md:64 (no mirror) | "the Page curve from nested trace-out, conditional on … H-scramble" | "a cycle-averaged Page curve conditional on … H-scramble and … H-decouple" | R M2; O-1 |
| bibliography +FULL | Page 1993 and Popescu–Short–Winter 2006 missing | Page (1993) PRL 71:1291, gr-qc/9305007; Popescu, Short & Winter (2006) Nat. Phys. 2:754, quant-ph/0511225 | R M8 |
| GR:605 | "it shows … well-defined …, and that the Page curve follows under H-scramble, while the GSL remains open" | "…well-defined when multiple boundaries coexist. Appendix A also obtains a cycle-averaged Page curve, conditional on H-scramble and H-decouple, and leaves the GSL open." | R M1; O-1 |
| GR:611 | "S_rad(t)=min·ln q plus exponentially small corrections"; "independent of mass and of the emission coefficient"; "from bijectivity (cycle decomposition) and PSW typicality [29], conditional on H-scramble" | "averaged over full cycles at the bipartition of stage t … \overline{S}_rad … up to a correction of at most ½, reached at n_R=n_B and exponentially small in \|n_R−n_B\| away from it (Theorem A.9) …; whether the entropy along a single trajectory follows the same curve is open"; "… when that coefficient is mass-independent"; "recovered, as a cycle average, … from PSW typicality [29] carried to the orbit by H-scramble …, the cycle decomposition supplying exact time averages, and conditional also on H-decouple, which timescale ordering does not supply" | R §2 GR:611; F D.2, D.3, D.6; O-1; §C.4 |
| GR:717 | "deriving the Page curve under H-scramble" | "deriving a cycle-averaged Page curve under H-scramble and H-decouple" | R M5; O-1 |
| GR:805 (A.6 GSL para) | "where B∪R is effectively pure (Theorem A.7), S(ρ_B)=S(ρ_R) follows Theorem A.9" | "where B∪R is effectively pure under H-decouple, S(ρ_B)=S(ρ_R) ≤ n_R ln q" | A.7 and A.9 restatements; the argument is unchanged |
| GR:811 | "D is frozen on evaporation timescales (τ_evap ≪ τ_B^D), so by Theorem A.5 …" | Step (i) of A.5 freezes D only for t ≪ τ_B^D ~ 1/H ~ 1e17 s; t_evap ~ 1e79 s at 30 M☉, Γ~1; ratio ~1e62; t_evap > τ_B^D above ~1e11 kg; A.7 is stated for t ≪ τ_B^D; A.8–A.9 work with a pure B∪R state and so rely on **H-decouple** (defined here), which timescale ordering does not supply and which is not established | F8 / R8 wording; O-1; A.7 gap |
| GR:813 (Thm A.7 statement) | "joint state of B and R effectively pure … + O(τ_S/τ_B^D) … ∈ H_B(t)⊗H_R(t)" | "(Effective pure state) joint state of V and B effectively pure … + O(t/τ_B^D) … ∈ H_V⊗H_B" | R M6 (scope its proof supports); error term per A.5(i) (R8(i), confirmed) |
| GR:815 (A.7 proof) | "…+O(τ_S/τ_B^D). Restricting to B∪R: ρ_BR ≈ \|ψ⟩⟨ψ\| pure … ~10^-32" | The proof now ends at ρ_VB, with correction O(t/τ_B^D). A new paragraph follows: the restriction to B∪R is pure only if V∖R is unentangled with B∪R, which A.7 does not establish, and A.8–A.9 take B∪R pure throughout, which is H-decouple. | R M6 |
| GR:829 | "By Popescu-Short-Winter [29], the set of atypical states …" | "By measure concentration for Haar-random pure states (Lévy's lemma applied to the entanglement entropy, as in Hayden-Leung-Winter [61]; Popescu-Short-Winter [29] give the corresponding bound for the distance of the reduced state from its canonical form), …" | R M7 |
| GR:831 | "[29] bounds … constrained Hilbert subspace … from [29] alone"; one-long-cycle example | "[29] and [61] bound … Hilbert space or subspace … from [29, 61] alone". New sentence after the example: "The same holds for every bijection: acting on a definite configuration, φ visits only configurations, each a product state across a bipartition aligned with the configuration coordinates, so S(ρ_R)=0 along every such orbit." | R M7; O-2 default, applied in GR so the book does not lead the paper |
| GR:841–847 (Thm A.9) | "(conditional on A.8, hence on H-scramble) (The Page curve). The entanglement entropy of the radiation follows: S_rad(t)=…" | "(The cycle-averaged Page curve; conditional on A.8, hence on H-scramble, and on H-decouple). At each stage t take the bipartition of A.8 with d_B=q^{n_B(t)}, d_R=q^{n_R(t)}, held fixed. For all but the fraction excluded in A.8, and up to its O(ε), the full-cycle time average … is: \overline{S}_rad(t)=…". New paragraph after the proof: A.9 concerns full-cycle averages at the fixed stage-t bipartition; the entropy along one trajectory with a moving bipartition is a different quantity, and whether it follows the same curve is open. | R §C.4 repair (a) |
| GR:865 | "the entropy of the radiation at the Page time is S_rad(t_P) ≈ …" (×2) | "the cycle-averaged entropy … \overline{S}_rad(t_P) ≈ …" | §C.4 propagation |
| GR:869 s1 | "invokes only Popescu-Short-Winter [29] …, with no replica trick, no ergodicity assumption, and no gravitational path integral" | "applies Popescu-Short-Winter [29] … under H-scramble, with no replica trick and no gravitational path integral; H-scramble is an equidistribution hypothesis on the orbit over pure states, which ergodicity over configurations does not supply". The theorem's object becomes "a cycle-averaged Page curve". | F8 / R9 |
| GR:869 last s. | "under Theorem A.8's typicality and horizon-factorization hypotheses … a Page curve" | "under H-scramble and H-decouple, at the G1 register — … a cycle-averaged Page curve" | R9 wording; O-5; O-1 |
| GR refs | — | [61] P. Hayden, D. W. Leung, A. Winter, "Aspects of generic entanglement," CMP 265, 95–117 (2006); quant-ph/0407049 | R M7 |

## 2. Owner decisions: defaults, accepted by the owner on 2026-10-26 (§7)

The manuscript text carries no decision markers. The alternatives below are kept as the record of what was decided against.

- **O-1 (H-decouple).**
  - *Default applied.* The condition is named **H-decouple** and defined once, at GR §A.7 (:811), which states
    that Theorems A.8–A.9 rely on it.
    - It is carried at every sufficiency-form site: GR:605, :611, :717, :841 (A.9 label), :869; ch07:116,
      :130, :149; ch19:72; ch18:146 uses the review's condition-list-free form.
    - It is also carried at the necessity-form and status sites: ch07:12, :143, :288; ch09:127; glossary:113;
      appendix-a:103 and G11; README:64.
  - *Alternative.* Leave the condition unnamed: state it once at GR:811 as in the review's wording, and use a
    condition-list-free form ("conditional") at the status cells.
- **O-1a: the scope of H-decouple.** This departs from the coordinator's definition.
  - *Default applied.* H-decouple = "over the evaporation, B∪R stays decoupled from D **and unentangled with
    V∖R**, so its joint state remains effectively pure".
  - *Why.* The review's A.7 gap (M6) is a second implicit decoupling. A.8 is stated for pure states on
    H_B⊗H_R, so what A.8–A.9 actually rely on is purity of B∪R. With D alone, every "conditional (H-scramble,
    H-decouple)" cell would still omit a condition, which is the sufficiency overclaim the review flagged.
  - *Alternative.* Narrow H-decouple to D only, and carry the V∖R step as a separately stated condition of
    A.9 or its application. Every status list would then need a third item.
- **A.7 gap: the conservative choice taken.**
  - A.7 is restated at the scope its proof supports: V∪B effectively pure for t ≪ τ_B^D, with error O(t/τ_B^D).
  - The B∪R step is stated as not established, and is folded into H-decouple.
  - No proof was invented.
  - *Alternative.* Keep A.7 on B∪R, with "if V∖R is unentangled with B∪R" as an explicit hypothesis in its
    statement.
  - *Error term.* Corrected to O(t/τ_B^D), as A.5 step (i) supplies (REVIEW item 8(i) confirms it). The
    "~10⁻³²" number, which was τ_S/τ_B^D, is removed.
- **§C.4 (Theorem A.9).**
  - *Default applied:* repair (a). A.9 is restated for full-cycle time averages at the fixed stage-t
    bipartition, with \overline{S}_rad, and the single-trajectory reading is stated as open. This adds no
    assumption.
  - *Propagated to:* GR:605, :611, :717, :805, :865, :869; ch07:116, :130–132, :149, :157; ch19:72;
    glossary:113; README:64.
  - *Alternative:* repair (b). Keep the pointwise statement and add a named pointwise-typicality hypothesis.
    That is a new assumption.
- **O-2.**
  - *Default applied.* The settled C1 fact is stated at ch07:126 s3 ("every finite bijection acting on a
    definite configuration … visits only product states") and generalized in GR:831.
  - *Not stated:*
    - the C6(a) consequence, that H-scramble therefore cannot hold in A.7's own setting of a definite initial
      state with an aligned split (a reader can infer it from GR:815 together with GR:831);
    - any remedy (a superposed initial state, or a non-aligned factorization).
  - ch07:151 and GR:871 ("it can be combinatorial") are left unchanged.
  - *Alternatives:* state C6(a) explicitly at GR:831/833 and ch07:126; and/or adopt a remedy.
- **O-3.**
  - *Default applied.* Both accounts are kept, conservation (bijectivity as premise) separated from recovery
    (conditional). ch18:150 receives the review's minimal scoping.
  - *Alternative.* Choose one account.
- **O-4.**
  - *Default applied.* The empty falsifier at ch07:161 is removed and no new one is proposed. The paragraph
    heading "Empirical status and falsification." is kept.
  - *Alternative.* Supply a falsifier for recoverability, which would be a new claim.
- **O-5.**
  - *Default applied.* "Horizon-factorization hypotheses" is removed at GR:869 and replaced by
    "H-scramble and H-decouple". No new hypothesis is defined.
  - *Alternative.* Define a horizon-factorization hypothesis. That would be a new assumption, possibly also
    covering BH-02 C6(c) (see §5).
- **O-6.**
  - *Default applied.* The ch19:334 cell reads "Preserved; Page curve conditional".
  - *Alternative.* "Conditional (H-scramble, H-decouple)".

## 3. Build and checks

**Build.** `sh ./build.sh GR`, then `sh ./build.sh --book`. `build.sh` takes either paper names or `--book`
alone, so `GR --book` in one call reports "--book: no such source".
- **GR:** 87 pages (main: 86).
- **Book:** 554 pages (main: 553).
- **Median characters per page:** GR 3200 against 3200 on main; book 3055 against 3063.
- **Dropped glyphs:** none ("build: OK", no "Missing character").
- **Toolchain.** Pandoc 3.1.3 with xelatex from TeX Live 2023. The producer is xdvipdfmx 20220710, the same as
  main's PDFs, so the PDFs are not provisional.
- **.tex diffs against main** are content hunks only.
- **Stamps.** Main's .tex stamps matched main's sources, so the artifacts were fresh before this change.
  `staleness_check` now reports GR and the book as "stamp matches source".
- **git status.** The .tex/.pdf files show as modified. `ls-files -v` reports `H`, so they are tracked
  normally despite the sparse-checkout patterns.

**Checks.** Run from the worktree root with `python3 -I -B`.

| Check | Result |
|---|---|
| tools/staleness_check.py | OK (2 matched, 11 unstamped: the other papers' .tex are absent in the sparse checkout) |
| tools/voice_check.py | OK (40 files) |
| tools/claims_check.py | OK |
| tools/duplicate_check.py | OK |
| papers/oi_lattice_code/mirror_check.py | 0 chapter lines absent from FULL.md |
| papers/oi_lattice_code/citation_check.py | 112 citations, 0 broken, 0 duplicate bib numbers ([61] new) |
| papers/oi_lattice_code/architecture_check.py | 259 invariants, 0 violations |
| tools/dependency_label_check.py --strict | self-test OK; no stale label (67 advisory notes, not gating) |
| tools/coverage_check.py | First run: **FAIL**, with STALE `GR:T-a.7` and `GR:T-a.9` (the statements changed). Both entries are GAP with no checks and delta "not formalized"; I re-read them, and the mapping, level and delta still hold. I updated the fingerprints afea3a8c…→ef7fd416… and d42ca3c5…→ed567edf…. Rerun: OK (128 canonical statements). A.7's ledger `line` (815) was already off from the census (813) on main and is untouched. |
| tools/lean_manuscript_census.py | OK (20 current families) |

## 4. Re-grep (§A.25 step 6)

Counts are lines in papers/*.md + book/*.md (FULL excluded), with FULL separate. Main 687e885b → now.

| Pattern | Non-FULL | FULL | Survivors and why legitimate |
|---|---|---|---|
| "resol" on lines that mention the paradox, BH information or the Page curve | 17 → 11 | 14 → 8 | See the list after this table. |
| "never lost" | 6 → 6 | 6 → 6 | ch07:12, :110, :118, :159; ch18:146; ch19:72. All are conservation clauses attributed to bijectivity, scoped from recovery where they sit or in the same section. |
| "because $\varphi$ is bijective" | 2 → 2 | 2 → 2 | ch07:110 and ch18:146. Each is now immediately followed by "whether the radiation carries it … bijectivity alone does not settle". |
| "exponentially small" | 4 → 4 | 1 → 1 | GR:611 and ch07:132 are the corrected "exponentially small in \|n_R−n_B\| away from the turnover"; Main:425 and Explainer:361 are unrelated (fast-bath / dephasing). |
| "mass-independent" | 5 → 7 | 4 → 5 | ch07:137 is the anchor. GR:611, ch07:12, ch18:148, ch19:72 and glossary:113 now state it as the condition "for a mass-independent emission coefficient". SM:1092 is unrelated. |
| "independent of mass" | 2 → 2 | 1 → 1 | GR:611 ("… when that coefficient is mass-independent") and ch19:72 ("… for a mass-independent emission coefficient"). |
| τ_evap (`\tau_{\text{evap}}`) | 1 → 0 | 0 → 0 | The false inequality is gone. |
| "horizon-factorization" | 1 → 0 | 0 → 0 | — |
| "Popescu" | 9 → 10 | 5 → 6 | The new hit is the bibliography entry. All mentions now attribute PSW to measure concentration, carried to the orbit by H-scramble (GR:611, :831, :873, ref [29]; ch07:126, :130, :147, :151; ch19:72). |
| "ergodic" | 10 → 10 | 0 → 0 | GR:873 is the corrected "which ergodicity over configurations does not supply". The others (Juno, Main, SM, Structure) are unrelated. |
| "Page curve" | 27 → 27 | 19 → 19 | Every framework-side mention is conditional or "cycle-averaged". The unconditional ones are the QES literature (ch07:116 s2, :145, :161; GR:871), Page's definition (ch07:114) and headings. ch07:147, "arrives at a Page curve of the same form", keeps the review's verdict *keep*: the next sentence conditions it on H-scramble, and :149 carries the full condition list. |
| "H-decouple" (new) | 0 → 20 | 0 → 11 | One definition, at GR:811. Every other occurrence cites it. |

Survivors of the "resol" re-grep:
- ch07:110: "resolves the paradox at the level of information preservation". This is ch19:72's anchor phrase, followed
  in the same sentence by the recovery split.
- ch07:116: "unresolved for decades". Historical.
- ch18:130: "same structural resolution". Its verdict is CONSISTENT, and it is scoped in the same line.
- ch18:347, ch19:10, README:92 and ch00:
  - These are inventories, "problems the framework addresses with a resolution, dissolution, conditional
    construction or partial treatment".
  - The BH entry falls under conditional construction.
- ch19:30 and ch19:72: "not a completed resolution of quantum gravity" and "Resolved at the level of information
  preservation". Both are anchors.
- Main:66: "a paradox to be resolved". This is the premise remark and is kept.
- GR:605: "Appendix A resolves the formal nested-partition machinery in three layers". It describes the
  appendix, not the paradox, and is left unchanged; "develops" would be clearer, and that change is optional.

## 5. Departures from the review's wording, and items not addressed

**Departures**
1. **GR:811.** H-decouple is named, and its scope is widened to V∖R (O-1a). The review's clause "assumes in
   addition that D stays decoupled …" became "Theorems A.8–A.9 work with a pure joint state of B and R … and so
   rely on the decoupling condition H-decouple: …".
2. **GR:869, last sentence.** "under H-scramble and H-decouple" replaces "under H-scramble, with D decoupled from
   B∪R over the evaporation" (O-1 naming).
3. **ch07:126 s2.**
   - Added "with subsystem dimensions d_min ≤ d_max", so the formula's symbols are defined.
   - Added the citations "(Page 1993)" and "(Popescu, Short & Winter 2006)", which tie to the new bibliography
     entries (M8).
4. **ch07:130–132.** The review gave wording only for :132. :130 (M10) is my wording. It removes the
   cycle-structure attribution, adds H-decouple and the cycle average, and adds the open single-trajectory
   sentence. The display becomes \overline{S}_rad.
5. **GR:611.** The review's attribution splice is used, with three additions:
   - "as a cycle average";
   - the H-decouple clause;
   - the stage-t cycle-average and open-trajectory clauses (§C.4).
6. **No wording was supplied by the review for these sites, so the text is mine:**
   - ch07:116 (M4), ch07:149 (M3), ch18:156 (M9);
   - GR:605 (M1), GR:717 (M5), GR:829/:831 (M7);
   - GR:805 and ch07:157 (A.9 propagation). The pointwise "≈ min(n_R,n_B) ln q" is replaced by the provable
     bound S(ρ_B)=S(ρ_R) ≤ n_R ln q, which keeps the GSL argument intact.
7. **ch07:149.** The open-step list is made non-exhaustive ("the open steps include"), and it omits BH-02 C6(c)
   (shell factorization), which no GR text states. Adding it to the book alone would make the book lead the
   paper.
8. **G11.** The FINDINGS *keep* of "Nested trace-out" in the Formula column is retained, with H-decouple added.

**Not addressed; needs the owner or a separate review**
- **BH-02 C6(c), shell factorization.**
  - Theorem A.8 states S_Page(d_B,d_R) with the full factor dimensions while positing equidistribution on a shell
    subspace.
  - BH-02 certifies that the Haar-on-shell mean differs from that value, in a direction that depends on the shell.
  - Neither FINDINGS nor REVIEW gives a verdict on A.8 itself. If confirmed, it is a GR:817–823 statement-level
    issue, so A.8 was left untouched.
- **ch07:151 / GR:871, "it can be combinatorial".** Left unchanged under O-2. The review calls it incomplete, not
  refuted.
- **Introduction draft (`paper/draft/Introduction-r4.md`).** It is not in the worktree and was not edited. Its
  substance is unaffected: it lists the A.8→A.9 step as open (:201) and the decoupling as not established (:204).
  Two wording adjustments would match the corrected corpus:
  - **:201.** "the step from the cycle time average of [GR, Thm A.8] to the pointwise curve of [GR, Thm A.9]" →
    "the step from the cycle-averaged curve of [GR, Thms A.8–A.9] to the entropy along a single trajectory".
    A.9 is no longer a pointwise curve.
  - **:241.** "the Page curve follows only under H-scramble" → "… only under H-scramble and H-decouple", if O-1
    stands.
- **Process corrections for the commit record, from REVIEW §0:**
  - GR:869 has lagged ch07:147 since **3fe27778** (2026-08-23), not 6adfff0e as FINDINGS says.
  - The BH-01 replay directory in `r11/replay-bh01` lacks `review/`; the review's full replay passes.
  - The fixed-m Page deficit is (m²−1)/(2mn); FINDINGS' m/(2n) is its large-m form.
- **Assumption-watch markers, recorded here and not in the manuscript:**
  - M6, A.7's V∖R purity step: made explicit, as part of H-decouple.
  - M12, GR A.5's coupling chain V↔B↔D uses B for the boundary layer, while Appendix A's B is the black-hole
    interior: record only, not edited.
- **Limits of this change.** It claims no OI–QM equivalence. No physical assumption is introduced beyond naming
  what A.8–A.9 already use, which is purity of B∪R over the evaporation.

## 6. Round 2: DIFF-REVIEW (`paper/r11/DIFF-REVIEW.md`, ACCEPT WITH CHANGES)

- **Base.** Applied uncommitted on top of 4c0d705e, using `bhfix/apply_edits2.py`: 9 exact-once replacements,
  with chapter edits mirrored into FULL.
- **Wording.** All text is the review's §7 wording, verbatim. No departures.

| Item | Site | Change |
|---|---|---|
| R1 | GR:811 | H-decouple redefined as the closure A.8 presupposes: B∪R is a closed system on which φ acts as a bijection of an energy shell Σ_E ⊂ H_B⊗H_R, with no coupling to D or V∖R, in a pure joint state. A.9's full-cycle averages use it over whole cycles of the dynamics, not only over the evaporation. This supersedes O-1a's state-only definition, "unentangled … over the evaporation". |
| R1 | GR:817 (paragraph after the A.7 proof) | "…pure, …, throughout the evaporation; that is H-decouple" → "Theorems A.8–A.9 take B∪R to be a closed system in a pure joint state on H_B(t)⊗H_R(t); that is the condition H-decouple." |
| R1 | ch07:130 +FULL | "which keeps the black hole and its radiation in an effectively pure joint state over the evaporation," → "which treats the black hole and its radiation as a closed system in a pure joint state," |
| R2 | GR:835 (H-scramble paragraph) | Adds the C6(a) consequence: H-scramble fails for every bijection in the setting of A.7's proof (a definite initial configuration with an aligned bipartition). It requires an initial superposition or a non-aligned bipartition; which one the substratum supplies is open. No remedy is adopted. |
| R2, R4 | ch07:126 s3 +FULL | "Applying it" → "Applying them". Adds "H-scramble therefore fails in that setting and requires an initial superposition of configurations or a bipartition not aligned with them; which of these the substratum supplies is open, and the condition is not established." |
| R3 | ch07:147 +FULL | "arrives at a Page curve" → "arrives at a cycle-averaged Page curve". "invokes the Popescu-Short-Winter theorem applied" → "applies Popescu-Short-Winter measure concentration". Now under H-scramble **and H-decouple**, "neither condition is established". This matches GR:869. |
| optional | GR:611 | "from Popescu-Short-Winter typicality [29] carried to the orbit" → "from measure concentration [29, 61] carried to the orbit" (matches GR:829) |
| optional | GR:869 | "applies Popescu-Short-Winter [29]" → "applies measure concentration [29, 61]" |
| optional | GR:605 | "Appendix A resolves the formal nested-partition machinery" → "develops" |

**Effect on the decision list (§2).**
- **O-1a** is settled by the review: H-decouple is the closure A.8 presupposes, which adds no assumption.
- **O-2:** the C6(a) consequence is now stated, per the review, which classes it as a fact. Only the *remedy* (a
  superposed initial state or a non-aligned bipartition) remains the owner's, and it is stated as open.
- **ch07:147** is no longer a survivor; §4's "Page curve" row note is superseded.
- **GR:605's "resolves"** is gone from the §4 survivors list, so the "resol" survivor count drops by one in
  GR only.

**Theorem A.8 on a proper energy shell: restriction applied in this change (§7); the shell version is open.**
- **The error.** Theorem A.8's value S_Page(d_B, d_R) does not hold in general when the energy shell is a proper
  subspace; it holds when the shell is the full product space H_B⊗H_R. The DIFF-REVIEW §6 settles this by exact algebra:
  - On the diagonal shell span{|i⟩|i⟩}, the Haar mean is H_m − 1. At m = 2 it is ½, against Page's 1/3 and
    the displayed ln 2 − ½.
  - On Hamming-weight shells BH-02 certifies values below S_Page (n=10, w=2: 1.60 against 2.97).
- **What inherits it.** The cycle-averaged A.9, the turnover at d_R = d_B, the min·ln q form, and every
  sufficiency statement "under H-scramble and H-decouple" (GR:869 last sentence, A.9's label, ch07:116, ch07:149,
  ch19:72).
- **Remedy applied (owner decision, 2026-10-26):** remedy 1, restricting A.8–A.9 to Σ_E = C_B × C_R, whose span
  is H_B⊗H_R, as an explicit hypothesis (§7). Remedy 2, using the Haar-on-shell mean and restating the turnover in
  shell terms, was not attempted. The shell-restricted version is stated as open in GR and the book.

**Introduction draft.** Left alone, as the coordinator instructed; it is handled separately.

**Round-2 build and checks.**
- **Builds.** `sh ./build.sh GR` gives 87 pages, median 3199 characters per page. `sh ./build.sh --book` gives
  554 pages, median 3074 characters per page. No dropped glyphs.
- **staleness_check:** GR and book stamps match their sources.
- **Checks, all OK:** mirror_check (0 lines absent), voice_check, claims_check, duplicate_check,
  dependency_label_check --strict, lean_manuscript_census.
- **coverage_check:** OK, 128 statements. The A.7 and A.9 statements are unchanged in round 2, so the
  fingerprints are unaffected.
- **Re-grep, all 0 hits** (papers + book, FULL included): "keeps the black hole", "throughout the
  evaporation", "arrives at a Page curve", "Applying it to the substratum".
- **Mirrors.** All 3 changed ch07 lines occur exactly once in FULL.

## 7. Owner decisions (2026-10-26) and the Theorem A.8 restriction

**Owner decisions on #936, 2026-10-26 (the owner's table, verbatim).**

| Decision | Recommendation |
|---|---|
| O-1 | Retain the named H-decouple condition |
| A.9 | State the time-averaged result, not pointwise typicality |
| O-2 | Leave the scrambling mechanism open |
| O-3 | Distinguish conservation from observable recovery |
| O-4 | Remove the empty falsifier |
| O-6 | Use "Preserved; Page curve conditional" |
- **Required before merge, verbatim:** "restrict Theorem A.8 to the domain where its Page-entropy expression is
  actually justified, or prove the appropriate energy-shell version. Do not leave the known mathematical error
  unresolved before release."
- **Option taken: the restriction.** No energy-shell proof was attempted.

**Applied with `bhfix/apply_edits3.py`.** It makes 22 exact-once replacements and one follow-up wording fix at
GR:611, with chapter edits mirrored into FULL.

| Site | Change |
|---|---|
| GR Thm A.8 (statement) | The theorem now assumes φ acts on B∪R with its whole configuration space as a single energy shell, Σ_E = C_B × C_R, whose span is the full product space H_B⊗H_R, and that H-scramble holds over the pure states of H_B⊗H_R. S_Page(d_B,d_R) is stated as the large-dimension form of Page's mean entropy for Haar-random pure states of H_B⊗H_R. |
| GR Thm A.8 (proof) | "restricts to a bijection on each energy shell, here on Σ_E = C_B × C_R"; the concentration step is for "Haar-random pure states of H_B⊗H_R". |
| GR H-scramble definition | "… over quantum pure states on the shell — in Theorem A.8, over the pure states of H_B⊗H_R — …" |
| GR, new paragraph after A.8's proof ("Proper energy shells.") | Measure concentration on a proper shell subspace concentrates about that subspace's own Haar mean, which depends on the shell and in general differs from S_Page. The paragraph gives the exact diagonal-shell example: mean H_m − 1, which is ½ at m = 2, against Page's 1/3. It notes that Hamming-weight shells can give values below S_Page. A.8 on a proper shell (with the shell's own Haar mean) and A.9 on such a shell are stated as open. Sources: BH-02 C6(c); DIFF-REVIEW §6; DIFF-RECHECK §5 N1, which keeps "fails in general", not "only when". |
| GR Thm A.9 (statement) | The stage-t bipartition is taken together with "the energy shell of Theorem A.8, the full configuration space of B ∪ R at that stage". |
| GR:811 (H-decouple) | "bijection of an energy shell Σ_E ⊂ H_B⊗H_R" → "bijection of its configuration space C_B × C_R (in Theorem A.8 a single energy shell, whose span is the full product space H_B⊗H_R)". Closure (no coupling to D or V∖R), purity, and the whole-cycles sentence are unchanged. |
| GR:605, :717 | The cycle-averaged Page curve is now qualified "taking the energy shell … to be their full product space" and "when the energy shell is the full product space". These are sufficiency surfaces added to the list per §A.25. |
| GR:611 | The Page value is now stated "when the energy shell of B ∪ R is the full product space H_B⊗H_R". "Cycle decomposition on the finite energy shell" → "of the finite configuration space". Adds: "On a proper energy shell the value differs in general, and the corresponding statement is open." |
| GR:869 (now :877) | The argument now applies concentration "on the full configuration space of B ∪ R"; "What the present derivation establishes" is now "with the full product space as the energy shell". |
| GR:871 (now :879) | "(PSW measure-concentration here …)" → "(measure concentration on the full product space, carried to the orbit by H-scramble, here; …)" |
| ch07:12, :116 +FULL | The cycle-averaged Page curve is qualified "taking the energy shell of the black hole and its radiation to be their full product space". These are sufficiency surfaces added per §A.25. |
| ch07:126 +FULL | New sentence: the results concern Haar-random states of the full product space; on a proper energy shell the mean entropy depends on the shell and in general differs from Page's value; the derivation takes the shell to be the full product space, and the energy-shell version is open ([GR Appendix A]). |
| ch07:130 +FULL | "… to the orbit of the bijection on the full product space of the black hole and its radiation …" |
| ch07:147 +FULL | "… substratum dynamics on the full product space of the black hole and its radiation …" |
| ch07:149 +FULL | "under H-scramble and H-decouple and with the full product space as the energy shell"; "the value on a proper energy shell" is added to the open steps. |
| ch19:72 +FULL | The dynamics is "on the full product space of the black hole and its radiation …; on a proper energy shell the value is open." |
| glossary:113 +FULL | "obtains a cycle-averaged Page curve on the full product space of black hole and radiation, under …" |
| appendix-a G11 +FULL | Formula "Nested trace-out, H-scramble, H-decouple; full product space"; status "Scrambling, decoupling, proper-shell value open". Class C is unchanged, so no count moves. |
| verification/coverage/LEDGER.json | A.8 fingerprint 17e40e97… → 31eafe29…; A.9 fingerprint ed567edf… → e3222fa7…, and its `line` 843 → 847. Both entries stay GAP, with no checks and delta "not formalized". |
| README.md (this directory) | "That error is left to a separate change" is corrected to state that the restriction is applied and the proper-shell version is open. |

**Left unchanged.** ch09:127, ch07:288, appendix-a:103 and book/README:64. These are necessity-form or
"conditional" status surfaces ("requires H-scramble and H-decouple", "conditional on …"); they assert no
sufficiency, and the restriction narrows scope without adding a condition they would understate.

**Re-grep** (papers/*.md and book/*.md, FULL separate).
- **"Σ_E"** (`\Sigma_E`): 6 lines, all in GR §A.7 (A.8's statement and proof, the H-scramble paragraph), where
  Σ_E is defined as C_B × C_R. FULL: 0.
- **`S_{\text{Page}}`:** GR:821, :825 (A.8's display and definition), :833 (the one-long-cycle example), :839
  (the bad-cycle step, ×2), and :845 (the proper-shells paragraph, ×3). All are inside A.8, its proof, or the
  restriction paragraph. FULL: 0.
- **"Page's average":** 0.
- **"energy shell":** 20 non-FULL lines, 7 in FULL.
  - New scope qualifiers and open-shell statements: GR:605, :611, :717, :811, :819, :829, :845, :847, :877;
    ch07:12, :116, :126, :149; ch19:72.
  - Mechanism descriptions that remain accurate when the shell is the full space: ch18:148 and ch19:72,
    "cycle typicality on the energy shell rather than replica wormhole computation"; and GR:877 / ch07:147,
    the conjectured "cycle structure on the energy shell" correspondence.
  - Unrelated: GR:58 (horizon temperature); SM:292, :294, :795.
- **"full product space":** 17 non-FULL lines, 9 in FULL. Every one is a new scope qualifier.

**Round-3 build and checks.**
- **Builds.** `sh ./build.sh GR` gives 87 pages, median 3200 characters per page. `sh ./build.sh --book` gives
  554 pages, median 3076 characters per page. No dropped glyphs. `staleness_check` OK: GR and book stamps match
  their sources.
- **coverage_check.** Countercontrol first: with the old fingerprints it FAILs, "STALE entry GR:T-a.8
  (17e40e97… → 31eafe29…)" and "STALE entry GR:T-a.9 (ed567edf… → e3222fa7…)". With the new fingerprints it is
  OK (128 canonical statements).
- **All OK:** mirror_check (0 chapter lines absent; all 9 changed chapter lines occur exactly once in FULL),
  voice_check, claims_check, duplicate_check, dependency_label_check --strict, lean_manuscript_census,
  architecture_check (259 invariants), citation_check.
