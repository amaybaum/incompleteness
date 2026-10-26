# Independent review: introductory-paper design (PR #918, paper-design stage)

- **Objects reviewed:** `S/paper/design/OUTLINE.md`, `CONTRIBUTION.md`, `SOURCES.md`,
  `probe/examples.py` (S = this session's scratchpad).
- **Checked against:** `main` `687e885b1cfd24d6f17eee439101afc8acf07015` (worktree
  `S/paper/mainwt`, clean); AUDIT r4 at branch head `1e9c05c7` (`S/pintro/repo/...`); the black-hole
  packages and review records on `main`; `S/paper/explainer/REVIEW.md`.
- **Read-only.** No repository file changed, nothing committed or posted. Every git command ran with
  `-c gc.auto=0 -c maintenance.auto=false`. Scratch outputs here: `run/` (probe run), `vc/` (voice
  check on the draft paragraph), `bridge-687e885b.log` (CI job log, read through the API, sha256
  `e20abaee6061de73cd5a98749b0040abc999bff0acbf70db26f78b67d27a5251`).

## Verdict: ACCEPT WITH CHANGES

The design is careful and mostly faithful. Every one of the 47 Lean declarations it names exists at
the cited module:line with the quoted statement. Two are mislocated in SOURCES (nit N1). The E1 and
E3/E4 witness tables are right direction by direction. The novelty classes match AUDIT r4 for every
C-item. The probe runs and prints what SOURCES says. The black-hole section uses only ACCEPT-closed
packages and states item F at the package's strength.

Eight changes are required (R-1 to R-8 below). Two of them are claim/evidence-boundary defects in
text meant for the paper:
- the contribution paragraph's "each independent of embedded observation, none supplied by it";
- §6-b's headline clause, attributed to kernel declarations that do not state it.

AGENTS.md's Code Review Rules make such defects blockers for manuscript text. At the design stage,
each has an exact fix, so the verdict is conditional acceptance: the design is accepted once R-1 to
R-8 are applied. Without them it should not go to drafting.

Coverage: 47 kernel declarations checked, all of them at their cited line, plus about 60 Main
lines, 12 GR lines, 14 ch07 lines and about 35 BH-01/BH-02 report and review lines. Every spot
check other than those in the findings matched its source.

***

## Findings

### F1 — The contribution paragraph overstates independence and makes "not supplied" a settled fact (required)

`CONTRIBUTION.md:33–34` reads: "exact finite operational quantum mechanics (characterized under
five completion conditions, each independent of embedded observation, none supplied by it)".

The kernel does not support "each independent of embedded observation".
- `five_way_minimality` (`RankGapTheory.lean:702`) is five existentials over
  `FiniteOperationalTheory (Fin 2)`.
- Each witness satisfies `RealizesSealedOICore`, which is defined only on `Fin 2`
  (`OIRealization.lean:234`). It is one fixed sealed C1–C4 core process.
- So the independence is shown on the qubit, against that one core. It is not shown against
  embedded observation in general.

"None supplied by it" contradicts the sources and the design itself.
- Main:562 and GR:226 say "none supplied by **bare finite** OI". Both leave "the physical question
  of which conditions the substratum supplies" open (GR:228, "whether the OI substratum supplies
  (iii)–(v)").
- The outline lists that same question as open (§8-a, `OUTLINE.md:193`).

The paragraph drops "bare finite" and so asserts as settled what §8-a calls open.
- Kind of overclaim: witness → theorem, and open → settled.
- `CONTRIBUTION.md:61–62` and `:111–112` are worded correctly ("bare finite OI").

### F2 — §6-d leaves out the qubit scope of independence (required)

`OUTLINE.md:158` reads: "each of (i)–(v) is independent of the others and of the C1–C4 process".
The kernel scope is the qubit and one sealed core (see F1). GR:220 says so: "for each condition
there is a qubit theory that realizes the sealed OI core".

The characterization E2 is carrier-general (`exactAll_iff_physical_general`). The independence and
`oi_alone_not_qm` are qubit statements (`GeneralCarrier.lean:160`, `∃ T : FiniteOperationalTheory
(Fin 2)`). The paper must keep the two apart.

### F3 — The §6-b headline clause is not stated by the cited kernel declarations, and UNTRACED-1 can be traced (required)

`OUTLINE.md:156` carries "one visible family admits coherent unitary lifts whose relating
evolutions differ", with layer "kernel (carried clauses)". It cites:
- `bridge_traj` (TrackBQfbBridge:276);
- `rooted_eq_iff_slice_eq` (:180);
- `realData_traj_stochastic` (:286);
- `padData_rooted` (OperationalSourcing:476).

These state:
- trajectory laws are fixed by the visible slice;
- rooted families are equal exactly when slices are equal;
- the laws are stochastic;
- padding invariance.

None of them states that the relating evolution is not unique. Main:624 names kernel identifiers
only for the fixed-basis-datum sentence.

The nonuniqueness clause does have a kernel witness. Main does not name it at the site, but the
census family "the coherent-lift stabilizer no-go (act 11, Track B)" anchors it to Main ("
representability, not selection of the relating evolution"):
- `gl2_strong_gauge_moves_relative_candidate` (`CoherentLiftGauge.lean:537`) gives two coherent
  lifts of one visible family, related by a time-dependent strong-class element, with different
  relative candidates.
- `gl3_constant_gauge_preserves_relative` (`CoherentLiftGauge.lean:451`) covers "a constant
  deformation cancels".
- Both report only the three standard axioms in the 687e885b bridge log (see F9).

UNTRACED-1, the fibre-Gram classification at `SOURCES.md:157–166`, can also be traced.
- The census family "the two-sided invisible gauge and the fibre-Gram classification (act 12,
  Track B)" maps `OIBridge/TwoSidedGauge.lean` to the Main anchors "The uniformly invisible
  deformations of a lift are two-sided" and "the fibre-Gram data — agrees up to the anchored
  phases".
- The module has `gramPhaseEquiv_of_twoSided` (TG2 forward, :263) and `sh1_necessity` (:168), with
  further TG2/SH1 directions.
- The pass searched only `CrossTimeInvariants.lean`. "Not located" is therefore a search gap, not
  an absence. It can stay not carried, but the reason should be "not yet checked direction by
  direction", not "not located".

### F4 — The E2 sufficiency chain cites the conditional lemma (required)

`OUTLINE.md:49` lists, under the ← witness: "via `krausSoundExt_of_validity_inert`,
`compositeCompleteness` (AncillaClosure:373), `exactAll_of_levelOne`".

`compositeCompleteness` takes the hypothesis `hext : ∀ k, FiniteIsometryExtensionSF (A × Fin
(k+1))` (`AncillaClosure.lean:373–378`). The proof `exactAll_of_physical_general` actually goes
through:
- `compositeCompleteness_unconditional` (`IsometryExtension.lean:179`), called from
  `GeneralCarrier.lean:84`;
- that lemma discharges `hext` by `finiteIsometryExtensionSF_discharged`.

GR:218 names both. The witness itself, `exactAll_of_physical_general` (GeneralCarrier:93), is
right, but a reader following the "via" list meets an apparent premise that the paper says is
absent.

### F5 — Two originality labels in CONTRIBUTION have no source, and one in OUTLINE/SOURCES is the design's own (required)

AUDIT r4 does not classify the BH-01/BH-02 findings.
- C16-S is "not classified".
- "#917's landed records … were not read" (AUDIT:1395–1402).

The outline therefore correctly gives §7-c (`OUTLINE.md:173`) and §7-h (`:178`) as "not classified".
CONTRIBUTION does not keep that.
- **`CONTRIBUTION.md:94`** puts §7-c and §7-d together as "covered in kind (the package itself
  labels C2 and C4 classical forms of known facts)". The package's self-label covers C2 and C4,
  which belong to §7-d (BH01 REPORT:110–112, :131–132, :253). Claim A (§7-c) is labelled
  CONFIRMING, which is an §A.31 output class and not an originality class (REPORT:251).
- **`CONTRIBUTION.md:97`** puts §7-g and §7-h together as "covered in kind (elementary)". Neither
  AUDIT r4 nor BH-02 gives such a label: BH-02's REPORT has no originality self-classification.
- **`OUTLINE.md:177` and `SOURCES.md:138`** give §7-g as "known in kind (elementary)". This is the
  design's own judgment, presented in the originality column.

The owner asked for classes that match AUDIT r4 exactly. These do not.

### F6 — R11: FULL.md mirrors left out, and the Alt-L "safe form" does not remove the conflict (required)

`SOURCES.md:247` lists the live sites ch07:110, ch07:159–161 and GR:811. It omits their verbatim
mirrors, which carry the same text at `687e885b`:
- `book/The-Incompleteness-of-Observation-FULL.md:1987` ("resolves the paradox at the structural
  level … because φ is bijective");
- `FULL.md:2036–2038` (the falsification framing).

BH01 MANUSCRIPT-AUDIT:9–11 itself says each book paragraph is mirrored in FULL and that any change
lands in both (§A.14, §A.25).

R11 also gives the owner two options: "correct those sites first, or keep §7 to statements that do
not contradict them (Alt-L)". The second option does not hold.
- Alt-L keeps §7-c, claim A (`OUTLINE.md:243`). MANUSCRIPT-AUDIT:60–61 finds that claim A
  "**contradicts**" ch07:110's resolution sentence.
- Alt-L removes only the GR:811 conflict, by dropping §7-f.
- No scope that carries §7-c avoids the ch07:110/FULL:1987 conflict. Only correcting those sites
  does, or dropping claim A.

The statement of item F itself is faithful. §7-f (`OUTLINE.md:176`) and non-claim 6
(`CONTRIBUTION.md:128–129`) say "stated support … reversed". They carry the package's three "does
not show" limits (BH01 REPORT:237–245) and nothing stronger. It says "reversed by at least 10^57",
where REPORT:228 gives `t_evap/τ_B^D ≥ 1.785×10^57`.

### F7 — The Page-time conditions are incomplete (required)

- §7-i (`OUTLINE.md:179`) and non-claim 6 (`CONTRIBUTION.md:125`, "conditional on β = 1") omit the
  constant-coefficient condition.
- BH-04's reviewed verdict is CONDITIONAL on three inputs: a constant coefficient in
  `dM/dt = −α/M²`, β = 1, and `S_BH ∝ M²` (BH02 REPORT:22, :118–121).
- It also records a counterexample to the unconditional reading: an M-dependent coefficient (species
  thresholds) moves the fraction, to 0.7027 for the power law p = 1/2 and up to 0.8707 in the step
  model (REPORT:22, :123–127).
- ch07:137 states the constant coefficient as a premise, but the paper must carry it as a
  condition.
- In §7-f, "t_P/τ_B^D ≥ 1.153×10^57" holds for t_P at β = 1 (REPORT:231, as amended after review).

### F8 — The non-claims list is incomplete (required)

The owner's list asks for ε-gluing not stated as "unconditional", and for F13 and F14–F18 not
carried. CONTRIBUTION (c) (`:101–135`) has F13 (item 8). It lacks:
- **ε-gluing.** Item 2 says the ε-theorems "are not uniqueness theorems". It does not say the paper
  neither relies on them nor repeats Main:580(4)'s "proved unconditionally" (F7 open, no kernel
  anchor). OUTLINE §6-f and R15 have this; the non-claims list should too.
- **Main's descriptions of Calvo, Pimenta and Doukas (F14–F16), the [11]/[12] swap (F17), the
  Born-equilibrium sentence (F18) and the stale [24] (F19).** They are in OUTLINE §9
  (`:221–224`) and R14, not in the contribution statement.
- **F3's open remark** "U_φ = e^{−iĤ} … fixed autonomous generator" (Main:532, AUDIT F3 "open").
  §3-d cites Main:532 without excluding it.

### F9 — R6: main's CI does report axioms for every cited declaration; the remaining gap is retention under §A.42 (resolves part of R6)

- Run `40291389159` was a `push` to `main` at `687e885b` (2026-10-26T08:18Z). Its required job
  `Mathlib bridge` (job `121467032075`) concluded success.
- It runs the real `tools/release_gate.py`. Its step `lean-axioms` (`tools/lean_axiom_check.py
  --require-lake`) did a `lake build` of the default target. That target imports every OIBridge
  module, including all 23 modules the design cites (`OIBridge.lean`).
- The step requires every `#print axioms` report to lie within `propext`, `Classical.choice` and
  `Quot.sound`, with no `sorryAx` and no missing report. The gate block reads "PASS lean-axioms
  lean_axiom_check: OK (6082 named result(s) reported …)" and "release gate: PASS".
- Every cited declaration has a `#print axioms` line in source. Each has its report in the log with
  exactly the three standard axioms. Examples:
  - `OIBridge.Equivalence.finite_horizon_equivalence`;
  - `OIBridge.GeneralCarrier.exactAll_iff_physical_general`;
  - `OIBridge.RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap`;
  - `OIBridge.PhysicalC4Discharge.routed_forces_indivisible_somewhere`;
  - `OIBridge.RootedClassification.finiteRootedRealizable_iff_pper`;
  - `OIBridge.CoherentLiftGauge.gl2_strong_gauge_moves_relative_candidate`.
- So `SOURCES.md:40` ("No Lean build was run, and no axiom report was observed, in the audit or
  here") and UNTRACED-4 ("not inspected here", `:173–175`) are out of date. The build and axiom
  report exist at the drafting commit.

What remains is §A.42.
- The job log expires, and a run id is not retention.
- Before the paper (an enduring claim on `main`) says "machine-checked", one of two things must
  happen:
  - an expected result, the structured file §A.42 item 1 describes, is retained beside the paper
    and holds at the drafting commit; it records build success, the release-gate verdict and the
    `#print axioms` report of each cited declaration, and names its recipe and the run/job/log
    digest as provenance;
  - or the paper's commit falls inside an archive the `evidence-retention` step already covers.
- Until then, "machine-checked" in the paper should name the commit and the recipe
  (`lake build` + `tools/lean_axiom_check.py`). It should not cite the run.

### F10 — R17 is correct; extend it

- AUDIT r4 sits only on `draft/oi-introductory-paper-20261025`. `1e9c05c7` is not an object in the
  `main` worktree's store.
- The two literature studies are in scratch only. Their hashes re-verify:
  - `005cfe94…1c26`;
  - `c7475d09…ce0d`.

R17 should add the following:
- The literature studies' own reviews (`S/introaudit/revlitbh/`, `revlitcorr/`) are also scratch
  only. AUDIT:134–145 rests on them.
- The AUDIT text relied on (`AUDIT.md`, sha256 `eacbdd56…22ad`) is r4 with Rc4's nits applied.
  Rc4 reviewed `AUDIT-r4-prerecheck.md` (sha256 `b8967887…a781`). The applied text was not itself
  re-checked. `OUTLINE.md:13–14` ("as re-checked") should say "r4 with Rc4's nits applied".
- §A.42's consequence for a paper: the attributions themselves (for example "RHP 2014 Eq. (15)")
  can be checked against the literature. The design decisions (which classes, which sentences are
  barred) are governed decisions, and they rest on scratch until the audit and studies are landed
  or retained.

### F11 — Missed risk: GR's displayed "OI-compatible + (i)–(v) ⟺ QM" box has no kernel converse beyond the qubit (owner flag)

- GR:226 displays "OI-compatible operational theory + (i)–(v) ⟺ finite operational QM … for every
  nonempty finite system (kernel: `main_result`, `oi_compatible_classification`)".
- `oi_compatible_classification` (`GeneralCarrier.lean:168`) and `RealizesSealedOICore` are typed
  on `Fin 2` only. `main_result` clause (i) is carrier-general but has no OI clause.
- So the ⟸ direction with the OI conjunct ("QM ⇒ OI-compatible") has a kernel witness only on the
  qubit (`realizesSealedOICore_of_control`). That is a §A.34 scope question in GR.
- The outline displays E2 without the OI conjunct, which is correct. It should add GR:226's box to
  "Not to be displayed", and flag GR:226 to the owner for a separate §A.25/§A.34 check.

### F12 — Missed risk: the census and gate consequences of a new manuscript are wider than question (b)

- `verification/lean-manuscript-census.json` has an explicit `manuscripts` list.
- Kernel citations from families with `manuscript: []` would make those families carried, so each
  needs an anchor (§A.35). That covers:
  - §5-c `RecurrenceHorizon`;
  - §5-e `routed_forces_indivisible_somewhere`, whose family "physical C4 discharge…" has
    `manuscript: []`;
  - Alt-X's `RootedClassification`.
- Question (b) (`SOURCES.md:207–208`) names only §5-c. It should cover all three.

### F13 — The page budget mostly adds up, but three items are off (owner decision)

- The arithmetic holds: body 13.25 pp, total 14.25 pp. Alt-X adds +0.75, giving 15.0.
- Appendix A at 0.5 pp (`OUTLINE.md:231–235`) promises "one row per claim". That is about 55 rows,
  plausible only at about 1.5 pp. Either restrict it to the kernel-backed claims (about 15 rows)
  or budget 1.0–1.5 pp.
- The page format (single- or two-column, words per page) is not stated. Without it, "12–15 pp"
  cannot be checked. §6 at 1.75 pp, with E2, the five conditions defined, §6-b, §6-e and §6-f, is
  the tightest section.
- Alt-L (`OUTLINE.md:243`) drops §7-g but keeps §7-h. §7-h's proof is "from §7-g" (`:178`; BH02
  C6(a) is "PROVED (from C1)"). Keep §7-g as one sentence.
- SOURCES' Alt-L ("BH-01 A and C2 plus the conditional Page time and H-scramble's role",
  `:196–197`) also differs from OUTLINE's (§7-b, §7-c, §7-d, §7-h, §7-i). Align them.
- The trade-offs are otherwise stated fairly. The recommendation does not oversell the
  recommended scope, and the Alt-X additions are correctly marked as new manuscript content or
  candidate.

### F14 — The probe does what SOURCES says, with two caveats (nit)

`python3 -I probe/examples.py` exits 0 and prints:
- T(1,0) = [[2/3, 1/3], [1/3, 2/3]];
- T(2,0) = I;
- Λ = [[2, −1], [−1, 2]];
- 1 against 1/3;
- the XOR two-time kernels all ½J;
- I = 1.0 bit, with the i.i.d. control at 0.0.

This matches `SOURCES.md:106, :110`. The caveats:
- **The CMI is computed in floating point** (`math.log2`); only the matrices are exact. The exact
  value is trivial here, since every probability is a power of 2. The record should say "float",
  or compute it exactly. The repository's own evidence is `review4_probes.py`.
- **P(x₂=0 | x₁=1) = 1/3 depends on the uniform x₀ prior the probe assumes.** By hand it is a/(2−a)
  for P(x₀=0) = a. Main:194 does not state the x₀ law, so the paper must.

The Λ order comment is right: Main writes T(2,0)·T(1,0)⁻¹, and with T(2,0) = I the two orders
agree.

### F15 — Checks that passed, recorded briefly

- **§A.34.**
  - E1's six directions are discharged by the three constructions with no hypotheses
    (`Equivalence.lean:462–468`).
  - E3 (`RootedClassificationAllTime:192`, → `RootedClassification:339`, ← `:162`) and E4
    (`CarrierGeneralOIPlus:213`, → :191, ← :198) are right.
  - Every non-kernel biconditional is moved to prose: §4-b, (ii) ⟺ (iii), C8-D, Main:610.
- **Novelty.**
  - C1, C1′ and C4 are PARTLY KNOWN; C2, C7, C8, C16a, C16b and XOR are KNOWN; C3, C9–C12 and C14
    are REFRAMING. These match AUDIT:1943–1953 and the PROVISIONAL marks.
  - C4-old and C16d are WITHDRAWN and kept out.
  - C8-R is NOVEL-CANDIDATE, Alt-X only, with no priority sentence (AUDIT:1032–1036,
    :2018–2029).
  - XOR is attributed to RHP 2014 Eq. (15) with no first-statement claim (AUDIT:1512–1525).
  - Correctness and originality are kept in separate columns throughout.
- **Black-hole review chain.**
  - BH-01 closed with "**ACCEPT at df2ea6f5…**" (`RECHECK-df2ea6f5.md:1`).
  - BH-02/BH-04 closed with "ACCEPT — ce7937d2…" (REVIEW.md:279; its parent is `ee2d4e68`, not
    `1f1aec6f`).
  - Both are ancestors of `687e885b`. Since review, the changes outside `review/` are wording, the
    replay recipe and the SHA256SUMS (diff checked).
  - BH-02 C6(c) (A1 disclosure) and C3 (NUMERICAL, supplied) are correctly kept out or flagged
    (R20).
- **Register.**
  - `tools/voice_check.py` on the draft paragraph: OK.
  - Manual pass: no self-assessment, no "first", no novelty sentence, no reader instruction, no
    capitals for emphasis.
- **Line stability.** `git diff 52e2db40 687e885b` changes Main only at the 519 and 607 hunks
  (:522, :610) and GR only at one line, as stated.

***

## Required changes (exact)

- **R-1 (F1).** In `CONTRIBUTION.md:33–34`, replace "each independent of embedded observation, none
  supplied by it" with: "each independent of the other four and of one finite C1–C4 observation
  process, by qubit countermodels, and none implied by bare finite OI; which of them a physical
  substratum supplies is open".
- **R-2 (F2).** In `OUTLINE.md:158`, replace "each of (i)–(v) is independent of the others and of the
  C1–C4 process" with: "on the qubit, each of (i)–(v) is independent of the other four and of the
  sealed C1–C4 core (`five_way_minimality`, `Fin 2`)". Add: "`oi_alone_not_qm` is a qubit
  countermodel; E2 itself is carrier-general".
- **R-3 (F3).**
  - In §6-b (`OUTLINE.md:156`; `SOURCES.md:120`), add `gl2_strong_gauge_moves_relative_candidate`
    (CoherentLiftGauge:537) as the witness for "relating evolutions differ" and
    `gl3_constant_gauge_preserves_relative` (:451) for "a constant deformation cancels". Otherwise
    mark that clause prose.
  - Rewrite UNTRACED-1's first bullet (`SOURCES.md:164–166`) to point to
    `OIBridge/TwoSidedGauge.lean` and its census family (act 12) as "not yet checked direction by
    direction".
- **R-4 (F4).** In `OUTLINE.md:49` (and `SOURCES.md:122`), replace "`compositeCompleteness`
  (AncillaClosure:373)" with "`compositeCompleteness_unconditional` (IsometryExtension:179), the
  conditional `compositeCompleteness` (AncillaClosure:373) with its extension premise discharged by
  `finiteIsometryExtensionSF_discharged`".
- **R-5 (F5).**
  - `CONTRIBUTION.md:94`: split into two rows. §7-c becomes "unverified: not classified (C16-S;
    AUDIT r4 did not read the #917 records, AUDIT:1397–1398)". §7-d becomes "covered in kind, per
    the package's own description of C2 and C4 (BH01 REPORT:110–112, :131–132); not
    literature-mapped".
  - `CONTRIBUTION.md:97`, `OUTLINE.md:177` and `SOURCES.md:138`: replace the §7-g/§7-h originality
    with "not classified (no literature examined)".
- **R-6 (F6).**
  - In R11 (`SOURCES.md:247`), add `FULL.md:1987` and `FULL.md:2036–2038` to the live sites.
  - Replace the safe form with: "owner choice: correct ch07:110, ch07:159–161, GR:811 and their FULL
    mirrors first, or drop §7-c and §7-f. Alt-L as defined still carries §7-c, which contradicts
    ch07:110/FULL:1987 (BH01 MANUSCRIPT-AUDIT:56–60)".
  - Mirror this in Decision 1(a) (`SOURCES.md:205–206`).
- **R-7 (F7).**
  - In §7-i (`OUTLINE.md:179`), add: "conditional on a constant coefficient in dM/dt = −α/M², β
    and S_BH ∝ M²; an M-dependent coefficient moves the fraction (BH02 REPORT:22, :123–127)".
  - In `CONTRIBUTION.md:125`, replace "conditional on β = 1" with "conditional on β = 1, a constant
    mass-loss coefficient and S_BH ∝ M²".
  - In §7-f (`OUTLINE.md:176`), write "t_P/τ_B^D ≥ 1.153×10^57 (t_P at β = 1)".
- **R-8 (F8).** Add three items to `CONTRIBUTION.md` (c):
  - "9. No conclusion rests on the ε-realization and gluing theorems, and they are not described as
    proved unconditionally (F7; Main:580(4) has no kernel anchor)."
  - "10. Main's descriptions of Calvo, Pimenta and Doukas, its [11]/[12] assignment, its
    Born-equilibrium sentence and its [24] are not carried (F14–F19); related work is written from
    the full-text studies."
  - "11. The 'fixed autonomous generator' remark of Main:532 is not carried (F3 open)."

## Owner decisions (in addition to SOURCES' Decisions 1 and 2)

1. **"Machine-checked" (F9).** Retain an expected result for the `687e885b` bridge build, or for
   the drafting commit, beside the paper's evidence before the paper lands, or accept the wording
   "kernel-checked at commit X by recipe Y" without the term "machine-checked".
2. **Provenance (F10).** Land or retain AUDIT r4 (as applied), the two literature studies and their
   reviews on `main` before any paper sentence relies on a class. The alternative is to state that
   the classes are design inputs only.
3. **GR:226's box (F11).** Commission a separate §A.34/§A.25 check of the OI-conjunct direction
   beyond the qubit. The paper does not need it, but it should not cite the box.
4. **Census (F12).** Accept that the paper's commit registers `papers/<name>.md` in the census
   `manuscripts` list and adds anchors for the RecurrenceHorizon, PhysicalC4Discharge and (Alt-X)
   RootedClassification families. The alternative is to cite those results as prose plus probe.
5. **Page format (F13).** State the target format, and choose Appendix A's scope: kernel rows only,
   at 0.5 pp, or the full map, at about 1.5 pp.

## Nits

- **N1.** `SOURCES.md:122`: "also `main_result` (:188), `oi_compatible_classification` (:168)"
  reads as OIRealization lines. Both are in `GeneralCarrier.lean`, at :188 and :168.
- **N2.** §7-a cites GR:719, which is the heading "### A.1 Setup". The nested partition is at
  GR:721.
- **N3.** E2 wording (`OUTLINE.md:49`): "the available families **on the system and** at every
  positive ancilla level" (GR:218; `ExactAllFiniteEndomorphicQuantumOps`).
- **N4.** `CONTRIBUTION.md:28`: "carries **at least** the visible predictive information", as
  AUDIT:1983–2016 has it (M_t ≤ I(X_<t;H_t|X_t)).
- **N5.** `CONTRIBUTION.md:36–37`: non-necessity is witnessed by non-injective maps, so "in finite
  reversible models" mis-scopes it. Use "in finite toy access models".
- **N6.** `CONTRIBUTION.md:134`, §5-f: "the XOR example is, up to flipping the final bit, RHP 2014
  Eq. (15)" (Main:606; AUDIT:1512–1514).
- **N7.** §7-c: "zero accessible advantage requires |K| ≥ |M| **in a bijective instance**". C2 is a
  bijective statement; 32 non-injective maps violate the bound (BH01 REPORT:21).
- **N8.** §7-f: disclose that the Γ and τ_B^D intervals were chosen after the plan, and that the
  margin makes the conclusion insensitive to them (BH01 REPORT:234–235).
- **N9.** Decision 2's list of Explainer dependents (`SOURCES.md:220–226`) is incomplete.
  `verification/README.md` has 15 references, `FULL.md` 1 and `book/bibliography.md` 1, and some
  frozen records also have references (`errata.json`, `certificates/A12P.json`). Frozen records
  are not correction targets.
- **N10.** `SOURCES.md:44–45`: BH-02's final ACCEPT at `ce7937d2` has parent `ee2d4e68`
  (REVIEW.md:279).
