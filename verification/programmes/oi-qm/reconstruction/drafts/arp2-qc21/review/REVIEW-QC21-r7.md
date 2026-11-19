# Independent re-review: Q-C2-1 r7 (ARP-2-QC21)

**Reviewer.** The same independent model reviewer as r6, 2026-11-09. Read-only, with `gh api` GETs only.

**Probe.** One new exact probe, in `review/probes-r7/`. It evaluates stabilizer-QM reference fixtures and two 3×3
matrices. It evaluates no OI construction beyond what the r6 probes and the writer's r7 probe already evaluate. No test
rule's orbit and no B fragment built from OI data was evaluated.

## Verdict: **REVISE**

r7 fixes the r6 findings in substance, with few exceptions:
- B2–B7 and the nits are applied correctly.
- The eraser, the C-R60-ODD control and Lemma P's expanded sketch are good.
- C-R60-ODD has real teeth: the fixed frame alone would miss it (below).

The fixed-point search finds five new blockers:

- **R7-B1. P's attribution step is analytic under every D14 option.** The D14 choice decides the token. Under D14(a)
  with Level-1 reading (i), no Level can ever be awarded in this round.
- **R7-B2. Construction A is not "the substratum alone".** P3 is mis-typed as crediting no dynamics. `mech_change` is a
  label, not the test that c.6734374076 asks for. Two ablations are under-specified.
- **R7-B3. B-P's LP does not read its owner-typed `Acc`.** The Level-2 eligibility rule therefore still admits a
  design-chosen subset. Construction A's imitability is not a consequence of Lemma NC-F as claimed.
- **R7-B4. `K` is not a disturbance measure for non-additive arms.** The writer's own probe shows `K = δ0` with `V = 0`.
- **R7-B5. D16(b) contradicts recorded owner directions and D8(a).**

## Inputs verified

| file | sha256 | status |
| --- | --- | --- |
| `preregistration.draft.md` r7 | `e75f0bc6a343cfb5942e0515d650b502ba1a75c3a1b0de69fdee97651f96e6b7` | matches |
| `PLAN.md` r7 | `6bb11f537f8b7e2f4b78222ca0b00c658a127a164757b42bc37c8061284e5b6c` | matches |
| `DESIGN-DS.md` r7 | `eea5553b8515a27cee5ecae76f33938624fc97f1086554280b6fb646ff1f123a` | matches |
| `probes-r7/p_native.py` | `d8fedf5677a829bebe0f612669c68a20ea0ff46aef15f39eaa9c51e527814b84` | matches. Run: its output reproduces every number r7 cites |

**Owner comments read:**
- c.6734304025 (the A/B construction);
- c.6734374076 (the ablation rule; #1210);
- c.6734561591 (07:22:01Z, the record of the owner's validation point, the newest comment).

## Reviewer probes

| file | sha256 | what it shows |
| --- | --- | --- |
| `review/probes-r7/qm_sham_frame.py` | `65524ef28b720583ae75e3cc4cdba667f4f8039afc310aa475599438e136d9c1` | (1) stabilizer QM under P's protocol, exact. (2) the characteristic polynomials for C-R60-ODD |
| `review/probes-r6/p_arms_indep.py` | `1e351a74…` (r6) | in construction B, `V` is a function of the kick law over all nine supplies and the composites |
| `review/probes-r6/b_incomplete.py` | `f02aeaeb…` (r6) | the classical register |

**QM output of `qm_sham_frame.py`.** `V` uses the two phases; `D` is the trace distance between the environment states
given path `|0⟩` and `|1⟩`.

| arm | V | D | reduced path state after the arm (X+ input) |
| --- | --- | --- | --- |
| off | 1 | 0 | `[[½, ½], [½, ½]]` |
| CNOT marker | 0 | 1 | `[[½, 0], [0, ½]]` |
| null sham (X on the environment only) | 1 | 0 | `[[½, ½], [½, ½]]` |
| kick-matched sham (classical noise `w` held; path gets `Z^w`) | 0 | 0 | `[[½, 0], [0, ½]]` |
| purified dephasing (environment `|+⟩`, CZ) | 0 | **1** | `[[½, 0], [0, ½]]` |

**C-R60-ODD.**
- R60 has characteristic polynomial `λ³ − 2λ² + 2λ − 1 = (λ − 1)(λ² − λ + 1)`, spectrum `{1, e^{±iπ/3}}`.
- `P·R60` has `λ³ − λ² − λ + 1 = (λ + 1)(λ − 1)²`, spectrum `{−1, 1, 1}`. That is a signed-permutation spectrum, so the
  fixed frame alone misses the control and `P^k β` catches it.

***

## Status of the r6 findings

| r6 finding | status in r7 | note |
| --- | --- | --- |
| B1 sham / disturbance | **applied, with new defects** | `K`, SH-0/SH-K, PL-CONFOUND and the confound finding are all present. New issues: R7-B1 (the rule is analytic) and R7-B4 (`K`'s definition) |
| B2 P text | fixed | two settings; non-attributive; classical models named, construction B included |
| B3 B scope | fixed in the scope sentence, B-REG and TOMO | remaining: R7-B3 (the LP's read set against `Acc`; construction A's paper claim) |
| B4 Level 2 setup | fixed | "in the interferometer" struck; PLAN and the preregistration agree |
| B5 eraser | fixed | required; computed on every arm and slot over both phases; CW-P's diagonal-analyser eraser; probe labels corrected (verified) |
| B6 W-CL frame | fixed | either-frame rule; C-R60-ODD verified to have teeth |
| B7 L-UPRIME | fixed | |
| B8 A/B | **applied, with defects** | R7-B2 |
| N1 | fixed, except one item | the validation point is now recorded, as c.6734561591 (07:22:01Z); fill it |
| N2–N18 | fixed | N2 quotes checked verbatim; N4 PL-SPI verified (SPI false); N5 `D_phase = 0` verified; N9 Lemma P sketch checked (below); N16 `bp_equals_qmp` is reported, not gating |
| R1, R2 | fixed | |

**Lemma P (N9), checked as a sketch.**
- Each step is sound: power-boundedness; semisimplicity; the peripheral projection as the limit of `Φ^{n_k}`; the
  restriction to `Ψ(O)` being a volume-preserving affine injection, hence onto; and the cases by rank.
- The unit-modulus spectrum of the linear part equals the spectrum of its restriction to the range of the limit
  projection, which the sketch uses implicitly. Say so in one line.
- The lemma remains unreviewed paper, correctly labelled.

**A record on #1169 to correct (not an r7 text issue).** c.6734561591's "Applied" note lists two exceptions: CPL and
SPI. The r6 audit's principal exception was COMP: the sham's comparability was asserted, not validated (r6 B1). r7 fixes
it through `K`. The record should say so, so that #1169 does not understate what the audit found.

***

## New blockers

### R7-B1. Step 5 is analytic under every D14 option; P must be restated (§A.31: NEW)

**The writer's claim is verified, and it is stronger than stated.**
- In construction B the screen port is `x + φ + kick`. So `V` is a function of the kick law `K`: over all nine single-cell
  supplies and the composites, `V = 1` iff `K` is a point mass (r6 probe).
- In QM, `V` is a function of the arm's reduced channel on the path qubit. The CNOT marker and the kick-matched
  classical-noise sham induce the same channel, and the same `V = 0` (probe). The classical wave is the same, with the
  field's reduced polarization-summed coherence.

The consequence holds in any theory where the screen statistics depend only on the system-level channel of the arm:
- **D14(a), and (c):** `COMP(SH-K)` forces `K(S*) = K(on)`, hence `V(S*) = V(on)`. Step 5 fires exactly when step 4
  passes, so P-TRANSITION is unreachable **by definition**, not by any property of QM, waves or OI.
- **D14(b):** SH-0 acts on the carrier as the identity (computed: the free tick), hence `V(S*) = V(off)`. Step 5 never
  fires.
- Either way, given steps 2–4, the token is fixed by the owner's D14 choice, not by any measurement. That is a variant
  that "can be adjusted to fit any outcome" (§A.29). The P-SUPPRESSION-UNATTRIBUTED and P-TRANSITION texts differ only by
  that choice.

**The interaction with *Levels* is unstated.** Under D14(a) with item L(i) ("Level 1 iff P-TRANSITION"), Level 1 is
unreachable. Then Levels 2 and 3 are unreachable whatever B and C show: a C-EXPOSURE could never lift any level. D14
must state this.

**The no-record arm is itself relative to access (§A.31: NEW).**
- In QM, the purified dephasing dilation (environment `|+⟩`, CZ) carries a path record in the environment's conjugate
  basis (`D = 1`). Only the mixed environment of classical noise has `D = 0` (probe).
- In construction B, `D(SH-K) = 0` likewise holds only because `w′` is unknown under N2. In the substratum, the
  bijection and RET-w keep everything.
- So "a path-correlated record or not" is not a property of the dynamics. It is relative to which variables are unknown
  or unread, a B-type (N2 and access) notion. This is the decoherence and dephasing equivalence at the level of
  dilations: equal system channels, and records that differ only in the environment's state and basis.

**What P can distinguish at all** through screen statistics plus validation:
1. fringes with the detector off;
2. that the on arm leaves a validated path record (`D`) and the system-level disturbance it induces (`K`);
3. **the class-level relation** over the admissible apparatus of a construction: whether every admissible arm that
   records the path also disturbs and suppresses. This is complementarity (`V + D ≤ 1`, and here `V² + D² ≤ 1`), which
   is r7's `ab-p` predicate;
4. that the record is erasable by conditioning on the held cells (the eraser).

It cannot attribute a *single* suppression to recording rather than dephasing, in any theory. Dephasing is an equally
valid explanation of each screen table.

**Two readings of A against B must both be reported.**
- *Existence* of the transition (there is an arm that records and suppresses): the same `(U, 0)` marker is admissible in
  both A and B, so **both succeed**. By the owner's case logic, observational incompleteness is then not necessary for
  existence.
- *Universality* (every recording arm suppresses, that is, complementarity): **A fails, B succeeds**, carried by SA-1(c).

r7 reports only the second, and calls it the transition. That re-narrates the comparison's valence (§A.22).

**Fix** (recommended statement of P, neither overclaiming nor vacuous):
- The P token reads steps 2–4 and the class-level predicate:
  - P-COMPLEMENTARITY: fringes off; the on arm records and suppresses; every admissible recording arm suppresses;
  - P-RECORD-WITHOUT-SUPPRESSION: some admissible arm records with `V = V(off)`, listed;
  - P-NO-RECORD, P-NO-FRINGES and P-VOID as now.
- Report both A/B readings.
- Report SH-0 and SH-K as a *decomposition*, never gating: the coupling alone does not suppress; the kick alone does.
  Report the dephasing look-alike, and add one sentence: "each suppression is equally explained by the accompanying
  disturbance; what the construction adds is that, in its admissible class, no record exists without that disturbance".
- Re-pose D14 with an option (d), "the sham arms are reported and gate nothing". State each option's consequence for
  *Levels*.
- Item L(ii), Level 1 as `V(off) > 0`, is known on paper. Under it, Levels 2–3 do not depend on P's attribution; say so.
- Keep the access-relative note on `D`: QM's purified dephasing has `D = 1`, and B's `D(SH-K) = 0` holds under N2.

### R7-B2. Construction A is mislabelled; P3 is mis-typed; `mech_change` is not a test; two ablations are under-specified

1. **Construction A is not "the substratum alone".**
   - `ab-p`'s A is the nine single-cell supplies with everything else of B kept: P3 arming and E-iso, N2 (probabilities
     at all), H-PREP (`X−`, `φ = 1`), the terminal screen registration, L-PATH and L-PORT. It is "B minus SA-1(c)".
   - DESIGN-DS §3 and §8 say A has "no terminality; full observer access", but `ab-p` does not compute either.
   - Without N2 there are no probabilities. Without P3 there is no detector switch: under FIX the coupling is fixed and
     translation-invariant, so the "off" arm does not exist.
   - Fix: name A honestly, for example "A_P = shared scaffolding (P3, E-iso, N2, H-PREP, the screen's terminality,
     L-PATH, L-PORT) without SA-1(c), SA-1(b) or L-ACC". List the scaffolding as untested in this round, and say that a
     substratum-only baseline cannot pose P (NR-16 names P under FIX).
2. **P3's kind is wrong.**
   - The preregistration's typing has "P3 arming and E-iso | control", and the ablation rule gives "control → no new
     dynamics".
   - P3 changes which step is applied per tick: armed against unarmed edges. The detector-on/off transition *is* a P3
     switch. That is why it is "in tension with FIX".
   - Crediting it with no dynamics is the converse error of the one c.6734374076 forbids. Type it "dynamics (control of
     couplings)", with `mech_change` "a different mechanism".
3. **`mech_change` is frozen from the row's kind, so it is a label, not a test.**
   - c.6734374076: "the ablation should therefore test both whether the principle changes the reachable observable
     predictions and whether it changes which mechanisms can be justified".
   - Make it computed: for each ablation, the set of admissible mechanisms (supply × coupling type) that realize each
     observed `(V, D, K)` cell, and whether that set changes.
     - Dropping SA-1(c) adds the sharp mechanisms to the cell `(1, 1, δ)`.
     - Dropping reciprocity adds the copy-only mechanism.
   - Keep the frozen kind label as a separate `dynamics_credit` field. A state or access restriction is never credited
     with new dynamics.
4. **The ablations are under-specified and cannot be decided mechanically.**
   - "The environment cell with a known slot" does not say which slot. A known `u` gives SH-0 (`V = 1`); a known `v`
     gives the marker (`V = 0`, `D = 1`). DESIGN-DS §8's expectation holds for the first only.
   - "Drop SA-1(b) (the held cell re-coupled at `t = 3` and registered)": at `t = 3` the carrier is coupled to the
     screen. Re-coupling the held cell is either a three-cell armed star or another tick, and the observable read is not
     stated.
   - "Drop L-ACC (observer reads held cells)" duplicates the required eraser and B-P's M2/M3.
   - Freeze each ablation's supplies, schedule and read set exactly, as a fixture.

### R7-B3. B-P's LP read set is not its `Acc`; construction A's imitability is not a Lemma NC-F consequence (§A.31: NEW)

1. **The fragment's reads do not match `Acc`.**
   - B-P's drafted `Acc` is "the screen port and each slot of each held cell (arm **and phase** cells)".
   - The fragment's measurements are M1–M3: the screen, and screen × one arm-cell slot. No phase-cell read, and no
     screen × arm-slot × phase-slot joint read.
   - Under SA-1(b), one functional per cell per run, so joint reads across cells are part of a native meter class.
   - If the LP runs on a strict subset of `Acc`, a B-CONTEXTUAL can be the B-REG artefact *inside* `Acc`: the
     contextuality is removed by `Acc`'s own effects. The owner's typing of `Acc` then does not protect Level 2.
   - Fix: either the LP's measurement set equals the full owner-typed `Acc` (all joint registrations it permits), or
     Level 2 additionally requires that the first completion, "add `Acc`'s remaining effects", does not restore a model.
     Freeze `Acc` as an explicit effect list per fragment.
2. **TOMO's configuration space must be frozen.** "the configurations of the cells `Acc` reads" includes unread slots
   (for example the screen's `v`), unless it means the read slots only. The two give different `r_E`. State which, and
   whether "charged" (QC22's `Ω_c`) applies.
3. **Construction A's imitability.**
   - r7 states A (complete access) is imitable "by Lemma NC-F". NC-F's fast path needs `d = r_S = r_E` on the charged
     configurations.
   - With 32 preparations on the configurations of screen, arm and phase cells, `r_S` can be less than `r_E` even with
     complete reads. Spanning reads make the preparation equivalences genuine. They do not make the measurement-side
     equivalences genuine.
   - Report A's B result as measured. Do not freeze it as a paper expectation unless TOMO is shown green on both sides.

### R7-B4. `K` is not a disturbance measure for non-additive arms

- `K(arm)` is "the law of `Δx` … under `X+`", with no phase stated. The writer's probe computes it at `φ = 0`.
- For PL-SPI (exchange of `x` with a known slot) it reports `K = {0: 1}`, the same as off and SH-0, while `V = 0`. The
  arm erases `x` but registers as "no kick".
- `K` coincides with disturbance only for arms that act additively on `x`.
- **Fix:** define `K(arm)` as the transition kernel of the encoded `x` across `t = 2`: the law of `x_after` given
  `x_before`, from `X+` and `X−` at both phases. A reset then differs from both the identity and the uniform kick. Use
  that kernel in COMP. The frozen arms are unaffected: the marker's and SH-K's kernels are both the uniformizing kernel.

### R7-B5. D16(b) contradicts recorded owner directions and D8(a)

- D16(b) "only interference statistics after recombination" would exclude "the marker reads in B and the eraser".
- The owner has already accepted marker-detector records as indirect access:
  - c.6733711272 item 3: "An observer can avoid directly reading hidden paths while still recording detector outcomes and
    correlations";
  - c.6733796760 element 3: "correlations between screen detections and an accessible marker detector".
- D8(a), the drafted eraser, requires them.
- Fix: restrict D16 to meters that copy a *carrier* functional without recombination (C's `S_Z`, and `S_X` and `S_Y` as
  applicable). Note that the screen is itself such a meter after recombination. Then state what each option leaves of C.

***

## Answers to the six focus points

1. **The sham.** Verified, and it generalizes:
   - Under any D14 option, step 5 is analytic. This holds wherever screen statistics depend only on the system-level
     channel: in QM, in classical waves and in construction B.
   - P is meaningful only when restated around class-level complementarity (record ⇒ disturbance ⇒ suppression over the
     admissible class), with the existence and universality readings of A/B both reported. Dephasing is an equally valid
     explanation of each single suppression (R7-B1).
2. **A/B and the ablations.**
   - `ab-p` is mechanical and correct for what it computes (verified). But A is mislabelled, and P3 is mis-typed.
   - `mech_change` is a frozen label, not the test that c.6734374076 requires.
   - Two ablations are ambiguous.
   - The rule that restrictions are never credited with dynamics holds as written. Its converse error, crediting P3 with
     no dynamics, is present (R7-B2).
   - SA-1(c), the carrying principle, is a state restriction, the knowledge-balance condition. A noncontextual model of
     P's table is therefore expected, consistent with OICORE-1 §5(b).
3. **`Acc`, TOMO, B-REG and Level 2.**
   - The scope sentence and B-REG are right. The "TOMO green ⇒ feasible" assertion is right (Lemma NC-F).
   - Gaps: the LP's read set against `Acc`, TOMO's configuration space, and A's claimed imitability (R7-B3).
4. **The eraser.**
   - Required; every arm and slot; both phases; CW-P's diagonal analyser; QM and wave references. The probe is fixed and
     verified.
   - Nit: freeze how `n/a` cells, conditioning on a slot value of probability zero, are recorded.
5. **W-CL.**
   - The either-frame rule is sound, because `P ∈ O_h` maps O-self-maps to O-self-maps.
   - C-R60-ODD has teeth: the fixed-frame spectrum `{−1, 1, 1}` is a signed-permutation spectrum, so only `P^k β` fires.
6. **D14–D18.**
   - D14 needs option (d) and its Level consequences (R7-B1).
   - D15 needs "the LP reads the whole `Acc`" (R7-B3).
   - D16(b) conflicts with D8(a) and the owner's element 3 (R7-B5).
   - D17 is neutral. Note that under D17(a), Level 3 joins B-P (P's apparatus) with C-EXPOSURE (the U′ gadget), two
     unrelated instances. Print that qualifier with Level 3.
   - D18(c) does not state its consequence: every P and C token becomes a benchmark result, so no Level is awardable.
   - D4(b) adds NNB, a dynamics-kind coupling, to P. Then `ab-p` and the ablation table need a dynamics row.
   - D1–D13 are otherwise consistent.

## Nits

- **r7-N1.** Fill the validation-point record: c.6734561591, 2026-11-09T07:22:01Z. Quote the owner's sentence from it.
- **r7-N2.** Eraser fields: freeze the representation of a conditional `V` on a zero-probability slot value (the writer's
  probe prints `n/a`).
- **r7-N3.** DESIGN-DS §1. Add the access-relativity of `D`: QM's purified dephasing has `D = 1`, and B's `D(SH-K) = 0`
  holds under N2 (R7-B1).
- **r7-N4.** PL-SPI uses a sharp `(0, 0)` cell (a P2 departure). Say so in its fixture cell.
- **r7-N5.** Lemma P sketch: add the one line on the peripheral spectral subspace (above).
- **r7-N6.** `ab-p` covers single-cell supplies only. The general B statement (`D = 1 ⇒ V = 0` for every SA-1 protocol)
  is AP1 Lemma 3 [W]. Cite it as the paper extension, labelled.

## Fixed point (§A.31)

| pass | findings | classification |
| --- | --- | --- |
| r7-1 | R7-B1 (analytic step 5; `D` relative to access) | NEW |
| r7-2 | R7-B3 (`Acc` against the read set; A's NC-F claim) and R7-B4 (`K` for non-additive arms) | NEW |
| r7-3 | R7-B2 (A mislabelled; P3 typing; `mech_change`) | NEW / ELABORATING |
| r7-4 | R7-B5; the nits | ELABORATING / CONFIRMING |

The fixed point is not reached. The r8 re-review should continue it on P's restated token, on `Acc` once D15 is
decided, and on the computed `mech_change`.
