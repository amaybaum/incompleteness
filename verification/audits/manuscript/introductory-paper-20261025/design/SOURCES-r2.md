# Introductory paper: source map, owner decisions and risks — revision 2 (design stage)

This revision applies `paper/review/REVIEW.md`. `SOURCES.md` is kept unchanged as the reviewed
object, and `CHANGES-r2.md` lists the changes. Every claim the outline would carry is mapped to:
- its exact source file:line at `main` `687e885b1cfd24d6f17eee439101afc8acf07015`;
- its kernel declaration;
- its verification layer and its correctness status;
- its originality class (AUDIT r4) and that class's evidence basis.

A claim with no source is listed under UNTRACED and is not carried.

## Provenance and path keys

- **Repository paths.** Read at `687e885b` in the worktree `S/paper/mainwt`, clean at HEAD
  `687e885b`. Git commands ran with `-c gc.auto=0 -c maintenance.auto=false`.
  - `Main:` = `papers/Main.md`; `GR:` = `papers/GR.md`; `ch07:` = `book/ch07-gravity.md`;
    `FULL:` = `book/The-Incompleteness-of-Observation-FULL.md`.
  - `OIBridge/X.lean:N` = `verification/lean-mathlib/OIBridge/X.lean`, line N.
  - `BH01/F:N` and `BH02/F:N` = the files under
    `verification/programmes/black-hole-information/bh01_access_v1/` and `bh02_scramble_v1/`.
- **Line stability.** `git diff 52e2db40 687e885b` changes:
  - Main only at :522 and :610 (#932, one line for one);
  - GR at :20, glossary at :39, plus FULL;
  - ch18:114;
  - the new directory `verification/audits/manuscript/f29-witness-quantifier/`.
- **AUDIT** = `verification/audits/manuscript/introductory-paper-20261025/novelty-v5/AUDIT.md` on
  branch `draft/oi-introductory-paper-20261025` at `1e9c05c7`, which is not on `main`.
  - Its status is "work-in-progress evidence record" (that directory's README.md:31–37).
  - The text relied on (sha256 `eacbdd56…22ad`, re-verified) is r4 with the nits of its re-check
    Rc4 applied. Rc4 reviewed `AUDIT-r4-prerecheck.md` (sha256 `b8967887…a781`, re-verified). The
    applied text was not itself re-checked.
  - AUDIT cites two literature studies by sha256. Both exist only in session scratch, and both
    hashes were re-verified:
    - `S/introaudit/lit-correspondence/LITERATURE-v2.md`, sha256 `005cfe94…1c26`;
    - `S/introaudit/lit-blackhole/LITERATURE-v2.md`, sha256 `c7475d09…ce0d`.
  - Their reviews, on which AUDIT:134–145 rests, are also scratch only: `S/revlitcorr/` and
    `S/revlitbh/`.
- **Kernel.**
  - Static criterion, as AUDIT §0.3 defines it (AUDIT:270–280): the declaration exists, its proof
    has no `sorry`, `admit` or `native_decide`, and its module declares no `axiom`. Re-checked here
    with zero hits.
  - **Build and axiom report observed at `687e885b` (review F9).** The push run on `main`, run
    `40291389159`, job `121467032075` ("Mathlib bridge"), concluded success.
    - The job's log, as read by the reviewer, is `S/paper/review/bridge-687e885b.log`, sha256
      `e20abaee6061de73cd5a98749b0040abc999bff0acbf70db26f78b67d27a5251` (re-verified).
    - At line 38887 it reads "PASS lean-axioms lean_axiom_check: OK (6082 named result(s)
      reported, …)", and at line 38895 "release gate: PASS".
    - Spot-checked here: the axiom reports of `finite_horizon_equivalence`,
      `exactAll_iff_physical_general`, `unavoidable_hidden_predictive_memory`,
      `pIndivisible_of_rooted_identity_return_of_overlap` and
      `gl2_strong_gauge_moves_relative_candidate`. Each lists `propext`, `Classical.choice` and
      `Quot.sound` only. The reviewer reports the same for every cited declaration.
  - **This is provenance, not retention.** A run id does not retain anything, and the log expires.
    §A.42 item 1 requires an expected result retained on `main` before the paper can say
    "machine-checked". That file records build success, the gate verdict and each cited
    declaration's `#print axioms` report, and names its recipe and the run, job and log digest as
    provenance. The alternative is that the paper's commit falls inside an archive the
    `evidence-retention` step covers. This is decision 2.
- **Black-hole "reviewed"** means a separate-agent internal review that closes with ACCEPT.
  - BH-01 (`BH01/review/README.md:5–11`):
    - BLOCK, on wording, at `587d4196`;
    - ACCEPT WITH NITS at `95458016`;
    - ACCEPT at `df2ea6f5` (opening line of `RECHECK-df2ea6f5.md`).
  - BH-02/BH-04 (`BH02/review/README.md:3–7`):
    - ACCEPT WITH NITS at `1739f4e0` (REVIEW.md:1) and at `91e2230a` (:188);
    - ACCEPT at `1f1aec6f` (:252) and at `ce7937d2` (:279). The parent of `ce7937d2` is
      `ee2d4e68`.
  - Both closing heads are ancestors of `687e885b`. Since review, the changes outside `review/` are
    wording, the replay recipe and SHA256SUMS.
  - These reviews are not external validation or owner adoption (`BH01/review/README.md:3`;
    PROGRAMME.md:3).
- **Layers.** Kernel; exact computation; numerical; prose proof; literature; definition.
- **Originality.** Classes follow AUDIT §0.4 (AUDIT:282–319), with evidence basis and PROVISIONAL
  marks where AUDIT gives them. A source package's own description is used only where it is
  stated, and is cited as such. No originality entry is this design's own judgment.

## Claim register

### §1–§2 Hypothesis, setting, definitions

| ID | Claim | Source @687e885b | Kernel | Layer | Correctness | Originality (AUDIT r4) |
|---|---|---|---|---|---|---|
| §1-a | OI hypothesis; the physical identification is a representation choice; the theorems are mathematical; no ontology-level falsifier is established | Main:28, :62, :702, :704 | — | prose | statement of hypothesis | not classified ((e); AUDIT:1409–1460). Positioning against 't Hooft 2016 and Spekkens 2007 is pending (NR; AUDIT:1452–1460) |
| §1-b | The question the reduction poses | Main:28 | — | prose | — | n/a |
| §1-c | Scope: exact at the finite observable-law level; operational completion is a separate question | Main:22, :534, :622, :758 | — | prose | — | n/a |
| §1-d | Incompleteness is not the uncertainty relations | Main:28, :572 | (Main:572 cites `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`, `finite_horizon_equivalence`) | prose | — | not classified |
| §2-a | Observation $(S,\varphi,V)$; finite visible space | Main:44, :48 | — | definition | — | n/a |
| §2-b | The bijective representative is a reconstruction choice; total finiteness is a posit | Main:56, :62, :708 (ii) | — | prose | — | n/a |
| §2-c | The prior is part of the realization datum; invariance does not select the measure | Main:60, :86 | `invariance_does_not_select` (CanonicalMeasure:242) | kernel (measure); definition | kernel | not classified ((e); AUDIT:1416–1423) |
| §2-d | The classes $S$, $D$, $Q_{\mathrm{fb}}$ | Main:98–99, :526–530 | `Stochastic` (Equivalence:147), `RevReal`/`RevRealizable` (:157/:182), `QfbReal`/`QfbRealizable` (:190/:216) | kernel definitions | — | n/a |
| §2-e | C1–C4 are diagnostics | Main:72, :74, :76, :78, :80, :596 | — | definition / prose; `primitive_probes.py` | prose + exhaustive probe | n/a |

### §3 The correspondence

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §3-a | E1: $S\iff D\iff Q_{\mathrm{fb}}$ | Main:16–18, :526–532, :580(1) | `finite_horizon_equivalence` (Equivalence:462); compositions at :466–468 | kernel | kernel, six directions; axiom report at `687e885b` (provenance above) | PARTLY KNOWN; packaging PROVISIONAL (C4, AUDIT:631–709) |
| §3-b | S⇒D | Main:500, :532 | `S_imp_D` (Equivalence:422) | kernel | kernel | PARTLY KNOWN (EG Prop. 13, FT); PROVISIONAL remainder (C1, AUDIT:496–542) |
| §3-c | S⇒D with the prior independent of $x_0$ | Main:496–500, :498 | none ("not formalized", Main:500) | prose + exact probes (`process_dilation_probes.py`; `review4_probes.py` P-G) | prose + probe | PARTLY KNOWN (EG Prop. 16, LPW Prop. 1.5); packaging PROVISIONAL (C1′, AUDIT:544–570) |
| §3-d | D⇒$Q_{\mathrm{fb}}$ (construction sentences only; F3's "fixed autonomous generator" remark at Main:532 is excluded) | Main:262–266, :532 | `D_imp_Qfb` (Equivalence:294); `permMatrix_mem_unitaryGroup` (EquivalenceChain:179); `isDiag_Phi` (:253) | kernel | kernel; `sdq_probes.py` | KNOWN (B25 v3 p.12; B23 §4.3; B26 §4) (C2, AUDIT:572–595) |
| §3-e | $Q_{\mathrm{fb}}$⇒S | Main:532 | `Qfb_imp_S` (Equivalence:245) | kernel | kernel | REFRAMING (FT-r4) (C3, AUDIT:597–629) |
| §3-f | The representation is universal; the bare form is false | Main:98–99, :534, :592, :596–598 | — | prose | via E1 | C4-old WITHDRAWN (AUDIT:697–702) |
| §3-g | The Born dictionary is in the definition; the exponent is not selected | Main:20, :534 | — | prose + probe (check 6, `equivalence_recovery_probes.py`) | prose + probe | KNOWN, non-discriminating (AUDIT:588–592) |
| §3-h | No exact all-time realization by one fixed substratum | Main:618 | — | prose proof | prose | not classified |

### §4 Memory

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §4-a | The three floors of the unavoidable-memory theorem | Main:582–590 | `unavoidable_hidden_predictive_memory` (HiddenMemory:185), `pushforward_identity` (:83), `distinguishability_floor` (:114), `capacity_floor` (:170) | kernel; `memory_probes.py` | kernel for the joint law; the time-$t$ reading is not formalized | REFRAMING; PROVISIONAL (C10, AUDIT:1128–1153) |
| §4-b | The biconditional, in prose | Main:99, :580(2), :592 | the components above + `S_imp_D` | kernel components + prose | two links not formalized | REFRAMING (C10-B, AUDIT:1155–1180) |
| §4-c | $\log_2 m \ge I^*$ | Main:484–494 | `c3_necessity` (C3Necessity:80), `card_hidden_ge_two_pow_Istar` (:117), `c3_necessity_and_capacity` (:130) | kernel | kernel | REFRAMING; PROVISIONAL (C11) |
| §4-d | The readback lemma | Main:167–170 | none | prose + exact probe (`c4_backflow_probes.py`) | prose + probe | REFRAMING; PROVISIONAL (C9) |
| §4-e | (ii) ⟺ (iii), with (iii) corrected | Main:516–522, :596, :608, :610; `verification/audits/manuscript/f29-witness-quantifier/result.md:6–30`, output :66–124 | none | prose (both directions); finite acceptance test (3 processes, $K\le3$) | prose + test | REFRAMING, near-definitional (C12, AUDIT:1191–1268; its F29 candidate is fixed by #932) |
| §4-f | (C1)–(C3) without (C4) give zero backflow | Main:172 | — | exact probe (`review3_probes.py`) | probe | not classified |

### §5 Quantum-like behaviour

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §5-a | Stochasticity by marginalization | Main:90, :105 | — | definition | — | n/a |
| §5-b | The minimal model | Main:178–196 | — | exact computation, in the text | Re-checked here by the scratch script `S/paper/design/probe/examples.py`, which is not a repository artifact. Its matrices are exact rationals: $T(1,0)$ has entries 2/3, 1/3; $T(2,0)=I$; $\Lambda=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$. **Caveats (review F14):** the script assumes $x_0$ uniform; for $P(x_0{=}0)=a$ the conditional is $a/(2-a)$, and Main:194 does not state the $x_0$ law. The paper cites Main:178–196 and states the $x_0$ law | not classified |
| §5-c | Non-permutation $T$ + recurrence ⇒ P-indivisible | Main:115–129 | `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148); census family "recurrence horizon: …", `manuscript: []` | kernel (rooted form) + prose | kernel | KNOWN (C8, AUDIT:821–913) |
| §5-d | Monotonicity is necessary, not sufficient | Main:121 | — | exact probe (`translation_probes.py`) | probe | not classified |
| §5-e | The stochastic-inverse lemma; readback ⇒ indivisibility in the recurrence cycle | Main:133–141 | `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110); `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122); census family "physical C4 discharge: …", `manuscript: []` | kernel (lemma; routed level); the history-level step is prose | the history-level step is prose (F11, AUDIT:1558) | KNOWN (C7, AUDIT:800–819; mechanism C8) |
| §5-f | XOR: memory, with a matrix family that factors through $\Lambda=I$ | Main:141, :606 | — | exact probe (`review4_probes.py`) | Re-checked by the same scratch script: all two-time kernels are $\tfrac12 J$, and $I(X_0;X_2\mid X_1)=1$ bit, with the i.i.d. control at 0. **Caveat (review F14):** the scratch CMI is computed in floating point (`math.log2`); only the matrices are exact. Every mass is a power of 2, so the value is exact in substance; the repository evidence is `review4_probes.py` | KNOWN: up to flipping the final bit, RHP 2014 Eq. (15) (FT-r4; AUDIT:1464–1525) |
| §5-g | Population P-indivisibility ≠ quantum non-Markovianity | Main:322–330, :334 | — | prose + exact probe (`c1_cp_scope_probes.py`) | prose + probe | not classified |
| Alt-X: C8-R | The `PPer` classification | not in any manuscript (AUDIT:938–946); census note `verification/lean-manuscript-census.json:809`; `verification/programmes/oi-qm/track-i/arc-b-rooted-classification/result.md` (full-support separation, :87–116) | `finiteRootedRealizable_iff_pper` (RootedClassificationAllTime:192); → `pper_of_finiteRootedRealizable` (RootedClassification:339); ← `pper_has_responseRealization` (RootedClassificationAllTime:162) | kernel (finite visible; zero-prior padding) | kernel; the full-support separation is prose + probe | NOVEL-CANDIDATE, unverified; no priority sentence (AUDIT:915–1070) |
| Alt-X: LG | An invasive classical comb reproduces $K=3/2$ | Main:460–464 | — | prose + exact probes (`intervention_probes.py`, `lg_comb_probes.py`) | prose + probe | not classified |

### §6 Reproduced versus derived

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §6-a | Representation, not explanation | Main:616 | — | prose | — | not classified ((e)) |
| §6-b | The relating evolution is not selected by representability (carried at kernel scope) | Main:624. The site names identifiers only for the fixed-basis-datum sentence. The census family "the coherent-lift stabilizer no-go (act 11, Track B)" anchors `CoherentLiftGauge` to this paragraph | `gl2_strong_gauge_moves_relative_candidate` (CoherentLiftGauge:537): two coherent lifts with different relative candidates. `gl3_constant_gauge_preserves_relative` (:451): a constant deformation cancels. `bridge_traj` (TrackBQfbBridge:276), `rooted_eq_iff_slice_eq` (:180), `realData_traj_stochastic` (:286), `padData_rooted` (OperationalSourcing:476): the quotient by visible equality | kernel | kernel; axiom report at `687e885b` (CoherentLiftGauge checked) | not classified |
| §6-c | The three statuses | Main:624 (closing sentences) | — | prose | — | n/a |
| §6-d | E2 (carrier-general). Independence of (i)–(v) on the qubit, against the sealed core. Bare finite OI ⇏ QM (qubit countermodel). Every theory with full reversible control realizes the core | GR:216–222, :228; Main:352, :542 | `exactAll_iff_physical_general` (GeneralCarrier:100), whose → direction is `physical_of_exactAll` (PhysicalCharacterization:301) and whose ← direction is `exactAll_of_physical_general` (GeneralCarrier:93). The ← direction runs through `krausSoundExt_of_validity_inert` (OperationalValidity:124) and `compositeCompleteness_unconditional` (IsometryExtension:179, called at GeneralCarrier:84), which is the conditional `compositeCompleteness` (AncillaClosure:373) with its premise discharged by `finiteIsometryExtensionSF_discharged` (IsometryExtension:116); also `exactAll_of_levelOne` (LevelOneSeam:196). `five_way_minimality` (RankGapTheory:702, over `Fin 2`). `oi_alone_not_qm` (GeneralCarrier:160, `∃ T : FiniteOperationalTheory (Fin 2)`). `realizesSealedOICore_of_control` (OIRealization:252). `RealizesSealedOICore` is defined on `Fin 2` only (OIRealization:234). See also `main_result` (GeneralCarrier:188) and `oi_compatible_classification` (GeneralCarrier:168); neither is cited by the paper (R21) | kernel | kernel; axiom report at `687e885b` | not classified (not examined by AUDIT r4) |
| §6-e | No fixed finite carrier reproduces a qubit | Main:538, :540, :580(3) | — | prose + import (HKLP [55]); `nogo_probes.py` | prose + import | REFRAMING; PROVISIONAL (C14, AUDIT:1287–1301) |
| §6-f | ε-realization and gluing; these are not uniqueness theorems | Main:544–562, :576–578, :580(4) | none (F7 open; AUDIT:1554) | prose + exact probes (`opglue_probes.py`) | not audited internally (AUDIT:1316) | not classified (C15) |
| Alt-X: OI⁺ | OI⁺ ⟺ exact finite endomorphic operational QM | Main:564–568 | `carrier_general_oiPlus` (CarrierGeneralOIPlus:213): → `qm_of_oiPlus` (:191), ← `oiPlus_of_qm` (:198); `oiPlus_independence` (:230; also CompletedOI:506) | kernel | kernel | not classified |
| Alt-X: RW | Read-write dynamics does not generate state mixing | Main:568 | `readWriteSourced_not_qm` (ReadWriteControl:174), `substratum_plus_control_qm` (StructuralClosure:414) | kernel | kernel | not classified |

### §7 Black-hole application

| ID | Claim | Source | Layer | Correctness | Originality |
|---|---|---|---|---|---|
| §7-a | The nested partition | ch07:120–122; GR:721 | definition | — | n/a |
| §7-b | Bijectivity conserves global information | ch07:118 (first sentence); BH01/MANUSCRIPT-AUDIT.md:91 | definition-level | — | n/a |
| §7-c | Bijectivity neither implies recovery nor is necessary for it. In a bijective instance, zero advantage needs $\lvert K\rvert\ge\lvert M\rvert$; 32 non-injective maps violate the bound | BH01/REPORT.md:17–18, :21, :35–47 | exhaustive exact enumeration + written proof | reviewed ACCEPT (`df2ea6f5`) | not classified (C16-S; AUDIT r4 did not read the #917 records, AUDIT:1397–1398). The report's "CONFIRMING" (REPORT:251) is an §A.31 output class, not an originality class |
| §7-d | Sufficiency of complete endpoint access; $P_{\mathrm{succ}}\ge1/\lvert K\rvert$; the conditions are sufficient, not necessary | BH01/REPORT.md:20–21, :49–58, :66–86, :98–112 | written proof + exhaustive check | reviewed | covered in kind, per the package's own description of C2 ("remnant-capacity form of a known fact", REPORT:110–112) and C4 ("linear secret-sharing threshold", :131–132); not literature-mapped |
| §7-e | The Fubini identity | BH01/REPORT.md:29, :139–142; GR:731; ch07:124 | written proof + exhaustive check | reviewed | not classified |
| §7-f | Item F, with its three "does not show" limits; the intervals were chosen post-plan, and the conclusion is insensitive to them | BH01/REPORT.md:30, :211–245 (:228 $t_{\mathrm{evap}}/\tau_B^D\ge1.785\times10^{57}$; :231 $t_P$ at β = 1; :234–235; :241–245); BH01/review/REVIEW.md:3; GR:811, :813 | exact interval arithmetic (control K7) | reviewed; independently recomputed (REPORT:233–235) | audit observation (REPORT:257) |
| §7-g | No entanglement from configuration states; $S(R)\le H(p_0)$; conserved overlap | BH02/REPORT.md:14–15, :26–42 | proofs + exhaustive exact sweeps | reviewed ACCEPT (`ce7937d2`); "C1, C2, C4 … correct and correctly scoped" (BH02/review/REVIEW.md:5) | not classified (no literature examined) |
| §7-h | H-scramble fails for every bijection in GR's configuration setting; the Page value enters only via the posited Haar ensemble | BH02/REPORT.md:18–19, :77–102; GR:817, :833 | proof (from §7-g); textual analysis | reviewed | not classified (no literature examined) |
| §7-i | The Page-time fraction, under three conditions: constant α, constant β, $S_{\mathrm{BH}}\propto M^2$. An M-dependent coefficient moves it | ch07:137–143; GR:859–865; BH02/REPORT.md:22, :118–134 (:123–127) | exact algebra + literature (Page 2013 read in full, REPORT:191) | reviewed; KNOWN | KNOWN — C16a, C16b (AUDIT:1327–1347) |
| §7-j | The open items | ch07:126, :147–151, :155–157; GR:805, :833; BH02/REPORT.md:21, :112–114; PROGRAMME.md:3 | — | open | C16c PARTLY KNOWN, PROVISIONAL, conditional (AUDIT:1348–1361); C16d WITHDRAWN (AUDIT:1362–1386) |
| Alt | C6(c) is CONDITIONAL; C3 is a supplied-superposition counterexample (NUMERICAL) | BH02/REPORT.md:16, :20, :103–111 | exact + numerical | reviewed. Amendment A1 was informed by the outcome and decided C6(c) (BH02/review/REVIEW.md:15–19) | not classified |

### §8 Open problems

Sources as in OUTLINE-r2 §8:
- Main:20, :22, :99, :139, :360–377, :392–394, :433–451, :480, :500, :534, :542, :580(2), :594,
  :608, :618, :624, :702–704, :708, :720, :758;
- GR:228.

The Bell ceiling is a prose proof with a probe (check 11). Main:379 calls it Bell's theorem
applied, so it is KNOWN in kind, but AUDIT r4 does not classify it.

## UNTRACED (not carried)

1. **Main:624, two sub-claims:**
   - (a) the single-time fibre-Gram classification;
   - (b) "an ancilla carried between steps … can separate two lifts … already in the two-step law
     (exact computation)".
   - For (a), the census family "the two-sided invisible gauge and the fibre-Gram classification
     (act 12, Track B)" maps `OIBridge/TwoSidedGauge.lean` to the Main anchors "The uniformly
     invisible deformations of a lift are two-sided" and "the fibre-Gram data — agrees up to the
     anchored phases". The module contains `gramPhaseEquiv_of_twoSided` (TwoSidedGauge:263, TG2
     forward) and `sh1_necessity` (:168), along with further TG2/SH1 directions.
   - Status of (a): **not yet checked direction by direction** against Main's statement, so not
     carried. The first pass searched only `CrossTimeInvariants.lean`; that was a search gap, not
     an absence.
   - (b) names no artifact at the site and is not carried.
2. **Main:352, "kernel-verified with no external premise".** No identifier is named at Main's site.
   Traced through GR:218 (§6-d).
3. **C8-D, the combined dichotomy.** Its only source is novelty audit revision 4 §4 (cited at
   AUDIT:1072–1112), not a file on `main`.
4. **"Machine-checked" as wording.** The build and axiom report exist at `687e885b` (provenance
   above). What is missing is a retained expected result on `main` (§A.42). Until one exists, the
   paper says "checked in Lean 4/Mathlib at commit X by recipe Y" (decision 2).
5. **Any empirical test or prediction of OI** (Main:702–704). Not carried.
6. **The cosmological realization of C1–C4** (Main:72). Out of scope.

## Owner decisions to prepare (not decided here)

### Decision 1: scope (OUTLINE-r2, "Alternative scopes")

- **Recommended (≈ 14.25 pp).**
  - Mathematics: §3, §4-a to §4-d, §5-c to §5-g, and §6-a to §6-e.
  - Black hole: BH-01 claims A, C1, C2 and E, plus item F; BH-02 C1, C2, C6(a) and C6(b); BH-04 C7,
    with Page 2013 and 2005.
  - Open items: listed in §7-j.
- **Alt-L (≈ 12.25 pp).**
  - §7 at 1.0 pp, carrying §7-b, §7-c, §7-d, §7-g (one sentence), §7-h and §7-i.
  - Drops §7-e, §7-f, §6-f and §8-h. Appendix A is folded into §3.
- **Alt-X (≈ 15.0 pp).** Adds:
  - C8-R as new manuscript content: a candidate with no priority sentence. Before any "not
    located" clause, P1.1 and P1.2 must be read in primary text and BD's forward citations
    checked (AUDIT:2018–2029).
  - OI⁺ (E4) and `readWriteSourced_not_qm`.
  - The Leggett–Garg comb.
- **(a) The R11 conflict.** The paper's §7-c (claim A) contradicts ch07:110 / FULL:1987. §7-f
  (item F) contradicts GR:811. Owner choice:
  - **correct first:** correct ch07:110, ch07:159–161, GR:811 and their FULL mirrors (FULL:1987,
    FULL:2036–2038) before the paper lands, in a separate §A.25 change; or
  - **drop §7-c and §7-f:** use the conflict-free §7 variant, which carries §7-a, §7-b, §7-g, §7-h,
    §7-i and §7-j.

  Alt-L as defined still carries §7-c, which contradicts ch07:110/FULL:1987 (BH01
  MANUSCRIPT-AUDIT:56–60). It is a page option, not a conflict resolution.
- **(b) Worked example.** If pages force a choice, use the Main §2.4 minimal model or the XOR
  family as the single worked example.

### Decision 2: "machine-checked" (review F9)

The build and axiom reports exist at `687e885b`: run `40291389159`, job `121467032075`, log sha256
`e20abaee…5251`. They are provenance only. Choose one:
- retain an expected result for the bridge build at `687e885b`, or at the drafting commit, on
  `main` beside the paper's evidence (§A.42 item 1), before the paper lands; or
- accept the wording "checked in Lean 4/Mathlib at commit X by recipe Y" and do not use the term
  "machine-checked".

### Decision 3: provenance of the design inputs (review F10)

Choose one:
- land or retain on `main` the following before any paper sentence relies on a class or a
  "do not carry" decision:
  - AUDIT r4 as applied (with its Rc4 record);
  - the two literature studies;
  - their reviews (`S/revlitcorr/`, `S/revlitbh/`);
- or state that the classes are design inputs only.

The attributions themselves (for example "RHP 2014 Eq. (15)") can be checked against the
literature directly. The governed decisions rest on scratch until the records are landed or
retained.

### Decision 4: census registration (review F12)

The paper's commit would:
- register `papers/<name>.md` in the census `manuscripts` list;
- add anchors for every family it cites that has `manuscript: []`:
  - "recurrence horizon: …" (`RecurrenceHorizon`, §5-c);
  - "physical C4 discharge: …" (`PhysicalC4Discharge`, §5-e);
  - in Alt-X, the rooted-classification family;
- add the paper's anchors to families it cites that already carry Main anchors (Equivalence,
  HiddenMemory, CoherentLiftGauge and others), where the registry requires them (§A.35).

The alternative is to cite §5-c and §5-e as prose plus probe, with no kernel identifier.

### Decision 5: GR:226 (review F11)

Commission a separate §A.34/§A.25 check of GR:226's box, which displays "OI-compatible operational
theory + (i)–(v) ⟺ finite operational QM … for every nonempty finite system".
- Its OI-conjunct converse (QM ⇒ OI-compatible) has a kernel witness only on the qubit
  (`oi_compatible_classification`, `realizesSealedOICore_of_control`, `RealizesSealedOICore` on
  `Fin 2`).
- This is a check of GR, not of the paper. The paper neither displays nor cites the box.

### Decision 6: page format and Appendix A (review F13)

- Confirm the target format: single column, about 550 words per page.
- Choose Appendix A's scope:
  - kernel-backed rows only, about 15 rows at 0.5 pp (the default);
  - or the full claim map, about 55 rows at about 1.5 pp, which needs about 1 pp cut elsewhere.

### Decision 7: the Explainer

The outline needs nothing from the Explainer. AUDIT:129–130 says it is superseded and not a drafting
source, and Appendix A is rebuilt from Main's status ledger (Main:710–722). Retiring the Explainer
is a separate change. Its live dependents at `687e885b` (counted with `git grep -c Explainer`) are:
- `verification/lean/edge_rigidity_probe.py`, 58 references, run in CI
  (`.github/workflows/verify.yml:257`);
- `verification/lean-manuscript-census.json`, 15 references, including anchors in the act 11 and
  act 12 families cited by §6-b;
- `verification/coverage/LEDGER.json`, 9;
- `verification/README.md`, 15;
- one each in `papers/Main.md` (:66), `README.md`, `book/README.md`, `book/bibliography.md`,
  `book/The-Incompleteness-of-Observation-FULL.md`, `.zenodo.json` and `LICENSE`.

Frozen records also reference it (for example `verification/audits/provenance-errata/errata.json`
and `verification/certificates/A12P.json`). They are not correction targets (§A.39, §A.42 item 4).
The planned filename `papers/Introduction.md` (audit README.md:112) would be picked up by every
`papers/*.md` glob.

**Further item: the title (R1).** Flagged, not required.

## Risks: claims that could read stronger than their evidence

| # | Risk | Safe form | Basis |
|---|---|---|---|
| R1 | The title reads as a derivation | a neutral title | F4 open (AUDIT:1551) |
| R2 | "Born rule derived" | the Born form is part of the definition of $Q_{\mathrm{fb}}$; the exponent is not selected | Main:534; AUDIT:588–592 |
| R3 | E1 read as characterizing non-Markovianity or QM | universal representation, Markov included | Main:596–598; AUDIT:460–464, :697–702 |
| R4 | (ii) ⟺ (iii) displayed | prose only, with its reduction (§A.34) | Main:608; AUDIT:1264–1267 |
| R5 | The memory biconditional displayed as proved | prose, with directions named and two links stated | Main:99, :580(2) |
| R6 | "Machine-checked" used without a retained expected result, or beyond the listed declarations | "checked in Lean 4/Mathlib at commit X by recipe Y", listing the declarations and the unformalized steps. The build and axiom report at `687e885b` (run `40291389159`, job `121467032075`) is provenance only; §A.42 retention is needed before "machine-checked" (decision 2) | REVIEW F9; AUDIT:2040–2045; §A.42 |
| R7 | C8-R priority | no priority sentence; in Alt-X, only the restricted "not located" form | AUDIT:1032–1070, :2018–2029 |
| R8 | (C4) said to force short-window P-indivisibility; P-indivisibility equated with quantum non-Markovianity | the global recurrence-cycle form only; the XOR and Hadamard limits | Main:141, :330, :334 |
| R9 | The history-level step presented as kernel-proved | marked prose (F11) | AUDIT:1558; Main:139 |
| R10 | Black-hole toy results presented as black-hole physics, or their reviews as validation | "finite toy access model"; "separate-agent internal review" | BH01/REPORT.md:285–302; BH01/review/README.md:3 |
| R11 | **Corpus tension (§A.25).** §7-c (claim A) contradicts the live sites ch07:110 / FULL:1987; the falsification framing at ch07:159–161 / FULL:2036–2038 is "unfalsifiable as stated"; §7-f (item F) contradicts GR:811. The packages authorize no manuscript change (BH01/MANUSCRIPT-AUDIT.md:3–11; PROGRAMME.md:3, :56) | owner choice: correct ch07:110, ch07:159–161, GR:811 and their FULL mirrors first, or drop §7-c and §7-f. Alt-L as defined still carries §7-c, which contradicts ch07:110/FULL:1987 (BH01 MANUSCRIPT-AUDIT:56–60) | BH01/MANUSCRIPT-AUDIT.md:9–11, :56–60, :143–160; BH01/REPORT.md:237–245 |
| R12 | 0.646 presented as the Page time; "derivation of the Page curve" | conditional on β = 1, a constant mass-loss coefficient and $S_{\mathrm{BH}}\propto M^2$, and on H-scramble | ch07:143; BH02/REPORT.md:22, :96–102, :118–127 |
| R13 | ≤ n³, the Main:210 contrast, Main:504 | omit (F13) | AUDIT:1872–1918 |
| R14 | Main's F14–F19 sentences imported | rewrite from the full-text studies | AUDIT:1561–1566 |
| R15 | ε-gluing relied on | cited, not used | F7 (AUDIT:1554) |
| R16 | C14's attribution | read Hardy 2004 and [55] first | AUDIT:1292–1301 |
| R17 | **Provenance (§A.42).** The design inputs rest on records off `main`: AUDIT r4 (on a branch at `1e9c05c7`, not on `main`; the applied text `eacbdd56…22ad` was not itself re-checked, since Rc4 reviewed the pre-recheck `b8967887…a781`); the two literature studies (scratch only); and their reviews `S/revlitcorr/` and `S/revlitbh/` (scratch only), on which AUDIT:134–145 rests. Attributions can be checked against the literature; the governed design decisions (which classes, which sentences are barred) rest on scratch | land or retain these on `main` before the paper cites a class (decision 3) | REVIEW F10; AUDIT:134–145 |
| R18 | The hypothesis read as supported by the theorems | "the theorems are mathematical …" | Main:62, :704 |
| R19 | Self-assessment in paper prose | content and status only; `tools/voice_check.py` | §A.32/§A.33 |
| R20 | BH-02 C6(c) presented as firm | omit, or cite with the A1 disclosure | BH02/review/REVIEW.md:15–19 |
| R21 | **GR:226's box carried.** It displays "OI-compatible + (i)–(v) ⟺ finite operational QM" for every nonempty finite system; its OI-conjunct converse has a kernel witness only on `Fin 2` | do not display or cite it; display E2, which has no OI conjunct; state the independence and `oi_alone_not_qm` as qubit results (decision 5) | REVIEW F11; GeneralCarrier:168, :188; OIRealization:234, :252 |
| R22 | The five conditions described as independent of embedded observation in general, or as not supplied by OI | "independent of the other four and of one finite C1–C4 observation process, by qubit countermodels, and none implied by bare finite OI; which of them a physical substratum supplies is open" | REVIEW F1, F2; GR:220, :228; RankGapTheory:702 |

## Literature keys (LC §1 retrieval table, sha256-pinned there)

| Key | Source |
|---|---|
| B23 | arXiv:2309.03085v2 |
| B25 | arXiv:2302.10778v3 |
| B26 | arXiv:2608.04354v1 |
| EG | arXiv:2602.23491v1 (Egri et al.) |
| BD | arXiv:1408.7062v3 (Buscemi–Datta) |
| DO3 | arXiv:2602.22095v3 |
| PI | arXiv:2505.08785v1 |
| CA2 | arXiv:2601.18720v2 (Calvo) |
| SCH | arXiv:2106.03513v1 |
| GO | arXiv:1309.6586v2 |
| HHO | arXiv:quant-ph/0212019v2 |
| GH | arXiv:quant-ph/0110166v3 |
| MO | arXiv:0711.4770v2 |
| SC | arXiv:cond-mat/9907176v2 |
| BB | arXiv:1209.3632v5 |
| BCN | arXiv:2405.05794v3 |
| BI | arXiv:2609.11402v1 |
| LPW | Levin–Peres–Wilmer, 2nd ed. |

The FT-r4 sources are listed in AUDIT §8 (AUDIT:2091–2111):
- RHP 2014, arXiv:1405.0303v2;
- RHP 2010, arXiv:0911.4270v2;
- BJA, arXiv:1603.04288v2;
- BLP 2009, arXiv:0908.0238v2;
- Milz et al. 2019, arXiv:1901.05223v2;
- Milz et al. 2020, arXiv:1907.05807v3;
- Strasberg–García Díaz, arXiv:1905.03018v2;
- Capela et al., arXiv:1910.04236v1;
- JDM 1960.

Page 2013 is arXiv:1301.4995v3 and Page 2005 is arXiv:hep-th/0409024v3 (BH02/review/README.md:7).
Page 1993 and Penington 2019 are taken from the black-hole study (sha256 `c7475d09…`).
