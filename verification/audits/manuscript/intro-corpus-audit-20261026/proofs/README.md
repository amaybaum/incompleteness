# Step 9: independent proof reviews

PLAN.md step 9 has independent reviewers check, line by line, the written-only proofs that the Introduction's central results rest on. Each review is in its own directory: verdicts first, then the statement as proved, the gaps, the counterexample attempts with their scripts, and proof correctness and physical interpretation kept apart. The coordinator re-ran every reviewer's scripts under `python3 -I -B`. Each review's header says what was re-run, and the outputs reproduce. The corpus is read at `eae01647` and the Introduction at `4a260ca9`.

| Directory | Object | Verdict |
|---|---|---|
| `eps-realization/` | ε-realization: Main.md:544, :560, :576–:580 | ACCEPT WITH CHANGES |
| `independent-prior/` | finite-horizon process dilation and its Extension: Main.md:496, :498, :715 | ACCEPT WITH CHANGES |
| `cp-indivisibility/` | CP-indivisibility, framework scope: Main.md:322–:334 | ACCEPT WITH CHANGES |
| `pinsker-bound/` | accessible-backflow lower bound: Main.md:160–:172 | ACCEPT WITH CHANGES |
| `bha-c1-c3/` | BH-01 C1–C3, Lemma 0, Lemma L, D1–D3 | ACCEPT WITH CHANGES (C1 ACCEPT; C2 and C3 ACCEPT WITH CHANGES) |
| `readback-recurrence/` | history readback plus finite recurrence implies indivisibility, with the stochastic-inverse lemma: Main.md:133–:139 | ACCEPT WITH CHANGES |
| `hidden-memory-theorem2/` | unavoidable hidden predictive memory (Theorem 2) and its Corollary: Main.md:99, :582–:598 | ACCEPT WITH CHANGES |
| `bell-ceiling/` | Bell ceiling for a screened local completion, with the cone lemma: Main.md:356–:394 | ACCEPT WITH CHANGES |

The first five were required by PLAN.md step 9. The last three came out of the disposition triage (`dispositions.json`, below) as central written proofs and were reviewed for that reason. No review rejects a proof outright. One finds a step that its own counterexamples refute (S9-M1), and others find statements that say more than the proofs reach.

## The findings, by class

Each finding has an ID, its source review and section, the sites it affects, and its disposition:
- **I:** an Introduction change, in FINDINGS (a);
- **C:** a corpus correction, in FINDINGS (d), PR-I;
- **#944:** an input to the whole-framework audit;
- **#945:** the research follow-up.

### Mathematical errors: a stated step or claim is false

| ID | Review | Finding | Sites | Disposition |
|---|---|---|---|---|
| S9-M1 | eps G1 | The negativity-ledger step fails: normalization amplifies negative mass. Exact counterexamples to the per-parent bound 4ηs + 8ν are d = 3, 5.0007 against 4.0002, and d = 4, 8.0022 against 4.0016. The finite-b constants, capacity figures and Summary 4's "at finite b" are unproved. The exact-regime results hold. | Main.md:556, :558, :576, :580 | C; #944 A1; #945 |
| S9-M2 | eps G2 | "Hidden capacity is independent of the net size \|N\|" holds only in fixed point. The ε-budget is exact-regime only. | Main.md:576 | C; #945 |
| S9-M3 | prior G3c | "The equivalence is between rational laws and finite realizations with rational priors" is false. Counterexample: a rational point-mass μ_H with an irrational visible initial law. | Main.md:496 | C; #944 B1 |
| S9-M4 | memory §4 | Main:594's diagnosis is wrong. Over bijective realizations the infimum of I(X_<t; H_t \| X_t) is H(X_<t \| X_t), so M_det = M_t fails at every hidden dimension, not only at fixed dimension. | Main.md:594 | C; #944 C2 |
| S9-M5 | bha gap 3 | The package's MANUSCRIPT-AUDIT (ch07 L12) says zero-advantage bijections exist "whenever the inaccessible endpoint set has at least \|M\| joint values". This is false: at \|M\| = 2, \|K\| = 3 none of 720 exists. The condition is N ≤ \|A\|·⌊\|K\|/\|M\|⌋. | `bh01_access_v1/MANUSCRIPT-AUDIT.md` | C |
| S9-M6 | bha gap 2 | "A single B–D coupling step defeats recovery" is one example, and false if read universally: 8 of 24 coupling steps preserve recovery. | BHa REPORT.md:61–62 | C |
| S9-M7 | cp G9 | Introduction L106, "no unconditional implication holds", is false. With a full-support initial law, P-indivisibility implies M_t > 0 for some t; this holds on all 3,924 instances. | Intro L106 | I (R-02, already required) |

### Correctable assumptions: the proof holds once a hypothesis or definition is stated

| ID | Review | Finding | Sites | Disposition |
|---|---|---|---|---|
| S9-A1 | recur G1, G2 | Rooted maps Γ_t must be defined for every root, under the shared prior. If rows exist only for realised roots, the theorem is false: 152,808 cases at (2,4). Periodicity is used but not stated. | Main.md:137–139 | C; I (R-37) |
| S9-A2 | bha gap 1 | "Zero advantage requires \|K\| ≥ \|M\|" needs a uniform message prior or equal-size supports. The bound P_succ ≥ 1/\|K\| needs neither. | BHa REPORT.md:42–47; Intro L160 | I (R-35); C |
| S9-A3 | pinsker gaps 2, 3 | The strict bound needs p0 > 0 and δ > 0. TV must be defined as ½‖·‖₁: read with ‖·‖₁, the bound is false by a factor of 4. | Main.md:167; Intro L77, L84, L90 | I (R-38); C |
| S9-A4 | memory §1, gaps | Posteriors must be of positive-probability histories. "Hidden prior" at :582 should be the initial law on C_V×C_H. The range is 1 ≤ t ≤ K−1. | Main.md:582; Intro L82 | I (R-36); C |
| S9-A5 | memory gaps | "(C3) as (c) itself" is insufficient; (C3) follows from `c3_necessity`, the whole-future argument. Counterexample: X_3 = X_0 with the rest i.i.d. gives M_1 = 0, while (C3) needs 1 bit. | Main.md:592; Intro L86 | I (R-36); C |
| S9-A6 | prior G1, G2, G5, G6 | Null contexts need kernels. The step formula holds only for c < K, and the completion needs its counting argument. The Extension's key independence step is asserted; it needs one line. The Extension has no stated size bound. | Main.md:498, :500 | C |
| S9-A7 | cp G1, G2 | The P-indivisibility hypothesis must be stated inline, with the same μ. μ_H must be diagonal, which is load-bearing: SWAP with a hidden \|+⟩ breaks it. | Main.md:322, :326 | C |
| S9-A8 | bell G1–G5 | "Screened" is undefined. Interventions must read and write only their own region, and readouts must be local. The cone condition must be stated; outcomes are ±1 in every run, with no post-selection; the site set must be finite. Loose readings admit CHSH = 4 in CE1–CE4. | Main.md:356–360 | C |
| S9-A9 | eps G3, G4, G6 | G = 0 when m = 1. The c₁K floor rests on ε-faithfulness. The single-dynamics map needs re-padding to be a bijection. | Main.md:560, :576 | C |

### Interpretation errors: the reading attached to a result is stronger than the result

| ID | Review | Finding | Sites | Disposition |
|---|---|---|---|---|
| S9-I1 | recur G5 | On the full-support representative, three conditions are equivalent: (C4) at some order below L; some Γ_s is not a permutation; the family is not P-divisible on {0..L}. So P-indivisibility at recurrence is generic, and a fair coin realised reversibly has it. The readback-driven, memory-discriminating framing is not supported. | Intro L12, L96; Main L20; glossary; FULL L6719 | I (R-37); #944 C1 |
| S9-I2 | memory interpretation | In every bijective realization, I(X_<t; H_t \| X_t) = H(X_<t \| X_t) for every law, Markov ones included. Hidden memory of the past is forced by reversibility. Readout-relevant memory is the visible witness re-described, and (C3) holds unconditionally. | Main §1.5, :592–:598; Intro L82–L88 | #944 C2; step 10 |
| S9-I3 | bell G8, interpretation | The dependency cone moves at 1 edge per step, and the observer-level lift moves at about 1/√3 edges per step (SM:230). Identifying the cone speed with c is unproved. Measurement independence (iv) is posited. Option (a) is fine-tuning in the Wood–Spekkens sense. | Main.md:389, :394; Substratum L130; abstract L22, L630 | C; #944 C3 |
| S9-I4 | pinsker interpretation | "Backflow" is used in two senses: M_t > 0, and BLP divisibility. The lemma proves the first. Main:153's "under (C2), information backflow occurs on observable timescales" goes beyond the lemma. | Main L80, 149, 153, 167, 172, 174, 492, 722 | C; #944 C4 |
| S9-I5 | eps I1–I3 | "The only combination Kochen–Specker permits" is overstated. "Density is the maximum" is misattributed for a fixed experiment, which :460 and :498 realize exactly. "The substratum ontology stated as a theorem" is not supported: the construction is reversible classical simulation with quantum mechanics as an input. | Main.md:550, :560, :580 | I (R-40); C; #944 C5 |
| S9-I6 | cp interpretation | The CP-indivisibility witness is entirely classical: Λ already fails on the diagonal subalgebra. The result does not evidence quantum memory. Within the class the converse fails (CNOT dilation), and "the exact conditions" should read "a sufficient condition". | Main.md:330, :334, :718; book appendix B:92, :96; FULL:5859 | C |
| S9-I7 | prior interpretation | "Time-invariant" holds only because a hidden clock carries the time dependence. (C4) is met by a perfect ledger of the visible past. t ≪ t_R is not controlled. | Main.md:496, :715 | C; step 10 |
| S9-I8 | bha interpretation | C1–C3 are not OI-specific. C1's K = ∅ never holds for an OI observer. The bound 1/\|K\| is classical; the quantum analogue is 1/d². | Intro §5 | step 10 |

### Documentation and evidence-labelling issues

| ID | Review | Finding | Sites | Disposition |
|---|---|---|---|---|
| S9-D1 | pinsker gap 1 | "Certified exactly" describes a floating-point probe on three instances, which cannot detect a factor-2 error in the constant. Other "Certified exactly" parentheticals may share the issue: Main L208, 324, 330, 451, 462, 500, 512, 590. | Main.md:170 and those lines | I (R-03, already required); C; #944 D1 |
| S9-D2 | bell G6 | "Certified in check 11" overstates the check: its controls (b), (c) and `withdrawn_would_allow` are vacuous. | Main.md:377 | C; #944 D1 |
| S9-D3 | cp G3 | "Certified exactly for t = 1…6" cites a one-instance probe. The general proof is `isDiag_Phi`, which is not cited. | Main.md:324; coverage LEDGER | C |
| S9-D4 | eps G1 | Probe check 16 measures raw, un-normalized blocks, so it does not test the step of S9-M1. | `papers/oi_lattice_code/foundations/opglue_probes.py` | C; #945 |
| S9-D5 | bha §Introduction | The 1,376 count needs the same map at every step and cumulative records; with endpoint-snapshot records it is 10,944. The 32 counter-maps need their setup stated. "Sufficient, not necessary" means sufficient for recovery. | Intro L160 | I (R-35) |
| S9-D6 | recur G4 | "With this lemma" (Intro L96) misattributes the machine-checked route, which is overlap plus TV contraction and does not use the lemma. | Intro L96 | I (R-37) |
| S9-D7 | memory gaps | The cross-references at :596/:598 are ambiguous ("clause (ii)"; "the theorem below" points above). The abstract's "one step not machine-checked" undercounts for the Corollary. | Main.md:596, :598; Intro L12 | C; I (R-36) |
| S9-D8 | prior G7, G8 | The ledger's "C2 leg conditional on the mixing hypothesis" conflicts with Main L516. "Arbitrary priors" means arbitrary kernels. | Main.md:498, :715 | C |
| S9-D9 | dispositions | The matrix cites the wrong line in four places: Main.md:16 should be :20; :97 should be :99; :379 should be :389; ch01:265 should be ch01:271–282. | matrix chains | audit-internal |

## The claims re-assessed

The step 9 findings change five matrix verdicts, applied through `matrix/resolutions.json` with the finding cited:
- **I-009, FAITHFUL → IMPRECISE** (S9-I1).
- **I-120, FAITHFUL → IMPRECISE** (S9-D6, S9-I1).
- **I-100, FAITHFUL → IMPRECISE** (S9-A4).
- **I-108, FAITHFUL → IMPRECISE** (S9-A5).
- **I-215, FAITHFUL → IMPRECISE** (S9-D5).

Three other rows are already IMPRECISE, and their reasons are extended: I-103 (S9-A3), I-218 (S9-A2) and I-010 (S9-D7). R-07's proposed text, which carries ε-realization into the Introduction, is revised to rest on the exact regime only (R-40). The verdicts of the other rows these reviews touch stand.

## Dispositions of the other written-only supports

`dispositions/dispositions.json` classifies the 86 paper-derivation sources behind the matrix's proved-paper rows:

| Classification | Entries |
|---|---|
| Part of the reviewed proofs | 10 |
| Central proof, reviewed here | 9 (four distinct proofs: the recurrence theorem, Theorem 2, its Corollary and the Bell ceiling, covered by the last three reviews above) |
| Peripheral proof | 2 |
| Elementary, checked by reading | 20 |
| Cited standard result | 3 |
| Not a proof | 42 |

`dispositions/build_dispositions.py` holds the triage reviewer's classification of each entry, with its reason, and builds the file from `dispositions/input.json` (`python3 -I -B dispositions/build_dispositions.py .`, run from `proofs/`). It regenerates the committed file byte for byte. The coordinator spot-checked four entries against their sources.
