# Independent pre-freeze review: Q-C2-1 r6 (ARP-2-QC21)

**Reviewer.** Independent model reviewer, 2026-11-09. Read-only. No repository write, GitHub write or dispatch. Two cheap
exact probes, written for this review, are in `review/probes-r6/`. Neither evaluates C's non-affine gadget, a test rule's
orbit or a B fragment built from OI data. The P-model probe re-derives the affine instance that is already evaluated on
paper (AP1 §4.5) and by the writer's `p_native.py`, and adds fixture variants only.

## Verdict: **REVISE**

r6 is a substantial and mostly honest redesign. The two-layer split, the Level cap on P, the disclosure that P is not
blind, the stated limits of the anticorrelation test, Lemma CL and the M-ARC relation are all sound. Eight blockers
remain, three of them structural:

- **The sham does not test disturbance.** The sham's coupling acts on the carrier exactly as a free tick. The only
  native arm whose disturbance matches the marker's is the dephasing cell, and COMP's one-unknown clause excludes it. The
  P-TRANSITION attribution therefore has no support from the validation layer (B1, B2).
- **B's contextuality is relative to the fragment.** A classical two-bit register fires it, so Level 2 could be awarded
  on an artefact of tomographic incompleteness (B3).
- **The owner's A/B construction is missing** (c.6734304025; B8).

## Inputs verified

| file | sha256 | status |
| --- | --- | --- |
| `preregistration.draft.md` r6 | `0120357a8b7d88ac7deed247656b3e1fde0255e3e11f175138df117df4efdb44` | matches |
| `PLAN.md` r6 | `c0c6667511f1884d27a0ffd7c80900d56433b479c77fba53ea0319ea362335fb` | matches |
| `DESIGN-DS.md` | `a233e762521106b9aad920325307be31e162b83b45ee65e5637e894642ef40cd` | matches |
| `probes-r6/p_native.py` | `092db1d65bde28e6cff62f80b10eccd6f1c987f8d1f08790a054b44a50e3b955` | matches DESIGN-DS §9 |
| `probes-r6/tri_affine.py` | `d6c3b1fb9481056e5e9960b27c84e92cefdca415c4d30932078664e484284271` | matches |
| `probes-r6/pusey_probe.py` | `b7526d68b8000282e65f65ab0f1a1122bdcf2b23fb053e0aeef4baf698dfad78` | matches |

**Other sources read:**
- The owner comments c.6733621500, c.6733711272, c.6733796760, c.6733825267, c.6733855134, c.6733935953 and
  c.6734304025, through `gh api`.
- AP1 (`R/apparatus-1-20261107/DESIGN.md`, blob `51c24aeb…` at `2cd49dc0`), §§3–4.7.
- Main:684, Main:688-691.
- QC22 r13 (*The exact method*, Lemma NC-F, the licensing text at :655-668 and :719-722).
- MR★ :1150 (tomographic completeness relative to `Acc`).
- M-ARC on `main` at `fd539e15`, and `REVIEW-MARC-S1-RESULTS.md`.
- OICORE-1 r6, §§2, 3.2, 5 and 8.

## Reviewer probes (exact; controls, not evidence)

| file | sha256 | what it shows |
| --- | --- | --- |
| `review/probes-r6/p_arms_indep.py` | `1e351a74884447ca6fa98530e2706009d7e37e61f985c3f6c919ad9f78c1e9a6` | It re-implements P's model independently, sharing no code with `p_native.py`, and reproduces the four arms. It also reports: every single-cell arm supply with its V, D and kick law; eraser sorting on the marker **and** on the dephasing arm; and r6's `decide-p` on a composite fixture |
| `review/probes-r6/b_incomplete.py` | `f02aeaebb65ff2112f0be99293b470b9d2a3baed87851272d0abbf657903a3a1` | A classical two-bit register with point preparations, read one bit at a time. It has no preparation-noncontextual model over the fragment's own equivalence (POM success 1 > 3/4). Adding the parity read removes the equivalence, and a model then exists |

**Key output of `p_arms_indep.py`.** All exact. "Kick" is the law of `Δx` on the carrier's encoded `x` across `t = 2`.

| arm cell at `t = 2` | V | D | kick law | note |
| --- | --- | --- | --- | --- |
| off (unarmed) | 1 | 0 | δ0 | |
| marker `(U, 0)` | 0 | 1 | uniform | |
| sham `(0, U)` | 1 | 0 | δ0 | **identical to the off arm on the carrier**: the coupled tick with `u_a = 0` is the free tick |
| `(1, U)` | 1 | 0 | δ1 | ports swapped: this is the phase cell with `φ = 1` |
| dephasing `(U, U)` | 0 | 0 | uniform | **same kick law as the marker** |
| sharp `(0, 0)` (P2 departure) | 1 | 1 | δ0 | |
| sharp + dephasing cell, both armed | 0 | 1 | uniform | `decide-p` returns **P-TRANSITION** |

Over all nine single-cell supplies, `V` is fixed by whether the `u` slot is known, that is, by the kick law. `D` is fixed by
whether the `v` slot is known, that is, by whether the record is masked. Under SA-1(c), exactly one slot is unknown, so
a path record (`D = 1`) comes with a uniform kick (`V = 0`), and a masked record comes with a deterministic kick.

**Eraser sorting** (`X+`; held slots labelled after the final free tick). The marker and the dephasing arm give
identical tables: sorting on the kick slot gives conditional `V = 1, 1`; sorting on the other slot gives `0, 0`; unsorted,
`V = 0`.

***

## Blockers

### B1. The sham does not produce comparable disturbance, and the validation layer never measures disturbance (§A.31: NEW)

**What the owner asked for** (c.6733855134):
- "an interaction that produces comparable disturbance but does not encode the path";
- "Unchanged single-path screen patterns are a good control, but not sufficient";
- "the sham interaction must be designed and validated accordingly".

The coordinator recorded the application as "a sham-detector arm whose comparable disturbance is defined natively and
frozen".

**What r6 freezes.** `COMP(sham)` is "same edge, tick and coefficient; `a` has exactly one unknown slot; `SPI(sham)`". This
is comparability of the *apparatus form*. No disturbance is measured.

**Evidence.**
- With `u_a = 0` known, the sham's coupled tick on the carrier is `u_c' = 0 + v_c`, `v_c' = u_c`. That is exactly the free
  tick (probe: kick law δ0, as in the off arm).
- So `V(sham) = V(off)` holds by construction. Rule step 5, P-SUPPRESSION-UNATTRIBUTED, cannot fire on the native instance.
- The sham is also the phase cell with `φ = 0`: the supply `(1, U)` at `t = 2` reproduces the `φ = π` setting.
- The one native arm whose disturbance law equals the marker's, a uniform kick, while recording no path is the dephasing
  cell `(U, U)`. It suppresses identically. COMP's one-unknown clause excludes exactly this cell. PL-SHAMBAD has to waive
  that clause in order to plant it.
- Under SA-1(c), with fresh single cells (all nine supplies enumerated), a uniform kick implies `D = 1`. In general, AP1
  Lemma 3 (isotropy) gives `D = 1 ⇒ V = 0`.
- The record and the kick are therefore perfectly confounded in the native class. The validation layer separates the marker
  from the dephasing arm by `D`. It cannot separate "suppression caused by recording" from "suppression caused by the
  unknown kick that SA-1(c) forces on every recording".
- The composite fixture shows the rule's blind spot directly. A record from a kick-free (P2-departure) cell, together with
  an unrecorded uniform kick, is labelled P-TRANSITION.

**Bearing on the owner's new point** ("the apparatus checks must validate properties of a mechanism generated by OI").
COMP is not a validated property of the mechanism. It is a property of the supply, chosen at design time. Because P's
outcome is already known, choosing a sham definition amounts to choosing P's outcome (§A.29; see item 6 below).

**Fix.**
- Add a validation-layer quantity `K(arm)`: the exact law of the kick `Δx` on the carrier's encoded `x` across the arm
  tick, computed from the native construction.
- Freeze COMP as `K(sham) = K(on)` and `D(sham) = 0`, plus the edge/tick/coefficient equalities. Drop the one-unknown
  clause, or keep it only as a stated option.
- Present to the owner neutrally (**new D14**):
  - **(a) Disturbance-matched sham.** The only native candidate is the dephasing cell. The paper expectation is then
    P-SUPPRESSION-UNATTRIBUTED, and it must be disclosed as known.
  - **(b) Keep the drafted arm.** Rename it a "coupling-matched null sham (no disturbance)". State in the token text that
    it disturbs nothing, and remove the causal attribution (B2).
  - **(c) Both arms,** with the rule reading (a) for attribution.
- Freeze the composite fixture as a planted control (PL-CONFOUND). Its expected token follows from D14's choice.
- Add the invariant "comparable disturbance is measured" with checkpoint `K` (§A.41).

### B2. The frozen P-TRANSITION text overstates what P establishes

1. **"The suppression is attributed to path recording by the validated apparatus checks."**
   - The checks show co-occurrence of `D = 1` with suppression. They also show identical suppression from the same kick
     law with `D = 0` (B1).
   - Supported wording: "suppression occurs with a validated path-correlated record (`D = {D_on}`). In this model every
     path-recording marker under SA-1(c) applies a uniformly unknown kick, and the same kick law without a path record (the
     dephasing arm) gives the same suppression. The screen suppression is a function of the kick law; its association
     with recording rests on SA-1(c)."
2. **"phase-dependent interference" needs its scope.**
   - Natively the phase takes the two settings `φ ∈ {0, π}`. The phase cell adds a known bit to the read functional `x`.
     This is a deterministic flip, the toy analogue of `Z^φ`. The "fringe" is two points.
   - Calling it interference is honest only with that qualifier: "two-setting phase dependence: with the coherent source the
     port equals `x + φ`; with single-path sources it is uniform."
   - Owner element 2 ("generate the phase-dependent statistics, not simply reproduce a preselected picture of fringes") is
     met minimally. This should be said in the scope, not left to D4.
3. **Classical look-alikes.** Hazard 2 and the text name only "a classical wave with a polarization-type marker".
   - The native affine class is itself an epistemically restricted classical model of the whole four-arm table.
   - OICORE-1 §5(b) already records that the Z/X Lüders law with backaction and eraser behaviour "at stabilizer scope" have a
     noncontextual model (AP1 §0; M1D Prop. C(d)). The same point is made by Catani–Leifer–Schmid–Spekkens 2023, cited in
     r6's ADA.
   - The text should say that P's table has a noncontextual classical model, the native class among them. "Excludes
     nothing" is the honest statement for P.

**Fix.** Rewrite the P-TRANSITION text and hazard 2 as above, and mirror them in DESIGN-DS §1 and §4. Replace "native
affine apparatus" by the owner's phrase (B8).

### B3. B's contextuality is relative to the fragment. Classical models fire it, and Level 2 can be awarded on an artefact (§A.31: NEW for r6; corpus precedent exists)

**Evidence.**
- `b_incomplete.py` is exact. A classical register `F_2²`, with point preparations and reads "bit 1" and "bit 2" only,
  makes `½P₀₀ + ½P₁₁ ≡ ½P₀₁ + ½P₁₀` an operational equivalence of the fragment. Any model needs disjoint supports for the
  two sides, so none is preparation-noncontextual.
- This is parity-oblivious multiplexing relative to an incomplete read set: success 1 against the bound 3/4. It is also
  the writer's own `pusey_probe` fragment at `(a, b) = (1, 1)`, the cube vertices. Adding the parity read removes the
  equivalence.
- QC22 r13, whose method r6 imports, states the consequence for native data (QC22:661-666). "LP infeasibility licenses
  only the statement 'no preparation- and measurement-noncontextual model over F1's own equivalences'. By Lemma NC-F it
  implies a degenerate pairing … CONTEXTUAL is the generic outcome … No text reads it as non-imitability beyond F1, or as a
  nonclassicality witness."
- The corpus already requires tomographic completeness relative to a declared `Acc` before labelling a violation (MR★ :1150,
  LIT-2-C1). AP1 Lemma 4′ makes the same point ("What excludes it as a witness is MR-1's tomographic-completeness caveat").
- Because every native table is generated by a configuration model, Lemma NC-F gives a stronger statement: **every native
  B-CONTEXTUAL is a degenerate pairing on the configurations**. Contextuality in OI data is always relative to reads that
  do not span the hidden configurations.

**What r6 gets wrong.**
- "Infeasibility excludes every generalized-noncontextual ontological model of that table (… epistemically restricted toy
  theories, including the native affine class)."
  - The native affine class is a configuration model.
  - If it produces a B-CONTEXTUAL table, it is a classical model of that table that the statement claims to exclude.
  - The parenthesis is false, and the claim needs "over the fragment's own equivalences".
- B-CLASS is drawn "with a spanning read set", which is exactly the case where the artefact cannot appear. No control
  exercises the incomplete-read route.
- **Level 2's significance.** The owner's Level 2 is "Excludes a defined class of classical explanations". Under r6,
  B-CONTEXTUAL excludes only models that respect equivalences the world itself does not respect.
  - It does not exclude classical stochastic registers with unread parities (`b_incomplete.py`).
  - It does not exclude classical fields with intensity-normalized detection (B-WAVE).
  - It does not exclude OI's own model.
  - The coordinator's recorded application of c.6733711272 also states that the criterion must be one "classical-wave and
    classical-stochastic models cannot meet from detector records alone". r6's B does not meet it.
- **Reachability.**
  - B-P: if its native table equals QM-P's (DESIGN-DS §4 asserts this for the screen columns; the joint M2/M3 tables are
    not stated), its token is fixed by the QM-P control. It is either feasible, or QM-P turns red and B is void.
  - B-C: with the three detectors on a four-bit carrier, B-CONTEXTUAL is close to W-OCT restated (the writer's finding 6:
    contextuality coincides with leaving the diamond). The reason is a chosen read set, not a native restriction.
  - So Level 2 is reachable mainly through a chosen restriction of access.

**Fix.**
1. State B's scope as QC22 does: "no noncontextual model over the fragment's own equivalences". Delete "including the
   native affine class".
2. Freeze an observer effect class `Acc` for each fragment, as an ADA row typed by the owner (new **D15**):
   - (a) every native meter effect on the cells the observer holds;
   - (b) a restricted set, with the restriction typed as a principle, for example ACC-R2, a traced-out sector, or the U′
     identification (B7).
3. Add a validation-layer check TOMO (`d = r_S = r_E` relative to `Acc` and the preparation class, QC22's Lemma NC-F
   pairing). Under (a), Lemma NC-F makes native tables imitable whenever both sides span. That is an informative paper
   expectation and should be stated.
4. Award Level 2 only from a B-CONTEXTUAL whose `Acc` is owner-typed. Report the TOMO status and the completion that
   restores a model, as QC22 reports `{S}`.
5. Add a planted control **B-REG**, the classical register of `b_incomplete.py`. Expected: infeasible, with TOMO red.
   Route to failure: "a Level 2 award from tomographic incompleteness".

### B4. Level 2 crosses setups, PLAN and the preregistration disagree, and "in the interferometer" is unsupported

- PLAN §1 gives "2 = also B-CONTEXTUAL on the same setup". The preregistration's *Levels* admits "B-P **or** the B-C
  fragment of a test-rule instance".
- B-C is on the triangle. DESIGN-DS §5.7 shows the triangle cannot host P. So Level 2 can combine P's transition on one
  apparatus with contextuality on another.
- The owner asked for "two separate acceptance tests: interference generation and quantum-specific discrimination" on the
  double-slit setup (c.6733796760).
- Question C and DESIGN-DS §6 say "in the interferometer". C has no screen, phase cell or marker. The source labels are
  relabelled toy states.

**Fix.**
- Make PLAN and the preregistration agree.
- Put the cross-setup question to the owner as **D17**: does B-C count toward Level 2?
- Strike "in the interferometer", or define it.

### B5. The eraser is optional, its classical-wave control is missing, and it does not separate recording from dephasing

- Owner element 3 is "Show what happens when a path record is created, kept, **or erased**". D8 offers "(b) omit it".
  The coordinator's recorded application of c.6733711272 lists "a classical-wave which-path/eraser model" among the
  controls. CW-P has no eraser part.
- Probe: sorting on the held noise slot recovers fringes in the dephasing arm exactly as sorting on the kick slot does in
  the marker arm. The observer-level eraser tables of the two arms are identical, so the eraser is not a discriminator here.
- The writer's `p_native.py` labels the held slots before the final free tick, so its printed labels are swapped:
  - "u (path)" gives the deterministic port;
  - it evaluates only `φ = 0`, so it computes no conditional `V`.

  DESIGN-DS §4's sentence is physically right, but the cited probe output, read by its labels, says the opposite.

**Fix.**
- Make the eraser a required part of P's report: frozen fields, run on all four arms, with frozen QM and classical-wave
  reference values. Remove D8(b), or record an owner waiver.
- Add the eraser to CW-P.
- Report that the marker and dephasing eraser tables are equal.
- Correct the probe's labels and compute `V` from both phases.

### B6. W-CL's frame is undefined for rounds with an odd tick count, and "frame-free" is overstated

`W-CL` takes the spectrum of `β` in `R_op` coordinates, read in fixed slots. For a round with `k` ticks, the encoded
action is `P^k β`, with `P` the transposition `x ↔ z` (r5's frame convention, Appendix A). This is a multiplication by
`P`, not a conjugation, so for odd `k` the spectra of `β` and `P β` differ.

**Effect.**
- Positives are sound in either frame: `P ∈ O_h`, so `β` is compatible with O_h iff `P β` is.
- Negatives are not. An encoded R60 in a round with odd `k` has an improper fixed-slot `β` whose spectrum can lie in the
  list. C-SURVIVAL's "exhaustive within its scope" then has an avoidable blind spot.
- No control exercises odd `k`. C-R60 is supplied without ticks.

**Fix.**
- Compute W-CL on both `β` and `P^k β`, and fire if either fires. This is sound by the argument above.
- Report both spectra.
- Add C-R60-ODD: the supplied encoded R60 composed with one free tick, which must fire.
- Say "invariant under linear recalibration" rather than "frame-free".

### B7. L-UPRIME is not removed from C's or B-C's tokens

- PLAN §3 and ADA Part 1 state "L-UPRIME … removed from every token".
- The detector set `S_Z`, `S_X`, `S_Y` reads exactly `f_z = u_0`, `f_x = v_0` and `f_y = u_0 + v_0 + u_1 + v_1`. That is
  the U′ identification in detector form.
- B-C's whole effect set is those three functionals. Meters on cell 1 exist natively, and C-DET's sixteen point laws show
  such detectors can be built.
- So the choice of `Acc` re-imports L-UPRIME, and it is the restriction that makes B-C's fragment incomplete (B3).

**Fix.**
- Retype L-UPRIME for C and B-C as "used: the detector set is U′'s functionals".
- Add it to the renaming check, Part 3.
- Tie it to D15.

### B8. The owner's A/B construction is absent (c.6734304025)

There is no construction A (the substratum alone) and no construction B (named OI principles over the same dynamics). The
principles are not typed under the owner's three-way classification, and there are no per-principle ablations for P, B or
C. r6 also uses "native" throughout, including in frozen texts ("In the native affine apparatus …"). The owner directs
that it be replaced by "OI substratum plus independently justified observational-incompleteness principles, with every
additional assumption identified and tested separately". Details are in the dedicated section below.

***

## Validation-layer audit (the owner's added point: the checks validate an OI-generated mechanism and import no quantum structure)

| quantity | how r6 computes it | native? | supplies anything to the dynamics or the screen? | quantum structure? | finding |
| --- | --- | --- | --- | --- | --- |
| `D(arm)` | total-variation distance between the configuration-count laws of the held cell's two slots, given `Z+` and given `Z−` | yes: classical TV on laws from the bijection under N2 counting | no: computed after the run | none: no density matrix, no trace distance, no overlap | sound. Nit N5: it is defined on one cell only |
| `NONABS(arm)` | carrier `z` across `t = 2` equal in every positive-weight configuration; no run discarded | yes (encoded frame, AP1 §4.2, C8) | no | none | sound. PL-ABSORB gives it teeth |
| `SPI(arm)` | `s(arm, Z±, φ) = s(off, Z±, φ)` | yes | no | none | **vacuous in the affine class**: under `Z±`, `x` is uniform and independent of every arm, so `s = ½` always (N4) |
| `COMP(sham)` | equal edge, tick and coefficient; exactly one unknown slot; SPI | **not a measured property**: a design property of the supply, and the one-unknown clause is the P2 posit | no | none | **fails the owner's point**: disturbance is asserted, not validated (B1) |
| `D(sham) = 0` | as `D` | yes | no | none | sound, but it validates only "no record", not comparable disturbance |
| `D(dephasing) = 0` | as `D`; the arm is a hidden-sector cell, both slots unknown | the step is native; the cell is an N2 environment supply | no | none | sound. "Dephasing is native" (finding 8) should read "native step with a supplied N2 environment cell" (N12) |
| `CPL = V(on)² + D(on)²` | arithmetic on `V` and `D` | the inputs are native; the **bound ≤ 1 is Englert's quantum relation** (trace distance), compared with a classical TV | no | the comparator is imported (E-COMPL); nothing quantum enters the computation | acceptable only as a labelled comparator. Under SA-1(c) it cannot exceed 1 natively (`V + D ≤ 1` from Lemma 3), so rule step 6 is unreachable except through P2 departures, which step 4 catches first (N6) |
| QM-P reference and control | exact rational density matrices | — | no: a control fixture only | yes, by design | permitted as a benchmark control. State that it enters only the controls and the note |

**Conclusion.** No validation-layer check imports quantum machinery into its computation. There is no trace distance on
density matrices and no Hilbert-space overlap. One check, COMP, does not validate a property of the mechanism at all, and
that is B1. CPL uses an imported quantum bound as a comparator and must be labelled as such.

***

## A/B construction (c.6734304025): what r6 contains, what is missing, and the candidate principles

### 1. What r6 contains, typed under the owner's three-way classification

"A" marks the substratum: a bijection on a finite state space under one fixed rule.

| ingredient (r6 id) | role in r6 | A or B-type | three-way type (reviewer's proposal; the owner decides) | basis |
| --- | --- | --- | --- | --- |
| bijective second-order step, class-N symmetric coupling, free tick (L-BIJ, L-SYM, L-SYMP, A4) | P, C | **A** | established native | Main:44-46, 62; AP1 §4.1 (symplectic, bijective) |
| `q = 2`, affine update (L-Q2, L-AFF) | P; C's ablations | A (rule choice) | established native for the reference branch; L-AFF is "uncertain (partly derived)" in r5 | r5 ADA |
| uniform law on unknown slots and hidden cells (L-N2) | every probability in P, B and C | B-type | candidate strengthened: "native measure, applied through H-PREP" (QA:777); Main's `T` counts uniformly over `H` (Main:688-691), so this is close to native for the hidden sector, but it is supplied for apparatus cells | — |
| half-known ready cells, SA-1(c) (L-P2; AP1:297-300, "Clause (c) is not derived", AP1:347) | **produces complementarity, which is the whole P result (B1)** | B-type | candidate strengthened: "new physical posit" (AP1 §3.1); justification status: posited; it is the knowledge-balance condition | AP1:292-299, C4 |
| known value 1, QA family as preparations (L-HPREP) | `X−`, `φ = π`, C's sources | B-type | candidate strengthened: an open hypothesis | r5 ADA |
| terminal registration, SA-1(b) (L-REG, L-P1) | screen, detectors, heralds | B-type | candidate strengthened: OICORE-1's RET-s (N; imported idealization below recurrence) | OICORE-1 §2 |
| per-tick, per-edge arming P3, and E-iso (L-ARM) | switches the detector on and off; selects phase and screen | B-type (observer interaction or control) | candidate strengthened, and in tension with FIX: "the native rule has a fixed, translation-invariant coefficient, so per-tick, per-edge arming is not native" (AP1:288-296); E-iso "is not derived" (AP1:305-309) | AP1 §3.1 |
| record retained in the held marker (L-HOLD) | the unread record | retention is A (RET-w, automatic under bijectivity); holding it decoupled and unread is B-type (E-iso, access) | retention: established native. Unread and isolated: candidate strengthened (access restriction) | OICORE-1 §2 RET-w |
| hidden-sector dephasing cell | the dephasing arm | B-type | candidate strengthened: an N2 environment supply; its link to Main's hidden sector `H` is plausible but not stated | — |
| observer interface restriction (the two layers; no carrier slot registered) | indirect access | B-type | candidate strengthened: an ACC-R2-type access principle; OICORE-1 gives ACC_op as CX†, with consistency with the core open | OICORE-1 §2, §3.2 |
| forward conditioning; refilled mediators (L-FWD, L-REFILL) | C | B-type | candidate strengthened (an access convention and a supply) | r5 ADA |
| NNB coupling for `Λ_{y,b}` (L-NNB) | C's sources; D4(b) | B-type | supplied (a conditional premise). It is not quantum structure, but it is the only route to a quarter phase (AP1 Lemma 5) | QA node 8 |
| path = encoded `z`, ports = values of one bit, frame calibration, U′ functionals (L-PATH, L-PORT, L-CAL, L-UPRIME) | they define what is called "path", "port" and "Bloch" | neither: identifications | **imported representation**. These are not coherent mixing, Hilbert space or instruments, so they are not the owner's third category, but they are not OI principles either. The owner should type them (D18) | — |
| Englert bound; Clifford-class definition; QM-P, C-STAB, C-R60, C-35, C-S3 | comparators and controls | — | imported quantum structure. Correctly confined to controls and benchmarks; none enters the primary derivation | — |
| non-affine rule `g` in C's gadget | C's test | **a change of dynamics**, not a principle | not an OI principle. The owner's scheme compares principles "using the same underlying dynamics wherever possible". C's affine/non-affine ablation is a dynamics ablation and must be labelled so | — |

### 2. Can r6 answer A against B? No, as written

r6 holds fragments of ablations: PL-SHARP drops SA-1(c); r5's direct-access diagnostics (D1) drop the access restriction;
the affine ablations change the rule in C. But it has no construction A run beside construction B, and no per-principle
ablation with its own reported readout. Precisely, these are missing:

- **P.**
  - An **A arm** on the same step and schedule with no B-type principles: arbitrary supplies, including sharp cells; no
    terminality; full observer access.
  - A **B arm** with SA-1(b), SA-1(c), N2, H-PREP, L-HOLD and the access restriction.
  - **Per-principle ablations** of the B arm, each reporting P's quantities (V, D, K, the eraser):
    - drop SA-1(c), which is PL-SHARP promoted to an ablation;
    - drop SA-1(b), as AP1 C9: the observer sharpens;
    - drop reciprocity, the copy-only meter of AP1 C3;
    - give the environment cell a known slot (N2);
    - drop the access restriction.
  - On paper the expected pattern is A fails (a record without suppression is possible) and B succeeds, with the effect
    carried by SA-1(c) (B1; AP1 C3, C4). That is the owner's case "A fails and B succeeds", which "would still need to
    determine whether the relevant conditions are genuinely implied by OI". It should be stated with SA-1(c)'s status.
- **B.**
  - An A arm with complete access (`Acc` = every native meter effect). By QC22's Lemma NC-F, native tables are imitable
    whenever both sides span.
  - A B arm with the owner-typed restriction (D15).
  - This is exactly the place where an access principle could matter (B3).
- **C.**
  - The principle arms are A = rounds without record-dependent access (`reg = none`) and B = with forward conditioning,
    terminal heralds and refilled mediators. These are the record-dependent-access route.
  - Currently ABL ablates only the rule and the idle gadget. The `reg = none` ablation is missing (N10), and CC-DYAD
    covers it only on `L_scope(g)`, not on orbits under W-CL.
  - The affine/non-affine comparison must be labelled as a change of dynamics, not a principle ablation.
- **All tests.**
  - A level-3 benchmark arm, labelled, for any imported structure. r6 has QM-P and the supplied gates as controls; if the
    owner wants a benchmark arm, it needs to be separate from the controls.
  - Reported outcome logic in the owner's three cases: both succeed; A fails and B succeeds; B fails.

This is a **blocker for r7** (B8).

### 3. Candidate principles for construction B (OICORE-1 §§2, 3.2, 8)

OICORE-1's governing finding applies throughout. **No candidate other than CTRL yields a quantum-selecting property**:
control, ℂ, a non-monomial operation, contextuality or the Born exponent (§5(b)). CTRL is rejected as the target's own
resource. The horizon-limited route (ENC-G-2) is an open conjecture.

| principle | OICORE-1 status | bearing on P | bearing on B | bearing on C |
| --- | --- | --- | --- | --- |
| FIX (one law for all operations) | C, nat. FIX_op: CX for exact control and CX dense on `Fin 2` (K); with the phase intervention, CX on `Fin 2` only | P runs with P3 arming, which is in tension with FIX (AP1:288-296). Under FIX the detector cannot be switched natively. An important A/B question for P | none: no quantum-selecting property | CX on the configuration carrier. The encoded non-affine case is open (§8.7(c) row 5) |
| ACC-R2 (V registers only its own configuration; H reaches V only through φ) | C, nat. ACC_op: CX† for exact control, with consistency with the core **open**; dense NS | it justifies the observer layer and L-HOLD; it does not produce the transition (SA-1(c) does) | **the plausible enabler of fragment-relative contextuality** (a degenerate pairing by restricted access), but only as typed access (B3) | NS |
| ACC-R1 (causal inaccessibility); ACC-R3 | R1 n/e (no causal structure); R3 unsatisfiable by any core-realizer | R1 could justify the traced-out dephasing environment | R1 could justify an `Acc` that excludes hidden cells | — |
| ACC-R4 / M-INACC | N, ext; no native instance; OC | — | a candidate route, under-specified | — |
| ACC-U (accessible but uncertifiable; CERT removed) | OC. One instance (QC22's F0) is classically imitable [draft] | — | **this is what B-CONTEXTUAL over the fragment's own equivalences operationalizes**; the precedent is imitable | — |
| FIN | C, nat (posit). FIN_op: CX exact; dense **not excluded** | — | — | consistent with rational reach; it does not exclude a dense route |
| RET-w (retention, automatic under bijectivity) | C, nat; no `T`-content | the held marker's record and its erasability are native | — | — |
| RET-s (P1 terminal registration) | N, imported idealization. Coh/Ctx excluded conditionally (AP1 Lemma 3; Theorem C [D]) | SA-1(b): needed for the non-sharpening that P relies on (AP1 C9) | — | used for heralds and detectors. Theorem C's octahedral confinement applies to the affine rules |
| CERT (spanning certification) | N, imported. It yields a noncontextual model [W] | — | **its removal (ACC-U) is what makes B able to fire at all**; with CERT kept, B is imitable | — |
| CTRL | N, emp + imp. It yields QM (EI) and is rejected as the target's resource | — | — | imported: allowed only as a labelled level-3 benchmark |
| EMB (embedded observation, observer recursion) | established (K) for OI-generated theories; supplies closure and the seam only; NI-W for control | none | none | none |
| implementation locality | established (K) for the substratum class | structural only | — | — |
| exchanges | established (K), native | — | — | the swap clause only |
| phases | stipulated; CX from observer machinery (K) | **the two-point limit of P (B2)**; quarter phases need NNB (D4(b)) | — | the stabilizer frame needs the quarter phase under U′ |
| ENC-G (new hypothesis, not adopted) | OC. ENC-G-2 is the horizon-limited conjecture | — | — | **C cannot instantiate ENC-G.** By r6's own rational-reach sketch, a positive W-CL can only show orders 3 or 6 (R60- or `S_3`-type), not infinite order or order beyond the horizon. See remark R1 for why an R60-type positive would still matter |

***

## Answers to the brief's questions

1. **Owner requirements.**
   - Met:
     - c.6733621500 (two layers; P's apparatus; D3);
     - c.6733711272 items 1, 2 and 4, the freeze decision, M-ARC's characterization and the central question;
     - c.6733825267 (non-absorption, an unread record, P primary at Level 1);
     - c.6733935953 (the two layers; "no path-correlated record").
   - Not met:
     - c.6733855134's comparable-disturbance sham (B1);
     - c.6733796760 element 3 "erased" (B5);
     - element 4's "explicitly state which classical models it excludes": the statement is inaccurate (B3);
     - c.6733796760's "discrimination on the double-slit setup" (B4);
     - c.6734304025's A/B construction (B8).
   - The comment ids are now resolvable (N1).
2. **Nativeness.**
   - Probabilities are configuration counts under uniform weights. Exact, with no amplitude, Born rule or mixing anywhere in
     P's computation. Confirmed by an independent implementation.
   - No quarter phase. The "phase cell" is a known bit added to `x`: the toy-theory `Z^φ`, ontically a deterministic flip.
     Calling it interference is honest only with the two-setting qualifier (B2.2).
   - Everything that makes P work beyond the step is B-type posit, not substratum: SA-1(c), N2, H-PREP, P3 and E-iso
     (A/B §1).
3. **Arms and validation.**
   - The sham is not disturbance-matched (B1).
   - The validation checks are exact, native, free of quantum structure, and outside the observer interface. Exceptions:
     COMP is not measured, and SPI is vacuous (N4).
   - A dephasing-like suppression can be labelled P-TRANSITION. It is so labelled on the composite fixture, and on the
     native marker the suppression is mechanically the same kick law as dephasing (B1).
   - The identifiability limit holds for screen-only observers. With the marker read (M2) under `Z±`, D is also visible in
     the observer layer (N17).
4. **B.**
   - The LP specification and the certificate independence are as in QC22 (C-INDEP is carried).
   - The scope statement is wrong in its parenthesis and lacks "over the fragment's own equivalences".
   - Given Lemma NC-F, Level 2 for OI is meaningful only relative to an owner-typed `Acc` (B3, B7). With complete access it
     is unreachable on paper.
5. **C.**
   - Correct:
     - The list of eight signed-permutation spectra.
     - The unit-root test on quadratic factors. Irreducible rational cubics cannot carry a unit-modulus pair, because the
       constant term forces a rational real root.
     - Lemma CL.
     - The labelling of Lemma P (sketch, unreviewed) in DESIGN-DS. It is not labelled so in CC-NAT (N8).
   - Gaps: the frame for odd `k` (B6); the conditioning ablation (N10).
   - C is not disguised: DESIGN-DS §6 states that the records equal the R statistics. Whether sharp copying meters count as
     "indirect access" is an owner question (N18).
6. **Blindness, §A.29 and governance.**
   - P's non-blindness is disclosed correctly. P belongs on the consistency axis (§A.23), as an end-to-end check of a paper
     derivation (N15).
   - The outcome rules carry one tuning risk: the sham definition, given the known outcome (B1). The other rules are not
     tuned.
   - The governance adopts ARP-3-QC22 r13's safeguards by reference: the dispatch-only decisive steps, attempt 1, the
     enumeration, halt-only and the Environment gate. That is consistent, but the copied text does not yet exist, and
     precondition 5's review must cover it.
7. **Relations, controls and levels.**
   - The M-ARC and Theorem C directions are stated correctly (§A.34).
   - CW-P, PL-NOREC, PL-ABSORB, PL-SHARP, PL-NOFR, B-POS, B-STAB, C-R60, C-35, C-S3, C-PLANT and C-CONSX have teeth.
   - Missing: PL-CONFOUND (B1), B-REG (B3), C-R60-ODD (B6) and an eraser look-alike (B5).
   - *Levels* never awards a higher level from a lower-level pass. Its Level 2 condition admits a different setup (B4).
8. **Findings and decisions.**
   - Findings 1, 3, 4 (`D, V ∈ {0, 1}`: the laws given `Z±` are translates of one coset, hence equal or disjoint), 5 and 7
     are correct.
   - Finding 6 is correct for the fragment but misses its own `(1, 1)` lesson (B3).
   - Finding 8 is overstated (N12).
   - D1–D13 are neutral except D8(b), which conflicts with an owner element (B5).
   - Missing decisions:
     - **D14**, the sham definition (B1);
     - **D15**, `Acc` and Level 2 eligibility (B3, B7);
     - **D16**, whether sharp copying meters count as indirect access (N18);
     - **D17**, whether B-C counts toward Level 2 (B4);
     - **D18**, the typing of the imported representations under c.6734304025 (A/B §1).

***

## Nits

- **N1.** The ids are now known:
  - six elements: c.6733796760 (06:29:08Z);
  - primary experiment: c.6733825267 (06:31:11Z);
  - safeguards: c.6733855134 (06:33:17Z);
  - identifiability: c.6733935953 (06:38:58Z);
  - A/B: c.6734304025 (07:04:54Z).

  c.6733621500 is at 06:16:40Z and c.6733711272 at 06:23:04Z. The freeze-decision, M-ARC and central-question passages are
  confirmed verbatim in c.6733711272. Add c.6734304025 and the owner's chat point on validation (once recorded) to
  *Authority*.
- **N2.** Two quotes are not verbatim, and the S4 exemption is by exact match:
  - "Identify the candidate operation …" should be "The design must identify the candidate operation, …";
  - the Level sentence is lowercase "reaching Level 2 …" in c.6733796760.
- **N3.** Precondition 2 says "D1–D12". PLAN has D13, and the new decisions D14–D18 are needed.
- **N4.** SPI is identically green in the affine class (`x` is uniform under `Z±`). Either state that it is
  non-discriminating here, or give it a mutation that can fail.
- **N5.** Define `D` over all held, unregistered cells, including the phase cell and multi-cell fixtures, not "`a`'s two
  slots". The phase cell holds `z + v_p`, which is path-independent; report it.
- **N6.** Label CPL and step 6 as an imported comparator that is unreachable under SA-1(c).
- **N7.** C-IFACE says every input of B's LP is observer-layer. QC22's rank fast path (step 2) reads the charged
  configuration laws. Either exempt certificate candidates explicitly (a verified model is sound whatever its provenance),
  or drop step 2.
- **N8.** CC-NAT's green-when column rests on Lemma P (a sketch, unreviewed) and Theorem C (conditional). Say so in the
  table. Add "or Lemma P / Theorem C(ii) fails" to its route to failure, because a red CC-NAT is then ambiguous.
- **N9.** Lemma P is plausible. Before it is cited, its sketch should spell out four things:
  - power-boundedness of the linear part, since O is full-dimensional and bounded;
  - `ΦΨ = ΨΦ`, and that `Φ` is bijective on `Ψ(O)`;
  - semisimplicity of the unit eigenvalues;
  - the non-affinely-regular centrally symmetric hexagon, whose automorphism group is a subgroup and gives no new spectra.
- **N10.** Add a `reg = none` ablation on the same `(g, m, k)`, reported (not gating), so that the "physical origin"
  (owner correction 4) says whether heralded conditioning is part of it. The C-EXPOSURE text attributes the operation to
  the rule alone.
- **N11.** L-HOLD's link misreads Main:684. Main:684 places the detector's degrees of freedom in the *visible* sector, and
  Main:688-691 concerns partition trace-out for nested observers. The screen marginal is the same whether the unread
  marker is in `V` (unregistered) or in `H`. Say that, rather than "an unread record is part of what is traced out".
- **N12.** Finding 8 and the arm table: "dephasing is native" should read "native step with a supplied N2 environment
  cell (both slots unknown, outside SA-1(c))".
- **N13.** M-ARC landed at `fd539e15` (#1208; receipt `ARP-1-MARC.json` holds; c.6734023161). Fill precondition 1 and `D`.
  The results review lists **three** qualifications (findings 9–11). The fourth item in DESIGN-DS §7 ("not a proof of
  inaccessibility") is the owner's characterization. Attribute it so.
- **N14.** Runtime: "B: at most 32 + …" reads as 32 fragments. B-P is one fragment with 32 preparations.
- **N15.** P's blindness. State P's paper expectation explicitly, as owner element 6 asks for "expected outcomes". Place P
  on the consistency axis in the note. Drop "decisive" for P in the S1 description ("the first evaluation of P's native
  instance in CI").
- **N16.** State on paper whether the native B-P table equals QM-P's. If it does, B-P's token is determined by the QM-P
  control (B3).
- **N17.** The identifiability limit is a statement about screen-only observers. Through M2 under `Z±`, the marker's
  record, and hence `D`, is observable. Say so in hazard 3.
- **N18.** Every OI detector is a meter that copies a carrier functional (C-DET; AP1 SA-1). "Indirect" in r6 means
  "through registered detector cells", not "through interference statistics". Make that explicit in *The two layers*
  and put it to the owner (D16).

## Remarks (no change required)

- **R1 (BORDERLINE).** If C ever fired with an R60-type spectrum, the gate would be of finite order, but O together with
  R60 generates an infinite subgroup of SO(3). No finite subgroup of SO(3) properly contains O, so its closure is SO(3):
  the pair is dense. So a finite-order positive would not be irrelevant to density. It would still need a bridge theorem
  (the kernel's dense route takes an infinite-order `FixedGateSourced` gate) and a native supply of the octahedral part,
  which the quarter-phase exclusion (AP1 Lemma 5) does not give under R1.
- **R2.** The eraser result (B5) and the kick/record confound (B1) both reproduce standard quantum facts: recorded
  random-Z dephasing is erasable by conditioning, and complementarity is the Englert–Scully–Walther and Storey debate. The
  findings concern what r6 may *attribute*, not a defect of the model.

## Fixed point (§A.31)

| pass | findings | classification |
| --- | --- | --- |
| 1 | B1 (record and kick confounded; the sham is the free tick) and B3 (fragment artefact) | NEW |
| 2 | B5 (eraser identity across arms), B6 (frame), B7 (L-UPRIME) | NEW |
| 3 | the A/B typing; the validation audit | ELABORATING |
| 4 | the nits | CONFIRMING |

These are four passes, but only the last two were free of NEW findings, short of the 3–4 the method asks for. The
re-review of r7 should continue the fixed-point search, especially on B's `Acc` once D15 is decided.
