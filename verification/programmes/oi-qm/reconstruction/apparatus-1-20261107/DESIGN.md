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
   bijective apparatus lies inside #914's class ceiling (`NonnegBounded`,
   `OnesBounded`) by construction (Lemma 2), so the test is decided on the
   encoded carrier fixed by the apparatus's physical identification. There the
   applicable ceiling has three parts: the transported quarter-phase test, the
   transported `rot` control test, and the noncontextual
   predictability–visibility bound `P + V ≤ 1` on the same two reads (§1.3).
2. **Selected lead (§2–3).** Embedded reciprocal registration, SA-1. The
   observer acquires a record only through the native symmetric second-order
   coupling to a ready cell with one known slot. A registered record cell is
   terminal. No sharp cell is supplied. The open question it answers is the
   one AW-MR5 and S-L7 of MR-1 left open: whether native access implements an
   epistemic restriction, and how a restriction survives retention across time.
3. **Decisive test (§4).** On the native `F_2` alphabet, the apparatus derives
   measurement backaction from the reciprocity of the coupling. It realizes a
   selectable read: the coupling tick's parity selects the setting. Both
   settings act on the same heralded preparation. The full three-record law
   equals the quantum sequential Lüders law for Pauli `Z`/`X` reads in all
   four setting combinations. The failure branch is heralded and leaves the
   carrier unchanged. The state handed on retains hidden information that
   recombination can use without decoding: an eraser restores the conjugate
   value when the record has been neither registered nor copied, and fails
   once it has been copied. All preregistered
   controls are green.
4. **Verdict (§4.7).** The complete operation does not escape the applicable
   ceiling. Every reachable encoded state satisfies `P + V ≤ 1` (Lemma 4).
   No SA-1 process, with any ancillas, adaptive corrections or input
   states, induces the encoded quarter phase (Lemma 5). The encoded image of
   `rot` is unreachable (`P + V = 31/25`). The candidate supplies the
   phase-sensitive selectable read with a correct continuation at stabilizer
   scope, and it lands on the noncontextual boundary. Up to the native
   derivation of its access premises, it is the MR-1 countercontrol CC4.
5. **Outcome type: stop with named premises (§5).** Removing any SA-1 clause
   moves the reachable region from the diamond `P + V ≤ 1` to the square
   (stronger-than-quantum). The quantum disk `P² + V² ≤ 1` lies strictly
   between. The missing physical assumption has two levels. MP-1 is a
   non-isotropic preparation inside the Bloch ball; it buys exact quantum
   `Z`/`X`/`Y` read laws with `P + V > 1` on the same test, but not the
   quarter phase or `rot`. MP-2 is an ontic carrier per encoded qubit whose
   representable states contain the Bloch ball, which by imported theorems is
   infinite and preparation-contextual. MP-2 buys the single-system
   repertoire and moves the open question to the re-preparation measure
   (cosine versus uniform) and to H-Bell for composites.

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
postulate ([endpoints §2.2](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md#L108)).

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

The invariants are [`NonnegBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L65)
and [`OnesBounded`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/F2CoherenceControls.lean#L52).
Both quantify over every available operation at every ancilla level, so
they bound a complete instrument together with its meters, its branches and
its continuation. The native observer theory is nonnegativity-bounded at
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

Consequently the hypotheses of
[`nonnegBounded_of_bijectionLevel`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/FrozenSourcing.lean#L74)
and [`permClass_onesFixing`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/PhaseSource.lean#L82)
hold at configuration level for any such apparatus, including the one in §3.
This file maps the apparatus to that class on paper. It states no new kernel
theorem.

So on the physical carrier no deterministic OI apparatus escapes the
ceiling, whatever it does. The owner's criterion, "on the same preparation
and readout interface", is meaningful only on the operational carrier that
the apparatus's fixed physical identification defines. By the
[PC-F1 gauge control](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/PC1Controls.lean#L90),
that identification must transport states, preparations, readouts and the
reference consistently, and it must be fixed for all settings. A change of
frame alone cannot count as escape. The **applicable ceiling** is fixed here,
before §4, as the conjunction of three encoded tests on the carrier `C²` that
the identification defines:

- **C-PH (transported phase test):** no available process induces the
  quarter phase `S = diag(1, i)` on the encoded carrier.
- **C-ROT (transported control test):** no available process induces
  conjugation by `rot` on the encoded carrier.
- **C-NC (frame-independent form, same two reads):** every reachable encoded
  state has predictability `P = |⟨Z⟩|` and visibility `V = |⟨X⟩|` with
  `P + V ≤ 1`. This is the noncontextual predictability–visibility bound that
  MR-1 uses as the carrier-preparation instance of its T7 inequality for witness W1
  ([MR-1 preregistration](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L519),
  [Catani et al. row](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L753)).
  The quantum comparator reaches the disk `P² + V² ≤ 1`.

C-NC is used here as the directly derived reachable region of the candidate
(Lemma 4). The literature theorem relating `P + V ≤ 1` to generalized
noncontextuality carries its own symmetry hypotheses and is not used as a
premise.

### 1.4 What the current interface does on this target

| Interface variant | Outcome on the target | Source |
| --- | --- | --- |
| Full configuration access, no hidden information | Lemma 1: every protocol is blind to anything beyond the `Z` law | §1.2 |
| Passive two-slice receiver `R_t = (u_t(o), u_{t−1}(o))` with sharp point preparations | Perfectly distinguishable preparation sets grow without bound, so there is no fixed finite-dimensional quantum carrier | [receiver](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L47); [E-AR obstruction](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md#L11) |
| Hidden signal with a copy-only (non-disturbing) detector | The single-use law can be matched; the two-use law fails every fixed `C²` instrument | [B2 §6.2](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-source.md#L116) |
| Detector-controlled exchange with supplied references | Conditional match; the interaction itself is unsourced | [B3 §9](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-exchange.md#L142) |
| Retained hidden correlation reused by later reads | A local-history signal on reuse | [two-system §4](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241) |

The common feature of the failures in rows 2–5 is that knowledge acquired
by a read does not cost knowledge of the conjugate quantity. Either the read
is passive or non-disturbing, or the disturbance is supplied by a separate
unsourced mechanism.

## 2. Working backward: leads

Lemma 2 rules out escaping on the physical carrier. Lemma 1 and the rows of
§1.4 locate the failure in access. Any phase-sensitive encoded behaviour
needs hidden information, and the continuation needs reads that disturb the
conjugate quantity. The smallest change to what the observer couples to is
therefore a change in how records are acquired. Enlarging the carrier or the
operation set does not address it.

| Lead | Covered by | Disposition here |
| --- | --- | --- |
| L1 Continuum or infinite hidden carrier (#1007/#1009) | [interface source §4](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L194) | Not re-surveyed. It reappears only as the necessary content of premise MP-2 (§5.3) |
| L2 Record conditioning and the declared cut (row 14, #1110) | same, row 1 | Not re-surveyed |
| L3 Frame or representation change (Koopman, amplitude assignment, Weil polarization) | F2-1 A★; [C5 discovery audit, candidate 2](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/audits/foundations/c5-discovery-audit.md#L91); PC-F1 | Excluded as a source by §1.3 |
| L4 Real amplitude carrier with quadratic sensor (B1–B3, E-AR, the L3 lift) | the #1173 papers | Not re-surveyed |
| L5 State-dependent or nonlinear dynamics (P-SDC, Native A, SM adjacency) | #1110 §§4.3–4.4; PC-1 | Not re-surveyed |
| L6 Boundary-mode mediator | [pair-operation source](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/pair-operation-source.md) | Not re-surveyed |
| L7 Hidden-correlation recombination with passive reads | recombination paper; two-system screen | Its reuse failure is a control (C5 below) |
| L8 External epistemically restricted models (Spekkens toy, CC4) | [PC-1 C11a](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md#L426); [PC★ Q9](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/amendments/PC-star.md#L151); [MR-1 CC4](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L571) | Treated as stipulated controls, never derived from native access |
| **L9 Embedded reciprocal registration** | open: [AW-MR5](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L406) ("Whether the native access implements an epistemic restriction is open"); [S-L7](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L603) (current-slice reads are isotropic at one time; retaining the earlier of two consecutive reads is not) | **Selected** |

L9 is new relative to the bounded screen. The earlier records establish that
the native step is symplectic (AW-MR5) and that current-slice readouts are
isotropic at a single time (S-L7). They also use epistemically restricted
models as stipulated countercontrols. No earlier record derives the
disturbance from the native coupling. None shows how isotropy survives
records retained across time, and none runs the result through #914's test.
Two leads not selected here appear only as stated alternatives in §5: an
enlarged finite ontic space per qubit, and a restriction with permanently
inaccessible functionals.

## 3. The candidate SA-1

### 3.1 The changed assumption

The current interface admits passive registration of a cell's two-slice
coordinate and sharp ready cells. SA-1 replaces that with three clauses.

- **SA-1(a) Reciprocal coupling.** Every coupling between the carrier, a
  meter cell and a record cell is a step of the native second-order update
  `u' = k·u_nbr − v, v' = u` over `Z_q`. The coefficient `k` on each edge is
  symmetric and is loaded classically per tick from the controller. Each
  coupled step is then linear and symplectic for the form
  `ω = Σ_cells (u ∧ v)`, conditional on the loaded coefficients.
- **SA-1(b) Terminal registration.** The observer acquires a record value
  only by registering the record functional of a meter cell. That is the
  slot written by its coupling, transported by the cell's free evolution.
  One functional is registered per cell. A registered cell is not coupled
  to any cell afterwards; it may be registered again on the same functional.
- **SA-1(c) Half-known ready cells.** Every supplied ready cell has exactly
  one known linear functional. Its other slot is unknown and uniformly
  distributed, independently of everything else. No cell with both slots
  known is supplied.

These are falsifiable as modelling premises. Section 4.6 shows that removing
any one of them changes the derived record law. Clause (a) and its
symplecticity are native for the wave branch. Clauses (b) and (c) are new
physical posits about access and resources.

An added idealization, **E-iso**, is also needed. The carrier and meter cells
interact with the rest of the lattice only through the controlled edges, and
other neighbour contributions are absent during the protocol. This is the
analog of B1's E-pair. It is not derived.

### 3.2 Independent motivation

1. **The coupling is native, and its reciprocity forces backaction.**
   Visible and hidden lattice degrees of freedom run the same wave equation,
   and the partition imposes access without changing the update
   ([Substratum:48](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Substratum.md#L48)).
   The rule is second-order, linear and free of a self-term
   ([A4](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Substratum.md#L98),
   [A5](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Substratum.md#L100)).
   With a symmetric adjacency it is symplectic (AW-MR5, re-checked in §4.1).
   A symplectic coupling that writes a carrier value into a meter must shift
   the carrier's conjugate slot by the meter's conjugate slot (§4.1). No
   separate disturbance mechanism is inserted. This is the classical
   counterpart of no information without disturbance, obtained from the
   native rule.
2. **Registration inside φ.** The Definition makes the observer a subsystem
   coupled through φ
   ([Main §1.2](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L44)).
   A passive two-slice read is an idealization; the recombination paper
   records that its receiver is "not a construction of a complete embedded
   apparatus". SA-1(b) replaces that idealization by registration through
   the dynamics. Terminality is the classical counterpart of a record that has
   been copied irreversibly into an archive. §4.3 shows it is sufficient for
   retention across time to keep the knowledge isotropic. Dropping it permits
   sharpening (§4.6, control C9).
3. **Closure.** Under SA-1(a)(b), a sharp cell cannot be manufactured from
   half-known cells (Lemma 3). Clause (c) is therefore a dynamically
   self-consistent initial-resource condition, of the same kind as the
   ready-state supply already tracked under #1147. Clause (c) is **not
   derived**. Its motivation is closure plus the E-AR obstruction, and the
   latter is a programme-internal reason. This is the weakest link.
4. **Uniform unknown slots.** The unknown slot's uniform law is Main's
   maximal-entropy selection
   ([Lemma 3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L56))
   applied conditionally on the ready constraint. §5.2 shows this choice is
   load-bearing.
5. **Literature.** Classical complementarity — knowledge restricted to
   Poisson-commuting functionals — is the epistemic restriction that
   Spekkens (arXiv:1409.5041) identifies as unifying the known epistricted
   theories. It "appeals to the symplectic structure". Bartlett, Rudolph and
   Spekkens (arXiv:1111.5057) impose the analogous restriction on Liouville
   mechanics. In those works the restriction is a postulate. Here the
   dynamical half of it (backaction) is derived, and the residual posits are
   (b), (c) and E-iso.

**Independent consequences beyond the target.** (i) A no-sharpening
statement for every SA-1 protocol (Lemma 3). (ii) Exact unavailability of the
encoded quarter phase at `q = 2` (Lemma 5). This reproduces #914's phase
ceiling on the encoded carrier, a postdiction that agrees with an existing
result and was not built in. (iii) Record probabilities are dyadic rationals
at `q = 2`.

### 3.3 The apparatus

Native alphabet `F_2` (the reference branch of the recombination paper), so
`−1 = 1`. The cells are a carrier `c`, meters `m0, m1a, m1b, m2a, m2b`, and
a controller with fields `s, s'`, readiness heralds `e_j`, coupling
coefficients and a clock. An isolated cell evolves by
`(u, v) ↦ (v, u)` (free tick, the swap `J`).

| Tick | Coupled edge (coefficient 1 if armed) | Armed when |
| --- | --- | --- |
| 1 | `c–m0` | always (heralded preparation read) |
| 2 | `c–m1a` | `s = 0` and `e_1 = 1` |
| 3 | `c–m1b` | `s = 1` and `e_1 = 1` |
| 4 | `c–m2a` | `s' = 0` and `e_2 = 1` |
| 5 | `c–m2b` | `s' = 1` and `e_2 = 1` |

All other edges are uncoupled; every cell not coupled at a tick takes a free
tick.

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
  maximal-entropy source). No special preparation is assumed; the
  preparation is the heralded read at tick 1.

### 3.4 Hypothesis ledger

| Item | Content | Status |
| --- | --- | --- |
| N1 | Second-order linear update with symmetric adjacency; symplecticity | Native OI result (Substratum A4/A5, SM §4.1; AW-MR5) |
| N2 | Uniform law on unknown slots | Native selection premise (Main Lemma 3), applied conditionally |
| N3 | Bijectivity of all ticks; finite configuration sets | Native OI result |
| P1 | SA-1(b), terminal registration | New physical posit |
| P2 | SA-1(c), half-known ready supply with correct heralds `h` | New physical posit; resource accounted under #1147 |
| P3 | E-iso, decoupled cells with per-tick symmetric coefficients loaded from a classical controller | Added idealization (B1 E-pair analog; a controlled adjacency) |
| R1 | Encoded identification of §4.2 (one cell with frame `J^{−t}` ↔ `C²` via the tetrahedral frame) | Mathematical representation, fixed for all settings |
| I1 | Pauli Lüders instruments, trace law, Bloch ball | Imported QM facts (comparator only) |
| I2 | Results of Spekkens, Gross, Hardy, Kochen–Specker and Catani et al. used in §5 | Imported literature; not used in §4 |

### 3.5 Preregistration (fixed before §4)

**Preserved results (controls).**

| ID | Existing result to preserve | Required outcome on SA-1 |
| --- | --- | --- |
| C1 | Gate A setting independence and causal prefix ([endpoints](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md#L81)) | Uncontrolled law identical across `s` up to tick 2; settings read only at their declared ticks |
| C2 | No-signalling of complete local histories | One-wing statement vacuous; two-wing extension must follow from native locality (Main §3.3) |
| C3 | B2 fixed-instrument failure | The copy-only variant (reciprocity removed) must fail the same comparator |
| C4 | E-AR obstruction scope | With (b) or (c) removed, the pairwise perfectly distinguishable preparations must exceed `dim = 2`; with SA-1, they must not |
| C5 | Two-system hidden-retention leak | Retained hidden information must not let a later read recover a value conjugate to a retained record |
| C6 | Bell-local classical countercontrol | SA-1 must be a local hidden-variable model on any two-wing extension (CHSH ≤ 2); no Bell claim |
| C7 | PC-F1 transport | One frame for all settings; escape judged by C-PH, C-ROT, C-NC |
| C8 | §A.21 exactness control | Free ticks act as the identity in the encoded frame; every coupled tick is bijective and symplectic |
| C9 | S-L7 | Re-registration or re-coupling of a registered cell must be shown to break isotropy |

**Decision rule.**

- **D0.** If any control fails, the verdict is void.
- **D1 (scope match).** On the declared domain, the derived three-record law
  equals the comparator for all `(s, s')`. The failure branch must be
  derived. The outgoing state, including retained hidden information, must
  be derived.
- **D2 (phase sensitivity, E1).** The same preparation yields classes with
  equal `O_0` laws and different `O_1` laws.
- **D3 (decisive, E2).** The operation escapes iff at least one of C-PH,
  C-ROT, C-NC fails for the complete SA-1 theory on the same encoded
  interface.
- **D4.** If D1 and D2 hold and D3 does not, the outcome is a stop. The
  missing physical assumption is then stated as a conditional premise, and
  what it buys is derived on this same test.

## 4. Decisive test

### 4.1 The coupled tick

For a carrier `(u_c, v_c)` and a meter `(u_m, v_m)` coupled with coefficient
`k` over `Z_q`:

```text
u_c' = k u_m − v_c,   v_c' = u_c,
u_m' = k u_c − v_m,   v_m' = u_m.
```

In the coordinates `(u_c, v_c, u_m, v_m)` the matrix is
`M_k = [[0,−1,k,0],[1,0,0,0],[k,0,0,−1],[0,0,1,0]]`. With
`Ω = diag(J₂, J₂)` and `J₂ = [[0,1],[−1,0]]`, one has `M_kᵀ Ω M_k = Ω`.
The inverse is explicit, `u_c = v_c'`, `v_c = k v_m' − u_c'`, and similarly
for the meter. So the tick is bijective and symplectic for every `k`. The
general statement is `[[A,−I],[I,0]]ᵀ Ω [[A,−I],[I,0]] = [[Aᵀ−A, I],[−I,0]]`,
which equals `Ω` iff `A = Aᵀ`.

For a ready meter `(w, 0)` and `k = 1`, the coupled tick gives:

```text
record      u_m' = u_c
kick        u_c' = w − v_c       (carrier's next value shifted by the unknown w)
memory      v_c' = u_c,  v_m' = w
```

The record copies the carrier's current slot. The reciprocal term `k·u_m` in
the carrier's own update injects the meter's unknown slot `w`. That is the
backaction, and it is fixed by the symmetry of the coupling.

### 4.2 Encoded identification

On `F_2`, define the encoded pair at tick `t` as
`(z, x) := (u_c, v_c)` for `t` even and `(v_c, u_c)` for `t` odd. A free tick
maps `(u, v)` to `(v, u)`, which is the identity on `(z, x)`. That is control
C8.

A coupled tick at `t` with a ready meter acts on the encoded pair as follows.

- **`t` even:** record `= z`; after the tick, `(z, x + w)`. This is a `Z`
  read, and the conjugate `x` is randomized.
- **`t` odd:** record `= x`; after the tick, `(z + w, x)`. This is an `X`
  read, and the conjugate `z` is randomized.

The setting is the parity of the coupling tick. One frame (`J^{−t}`) is used
for all settings, as C7 requires.

The identification with `C²` is the tetrahedral frame. An ontic point `(z, x)`
corresponds to the Bloch-type vector `((−1)^z, (−1)^x, (−1)^{z+x})`. A law
`w` on `F_2²` corresponds to the vector of expectations of these three
functions. A law uniform on `{z = a}`, `{x = a}` or `{z + x = a}` corresponds
to the Pauli eigenstates `Z_±`, `X_±`, `Y_±`. The `Y` sign is a fixed
convention; nothing below depends on it. Encoded `Z`, `X` and `Y` reads
register `z`, `x` and `z + x`.

### 4.3 No sharpening

**Lemma 3 (isotropy of the observer's knowledge).** Under SA-1, at every
tick, the set of linear functionals on the active cells whose values are
determined by the observer's registered records and the supplied known
functionals is isotropic for `ω`. The active cells are those not registered.
In particular, no active cell is ever known on both slots.

*Proof.* Let `I` be the supplied known functionals: one per ready cell by
(c), with none on the unknown carrier source. They are supported on distinct
cells and each is isotropic, so `I` is isotropic. Each tick is symplectic
(§4.1), so the transported `I_t` stays isotropic. Let `R` be the span of
registered functionals. By (b) they lie on terminal cells, one per cell,
transported by free ticks, so they commute pairwise and with every
functional supported on active cells.

A functional `f` on active cells is determined iff `f = κ + ρ` with
`κ ∈ span I_t` and `ρ ∈ R`. Take two such, `f = κ₁ + ρ₁` and
`f' = κ₂ + ρ₂`. Then
`0 = ω(κ₁, κ₂) = ω(f, f') − ω(f, ρ₂) − ω(ρ₁, f') + ω(ρ₁, ρ₂) = ω(f, f')`,
because the last three terms vanish by disjoint support and commutation. ∎

The global law conditional on all records is uniform on an affine subspace.
Its marginal on any active cell is uniform on an affine subspace of `F_2²`
whose determined functionals form an isotropic set, so its dimension is 1
(a toy pure state) or 2 (uniform). Without terminality the proof fails at
`ω(ρ₁, f') = 0`; the counterexample is C9 in §4.6.

### 4.4 Records, failure and the complete instrument

**Preparation (tick 1, odd, `X` read).** The carrier source gives an
encoded pair `(z, x)` that is uniform. Then `r0 = x`, which is uniform, and
the outgoing pair is `(z + w0, x)`. Conditional on `r0`, the carrier is
uniform on `{x = r0}`; this is the encoded state `X_{r0}`. The preparation
procedure is the same for every `s` and `s'`.

**Operation (window ticks 2–3).**

- `s = 0`: `r1 = z`, uniform and independent of `r0`. Outgoing state `Z_{r1}`.
- `s = 1`: `r1 = x = r0` with certainty. Outgoing state `X_{r0}`.

**Continuation (window ticks 4–5).** The same rule, applied to the incoming
toy state.

**Joint law** of `(r0, r1, r2)` with all heralds `1`, derived from the
dynamics. The quantum column is the comparator from a maximally mixed
carrier: `X` Lüders, then `O_s`, then `O_{s'}`.

| `(s, s')` | SA-1 law | Quantum comparator |
| --- | --- | --- |
| (0,0) | `¼ · [r2 = r1]` | identical |
| (0,1) | `⅛` for every triple | identical |
| (1,0) | `¼ · [r1 = r0]` | identical |
| (1,1) | `½ · [r1 = r0] · [r2 = r0]` | identical |

Here `[·]` is the indicator. Written out: (0,0) assigns `¼` to each
`(r0, r1, r1)`; (1,0) assigns `¼` to each `(r0, r0, r2)`; (1,1) assigns `½`
to each `(r0, r0, r0)`.

**D2 (E1).** For both preparation classes, `P(r1 | r0, s = 0) = ½`, while
`P(r1 | r0, s = 1) = [r1 = r0]`. The `O_0` laws are equal and the `O_1` laws
differ.

**Failure branch.** With `e_j = 0` the edge is not armed, the record is
`⊥`, and the carrier takes a free tick, which is the identity on the encoded
pair. The complete instrument for setting `s` on any encoded toy state `ρ` is
therefore

```text
{ h · L^s_0(ρ),  h · L^s_1(ρ),  (1−h) · ρ  on ⊥ },
```

with `L^s_b` the toy update, which coincides with the Pauli Lüders branch on
the toy domain. Heralds are independent of the carrier, so the failure
probability carries no information.

An unheralded defect behaves differently. A meter supplied as `(w, w')` with
`w'` unknown but treated as ready gives the record `u_c + w'`, which is
uniform, and still kicks the carrier. Each record value then has branch map
`½ Δ_s(ρ)`, where `Δ_s` is dephasing in the read basis. That is a valid
instrument of the comparator ("measure and lose the record"), not a silent
change of the operation.

**Probabilities.** Every record probability of a finite SA-1 protocol at
`q = 2` is a dyadic rational, because it is a count of uniform bits.

### 4.5 The state handed on, retained information and recombination

After a `Z` read at even tick `t` from encoded `(z, x)`:

```text
carrier  (u_c, v_c) = (w + x, z)      encoded at t+1: (z, x + w)
meter    (u_m, v_m) = (z, w)          record z; kick variable w retained
```

The old conjugate value is not erased. It is held as the relation
`x = x_new + w` between the carrier and the meter's second slot. Neither
side alone carries information about `x`.

**Recombination without decoding.** Suppose the record has not been
registered, so the meter is still active. Apply one free tick to both cells
and then one further coupled tick `c–m`. Then
`(u_c, v_c) = (x, z)`, encoded at `t+3` as `(z, x)`, and the meter returns to
`(0, w)`, independent of `z`. The pre-read encoded state is restored exactly,
and the record is erased. `w` is never decoded; it cancels through the
reciprocal coupling.

If instead the record is first copied into a fresh ready cell by a coupled
tick, so that the copy is registered and terminal while `m` stays active, the
same word no longer restores `x`. Twelve of the sixteen
`(z, x, w, w_copy)` assignments fail, because the copy's kick enters `m`'s
second slot. If `m` itself is registered, (b) forbids the re-coupling.

These are the classical counterparts of the eraser and of its loss when the
which-way record is copied. They are the form of "hidden information affects
later results through recombination without being decoded" that SA-1
supplies.

**Next operation receives.** The carrier is in a toy pure state (or a
mixture once records are discarded). Meters retain the kick variables.
Unused ready meters are untouched. Spent ready cells are recorded as
consumed; a reset or further supply is a #1147 resource.

### 4.6 Controls

| ID | Derivation | Status |
| --- | --- | --- |
| C1 | Supply, carrier source and heralds are independent of `(s, s')`. `m1a` and `m1b` are supplied for both settings. Coefficients are read only at their ticks. The one-read and two-read protocols share every prefix | green |
| C2 | One wing: vacuous. Two wings: every coupling is a nearest-neighbour edge armed by its own wing's controller, so each wing's complete local history is a function of its own setting and the setting-independent source (Main §3.3 cone argument) | green at this scope; full two-wing derivation is step-3 work |
| C3 | Copy-only variant, a record without the reciprocal kick: (0,1) gives `r2 = r0` with certainty, where the comparator gives `⅛` per triple. The B2-type failure is reproduced; removing SA-1(a)'s reciprocity breaks the test | green |
| C4 | (b) or (c) removed: the observer obtains both slots (sharp `(z, x)`). The four sharp points are pairwise perfectly distinguishable, each pair by the `Z` or the `X` read, so there are 4 > 2 such preparations and no `C²` carrier — the E-AR situation. With SA-1, two toy states are perfectly distinguishable only if their supports are disjoint, that is, complementary values of one functional. The maximum is 2 (for example `Z_+`, `Z_−`) | green |
| C5 | Lemma 3 at the global level: a retained record and the retained kick never combine into knowledge of both slots of an active cell. Recovery of `x` (§4.5) costs the record | green |
| C6 | SA-1 is a deterministic local model with a setting-independent source, so Main §3.3's Bell ceiling applies to two wings (CHSH ≤ 2). No Bell claim is made | green (scoped) |
| C7 | A single frame `J^{−t}`; escape is decided by C-PH, C-ROT, C-NC (§4.7) | green |
| C8 | Free tick is the identity on `(z, x)`; `M_k` is bijective and symplectic for all `k` and `q` (§4.1) | green |
| C9 | Without terminality, for an `X`-known input `x`: register a meter's record, then read its kick slot through a fresh meter. The observer knows `z` and `w`, hence `u_c' = x + w` and `v_c' = z`, and the carrier becomes sharp. This is S-L7's retention failure; SA-1(b) is a sufficient repair | green |

### 4.7 Evaluation of the decisive criterion

**D1** holds on the declared domain: toy states as inputs, `Z`/`X` reads,
heralded failure, one continuation (§4.4). **D2** holds (§4.4).

**Lemma 4 (C-NC holds).** Every encoded state reachable under SA-1 lies in the
octahedron spanned by `Z_±, X_±, Y_±`. Hence `P + V ≤ 1`.

*Proof.* By Lemma 3, the conditional law of the carrier given any record
history is a toy pure state or uniform. Unconditional states are mixtures of
these. The Bloch-type images are `(±1, 0, 0)`, `(0, ±1, 0)`, `(0, 0, ±1)` and
`0`. On the `(⟨Z⟩, ⟨X⟩)` plane they span the diamond `|⟨Z⟩| + |⟨X⟩| ≤ 1`. ∎

**Lemma 5 (C-PH holds).** No SA-1 process induces the encoded quarter phase,
for any ancillas, adaptive record-conditioned corrections or input states.

*Proof.* Ancillas are attached in fixed laws independent of the carrier. The
whole process, including record-controlled corrections, is one bijection on
carrier, ancillas, records and controller, followed by discarding everything
except the carrier. Its total channel on the carrier's laws is therefore a
stochastic matrix `T` on the four ontic points. To induce `S`, `T` must send
each toy state to its `S`-image: `Z_± ↦ Z_±` and
`X_+ ↦ Y_+ ↦ X_− ↦ Y_− ↦ X_+`.

The six toy states span the signed measures on `F_2²`, since
`δ_(a,b) = (1{z=a} + 1{x=b} + 1{z+x=a+b} − 1)/2`, where each indicator is
twice a toy state and `1` is the sum of two complementary indicators (the identity is MR★'s Lemma G(ii) for CC4). So these conditions
determine `T` uniquely. In the basis `(00, 01, 10, 11)` and for one `Y`
convention, the unique solution is

```text
T = ½ [[ 1, 1, 1,−1],
       [ 1, 1,−1, 1],
       [−1, 1, 1, 1],
       [ 1,−1, 1, 1]],
```

and the analogous matrix for the other convention. Each has entries `−½`, so
neither is stochastic. ∎

The same argument excludes a heralded implementation whose success branch
`B` has an input-independent probability `p > 0`, because `B/p` would again be
determined uniquely. The proof uses no property of the ancilla laws, so it
holds for any supplied ancilla states, including those of §5.2.

For permutations alone the argument is shorter. A permutation fixing the
cosets `{z = 0}` and `{z = 1}` lies in a Klein four-group of involutions.
Its induced action on the four `X`/`Y` states then has order at most 2,
while `S` acts on them as a 4-cycle.

**C-ROT holds.** Conjugation by `rot` sends `Z_+` to the pure state with
`(⟨Z⟩, ⟨X⟩) = (−7/25, −24/25)`, where `P + V = 31/25 > 1` and
`P² + V² = 1`. By Lemma 4 that state is unreachable, so `rot` is unavailable
on the encoded carrier. It is also excluded by dyadicity (§4.4), since its
`Z` read would need `P(z = 0) = (1 − 7/25)/2 = 9/25`, which is not dyadic.

**Verdict by D3:** no part of the applicable ceiling fails. The complete
operation does not escape it on the same preparation and readout interface.
By D4, the outcome is a stop.

What the candidate supplies at its scope is the following. In the sources
reviewed for this unit, the read disturbance was supplied separately (B3's
exchange) or stipulated (CC4). Here it comes from the native coupling rule.
With it, a selectable phase-sensitive read with heralded failure and
a reusable continuation matches the comparator on the stabilizer domain. In
MR-1's terms it is CC4 with the epistemic restriction partly derived and
partly posited by SA-1(b)(c). It shares CC4's reference behaviour
`V + P = 1` ([CC4 instance](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L1066)).

## 5. Outcome: stop, and the missing physical assumption

### 5.1 Three regimes on one interface

On the `(P, V)` plane of the same two reads:

| Access | Reachable region | Relation to the comparator |
| --- | --- | --- |
| SA-1 (all clauses) | diamond `P + V ≤ 1` (Lemma 4) | inside; the boundary point `(1/√2, 1/√2)` is missing |
| SA-1 without (a), (b) or (c) (C3, C9, C4) | sharp states reach the square, `(P, V) = (1, 1)` | stronger than quantum |
| SA-1 with a biased kick, `P(w = 1) = p ≠ ½` | after a `Z` read of an `X`-known state, `(1, |1−2p|)` | stronger than quantum for every `p ≠ ½` |
| Quantum comparator | disk `P² + V² ≤ 1` | target |

This is the one-system analog of #1169's "Next design question", where the
screened local wave case gives CHSH ≤ 2 and global response tables give PR
behaviour. Here the native reciprocal mechanism lands exactly on the
classical boundary, and every discrete relaxation of it overshoots the
quantum region. Removing a clause of SA-1 or biasing the kick yields either
the diamond itself or a region containing points outside the disk; none
yields the disk. A continuous family tuned to hit the disk would be easy to
vary and is excluded by §A.29.

**Assumption-watch marker.** The uniform law on unknown slots (Main Lemma 3,
counting measure) is what keeps SA-1 below the quantum region. A
non-maximal-entropy hidden prior moves the same apparatus into the
stronger-than-quantum region. This bears on #1059's measure-selection
questions.

### 5.2 The missing assumption, level 1 (MP-1): a non-isotropic preparation

**MP-1.** The observer can prepare the carrier cell in a law on `F_2²` whose
known content is not isotropic but whose encoded vector lies in the Bloch
ball. The example used here is the T-type law

```text
w(00) = (1+√3)/4,   w(01) = w(10) = w(11) = (3−√3)/12,
```

with encoded vector `(1, 1, 1)/√3` (unit length).

**What it buys on the same test.** All SA-1 operations act on MP-1 laws as
they act on any law. Then `P(r = 0)` is `(1 + 1/√3)/2` for each of the `Z`,
`X` and `Y` reads, equal to the comparator. Each read leaves a toy pure state,
and every continuation then follows §4.4, which equals the comparator. The
failure branch leaves the MP-1 law untouched. On the `(P, V)` plane,
`P + V = 2/√3 > 1` with `P² + V² = 2/3`. So C-NC fails on the declared domain
and the diamond is escaped at this point.

C-PH and C-ROT still hold. Lemma 5 is independent of the input states. The
encoded image of `rot` needs the Bloch vector `(−7/25, −24/25, 0)`, whose
tetrahedral-frame weight at `00` is `(1 − 31/25)/4 < 0`, so it is not a law
on `F_2²`. The parity-oblivious-multiplexing states `(±1/√2, ±1/√2, 0)` likewise have a
weight `(1 − √2)/4 < 0`. The 4-point carrier cannot hold the in-plane
boundary of the disk.

**Status.** New physical posit, and it contradicts SA-1(c). It is therefore
a weakening of (c), not an addition. As a free supply of a chosen law it is
easy to vary (any point of the tetrahedron could be posited) and is not
adoptable under §A.29 unless a specified native process selects the law.
It is retained as a diagnostic: it shows which quantity the test responds
to.

### 5.3 The missing assumption, level 2 (MP-2): a ball-containing ontic carrier

**MP-2.** For each encoded qubit, the ontic carrier's representable laws
contain the whole Bloch ball. Encoded rotations are ontic bijections, and
reads re-prepare the outcome's law, with a disturbance in the sense of
SA-1(a).

**Necessary content (imported, not re-derived here).** Hardy (*Stud. Hist.
Phil. Mod. Phys.* 35, 267 (2004)) shows that an ontological model of a
qubit's pure states and projective measurements needs infinitely many ontic
states. Spekkens (arXiv:quant-ph/0406166) shows that any model of the
qubit's mixed-state decompositions is preparation-contextual. So MP-2 entails
an infinite carrier (lead L1 reappears as a necessary component) and
preparation contextuality. C-NC is then escaped by construction.

**What it buys on the same test (imported existence).** The Kochen–Specker
single-qubit model (*J. Math. Mech.* 17, 59 (1967)) is a deterministic
instance. The ontic state is `λ ∈ S²`. State `n` has density
`(1/π) max(n·λ, 0)`. A read along `a` records the sign of `a·λ`, which gives
`P(+|a) = (1 + n·a)/2`. Encoded unitaries rotate `λ`, and a read re-prepares
`λ` from the density of its outcome direction. On the same one-observer test
this supplies `S`, `rot` and every rotation, with the comparator's read and
continuation laws. C-PH and C-ROT both fail, so the ceiling is escaped at
the single-system level.

**What remains concrete.** Two points stay open for MP-2.

1. **The re-preparation measure is the load-bearing choice.** A read whose
   kick re-prepares `λ` uniformly on the outcome hemisphere gives
   `P(+|a) = 1 − θ/π`, linear in the angle `θ` between `n` and `a`. Only the
   cosine-weighted law gives `(1 + cos θ)/2`. This is B2's measure question in
   a sharper form, and it belongs to #1059.
2. **Composites.** A per-qubit model of this kind does not by itself account
   for entangled composites. By Bell's theorem a two-wing extension needs
   ontic parameter dependence (Main §3.3; H-Bell, Substratum §3.3), which is
   #868's composition question. MP-2 is a single-system premise only.

### 5.4 What would weaken, derive or rule out the premises

| Premise | Ruled out within | Derivation route | First decisive check |
| --- | --- | --- | --- |
| MP-1 | SA-1 as stated (Lemma 3) | A native process whose stationary or prepared law is non-isotropic yet ball-contained, without reaching the square | Compute the reachable `(P, V)` region of that process: diamond, disk or square |
| MP-2 | every finite-cell identification (Hardy) | SA-type embedded reciprocal reads on a continuum cell carrying a symplectic area form (classical spin `S²` is the minimal candidate) | Whether the native reciprocal read on that cell produces the cosine-weighted re-preparation law without a supplied measure |
| Weakening of SA-1(c) | — | Replace "no sharp supply" by a quantitative sharpness bound | Whether any bound that is not tuned to the target yields the disk; a bound read off from the quantum target is a reconstruction, not a source |

### 5.5 Open items and the first step-3 test

Open items: the native derivation of SA-1(b) and (c) and of E-iso; the
odd-`q` case; Bell behaviour of any extension; preparation of all target
states; Born-rule selection beyond the values `0, ½, 1`; and the full
`J_exact(A)` target. For odd prime `q`, SA-1 is expected to give the qudit
stabilizer theory exactly, by Gross (arXiv:quant-ph/0602001: nonnegative
Wigner function and Clifford positivity in odd dimension) together with
Spekkens' classical complementarity. That would include Clifford diagonal
phases, which the `q = 2` case lacks, while staying inside a nonnegative
frame. This expectation is stated, not derived here.

Step 3 begins only after independent review of this stop. The first test it
would run is the cheapest decisive one: SA-1 on two wings, to confirm C2 and
C6 in full and to record SA-1 as a complete classical countercontrol for the
composite interface. The premise test it would run first is the MP-2 measure
question in §5.4, row 2. That turns the remaining open item into one
computable quantity: the re-preparation law produced by an embedded
reciprocal read on a continuum cell.

### 5.6 Classification (§A.31)

| Finding | Class |
| --- | --- |
| Backaction derived from native reciprocity; SA-1 gives the toy-bit read and continuation with heralded failure | Elaborating (AW-MR5, S-L7) and positive (validates CC4 as natively reachable) |
| Terminal registration is sufficient for isotropy under retention, and its removal permits sharpening (Lemma 3, C9) | New for this programme |
| Encoded quarter-phase impossibility (Lemma 5) agrees with #914's phase ceiling | Confirming |
| Three-regime structure (diamond / disk / square) on one interface; maximal-entropy kick as the load-bearing element | New for this programme; literature has the diamond/disk comparison (Catani et al.) |
| MP-1/MP-2 as a two-level missing-assumption statement | Elaborating, with literature necessity results |

## 6. Sources and dependencies

### 6.1 Prior repository results, with review status

| Source | Use here | Review status |
| --- | --- | --- |
| Kernel declarations in §1.2 (`main@e61e5673`) | Phase and control tests; class ceilings | On `main`; kernel-checked statements, read and not rebuilt in this unit |
| [Gate A endpoints](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md) | Comparator definition, C1 | Independently accepted (#1173), off `main` |
| B2 [measurement-source](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-source.md), B3 [measurement-exchange](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-exchange.md) | C3; §1.4 | Accepted at scoped review (#1173), off `main` |
| [Whole-model bridge](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md) | C4 | Accepted at scoped review, off `main` |
| [Two-system interface](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md) | C5 | Full review plus clock delta accepted, off `main` |
| [Correlation recombination](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md) | Passive receiver (§1.4); native `F_2` branch | Accepted at scoped review, off `main` |
| [Observer-interface source](https://github.com/amaybaum/incompleteness/blob/62502618074da4408162a9d5a0dfecf1b3bd8ab4/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md) | Prior screen (§2) | Accepted at scoped review, off `main` |
| MR-1 preregistration (AW-MR5, W1, CC4) and MR★ (S-L7, CC4 instance), `main@e61e5673` | Open question, W1 instance, countercontrol | Frozen preregistration with append-only amendments; its stage-1 token is provisional ([status](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/programmes/oi-qm/reconstruction/measurement-record-formation/README.md)). S-L7's content is re-derived in Lemma 3's setting, not relied on as reviewed |
| PC-1 C11a and PC★ Q9, `main@e61e5673` | Prior treatment of toy and Kochen–Specker models as controls | PC★ procedural standing per its owner disposition; used only as a coverage record |
| [C5 discovery audit](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/audits/foundations/c5-discovery-audit.md#L91) | L3 coverage (Weil polarization) | On `main` |
| Main [Lemma 3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L56) and [§3.3](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/papers/Main.md#L360); Substratum lines 48, 98, 100 (`main@e61e5673`) | N1, N2, C2, C6 | Manuscript text at `main@e61e5673` |
| [GeneralCarrier](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/GeneralCarrier.lean#L100), [`oi_alone_not_qm`](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/GeneralCarrier.lean#L160), [five-way minimality](https://github.com/amaybaum/incompleteness/blob/e61e5673d335797048b8be0eec13591a9153c968/verification/lean-mathlib/OIBridge/RankGapTheory.lean#L702) | Baseline (not reproved) | On `main` |

### 6.2 Imported literature

| Work | Used for | Read in this unit |
| --- | --- | --- |
| R. W. Spekkens, "Quasi-quantization: classical statistical theories with an epistemic restriction", arXiv:1409.5041 | Classical complementarity (§3.2) | Abstract |
| S. D. Bartlett, T. Rudolph, R. W. Spekkens, arXiv:1111.5057 (*Phys. Rev. A* 86, 012103) | Liouville mechanics with an epistemic restriction (§3.2) | Abstract |
| R. W. Spekkens, "In defense of the epistemic view of quantum states: a toy theory", arXiv:quant-ph/0401052 | Toy-bit identification (§4.2) | Title and corpus summaries |
| D. Gross, "Hudson's theorem for finite-dimensional quantum systems", arXiv:quant-ph/0602001 | Odd-`q` expectation (§5.5) | Abstract |
| L. Catani, M. Leifer, G. Scala, D. Schmid, R. W. Spekkens, arXiv:2207.11779 and arXiv:2211.09850 | C-NC as W1's instance (§1.3) | Abstract of 2207.11779; MR-1's reading of 2211.09850 |
| R. W. Spekkens, "Contextuality for preparations, transformations, and unsharp measurements", arXiv:quant-ph/0406166 | MP-2 necessity (§5.3) | Title; corpus summaries |
| L. Hardy, "Quantum ontological excess baggage", *Stud. Hist. Phil. Mod. Phys.* 35, 267 (2004) | MP-2 necessity (§5.3) | Not read; cited for its stated theorem |
| S. Kochen, E. P. Specker, *J. Math. Mech.* 17, 59 (1967) | MP-2 existence (§5.3) | Not read; standard model as described |
| J. J. Wallman, S. D. Bartlett, arXiv:1203.2652 | Alternative enlarged finite ontic space (§2, not selected) | Title |

No literature result is a premise of §4. §4 is self-contained paper algebra
over `F_2` and `Z_q`.

## 7. Verification scope

The derivations in §§1–5 are paper derivations. Small exact checks of this
file's own algebra were run as author self-checks: symplecticity, the
three-record laws, the copy-only control, Lemma 5's linear system, the
eraser word, the frame weights and a no-sharpening check with and without
terminal registration. They are not committed and not evidence. No Lean
build, simulation, enumeration campaign, manuscript edit, freeze, dispatch or
merge was performed. Independent review of this file is a separate step
before step 3.
