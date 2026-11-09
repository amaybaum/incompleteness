# ARP-2 (Q-C2-1) — plan for the native round ARP-2-QC21 (draft r13a)

**Status.** WIP / UNVERIFIED. Model-written. Prepared 2026-11-09 against `main@fd539e15` (ARP-1 landed).

**Review history.**
- r6 was reviewed REVISE (`review/REVIEW-QC21-r6.md`, `facdd215…`).
- r7 was re-reviewed REVISE (`review/REVIEW-QC21-r7.md`, `a9488c6f…`; probe `review/probes-r7/qm_sham_frame.py`).
- r8 applied R7-B1–B5, r7-N1–N6 and the coordinator's decision items (§11). It was re-reviewed REVISE (minor)
  (`review/REVIEW-QC21-r8.md`, `32bec1f0…`; probe `review/probes-r8/adm_closure.py`), and the design-level fixed
  point is reached.
- r9 applies only R8-B1, R8-B2 and r8-N1–N8 (§12). Its confirming check (`review/REVIEW-QC21-r9.md`, `50779a74…`)
  returned ACCEPT-WITH-NITS.
- r9a applied r9-N1 to r9-N4 in place (§13). r9 is kept in `r9/`.
- **r11** applies the r10 re-review (`review/REVIEW-QC21-r10.md`, `b01baa3e…`) and the owner's D12 waiver
  (c.6735159962) (§15). r10 is kept in `r10/`. r11 is not reviewed.
- **r10** builds on the owner's freeze decisions (#1169 c.6735014875, 2026-11-09T07:52:50Z) and continues the approved
  preparation (§14). It is not reviewed. r9a is kept in `r9a/` (preregistration `9692dc40…`, PLAN `63c38e1b…`,
  DESIGN-DS `f4d1c078…`, DECISIONS `df4b5d78…`). No scripts are written yet.

Earlier drafts are kept:
- `r8/`: preregistration `2c385a97…`, PLAN `a2083a69…`, DESIGN-DS `7ed08a60…`.
- `r7/`: preregistration `e75f0bc6…`, PLAN `6bb11f53…`, DESIGN-DS `eea5553b…`.
- `r6/` and `r5/`.

**Not done.** No repository edit, push, GitHub write (only `gh api` GETs), dispatch or designation. No test rule's orbit
was evaluated, and no B fragment built from OI data. The probe evaluates P's construction B, as disclosed.

**Files.**
- `preregistration.draft.md` r8;
- `DESIGN-DS.md` r8;
- `probes-r8/p_native.py` (unchanged) and `probes-r9/olc.py`;
- `r7/`, `r6/`, `r5/`.

## 1. The round in one table

| item | choice |
| --- | --- |
| round | `ARP-2-QC21`, non-sealing; digest `1d195f93…`; `D` = `fd539e15` (to re-confirm) |
| P | Complementarity in construction B's two-path apparatus. Tokens: `P-COMPLEMENTARITY`, `P-RECORD-WITHOUT-SUPPRESSION`, `P-NO-RECORD`, `P-NO-FRINGES`, `P-VOID`. The shams (SH-0, SH-K) are a reported decomposition and gate nothing. Two A/B readings (existence, universality). Ablations report `pred_change`, a computed `mech_change`, and `dynamics_credit` |
| B | Noncontextuality over the fragment's own equivalences, with the LP reading the whole owner-typed `Acc` (B-P: nine SA-1(b) joint settings). TOMO on the read slots' charged configurations. Construction A's B result is measured, not predicted. Tokens: `B-CONTEXTUAL`, `B-CLASSICALLY-IMITABLE`, `B-VOID` |
| C | As r7: the U′ gadget, `K ∈ {6, 12}`, W-CL on both frames, ABL as dynamics, C-A `reg = none`, L-UPRIME used. Tokens unchanged |
| levels | 1 = P-COMPLEMENTARITY (D14 item L: or `V(off) > 0`). 2 = also B-CONTEXTUAL on B-P, with its LP reading the owner-typed `Acc`. 3 = also C-EXPOSURE (the D17(a) qualifier is printed). 4 = not tested |
| governance | ARP-3-QC22 r13's gated two-job pattern (c.6726548830), copied per D10 |

## 2. Paper expectations, disclosed (owner element 6; §A.23)

**P, construction B** (AP1 §4.5; writer's and reviewer's probes): P-COMPLEMENTARITY.

| arm | V | D | K |
| --- | --- | --- | --- |
| off | 1 | — | identity |
| on | 0 | 1 | uniformizing |
| SH-0 | 1 | 0 | identity |
| SH-K | 0 | 0 | uniformizing |

The eraser recovers fringes for the marker and the dephasing arm alike.

**P, A/B.**
- Existence: both succeed. The marker is admissible in `A_P` and in B.
- Universality: `A_P` fails (four sharp supplies) and B succeeds, carried by SA-1(c), which is posited.

**QM and classical waves** give P-COMPLEMENTARITY under P's rule. QM's purified dephasing has `D = 1`; classical noise has
`D = 0`.

**B.** Construction A is measured; Lemma NC-F applies only if `d = r_S = r_E`. On the `p`-free settings M00, M10 and
M20, B-P's table equals QM-P's by paper equality. The six settings that read the phase cell have no QM counterpart in
this round, because QM-P has no phase register (R8-B1, fix 2). No B token is predicted.

**C.** CC-NAT: no witness (Theorem C, conditional; Lemma P, sketch).

## 3. ADA summary

| construction | ingredients |
| --- | --- |
| A (established native) | bijective symmetric second-order step; free tick; `q = 2`; affine rule choice; RET-w |
| B, candidate strengthened | SA-1(c) (posited); N2; H-PREP; SA-1(b); isolation and non-reading of the held marker; L-ACC; forward conditioning and refills (C) |
| B, dynamics rows | **P3 arming and E-iso (control of couplings; credited with a different mechanism)**; NNB (supplied premise) |
| `A_P`'s untested scaffolding | P3, E-iso, N2, H-PREP, terminal screen, L-PATH, L-PORT |
| imported representation | L-PATH, L-PORT, L-CAL, L-UPRIME (D18) |
| imported quantum structure | Englert's bound; the Clifford class; QM-P; the supplied gates (controls and comparators only) |
| change of dynamics | the non-affine `g` (C's ABL) |

## 4. Relation to the earlier work

Unchanged from r7 (`DESIGN-DS.md` §7).

## 5. Probe

| file | sha256 | finding |
| --- | --- | --- |
| `probes-r9/olc.py` | `991b5219b565276515aa59171415b2ebb9c6bc925eb425de0dc452aab312200f` | `OLC` for ABL-SA1b: `(V, Pz) = (1, 1)` in all four joint subsets, so `OLC.joint` is true; the slot-wise `Adm` generated by rule |
| `probes-r8/p_native.py` | `72c4db13ad50c8a3172bb08480493a95d9983a007504ef15077796631f0bb8e6` | the kernels (PL-SPI: the reset kernel `x_after = 0`, distinct from the identity of off and SH-0 and from the uniformizing kernel of on and SH-K). `mech_change`: ABL-SA1c changes two `(1, 1)` cells (sharp supplies); ABL-RECIP adds the copy-only mechanisms. ABL-ENV-u gives SH-0's values and ABL-ENV-v the marker's. ABL-SA1b: conditional `V = 1` given both held slots, with the path in the same record. **Evaluates P's construction B** (disclosed) |

## 6. Owner decisions at the freeze (decided in c.6735014875; the table below is the option menu as presented, kept for reference)

Already decided: indirect access is the only decisive interface (c.6733711272).

| # | decision | options and consequences |
| --- | --- | --- |
| D1 | r5's direct-access arms | (a) keep as labelled diagnostics; (b) drop |
| D2 | P's non-blindness | (a) run as a consistency-axis check of a paper derivation (disclosed); (b) add a blind P arm (NR-10) **[needs a further revision and re-review before `F`]**; (c) defer P |
| D3 | P's geometry | (a) encoded path; (b) also the spatial `F_2` ring (NR-13) **[needs a further revision]** |
| D4 | phase set | (a) `{0, π}`; (b) also NNB quarter phases on U′ (NR-12) **[needs a further revision: the four-setting model is not specified]**. Consequence of (b): NNB, a dynamics row, enters `Adm_A` and `Adm_B`; `ablate-p` gains ABL-NNB; four settings; P stays at Level 1 at most |
| D5 | C's detectors | (a) native-rule detectors (L-HET); (b) one homogeneous rule (AND and NAND blind); (c) drop `S_Y` |
| D6 | composition horizons | (a) `K ∈ {6, 12}`; (b) other |
| D7 | B's fragments | (a) B-P plus B-C for flagged instances; (b) B-P only |
| D8 | eraser | (a) required (drafted); (b) an owner waiver |
| D9 | `DESIGN-DS.md`'s landing | (a) a separate paper record before `D`; (b) in the record directory |
| D10 | LP method and workflow | (a) copy ARP-3-QC22 r13's; (b) a separate method **[needs a further revision]** |
| D11 | composition with a second system | (a) a later round (NR-11); (b) this round **[needs a further revision]** |
| D12 | Environment | a requirement, not a choice: ARP-3-QC22 precondition 2b (E-ID, E-READ, E-BIND) for `arp2-qc21-decisive` |
| D13 | intermediate marker strength | (a) report the finding; (b) add a mixed-setting arm **[needs a further revision]** |
| **D14** | **the shams' role, and Level 1's reading** | **(d) drafted:** both shams are reported as a decomposition and gate nothing, so the token is the same under every choice (§A.29-clean). **(a)** gate on SH-K. **Conflicts with §A.29: the choice fixes the token.** Since `K(SH-K) = K(on)` forces `V(SH-K) = V(on)`, the gate fires whenever the on arm suppresses, in QM, classical waves and construction B alike. The choice would then fix the token, and with item L(i) no Level could ever be awarded. **(b)** gate on SH-0: its kernel is the identity, so the gate never fires; it is equivalent to (d). **(c)** both computed, gate on SH-K. **Conflicts with §A.29**, as (a). **Item L:** Level 1 reads (i) P-COMPLEMENTARITY, or (ii) the owner's literal "`V(off) > 0` in construction B, two settings". (ii) is known on paper, and under it Levels 2–3 do not depend on P's class-level predicate |
| **D15** | `Acc` per fragment, and Level-2 eligibility | (a) `Acc` = every SA-1(b) joint registration on the cells the observer holds (B-P: nine settings), read in full by the LP, typed as an access principle (ACC-R2-type, candidate strengthened); (b) a restricted set, with the restriction typed as a principle **[needs a further revision]**. Concrete candidates:<ul><li>(b1) r6's M1–M3: the screen × the arm-cell slots, with the phase cell unread. Typing: the phase cell is traced out (access restriction, ACC-R2-type).</li><li>(b2) M00 alone: P's screen-only interface. Typing: L-ACC.</li><li>(b3) the screen × the phase-cell slots, with the marker unread. Typing: the unread marker (L-HOLD) as part of the traced-out sector.</li></ul>Under (b), Level 2 also requires that the completion "add `Acc`'s remaining effects" does not restore a model. In both (a) and (b), Level 2 requires the owner's typing as established native or candidate strengthened. Under (a), `Acc` is not tomographically complete for the five read slots: it spans at most 18 of 32 functions |
| **D16** (restated) | do C's end-of-run carrier meters count as indirect access? Marker reads, coincidences and the eraser are admitted under every option (c.6733711272 item 3; c.6733796760 element 3; D8(a)) | (a) yes: meters that copy a carrier functional at the end of a run count (drafted). (b) no: only the screen after recombination and held-marker records correlated with it count. Then `S_X` survives as the screen; `S_Z` survives only as a held marker read together with a screen; `S_Y` is excluded unless realized as the screen after an NNB quarter phase. C becomes rebit-like (`x`–`z` plane), as D5(c) |
| **D17** | does B-C count toward Level 2? | (a) no: B-P only. Then Level 3 joins B-P (P's apparatus) with C-EXPOSURE (the U′ gadget), two unrelated instances, and the note prints that qualifier. (b) yes, with the cross-setup qualifier, and Level 3 requires the same C instance's B-C |
| **D18** | typing of L-PATH, L-PORT, L-CAL, L-UPRIME | (a) imported representation, outside the three-way typing; (b) candidate strengthened principles, to be justified; (c) imported, admitted only in a benchmark arm. Consequence of (c): every P and C token becomes a benchmark result, no Level is awardable, and constructions A and B cannot pose P or C |

## 7. Disposition of owner directions

r7's table is carried. Added: c.6734561591 (07:22:01Z), the validation point, quoted and applied through `K` (a kernel
computed from the construction), TOMO and the computed `mech_change`.

## 8. A correction to a record on #1169 (not a text of this round)

c.6734561591's "Applied" note lists CPL and SPI as the r6 audit's exceptions. Its principal exception was COMP, the
sham's comparability, which was asserted rather than validated (r6 B1). r7 and r8 address it with `K`, now a kernel, and
the decomposition. The coordinator may correct the record. This file changes nothing on GitHub.

## 9. Blockers and open items

- **Review.** A re-review of r8 should continue the §A.31 fixed point on P's restated token, on `Acc` after D15, and on
  the computed `mech_change`.
- **Decisions.** D1–D18.
- **Text and records to fill.** ARP-3-QC22's method and workflow (D10); the inlined r5 authority passages and the full
  c.6733796760 text; the ARP-1 blobs and `--verify-round` output; `D` to be re-confirmed.
- **Unreviewed sketches.** Lemma P and the cone argument.

## 10. Steps to `F` (none taken)

As r7.

## 11. Disposition of the re-review of r7 (`review/REVIEW-QC21-r7.md`, `a9488c6f…`)

| finding | disposition | where |
| --- | --- | --- |
| **R7-B1**: P's step 5 analytic; `D` relative to access | P is restated around complementarity.<ul><li>Tokens: P-COMPLEMENTARITY, P-RECORD-WITHOUT-SUPPRESSION, P-NO-RECORD, P-NO-FRINGES, P-VOID.</li><li>The shams are a reported decomposition that gates nothing.</li><li>"Each suppression is equally explained by the accompanying disturbance; what the construction adds is that, in its admissible class, no record exists without that disturbance."</li><li>Dephasing is stated as an equally valid explanation in every theory, and "no path record" is access-relative (QM's purified dephasing `D = 1`; B's `D(SH-K) = 0` under N2). QM-P gains the purified arm.</li><li>D14 is re-posed with (d) drafted and each option's consequence for the token and the Levels; (a) with L(i) awards no Level ever.</li><li>Both A/B readings are reported: existence (both succeed) and universality (`A_P` fails, B succeeds; SA-1(c)).</li></ul> | prereg hazards 1–3, *The question*, *Test P*, *Levels*, controls, *What no outcome shows*, invariants; DESIGN §1, §4; PLAN §2, D14 |
| **R7-B2**: A mislabelled; P3 mis-typed; `mech_change` a label; ablations under-specified | <ul><li>`A_P` = construction B minus SA-1(c). Finding: no substratum-only P can be posed. The scaffolding is named and typed (P3, E-iso, N2, H-PREP, terminal screen, L-PATH, L-PORT) and untested.</li><li>P3 and E-iso are retyped as dynamics (control of couplings), credited with a different mechanism.</li><li>`mech_change` is computed (cells `(V, D, K)` → realizing mechanisms), with `dynamics_credit` as a separate label; MECH-FIX added.</li><li>Ablations frozen as fixtures: ABL-SA1c, ABL-SA1b (both held slots registered), ABL-RECIP, ABL-ENV-u `(0, w′)`, ABL-ENV-v `(w, 0)`, ABL-P3 (not posable). L-ACC's ablation is the eraser and B-P</li></ul> | prereg hazard 4, *The A/B typing*, *The model of P*, *Test P*, controls, ADA; DESIGN §2, §8; probe |
| **R7-B3**: B-P's LP and `Acc`; TOMO's space; A's NC-F claim | <ul><li>`Acc(B-P)` is an explicit list of nine SA-1(b) joint settings; the LP reads exactly `Acc` (`lp_reads_equal_acc`, VOID otherwise), and B-REG is extended to a subset of `Acc`.</li><li>TOMO's `Ω_c` is the joint values of the slots `Acc` reads, charged.</li><li>Construction A's result is measured; "imitable by Lemma NC-F" is withdrawn and qualified by `d = r_S = r_E`, with the preparation side (`r_S ≤ 32` against up to `2⁸`) noted</li></ul> | prereg *Test B*, *Levels*, controls; DESIGN §5.6; PLAN D15 |
| **R7-B4**: `K` not a disturbance measure | `K` is the transition kernel of `x` (from `X±`, both phases). PL-SPI is re-checked: the reset kernel is distinct from the others (probe) | prereg *Test P*, PL-SPI; DESIGN §4; probe |
| **R7-B5**: D16(b) contradicts owner directions | D16 restated: marker reads, coincidences and the eraser are admitted under every option; D16 concerns only C's end-of-run carrier meters; what remains of C under (b) is stated | prereg *The two layers*, *Levels*; DESIGN §1; PLAN D16 |
| D17 note | the Level 3 qualifier under D17(a) is printed | prereg *Levels*; PLAN D17 |
| D18(c), D4(b) | consequences stated | prereg *Levels*; PLAN D4, D18 |
| r7-N1 | c.6734561591 (07:22:01Z) quoted | prereg *Authority* |
| r7-N2 | `n/a` cells recorded as JSON `null`; a conditional `V` with a `null` factor is `null`; the note prints "undefined" | prereg *Test P* |
| r7-N3 | the access-relativity of `D` added | DESIGN §1 |
| r7-N4 | PL-SPI's sharp `(0, 0)` cell labelled a P2 departure | prereg controls |
| r7-N5 | Lemma P: the peripheral spectral subspace line added | DESIGN §6 |
| r7-N6 | AP1 Lemma 3 [W] cited as the labelled paper extension beyond single cells | prereg *Test P*; DESIGN §5.13 |
| record on #1169 | the COMP omission in c.6734561591's "Applied" note is flagged for the coordinator | §8 |

## 12. Disposition of the r8 re-review (`review/REVIEW-QC21-r8.md`, `32bec1f0…`)

| finding | disposition | where |
| --- | --- | --- |
| **R8-B1**: QM-P has no phase register | **Fix 2 chosen.** QM-P's fragment, the paper equality, `bp_equals_qmp` and PLAN §2's claim are restricted to M00, M10 and M20. The settings that read the phase cell have no QM counterpart in this round. Fix 1 was not chosen: a QM register reproducing B's phase cell, a masked path copy together with `φ`, would need its own design | prereg *Test B* (B-P against QM-P), QM-P row; DESIGN §5.6; PLAN §2 |
| **R8-B2**: ABL-SA1b's token hides the finding | Read-set ablations print "not applicable (access ablation)" and report `OLC`: per joint subset, the conditional `V` and `Pz`, and `OLC.joint`. ADA Part 2: SA-1(b) carries observer-level complementarity when `OLC.joint` is true; its `dynamics_credit` is none. Probe: `OLC.joint` is true | prereg *Test P* (`ablate-p`, table), ADA, invariants; DESIGN §8; `probes-r9/olc.py` |
| r8-N1 | D14(a) and D14(c) labelled "conflicts with §A.29: the choice fixes the token" | prereg *Levels*; PLAN D14 |
| r8-N2 | the review's freeze disclosure inserted verbatim, printed first in every P text and in `result.md` | prereg *Frozen P texts* |
| r8-N3 | `Adm_A` and `Adm_B` are generated by rule from the frozen alphabet `Σ`. The `u + v`-known cells are excluded from B, with the reasons (SA-1(c) wording; type grading), and included in A; the outcome is unaffected | prereg *The model of P*, ABL-SA1c; DESIGN §3, §8 |
| r8-N4 | the mechanism grain is frozen as supply × coupling type; "observed cell" is renamed "validation cell" | prereg *The A/B typing*; DESIGN §2 |
| r8-N5 | `Acc(B-P)` is justified by SA-1(b) together with AP1's type grading (no `u + v` read) | prereg *Test B* |
| r8-N6 | stated in corrected form. Under D15(a), `Acc` spans at most 18 of 32 functions on the read slots, so it is not tomographically complete. TOMO as frozen (`d = r_S = r_E`) is red when `r_S > r_E` or the pairing is degenerate, which is not computed before `F`. "Necessarily red" holds when TOMO is read as completeness relative to `Ω_c`. Either way, a B-CONTEXTUAL is relative to SA-1(b) | prereg *Test B*; DESIGN §5.6; PLAN D15 |
| r8-N7 | the completion list says "registered jointly (SA-1(b) dropped)" | prereg *Test B* |
| r8-N8 | the options that need a further revision are marked: D2(b), D3(b), D4(b), D10(b), D11(b), D13(b), D15(b). D15(b) has the concrete candidates (b1)–(b3), each typed. D12 is noted as a requirement | PLAN §6 |

## 13. Disposition of the r9 confirming check (`review/REVIEW-QC21-r9.md`, `50779a74…`)

| nit | disposition | where |
| --- | --- | --- |
| r9-N1 | "(given `|Ω_c| > 18`)" added to the completeness-reading sentence | prereg *Test B* |
| r9-N2 | *Runtime*: `Adm_A` has 12 arms | prereg *Runtime* |
| r9-N3 | `ab-p` enumerates all of `Σ`; self-test asserts `|Adm_A| = 12` and `|Adm_B| = 6`, off arm included | prereg *The controls* (self-test paragraph) |
| r9-N4 | D14 row: "token. Since" | PLAN §6 |

## 14. Disposition of the owner's freeze decisions (c.6735014875) and the preparation items (r10)

| item | disposition | where |
| --- | --- | --- |
| L(i) | Level 1 iff P-COMPLEMENTARITY | prereg *Levels* |
| Level-1 presentation ("Passing a consistency check must not be presented as a new derivation") | a frozen sentence printed with every Level-1 award; hazard 1 | prereg *Levels*, hazards, P text; DESIGN §11 |
| D1–D3, D5–D11, D13, D16, D17 as drafted; D4(a); D15(a) typed candidate strengthened; the A/B typing as frozen | recorded in the decisions table. D1(a) and D9(a) are covered by "Accept recommendations" (c.6735014875), as the coordinator confirmed | prereg *Owner decisions at the freeze*, *Test B*, *Levels* |
| D12 | the owner creates the Environment `arp2-qc21-decisive`; its protection is verified before any decisive dispatch | prereg decisions table, *The workflow edit*, precondition 2 |
| D18(a), conditional | a separate representation ledger for L-PATH, L-PORT, L-CAL and L-UPRIME (what each identifies; why it supplies no dynamics, probabilities or outcomes; its admissible alternatives). REP-INV varies each over its alternatives. The reclassification rule moves an identification to imported, and its tokens to benchmark results, if a variation changes a token, a witness, a contextuality verdict or P's predicate. The REP-PLANT control is added | prereg *The representation ledger*, *Levels*, controls, invariants |
| D14(d), with the attribution rule | the token reads only the off/on contrast and the class predicate. A separate frozen `ATTR` field ("attributable to which-path recording" / "not attributable" / "undefined") is computed from the validation layer and printed beside the token. "Not attributable" in construction B, QM and classical waves is disclosed as a known structural fact. ATTR-FIX is added; CW-P and QM-P expect "not attributable" | prereg *Test P*, P text, controls |
| the three A/B fields | `pred_change`, `mech_change` and `access_only` (computed as the identity of the full world laws), for every ablation and for `A_P` against B. ACC-ONLY-FIX is added | prereg *The A/B typing*, ADA, controls |
| Lemma P and the cone argument | marked "under independent review". A frozen table states what a failed review withholds: for Lemma P, CC-NAT's expectation, and CC-NAT gates nothing; for the cone argument, the "orders 3 or 6" and ENC-G statements. No token depends on either | prereg *Sketches under independent review*, hazard 7, CC-NAT row; DESIGN §6 |
| fill: r5's authority passages | inlined verbatim | prereg *Authority* |
| fill: c.6733796760 | its recorded verbatim text inlined | prereg *Authority* |
| fill: ARP-1 | the blobs at `fd539e15` (receipt, preregistration, result, measurements, both scripts); `--verify-round e064e766…` with the verifier from `fd539e15`, run read-only: `VERDICT  HOLDS`, exit 0 | prereg *Inputs*, precondition 1 |
| fill: `D` | `fd539e15` re-confirmed as `main`'s head via `gh api` on 2026-11-09; re-confirmed again when the PR opens | prereg *The objects* |
| D10(a): copy ARP-3-QC22 r13 | Appendix C copies *The exact method*, *The workflow edit* and *Runs, evidence, approvals* from r13 (`15d90b24…`) verbatim, with five identifier renames and a frozen adaptation table for QC22-specific terms. Not yet reviewed (precondition 5) | prereg Appendix C |

**Still `PENDING`.**
- The record-directory date and digest.
- The RCH path and blob (REACHABLE lands per D9(a)).
- The benchmark.
- The design-run anchors and records, the stress-fixture generator and seeds, and the timeout-test term count
  (Appendix C).
- The two sketch-review verdicts.

## 15. Disposition of the r10 re-review (`review/REVIEW-QC21-r10.md`, `b01baa3e…`) and the D12 waiver (c.6735159962)

| item | disposition | where |
| --- | --- | --- |
| **R10-B1**: Appendix C not self-contained | Copied from QC22 r13 with the five renames:<ul><li>the controls rows F10, ZPT, C-CERT, C-INDEP, C-STATELESS, C-BUDGET, C-NCF, C-SYM, C-EXACT;</li><li>the full self-test block (M-GUARD with the control-B name rules and route allowlist, M-MODE, M-INDEP and the rest);</li><li>*Scripts* (checker modes and keys, the builder's refusal, `derive-run`, `order`, `check --freeze`, controls T, G, R, B, W, DS, X, V, P);</li><li>the stop rule with the host-VOID definition.</li></ul>Preconditions 6, 6′ and 6″ are adapted. A11 and the Environment-only preconditions and gate tests are dropped. Schema adapted (C.5a). The adaptation table is extended. Nothing rests on the scratch file | prereg Appendix C (C.4–C.7) |
| **R10-B2**: one-builder guard; control modes | A single gated entry `s_decisive` and a frozen registry `DECISIVE_BUILDERS` (P's arm classes and ablations, REP-INV, B-P, construction A of B, B-C, C's orbits, ABL, C-A), each with its own refusal. Control B's name rules and the M-GUARD counter cover every registered builder. A frozen per-control mode table (fixture/A or decisive/B) with reasons. The controls header is corrected | prereg *The controls* (*Decisive builders and the guard*, *Control modes*); Appendix C adaptation table |
| **R10-B3**: L-UPRIME; REP-INV's reach | Scope stated: REP-INV tests outcome-neutrality within each symmetry class. Paper confirmation recorded for L-PATH, L-PORT, L-CAL. The non-symmetric test UPR-BC reclassifies L-UPRIME as imported for B-C when the completion "every slot of every cell" restores a model; UPR-BC fixture added | prereg *The representation ledger*, controls; DESIGN §11 |
| **R10-B4**: frame transport | Under recalibration `S`, the encoded transposition is `S P S⁻¹` and `det_enc` is computed in the transported frame. REP-FRAME (C-R60-ODD under all 48) added | prereg *The representation ledger*, controls |
| **R10-B5**: D12 removal | E1–E13 removed in the copy, with the edit log in Appendix C. Claims downgraded from "prevented" to "detected" (scope of guarantee, after merging, the `Λ` window, the latent route). Ref key added to B3, B4's expression, B6's `if:` and the checker's keys; GT-REF added. The activity API is read in every capture. Approval binding re-anchored on the owner's quoted commit, with the edited-comment rule, the authorship rule and the owner's ratification at `E` (fail-closed). A three-way classification table and a session-credential table with per-control independence. The no-deletion commitment (runs, logs, artifacts until `Q`) is restated as an owner commitment at the freeze | prereg *Scope of authorization and detection*, *The workflow edit*, preconditions 2 and 7; Appendix C.2, C.3, C.5, C.6, C.7 |
| r10-N1 | "no sham-specific gate"; C-IFACE rule; ATTR-FIX mutation | prereg *Test P*, controls |
| r10-N2 | registration modelled without meter cells | prereg *The A/B typing*; DESIGN §11 |
| r10-N3 | `A_P` against B: arms matched; an arm in only one class makes `access_only` false | prereg *The A/B typing*; DESIGN §11 |
| r10-N4 | the stale D1/D9 `PENDING` removed from §14 | PLAN §14 |
| r10-N5 | the header states only source spans; no appendix line numbers are claimed | prereg Appendix C header |
| c.6735159962 | quoted; D12 row updated; every Environment element removed; "detected, not prevented" stated | prereg *Authority*, decisions table, *Scope of authorization and detection* |

**Still `PENDING`.**
- The record-directory date and digest.
- The REACHABLE path and blob.
- The benchmark.
- The design-run and confirmation-run records.
- The gate-test record.
- `T0`.
- The stress generator and seeds, budgets and timeout-test terms.
- The sketch-review verdicts.
- The owner commitments, recorded.

## 16. Disposition of the r11 re-review (`review/REVIEW-QC21-r11.md`, `7d81f43c…`), applied in place as r11a

| item | disposition | where |
| --- | --- | --- |
| **R11-B1**: post-landing routes | Three routes are now stated as unobservable after the final capture: (a) a fast-forward push deleting the receipt; (b) deletion and re-creation of the round branch at a pre-`Q` commit; (c) a force-move. They are added to *Limits*, to the three-way table and to the credential table. "Turns them into prevention" now reads "prevents them for the frozen splice, except through three routes that this round does not observe after the final capture". The owner's freeze commitment is extended: after `Q`, no push to, deletion or re-creation of the round branch without a recorded authorization. A note says the output is public from `E`, so this is attestation hygiene, not blindness | prereg *Scope of authorization and detection*; invariants |
| r11-N1 | UPR-BC moved to fixture mode (synthetic records) | prereg *Control modes* |
| r11-N2 | the re-wrap and the heading-level changes logged | prereg Appendix C header |
| r11-N3 | GT-ACT added. The activity API's horizon was observed read-only (oldest entry 2026-02-12T12:35:51Z, the repository's creation). The documented retention is not confirmed and stays `PENDING` | prereg C.7, *Limits* |

## 17. Disposition of the r11a check (`review/REVIEW-QC21-r11a.md`, `eebd2d6d…`), applied in place as r11b

| item | disposition | where |
| --- | --- | --- |
| **R11a-B1**: GT-ACT would VOID the round | GT-ACT runs on a dedicated disposable branch created from `D`, which is not a recorded branch: no pinned checker and no frozen names, so it has no checker-bearing runs. Its activity is read once and recorded in `gate-tests.json`. C.3 states the exclusion and the reason | prereg C.3 rule (d); C.7 GT-ACT |

## 18. Disposition of the proof reviews (r12)

| item | disposition | where |
| --- | --- | --- |
| Lemma P: PROVED, conditional on Theorem C(ii) and L1–L3 (`REVIEW-LEMMA-P.md`, `07170453…`) | verdict quoted; nothing withheld; CC-NAT's basis relabelled; LP-1 wording applied (`conv R(Q) = O` with `R(πQ) ⊆ O`) | prereg *Proof reviews*, CC-NAT row; DESIGN §6, §7 |
| Cone argument: PROVED UNDER STATED EXTRA HYPOTHESES, with STAB the missing one (`REVIEW-CONE.md`, `07bc8fd7…`) | verdict quoted. A reported, non-gating `STAB(K)` field computed exactly at `K ∈ {6, 12}`. Hazard 7, the ENC-G sentence and remark R1's scope sentence made conditional on STAB per instance. r6's `arccos(3/5)` sentence withdrawn | prereg hazard 7, *Proof reviews*, *Obligation C*; DESIGN §6 |
| the review's STAB controls | STAB-FALSE (the `K = 1` certificate `e6719947…` and the `K = 2` certificate `f24a68d9…`, pinned by sha256, copied into the record directory at S1) and STAB-TRUE (the idle round), both in fixture mode | prereg controls, *Control modes* |
| unaffected | W-CL's computation, the C tokens, C-35 and the rational-reach arithmetic | prereg *Proof reviews* |

## 19. Disposition of the r12 review nits (`review/REVIEW-QC21-r12.md`, `dac201a3…`), applied in place as r12a

| nit | disposition | where |
| --- | --- | --- |
| r12-N1 | STAB-TRUE's input is the supplied identity map on the seven QA laws, outside `DECISIVE_BUILDERS`. STAB-FALSE's orbit reconstruction is stated: `O_0` is the seven QA laws; the `K = 1` branch matrix is rebuilt from `q`, `P` and `G`, with `beta` cross-checked; the `K = 2` branch matrix is the field `B` | prereg controls (STAB-FALSE, STAB-TRUE) |
| r12-N2 | L1–L3 added to CC-NAT's route to failure | prereg CC-NAT row |
| r12-N3 | C-IFACE: `decide-c` and `decide-levels` do not reference `STAB` | prereg C-IFACE row |

## 20. Disposition of the implementer's nineteen items (against r11b with the r12 STAB hook), as r13

Kinds (owner, 2026-11-09): **IMPL**, an implementation clarification that preserves the approved mathematical
definitions, controls and outcome rules, applied in the text; **SCI**, a scientific scope change, not adopted, put to
the owner as a neutral decision (prereg *Owner decisions pending at r13*). Implementer blobs `qc21_check.py` `aa9cd82e`
and `controls.py` `b1d4bea4` are references only; the pins are frozen at `F`.

**Feasibility, stated.** With the caps counted as listed (D19 (0)(b)), B-P (32 preparations against 16) is
`out_of_scope`: B is VOID and Levels 2 and 3 are not awarded unless the owner approves D19 (0)(a) (and B-P then has at
most 16 distinct generators, unknown before `F`), D19 (i)(a) or D19 (i)(b). Construction A of B (up to 256 outcomes
against 200) and every B-C fragment (up to 91 preparations against 16) exceed the caps as listed too. Under the copied
consequence (D21 (a)) each such `out_of_scope` halts the whole round with VOID; with D19 (0)(b), (i)(c), (ii)(a) and
D21 (a) the round is VOID by construction.

| # | item | kind | resolution | where |
| --- | --- | --- | --- | --- |
| 1 | caps against decisive sizes | **SCI** | not adopted. D19 (0): how the caps count (implementer's reading, or as listed). D19 (i): raise the caps from SF-1, reduce B-P to 16 preparations ((b1) arms {off, on}, (b2) `φ = 0`, (b3) `X±`), or keep both and accept B VOID. D19 (ii), (iii): construction A of B and B-C. D21: whether `out_of_scope` halts the round. The feasibility facts are stated | prereg D19, D21; C.8 item 1 |
| 2 | step 3 costly at B-P's size; SF-1 of B-P's shape | IMPL | SF-1 defined at B-P's shape (`F_2⁵`, coset laws, `Acc(B-P)`'s 51 effects), its size following D19; SF-2 at B-C's maximal shape. No verdict frozen | C.8 item 2 |
| 3 | replay as byte comparison fails on `dispatch_sha` | IMPL | canonical-JSON comparison with `parameters.dispatch_sha` removed; "not-applicable" exit 0 when no committed file (S1); impossible at `E` (control R). `verdict`'s S1-artifact condition replaced by B6 at `E` | C.8 item 3; rows 50, 51, 54, 57, 66 |
| 4 | no `hashlib`, `cert_sha256` required | IMPL | pure-Python `h_sha256`, own namespace, three FIPS 180-4 vectors in A8 | C.8 item 4; row 61 |
| 5 | `os` at two sites vs refusal in every builder | IMPL | one shared `s_refusal()`, first statement of `s_decisive` and each builder; `os` in `s_refusal` and the `__main__` block; entry `s_entry(argv, environ)` | C.8 item 5; rows 61–64 |
| 6 | `t_builder_refuses` under synthetic environments | IMPL | runs once under A8's real environment; synthetic cases go through `s_mode` and `s_entry` | C.8 item 5; row 58 |
| 7 | "one name per family" | IMPL | `DECISIVE_BUILDERS = (s_build_p, s_build_repinv, s_build_b, s_build_c)` | prereg *Decisive builders*; C.8 item 6; row 64 |
| 8 | `fixtures_mode` from artifact content unimplementable | IMPL (governance control; evidence source changed, rule kept) | marker step A3b "ARP-2-QC21 fixture output is fixture mode" (`controls.py fixture-mode-check`); rule (d) reads its conclusion; artifact digests are provenance; the stress pin is bound by A7 at 6′ | C.2 A3b; C.3; C.8 item 7; rows 48, 49, 52, 53, 55, 56, 60, 67–69; scope section |
| 9 | `"workflow_dispatch"` only in run-classification functions | IMPL | allowed in `SPLICE_*` constants and `run_class_*` functions | C.8 item 8; row 65 |
| 10 | "flagged" C instances undefined | **SCI** | not adopted. D19 (iv): step 2/3/4 conjunctions (implementer's), W-CL conjunctions only, or every instance | prereg D19 (iv); *Obligation C* |
| 11 | references outside the file ("as r5/r6/r7", "adapted to orbits") | IMPL (review point: the orbit adaptations of Appendix B's controls are written out) | Appendix D states every carried passage (inputs, diagnostics, C model, quantities, C texts, common clause, C controls, S4, ADA, NR list, invariants); RC2 defined from REACHABLE §2.3; ARP-1 effect row inlined | Appendix D; body references |
| 12 | QM-P slot-to-basis map; SH-K column fails | **SCI** | not adopted. D22: map slot 0 ↔ `X`, slot 1 ↔ `Z` with CNOT-prepared-marker arms (`|0⟩`, `|+⟩`, `I/2`; all four columns equal, QM side exact, `probes-r13/qmp_marker.py` `efd583bd…`), the same map with QM-P's present arms (off and on equal), or no column comparison. Slot naming (slot 0 = `u` after `t = 3`) is IMPL: `Acc` is symmetric in the slots | prereg D22; *Test B*; DESIGN finding 6 |
| 13 | readings to state | IMPL, except `pred_change` for ABL-SA1b (**SCI**, D23) | L-PATH (β), L-PORT (β), "up to relabelling", ABL-RECIP (11 arms), ABL-ENV-u/v, `decide-b`'s range (B-P and built B-C; construction A reported), QM `D` = trace distance: in the text. D23: `pred_change` for the read-set ablation as a boolean on common quantities, a boolean including added quantities, or a pair | prereg ledger readings; *Test P*; *Test B*; QM-P row; D23 |
| 14 | A3 and B4 need `mkdir -p` | IMPL | both prefixed | rows 46, 47; C.8 item 11 |
| 15 | step 4 feasible with `T > 0` untested | IMPL | fixture B-S4F (`F_2²`, noisy reads, `d = 3`, `r_S = 4`, `m = 4`, `T = 3`; triangle model checked exactly, `probes-r13/s4f.py` `d1e56566…`); M-MODEL uses it for Q+RY's role | B-S4F row; adaptation table; row 59 |
| 16 | CC-NAT gating | IMPL for the gating path; the round-vs-test level of a VOID is **SCI** (D21) | CC-NAT red ⇒ C-VOID; under D21 (a) exit 3 and round VOID, under D21 (b) C alone | CC-NAT row; D21; stop rule |
| 17 | r5 diagnostics cost (≈ 4 × 10⁶ propagations, untimed) | **SCI** | not adopted. D20: keep in full with benchmark SF-D, bound to depth 1, or drop (D1 revised) | prereg D20; C.8 item 2 |
| 18 | `order` and `verdict` await post-`F` inputs | IMPL | inputs stated: stage commits as arguments, `evidence/approvals.json` (schema v1), `T_repo` live, `T0` frozen constant; self-test only before `F` | C.8 item 9; objects; row 70 |
| 19 | `--fixture-output` | IMPL | names the checker run with `--event fixture`; not a flag | C.7; C.8 item 10 |
| cert. | where the `K = 2` certificate lives; STAB-FALSE not in `measurements.json` | IMPL | pinned data files in `evidence/`, read by `controls.py --self-test` (A9) with sha256 checks; the checker reads no file. STAB-FALSE's result is A9's step conclusion, required `success` by `verdict`; not compared by C-STATELESS, by intent (separate process, pinned inputs). 652 KB lands on `main` with the record | C.8 item 12; STAB-FALSE row; objects; rows 70, 71 |

Also: the edit log gains row 45 for the R11a-B1 edit to C.3 made in r11b without a row. r12 is kept in `r12/`, r12a in
`r12a/`. Writer's probes (exact, paper-sized, no decisive data): `probes-r13/s4f.py` and `probes-r13/qmp_marker.py`.

## 21. Disposition of the r13 review (`review/REVIEW-QC21-r13.md`, `43c7cef7…`), applied in place as r13a

| item | disposition | where |
| --- | --- | --- |
| **R13-B1**: #3's verdict change is IMPL only under D21 (a) | #3's second half is reclassified: IMPL under D21 (a); under D21 (b) the S1 binding must be restored. D21 (b)'s required edits gain a frozen `actions/artifacts/{DEC}/zip` template with `zipfile` and `io` (in-memory) and an S1-versus-committed canonical-JSON comparison without `dispatch_sha`, or an equivalent exact S1-versus-`E` comparison; the consequence without it is stated. The `E`-binding by B6 is stated in *The objects* and the note | prereg D21; *The objects*; C.8 item 3 |
| **R13-B2**: D19 is missing options | added before the narrowing option: (0)(c) extreme rays of `cone{a_p}`, decisions unchanged, value unknown before `F`; (i)(d) a covering by sub-fragments of at most 16 preparations, sound and one-sided ("not decided" if all feasible); (i)(e) a different exact facet enumeration, a D10 method change needing its own review. The caveat that `d ≤ 16` can still fail (only `d ≤ 18` known) is stated; the feasibility statement lists the new options | prereg D19, *Feasibility* |

Nothing else changed. The scripts are updated after the owner's D19–D23 decisions.
