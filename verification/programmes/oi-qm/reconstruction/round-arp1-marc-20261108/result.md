# ARP-1-MARC result

- round: `ARP-1-MARC`
- D: `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`
- F: `360de3b64ea3ab8f886b1a0e9798554726300115`
- S1: `d0012c80f367f5b3caa24e239dac679d47eacf26`
- E: the commit that adds this note

## Controls

| code | size | status | raw counts |
| --- | --- | --- | --- |
| CC-ISO | 4 | PASS | I.exposing_V=0, I.exposing_active=0, I.nonisotropic=0 |
| CC-ISO | 6 | PASS | I.exposing_V=0, I.exposing_active=0, I.nonisotropic=0 |
| C-NV | 4 | PASS | D.nv_cases=976, I.nv_cases=1006 |
| C-NV | 6 | PASS | D.nv_cases=976, I.nv_cases=1006 |
| C-SUPP-X | 4 | PASS | supp_x.exposing_V=3726 |
| C-SUPP-X | 6 | PASS | supp_x.exposing_V=3726 |
| C-SUPP-F | 4 | PASS | supp_f.cond_v0_0=3/4, supp_f.cond_v0_1=1/4, supp_f.span_determined=false |
| C-SUPP-F | 6 | PASS | supp_f.cond_v0_0=3/4, supp_f.cond_v0_1=1/4, supp_f.span_determined=false |
| C9 | 4 | PASS | c9.exposing_V=3486, c9.exposing_at_registration=1560 |
| C9 | 6 | PASS | c9.exposing_V=3486, c9.exposing_at_registration=1560 |
| C-DEISO | 4 | PASS | D.step_is_ring_violations=0, d_i_diff_outside_archived=0, D.coupling_cases=4792, I.coupling_cases=0, case_list_sha256.D=fc2a302a9ab5, case_list_sha256.I=fc2a302a9ab5, D.records_kept_violations=0, D.min_rank_I=3, D.knowledge_injections=0 |
| C-DEISO | 6 | PASS | D.step_is_ring_violations=0, d_i_diff_outside_archived=0, D.coupling_cases=4792, I.coupling_cases=0, case_list_sha256.D=fc2a302a9ab5, case_list_sha256.I=fc2a302a9ab5, D.records_kept_violations=0, D.min_rank_I=3, D.knowledge_injections=0 |
| C-XB | 4 | PASS | xb.checked_cases.D=6008, xb.checked_cases.I=6008, xb.checked_cases.C9=6008, xb.checked_times.D=30040, xb.checked_times.I=30040, xb.checked_times.C9=30040, xb.mismatches=0, xb.exposure_mismatches=0, xb.exposing_V.D=0, xb.exposing_V.I=0, xb.exposing_V.C9=3486, xb.all1.checked_cases.D=6008, xb.all1.checked_cases.I=6008, xb.all1.mismatches=0, xb.all1.exposure_mismatches=0 |
| C-XB | 6 | PASS | xb.checked_cases.D=6008, xb.checked_cases.I=6008, xb.checked_cases.C9=6008, xb.checked_times.D=30040, xb.checked_times.I=30040, xb.checked_times.C9=30040, xb.mismatches=0, xb.exposure_mismatches=0, xb.exposing_V.D=0, xb.exposing_V.I=0, xb.exposing_V.C9=3486 |
| M-PLANT | 4 | PASS | plant.D.empty_t0=true, plant.I.empty_t0=true, plant.D.exposing_V=4968, plant.I.exposing_V=4968 |
| M-PLANT | 6 | PASS | plant.D.empty_t0=true, plant.I.empty_t0=true, plant.D.exposing_V=4968, plant.I.exposing_V=4968 |
| C-STEP | 4 | PASS | step.violations=0 |
| C-STEP | 6 | PASS | step.violations=0 |
| C-HOR | 4 | PASS | horizon.T_le_H=true, horizon.radius_violations=0 |
| C-HOR | 6 | PASS | horizon.T_le_H=true, horizon.radius_violations=0 |

**Token:** `ARP1-MARC-SURVIVAL`

In variant D, where the registered cell stays on the ring and its site joins `H`, no case up to `T = 4` places a `Q* = 1` linear functional on the current `V` in the span of the transported known and registered functionals, at `|H| = 4` or at `|H| = 6`. Every control is green at both sizes. In this model, protection of `Q* = 1` functionals on the current `V` survives the removal of the archive's coupling isolation. It does not derive P1, P2 or the support clause, and it is not a statement beyond the stated horizon and sizes. This concerns the finite model of this round: the ring `Z_L` with `L ∈ {7, 9}`, the rule `N_1` at `q = 2`, a three-cell window, horizon `T = 4`, at most one registration per tick and each cell registered at most once. It is conditional on the supplied registration, on P2 with its support clause, and on H-PREP for a known value 1. Determination uses no measure; no statement about bias is made. Agreement of the two ring sizes is not evidence about an infinite chain: at both sizes some sites of `H` are reached within `T` from both ends of the window, which only `|H| ≥ 2T = 8` would exclude. Nothing here concerns other rules, larger windows or horizons, an archive held elsewhere, or a physically sourced observer.

What no outcome shows: it is not a universal statement in either direction; it does not adopt or promote M2D's reading of Lemma Q as an instance of M-INACC, or Lemma Q's labels; it does not change the status of P1, P2, H-PREP or any manuscript claim; an exposure is not evidence that a physically sourced observer could expose, and a survival is not evidence that P1 is dispensable outside this model.

## ADA

**Which direction is the obstruction.** Primary reading: the target is QM-like inaccessibility, a functional the dynamics uses and the observer cannot determine (M-INACC, M2D:832-840). Under it the obstruction is **EXPOSURE**: exposure means that the protection depended on the imported isolation L-ISO. Opposite reading: if the target is taken instead as an observer able to determine what the dynamics uses, the obstruction is **SURVIVAL**. Part 2 answers the five questions for whichever substantive label is measured, under the reading in which that label is the obstruction, and states the other reading beside it. Neither label is pre-judged as favourable. SIZE-DEPENDENT and VOID get no ADA beyond Part 3 and the record of what was measured.

### Statuses

| item | status | kind |
| --- | --- | --- |
| L-ISO | at `|H| = 4`: **removal measured not to expose**; at `|H| = 6`: **removal measured not to expose** | measured |
| L-ACC | at `|H| = 4`: **protection-carrying** (`c9.exposing_at_registration = 1560`); at `|H| = 6`: **protection-carrying** (`c9.exposing_at_registration = 1560`) | fixed by design, read from the recorded count |
| L-P2 | **protection-carrying**: a planted `u + v`-known cell exposes, in both variants (M-PLANT) | fixed by design |
| L-SUP | **protection-carrying in variant I**: a supplied exact relation exposes (C-SUPP-X runs in variant I only) | fixed by design |
| L-PRIOR | **idle for determination**: a full-support correlated law does not determine (C-SUPP-F, variant I, one protocol); it enters no span computation | fixed by design |
| L-HPREP | **idle at `L = 7`**: C-XB's all-1 repeat agrees with the span method (`L = 9` not repeated) | fixed by design |
| L-SWAP, L-PROTB | **absent or not evaluated** | — |
| L-STEP, L-NN, L-Q2, L-REG, L-DET, L-INACC, E-AR | **used, not varied** (E-AR: not used). L-STEP's center-freeness is used by Lemma Q(i) (QA:478-486); its necessity is the records' result (QA:518-521), not measured here | used, not varied |
| L-RING | `|H|` varied (agreement of the two sizes, measured); `w`, `T`, the dimension, the parity of `L` and the archive's adjacency not varied; agreement is not evidence about an infinite chain (`|H| ≥ 2T` would be needed) | partly measured |

### The five questions

**The five questions, for SURVIVAL (the obstruction under the opposite reading):**
1. *Essential to the survival:* L-ISO's removal is measured not to expose. The protection-carrying items, as fixed by the controls' design: L-ACC (C9, exposure at registration time), L-P2 (M-PLANT, both variants), L-SUP (C-SUPP-X, variant I only). Used and not varied: L-STEP, L-NN, L-Q2, L-REG, L-RING.
2. *Their types:* from the ledger, both readings for L-Q2, L-NN and L-PRIOR.
3. *Does removing an imported assumption eliminate it?* Not decided here; removing L-REG or L-P2, or changing L-RING, needs a new variant (NR-2 to NR-4).
4. *A counterexample satisfying the same observable requirements without it?* Not decided here (NR-7).
5. *All OI models, or only this one?* Only this model, as listed for EXPOSURE.

**The witness principle, applied to SURVIVAL.** The note prints, verbatim, the owner's principle: "failure to construct a witness is not proof that no witness exists, unless a theorem establishes that impossibility within a clearly stated scope." A SURVIVAL label is finite and conditional. Within the enumerated scope (the 6008 fixed-schedule cases at each size, `T = 4`, `w = 3`, `|H| ∈ {4, 6}`, the kept assumptions) it is an exhaustive finite computation of span membership, cross-checked by C-XB's direct simulation under the uniform law with known values 0; it is classified as that verification layer. Its extension to every full-support law and every adaptive schedule is a paper reduction (*The exact method*: the knowledge set is affine; an adaptive schedule is fixed within a branch), sound but on paper. Outside that scope it is not an impossibility of exposure. The only impossibility result used here is Lemma Q(iii), and its scope is the isolated archive under P1 and P2 (variant I), not variant D.

**For either substantive label**, the note adds the owner's standard verbatim: "Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still produce valid probabilities, observable quantum predictions and consistent behavior across repeated experiments." Variant D's probabilities, predictions and repeatability are not measured here (NR-5, NR-7).

**Candidate new rounds (named, not run):** NR-1 the archive held away from the window (a non-adjacent site of `H`, or moved), the budget question of AP1:338-343; NR-2 larger `w`, `T`, `|H|`, including `|H| ≥ 2T` (free of two-sided finite-size effects) and `T > |H|`; NR-3 registration through a native coupling to a meter cell instead of a supplied slot read (removing L-REG); NR-4 ready cells prepared by the dynamics instead of supplied (removing L-P2); NR-5 bias (PROT-B) in D under named full-support laws; NR-6 other alphabets (L-Q2), next-nearest-neighbour center-free couplings (L-NN) and the cubic graph (L-RING), as extensions; NR-7 the observable level: valid probabilities, quantum predictions and repeatability of variant D's induced statistics, without weakening the empirical standard.

### Ledger (frozen at `F`)

| id | assumption, as this round uses it | type | source |
| --- | --- | --- | --- |
| L-STEP | second-order, linear, symmetric, center-free update (`k_ij = k_ji`, `k_ii = 0`) | native | Substratum:98, :100 (A4, A5); QA:774-775 |
| L-NN | nearest-neighbour coupling | **uncertain**: QA's ledger calls it "Native, selected branch"; SM calls it an assumption beyond bounded coupling degree (A3). Carried both ways | SM:224-226; QA:776 |
| L-Q2 | alphabet `F_2` (`q = 2`) | **uncertain**: the records call it "Native parameter value, chosen per the owner's instruction"; whether the protection depends on it is untested; carried both ways | QA:462-464; MI-D:595 |
| L-RING | one-dimensional ring `Z_L`, odd `L ∈ {7, 9}`, three-cell window, horizon `T = 4`; the archived site adjacent to the window | imported (modelling reduction of the cubic graph; the odd ring is not bipartite globally, only within the no-wrap cones C-HOR measures; at both sizes some `H` sites are reached from both window ends within `T`) | QA:776 (H-FIN); M-ARC parameters |
| L-P2 | ready cells with exactly one known slot; no supplied cell with both slots, or `u + v`, known | imported (supplied posit; motivation programme-internal) | AP1:297-299, :347-349; QA:780 |
| L-SUP | full joint support of the unknowns (P2's support clause) | imported | AP1:297-299, :547; QA:499-501 |
| L-PRIOR | product-uniform law (N2, H-PS) | **uncertain**: the records call N2 a native measure applied through H-PREP; its use on supplied cells goes through an imported hypothesis | QA:777; MI-D:309, :605 |
| L-HPREP | known value 1 through H-PREP | imported (open hypothesis) | QA:782 |
| L-REG | supplied registration: one slot of one window cell between ticks, at most once per cell, the joint record kept whole | imported (SA-1(b), access part) | AP1:292-296; MI-D:351-365 |
| L-SWAP | refills and archive swaps | imported; **not in this model** | MI-D:361-362; MI-A1:203-213 |
| L-ISO | the archived cell's coupling isolation (P1 terminality) | imported; **removed in variant D**, kept in I. Not enforced natively; enforced within a budget below recurrence only by the supplied P3 and E-iso | AP1:295-296, :338-343; QA:781; MI-D:357-358 |
| L-ACC | the archived cell leaves the window and is not read again | imported (access part of P1), kept in both variants | MI-D:357-360; M-ARC |
| L-DET | "determined" as constant on the support given `K`; PROT-D as the absence of a determined `Q* = 1` functional on active cells | imported (definitional) | MI-D:135-137, :429-432 |
| L-PROTB | PROT-B (no bias) | imported (definitional); **not evaluated** here | MI-D:433-436 |
| L-INACC | the identification of protection with inaccessibility in M-INACC's sense. Reading used (AW-C3-4): clause (b) read as non-determination of a `Q* = 1` functional on the current window (PROT-D); clause (b)'s conditional-law reading (bias) and clause (a) are not tested | imported (interpretive); the identification with this functional is model-specific | M2D:832-840; MI-A1:59-70 |
| E-AR | at most two perfectly distinguishable preparations of a qubit carrier: the observable bound behind L-INACC | empirical; **not tested** in this round (NR-7) | AP1:439, :677 |

### Part 3: the renaming check

Variant D must not carry an imported item under another name. Each row is measured at both sizes and is part of C-DEISO's green criterion.

| imported item | the form it could take in D | how it is excluded |
| --- | --- | --- |
| L-ISO (coupling isolation) | a dropped or weakened edge, a vacancy, a free tick, delayed coupling | (a) D's step is the unmodified ring matrix at every tick; (b) D and I differ only in archived rows and columns; (c) re-coupling reaches the window in D and in no case of I |
| L-SWAP (refill, swap) | a reset or replacement of the archived cell's state; a fresh known cell | (a); (e) no functional is added to `I_t` after `t = 0` (`knowledge_injections = 0`) |
| P3, E-iso | an edge multiplier | (a) |
| narrower access in D | fewer schedules or windows than I | (d) identical case lists, supply patterns included |
| discarded knowledge | a dropped record, or `I_t` not transported whole | (d) `R_t` carries every registration; `I_t` keeps rank 3 |
| a restricted prior | a support restriction in D's supply | (d) identical supply patterns; C-SUPP-X's relation enters variant I only |
| a narrowed target | fewer functionals evaluated in D than in I | the same evaluation rule (every functional on the current window) in both; L-ACC is shared and its effect is measured by C9 |

L-ACC is the archive's access property. It is kept in both variants, named in the ledger, and its effect is measured (C9). It is not isolation renamed: it restricts what the observer reads, not what the dynamics couples.

C-DEISO at `|H| = 4`: D.step_is_ring_violations 0, d_i_diff_outside_archived 0, D.coupling_cases 4792, I.coupling_cases 0, case_list_sha256.D fc2a302a9ab5, case_list_sha256.I fc2a302a9ab5, D.records_kept_violations 0, D.min_rank_I 3, D.knowledge_injections 0.
C-DEISO at `|H| = 6`: D.step_is_ring_violations 0, d_i_diff_outside_archived 0, D.coupling_cases 4792, I.coupling_cases 0, case_list_sha256.D fc2a302a9ab5, case_list_sha256.I fc2a302a9ab5, D.records_kept_violations 0, D.min_rank_I 3, D.knowledge_injections 0.
