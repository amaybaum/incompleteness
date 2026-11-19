# Independent re-review: Q-C2-1 r8 (ARP-2-QC21)

**Reviewer.** The same independent model reviewer as r6 and r7, 2026-11-09. Read-only, with `gh api` GETs only.

**Probe.** One new exact probe, in `review/probes-r8/`. It evaluates fixture variants of P's construction B (arm-cell
supplies outside the drafted `Adm_B`). P's construction B is already evaluated on paper and by the writer's probe. No
test rule's orbit and no B fragment built from OI data was evaluated.

## Verdict: **REVISE (minor)**

**Structurally, the fixed point is reached.** This pass finds no new design-level blocker:
- P's restated token, the A/B construction, `K`, `mech_change`, `Acc`/TOMO and the D16 restatement are all sound.
- R7-B1 to R7-B5 and r7-N1 to r7-N6 are fixed in substance.

**Two small, mechanical blockers remain.** Each has an exact fix:
- **R8-B1** is a regression introduced by the fix to R7-B3. B-P's `Acc` now reads the phase cell, but QM-P's fragment and
  the paper claim that B-P's token equals QM-P's were not updated.
- **R8-B2.** ABL-SA1b's reported `decide-p` token hides the ablation's own finding: with SA-1(b) dropped, the observer
  learns the path and keeps full conditional fringes.

Once both are applied, I expect the fixed point to hold. A confirming pass on the two edits is enough; a full re-review is
not needed.

## Inputs verified

| file | sha256 | status |
| --- | --- | --- |
| `preregistration.draft.md` r8 | `2c385a97fa28dda60b785e4b445c39f5cf4be400ebfebfc23ecdadf7b9681892` | matches |
| `PLAN.md` r8 | `a2083a69db8436bf9eb1777845b80a592108c030789675b5b619ff2d54e2f6b3` | matches |
| `DESIGN-DS.md` r8 | `7ed08a604588690ac253a8748584c020b3380836c87f61da5038e0939b50c11e` | matches |
| `probes-r8/p_native.py` | `72c4db13ad50c8a3172bb08480493a95d9983a007504ef15077796631f0bb8e6` | matches. Run: the output reproduces every number r8 cites (the kernels, both `mech_change` sets, ABL-ENV-u/v and ABL-SA1b) |

c.6734669526 (2026-11-09T07:29:31Z) corrects the COMP omission on #1169, as requested.

## Reviewer probe

| file | sha256 | what it shows |
| --- | --- | --- |
| `review/probes-r8/adm_closure.py` | `479a10c215619960696904c571b1e68da4b4c59dc448e3e2eeadee6c0834a147` | SA-1(c) says "exactly one known linear functional". Cells whose known functional is `u + v`, `(w, w)` and `(w, w + 1)`, are not in r8's hand-listed `Adm_B`. Both give `V = 0`, `D = 1`, so complementarity holds on them too. The drafted members are reproduced: `(w, 0)` gives `V = 0, D = 1`; `(0, w′)` gives `V = 1, D = 0`; `(w, w′)` gives `V = 0, D = 0` |

***

## Status of the r7 findings

| r7 finding | status | note |
| --- | --- | --- |
| R7-B1 (analytic step 5) | **fixed** | the token is on class-level complementarity; the shams gate nothing; "no single suppression attributable, in any theory"; both A/B readings; QM-P's purified arm; D14(d) drafted with each option's consequences |
| R7-B2 (A; P3; `mech_change`; ablations) | **fixed** | `A_P` = B minus SA-1(c), with its scaffolding named; "no substratum-only P" stated; P3 and E-iso typed as dynamics; `mech_change` computed, with MECH-FIX; the fixtures are exact (ABL-ENV-u and ABL-ENV-v split) |
| R7-B3 (`Acc`, TOMO, A's claim) | **fixed, with one regression (R8-B1)** | `Acc(B-P)` is an explicit nine-setting list; `lp_reads_equal_acc` added; B-REG extended; TOMO's `Ω_c` is defined on the read slots; NC-F imitability is withdrawn |
| R7-B4 (`K`) | **fixed** | a kernel. Verified that PL-SPI gives the constant kernel `{0: (1, 0), 1: (1, 0)}` |
| R7-B5 (D16) | **fixed** | marker reads and the eraser are admitted under every option; D16 is limited to C's end-of-run carrier meters |
| r7-N1 to r7-N6 | fixed | c.6734561591 quoted; the `null` convention; access-relativity of `D`; PL-SPI labelled a P2 departure; Lemma P's line; AP1 Lemma 3 cited |

***

## Blockers

### R8-B1. B-P's nine-setting `Acc` reads the phase cell, but QM-P has no phase register (regression)

- `Acc(B-P)` now includes reads of the phase cell `p`: the settings M01, M02 and M11–M22.
- QM-P's fixture has a phase *gate* `Z^φ`, with no register to read.
- Three statements are therefore undefined or unsupported for the new `Acc`:
  - QM-P's "B-P-shaped fragment decided with a verified certificate";
  - the paper equality "B-P's table equals QM-P's column by column";
  - PLAN §2's "B-P's token equals that of QM-P's fragment, by paper equality".
- QM-P is a frozen control, and a control with an undefined fixture cannot be decided before `F`.

**Fix** (either one):
1. Give QM-P a phase register with a stated map to B's phase cell. B's phase coupling is the reciprocal coupling with a
   known `u = φ`: it leaves `(z + v_p, φ)`, a masked path copy, as SH-0 does. Re-derive the column equality on paper for
   all nine settings.
2. Restrict `bp_equals_qmp`, the QM-P fragment and PLAN §2's sentence to the `p`-free settings M00, M10 and M20, and say
   that the `p`-reading settings have no QM counterpart in this round.

### R8-B2. ABL-SA1b's reported token hides the ablation's finding

- ABL-SA1b registers both slots of the held marker together with the screen. The probe shows a conditional `V = 1` given
  both slots, with the path-record slot in the same joint record. In each subset the observer knows `z` and sees a
  deterministic, phase-dependent port. That is joint path and phase knowledge, the sharpening of AP1 C9.
- So complementarity fails *at the observer level* when SA-1(b) is dropped.
- But `ablate-p` reports "the token `decide-p` gives with `Adm_B` replaced by the ablation's class". `Adm` is unchanged
  for ABL-SA1b, so the printed token is **P-COMPLEMENTARITY**. Its `mech_change` is empty by construction.
- The frozen output would therefore say the ablation leaves complementarity intact. The A/B accounting would also miss
  the fact that SA-1(b) carries complementarity as seen by an observer who reads the marker, while SA-1(c) carries the
  class-level, unread form.

**Fix.**
- Add an observer-level complementarity field for read-set ablations: over the joint-read subsets, report the
  conditional `V` and the conditional path predictability, and whether both reach 1 in some subset.
- Print "not applicable (access ablation)" instead of the `decide-p` token for ABL-SA1b.
- In ADA Part 2, add: "SA-1(b) carries observer-level complementarity in this model when ABL-SA1b's field shows joint
  path and phase knowledge". Its `dynamics_credit` stays none, as an access restriction.

***

## The five questions

**1. Is the P token §A.29-clean?**
- The decision rule is clean. Steps 1–5 read only measured `V`, `D`, NONABS and SPI over a frozen `Adm_B`, and no D14
  option enters the drafted rule.
- D14(a) and (c) remain on the owner's menu. Their consequence is stated: the choice would fix the token. They conflict
  with §A.29 ("reject any variant that can be adjusted to fit any outcome") and should be labelled so in the menu
  (r8-N1).
- The outcome is already known. P-COMPLEMENTARITY in construction B is an instance of AP1 Lemma 3 [W]: under SA-1(c) a
  fresh cell records iff its `v` is known, iff its `u` is unknown, iff the kernel uniformizes, iff `V = 0`. Both probes
  evaluated it before `F`. So P cannot fail in CI except through a code error or a red control.

**How the disclosure should read at the freeze.** Print it verbatim, as a frozen sentence in every P note text and in
the first paragraph of `result.md`:

> "P's construction-B token, P-COMPLEMENTARITY, was derived on paper before the freeze (AP1 §4.5 with SA-1(c); AP1 Lemma
> 3) and evaluated before the freeze by the writer's probe (`probes-r8/p_native.py`, `72c4db13…`) and the reviewer's
> probes (`review/probes-r6/p_arms_indep.py`, `1e351a74…`; `review/probes-r8/adm_closure.py`, `479a10c2…`). The CI
> evaluation reproduces that derivation under frozen controls. It is a consistency check (§A.23), not a novel
> confrontation, and under item L(i) Level 1's condition was known before the freeze."

r8 carries the disclosure in hazard 1 and PLAN §2, but not in the frozen P texts (r8-N2).

**2. Is `Adm_B` fixed by principle, or chosen so that complementarity holds?**
- It is frozen before computation and is not tuned:
  - every SA-1 class satisfies complementarity (AP1 Lemma 3);
  - the probe shows that the unlisted `u + v`-known cells also record and suppress;
  - no admissible member was dropped to make the predicate hold.
- But `Adm_B` is defined by SA-1(c), and SA-1(c) implies the property. The universality reading is therefore near-analytic
  within B. It checks Lemma 3 on five single cells; it does not test OI.
- Hard-to-vary in the §A.29 sense means it cannot be adjusted after the fact. That holds, because the class is frozen.
  Informative it is not, beyond the code check, and r8 says so correctly through hazard 1 and "SA-1(c), posited".
- Recommendation (r8-N3): generate `Adm_B` by a stated rule rather than by hand. The rule would be every single fresh
  cell admitted by SA-1(c), plus the N2 environment cell. Either include the `u + v`-known cells, or exclude them with
  the reason: AP1's "its other slot is unknown", and the type grading, which assigns each fresh unknown one slot type.
  Either way the outcome is unaffected (probe).

**3. Is `mech_change` operational and independent of the dynamics?**
- Yes. It is computed: for each observed cell `(V, D, K)`, the set of realizing mechanisms (supply × coupling type), and
  whether that set changes. It is separate from the frozen `dynamics_credit` label.
- MECH-FIX gives it teeth. The probe reproduces ABL-SA1c's two new `(1, 1)` cells (sharp supplies, identity and flip
  kernels) and ABL-RECIP's copy-only additions.
- It does not depend on the kind label. It does depend on the declared mechanism grain (supply × coupling type), which
  should be stated as the frozen grain.
- Two small points:
  - The "observed cell" includes the validation quantities `D` and `K`. Call it a "validation cell" (r8-N4).
  - For access ablations `mech_change` is empty by construction. That is correct, but it is why R8-B2's field is needed.

**4. Is B-P's read list consistent with D15 and TOMO?**
- Yes, with one regression (R8-B1).
- The nine settings are exactly the joint registrations of the screen with at most one slot of `a` and at most one slot
  of `p`. The justification is stronger than "SA-1(b)": AP1's type grading also excludes `u + v` reads (no Y read). Cite
  both (r8-N5).
- **TOMO is necessarily red under D15(a).** No setting reads both slots of one cell, so `r_E < 2⁵` on the five read slots.
  B-CONTEXTUAL is then possible, and it would be relative to SA-1(b)'s one-functional-per-cell restriction. That is the
  principled form the owner's typing is meant to judge. State "TOMO red under D15(a)" as a paper fact (r8-N6).
- decide-b's completion list: "every slot of the held cells" should say "registered jointly (SA-1(b) dropped)" (r8-N7).

**5. Can the owner now answer D1–D18 without further design work?**
- Yes for the drafted options. Some alternative options would require a further control-plane revision and re-review,
  and the menu should mark them so (r8-N8):
  - D2(b), a blind P arm;
  - D3(b), the spatial ring;
  - D4(b), NNB quarter phases, which needs the four-setting model specified;
  - D10(b), a separate LP method;
  - D11(b), a second system;
  - D13(b), a mixed arm;
  - D15(b), a restricted `Acc`, which has no concrete list.
- D15(b) should offer concrete candidates, for example r6's M1–M3 (screen × arm slots only), each with its typing.
- D14(a) and (c) are as in question 1. D12 is a requirement, not a choice.

***

## Nits

- **r8-N1.** D14 menu: label (a) and (c) "conflicts with §A.29: the choice fixes the token".
- **r8-N2.** Put the freeze disclosure (question 1) in every frozen P text and in `result.md`.
- **r8-N3.** Generate `Adm_B` and `Adm_A` by rule. Include the `u + v`-known cells, or exclude them with the stated reason
  (probe `adm_closure.py`).
- **r8-N4.** Rename the `mech_change` "observed cell" to "validation cell `(V, D, K)`", and freeze the mechanism grain.
- **r8-N5.** Justify `Acc(B-P)` by SA-1(b) together with the type grading (AP1 §4.2: no `u + v` read).
- **r8-N6.** State that TOMO is red under D15(a) a priori, and what that means for a B-CONTEXTUAL.
- **r8-N7.** decide-b's completion list: say "jointly", with SA-1(b) dropped.
- **r8-N8.** Mark the D-options that require a further revision before `F` (question 5).

## What remains for the owner before `F` (once R8-B1 and R8-B2 are applied)

1. **Decisions D1–D18.** The drafted defaults are D14(d); item L, (i) or (ii); D15(a) with its typing; D16(a); D17(a)
   or (b); D18(a). In particular:
   - the owner-typing of the A/B table (*The A/B typing*), as frozen at `F`;
   - the typing of `Acc(B-P)` (D15);
   - the typing of the identifications (D18).
2. **Text to fill.**
   - Inline r5's five authority passages and the full c.6733796760 text.
   - The ARP-1 blobs and the `--verify-round` output for precondition 1.
   - Re-confirm `D` (`fd539e15`).
   - The directory date and governed digest.
3. **D10 copy.** Copy ARP-3-QC22 r13's exact method and gated workflow, with this round's names. Precondition 5's
   independent review must cover the copied text. This review could not see it.
4. **D9 landing.** Land REACHABLE r3 and DESIGN-DS r8 per D9, pinned by blob.
5. **Scripts and gates.** `qc21_check.py` and `controls.py` with self-tests; the design run; the gate tests; the
   benchmark; the Environment settings (D12; ARP-3-QC22 preconditions 2a, 2b, 6, 6′ and 6″).
6. **Labelled paper.** Lemma P and the cone argument remain unreviewed sketches. They are labelled, and CC-NAT's route to
   failure covers them. Accept this or require their review.
7. **Freeze sequence.** The `F` dispatch with its approval entry, and the designation request.

## Fixed point (§A.31)

| pass | findings | classification |
| --- | --- | --- |
| r8-1 | P token, A/B, `K`, `mech_change`: no new structural issue | CONFIRMING |
| r8-2 | R8-B1, a regression from the fix to R7-B3 | ELABORATING (mechanical) |
| r8-3 | R8-B2, observer-level complementarity under ABL-SA1b | ELABORATING |
| r8-4 | `Adm_B` closure (`u + v` cells; outcome unchanged); TOMO red a priori; menu labelling | CONFIRMING |

This pass finds no NEW structural finding. Counting r7's passes 3–4, which were partly ELABORATING, this is the
first full pass without one. The design-level fixed point is therefore reached, subject to R8-B1 and R8-B2, which are
mechanical. A short confirming check of those two edits completes the review.
