# Apparatus-1: embedded reciprocal registration and the one-observer test

**Standing.** Paper-only candidate selection (owner step 1) and decisive test
(owner step 2) for the apparatus milestone of #1169. Author: Claude Code
session, 2026-11-07. Scope: [owner direction and writer record](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6711244102).
Accountable homes: #914 row 12 (observer-level available operation), #866
(interaction/access), #1169 (programme). This file proposes one changed
premise; it adopts none. No simulation, enumeration campaign, Lean build,
manuscript change, freeze, dispatch or merge is part of this unit. Small exact
checks of this file's own algebra were run as author self-checks; they are not
evidence and are not cited.

**Source snapshots.** Main: `e61e5673d335797048b8be0eec13591a9153c968`
(cited as `main@e61e5673`). Research branch carrying the #1173 papers:
`62502618074da4408162a9d5a0dfecf1b3bd8ab4` (cited as the research branch), whose first
parent is the reviewed #1173 head `8dd58694` and second parent is `main@e61e5673`.

## 0. Result

1. **Target and ceiling (§1).** The target is one carrier, one preparation,
   two selectable reads with a phase-sensitive relation between them, and a
   reusable continuation. On the physical carrier, every deterministic
   bijective apparatus generates a subtheory of the permutation theory, so it
   satisfies #914's invariants (`NonnegBounded`, `OnesBounded`) by
   construction (Lemma 2). The escape test is therefore decided on the encoded
   carrier fixed by the apparatus's physical identification. The applicable
   ceiling is #914's phase test and control tests transported to that carrier:
   C-PH (no encoded quarter phase) and C-ROT (no encoded `rot`, hence no dense
   control). Two further diagnostics are recorded but are not escape
   conditions. C-IS is the per-state isotropy bound `P + V ≤ 1` on the two
   reads. C-NC is the certified-quadruple form of MR-1's noncontextuality
   witness W1 (§1.3).
2. **Selected lead (§2–3).** Embedded reciprocal registration, SA-1. The
   observer acquires a record only through a symmetric second-order coupling
   to a ready cell with one known slot. The coupling's step is native; its
   per-tick, per-edge arming is a posit (P3). A registered record cell is
   terminal. No sharp cell is supplied. AW-MR5 left open whether native access
   implements an epistemic restriction, and S-L7 gave a conditional
   single-time answer. This file supplies posited access clauses, SA-1(b) and
   (c), under which the restriction holds and survives retention across time.
3. **Decisive test (§4).** On the native `F_2` alphabet, the coupling's
   reciprocity produces the measurement backaction. Under the posited coupling
   control P3 and isolation E-iso, the parity of the armed tick selects a `Z`
   or `X` read. Both settings act on the same heralded preparation. The full
   three-record law equals the quantum sequential Lüders law for Pauli `Z`/`X`
   reads in all four setting combinations. The failure branch is heralded and
   leaves the carrier unchanged. The state handed on retains hidden information
   that recombination can use without decoding. An eraser restores the
   conjugate value when the record has been neither registered nor copied; after
   a copy, the returned value is `x + w`. The controls derived here (C1, C3, C4,
   C5, C8, C9) are green. C2 and C6 are deferred to step 3 and were not run. C7
   is design conformance.
4. **Verdict (§4.7).** The complete operation does not escape the applicable
   ceiling. Under the one-cell identification R1, no SA-1 process, with any
   ancillas, adaptive corrections or input states, induces the encoded quarter
   phase (Lemma 5). The encoded image of `rot` is unreachable. The candidate
   supplies the phase-sensitive selectable read with a correct continuation at
   stabilizer scope and saturates the per-state isotropy bound. It is MR-1's
   countercontrol CC4 with the marking identified with the native step under
   E-iso and P3; its access premises are posits.
5. **Outcome type: stop, with three levels kept distinct (§5).**
   - Level 1, the per-state bound `P + V ≤ 1`. Removing (a), (b) or (c), or
     biasing the kick (four variants computed), gives regions containing
     points outside the quantum disk. All of them stay inside noncontextual
     4-point models (Lemma 4′). The non-isotropic preparation MP-1 likewise
     exceeds the bound with exact `Z`/`X` read laws (and an exact `Y`-read law
     if a `Y` read is supplied; SA-1 exhibits none). Exceeding this bound does
     not establish nonclassicality.
   - Level 2, the quarter phase. The finite 8-point carrier P-8 realizes it as
     an ontic permutation, with transformation contextuality in that
     construction.
   - Level 3, the continuous rotations (`rot`). Inducing `rot` with exact
     statistics excludes every finite carrier: its encoded action would be a
     finite stochastic matrix, whose unit-modulus eigenvalues are roots of
     unity, while `cos²(jφ)` with `cos φ = 3/5` is not periodic (§5.3). MP-2, a
     ball-containing carrier, is one sufficient further condition. Read as
     including all pure states and projective reads, it is infinite (Hardy) and
     preparation-contextual (Spekkens). MP-2 moves the open question to the
     re-preparation measure and, for composites, to H-Bell or measurement
     dependence.
   - Reproducing one operation does not establish the full quantum structure.
     §5 ends with two open step-3 questions: Q-A (a native finite mechanism for
     the quarter phase) and Q-B (an OI principle for the continuous rotations).

## 1. Target operation and the ruled-out step

### 1.1 The target operation

One observer, one carrier. A single preparation procedure `Π` is applied,
independently of the later setting. A setting `s ∈ {0,1}` is loaded into an
isolated controller field. The operation `O_s` is a two-outcome read with a
heralded failure outcome `⊥`, and it leaves the carrier for the next operation.
One continuation `O_{s'}`, `s' ∈ {0,1}`, follows on the state left by `O_s`.

The quantum comparator is the imported definition: carrier `C²`, `O_0` the
Lüders instrument of Pauli `Z`, `O_1` the Lüders instrument of Pauli `X`, and
for heralded failure the branch map `(1−h)·ρ`. Thus
`O_s = { h P^s_b ρ P^s_b (b = 0,1), (1−h) ρ (⊥) }`. The phase-sensitive
content is that preparations with equal `Z` law (equal diagonal) can have
different `X` laws, and that after a `Z` read the `X` value is uniform. The
quantum trace/Lüders law is the comparator's definition, not a native OI
postulate ([Gate A endpoints §2.2](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md#L108)).

### 1.2 #914's phase and control tests

The [selection record](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707416018),
[named controls](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707509318)
and [reassessment closeout](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707783516)
use the following kernel tests (all on `main@e61e5673`, under
`verification/lean-mathlib/OIBridge/`):

| Test | Statement | Ceiling it meets |
| --- | --- | --- |
| Phase | [`PhasesAvailable`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/RouteB.lean#L132): the quarter phase on any state at every level | [`onesFixing_not_phasesAvailable`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/PhaseSource.lean#L55) with [`permClass_onesFixing`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/PhaseSource.lean#L82); [`nonnegBounded_not_phasesAvailable`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L99) |
| Control (falsifier) | [`FalsifierUnavailable`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/RouteB.lean#L179): conjugation by [`rot`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/DiagonalTheory.lean#L368) `= [[3/5, 4/5], [−4/5, 3/5]]` is unavailable | [`falsifierUnavailable_of_nonnegBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/F2CoherenceControls.lean#L98), [`falsifierUnavailable_of_onesBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/F2CoherenceControls.lean#L102) |
| Control (generated) | composite unitary control; dense unitary control | [`substratumGen_not_control`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/StructuralClosure.lean#L348) (monomial class); [`nonnegBounded_not_denseUnitaryControl`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L173) |

The two invariants quantify over different objects.

- [`NonnegBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L65)
  quantifies over every available one-outcome operation (`availExt n Unit`) at
  every ancilla level `n`. These are the complete instruments with their
  outcomes coarse-grained into one; individual branches are not covered by the
  predicate alone.
- [`OnesBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/F2CoherenceControls.lean#L52)
  quantifies only over available unitary conjugations at every level.

The quarter phase and `rot` are one-outcome unitary conjugations, so both
predicates decide them. The native observer theory is nonnegativity-bounded at
every substratum ([`obsTheory_nonnegBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L84)).

**Lemma 1 (diagonal blindness of the monomial interface; paper algebra).** Let
every Kraus operator of every available branch be monomial,
`K = P_σ D` ([`IsMonomial`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/SubstratumInterface.lean#L75)).
Let readouts be configuration projectors, and let ancillas be attached in
diagonal states. Then every finite protocol's history probability
`p(h) = tr(E_h ρ)` depends on `ρ` only through `diag(ρ)`.

*Proof.* `K† |k⟩⟨k| K = |d_{σ⁻¹k}|² |σ⁻¹k⟩⟨σ⁻¹k|` is diagonal. Sums and
products of diagonal effects are diagonal. Tensoring with a diagonal ancilla
and taking the partial trace of a diagonal effect preserve diagonality. Hence
`E_h` is diagonal and `tr(E_h ρ) = Σ_k (E_h)_{kk} ρ_{kk}`. ∎

Lemma 1 is the operational reading of
[`preservesDiag_conj_of_monomial`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/SubstratumInterface.lean#L126)
for this test. Under the identification "operational state = law on the
observer's configurations", two preparations with the same `Z` law have the
same law for every setting and continuation. The target in §1.1 is
therefore excluded.

### 1.3 The applicable ceiling for this test

**Lemma 2 (every deterministic bijective apparatus is inside the class
ceiling on its physical carrier).** Let an apparatus act on a finite set of
configurations by bijections, attach fresh cells with fixed laws, and
discard cells by marginalization. Then each branch of each complete
instrument is a sum of conjugations by scaled partial permutations of the
configuration basis.

*Proof.* A bijection is a permutation matrix. Attaching a fresh cell is a
product with a fixed law. Discarding is a partial trace over the
configuration basis. Conditioning on a configuration record multiplies by a
`0/1` diagonal. ∎

Consequently the apparatus's admissible operators lie in
[`permClass`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L236),
so its generated theory is a subtheory of `permTheory`. Both invariants are
statements of the form "every available … satisfies …", so a subtheory
inherits them. They then follow from
[`nonnegBounded_of_bijectionLevel`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L74)
and from [`permClass_onesFixing`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/PhaseSource.lean#L82),
which has no hypotheses. This file makes the mapping on paper. It states no
new kernel theorem.

So on the physical carrier no deterministic OI apparatus escapes the
ceiling, whatever it does. The owner's criterion, "on the same preparation
and readout interface", is meaningful only on the operational carrier that
the apparatus's fixed physical identification defines. By the
[PC-F1 gauge control](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/PC1Controls.lean#L90),
that identification must transport states, preparations, readouts and the
reference consistently, and it must be fixed for all settings. A change of
frame alone cannot count as escape. The **applicable ceiling** consists of
#914's tests transported to the encoded carrier `C²` that the identification
defines:

- **C-PH (transported phase test):** no available process induces the
  quarter phase `S = diag(1, i)` on the encoded carrier.
- **C-ROT (transported control test):** no available process induces
  conjugation by `rot` on the encoded carrier.

The transported dense-control test is decided through `S`: encoded dense
unitary control would make `S` a limit of available encoded conjugations, which
the closedness argument of §4.7 excludes.

Two further quantities on the same two reads are recorded. They are not escape
conditions.

- **C-IS (per-state isotropy bound):** every reachable encoded state has
  predictability `P = |⟨Z⟩|` and visibility `V = |⟨X⟩|` with `P + V ≤ 1`.
  This is the knowledge-balance bound of the toy theory. It is not a
  noncontextuality bound: sharp and non-isotropic laws on a 4-point cell
  violate it inside noncontextual models, with the read-set scope stated after
  Lemma 4′ (§5.1).
- **C-NC (certified-quadruple noncontextual bound):** for four preparations
  `Π_ab` whose mixtures `½(Π_00 + Π_11)` and `½(Π_01 + Π_10)` are certified
  operationally equivalent, the average of the signed predictabilities
  `(2 Pr_ab(z = a) − 1) + (2 Pr_ab(x = b) − 1)` is at most 1. This is the
  carrier-preparation instance of MR-1's T7 inequality used for witness W1
  ([MR-1 W1](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L519);
  [Catani et al. row](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L753);
  [MR★ Lemma G](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L1020)).
  The quantum comparator reaches `√2` with the parity-oblivious-multiplexing
  states. A violation is a nonclassicality witness; it is reported if it
  occurs, but it is not required for escape.

### 1.4 What the current interface does on this target

| Interface variant | Outcome on the target | Source |
| --- | --- | --- |
| Full configuration access, no hidden information | Lemma 1: every protocol is blind to anything beyond the `Z` law | §1.2 |
| Passive two-slice receiver `R_t = (u_t(o), u_{t−1}(o))` with sharp point preparations | Perfectly distinguishable preparation sets grow without bound, so there is no fixed finite-dimensional quantum carrier | [receiver](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L47); [E-AR obstruction](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md#L11) |
| Native bidirectional receiver with a uniform or known background | A local transfer law with masking and later recovery; stops at the preparation, setting and access map | [receiver assessment §§3–6](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L88) |
| Hidden signal with a copy-only (non-disturbing) detector | The single-use law can be matched; the two-use law fails every fixed `C²` instrument | [B2 §6.2](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-source.md#L116) |
| Detector-controlled exchange with supplied references | Conditional match; the interaction itself is unsourced | [B3 §9](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-exchange.md#L142) |
| Retained hidden correlation reused by later reads | A local-history signal on reuse | [two-system §4](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241) |

In rows 2, 4, 5 and 6, a read either does not cost knowledge of the conjugate
quantity, or its disturbance comes from a separate mechanism that is not
sourced. Row 3 has the native backaction identity but no preparation, setting
or access map.

## 2. Working backward: leads

Lemma 2 rules out escaping on the physical carrier. Lemma 1 and the rows of
§1.4 locate the continuation failure in access: any phase-sensitive encoded
behaviour needs hidden information, and a correct continuation needs reads
that disturb the conjugate quantity. Enlarging the carrier or the operation set
does not by itself supply that disturbance requirement. (For C-PH it can
matter: see the 8-point rung in §5.2.) The smallest change to what the
observer couples to is therefore a change in how records are acquired.

| Lead | Covered by | Disposition here |
| --- | --- | --- |
| L1 Continuum or infinite hidden carrier (#1007/#1009) | [interface source §4](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L194) | Not re-surveyed. It reappears only as the necessary content of premise MP-2 (§5.3) |
| L2 Record conditioning and the declared cut (row 14, #1110) | same, row 1 | Not re-surveyed |
| L3 Frame or representation change (Koopman, amplitude assignment, Weil polarization) | [F2-1 A★](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L62); [C5 discovery audit, candidate 2](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/audits/foundations/c5-discovery-audit.md#L91); PC-F1 | Excluded as a source by §1.3 |
| L4 Real amplitude carrier with quadratic sensor (B1–B3, [E-AR](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md#L11), the L3 lift) | the #1173 papers | Not re-surveyed |
| L5 State-dependent or nonlinear dynamics ([P-SDC](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/observer-interface-obsmu-20261104/ANALYSIS.md#L728), [Native A](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/record-control-20261107/DESIGN.md#L27), SM adjacency) | #1110 §§4.3–4.4; PC-1 | Not re-surveyed |
| L6 Boundary-mode mediator | [pair-operation source](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/pair-operation-source.md) | Not re-surveyed |
| L7 Native bidirectional receiver: masking by a uniform background, recovery by later background access, ready slice `K = 0` | [receiver assessment](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L144) (its eq. (3)); recombination paper; two-system screen | Precursor of L9. It stopped at the preparation, setting and access gates ([§6](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L269)). The reuse failure is a control (C5) |
| L8 Epistemically restricted models (Spekkens toy, CC4) | [PC-1 C11a](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md#L426); [PC★ Q9](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/amendments/PC-star.md#L151); [MR-1 CC4](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L571) and its [instance](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L1066) | Classical controls. CC4 already derives the marker backaction from a symplectic marking with a half-known ready marker (`x_M ← x_M + x`, `p ← p + p_M`) |
| **L9 Embedded reciprocal registration** | open: [AW-MR5](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L406) ("Whether the native access implements an epistemic restriction is open"); [S-L7](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L603) (current-slice reads are isotropic at one time; retaining the earlier of two consecutive reads is not) | **Selected** |

The existing records already contain several ingredients of L9:

- the native step is symplectic (AW-MR5);
- current-slice readouts are isotropic at a single time (S-L7);
- the native bidirectional coupling gives masking and later recovery
  (receiver assessment);
- CC4's symplectic marking gives backaction from a half-known marker.

Three elements are new here. CC4's marking is identified with the native
second-order step, under E-iso and P3. The terminality posit is introduced,
together with its retention analysis (Lemma 3, C9). And the result is run
through #914's transported tests.

Two further leads are not selected as candidates. They enter §5 as rungs of
the premise ladder:

- an enlarged finite ontic space per qubit (the 8-point rung P-8, §5.2), which
  turns out to be a carrier with a permanently inaccessible functional (the
  parity `xyz`);
- a ball-containing continuum carrier (MP-2, §5.3).

## 3. The candidate SA-1

### 3.1 The changed assumption

The current interface admits passive registration of a cell's two-slice
coordinate and sharp ready cells. SA-1 replaces that with three clauses.

- **SA-1(a) Reciprocal coupling, native part.** Every coupling between the
  carrier, a meter cell and a record cell is a step of the second-order update
  `u' = k·u_nbr − v, v' = u` over `Z_q`, with symmetric coefficients. Each
  coupled step is then linear and symplectic for the form
  `ω = Σ_cells (u ∧ v)`. The step's form, its symmetry and its symplecticity
  are native for the wave branch.
- **SA-1(a′) Controlled arming (posit; ledger item P3).** The coefficient `k`
  on each edge is loaded classically per tick from a controller. The native
  rule has a fixed, translation-invariant coefficient, so per-tick, per-edge
  arming is not native. The setting selection of §4.2 rests on this posit.
- **SA-1(b) Terminal registration.** The observer acquires a record value only
  by registering the record functional of a meter cell. That is the slot
  written by its coupling, transported by the cell's free evolution. One
  functional is registered per cell. A registered cell is not coupled to any
  cell afterwards; it may be registered again on the same functional.
- **SA-1(c) Half-known ready cells.** Every supplied ready cell has exactly one
  known linear functional. Its other slot is unknown and uniformly distributed,
  independently of everything else. No cell with both slots known is supplied.

Each clause can be falsified as a modelling premise: §4.6 shows that removing
(a), (b) or (c) changes the derived record law. Clauses (a′), (b) and (c) are
new physical posits about control, access and resources.

An added idealization, **E-iso**, is also needed. The carrier and meter cells
interact with the rest of the lattice only through the controlled edges, and
other neighbour contributions are absent during the protocol. This is the
analog of B1's [E-pair](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-mode-drive.md#L25).
It is not derived.

### 3.2 Motivation

1. **The step is native, and its reciprocity yields backaction.** Visible and
   hidden lattice degrees of freedom run the same wave equation, and the
   partition imposes access without changing the update
   ([Substratum:48](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Substratum.md#L48)).
   The rule is second-order, linear and free of a self-term
   ([A4](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Substratum.md#L98),
   [A5](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Substratum.md#L100)).
   With a symmetric adjacency it is symplectic (AW-MR5, re-checked in §4.1).
   A symplectic coupling that writes a carrier value into a meter shifts the
   carrier's conjugate slot by the meter's conjugate slot (§4.1). Given (c) and
   N2, that slot is unknown and uniform, so the shift is a disturbance. With a
   known meter slot the shift would be a known displacement and no
   disturbance. No separate disturbance mechanism is inserted. The same
   identity appears as eq. (3) of the
   [receiver assessment](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L144).
2. **Registration inside φ.** The Definition makes the observer a subsystem
   coupled through φ
   ([Main §1.2](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L44)).
   A passive two-slice read is an idealization; the recombination paper
   records that its receiver is "not a construction of a complete embedded
   apparatus". SA-1(b) replaces that idealization by registration through the
   dynamics. Terminality is the classical counterpart of a record copied into an
   archive. §4.3 shows it is sufficient for retention across time to keep the
   knowledge isotropic, and dropping it permits sharpening (§4.6, C9).

   The native dynamics does not enforce terminality. On a finite substratum
   `φ^N = id`
   ([MR★ S-L6](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L595)),
   so an archive is irreversible only relative to a budget below recurrence.
   Within that budget, terminality is enforced by P3 and E-iso: the registered
   cell's edges are never armed.
3. **Closure.** Under SA-1(a)(b), a sharp cell cannot be manufactured from
   half-known cells (Lemma 3). Clause (c) is therefore a dynamically
   self-consistent initial-resource condition, of the same kind as the
   ready-state supply already tracked under #1147. Clause (c) is not derived.
   Its motivation is closure plus the E-AR obstruction, and the latter is a
   programme-internal reason. This is the weakest link.
4. **Uniform unknown slots.** The uniform law on the unknown slot uses Main's
   maximal-entropy selection
   ([Lemma 3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L56)).
   Applying it to a supplied ready cell, that is, conditionally on the ready
   constraint, goes through the open H-PREP identification (ledger). §5.1
   shows this choice is load-bearing.
5. **Literature.** Spekkens (arXiv:1409.5041) presents classical
   complementarity, a restriction of knowledge to Poisson-commuting
   functionals that "appeals to the symplectic structure", as providing "the
   beginning of a unification" of the known epistricted theories. Bartlett,
   Rudolph and Spekkens (arXiv:1111.5057) impose the analogous restriction on
   Liouville mechanics. In those works the restriction is a postulate. Here the
   backaction half follows from the native step, and the residual posits are
   (a′), (b), (c) and E-iso.

**Further consequences.**

- (i) A no-sharpening statement for every SA-1 protocol (Lemma 3).
- (ii) Unavailability of the encoded quarter phase at `q = 2` under R1
  (Lemma 5). This is a known property of the `q = 2` toy theory: Lillystone,
  Wallman and Emerson note that the Hadamard and phase gates are not elements
  of the toy theory (arXiv:1802.06121, Discussion; toy theory:
  arXiv:quant-ph/0401052). It is also the stop itself, not a success beyond the
  target.
- (iii) Herald-conditional record probabilities are dyadic rationals at
  `q = 2`.

None of the three is independent support for SA-1.

### 3.3 The apparatus

Native alphabet `F_2` (the reference branch of the recombination paper), so
`−1 = 1`. The cells are a carrier `c`, meters `m0, m1a, m1b, m2a, m2b`, and
a controller with fields `s, s'`, readiness heralds `e_j`, coupling
coefficients and a clock. An isolated cell evolves by
`(u, v) ↦ (v, u)` (free tick, the swap `J`).

| Tick | Coupled edge (coefficient 1 if armed, by P3) | Armed when |
| --- | --- | --- |
| 1 | `c–m0` | always (heralded preparation read) |
| 2 | `c–m1a` | `s = 0` and `e_1 = 1` |
| 3 | `c–m1b` | `s = 1` and `e_1 = 1` |
| 4 | `c–m2a` | `s' = 0` and `e_2 = 1` |
| 5 | `c–m2b` | `s' = 1` and `e_2 = 1` |

All other edges are uncoupled (E-iso); every cell not coupled at a tick takes
a free tick.

- **Ready meters.** A meter used at tick `t` is supplied so that its state at
  `t` is `(w, 0)`, with `w` unknown and uniform. Equivalently, it read `0` at
  tick `t − 1`. Both `m1a` and `m1b` are supplied for every setting, so the
  supply law does not depend on `s`. The unused meter is left idle.
- **Records.** After its coupling at tick `t`, a meter's `u` slot holds the
  record. The observer registers that record functional, and the meter is
  terminal from then on (SA-1(b)).
- **Heralds.** `e_j = 1` with probability `h`, independently. If `e_j = 0` the
  edge is not armed, the record is `⊥`, and the carrier takes a free tick.
- **Carrier source.** At tick 1 the carrier is uniformly unknown (a
  maximal-entropy source). No special preparation is assumed; the preparation
  is the heralded read at tick 1.

### 3.4 Hypothesis ledger

| Item | Content | Native or externally supplied | Status |
| --- | --- | --- | --- |
| N1 | Second-order linear update with symmetric adjacency; symplecticity (SA-1(a)) | Native | Native OI result (Substratum A4/A5, SM §4.1; AW-MR5) |
| N2 | Uniform law on unknown slots | Native measure; its application to supplied ready cells is supplied (via H-PREP) | Main Lemma 3, applied through the open H-PREP identification |
| N3 | Bijectivity of all ticks; finite configuration sets | Native | Native OI result |
| H-PREP | A laboratory preparation law is the in-realization conditional of the stated measure on the observer's visible past | Supplied | Open named hypothesis on main ([ANALYSIS L892–900](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/observer-interface-obsmu-20261104/ANALYSIS.md#L892); owner D-OB8, not adopted). Used to read the `r0`-conditioned classes as preparations `X_{r0}` (§4.4, D2) and in N2. The unconditional three-record law (D1) does not use it |
| P1 | SA-1(b), terminal registration | Supplied | New physical posit |
| P2 | SA-1(c), half-known ready supply with correct heralds `h` | Supplied | New physical posit; resource accounted under #1147 |
| P3 | SA-1(a′) and E-iso: per-tick, per-edge symmetric coupling coefficients loaded from a classical controller; decoupled cells | Supplied | Added posit and idealization (B1 E-pair analog; a controlled adjacency). The setting selection rests on it |
| R1 | Encoded identification of §4.2 (one cell with frame `J^{−t}` ↔ `C²` via the tetrahedral frame, so `Y = z + x`) | Supplied (mathematical representation) | Fixed for all settings |
| I1 | Pauli Lüders instruments, trace law, Bloch ball | Externally supplied (imported QM; comparator only) | Not a premise of the model |
| I2 | Results of Spekkens, Gross, Hardy, Kochen–Specker, Lillystone–Wallman–Emerson and Catani et al. used in §5 | Externally supplied (literature) | Not used in §4 |
| MP-1, P-8, MP-2 | Rungs of §5 | Supplied (conditional premises, not adopted) | §5.4 |

### 3.5 Decision rule stated in this file (same commit as the result)

The decision rule and controls below are stated in the same commit as the
derivation. Their priority over the result is not separately recorded.

**Preserved results (controls).**

| ID | Existing result to preserve | Required outcome on SA-1 |
| --- | --- | --- |
| C1 | Gate A setting independence and causal prefix ([endpoints](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md#L81)) | Uncontrolled law identical across `s` up to tick 2; settings read only at their declared ticks |
| C2 | No-signalling of complete local histories | Two-wing statement must follow from locality; deferred to step 3 |
| C3 | B2 fixed-instrument failure | The copy-only variant (reciprocity removed) must fail the same comparator |
| C4 | E-AR obstruction scope | With (b) or (c) removed, the pairwise perfectly distinguishable preparations must exceed `dim = 2`; with SA-1, they must not |
| C5 | Two-system hidden-retention leak | Retained hidden information must not let a later read recover a value conjugate to a retained record |
| C6 | Bell-local classical countercontrol | Any two-wing SA-1 must be Bell-local (CHSH ≤ 2); deferred to step 3 |
| C7 | PC-F1 transport | One frame for all settings; escape judged by C-PH and C-ROT (design conformance) |
| C8 | §A.21 exactness control | Free ticks act as the identity in the encoded frame; every coupled tick is bijective and symplectic |
| C9 | S-L7 | Re-coupling of a registered cell must be shown to break isotropy |

**Decision rule.**

- **D0.** If any derived control fails, the verdict is void. Deferred controls
  limit the verdict's scope to one wing.
- **D1 (scope match).** On the declared domain, the derived three-record law
  equals the comparator for all `(s, s')`. The failure branch and the outgoing
  state, including retained hidden information, must be derived.
- **D2 (phase sensitivity, E1).** The same preparation yields classes with
  equal `O_0` laws and different `O_1` laws.
- **D3 (decisive, E2).** The operation escapes iff C-PH or C-ROT fails for the
  complete SA-1 theory on the same encoded interface. A C-IS violation alone is
  not an escape. A C-NC violation is reported as a nonclassicality witness.
- **D4.** If D1 and D2 hold and D3 does not, the outcome is a stop. The missing
  physical assumption is then stated as a conditional premise, and what it buys
  is derived on this same test.

## 4. Decisive test

### 4.1 The coupled tick

For a carrier `(u_c, v_c)` and a meter `(u_m, v_m)` coupled with coefficient
`k` over `Z_q`:

```text
u_c' = k u_m − v_c,   v_c' = u_c,
u_m' = k u_c − v_m,   v_m' = u_m.
```

In the coordinates `(u_c, v_c, u_m, v_m)` the matrix is
`M_k = [[0,−1,k,0],[1,0,0,0],[k,0,0,−1],[0,0,1,0]]`. With the cell-ordered
form `Ω_cell = diag(J₂, J₂)` and `J₂ = [[0,1],[−1,0]]`, one has
`M_kᵀ Ω_cell M_k = Ω_cell`. The inverse is explicit: `u_c = v_c'`,
`v_c = k v_m' − u_c'`, and similarly for the meter. So the tick is bijective
and symplectic for every `k`.

In the block (slice-ordered) form `Ω_blk = [[0, I], [−I, 0]]` on `(u, v)`
with adjacency `A`, the general statement is
`[[A,−I],[I,0]]ᵀ Ω_blk [[A,−I],[I,0]] = [[Aᵀ−A, I],[−I,0]]`, which equals
`Ω_blk` iff `A = Aᵀ`.

For a ready meter `(w, 0)` and `k = 1`, the coupled tick gives:

```text
record      u_m' = u_c
kick        u_c' = w − v_c       (carrier's next value shifted by the unknown w)
memory      v_c' = u_c,  v_m' = w
```

The record copies the carrier's current slot. The reciprocal term `k·u_m` in
the carrier's own update injects the meter's unknown slot `w`. That injection
is the backaction, and the symmetry of the coupling fixes it.

### 4.2 Encoded identification

On `F_2`, define the encoded pair at tick `t` as
`(z, x) := (u_c, v_c)` for `t` even and `(v_c, u_c)` for `t` odd. A free tick
maps `(u, v)` to `(v, u)`, which is the identity on `(z, x)` (C8). A coupled
tick at `t` with a ready meter acts as follows.

- **`t` even:** record `= z`; after the tick, `(z, x + w)`. This is a `Z`
  read, and the conjugate `x` is randomized.
- **`t` odd:** record `= x`; after the tick, `(z + w, x)`. This is an `X`
  read, and the conjugate `z` is randomized.

The setting is the parity of the armed tick, which is available only through
P3 and E-iso. One frame (`J^{−t}`) is used for all settings (C7).

The identification R1 with `C²` is the tetrahedral frame. An ontic point
`(z, x)` corresponds to the Bloch-type vector
`((−1)^z, (−1)^x, (−1)^{z+x})`. A law on `F_2²` corresponds to the vector of
expectations of these three functions. A law uniform on `{z = a}`, `{x = a}`
or `{z + x = a}` corresponds to the Pauli eigenstates `Z_±`, `X_±`, `Y_±`.
The `Y` sign is a fixed convention; nothing below depends on it. Encoded `Z`
and `X` reads register `z` and `x`.

A `Y` read, registering `z + x`, is not exhibited for the §3.3 apparatus class.
A type invariant excludes it. Colour the carrier 0 and each meter 1, and give
each fresh unknown the type of the slot it enters. Then at tick `t` the `u` slot
of a colour-`χ` cell carries only variables of type `t + χ` mod 2, and its `v`
slot only type `t + χ + 1`. Free ticks and carrier–meter coupled ticks preserve
this grading. Since `z` and `x` have different types, no slot, and so no record,
equals `z + x`. The same grading keeps every determined functional type-pure,
so no `Y_±` state is reached either. The labels `Y_±` are used below only to
name toy states in the frame and in the comparator.

### 4.3 No sharpening

**Lemma 3 (isotropy of the observer's knowledge).** Under SA-1, at every tick,
the linear functionals on the active cells (those not registered) whose values
are determined by the registered records and the supplied known functionals
form an isotropic set for `ω`. In particular, no active cell is ever known on
both slots.

*Proof.* Let `I` be the supplied known functionals: one per ready cell by (c),
with none on the unknown carrier source. They are supported on distinct cells
and each is isotropic, so `I` is isotropic. Each tick is symplectic (§4.1), so
the transported `I_t` stays isotropic. Let `R` be the span of registered
functionals. By (b) they lie on terminal cells, one per cell, and are
transported by free ticks, so they commute pairwise and with every functional
supported on active cells.

A functional `f` on active cells is determined iff `f = κ + ρ` with
`κ ∈ span I_t` and `ρ ∈ R`. Take two such, `f = κ₁ + ρ₁` and `f' = κ₂ + ρ₂`.
Then

```text
0 = ω(κ₁, κ₂) = ω(f, f') − ω(f, ρ₂) − ω(ρ₁, f') + ω(ρ₁, ρ₂) = ω(f, f'),
```

because the last three terms vanish by disjoint support and commutation. ∎

The global law conditional on all records is uniform on an affine subspace.
Its marginal on any active cell is uniform on an affine subspace of `F_2²`
whose determined functionals form an isotropic set, so its dimension is 1 (a
toy pure state) or 2 (uniform). Without terminality the proof fails at
`ω(ρ₁, f') = 0`; the counterexample is C9 in §4.6.

### 4.4 Records, failure and the complete instrument

**Preparation (tick 1, odd, `X` read).** The carrier source gives an encoded
pair `(z, x)` that is uniform. Then `r0 = x`, which is uniform, and the
outgoing pair is `(z + w0, x)`. Conditional on `r0`, the carrier is uniform on
`{x = r0}`. Reading this conditional class as the laboratory preparation
`X_{r0}` uses H-PREP. The preparation procedure is the same for every `s` and
`s'`.

**Operation (window ticks 2–3).**

- `s = 0`: `r1 = z`, uniform and independent of `r0`. Outgoing state `Z_{r1}`.
- `s = 1`: `r1 = x = r0` with certainty. Outgoing state `X_{r0}`.

**Continuation (window ticks 4–5).** The same rule, applied to the incoming toy
state.

**Joint law** of `(r0, r1, r2)` with all heralds `1`, derived from the
dynamics. The quantum column is the comparator from a maximally mixed carrier:
`X` Lüders, then `O_s`, then `O_{s'}`. This unconditional law does not use
H-PREP.

| `(s, s')` | SA-1 law | Quantum comparator |
| --- | --- | --- |
| (0,0) | `¼ · [r2 = r1]` | identical |
| (0,1) | `⅛` for every triple | identical |
| (1,0) | `¼ · [r1 = r0]` | identical |
| (1,1) | `½ · [r1 = r0] · [r2 = r0]` | identical |

Here `[·]` is the indicator. Written out: (0,0) assigns `¼` to each
`(r0, r1, r1)`; (1,0) assigns `¼` to each `(r0, r0, r2)`; (1,1) assigns `½` to
each `(r0, r0, r0)`.

**D2 (E1).** For both preparation classes, `P(r1 | r0, s = 0) = ½`, while
`P(r1 | r0, s = 1) = [r1 = r0]`. The `O_0` laws are equal and the `O_1` laws
differ.

D2 does not discriminate on its own. The copy-only control C3 also satisfies
it. The discrimination comes from D1's continuation entries, in particular
`(s, s') = (0, 1)`.

**Failure branch.** With `e_j = 0` the edge is not armed, the record is `⊥`,
and the carrier takes a free tick, which is the identity on the encoded pair.
The complete instrument for setting `s` on any encoded toy state `ρ` is
therefore

```text
{ h · L^s_0(ρ),  h · L^s_1(ρ),  (1−h) · ρ  on ⊥ },
```

with `L^s_b` the toy update, which coincides with the Pauli Lüders branch on
the toy domain. Heralds are independent of the carrier and the setting, so the
failure probability carries no information.

An unheralded defect behaves differently. Take a meter supplied as `(w, w')`,
with `w'` unknown, but treated as ready. Its record is `u_c + w'`, which is
uniform, and it still kicks the carrier. Each record value then has branch map
`½ Δ_s(ρ)`, where `Δ_s` is dephasing in the read basis. That is a valid
instrument of the comparator ("measure and lose the record"). It is a
different instrument, not the one targeted.

**Probabilities.** Conditional on herald success, or for dyadic `h`, every
record probability of a finite SA-1 protocol at `q = 2` is a dyadic rational,
because it is a count of uniform bits.

### 4.5 The state handed on, retained information and recombination

After a `Z` read at even tick `t` from encoded `(z, x)`:

```text
carrier  (u_c, v_c) = (w + x, z)      encoded at t+1: (z, x + w)
meter    (u_m, v_m) = (z, w)          record z; kick variable w retained
```

The old conjugate value is not erased. It is held as the relation
`x = x_new + w` between the carrier and the meter's second slot. Neither side
alone carries information about `x`.

**Recombination without decoding.** Suppose the record has not been registered,
so the meter is still active. Apply a free tick to both cells at `t+1`, then a
coupled tick `c–m` at `t+2`. Then `(u_c, v_c) = (x, z)`, encoded at `t+3` as
`(z, x)`. The meter returns to `(0, w)`, independent of `z`. The pre-read
encoded state is restored exactly, and the record is erased. `w` is never
decoded; it cancels through the reciprocal coupling.

**Recombination after a copy.** The word is:

- `Z` read (`c–m`) at `t`;
- at `t+1`, a coupled tick `m–f` with a fresh ready cell `f`, while the carrier
  takes a free tick (`f` is registered and terminal);
- at `t+2`, a free tick on `c` and `m`;
- at `t+3`, a coupled tick `c–m`.

At `t+4` the returned conjugate value is `x + w` in every assignment, which is
uniform and independent of `x`. Over the sixteen assignments of
`(z, x, w, w_f)`, the conjugate fails to return in 8 and the full pre-read
state fails in 12. If `m` itself is registered, (b) forbids the re-coupling.

These are the classical counterparts of the eraser and of its loss once the
which-way record has been copied. They are the form in which SA-1 lets hidden
information affect later results through recombination without being decoded.

**Next operation receives.** The carrier is in a toy pure state (or a mixture
once records are discarded). Meters retain the kick variables. Unused ready
meters are untouched. Spent ready cells are recorded as consumed; a reset or
further supply is a #1147 resource.

### 4.6 Controls

| ID | Derivation | Status |
| --- | --- | --- |
| C1 | Supply, carrier source and heralds are independent of `(s, s')`; `m1a` and `m1b` are supplied for both settings; coefficients are read only at their ticks; the one-read and two-read protocols share every prefix | derived, green |
| C2 | One wing: no content. Two wings: not constructed | deferred to step 3, not run |
| C3 | Copy-only variant, a record without the reciprocal kick. At `(0,1)` it gives `r2 = r0` with certainty, where the comparator gives `⅛` per triple. The B2-type failure is reproduced, and removing SA-1(a)'s reciprocity breaks the test | derived, green |
| C4 | Removing (b) or (c) lets the observer obtain both slots (sharp `(z, x)`). The four sharp points are pairwise perfectly distinguishable, each pair by the `Z` or the `X` read, so there are 4 > 2 such preparations and no `C²` carrier: the E-AR situation. With SA-1, two toy states are perfectly distinguishable only if their supports are disjoint, that is, complementary values of one functional; the maximum is 2 (for example `Z_+`, `Z_−`) | derived, green |
| C5 | Lemma 3 at the global level: a retained record and the retained kick never combine into knowledge of both slots of an active cell. Recovery of `x` (§4.5) costs the record | derived, green |
| C6 | Main §3.3's Bell ceiling assumes a ±1 outcome in every run. SA-1 has heralded `⊥` branches, but its heralds are independent of the settings and the carrier, so conditioning on success opens no detection loophole. No two-wing SA-1 is constructed and no Bell claim is made | deferred to step 3, not run |
| C7 | A single frame `J^{−t}`; escape is decided by C-PH and C-ROT (§4.7) | design conformance |
| C8 | Free tick is the identity on `(z, x)`; `M_k` is bijective and symplectic for all `k` and `q` (§4.1) | derived, green |
| C9 | Without terminality, for an `X`-known input `x`: register a meter's record, then read its kick slot through a fresh meter. The observer knows `z` and `w`, hence `u_c' = x + w` and `v_c' = z`, and the carrier becomes sharp. This is S-L7's retention failure; SA-1(b) is a sufficient repair | derived, green |

### 4.7 Evaluation of the decisive criterion

**D1** holds on the declared domain: toy states as inputs, `Z`/`X` reads,
heralded failure, one continuation (§4.4). **D2** holds (§4.4).

**Lemma 4 (C-IS holds for SA-1).** Every encoded state reachable under SA-1
lies in the octahedron spanned by `Z_±, X_±, Y_±`, so `P + V ≤ 1`.

*Proof.* By Lemma 3, the conditional law of the carrier given any record
history is a toy pure state or uniform, and unconditional states are mixtures
of these. Their Bloch-type images are `(±1, 0, 0)`, `(0, ±1, 0)`,
`(0, 0, ±1)` and `0`. On the `(⟨Z⟩, ⟨X⟩)` plane they span the diamond
`|⟨Z⟩| + |⟨X⟩| ≤ 1`. ∎

**Lemma 4′ (C-NC holds for every law on one 4-point cell).** Let `μ_ab`, for
`a, b ∈ F_2`, be any four laws on `F_2²` with `μ_00 + μ_11 = μ_01 + μ_10`.
Then `(1/4) Σ_ab [Pr_ab(z = a) + Pr_ab(x = b)] ≤ 3/2`. Equivalently, the
average signed `P + V` is at most 1. Without the equality, the bound is 2,
attained by sharp laws.

*Proof.* Let `M = μ_00 + μ_11 = μ_01 + μ_10`, a measure of mass 2, and fix an
ontic point `λ = (z, x)`.

- In the pair `(00, 11)`, the weight `[z = a] + [x = b]` is `2` and `0` if
  `z + x = 0`, and `1` and `1` if `z + x = 1`. The pair therefore contributes
  at most `2M(λ)` when `z + x = 0` and exactly `M(λ)` when `z + x = 1`.
- For the pair `(01, 10)` the roles of the two parities are exchanged.

Summing over both pairs and all `λ` gives at most `3 Σ_λ M(λ) = 6`. ∎

**Scope of Lemma 4′.** The hypothesis `μ_00 + μ_11 = μ_01 + μ_10` is an
equality of laws. A certified operational equivalence gives it when the
certifying reads have response functions spanning the functions on `F_2²`, for
example `Z`, `X` and a `Y` read (MR★ Lemma G(ii)). Under that certification, no
law on a single 4-point cell yields W1 through this instance; this covers MP-1
and sharp laws.

SA-1 exhibits only `Z` and `X` reads (§4.2). Certified over those, equivalence
means equal `z`- and `x`-marginals only, and the test reaches `2/√3`. Four
MP-1-type laws with Bloch vectors `(±a, ±a, ±a)`, `a = 1/√3`, and the product
sign on `Y` achieve it: they are nonnegative, pairwise `Z`/`X`-equivalent, and
their `Y` marginals differ. Over the exhibited read set the test is therefore
inconclusive. What excludes it as a witness is MR-1's tomographic-completeness
caveat, not Lemma 4′. SA-1's own laws satisfy the per-state bound (Lemma 4),
which bounds every quadruple, so SA-1 is unaffected. So are the sharp and
biased-kick variants, whose reads recover the joint law.

**Lemma 5 (C-PH holds under R1).** Under the one-cell identification R1, no
SA-1 process induces the encoded quarter phase, for any ancillas, adaptive
record-conditioned corrections or input states.

*Proof.* Ancillas are attached in fixed laws independent of the carrier. The
whole process, including record-controlled corrections, is one bijection on
carrier, ancillas, records and controller, followed by discarding everything
except the carrier. Its total channel on the carrier's laws is therefore a
stochastic matrix `T` on the four ontic points. To induce `S`, `T` must send
each toy state to its `S`-image: `Z_± ↦ Z_±` and
`X_+ ↦ Y_+ ↦ X_− ↦ Y_− ↦ X_+`.

The six toy states span the signed measures on `F_2²`. Indeed
`δ_(a,b) = (1{z=a} + 1{x=b} + 1{z+x=a+b} − 1)/2`, where each indicator is
twice a toy state and `1` is the sum of two complementary indicators (MR★
Lemma G(ii) for CC4). So these conditions determine `T` uniquely. In the basis
`(00, 01, 10, 11)` and for one `Y` convention, the unique solution is

```text
T = ½ [[ 1, 1, 1,−1],
       [ 1, 1,−1, 1],
       [−1, 1, 1, 1],
       [ 1,−1, 1, 1]],
```

and the analogous matrix holds for the other convention. Each has entries
`−½`, so neither is stochastic. ∎

The same argument excludes a heralded implementation whose success branch `B`
has an input-independent probability `p > 0`: `B/p` would again be determined
uniquely. The proof uses no property of the ancilla laws, so it holds for any
supplied ancilla states, including MP-1's.

For permutations alone the argument is shorter. A permutation fixing the
cosets `{z = 0}` and `{z = 1}` lies in a Klein four-group of involutions, so
its induced action on the four `X`/`Y` states has order at most 2, while `S`
acts on them as a 4-cycle. For the §3.3 apparatus class the conclusion is also
immediate from §4.2: `S` sends `X_+` to `Y_+`, and no `Y_±` state is reached.
The restriction to R1 is essential, because `Y = z + x` there. A carrier with an independent third bit realizes `S` as a
permutation (§5.2).

**C-ROT holds under R1.** Conjugation by `rot` sends `Z_+` to the pure state
with `(⟨Z⟩, ⟨X⟩) = (−7/25, −24/25)`, where `P + V = 31/25 > 1` and
`P² + V² = 1`. By Lemma 4 that state is unreachable, so `rot` is unavailable on
the encoded carrier. Conditional on herald success it is also excluded by
dyadicity (§4.4): its `Z` read would need `P(z = 0) = (1 − 7/25)/2 = 9/25`.

**Dense control (decided through `S`, as in §1.3).** The transported
dense-control test is also met. The
encoded channels induced by SA-1 processes are stochastic matrices on four
points, determined linearly (hence continuously) by their action on the toy
states. The set of stochastic matrices is closed. Encoded `S` is a unitary whose
required `T` is not stochastic. So `S` is not a limit of available encoded
conjugations, and encoded dense unitary control fails.

**Verdict by D3:** C-PH and C-ROT both hold. The complete operation does not
escape the applicable ceiling on the same preparation and readout interface.
By D4, the outcome is a stop. No C-NC witness occurs (Lemma 4′).

**What the candidate supplies at its scope.** The marker backaction of CC4,
derived there from a symplectic marking, is here identified with a step of the
native second-order rule. The identification rests on E-iso and P3. With it, a
selectable phase-sensitive read with heralded failure and a reusable
continuation matches the comparator on the stabilizer domain. SA-1 shares
CC4's reference behaviour `V + P = 1` on the certified quadruple
([CC4 instance](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L1066)).

## 5. Outcome: stop, and three levels kept distinct

Following the owner's direction ([#1169 c.6711920779](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6711920779)),
the stop is organized by three levels that do not substitute for one another:

1. the per-state bound `P + V ≤ 1`, which a model can exceed without being
   nonclassical (§5.1);
2. the quarter phase, which a finite 8-point carrier supplies, with
   transformation contextuality in that construction (§5.2);
3. the continuous rotations, `rot` among them: inducing `rot` with exact
   statistics excludes every finite carrier, and MP-2 is one sufficient
   further condition (§5.3).

Reproducing one operation, or passing one level, does not establish the full
quantum structure. The `J_exact(A)` target requires every preparation,
instrument, adaptive protocol and composite at once.

### 5.1 Level 1: the per-state bound

On the `(P, V)` plane of the same two reads (per-state values), four variants
were computed:

| Access | Reachable per-state region | Relation to the comparator | C-NC (Lemma 4′) |
| --- | --- | --- | --- |
| SA-1 (all clauses) | diamond `P + V ≤ 1` (Lemma 4) | inside; the boundary point `(1/√2, 1/√2)` is missing | holds |
| SA-1 without (a), (b) or (c) (C3, C9, C4) | sharp states reach `(P, V) = (1, 1)` | contains points outside the disk | holds (4-point laws) |
| SA-1 with a biased kick, `P(w = 1) = p ≠ ½` | after a `Z` read of an `X`-known state, `(1, |1−2p|)` | outside the disk for every `p ≠ ½` | holds (4-point laws) |
| Quantum comparator | disk `P² + V² ≤ 1` | target | `√2` |

Each of these four variants gives either the diamond or a per-state region
containing points outside the disk. None yields the disk. All four remain
noncontextual 4-point models in the sense of Lemma 4′ (for the sharp and
biased variants the reads recover the joint law), so their `P + V > 1` points
are not nonclassicality witnesses. **Exceeding the per-state bound does
not establish nonclassicality.** This is the one-system counterpart of #1169's
"Next design question", where the screened local wave case gives CHSH ≤ 2 and
global response tables give PR behaviour. A continuous family tuned to land on
the disk would be easy to vary and is excluded by §A.29.

**Assumption-watch marker.** The uniform law on unknown slots (Main Lemma 3,
counting measure, applied through H-PREP) keeps SA-1 at the per-state
isotropy bound. A non-maximal-entropy hidden prior moves the same apparatus
beyond the disk in per-state terms. This bears on #1059's measure-selection
questions.

**Rung MP-1: a non-isotropic preparation on the 4-point cell.**
The observer can prepare the carrier cell in a law on `F_2²` whose
known content is not isotropic but whose encoded vector lies in the Bloch
ball. The example used here is the T-type law

```text
w(00) = (1+√3)/4,   w(01) = w(10) = w(11) = (3−√3)/12,
```

with encoded vector `(1, 1, 1)/√3` (unit length).

**What it buys on the same test.** All SA-1 operations act on MP-1 laws as
they act on any law.

- For the `Z` and `X` reads, `P(r = 0) = (1 + 1/√3)/2`, equal to the
  comparator. If a `Y` read is supplied (SA-1 exhibits none, §4.2), its law is
  the same and also equals the comparator.
- Each read leaves a toy pure state, and every continuation then follows §4.4,
  which equals the comparator.
- The failure branch leaves the MP-1 law untouched.
- On the `(P, V)` plane, `P + V = 2/√3 > 1` with `P² + V² = 2/3`. So C-IS fails
  on the declared domain.

That failure occurs inside a noncontextual 4-point model when equivalences are
certified over a spanning read set (Lemma 4′). Over SA-1's exhibited `Z`/`X`
reads the certified-quadruple test reaches `2/√3` and is inconclusive (scope
paragraph after Lemma 4′). MP-1 buys a per-state relaxation, not a
nonclassicality witness.

C-PH and C-ROT still hold under R1. Lemma 5 is independent of the input
states. The encoded image of `rot` needs the Bloch vector
`(−7/25, −24/25, 0)`, whose tetrahedral-frame weight at `00` is
`(1 − 31/25)/4 < 0`, so it is not a law on `F_2²`. The
parity-oblivious-multiplexing states `(±1/√2, ±1/√2, 0)` likewise have a
weight `(1 − √2)/4 < 0`. The 4-point carrier cannot hold the in-plane boundary
of the disk.

**Status.** New physical posit, and it contradicts SA-1(c). It is therefore a
weakening of (c), not an addition. As a free supply of a chosen law it is easy
to vary, since any point of the tetrahedron could be posited. It is not
adoptable under §A.29 unless a specified native process selects the law. It is
retained as a diagnostic: it shows which quantity the per-state test responds
to.

### 5.2 Level 2: the quarter phase on a finite carrier

**P-8.** The encoded qubit is carried by three binary functionals `x, y, z`
that are independent ontic variables. The ontic space is `{±1}³` (eight
points); `Y` is not `z + x`. Each read registers one functional and
re-randomizes the other two with fresh uniform bits; this is an SA-type kick
with two unknown slots. The parity `xyz` is never read, and no preparation
sets it.

This is the Wallman–Bartlett 8-state model of the single-qubit stabilizer
subtheory, as described first-hand in Lillystone–Wallman–Emerson
(arXiv:1802.06121v2).

**What it buys on the same test** (exact; author self-check of the algebra):

- The state with vector `r` has law `μ_r(λ) = (1 + r·λ)/8`. Since
  `min_λ (1 + r·λ) = 1 − |r|₁`, the law is nonnegative exactly on the
  octahedron `|r|₁ ≤ 1`, so C-IS still holds.
- A read along axis `a` gives `P(+) = (1 + r_a)/2`. After it, re-randomizing
  the other two functionals leaves the Pauli eigenstate's law, so the read and
  continuation laws equal the comparator on the stabilizer domain.
- The encoded quarter phase is the order-4 ontic permutation
  `(x, y, z) ↦ (−y, x, z)`, which carries `μ_r` to `μ_{Sr}`. C-PH fails, and
  the transported phase test is escaped.
- C-ROT holds: `rot(Z_+)` has `r = (−24/25, 0, −7/25)` and minimum weight
  `−3/100`. The rung is finite, so it carries only the stabilizer repertoire.

**Cost.** Theorem 1 of Lillystone–Wallman–Emerson (read first-hand, v2) states
that every convex-linear ontological model of the single-qubit stabilizer
subtheory is preparation-contextual or transformation-contextual. Their
subtheory is Pauli eigenstates, Pauli reads, the Clifford group including `H`
and the phase gate, and convex mixtures. In the 8-state model the contextuality
is in the transformations: their `T_1` (the uniform Pauli twirl) and
`T_2(ρ) = H T_1(ρ) H` (`T_1`, then the Hadamard) are operationally
equivalent, but the first preserves the ontic parity `xyz` and the second
reverses it (their eqs. (5)–(7)). By Theorem 1, every preparation-noncontextual
model of the full subtheory is transformation-contextual, not only the 8-state
model.

So P-8 is the "permanently inaccessible functional" lead of §2. Its escape of
C-PH costs transformation contextuality relative to the subtheory's
equivalences. Its physical source in OI is not specified here. A cell with two
slots does not carry three independent binary functionals, so P-8 needs a
larger cell or a multi-cell encoding plus a mechanism that keeps the parity
inaccessible. Status: posit.

**Remark (beyond R1).** Let `Θ` identify a finite SA-type subsystem with ontic
set `Λ` with the full single-qubit stabilizer subtheory, matching all
statistics. Assume each subtheory transformation acts on `Λ` as one stochastic
map, with ancillas fresh and discarded as in Lemma 5; this is Theorem 1's
convex-linear setting. Suppose the images of its preparations span the signed
measures on `Λ` and the images of its reads span the functions on `Λ`. Under
preparation noncontextuality the stabilizer laws are affine in `ρ`, so this
spanning hypothesis forces `|Λ| ≤ 4`, R1's size; the remark generalizes Lemma 5
across identifications of that dimension.

- Operational equivalence in the subtheory then implies equality of ontic
  laws, of stochastic transformation maps and of response functions. The
  subsystem's own model is then a universally noncontextual model of the
  subtheory, which contradicts Theorem 1.
- Hence any finite realization of `S` within the full stabilizer subtheory
  needs ontic directions that the subtheory's preparations and reads do not
  span. The 8-point parity `xyz` is one example.

This uses Theorem 1 within its stated hypotheses and adds only the spanning
argument. It does not exclude realizations of `S` outside the full subtheory,
for example without `H`.

### 5.3 Level 3: continuous rotations

**MP-2.** For each encoded qubit, the ontic carrier's representable laws
contain the whole Bloch ball. Encoded rotations are ontic bijections, and reads
re-prepare the outcome's law, with a disturbance in the sense of SA-1(a).

**What level 3 rests on (derived here).** Suppose a finite carrier with
ontic set `Λ` induces `rot` with exact statistics. As in Lemma 5, its encoded
action is one stochastic matrix `Γ` on `Λ`, applied `j` times for `rot^j`.
Prepare `Z_+` with law `μ` and read `Z` with response function `ξ`. Then
`P_j = μᵀ Γ^j ξ = cos²(jφ) = ½ + ½ cos(2jφ)`, with `cos φ = 3/5`.

- A finite stochastic matrix is power-bounded, and its unit-modulus eigenvalues
  are roots of unity (Perron–Frobenius). So `P_j` is a periodic sequence plus a
  sequence tending to 0.
- `cos 2φ = −7/25` is rational and not in `{0, ±½, ±1}`, so by Niven's theorem
  `2φ/π` is irrational, and `j ↦ 2jφ mod 2π` is equidistributed.
- If `cos(2jφ)` were asymptotically `p`-periodic, then
  `cos(2(j+p)φ) − cos(2jφ) = −2 sin((2j+p)φ) sin(pφ)` would tend to 0. The
  first factor does not tend to 0, so `sin(pφ) = 0`, which would make `e^{2iφ}`
  a root of unity. Contradiction.

So no finite carrier induces `rot` with exact statistics. This holds for `rot`
itself; it does not depend on supplying the full qubit repertoire.

**Necessary content of MP-2 (imported, not re-derived here).**

- Hardy (*Stud. Hist. Phil. Mod. Phys.* 35, 267 (2004)) shows that an
  ontological model of a qubit's pure states and projective measurements
  needs infinitely many ontic states.
- Spekkens (arXiv:quant-ph/0406166) shows that any model of the qubit's
  mixed-state decompositions is preparation-contextual.
- So MP-2, read as including all pure states and projective reads, entails an
  infinite carrier (lead L1 reappears as a necessary component) and
  preparation contextuality. C-NC can then be violated (`√2`).

Infinitude is forced by an operation with an infinite exact orbit, such as
`rot`, not by leaving the stabilizer fragment: MP-1 leaves it on four points.
The quarter phase alone is supplied by the finite rung P-8. MP-2 is one
sufficient further condition for level 3, not the only one.

**What it buys on the same test (imported existence).** The Kochen–Specker
single-qubit model (*J. Math. Mech.* 17, 59 (1967)) is a deterministic
instance:

- The ontic state is `λ ∈ S²`, and state `n` has density
  `(1/π) max(n·λ, 0)`.
- A read along `a` records the sign of `a·λ`, which gives
  `P(+|a) = (1 + n·a)/2`.
- Encoded unitaries rotate `λ`, and a read re-prepares `λ` from the density of
  its outcome direction.

On the same one-observer test this supplies `S`, `rot` and every rotation, with
the comparator's read and continuation laws. C-PH and C-ROT both fail.

**What remains concrete.**

1. **The re-preparation measure is the load-bearing choice.** A read whose kick
   re-prepares `λ` uniformly on the outcome hemisphere gives
   `P(+|a) = 1 − θ/π`, linear in the angle `θ` between `n` and `a`. Only the
   cosine-weighted law gives `(1 + cos θ)/2`. This is B2's measure question in a
   sharper form, and it belongs to #1059.
2. **Composites.** A per-qubit model of this kind does not by itself account for
   entangled composites. For a two-wing extension,
   [Main §3.3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L360)
   gives two routes, neither adopted: ontic parameter dependence (H-Bell,
   Substratum §3.3), or setting-dependent ontic ensembles (measurement
   dependence), with Main's lower bound on the ontic information. This is
   #868's composition question. MP-2 is a single-system premise only.

### 5.4 The ladder, and what would weaken, derive or rule out each rung

| Rung | C-IS | C-PH | C-ROT | C-NC | Ruled out within | First decisive check |
| --- | --- | --- | --- | --- | --- | --- |
| SA-1 | holds | holds (R1) | holds | holds | — | — |
| MP-1 | fails | holds (R1) | holds | holds over a spanning read set; inconclusive over SA-1's `Z`/`X` reads (`2/√3`) | SA-1 as stated (Lemma 3) | A native process whose prepared law is non-isotropic yet ball-contained: compute its reachable region and its certified-quadruple value |
| P-8 | holds | fails | holds | holds (prep/measure); transformation-contextual | every one-cell (R1) identification (Lemma 5) | A native multi-cell encoding with an inaccessible parity, and a mechanism keeping it inaccessible under all permitted reads |
| MP-2 | fails (`√2`) | fails | fails | can fail (`√2`) | every finite carrier (§5.3 eigenvalue argument, for `rot`) | Whether a native reciprocal read on a continuum cell with a symplectic area form (classical spin `S²` is the minimal candidate) produces the cosine-weighted re-preparation law without a supplied measure |

A further option is to weaken SA-1(c) to a quantitative sharpness bound. A
bound read off from the quantum target is a reconstruction, not a source.

The levels are separate. P-8 passes level 2 without level 3. MP-1 exceeds
level 1 without level 2. No rung establishes the full quantum structure: each
reproduces specific operations on the one-observer interface, and composites
are not addressed.

### 5.5 Classification (§A.31)

| Finding | Class |
| --- | --- |
| CC4's marker backaction identified with the native step under E-iso and P3; SA-1 gives the toy-bit read and continuation with heralded failure | Elaborating (AW-MR5, S-L7, receiver assessment) and positive (CC4 is reachable under P1–P3) |
| Terminal registration is sufficient for isotropy under retention, and its removal permits sharpening (Lemma 3, C9) | New for this programme |
| Encoded quarter-phase impossibility under R1 (Lemma 5) agrees with #914's phase ceiling and with the toy-theory literature | Confirming |
| On a 4-point cell, per-state `P + V > 1` occurs inside noncontextual models (Lemma 4′); the certified-quadruple bound holds for every law | Elaborating (MR★ Lemma G) |
| Premise ladder SA-1 → MP-1 → P-8 → MP-2 by what each buys; the maximal-entropy kick as load-bearing | New for this programme; literature has the components (Catani et al., Wallman–Bartlett, Lillystone–Wallman–Emerson, Hardy, Kochen–Specker) |

### 5.6 Open items

Open items:

- the native derivation of SA-1(a′), (b) and (c) and of E-iso;
- H-PREP;
- the source of P-8's inaccessible parity;
- the odd-`q` case;
- Bell behaviour of any extension;
- preparation of all target states;
- Born-rule selection beyond the values `0, ½, 1`;
- the full `J_exact(A)` target.

For odd prime `q`, SA-1 is expected to give the qudit stabilizer theory, by
Gross (arXiv:quant-ph/0602001: nonnegative Wigner function and Clifford
positivity in odd dimension) together with Spekkens' classical
complementarity. That would include Clifford diagonal phases while staying
inside a nonnegative frame. Whether the per-edge couplings generate the full
symplectic group is not shown. This is an expectation, not a derivation.

### 5.7 Questions for step 3 (open)

Step 3 begins only after independent review of this stop, and this file does
not start it. The two-wing run of C2 and C6 is a prerequisite check. The
step-3 questions are stated here as open, not answered:

- **Q-A.** Can OI natively produce the finite-state mechanism for the quarter
  phase (§5.2), including its transformation contextuality? This means a native
  multi-cell carrier with three independently readable functionals, an
  inaccessible parity, and reads that re-randomize the other two functionals.
- **Q-B.** What additional OI principle could produce the continuous rotations
  (§5.3)? This means a ball-containing carrier whose reads re-prepare with the
  cosine-weighted law, without a supplied measure, and whose composite
  extension respects Main §3.3.

## 6. Sources and dependencies

### 6.1 Prior repository results, with review status

| Source | Use here | Review status |
| --- | --- | --- |
| Kernel declarations in §1.2 (`main@e61e5673`) | Phase and control tests; class ceilings | On `main`; kernel-checked statements, read and not rebuilt in this unit |
| [Gate A endpoints](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md) | Comparator definition, C1 | Independently accepted (#1173), off `main` |
| [Receiver assessment](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md) | Precursor of L9 (eq. (3), masking, recovery, `K = 0`, §6 stopping point) | Accepted at scoped review (#1173), off `main` |
| B2 [measurement-source](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-source.md), B3 [measurement-exchange](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-exchange.md) | C3; §1.4 | Accepted at scoped review (#1173), off `main` |
| [Whole-model bridge](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md) | C4 | Accepted at scoped review, off `main` |
| [Two-system interface](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md) | C5 | Full review plus clock delta accepted, off `main` |
| [Correlation recombination](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md) | Passive receiver (§1.4); native `F_2` branch | Accepted at scoped review, off `main` |
| [Observer-interface source](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md) | Prior screen (§2) | Accepted at scoped review, off `main` |
| #1110 [ANALYSIS](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/observer-interface-obsmu-20261104/ANALYSIS.md) (H-PREP L892–900; P-SDC L728) | Ledger H-PREP; lead L5 | On `main` at its reviewed scope; H-PREP open (D-OB8) |
| MR-1 preregistration (AW-MR5, W1, CC4) and MR★ (S-L6, S-L7, Lemma G, CC4 instance), `main@e61e5673` | Open question, C-NC instance, countercontrol, recurrence caveat | Frozen preregistration with append-only amendments; its stage-1 token is provisional ([status](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/README.md)). S-L7's content is re-derived in Lemma 3's setting; Lemma G(ii)'s spanning identity is re-checked here |
| PC-1 C11a and PC★ Q9, `main@e61e5673` | Prior treatment of toy and Kochen–Specker models as controls | PC★ procedural standing per its owner disposition; used only as a coverage record |
| [F2-1 A★](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md), [C5 discovery audit](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/audits/foundations/c5-discovery-audit.md#L91) | L3 coverage | On `main` |
| Main [Definition](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L44), [Lemma 3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L56) and [§3.3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L360); Substratum lines 48, 98, 100 (`main@e61e5673`) | N1, N2, C6, §5.3 | Manuscript text at `main@e61e5673` |
| [GeneralCarrier](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/GeneralCarrier.lean#L100), [`oi_alone_not_qm`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/GeneralCarrier.lean#L160), [five-way minimality](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/RankGapTheory.lean#L702) | Baseline (not reproved) | On `main` |

### 6.2 Imported literature

| Work | Used for | Read in this unit |
| --- | --- | --- |
| P. Lillystone, J. J. Wallman, J. Emerson, "Contextuality and the single-qubit stabilizer subtheory", arXiv:1802.06121v2 | P-8 cost (Theorem 1, eqs. (5)–(7)); 8-state model (§5.2); toy-theory remark (§3.2) | Full text |
| J. J. Wallman, S. D. Bartlett, arXiv:1203.2652 (*Phys. Rev. A* 85, 062121) | Origin of the 8-state model (§5.2) | Title; model as described in Lillystone et al. |
| R. W. Spekkens, "Quasi-quantization: classical statistical theories with an epistemic restriction", arXiv:1409.5041 | Classical complementarity (§3.2) | Abstract |
| S. D. Bartlett, T. Rudolph, R. W. Spekkens, arXiv:1111.5057 (*Phys. Rev. A* 86, 012103) | Liouville mechanics with an epistemic restriction (§3.2) | Abstract |
| R. W. Spekkens, "In defense of the epistemic view of quantum states: a toy theory", arXiv:quant-ph/0401052 | Toy-bit identification (§4.2) | Title and corpus summaries |
| D. Gross, "Hudson's theorem for finite-dimensional quantum systems", arXiv:quant-ph/0602001 | Odd-`q` expectation (§5.6) | Abstract |
| L. Catani, M. Leifer, G. Scala, D. Schmid, R. W. Spekkens, arXiv:2207.11779 and arXiv:2211.09850 | C-NC as W1's instance (§1.3) | Abstract of 2207.11779; MR-1's reading of 2211.09850 |
| R. W. Spekkens, "Contextuality for preparations, transformations, and unsharp measurements", arXiv:quant-ph/0406166 | MP-2 necessity (§5.3) | Title; corpus summaries |
| L. Hardy, "Quantum ontological excess baggage", *Stud. Hist. Phil. Mod. Phys.* 35, 267 (2004) | MP-2 necessity (§5.3) | Not read; cited for its stated theorem |
| S. Kochen, E. P. Specker, *J. Math. Mech.* 17, 59 (1967) | MP-2 existence (§5.3) | Not read; standard model as described |

No literature result is a premise of §4. §4 is self-contained paper algebra
over `F_2` and `Z_q`.

## 7. Verification scope

The derivations in §§1–5 are paper derivations. Small exact checks of this
file's own algebra were run as author self-checks. They covered:

- symplecticity and the three-record laws;
- the copy-only control and Lemma 5's linear system;
- the eraser words, with and without the copy;
- the frame weights and Lemma 4′'s bound;
- the 8-point model: positivity region, read laws, `S` as a permutation and
  the `rot` weight;
- a no-sharpening check with and without terminal registration.

They are not committed and not evidence. No Lean build, simulation,
enumeration campaign, manuscript edit, freeze, dispatch or merge was performed.
Independent review of this file is a separate step before step 3.
