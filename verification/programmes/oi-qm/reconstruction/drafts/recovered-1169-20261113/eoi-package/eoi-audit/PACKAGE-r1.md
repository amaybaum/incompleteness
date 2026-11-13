# EOI retrospective audit: decision package for the owner

Citation forms: `C1:n`, `C2:n`, `C3:n`, `C5:n` = line `n` of `AUDIT-C1.md`, `AUDIT-C2.md`, `AUDIT-C3.md`, `AUDIT-C5.md`; `GATE:n` = line `n` of
`../gate/GATE-DRAFT.md`; repository paths and lines are at `5ce4f98e` as the audits cite them. Abbreviations follow the audits (Main, GR, Sub, SM,
Intro, Comp, Cplx, Str = Structure, FULL, chNN, PROG, QA, M1D, M2D, MI-D/MI-R/MI-A1/MI-A3, AP1, FB, OA, CR; C3:13-22, C1:11-16, C5:7-9). Book files:
ch00 = `ch00-introduction`, ch01 = `ch01-observation`, ch02 = `ch02-substratum`, ch07 = `ch07-gravity`, ch09 = `ch09-universality`, ch14 =
`ch14-quantum-computing`, ch18 = `ch18-beyond`, ch19 = `ch19-open-problems`, appendix-b/-c = `appendix-b-derivations`/`appendix-c-objections`.

## 1. Scope and standing

- **What this is.** A paper-only audit of merged OI–QM findings at `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`, consolidated from four
  accepted cluster audits and the EOI gate draft. No build, computation or repository write was made.
- **Who checked it.** Model-written and model-reviewed. It is not human verification.
- **What it does not do.** Nothing is edited or adopted. No scientific status changes (§A.45 rule 1). No correction, follow-up or investigation is
  authorized; the owner direction is that "No manuscript corrections or new scientific investigations are authorized until the reconciled findings are
  reviewed" (BRIEF-P2.md:51).
- **R-I1.** "Corrections change scope or interpretation, never silently discard a valid proof" (BRIEF-P2.md:45); every original finding below keeps
  its proved scope.
- **Inputs (sha256 re-computed for this package).**

| Input | Revision | sha256 | Final review |
|---|---|---|---|
| AUDIT-C1.md (equivalence core) | r3 | `8aaa7518…dfacec43` | REVIEW-C1-r2: ACCEPT WITH CHANGES; four items applied in r3 (C1:703-710) |
| AUDIT-C2.md (scope of no-gos) | r4 + citation fix (file header still reads "r2", C2:1) | `54699d91…e38f80d7f` | REVIEW-C2-r4: ACCEPT WITH CHANGES; its one citation fix is the only diff from r4 (C2:706-711) |
| AUDIT-C3.md (inaccessibility) | r3 | `d143754b…5e40e68b` | REVIEW-C3-r3: ACCEPT; optional n1–n3 applied in §6 below only |
| AUDIT-C5.md (cross-document) | r2 + nits R1, R2 | `65f844f0…cf50627c` | REVIEW-C5-r2: ACCEPT (on `ff858e47`); the diff is those two nits (C5:145, 204, 548) |
| ../gate/GATE-DRAFT.md | r4 | `a5d42f92…acf936` | REVIEW-GATE-r3: ACCEPT WITH CHANGES; r4 takes R3-B1/R3-B2 verbatim (diff r3→r4 re-checked) |

- **Snapshot drift.** `origin/main` has since advanced to `2cd49dc0` (merge of #1206, MATH-CON-1 design). `git diff 5ce4f98e origin/main` touches no
  file under `papers/` or `book/`; its only change is the MC1 `DESIGN.md`, which differs from the gate's pin `41a42cb9` at one line (758, a
  disposition-table row the gate does not cite).
- **Coverage (from the phase-1 inventories, coverage only).** No accepted audit in this package classifies MQ-22 (GR:214 completion classification) or
  MQ-30 (Str:128), both priority H (INV-MANUSCRIPT:41, 49, 69), nor INV-RECON rows 7.a–7.c (`oi-qm-ext-1` whole-model bridge, measurement exchange,
  two-system interface; INV-RECON:33-35). MQ-09 (Main:684) is touched only as an over-read text (C1:178) and an owner-judgement site (C5:337-340).
  There is no C4 cluster input.

## 2. Headline findings

Outcome 1 = valid as stated, 2 = valid but conditional, 3 = requires new investigation (BRIEF-P2.md:12-19).

1. **S⟺D⟺Q_fb holds and derives no quantum structure.** Outcome 1; n/a for S⟺D, Q_fb leg an imported comparator; kernel `finite_horizon_equivalence`
   (Equivalence.lean:462-468). Q_fb is a function of a Markov chain with kernel |U|² (Equivalence.lean:190-217); at law-class level it adds nothing to
   S⟺D (C1:37-54, 105-140).
2. **The operational reading of "QM emerges under C1–C4" is refuted at its interface.** Kernel counterexample `oi_alone_not_qm`
   (GeneralCarrier.lean:160-163; GR:220-222), scope `Fin 2`, one sealed core, `FiniteOperationalTheory`; one direction only, since full control also
   realizes the core (OIRealization.lean:252-258). Representation reading outcome 1, C1–C4 idle (Main:72, 82(2)). Class imported. A refuted text, not
   outcome 3 (C1:153-167).
3. **Operational characterizations: kernel 1; statements as made 2; imported.** MQ-12: the drive generator `−i(E_ab+E_ba)`, consumed by
   `control_of_phaseFree` (MinimalRepertoire.lean:529, 559), is unnamed. MQ-13: `ExtendsSubstratum` is unused (StructuralClosure.lean:414-417); `hc`
   and a swaps-and-phases step are missing from the GR:262 box (C1:298-304, 351-355).
4. **Main:590's negative clause: outcome 2, conditional; its own citation is vacuous.** `ReadWriteSourced` is unsatisfiable (paper re-derivation;
   recorded on `main`; #1188). Content survives at kernel level on `substratumGen_not_control` (`Fin 2`) and `permTheory_not_control` (every carrier);
   the interface qualifier is absent at Main:590 and mirrors (C2:125-243).
5. **No-go coverage of hidden memory is layered.** Kernel: hidden cells in the carrier and fresh uniform ancillas. Paper only: pre-correlated external
   memory (AP1 Lemma 1, enlarged carrier). Encoded identifications: outside, representation only (C2:51-89).
6. **Act 45 (R-I2).** Kernel verdict: trivial-ancilla dilations under the uniform initial law have slice-determined fixed-basis laws (act-45
   result.md:3-5, 11-26). Exact-arithmetic probe, replayed in CI, not kernel and not in the verdict: two dilations of one slice sharing every column
   entering the slice separate at two steps with an ancilla carried as hidden basis states; a tensor-factor ancilla does not (result.md:5, 30-39;
   kernel anchor `padData_rooted`). Main:646 layers this; ch19:289-291 does not (C1:620-635).
7. **Inaccessibility is a joint property of a native step and a supplied interface.** Symmetric center-free linear step at `q = 2` (necessary) plus
   SA-1: P2 with full support → single-time isotropy; P1, supplied and not enforced natively (AP1:338-343) → retention. Lemma Q(iii) outcome 2
   (support used at AP1:547, absent from QA:460-474), conditional, paper. M-INACC-1 exposures outcome 1, equally interface-relative, WIP/UNVERIFIED
   (C3:35-59, 224-265).
8. **Outcome 3 at two MECH-2 sites, paper, conditional.** "Every nonclassical route at `q = 2` … never access" (M2D:728-733) rests on an enumeration
   (C2:586-593); Lemma Q as M-INACC's "native instance" (M2D:853-854) exceeds Lemma Q's proof (C3:161-164). M-INACC clauses (a), (b) cannot both hold
   under MI-A1:59-70's readings (definitional observation).
9. **Hidden-prior dependence (R-I3) splits by half.** Determination rests on support; non-bias and per-state bounds on the product-uniform law; `E_A`,
   `E_B` are pointwise (C3:393-424). L3B: H₁ removes a favourable rank-4 fit, no no-go rescued (1, n/a, exact integer; C2:517-548). 8.a: a finite
   closed OI world with any prior is inside T(h)→1 (auditor, paper; C2:658-670).
10. **MECH-1 "Selection passes natively": outcome 2, conditional, imported comparator.** "Natively" holds only for the affine-symplectic dynamics; P1,
    P2/H-PREP, P3, NNB and linearity are supplied; frame and C-CP come from the comparator; the selected fragment is classical (M1D:763-766). Paper
    (C2:603-637).
11. **Five confirmed cross-document contradictions** (C5-1, -2, -3, -4, -8) plus C5-7 per site, by source reading. Every common realization Main
    supplies holds the quantum state in a hidden register (Main:582); an exact common realization for a fixed finite noncommuting family is open
    (C5:363-398, 496-523).

## 3. Per-cluster tables

### C1: equivalence core

| Claim | Statement site | Where proved | Out. | Class | Over-reading texts |
|---|---|---|---|---|---|
| MQ-01 S⟺D⟺Q_fb | Main:16-20, 548-552, 602 | `finite_horizon_equivalence` (kernel) | 1 | n/a; Q_fb leg imported | Main:776; FULL:266; FULL:64; ROADMAP:48-52 (frozen) (C1:134-140) |
| MQ-02 "QM emerges" | Main:68, 206, 682 | representation: MQ-01; operational: refuted by `oi_alone_not_qm` | 1 / refuted | imported | Main:68, 206, 682, 684; FULL:244, 334; SM:1100; Sub:459; FULL:684 vs 690 tension (C1:173-180) |
| MQ-03 Definition label | Main:526, 530, 648 | one-step lemma (paper + exact probe); fixed-Ĥ lemma | 1 | label imported; fixed-Ĥ n/a | Main:526, 530, 648, 656; FULL:6207 (C1:223-227) |
| MQ-11 five conditions | Main:564; GR:218-228 | `general_characterization`, `main_result` (kernel) | 1; "what OI must supply" 2 | imported | Main:564; GR:226 with 228 (C1:267-269) |
| MQ-12 OI⁺, `oiPlusMin_iff_qm` | Main:586-590; GR:230-256 | kernel, both directions checked (§A.34) | 1; as made 2 | imported | GR:232-236, 252, Main:590 (mild); GR:242 not pressed (C1:323-325) |
| MQ-13 substratum + control | GR:262 box, 264; Main:590 | `substratum_plus_control_qm`, converse (kernel) | 1; as made 2 | imported | GR:262, 264; Main:590; PROG:80 (C1:361-363) |
| MQ-27 | GR:40 | MQ-01 only | text | imported | GR:40 (C1:367-376) |
| MQ-28 | Sub:389 | MQ-01 only | text | imported | Sub:389, 459; GR:346 (C1:386-389) |
| MQ-29 Stage-1 output | Sub:126 | Sub:137, 141 via Main `S ⇒ D` | 2 | per context conditional; per menu imported | Sub:126, 137 (C1:414-416) |
| MQ-32 Bohmian reading | FULL:6409 | MQ-01; Main:566, 598 | 2 | imported | FULL:6409, 4920, 6417 (C1:432-435) |
| MQ-42 SM consumes "only" | SM:22 | Main + imported QFT layer | 2 | imported | SM:22, 428, 1100 (C1:455-458) |
| PROG F1/F2 | PROG:23-25, 72 | strategic map | n/a | imported (F2 route) | PROG:72 (omission), 80 (C1:486-488) |
| TI-B `C_OI = PPer` | arc-b result.md:13 | kernel, both directions | 1 | n/a | amendment-1.md:19; PROG:195 (minor) (C1:515) |
| TI-C `C_OI ⊊ Q*` | arc-c result.md:12-37 | kernel | 1 | n/a | ROADMAP:48-52 (frozen) (C1:541) |
| TB-BA | boundary-audit result.md:8 | source reading | 1 | n/a | GR:134 "determines" (C1:555-559) |
| TB-01 | act-01 result.md:18-26 | definition-level audit | 1 | n/a | Main:656; Main:218 "to obtain Born-rule statistics" (C1:582-584) |
| TB-06 | act-06 result.md:17-31 | kernel (BarandesTuple.lean) | 1 | n/a | none |
| M2/M3 lifts, Act 14/45 | DilationChoice.lean:134-136 | kernel verdict + exact probe | 1 | imported by design | ch01:187 = FULL:522 and Main:646 ("visible law"); ch19:289-291 (layer); ch19:302 (C1:633-636) |

### C2: scope of negative results

| Claim | Statement site | Where proved | Out. | Class | Over-reading texts |
|---|---|---|---|---|---|
| MQ-14 no state mixing | Main:590 (+ mirrors) | `substratumGen_not_control` (`Fin 2`), `permTheory_not_control` (kernel); own citation vacuous | 2 | conditional | Main:590; GR:260; FULL:500, 5271; ch01:165; ch19:126; source-audit.md:199-200; Intro:129 headline (C2:228-243) |
| MQ-15 layer flow | GR:266-274; Main:590 | `obs_not_layerFlowExecutable` (kernel) | 1 | conditional | none |
| MQ-16 bare OI ⇏ QM | GR:222; Intro:127 | `oi_alone_not_qm` (kernel) | 1 | n.a. | none |
| MQ-18 classical dimension | Main:560 | paper + HKLP import + exact probe | 2 | conditional | none established; r1 charge withdrawn (C2:330-341) |
| MQ-20 Bell ceiling | Main:366-395 | paper + exhaustive 16-table check | 1 | conditional | none; restatements carry hypotheses |
| MQ-23 2×2 no local lift | GR:194 | `twoByTwo_no_local_lift` (kernel) | 1 | imported (target) | none |
| MQ-17 ε-gluing | Main:566-584 | paper + exact probes | 1 | imported | outside MQ-14's statement (C2:434-437) |
| PROG F1 retirement | PROG:40, 521, 634 | `frozen_sourcing_verdict` (kernel) | 2 | conditional | PROG:40, 82, 521 (definitional, `rfl`); :634 clarity only (C2:465-473) |
| TI-D Arc D RD1 | arc-d result.md:124-131 | kernel (53 results) | 1 | conditional | none |
| TI-CR causal readback | causal-readback result.md:18 | exact witness | 1 | n.a. | none |
| IF-L3B | l3b result.md:13-15 | exact integer | 1 | n.a. | none; R_LL inputs off-repository (C2:543-546) |
| MECH-2 Lemma F, U2, NC | M2D:109-111 | paper | 2 | conditional | — |
| M-INACC framing | M2D:728-733 | enumeration (M2D:706-727) | 3 | conditional | M2D:728-733 |
| MECH-1 selection | M1D:1, 120, 931 | paper (Prop. AS, Thm W) | 2 | conditional, imported comparator | M1D:120, 931 "natively" (C2:628-630) |
| C-CP verdicts | M2D:61-63, 99, 792 | frame-relative | 2 | imported comparator | — |
| 8.a controller | CURRENT-HANDOFF.md:77-80 | paper + exhaustive step 5 | 1 | n.a. | none |

### C3: inaccessibility and hidden-sector modelling

| Claim | Statement site | Where proved | Out. | Class | Over-reading texts |
|---|---|---|---|---|---|
| M-INACC-1 exposure | MI-R:91-96 | explicit protocols, MI-R §§2-3 (WIP) | 1 | conditional | none stronger; MI-R:255 understates; MI-R:84-85, 526-529 (hand-check pointer) (C3:137-141) |
| M-INACC "native instance" | M2D:853-854 | Lemma Q under P1/P2 only | 3 | conditional | M2D:853-854, 947; M2D:728-729 routed to C2 (C3:217-222) |
| QA Lemma Q(iii) | QA:472-474, 51-53, 523-525 | QA:476-495 via AP1 Lemma 3 | 2 | conditional | QA:46 heading; QA:799 status cell; QA:51-53, 523-525 "never/permanently" (C3:266-278) |
| QA G2; R1 C-CP | QA:36-40; QA-PR:140-143 | pointwise identity; product law | 1 | conditional | none |
| FB | FB:16-19 | FB:97-117 | 1 | conditional | none |
| AP1 Lemmas 2, 3, 4; D1 | AP1:153-163, 533-537, 689-696, 580-594 | paper | 1 | n/a (L2); conditional | — |
| AP1 Lemma 5; Level 3 | AP1:731-733; 72-75, 961-977 | paper | 2 | conditional | AP1:732-733 "for any ancillas" (C3:352-357) |
| Observer access | OA:11-14 | OA:103-137 | 1 | conditional | none |
| Correlation recombination | CR:11-13 | CR:118-140 | 1 | conditional | none |
| MQ-33 | GR:450 | immediate from definitions | 2 | n/a (operator); conditional (dark sector) | GR:450 "theorem of Part I", "(from Part I alone)", "invisible … by construction" (C3:468-475) |
| MQ-07 late-time correction | FULL:4860-4862; ch18:56, 58 | conditional mechanism proposal | 2 | conditional | FULL:4860, 4862; ch18:56, 58 |
| MQ-31 resampling clause | Main:674 | hypothesis Main:445, 455 | 2 | conditional | Main:674 (+ Main.tex:4848) |
| PR (pre-stored records) | Main:554, 566 | existence theorems state constructions | 1 | conditional | none |

### C5: cross-document consistency (C5 uses its own verdicts; it assigns no outcome or class)

| Item | Side A | Anchor | Verdict | Sites |
|---|---|---|---|---|
| C5-1 composite factorization | FULL:3714 = ch14:50 | Main:218, 652 | confirmed contradiction | + GR:330 related (owner may check) |
| C5-2 visible marginal unitary | Comp:100 | Main:342, 650 | confirmed (literal reading) | single site; not load-bearing |
| C5-3 QM as Ch. 1 input | FULL:690 = ch02:56 | Sub:76; Main:68; Main:556, 564 | confirmed, either reading | — |
| C5-4 dropped OI_Q scope | Main:712; GR:368; FULL:2065 = ch07:199; stronger FULL:2765 = ch09:298 | GR:288; Main:584, 590, 592 | confirmed (dropped scope) | related: Main:712 "this content", SM:1472, Str:108 (owner) |
| C5-5 gap degeneracy | Main:260 vs 262 | Main:260 | reading-dependent; owner judgement | Main:262 parenthetical unsupported |
| C5-6 Intro:129 condition 4 | Intro:129 | GR:260 + PhaseSource, `permTheory_not_control` | not a contradiction | citation gap only |
| C5-7 memory → interference | FULL:560; FULL:542, 544, 568; Cplx:236; Str:887 | Main:326, 340, 556, 592, 656 | confirmed per site | owner: FULL:546, 548, 592-596; Main:684 |
| C5-8 single triple | Sub:126; FULL:724 = ch02:90 | Sub:137, 141; Main:560, 566, 598; Intro:133-137 | confirmed (scope) | PC marker corrected (C5:393-399) |
| P1–P3 provenance | composition-access, OI-CHANNEL-1, o-ret | §A.42 item 8 | P1 gap; P2, P3 no gap | C5:406-488 |

### 3.5 Overlaps and differences between clusters (noted, not resolved)

- **FULL:690.** C1 calls FULL:684 vs 690 an "internal tension" readable two ways (C1:180); C5 classifies it a confirmed contradiction on either
  reading (C5:105-110).
- **Main:684 (MQ-09).** C1 lists it among texts read too strongly (C1:178); C5 marks it "needs owner judgement" (C5:337-340).
- **Common realization.** C1 states multi-protocol coverage "only per finite menu to ε" (C1:100, 406, 653); C5 reads Main:598 as ε-common over all
  ≤m-outcome instruments on ℂ^d at fixed d, K (C5:367-369, 393-398).
- **H-LIFT.** C2 treats H-LIFT as supplied by carrier enlargement and H-C as the genuine exclusion (C2:567-572, 832-835); C3's AW-C3-5 groups H-LIFT
  with H-C, AP1 Lemma 5 and Level 3 as one preparation-independent hidden-law assumption (C3:576-577).
- **Intro:129.** C2 flags its opening headline as OI-level (C2:239-243); C5-6 finds the scoped clause consistent (C5:272-277). Different sentences of
  the same paragraph.
- **Main:674.** C3 grades its resampling clause outcome 2 (C3:488-490); C5 finds its "represents" clause literally consistent (C5:337). Different
  clauses. C3's routing of Cplx:236 to an A5 cluster (C3:491-493) is met by C5-7.
- **Consistent overlaps:** Sub:126 (C1:415; C5:388-391); M2D:728 (C2:586-593; C3:221-222; GATE:148); Act 45 (C1:620-635; C2:68-72; GATE:151-155);
  missing "two-state" qualifier at Main:216, 354, 776 is minor (C2:198-203; C5:272-277).

## 4. Proposed manuscript and record corrections, for the owner's decision only

No replacement wording is drafted. Book chapter mirrors not named by an audit were located for this package by matching the FULL line at `5ce4f98e`;
they were not audited. Every `.md` site has `.tex`/`.pdf` derivatives (`papers/<X>.tex/.pdf`, `book/…-FULL.tex/.pdf`, C5:19-21); chapter files have
none. Frozen status: `verification/ROADMAP.md` is frozen (§A.36); `verification/programmes/substratum/source-audit.md` declares itself frozen (:191)
but was appended after (:211) and is not in `legacy-records.json` (C2:117-120). The reconstruction records, PROG and `amendments/amendment-1.md` are
not in `legacy-records.json`, and no receipt names them (checked at `5ce4f98e`).

| # | Finding | Authoritative anchor | Sites (papers / book ch*.md = FULL / derived) | Frozen |
|---|---|---|---|---|
| K-1 | Emergence/equivalence readings of MQ-01, MQ-02 operational reading (C1:134-140, 173-178, 374, 386-389) | Main:72, 82(2), 556; GR:220-222 | Main:68, 206, 682, 776; GR:40, 346; Sub:389, 459; SM:1100 / preface:3 = FULL:64; ch00:39 = FULL:266; ch00:17 = FULL:244; ch00:107 = FULL:334 / Main, GR, Sub, SM, FULL `.tex/.pdf` | ROADMAP:48-52 frozen: mutable record only (§A.42 item 6) |
| K-2 | Definition label, "establishes …", "structures identical" (MQ-03, TB-01) (C1:223-227, 582-584) | Main:218(i), 556, 634, 646 | Main:218, 526, 530, 648, 656 / appendix-b:455 = FULL:6207 / Main, FULL | — |
| K-3 | Characterization boxes as made (MQ-11, -12, -13) (C1:267-269, 300-304, 351-363) | kernel statements; GR:216, 228, 260 | Main:564, 590; GR:226, 228, 250, 256, 262, 264 / none named by C1 / Main, GR | PROG:72, 80 (mutable) |
| K-4 | Main:590 negative clause lacks interface qualifier (MQ-14) (C2:228-243) | GR:260 reason; `permTheory_not_control` | Main:590; GR:260; Intro:129 headline / ch01:165 = FULL:500; ch19:126 = FULL:5271 / Main.tex:3915; GR.tex:1850; FULL.tex:2235, 24181 | source-audit.md:199-200 (self-declared frozen, appended) |
| K-5 | PROG "the rule contributes no availability" is definitional (C2:465-473) | `rfl`/`Iff.rfl` (§0, C2:78-81) | PROG:40, 82, 521; :634 clarity note only | mutable |
| K-6 | "Visible law" ambiguity and Act 45 layer (R-I2) (C1:633-636) | Main:646; act-45 result.md:5, 30-39 | Main:646 / ch01:187 = FULL:522; ch19:289-291 = FULL:5434-5436; ch19:302 = FULL:5447 / Main, FULL. Located, not audited: FULL:522 also states the carried-ancilla separation without a layer and ends "none of it makes embedded observation and quantum mechanics inequivalent" | act-45 record has receipt A45 (immutable; not a site) |
| K-7 | MQ-29, MQ-32, MQ-42, TB-BA texts (C1:414-416, 432-435, 455-458, 555) | Main:520-522, 560, 566, 598; Main:218(i), 646 | Sub:126, 137; SM:22, 428, 1100; GR:134 / appendix-c:180 = FULL:6409; ch18:116 = FULL:4920; appendix-c:188 = FULL:6417 / Sub, SM, GR, FULL | — |
| K-8 | TI-B "visible stochastic boundary" (minor) (C1:515) | arc-b result.md:13, 50-56 | PROG:195; amendment-1.md:19 | arc-b result.md legacy-listed (not a site) |
| K-9 | GR:450 "theorem of Part I" (MQ-33) (C3:468-475) | Main:50, 268, 650; GR:454 | GR:450 / book mirrors ch07:256 = FULL:2122, ch19:116 = FULL:5261 do not repeat it / GR.tex:3016 | — |
| K-10 | Unlabelled hidden mixing (MQ-07, MQ-31) (C3:504-508) | Main:445, 455; FULL:4844, 4856 | Main:674 / ch18:56 = FULL:4860; ch18:58 = FULL:4862 / Main.tex:4848; FULL | — |
| K-11 | C5-1 composite factorization | Main:218, 652 | ch14:50 = FULL:3714 / FULL.tex:17479-17480; GR:330 related | — |
| K-12 | C5-2 visible marginal unitary | Main:342, 650 | Comp:100 / Comp | — |
| K-13 | C5-3 QM as Chapter 1 input | Sub:76; Main:68, 556, 564 | ch02:56 = FULL:690 (with ch02:50 = FULL:684) | — |
| K-14 | C5-4 dropped OI_Q scope | GR:288; Main:584, 590, 592 | Main:712; GR:368 / ch07:199 = FULL:2065; ch09:298 = FULL:2765 / Main, GR, FULL | — |
| K-15 | C5-7 memory → interference, QM = observation | Main:326, 340, 556, 592, 656 | Cplx:236; Str:887 / ch01:225 = FULL:560; ch01:207, 209, 233 = FULL:542, 544, 568 / Cplx, Str, FULL. Sweep list: Cplx:276, 348; Medicine:552; ch18:64 = FULL:4868-4876; appendix-c:315 = FULL:6544; ch09:16 = FULL:2483; appendix-c:108 = FULL:6337 (C5:342-346) | — |
| K-16 | C5-8 single triple | Sub:137, 141; Main:560, 566, 598 | Sub:126 (= K-7) / ch02:90 = FULL:724; related Methodology:339 | — |
| K-17 | Record over-readings (C2, C3) | Lemma Q at its scope; Prop. AS; enumeration M2D:706-727 | QA:46, 51-53, 523-525, 799; M2D:728-733, 853-854, 947; M1D:1, 120, 931; AP1:72-75, 732-733; MI-R:255 (understatement) | WIP/UNVERIFIED (MI-R:3-7); not legacy-listed |

## 5. Already-tracked items (no duplicate proposed)

- **#1188 KERNEL-VAC-1** (open): `ReadWriteSourced` vacuity, repair or retirement of `readWriteSourced_not_qm`/`_not_control`, and repointing of their
  citations; recorded on `main` at QA DESIGN.md:864-866, minacc-1 DESIGN.md:585, 619, RESULT.md:613 and quarter-phase-feedback RESULT.md:187. C2 makes
  it the home of every citation defect it lists (Main:590, GR:260, verification/README.md:298, source-audit.md:100, 121,
  completion-assumption-audit.md:95, route-b-audit.md:29, RouteB.lean:13, probe and census entries) and of the one-lemma kernel check
  `not_readWriteSourced` (C2:126-189). K-4's prose qualifier is not a citation defect.
- **#1193 WAVE-SIGN-1**: the MECH-1 memory sign is conditional on it (M2D:739, 755; C2:624). **#1169**: home of the gate and of owner addendum
  c.6714136234 (MID:25-29; GATE:236). **#1206** (merged at `2cd49dc0`), **#1203–#1205** (drafts).
- **F-1 and the source of i**: pursued or located by Q-A (DESIGN.md, PROOF-RECOVERY.md), MECH-2, `two-mode-drive.md:11, 54, 145-147`, PROG:40, GR:250,
  258, MinimalRepertoire.lean:13-25, LieRankSource.lean:36-43, Intro:129 (C1:190-196, 306-312).
- **Recorded open or recorded already:** Q-C2-1(i) at M2D:717-727 (C2:702-703); the M-INACC clause clash at MI-A1:59-70; retrodiction limits at
  MI-A3:21-38, 60-84 (C3:152-155, 253-258); Act 45 layering at Main:646 (C1:627); MQ-20, -34, -35, -40 labels (C2:375-379; C3:494-498);
  composition-access `SCOPE.md:15-22`, o-ret README:40-45 and `bridge-compatibility-audit/result.md:236-246` on provenance (C5:411-488).

## 6. Proposed follow-ups: named only, not authorized

Ranked by expected information per cost, using the audits' own statements of cost and decisiveness; the decision is the owner's.

1. **M-ARC (C3:165-215; REVIEW-C3-r3 n1–n3 applied).** *Question:* on ring `Z_L` under always-on `N_1` at `q = 2`, window `V` of `w` sites, in variant
   D (a registered cell stays on the ring, its site joins `H`, never re-registered), is any `Q* = 1` linear functional on the current `V` determined
   in a positive-probability branch within the horizon? *Assumption tested:* P1's archive isolation, supplied and not enforced natively (AP1:338-343),
   which carries retention for Lemma Q, AP1 Lemma 3, Theorem W and the "native instance" claim (AW-C3-1). *Check:* exact `F_2` span membership over
   every registration schedule up to `T` (≤ 1 slot of one `V` cell per tick, each cell once, no refills or swaps); `w = 3`, `T = 4`, `|H| ∈ {4, 6}`;
   N2 does not enter. *Controls:* CC-ISO (variant I reproduces PROT-D); C-NV (n2: in both variants a `Q* = 0` functional on the current `V` is
   determined by one registration); C-SUPP (n1: in variant I an exact-relation pair exposes and a full-support pair with `P(w = b) = 3/4`, C3:91-92,
   gives at most bias); C9 (re-coupling a registered cell in variant I exposes); `T ≤ |H|`, no wrap-around through `H`. *Rule, to be preregistered:*
   Exposure = in variant D (n3) some schedule and tick put a `Q* = 1` functional on the current `V` in the span at both `|H|`, controls green;
   Survival = in variant D (n3) none at both `|H|`, controls green; Size-dependent = the `|H|` disagree; Void = a control fails. *Would show:*
   exposure, that this de-isolated interface does not protect at that size and horizon; survival, protection within that finite model, still
   conditional on P2's support clause, H-PREP and supplied registration. Neither is universal. *Rank:* fully specified; small enumeration
   (REVIEW-C3-r3:32); bears on C3's only outcome-3 item.
2. **Theorem W R-W positivity, as corrected (C3:407-414, 568-570).** *Question:* at odd `q`, does a correlated or non-uniform hidden law, full-support
   ones included, keep the hypothesis "every ancilla law has a quantum state as its R-W image" (M1D:473-474)? *Assumption:* a positivity condition,
   distinct from determination; P2 load-bearing (M1D:914); R-I3. *Check, controls, rule:* none stated by the accepted audit; the `q = 2` sharp-cell
   argument does not transfer; the r2 review's `q = 3` control reporting a non-positive full-support law is provenance only. *Would show:* a recorded
   non-positive law means Theorem W's scope must name the dependence; it would not refute Theorem W within its hypotheses or bear on determination.
   *Rank:* plausibly one exact check, but controls and rule must be written first.
3. **Q-C2-2, the M-INACC dichotomy (C2:771-788).** *Question:* at `q = 2` with native `Z`/`X` reads only, is there a protocol with (a) a hidden
   functional used by the rule and partially accessible, with a witness for the functional `G_SM` uses in P★; (b) not spanning-certifiable there; (c)
   encoded record statistics with no exact noncontextual model? *Assumption:* the dichotomy rests on an enumeration; an accessible but uncertifiable
   functional falls in neither horn (C2:588-592). *Check:* finite noncontextuality LP on P★'s fragment (P★'s heralded branches and mechanism-off
   stabilizer preparations; native `Z`, `X` reads at the stated record times; only natively certified equivalences; exact rationals); no further
   controls stated. *Rule:* infeasibility refutes the dichotomy for that instance only with instance-specific checks of (a) and (b); feasibility
   closes the instance; P★ fails C-CP, so infeasibility gives a nonclassical fragment that is not quantum. The gate's imitation rule would also
   require a physical-absence proof for non-spanning reads (GATE:76-79); the audit does not cite it. *Rank:* the LP is cheap, but (a) needs a witness
   no record gives (MI-R:41-53 is for `G_σ`, a template only).
4. **Drive-phase `diagGen_not_control` analogue (W2, C1:659-665, 314-319).** *Question:* in a candidate mechanism, is the phase relation between drive
   generator and exchange basis physically sourced? *Assumption:* "phase-free" covers the primitives, not what they generate: `flow(X_ab, π/2)·swap_ab
   = diag(−i, −i, 1, …)` on D ≥ 3 (audit derivation, exact algebra, reviewer sympy check); the real rotation gives `diag(1, −1, 1, …)`, D = 2 the
   global `−i·I`. *Check:* compute `flow(drive, π/2)·swap`; a relative quarter phase indicates the complex direction. Decisive form: prove every
   available conjugation in the generated theory preserves real matrices, so control fails (LieRankSource.lean:146); a zero-diagonal lemma is not
   decisive (ReachabilitySeam.lean:71-72). No rule is preregistered. *Would show:* real preservation, no control for that candidate; a quarter phase
   locates the complex direction without sourcing it. *Rank:* ELABORATING; `two-mode-drive.md:54, 145-147` already treats its candidate.
5. **Q-C2-1, narrowed open case (C2:744-758).** *Question:* on the laws `L` reachable from supplied preparations (P2, H-PREP), is every
   encoded-induced unitary octahedral when supplies are non-dyadic or protocols record-conditioned? *Assumption:* dyadic supply, no conditioning
   ("With non-uniform hidden priors the dyadic argument is unavailable", QA:649-650); heralds give other denominators and rows such as `(2/3, 2/3,
   −1/3)` exist. *Check:* none named; it first needs a characterization of `L`. Closed already: the all-laws form, negatively (auditor, re-derived by
   reviewer, paper); the dyadic unconditioned sub-case (reviewer, paper; integer control for m ≤ 5 only); AGL(4,2) is a control, not evidence. *Would
   show:* a non-octahedral case bears on C2:256-260 and stays representation-level (C2:83-89); a negative extends the Clifford ceiling to that
   sub-case only.
6. **F-1, extended mechanisms (C1:182-196).** *Question:* does an OI mechanism outside the classes of `oi_alone_not_qm` and
   `substratumGen_not_control` generate an operational theory with the five completion conditions, or does a no-go hold for a stated wider class?
   *Check:* per candidate, the `diagGen_not_control`/`substratumGen_not_control` analogue; C1 proposes none beyond the cited records'. *Would show:*
   per-candidate verdicts only; a positive still needs its resources sourced (two-mode-drive.md §1). *Rank:* open-ended and already pursued (§5).

## 7. Gate

EOI r4 (GATE:1-250) is a WIP/UNVERIFIED planning criterion for #1169; it changes no status and edits no record (GATE:3-9). It assigns each claimed
item exactly one class by first matching row: reachable set only (no result), EOI-NEG (negative, with G0 labels *within its stated class*,
*restricted* or *idealization-dependent*), EOI-I (G1 import fails), EOI-N (native; G1–G5 pass with no departure, preregistered criterion), EOI-C
(disclosed departures carried into the conclusion), EOI-0 (remainder); only EOI-N counts as deriving QM from OI, and the operator-level rule caps A-2
constructions at EOI-C (GATE:83-113). MATH-CON-1's reachable set is {EOI-I, EOI-NEG, EOI-0} (GATE:127-129). Retrospectively, P-CONTROL, P-OBS,
M-INACC-1 and MECH-2 are EOI-NEG, MECH-1 is EOI-C for its imitable stabilizer fragment, P-MIX is reachable set only, and none reaches EOI-N
(GATE:142-151). K2: EOI-N is closed on A-2 and open in principle only at configuration level, for a construction whose every preparation,
registration, retention, reset and timing is executed by the rule, with G3 inputs that are framework posits (any prior dependence shown for a
preregistered prior class) and a claimed item passing G5; no reviewed unit meets it, which is a finding about the present record (GATE:177-185). Open
owner questions (a)–(e): S1B (recommendation: no change to the round text); EOI-N certification; G0 countercontrols; comparator frames; placement
(GATE:204-221). Its §7 gap for MC1 "until #1206 lands" (GATE:232) now concerns content on `main` at `2cd49dc0`, unchanged at the lines the gate cites.

## 8. Owner decisions needed

1. Whether this package and its four audits and gate are accepted as the reconciled findings, the precondition the owner set for any correction or
   investigation.
2. For each of K-1 to K-17: correct or not, and the accountable Issue for each authorized correction (§A.45 rule 6).
3. K-4: whether Main:590's prose qualifier is handled with #1188's citation repoint (same sentence) or separately.
4. ROADMAP:48-52 (frozen): whether a correcting reading is recorded, and in which mutable record (§A.42 item 6).
5. source-audit.md:199-200 (self-declared frozen, appended since, not legacy-listed): the correction route (C2:117-120).
6. C5 owner-judgement items: which reading of G2 governs Main:262 (C5-5); FULL:546, 548, 592-596 and Main:684 (C5-7); GR:330's attribution (C5-1);
   "this content" at Main:712 with SM:1472, Str:108 (C5-4); the intended reading of Sub:126 (C5-8).
7. The §3.5 differences: FULL:690 strength; Main:684 classification; C1's "per finite menu" against C5's reading of Main:598; H-LIFT's treatment in C2
   against AW-C3-5.
8. K-6: whether FULL:522 = ch01:187 (located here, not audited) enters the R-I2 correction scope.
9. Which follow-ups of §6, if any, to authorize, in what order, and with what preregistration; M-ARC's rule is stated as "to be preregistered before
   any run" (C3:203).
10. Coverage: whether to audit MQ-22, MQ-30, MQ-09 and INV-RECON 7.a–7.c, which no accepted cluster classifies.
11. §A.42 item 8: composition-access P1 (support off `main` unless SCOPE.md's location statement is taken as the narrowing; C5:421-424), and L3B's
    off-repository R_LL inputs (PV-1; C2:543-546).
12. Gate: questions (a)–(e) (GATE:204-221), and whether §7's MC1 row is updated for #1206's merge.

## 9. Assumption-watch markers (merged, deduplicated)

- **Representation vs mechanism:** Q_fb, QfbData, Q* are functions of Markov chains with kernel |U|² (W1); "unitary" names both the representation and
  the visible dynamics (AW-C5-a); common realizations store the state in a hidden register and take instruments as data (W6, AW-C5-g); cite per-law
  exact, ε-common or the exact-uniform obstruction (AW-C5-e).
- **Complex import:** complex kinematics is the A1 import; uniform ancillas, discard and readout are A3/A4 idealizations met by `diagTheory` (W3);
  drive-phase sourcing (W2).
- **Idle or vacuous hypotheses:** check OI's work in each direction of an "OI + X ⟺ QM" box (W4); check exact-equality predicates for closure under
  unit scalars (VQ-1, the #1188 case).
- **Carrier and class:** "does not source X" is relative to (P-a)–(P-c), encoded re-identifications representation only (CI-1); `obsTheory` reads only
  `Conf` (RI-1); name the class, ones-fixing or phase-augmented (AW-C5-c); OI_Q/OI⁺ results are not properties of "the framework", search by meaning
  (AW-C5-b).
- **Hidden prior:** support for determination, product-uniform law for non-bias and per-state bounds, neither for pointwise exposures (AW-C3-2); does
  a hidden law remove a no-go or a favourable fit (SG-1); multi-time root-independent prior is paper-only (W5).
- **Common lift:** H-LIFT by enlargement, H-C a genuine exclusion, spanning certification the transfer (HC-1); AP1 Lemma 5, Level 3, FB H-C and H-LIFT
  assume one preparation-independent hidden law (AW-C3-5); the clusters differ on H-LIFT (§3.5).
- **Supplied access:** P2 + step → single-time isotropy, P1 → retention (AW-C3-1); "never/permanently" fail for information moved to archived cells
  (AW-C3-3); state the reading of M-INACC (AW-C3-4).
- **Definitional or unlabelled:** Main Lemma 2's partition is a definition (AW-C3-6); "thermalizes/resampled" as fact (AW-C3-7); genericity fails at
  the permutation limit for the dilated spectrum (AW-C5-f).
- **Matching level:** "visible law" names Γ and the multi-time law; carried vs tensor-factor ancillas (W7); memory is not coherence or interference
  (AW-C5-d). **Other:** MI-1, FV-1, FT-1, PV-1.

