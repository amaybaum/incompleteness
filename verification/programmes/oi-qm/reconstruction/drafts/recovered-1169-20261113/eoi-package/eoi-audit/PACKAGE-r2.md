# EOI retrospective audit: decision package for the owner (r2)

Citation forms: `C1:n`, `C2:n`, `C3:n`, `C5:n` = line `n` of `AUDIT-C1.md`, `AUDIT-C2.md`, `AUDIT-C3.md`, `AUDIT-C5.md`; `GATE:n` = line `n` of
`../gate/GATE-DRAFT.md`; `RP:n` = line `n` of `REVIEW-PACKAGE.md`; repository paths and lines are at `5ce4f98e` as the audits cite them. Abbreviations
follow the audits (Main, GR, Sub, SM, Intro, Comp, Cplx, Str = Structure, FULL, PROG, QA, M1D, M2D, MI-D/MI-R/MI-A1/MI-A3, AP1, FB, OA, CR; C3:13-22,
C1:11-16, C5:7-9). Book files: ch00 = `ch00-introduction`, ch01 = `ch01-observation`, ch02 = `ch02-substratum`, ch07 = `ch07-gravity`, ch09 =
`ch09-universality`, ch14 = `ch14-quantum-computing`, ch18 = `ch18-beyond`, ch19 = `ch19-open-problems`, appendix-b/-c =
`appendix-b-derivations`/`appendix-c-objections`.

## 1. Scope and standing

- **What this is.** A paper-only audit of merged OI–QM findings at `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`, consolidated from four
  accepted cluster audits and the EOI gate draft. No build, computation or repository write was made.
- **Who checked it.** Model-written and model-reviewed; not human verification. r1 (`PACKAGE-r1.md`, `c8960f5c…a1ec91bd`) was reviewed in
  `REVIEW-PACKAGE.md`: ACCEPT WITH CHANGES (B1–B3, N1–N20). r2 applies them.
- **What it does not do.** Nothing is edited or adopted, and no scientific status changes (§A.45 rule 1). The package itself authorizes nothing.
  Manuscript corrections remain unauthorized: "No manuscript corrections or new scientific investigations are authorized until the reconciled findings
  are reviewed" (owner chat, relayed, BRIEF-P2.md:51). The four follow-ups of the programme below are authorized separately by the owner.
- **R-I1.** "Corrections change scope or interpretation, never silently discard a valid proof" (owner chat, relayed, BRIEF-P2.md:45); every original
  finding below keeps its proved scope.
- **Standing: the owner's programme now governs §6 and part of §8.**
  - *#1169 c.6723277401* (amaybaum, 2026-11-08T15:21:11Z), the Sequential Assumption-Removal Programme (ARP): "I authorize **all four
    assumption-removal follow-ups**, including preparation, independent review, and eventual scientific execution, in the following order: 1.
    **M-ARC** … 2. **Q-C2-1** … 3. **Q-C2-2** … 4. **Drive-phase check**". Also: "The C2 re-review and consolidated classification-audit findings must
    be incorporated before M-ARC's freeze. If they require material changes, revise and independently review the affected preregistration first." This
    package is therefore an input to M-ARC's freeze.
  - *#1169 c.6723329527* (amaybaum, 2026-11-08T15:25:55Z): "Approve option (a): retain owner designation of each freeze point F and execution head E."
    "Before each execution, present the exact execution head E and proposed dispatch for my approval." "No automatic freezes or dispatches."
  - *#1169 c.6723491138* (amaybaum, 2026-11-08T15:40:41Z): every ARP investigation carries an assumption-dependence analysis. Types: "Native OI
    principles | Preserve unless we're explicitly testing an extension"; "Genuine empirical requirements of QM | Must reproduce their observable
    consequences"; "Imported mathematical or modeling assumptions | Challenge individually; don't assume they are necessary". For each negative
    result: "Which assumptions were essential to the failure?" "Are those assumptions native to OI, experimentally required, or imported from existing
    theoretical frameworks?" "Does removing an imported assumption eliminate the obstruction?" "Can we construct a counterexample that satisfies the
    same observable requirements without that assumption?" "Does the failure actually concern all OI models, or only the specific model tested?" And:
    "The preregistered outcomes should remain unchanged. Any broader conclusion should be separately qualified, and new variants should be tested in
    new rounds rather than retroactively modifying the original experiment."
  - *Owner chat, 2026-11-08, later (relayed by the coordinating session; not yet recorded on #1169):* "Continue the approved sequence unchanged. I would
    not introduce another round or change M-ARC's acceptance criteria now." The final question the synthesis must answer: "Which apparent obstacles
    survive when we retain only native OI principles and genuinely observable quantum requirements?" Significance tiers, as relayed: (1) an imported
    assumption causes an apparent obstruction → we identify an unnecessarily restrictive test; (2) removing that assumption yields a valid OI mechanism
    → we overcome a genuine obstruction in the tested model; (3) the mechanism reproduces the required quantum predictions, measurements and
    composition → we advance toward operational equivalence.
  - Theorem W positivity and F-1 (§6 items 2 and 6) are not in the programme.
- **Inputs (sha256 re-computed).**

| Input | Revision | sha256 | Final review |
|---|---|---|---|
| AUDIT-C1.md (equivalence core) | r3 | `8aaa7518…dfacec43` | REVIEW-C1-r2: ACCEPT WITH CHANGES; four items applied in r3 (C1:703-710) |
| AUDIT-C2.md (scope of no-gos) | r4 + citation fix (file header still reads "r2", C2:1) | `54699d91…e38f80d7f` | REVIEW-C2-r4: ACCEPT WITH CHANGES; its one citation fix is the only diff from r4 (C2:706-711) |
| AUDIT-C3.md (inaccessibility) | r3 | `d143754b…5e40e68b` | REVIEW-C3-r3: ACCEPT; optional n1–n3 applied in §6 below only, not in the audit file |
| AUDIT-C5.md (cross-document) | r2 + nits R1, R2 | `65f844f0…cf50627c` | REVIEW-C5-r2: ACCEPT (on `ff858e47`); the diff is those two nits (C5:145, 204, 548) |
| ../gate/GATE-DRAFT.md | r4 | `a5d42f92…acf936` | REVIEW-GATE-r3: ACCEPT WITH CHANGES; r4 takes R3-B1/R3-B2 verbatim (diff r3→r4 re-checked) |

- **Snapshot drift.** `origin/main` is now `2cd49dc0` (merge of #1206, MATH-CON-1 design). `git diff 5ce4f98e origin/main` touches no file under
  `papers/` or `book/`; its only change is the MC1 `DESIGN.md`. The gate's MC1 pin `41a42cb9` is an ancestor of `origin/main`, and the file differs
  from the pin at one line (758, a disposition-table row the gate does not cite).
- **Coverage (phase-1 inventories, coverage only).** No input states a C4 cluster or its scope; the cluster numbering skips C4. Unclassified by any
  accepted audit here:
  - priority H: MQ-22 (GR:214), MQ-30 (Str:128) (INV-MANUSCRIPT:41, 49, 69); MQ-09 (Main:684) only as an over-read text (C1:178) and an
    owner-judgement site (C5:337-340); INV-RECON 7.a–7.c (INV-RECON:33-35); the collections INV-RECON 7 and 8 beyond `two-mode-drive.md` (C1:193, 296)
    and 8.a (C2 §15);
  - priority M, which the owner's guide assigns to measurement and Born-rule results (BRIEF.md:43): MQ-04, -05, -06, -08, -10, -19, -26, -38, -39,
    -41 (MQ-41: "unitary emergent statistics are unistochastic", Main:62); INV-RECON 7.d, 7.e, 8.b, 9, 11, 12, 13, 15, 16, 18–22, 29, 36, 37, 39, 44,
    45, 49, 51, 53, 54; INV-TRACKS TI-RT, TI-RS, TB-03, TB-04, TB-05, TB-07b, TB-11, HB-1;
  - the Theorem W positivity pointer, which C3 routes to "a MECH-1-cluster check" (C3:410-411, 568-570) and C2 does not take up (§6 item 2);
  - a candidate paraphrase of Sub:389's "derived rather than fundamental" at ch02:198 = FULL:832, found by the package review (RP:77).

## 2. Headline findings

Outcome 1 = valid as stated, 2 = valid but conditional, 3 = requires new investigation (BRIEF-P2.md:12-19).

1. **S⟺D⟺Q_fb holds and derives no quantum structure.** Outcome 1; n/a for S⟺D, Q_fb leg an imported comparator; kernel `finite_horizon_equivalence`
   (Equivalence.lean:462-468). Q_fb is a function of a Markov chain with kernel |U|² (Equivalence.lean:190-217); at law-class level it adds nothing to
   S⟺D (C1:37-54, 105-140).
2. **The operational reading of "QM emerges under C1–C4" is refuted at its interface.** Kernel counterexample `oi_alone_not_qm`
   (GeneralCarrier.lean:160-163; GR:220-222), scope `Fin 2`, one sealed core, `FiniteOperationalTheory`; one direction only, since full control also
   realizes the core (OIRealization.lean:252-258). Representation reading outcome 1, C1–C4 idle (Main:72, 82(2)). MQ-02's class is imported; the
   theorem itself is n/a (MQ-16, C2:302). A refuted text, not outcome 3 (C1:153-169).
3. **Operational characterizations: kernel 1; statements as made 2; imported.** MQ-12: the drive generator `−i(E_ab+E_ba)`, consumed by
   `control_of_phaseFree` (MinimalRepertoire.lean:529, 559), is unnamed. MQ-13: `ExtendsSubstratum` is unused (StructuralClosure.lean:414-417); (a) a
   swaps-and-phases step is unformalized (the kernel assumes full `DrivesElementary` in `hd`); (b) `hc` is missing from the GR:262 box, GR:264 and
   Main:590 (C1:298-304, 351-355).
4. **Main:590's negative clause: outcome 2, conditional; its own citation is vacuous.** `ReadWriteSourced` is unsatisfiable (paper re-derivation;
   recorded on `main`; #1188). Content survives at kernel level on `substratumGen_not_control` (`Fin 2`) and `permTheory_not_control` (every carrier);
   the interface qualifier is absent at Main:590 and mirrors (C2:125-243). `permTheory_not_control` is kept kernel-only by guards R7-SUB and R7-SRCP, and
   the owner decided "do not broaden the two-state result into a universal claim without further proof" (#1188; §5).
5. **No-go coverage of hidden memory is layered.** Kernel: hidden cells in the carrier and fresh uniform ancillas. Paper only: pre-correlated external
   memory (AP1 Lemma 1, enlarged carrier). Encoded identifications: outside, representation only (C2:51-89).
6. **Act 45 (R-I2).** Kernel verdict: trivial-ancilla dilations under the uniform initial law have slice-determined fixed-basis laws (act-45
   result.md:3-5, 11-26). Exact-arithmetic probe, replayed in CI, not kernel and not in the verdict: two dilations of one slice sharing every column
   entering the slice separate at two steps with an ancilla carried as hidden basis states; a tensor-factor ancilla does not (result.md:5, 30-39;
   kernel anchor `padData_rooted`). Main:646 layers this; ch19:289-291 does not (C1:620-635).
7. **Inaccessibility is a joint property of a native step and a supplied interface.** Symmetric center-free linear step at `q = 2` (necessary) plus
   SA-1: P2 with full support → single-time isotropy; P1, supplied and not enforced natively (AP1:338-343) → retention. Lemma Q(iii) outcome 2 (support
   used at AP1:547, absent from QA:460-474; 1 on AP1's P2 reading, C3:262-264), conditional, paper. M-INACC-1 exposures outcome 1, equally
   interface-relative, WIP/UNVERIFIED (C3:35-59, 224-265).
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
| MQ-14 no state mixing | Main:590 (+ mirrors) | `substratumGen_not_control` (`Fin 2`), `permTheory_not_control` (kernel; kernel-only under R7-SUB/R7-SRCP); own citation vacuous | 2 | conditional | Main:590; GR:260; FULL:500, 5271; ch01:165; ch19:126; source-audit.md:199-200; Intro:129 headline (C2:228-243) |
| MQ-15 layer flow | GR:266-274; Main:590 | `obs_not_layerFlowExecutable` (kernel) | 1 | conditional | none |
| MQ-16 bare OI ⇏ QM | GR:222; Intro:127 | `oi_alone_not_qm` (kernel) | 1 | n.a. | none |
| MQ-18 classical dimension | Main:560 | paper + HKLP import + exact probe | 2 | conditional | none established; r1 charge withdrawn (C2:330-341) |
| MQ-20 Bell ceiling | Main:366-395 | paper + exhaustive 16-table check | 1 | conditional | none; restatements carry hypotheses |
| MQ-23 2×2 no local lift | GR:194 | `twoByTwo_no_local_lift` (kernel) | 1 | imported (target) | none |
| MQ-17 ε-gluing | Main:566-584 | paper + exact probes | 1 | imported | outside MQ-14's statement (C2:434-437) |
| PROG F1 retirement | PROG:40, 521, 634 | `frozen_sourcing_verdict` (kernel) | 2 | conditional | PROG:40, 82, 521 (definitional, `rfl`); :634 clarity only (C2:465-473) |
| TI-D Arc D RD1 | arc-d result.md:124-131 | kernel (53 results) | 1 | conditional | none |
| TI-CR causal readback | causal-readback result.md:18 | exact witness | 1 | n.a. | none |
| IF-L3B | l3b result.md:13-15 | exact integer | 1 | n.a. | none; R_LL and 3A inputs off-repository (C2:543-546, 844) |
| MECH-2 Lemma F, U2, NC | M2D:109-111 | paper | 2 | conditional | — |
| M-INACC framing | M2D:728-733 | enumeration (M2D:706-727) | 3 | conditional | M2D:728-733 |
| MECH-1 selection | M1D:1, 120, 931 | paper (Prop. AS, Thm W) | 2 | conditional, imported comparator | M1D:120, 931 "natively" (C2:628-630) |
| C-CP verdicts | M2D:61-63, 99, 792 | frame-relative | 2 | imported comparator | — |
| 8.a controller | CURRENT-HANDOFF.md:77-80 | paper + exhaustive step 5 | 1 | n.a. | none |

### C3: inaccessibility and hidden-sector modelling

| Claim | Statement site | Where proved | Out. | Class | Over-reading texts |
|---|---|---|---|---|---|
| M-INACC-1 exposure | MI-R:91-96 | explicit protocols, MI-R §§2-3 (WIP) | 1 | conditional | none stronger; MI-R:255 understates; MI-R:84-85, 526-529 (hand-check pointer) (C3:137-141) |
| M-INACC "native instance" | M2D:853-854 | Lemma Q under P1/P2 only | 3 | conditional | M2D:853-854, 947; M2D:728-729 routed to MECH-2 (C3:217-222) |
| QA Lemma Q(iii) | QA:472-474, 51-53, 523-525 | QA:476-495 via AP1 Lemma 3 | 2 (1 on AP1's P2 reading, C3:262-264) | conditional | QA:46 heading; QA:799 status cell; QA:51-53, 523-525 "never/permanently" (C3:266-278) |
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
| C5-5 gap degeneracy | Main:260 vs 262 | Main:260 | contradiction call reading-dependent; Main:262's parenthetical unsupported on either reading (C5:212-214) | no mirrors (C5:234) |
| C5-6 Intro:129 condition 4 | Intro:129 | GR:260 + PhaseSource, `permTheory_not_control` | not a contradiction | citation gap only |
| C5-7 memory → interference | FULL:560; FULL:542, 544, 568; Cplx:236; Str:887 | Main:326, 340, 556, 592, 656 | confirmed per site | owner: FULL:546, 548, 592-596; Main:684 |
| C5-8 single triple | Sub:126; FULL:724 = ch02:90 | Sub:137, 141; Main:560, 566, 598; Intro:133-137 | confirmed (scope) | PC marker corrected (C5:393-399) |
| P1–P3 provenance | composition-access, OI-CHANNEL-1, o-ret | §A.42 item 8 | P1 gap; P2, P3 no gap | C5:406-488 |

### 3.5 Overlaps and differences (noted, not resolved)

- **FULL:690.** C1: an "internal tension" readable two ways (C1:180). C5: a confirmed contradiction on either reading (C5:105-110).
- **Main:684 (MQ-09).** C1 lists it among texts read too strongly (C1:178). C5 marks it "needs owner judgement" (C5:337-340).
- **Common realization.** C1: multi-protocol coverage "only per finite menu to ε" (C1:100, 406, 653). C5: Main:598 is ε-common over all ≤m-outcome
  instruments on ℂ^d at fixed d, K (C5:367-369, 393-398). The package review reads Main:598 as supporting C5's reading (RP:70).
- **H-LIFT, three ways.** The record defines it as "FB's common-lift condition H-C, stated for the identification" (M2D:319-321) and ledgers it
  "Modelling condition (FB H-C)" (M2D:776). C3's AW-C3-5 groups it with H-C (C3:576-577). C2 separates them: H-LIFT supplied by enlargement, H-C the
  genuine exclusion (C2:567-572, 832-835). The gate labels MECH-2 "restricted by H-LIFT" (GATE:148) and states "H-LIFT is not a memoryless-environment
  assumption" (GATE:167).
- **M2D:728.** C3 routes it to MECH-2, "scoped at M2D:109-113" (C3:221-222); C2 decides outcome 3 because the sentence lacks those qualifiers
  (C2:586-593); the gate leaves it undecided (GATE:148).
- **Two-state qualifier at Main:216, 354, 776.** C2 calls its omission minor, resting on an "unstated kernel corollary" (auditor, paper; C2:198-203);
  #1188 records the owner decision "do not broaden the two-state result into a universal claim without further proof" (§5).
- **Intro:129.** C2 flags its opening headline as OI-level (C2:239-243); C5-6 finds the scoped clause consistent (C5:272-277). Different sentences.
- **Main:674.** C3 grades its resampling clause 2 (C3:488-490); C5 finds its "represents" clause literally consistent (C5:337). Different clauses.
  C3's routing of Cplx:236 to an A5 cluster (C3:491-493) is met by C5-7.
- **Consistent:** Sub:126 (C1:415; C5:388-391); Act 45 (C1:620-635; C2:68-72; GATE:151-155).

## 4. Proposed manuscript and record corrections, for the owner's decision only

No replacement wording is drafted. Book mirrors not named by an audit were located by matching the FULL line at `5ce4f98e` and are marked "located"; they
were not audited. Every `.md` site has `.tex`/`.pdf` derivatives (`papers/<X>.tex/.pdf`, `book/…-FULL.tex/.pdf`, C5:19-21); chapter files have none.
Frozen status: `verification/ROADMAP.md` is frozen (§A.36). `verification/programmes/substratum/source-audit.md` declares itself frozen (:191), was
appended after (:211) and is not in `legacy-records.json` (C2:117-120); #1188 calls "several of the records above" frozen, "which only a native round
can correct". The cited reconstruction records (M1D, M2D, QA, AP1, FB, MI-*, states-dynamics, oi-qm-ext-1), PROG and `oi-qm/amendments/amendment-1.md`
are not in `legacy-records.json`, and no receipt names them (checked at `5ce4f98e`). Receipts A45 and L3B make those two records immutable (§A.39).

| # | Finding | Authoritative anchor | Sites (papers / book ch*.md = FULL / derived) | Frozen |
|---|---|---|---|---|
| K-1 | Emergence/equivalence readings of MQ-01, MQ-02 operational reading (C1:134-140, 173-178, 374, 386-389) | Main:72, 82(2), 556; GR:220-222 | Main:68, 206, 682, 776; Main:684 (C1 over-read; C5 owner judgement, §3.5); GR:40, 346; Sub:389, 459; SM:1100 / preface:3 = FULL:64; ch00:39 = FULL:266; ch00:17 = FULL:244; ch00:107 = FULL:334 / Main, GR, Sub, SM, FULL `.tex/.pdf` | ROADMAP:48-52 frozen: mutable record only (§A.42 item 6) |
| K-2 | Definition label, "establishes …", "structures identical" (MQ-03, TB-01) (C1:223-227, 582-584) | Main:218(i), 556, 634, 646 | Main:218, 526, 530, 648, 656 / appendix-b:455 = FULL:6207 / Main, FULL | — |
| K-3 | Characterization boxes as made (MQ-11, -12, -13) (C1:267-269, 300-304, 323-324, 351-363) | kernel statements; GR:216, 228, 260 | Main:564, 590; GR:226, 228, 250, 256, 262, 264; GR:232-236, 252 (mild) / none named by C1 / Main, GR | PROG:72, 80 (mutable) |
| K-4 | Main:590 negative clause lacks interface qualifier (MQ-14) (C2:228-243) | GR:260 reason; `substratumGen_not_control` (`Fin 2`, citable per #1188); `permTheory_not_control` (kernel-only under R7-SUB/R7-SRCP; owner decision in #1188) | Main:590; GR:260; Intro:129 headline / ch01:165 = FULL:500; ch19:126 = FULL:5271 / Main.tex:3915; GR.tex:1850; FULL.tex:2235, 24181 | source-audit.md:199-200 (self-declared frozen, appended; #1188 calls it frozen) |
| K-5 | PROG "the rule contributes no availability" is definitional (C2:465-473) | `rfl`/`Iff.rfl` (C2:78-81) | PROG:40, 82, 521; :634 clarity note only | mutable |
| K-6 | "Visible law" ambiguity and Act 45 layer (R-I2) (C1:633-636) | Main:646; act-45 result.md:5, 30-39 | Main:646 / ch01:187 = FULL:522; ch19:289-291 = FULL:5434-5436 (located); ch19:302 = FULL:5447 (located) / Main, FULL. Located, not audited: FULL:522 also states the carried-ancilla separation without a layer and ends "none of it makes embedded observation and quantum mechanics inequivalent" | act-45 record immutable (receipt A45; not a site) |
| K-7 | MQ-29, MQ-32, MQ-42, TB-BA texts (C1:414-416, 432-435, 455-458, 555) | Main:520-522, 560, 566, 598; Main:218(i), 646 | Sub:126, 137 (its interference clause also in K-15's family); SM:22, 428, 1100; GR:134 / appendix-c:180 = FULL:6409; ch18:116 = FULL:4920; appendix-c:188 = FULL:6417; GR:134's mirror appendix-b:193 = FULL:5945 (located) / Sub, SM, GR, FULL | — |
| K-8 | TI-B "visible stochastic boundary" (minor) (C1:515) | arc-b result.md:13, 50-56 | PROG:195; amendment-1.md:19 | arc-b result.md legacy-listed (not a site) |
| K-9 | GR:450 "theorem of Part I" (MQ-33) (C3:468-475) | Main:50, 268, 650; GR:454 | GR:450 / ch07:256 = FULL:2122 and ch19:116 = FULL:5261 do not repeat it / GR.tex:3016 | — |
| K-10 | Unlabelled hidden mixing (MQ-07, MQ-31) (C3:504-508) | Main:445, 455; FULL:4844, 4856 | Main:674 / ch18:56 = FULL:4860; ch18:58 = FULL:4862 / Main.tex:4848; FULL | — |
| K-11 | C5-1 composite factorization | Main:218, 652 | ch14:50 = FULL:3714 / FULL.tex:17479-17480; GR:330 related | — |
| K-12 | C5-2 visible marginal unitary | Main:342, 650 | Comp:100 / Comp; related softer form ch14:50 = FULL:3714 "unitary evolution under the reduced Hamiltonian" (C5:84-86) | — |
| K-13 | C5-3 QM as Chapter 1 input | Sub:76; Main:68, 556, 564 | ch02:56 = FULL:690 (with ch02:50 = FULL:684) | — |
| K-14 | C5-4 dropped OI_Q scope | GR:288; Main:584, 590, 592 | Main:712; GR:368 / ch07:199 = FULL:2065; ch09:298 = FULL:2765 / Main, GR, FULL | — |
| K-15 | C5-7 memory → interference, QM = observation | Main:326, 340, 556, 592, 656 | Cplx:236; Str:887 / ch01:225 = FULL:560; ch01:207, 209, 233 = FULL:542, 544, 568 / Cplx, Str, FULL. Sweep list: Cplx:276, 348; Medicine:552; ch18:64-72 = FULL:4868-4876; appendix-c:315 = FULL:6544; ch09:16 = FULL:2483; appendix-c:108 = FULL:6337 (C5:342-346); Sub:137's interference clause (C1:416) | — |
| K-16 | C5-8 single triple | Sub:137, 141; Main:560, 566, 598 | Sub:126 (= K-7) / ch02:90 = FULL:724; related Methodology:339 | — |
| K-17 | Record over-readings (C2, C3) | Lemma Q at its scope; Prop. AS; enumeration M2D:706-727 | QA:46, 51-53, 523-525, 799; M2D:728-733, 853-854, 947; M1D:1, 120, 931; AP1:72-75, 732-733; MI-R:255 (understatement) | WIP/UNVERIFIED (MI-R:3-7); not legacy-listed |
| K-18 | C5-5: Main:262's parenthetical ("Ĥ_eff … retains non-degenerate gaps") has no support in the corpus, on either reading (C5:212-214) | Main:260; `source_lift_probes.py:75-77`; `bohr_frequency_probe.py:2365-2368` | Main:262, no mirrors (C5:234) / Main.tex, Main.pdf. Related genericity statements: Main:718; GR:20, 589; FULL:5852, 6176 (C5:218-219, 235) | — |

## 5. Already-tracked items (no duplicate proposed)

- **#1188 KERNEL-VAC-1** (open; amaybaum, 2026-11-07T21:44Z; no comments): `ReadWriteSourced` vacuity, repair or retirement of
  `readWriteSourced_not_qm`/`_not_control`, and repointing of their citations; recorded on `main` at QA DESIGN.md:864-866, minacc-1 DESIGN.md:585, 619,
  RESULT.md:613 and quarter-phase-feedback RESULT.md:187. C2 makes it the home of every citation defect it lists (Main:590, GR:260,
  verification/README.md:298, source-audit.md:100, 121, completion-assumption-audit.md:95, route-b-audit.md:29, RouteB.lean:13, probe and census
  entries) and of the kernel check `not_readWriteSourced` (C2:126-189). #1188 also records:
  - "`permTheory_not_control` / `obs_not_control` … Guards R7-SUB and R7-SRCP keep these kernel-only. Owner decision: keep those guards, and do not
    broaden the two-state result into a universal claim without further proof." R7-SUB (`verification/lean/edge_rigidity_probe.py`, `ok_sub` from
    :3623, manuscript check :3722-3726, registry `kernel-only` with `manuscript == []` :3727-3729, `check` :3751) fails if GR, Main, Substratum, SM or
    FULL contains `permTheory`, `obsTheory`, `SourcedOI` or `SubstratumInterfaceAudit`. R7-SRCP (from :4883; file and token lists :4943-4947; `check` :4970) bars
    `permTheory` and `obsTheory`, among others, from GR, Main, Substratum, SM, ch01, ch19, FULL and the GR, Main and FULL `.tex`.
  - Its proposed round, step 3: "Repoint the manuscript citations (GR:260, Main:590) and correct the frozen records by the native-round mechanism."
  - K-4's prose qualifier is not a citation defect.
- **#1169 ARP** (c.6723277401): ARP-1 M-ARC addresses the outcome-3 claim M2D:853-854; ARP-3 Q-C2-2 addresses M2D:728-733 (§8 item 6).
- **#1193 WAVE-SIGN-1**: the MECH-1 memory sign is conditional on it (M2D:739, 755; C2:624). **#1169** c.6714136234 (owner addendum; support on `main`
  via MID:25-29; GATE:236). **#1206** (merged at `2cd49dc0`), **#1203–#1205** (drafts).
- **F-1 and the source of i**: pursued or located by Q-A (DESIGN.md, PROOF-RECOVERY.md), MECH-2, `two-mode-drive.md:11, 54, 145-147`, PROG:40, GR:250,
  258, MinimalRepertoire.lean:13-25, LieRankSource.lean:36-43, Intro:129 (C1:190-196, 306-312).
- **Recorded open or recorded already:** Q-C2-1(i) at M2D:717-727 (C2:702-703); the M-INACC clause clash at MI-A1:59-70; retrodiction limits at
  MI-A3:21-38, 60-84 (C3:152-155, 253-258); Act 45 layering at Main:646 (C1:627); MQ-20, -34, -35, -40 labels (C2:375-379; C3:494-498);
  composition-access `SCOPE.md:15-22`, o-ret README:40-45 and `bridge-compatibility-audit/result.md:236-246` on provenance (C5:411-488).

## 6. Follow-ups: four authorized by the owner's ARP, two named only

**The owner's order governs:** ARP-1 M-ARC → ARP-2 Q-C2-1 → ARP-3 Q-C2-2 → ARP-4 drive-phase check, executed sequentially, each F and E designated by
the owner, with M-ARC's acceptance criteria unchanged (c.6723277401; c.6723329527; later chat, relayed). Each ARP preregistration carries the
native/empirical/imported assumption ledger and the five questions of c.6723491138; the preregistered outcomes stay unchanged. Theorem W positivity
(item 2) and F-1 (item 6) are not in the programme. The ranking below is the r1 text, kept as written: ranked by expected information per cost, using
the audits' own statements of cost and decisiveness. It does not alter the owner's order.

1. **[ARP-1] M-ARC (C3:165-215; REVIEW-C3-r3 n1–n3 applied).** *Question:* on ring `Z_L` under always-on `N_1` at `q = 2`, window `V` of `w` sites, in
   variant D (a registered cell stays on the ring, its site joins `H`, never re-registered), is any `Q* = 1` linear functional on the current `V`
   determined in a positive-probability branch within the horizon? *Initial state (C3:169-170):* every `V` site holds a P2 ready cell (known value 0,
   or 1 through H-PREP); every `H` site holds a source cell. *Variant I (C3:175-176):* the registered cell is removed from the ring and takes free
   ticks, as in MI's archive (MI-D:357-358); its site is left decoupled. *Assumption tested:* P1's archive isolation, supplied and not enforced natively
   (AP1:338-343), which carries retention for Lemma Q, AP1 Lemma 3, Theorem W and the "native instance" claim (AW-C3-1). *Check:* exact `F_2` span
   membership over every registration schedule up to `T` (≤ 1 slot of one `V` cell per tick, each cell once, no refills or swaps); `w = 3`, `T = 4`,
   `|H| ∈ {4, 6}`; N2 does not enter. *Controls:* CC-ISO (variant I reproduces PROT-D); C-NV (n2: in both variants a `Q* = 0` functional on the
   current `V` is determined by one registration); C-SUPP (n1: in variant I an exact-relation pair exposes and a full-support pair with
   `P(w = b) = 3/4`, C3:91-92, gives at most bias); C9 (re-coupling a registered cell in variant I exposes); `T ≤ |H|`, no wrap-around through `H`.
   *Rule, to be preregistered:* Exposure = in variant D (n3) some schedule and tick put a `Q* = 1` functional on the current `V` in the span at both
   `|H|`, controls green; Survival = in variant D (n3) none at both `|H|`, controls green; Size-dependent = the `|H|` disagree; Void = a control fails.
   The n1–n3 wording exists in REVIEW-C3-r3:58-64 and this package, not in the accepted audit; a preregistration would cite REVIEW-C3-r3 for it.
   *Would show:* exposure, that this de-isolated interface does not protect at that size and horizon; survival, protection within that finite model,
   still conditional on P2's support clause, H-PREP and supplied registration. Neither is universal. *Rank:* fully specified; small enumeration
   (REVIEW-C3-r3:32); bears on C3's only outcome-3 item.
2. **[Not in the ARP; open owner decision. C3 pointer, not taken up by C2.] Theorem W R-W positivity, as corrected (C3:407-414, 568-570).** *Question:*
   at odd `q`, does a correlated or non-uniform hidden law, full-support ones included, keep the hypothesis "every ancilla law has a quantum state as its
   R-W image" (M1D:473-474)? *Assumption:* a positivity condition, distinct from determination; P2 load-bearing (M1D:914); R-I3. *Check, controls,
   rule:* none stated by the accepted audit; the `q = 2` sharp-cell argument does not transfer; the r2 review's `q = 3` control reporting a
   non-positive full-support law is provenance only. If that witness holds, the open item is landing and controlling it, not a new search (RP:51).
   *Would show (consolidator's reasoning):* a recorded non-positive law means Theorem W's scope must name the dependence; it would not refute Theorem W
   within its hypotheses or bear on determination. *Rank (consolidator's reasoning):* plausibly one exact check, but controls and rule must be written
   first.
3. **[ARP-3] Q-C2-2, the M-INACC dichotomy (C2:771-788).** *Question:* at `q = 2` with native `Z`/`X` reads only, is there a protocol with (a) a hidden
   functional used by the rule and partially accessible, with a witness for the functional `G_SM` uses in P★; (b) not spanning-certifiable there; (c)
   encoded record statistics with no exact noncontextual model? *Assumption:* the dichotomy rests on an enumeration; an accessible but uncertifiable
   functional falls in neither horn (C2:588-592). *Check:* finite noncontextuality LP on P★'s fragment (P★'s heralded branches and mechanism-off
   stabilizer preparations; native `Z`, `X` reads at the stated record times; only natively certified equivalences; exact rationals); no further
   controls stated. *Rule:* infeasibility refutes the dichotomy for that instance only with instance-specific checks of (a) and (b); feasibility
   closes the instance; P★ fails C-CP, so infeasibility gives a nonclassical fragment that is not quantum. The gate's imitation rule would also
   require a physical-absence proof for non-spanning reads (GATE:76-79); the audit does not cite it. *Rank:* the LP is cheap, but (a) needs a witness
   no record gives (MI-R:41-53 is for `G_σ`, a template only).
4. **[ARP-4] Drive-phase `diagGen_not_control` analogue (W2, C1:659-665, 314-319).** *Question:* in a candidate mechanism, is the phase relation
   between drive generator and exchange basis physically sourced? *Assumption:* "phase-free" covers the primitives, not what they generate:
   `flow(X_ab, π/2)·swap_ab = diag(−i, −i, 1, …)` on D ≥ 3 (audit derivation, exact algebra, reviewer sympy check); the real rotation gives
   `diag(1, −1, 1, …)`, D = 2 the global `−i·I`. *Check:* compute `flow(drive, π/2)·swap`; a relative quarter phase indicates the complex direction.
   Decisive form: prove every available conjugation in the generated theory preserves real matrices, so control fails (LieRankSource.lean:146); a
   zero-diagonal lemma is not decisive (ReachabilitySeam.lean:71-72). No rule is preregistered. *Would show:* real preservation, no control for that
   candidate; a quarter phase locates the complex direction without sourcing it. *Rank:* ELABORATING; `two-mode-drive.md:54, 145-147` already treats
   its candidate.
5. **[ARP-2; precondition: its preregistration must first supply a characterization of the reachable law set `L`, which C2 says the records do not
   state (C2:757-758).] Q-C2-1, narrowed open case (C2:744-758).** *Question:* on the laws `L` reachable from supplied preparations (P2, H-PREP), is
   every encoded-induced unitary octahedral when supplies are non-dyadic or protocols record-conditioned? *Assumption:* dyadic supply, no conditioning
   ("With non-uniform hidden priors the dyadic argument is unavailable", QA:649-650); heralds give other denominators and rows such as
   `(2/3, 2/3, −1/3)` exist. *Check:* none named; it first needs a characterization of `L`. Already settled or settleable: the all-laws form, closed
   negatively at paper level (auditor, re-derived by reviewer); the dyadic unconditioned case, a closable sub-case (reviewer, paper; descent for every
   m, integer control for m ≤ 5 only); AGL(4,2) is a control, not evidence. *Would show:* a non-octahedral case bears on C2:256-260 and stays
   representation-level (C2:83-89); a negative extends the Clifford ceiling to that sub-case only.
6. **[Not in the ARP.] F-1, extended mechanisms (C1:182-196).** *Question:* does an OI mechanism outside the classes of `oi_alone_not_qm` and
   `substratumGen_not_control` generate an operational theory with the five completion conditions, or does a no-go hold for a stated wider class?
   *Check:* per candidate, the `diagGen_not_control`/`substratumGen_not_control` analogue; C1 proposes none beyond the cited records'. *Would show:*
   per-candidate verdicts only; a positive still needs its resources sourced (two-mode-drive.md §1). *Rank:* open-ended and already pursued (§5).

## 7. Gate

EOI r4 (GATE:1-250) is a WIP/UNVERIFIED planning criterion for #1169; it changes no status and edits no record (GATE:3-9). It assigns each claimed
item exactly one class by first matching row: reachable set only (no result), EOI-NEG (negative, with G0 labels *within its stated class*,
*restricted* or *idealization-dependent*), EOI-I (G1 import fails), EOI-N (native; G1–G5 pass with no departure, preregistered criterion), EOI-C
(disclosed departures carried into the conclusion), EOI-0 (remainder); only EOI-N counts as deriving QM from OI, and the operator-level rule caps A-2
constructions at EOI-C (GATE:83-113). MATH-CON-1's reachable set is {EOI-I, EOI-NEG, EOI-0} (GATE:127-129). Retrospectively (GATE:142-151): P-CONTROL
EOI-NEG, within its class (a census null, not a protocol-class negative); P-OBS EOI-NEG, within its class (definition-level LIMIT); M-INACC-1 EOI-NEG,
within its stated class, existential, idealization-dependent on `Π_A`'s supplied resources, containment of the embedded class not stated; MECH-2
EOI-NEG, universal within Lemma F's operation set and H-LIFT, restricted by H-LIFT, containment not stated, with M2D:728's unqualified sentence left
undecided; MECH-1 EOI-C for its imitable stabilizer fragment; P-MIX reachable set only; none reaches EOI-N. K2: EOI-N is closed on A-2 and open in
principle only at configuration level, for a construction whose every preparation, registration, retention, reset and timing is executed by the rule,
with G3 inputs that are framework posits (any prior dependence shown for a preregistered prior class) and a claimed item passing G5; no reviewed unit
meets it, which is a finding about the present record (GATE:177-185). Open owner questions (a)–(e): S1B (recommendation: no change to the round text);
EOI-N certification; G0 countercontrols; comparator frames; placement (GATE:204-221). Its §7 MC1 gap "until #1206 lands" (GATE:232) is closed at the
pinned commit, which is now an ancestor of `main`.

## 8. Owner decisions needed

1. Whether this package, its four audits and the gate are accepted as the reconciled findings: the precondition for any manuscript correction
   (BRIEF-P2.md:51, relayed), and the findings to be incorporated before M-ARC's freeze (c.6723277401).
2. For each of K-1 to K-18: correct or not, and the accountable Issue for each authorized correction (§A.45 rule 6). Within this item:
   - K-4: #1188 step 3 already plans to repoint GR:260 and Main:590; whether the prose qualifier joins that round. Any correction is bounded by R7-SUB,
     R7-SRCP and the owner decision not to broaden the two-state result without further proof.
   - K-4's frozen site source-audit.md:199-200: #1188 calls the affected records frozen, correctable only by a native round; this package and C2 find
     it self-declared frozen, appended after (:211) and absent from `legacy-records.json` (C2:117-120). The correction route.
   - Whether Main:216, 354, 776, which state the no-control result without the two-state qualifier (C2:198-203), enter §4 under #1188's owner decision.
   - K-6: whether FULL:522 = ch01:187 (located, not audited) is in the R-I2 scope. K-18: Main:262's unsupported parenthetical.
3. ROADMAP:48-52 (frozen): whether a correcting reading is recorded, and in which mutable record (§A.42 item 6).
4. C5 owner-judgement readings: which operator G2 is read on at Main:262 (C5-5); FULL:546, 548, 592-596 (C5-7); GR:330's attribution (C5-1); "this
   content" at Main:712 with SM:1472, Str:108 (C5-4); the intended reading of Sub:126 (C5-8).
5. The §3.5 differences: FULL:690; Main:684 (C1 over-read against C5 owner judgement); C1's "per finite menu" against C5's Main:598; H-LIFT (record,
   C2, C3, gate); M2D:728 (C3 routes, C2 decides, gate undecided).
6. Follow-ups: the ARP order governs M-ARC, Q-C2-1, Q-C2-2 and the drive-phase check (c.6723277401). Open: Theorem W positivity (not in the ARP; an
   unclassified hand-off) and F-1 (not in the ARP). Under §A.46 item 4, whether ARP-1 and ARP-3 on #1169 are recorded as the accountable home of the
   outcome-3 claims M2D:853-854 and M2D:728-733.
7. Coverage: whether, and by which cluster, to audit the items listed in §1 (MQ-22, MQ-30, MQ-09, INV-RECON 7.a–7.c and the collections, the M
   items including MQ-41, the INV-TRACKS M items, FULL:832), and what a C4 cluster was or is scoped to.
8. §A.42 item 8: composition-access P1 (support off `main` unless SCOPE.md's location statement is taken as the narrowing; C5:421-424); L3B's R_LL and
   3A inputs (PV-1; C2:543-546, 844), whose record is immutable under receipt L3B, so closure is a new round or a mutable record citing it (§A.42 item 6).
9. Gate: questions (a)–(e) (GATE:204-221), and §7's MC1 row now that the pin is on `main`.
10. Posting: whether this package is posted to #1169, with the §10 table, after the relayed owner quotes (BRIEF.md, BRIEF-P2.md, the later chat) are
    recorded on #1169 with author and time, as GATE:24-25 and 238 require for the gate.

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
  (AW-C5-b); the every-carrier no-control theorems are kernel-only by owner decision (#1188).
- **Hidden prior:** support for determination, product-uniform law for non-bias and per-state bounds, neither for pointwise exposures (AW-C3-2); does
  a hidden law remove a no-go or a favourable fit (SG-1); multi-time root-independent prior is paper-only (W5).
- **Common lift:** H-LIFT, H-C, AP1 Lemma 5's carrier-independent ancilla laws and Level 3's single Γ concern a preparation-independent hidden law
  (AW-C3-5; HC-1). M2D:319-321 identifies H-LIFT with H-C; C2 separates them (supplied by enlargement vs genuine exclusion, spanning certification as
  the transfer); see §3.5.
- **Supplied access:** P2 + step → single-time isotropy, P1 → retention (AW-C3-1); "never/permanently" fail for information moved to archived cells
  (AW-C3-3); state the reading of M-INACC (AW-C3-4).
- **Definitional or unlabelled:** Main Lemma 2's partition is a definition (AW-C3-6); "thermalizes/resampled" as fact (AW-C3-7); genericity fails at
  the permutation limit for the dilated spectrum (AW-C5-f).
- **Matching level:** "visible law" names Γ and the multi-time law; carried vs tensor-factor ancillas (W7); memory is not coherence or interference
  (AW-C5-d). **Other:** MI-1, FV-1, FT-1, PV-1.

## 10. References off `main` (§A.42 item 8)

| Reference | Use in this package | Classification |
|---|---|---|
| AUDIT-C1/C2/C3/C5, every REVIEW-*.md, GATE-DRAFT.md, REVIEW-GATE-r3, REVIEW-PACKAGE (scratchpad) | every finding | support off `main` (gap) |
| REVIEW-C3-r3 n1–n3 and :32 | §6 item 1 | support off `main` (gap) |
| reviewer's `rv4/agl.py` control (via C2:763) | §6 item 5 | support off `main`; a control, not evidence |
| r2 review's `q = 3` control (C3:413-414) | §6 item 2 | provenance only, as the audit marks it |
| PCD, PMD, POD pins `cc453774`, `7d707bb5`, `83eca7cd` (#1203–#1205) | §7, via GATE §3 | support off `main` (gap); not ancestors of `origin/main` (checked) |
| S1B draft r5 (scratchpad, pre-`F`) | §7, via GATE §6 (a) | support off `main` (gap) |
| composition-access packages (C5 P1) | §8 item 8 | support off `main` (C5's gap) |
| L3B R_LL and 3A inputs | §3 C2 table; §8 item 8 | off-repository (PV-1) |
| MC1 `DESIGN.md` at `41a42cb9` | §1; §7 | support on `main` (ancestor of `2cd49dc0`); differs at line 758 only |
| #1188 vacuity record sites (QA DESIGN.md:864-866; MI-D:585, 619; MI-R:613; FB RESULT.md:187) | §5 | support on `main` |
| #1169 c.6714136234 | §5 | support on `main` via MID:25-29 |
| #1188 body; #1169 c.6723277401, c.6723329527, c.6723491138 | §1 standing; §5; §6; §8 | owner records of decisions and authorization; no scientific claim rests on them |
| #1188, #1193, #1203–#1206 as identifiers | §5 | provenance; assigning a gap to an Issue is responsibility, not retention |
| Owner chat relayed in BRIEF.md and BRIEF-P2.md (R-I1–R-I4, "main risk", the three questions, "No manuscript corrections …") and the later chat relayed by the coordinating session | §1; §6 | provenance; verbatim as relayed; no #1169 comment through 15:40Z records them (checked); to be quoted from a #1169 record with author and time before posting |
