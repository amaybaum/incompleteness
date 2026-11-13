# QX-4: measurement disturbance, incompatibility, and Leggett–Garg with invasiveness controls — Phase 1 experiment specification (draft)

## 0. Standing

The standing, snapshot, evidence layers (K, P, W, D, A, L) and requirement types (EN, CS, IQ, IR, MC, NX) are as in
`QX3-ANTIBUNCHING.md` §0.
- **Status.** Paper only, model-written and awaiting independent review.
- **Not done.** No mechanism is built, no computation is run, and no acceptance criterion is frozen (#1210
  c.6736966265).

***

## 1. The phenomenon and its operational observables

The experiment has three parts. All three share one carrier, one set of detectors and one construction.

**QX-4a. Disturbance and order dependence.** A two-valued carrier is prepared and read sequentially by two
detector types, `S_Z` and `S_X` (QX-0's path and port reads; C's `S_Z` and `S_X` meters). The observables are:
- the sequential joint laws `P(z₁, x₂)`, `P(x₁, z₂)` and `P(z₁, x₂, z₃)`;
- **order dependence**: whether `P_{Z→X}(z, x) ≠ P_{X→Z}(z, x)`;
- the repeatability `P(z₃ = z₁)`, with an intervening `X` read and without one;
- **no-signalling in time** (NSIT, Kofler and Brukner, PRA 87, 052115 (2013); L): `P(z₃)` with and without a read at
  `t₂`, the read's outcome summed over.

**QX-4b. Incompatibility witnessed by a parity-oblivious task.** Four preparations are labelled by two bits
`(b₀, b₁)`, and either `S_Z` or `S_X` is read to guess `b_y`. The observables are:
- the success rate `P_succ`;
- the parity-obliviousness check: the law of every read is independent of `b₀ ⊕ b₁`, verified over the fragment's own
  operational equivalences.

`P_succ > 3/4` with parity-obliviousness is equivalent to preparation contextuality (Spekkens et al., PRL 102, 010401
(2009); L). This part is QX-5's method applied to a two-read fragment. Under programme rule 6 it is run as a QX-5
scenario, not as separate work (§4).

**QX-4c. Leggett–Garg with invasiveness controls.** One binary quantity `Q = ±1` is read at times `t₁ < t₂ < t₃`, with
one fixed operation `G` applied between reads. The observables are:
- `C_ij = ⟨Q_i Q_j⟩`, from runs that read only at `t_i` and `t_j`;
- the four three-term Leggett–Garg forms `K₃^{(s)} = s₁ C₁₂ + s₂ C₂₃ + s₃ C₁₃`, with `s₁s₂s₃ = −1`. Macrorealism per
  se together with non-invasive measurability bounds each by 1 (Leggett and Garg, PRL 54, 857 (1985); L). The
  standard form is `K₃ = C₁₂ + C₂₃ − C₁₃ ≤ 1`.
- three invasiveness controls:
  - **(i) Adroitness** (Wilde and Mizel, Found. Phys. 42, 256 (2012); abstract read). Each read at `t₂` is applied to
    each eigen-preparation of `Q`, and its effect on the subsequent law of `Q₃` is measured. A violation then
    excludes macrorealist models whose invasiveness would show in those control runs. Only a collusion loophole
    remains.
  - **(ii) Ideal negative measurement (INM).** A detector that interacts only with one value of `Q` is placed at
    `t₂`, and only its silent runs are used (Knee et al., Nat. Commun. 7, 13253 (2016); Robens et al., PRX 5, 011003
    (2015); L).
  - **(iii) NSIT at `t₂`.**

**Observer access.** Detector records only, with conditioning on recorded outcomes. Each detector is a meter cell
coupled through the native step and terminally registered (SA-1(b)).

**Validation layer.** Per detector, computed from the construction:
- the kernel `K` of the unread conjugate functional (Q-C2-1 `DESIGN-DS.md` §4 [D]);
- for an INM detector, the kernel `K_null` on its silent branch;
- `D`;
- whether `Q` is a configuration functional, which decides whether macrorealism per se holds of `Q` in the ontic
  model.

## 2. QM's predictions and the classical alternatives each witness excludes

**QM's predictions** (comparators; IQ):
- **Disturbance (4a).** For `Z⁺` followed by `X` then `Z`, `P(z₃ = z₁) = 1/2`; without the `X` read it is 1. The
  sequential `Z/X` laws depend on order. NSIT fails whenever `t₂`'s read does not commute with the evolved `Q₃`.
- **Joint measurability.** Unsharp `Z` and `X` with sharpnesses `η_Z` and `η_X` are jointly measurable iff
  `η_Z² + η_X² ≤ 1` (Busch, PRD 33, 2253 (1986); L). Classical mixing of sharp reads reaches only the line
  `η_Z + η_X ≤ 1`.
- **4b.** Qubit `P_succ = (1 + 1/√2)/2 ≈ 0.854`, which needs non-stabilizer preparations or reads at `π/4`. With
  stabilizer preparations and Pauli reads, `P_succ ≤ 3/4`, because that fragment has a noncontextual model.
- **4c.** For a qubit under rotation by `θ` about an axis `n` between `Z` reads, `C(θ) = n_z² + (1 − n_z²) cos θ`. With
  `n ⊥ z`, `K₃ = 2cos θ − cos 2θ`, maximal at `θ = π/3` with `K₃ = 3/2`. Every probability there is rational. Main's
  `lg_comb_probes.py` uses this case (Main:486).
- **INM.** QM predicts the same violation with ideal negative measurements: the silent detector's effect is the
  state update.

**The witnesses and the classes each one excludes.**

| witness | excludes | does not exclude |
| --- | --- | --- |
| order dependence, loss of repeatability, NSIT violation (4a) | only classical models with sharp, non-invasive reads | every invasive classical model. Epistemically restricted models reproduce the stabilizer sequential `Z/X` Lüders law with backaction (Spekkens' toy theory; AP1 §0 and OICORE-1 §5(b) for construction B [W, D]). Main's classical comb reproduces arbitrary sequential laws with permutation instruments (Main:478-486) [P, exact] |
| intermediate incompatibility, a point beyond the line `η_Z + η_X = 1` | nothing classical: a classical wave with a partially rotated polarization marker reaches `V² + D² = 1` | — (quantum-compatible only) |
| 4b, `P_succ > 3/4` with parity-obliviousness on the fragment's equivalences | preparation-noncontextual models **over that fragment's equivalences** | models in which those equivalences fail ontically (Q-C2-1 r6 B3: a classical two-bit register read one bit at a time reaches `P_succ = 1` [D]). Contextuality is relative to the fragment and needs an owner-typed access class with a completeness check (#1210 c.6734406842 item 2) |
| 4c, `K₃ > 1` alone | macrorealism per se with non-invasive measurability (and induction) | every invasive macrorealist model, Main's comb among them (`K₃ = 3/2` with a classical permutation realization; Main:486 [P, exact; `lg_comb_probes.py`]) |
| 4c with adroitness control (i) | macrorealist models whose invasiveness shows on eigen-preparations, up to collusion | epistemically restricted invasive models in which the kick lands on a variable already unknown under the eigen-preparation (A4.3); the classes Maroney and Timpson identify as untouched by LG violation (arXiv:1412.6139; abstract read) |
| 4c with INM control (ii) | macrorealist models in which a silent detector leaves the ontic state unchanged | models with **null-result invasiveness**: the detector acts on the ontic state on its silent branch (A4.4) |

## 3. What the experiment needs from an OI construction

| # | requirement | type | status |
| --- | --- | --- | --- |
| R4.1 | the step, N2, the supplies (`Z±`, `X±`) and H-PREP | EN / CS | available (shared with QX-0) |
| R4.2 | the `S_Z` and `S_X` meters with terminal registration | CS (SA-1(b)) | available (Q-C2-1 C's detectors; AP1) |
| R4.3 | backaction: each record comes with a kick on the conjugate functional | consequence of EN reciprocity with CS SA-1(c) | available. The `Z/X` sequential Lüders law at stabilizer scope is conditional on the SA-1 posits (AP1 §0 [W]; OICORE-1 §5(b) [D]) |
| R4.4 | a fixed operation `G` between reads, applied repeatedly | EN (affine symplectic maps) for Clifford-class `G`; **MC** for non-Clifford `G` | Clifford class: available. Non-Clifford: Obligation C |
| R4.5 | reads at non-Pauli directions, or non-stabilizer preparations, for 4b's quantum value | MC | not available natively. `V` and `D` lie in `{0, 1}`, and intermediate values only on `V + D = 1` (`DESIGN-DS.md` §5 finding 4 [D]) |
| R4.6 | an owner-typed access class and completeness check for 4b | CS (D15-type) | method available (Q-C2-2's exact LP with Farkas certificates and attributed completions [D]) |
| R4.7 | the validation fields `K`, `K_null`, `D` and the configuration-functional status of `Q` | method | definable |
| R4.8 | an adroitness control: reads applied to eigen-preparations, and the effect on `Q₃` measured | access and validation | posable natively with the `Z±` supplies |
| R4.9 | **an INM detector**, interacting only when `Q` has one value | NX (location-based detection, as in QX-3's routing) | **not posable in the affine encoded setting**. There `Q` is a functional, not a location, and the meter couples to the carrier for either value. It needs QX-3's non-affine routing (QX-3 R3.6) |
| R4.10 | **null-result invasiveness** of the INM detector, `K_null ≠ id` | NX constraint on R4.9's coupling | required if QX-4c-INM is to match QM (A4.4) |

**Paper derivations** (A; unreviewed).

**A4.1. At native scope, Leggett–Garg is not violated.**
- **Setting.** Take the encoded carrier `(z, x)` over `F_2` under affine symplectic maps, with `Z`-type reads that
  carry SA-1(c) backaction.
- **Correlators.** After a `Z` read the conjugate `x` is uniform. An affine map `M` sends the functional `z` to
  `z + c`, to `x + c` or to `z + x + c`, so `C = ±1` in the first case and `0` in the other two.
- **Composition.** Write `a = C₁₂`, `b = C₂₃` and `c = C₁₃`, and use symplecticity: a map fixing `z` up to a constant
  sends `x` to `x` or `x + z`. Then:
  - if `a, b ≠ 0`, then `c = ab`;
  - if `a ≠ 0` and `b = 0`, then `c = 0`;
  - if `a = 0` and `b ≠ 0`, then `c = 0`;
  - if `a = b = 0`, then `c ∈ {−1, 0, 1}`.
- **Bound.** Each case gives `K₃ = a + b − c ≤ 1`, and by the relabellings each of the four forms is bounded the same
  way.
- **Quantum counterpart.** Clifford unitaries with Pauli reads give the same table, since a Pauli either commutes or
  anticommutes with `Z`.
- **Consequence.** The quantum Leggett–Garg violation needs a non-Clifford `G`. QX-4c depends on Obligation C (MC).

**A4.2. Non-stabilizer preparations alone do not help.** With a Clifford-class `G` and `Z` reads, the correlators above
do not depend on the preparation. So C-NONSTABILIZER, which reaches non-stabilizer states but no non-Clifford fixed
operation, does not enable a violation.

**A4.3. Adroitness passes in construction B and in quantum mechanics.**
- On a `Z±` preparation the conjugate slot is already unknown and uniform. The `t₂` read's kick does not change the
  law of `Q₃` there.
- Construction B's reads therefore pass the adroitness control, while remaining invasive on `X±` preparations and at
  the ontic level (`DESIGN-DS.md` §1: every recording carries a kick [D]).
- QM's projective reads pass the same control.
- **Consequence.** Construction B with a Leggett–Garg violation would itself be a model in the "invasive but adroit"
  class. Adroitness then cannot exclude epistemically restricted models.

**A4.4. Without null-result invasiveness, OI's own ontic model obeys the INM bound.**
- In OI, `Q` read through a configuration functional is definite at every time, so macrorealism per se holds of `Q` in
  the ontic model.
- If an INM detector's silent branch leaves the ontic configuration unchanged (`K_null = id`), the standard
  Leggett–Garg argument applies to OI's own deterministic model. Then every INM form of `K₃ ≤ 1` holds, against QM's
  prediction.
- **Consequence.** An OI construction matching QM under INM controls must have null-result invasiveness. The coupling
  must act on the ontic state even when the detector does not fire.
- In the affine reciprocal coupling the kick is independent of the outcome, so the property holds there. But the
  affine class cannot pose INM at all (R4.9).
- So an OI QX-4c-INM needs a location-based detector, which needs QX-3's routing, whose coupling keeps an
  outcome-independent kick. This is the same constraint as QX-3's A3.2, from the other side.

**A4.5. Leggett–Garg needs only two applications of `G`.** The fixity a C instance must show for QX-4c is over two
compositions. C-SIZE-DEPENDENT (fixed at `K = 6`) therefore suffices for posing QX-4c, though not for Level 4's
repeated compositions.

**A4.6. Leggett–Garg values for the spectra C can report** (QM comparators on paper, IQ, not OI predictions):
- **R60 type** (a rotation by `π/3`): `K₃ = 3/2` with axis `⊥ z`, and `K₃ = 4/3` with the axis along a body diagonal
  (`C₁₂ = C₂₃ = 2/3`, `C₁₃ = 0`).
- **A rotation by `arccos(3/5)`** with axis `⊥ z` (possible when `STAB(K)` is false; cone review [D]):
  `K₃ = 6/5 + 7/25 = 37/25`.
- **`S_3` type** `{−1, ω, ω²}`: `det = −1`, so it is not a rotation. Its order-3 rotational part violates
  `C₁₂ + C₂₃ + C₁₃ ≥ −1` (value `−3/2`) when `z` lies in its rotation plane. Whether such a record map is a valid
  transformation is C's `VAL` and `CONS` question.
- **Caveat.** The OI value depends on the C operation's axis relative to `S_Z`, its affine part `α`, and the
  backaction of the `t₂` read on the carrier after the gadget. None is computed here.

**Corpus search (§A.19).** OI already states the following.
- Main §3.4(iii) (Main:654): Leggett–Garg protocols are "intervention-rooted and belong to the intervention dilation
  — the delivered formalism underdetermines them". Residual pre-division memory would show as deviations from
  quantum multi-time predictions, "a falsifiable texture".
- Main:486 *Remark (scope of the closure)*: the classical action-labelled comb reproduces the quantum Leggett–Garg
  violation, `K = 3/2`, with invasive permutation instruments. So "the open remainder is therefore not the numbers".
  It is exact (`lg_comb_probes.py`).
- Main:488 *Proposition (no uniform finite realization)*, and the remark that the operational bridge's remainder is
  the instrument algebra: the composition of noncommuting interventions and complete positivity.
- Main cites Le et al. [26], temporal Tsirelson for divisible dynamics.

So QX-4c's numbers are already reachable by a classical realization in OI's corpus. QX-4's content is not the
numbers. It is whether one fixed construction produces them with the controls of §1 and the invasiveness structure
of A4.3 and A4.4.

## 4. Reuse of the single shared construction

**Shared with QX-0, QX-1, QX-2 and QX-7.**
- The carrier and supplies, the `S_Z` and `S_X` meters, and the SA-1 clauses.
- The backaction mechanism of R4.3. It is the same mechanism that carries QX-0's complementarity.
- The fixed operation `G` of QX-4c must be C's operation, or QX-1's, or QX-7's, under the same rule and detectors. A
  QX-4-specific gate is not admissible.

**Shared with QX-5.** 4b is a prepare-measure fragment. It uses Q-C2-2's method (exact LP, Farkas certificates,
Lemma NC-F, attributed completions) and QX-5's owner-typed access class. It is proposed as a QX-5 scenario.

**Shared with QX-3.** R4.9 and R4.10 need QX-3's routing and location-based detectors. A single routing rule must give
QX-3's dynamical exclusivity and QX-4's INM with null-result invasiveness, and keep QX-0's complementarity.

**Specific to QX-4:**
- the three-time schedule;
- the adroitness and INM control runs;
- `K_null`;
- the NSIT pairs.

**Flagged experiment-specific assumptions.**
- The identification of `Q` with a detector functional (IR; L-CAL and L-UPRIME for C's carrier).
- A supplied `π/3` rotation is IQ and allowed only in a labelled benchmark arm.

## 5. A/B arms and candidate ablations (outline only; not frozen)

**Arms.**
- **`A_4`.** As in Q-C2-1, not posable without the B scaffolding. Its closest posable form drops SA-1(c): sharp
  supplies record without kicking. The paper expectation: 4a order dependence vanishes for sharp supplies, and
  `K₃ ≤ 1`.
- **`B_4-nat`.** Construction B with native affine `G`. The paper expectations:
  - 4a shows order dependence and NSIT violation (Level 1 only; classically imitable);
  - 4b gives `P_succ ≤ 3/4` at stabilizer scope;
  - 4c gives `K₃ ≤ 1` (A4.1).
- **`B_4-C`.** Construction B with `G` = a C-EXPOSURE (or C-SIZE-DEPENDENT) operation. 4c is posable, and its value
  is not predicted (A4.6). INM is posable only with routing (`B_4-C-route`).
- **Benchmark.** `G` = a supplied rotation by `π/3` (IQ), labelled level-3 benchmark.
- **Comparators** (gating nothing):
  - CC-4: Main's classical comb, `K₃ = 3/2`, invasive;
  - NIM-4: a non-invasive macrorealist model, `K₃ ≤ 1`;
  - ER-4: the toy theory at stabilizer scope.

**Candidate ablations.** Each reports `pred_change`, `mech_change` and `access_only`.

| ablation | kind | paper expectation |
| --- | --- | --- |
| ABL-SA1c: sharp supplies admitted | state restriction; credit none | 4a: some reads record without kicking. `pred_change` true; `mech_change` true |
| ABL-SA1b: both slots of a meter registered | access; credit none | the observer reads the kick value, so NSIT and order dependence can be undone by conditioning. `access_only` true |
| ABL-RECIP: a copy-only (non-reciprocal) meter | dynamics | no backaction. `pred_change` true (4a and 4c); `mech_change` true |
| ABL-G: non-Clifford `G` replaced by its Clifford projection, or the affine rule | dynamics | 4c `K₃ ≤ 1` (A4.1) |
| ABL-NULL: INM detector with `K_null = id` | dynamics | `K₃ ≤ 1` under INM (A4.4), against QM |
| ABL-ACC4b: 4b's access class completed with every slot of every cell | access | contextuality, if present, is expected to be restored to a model (Lemma NC-F [D]). It reports the access-relativity |

## 6. Dependence on Q-C2-1's outcomes (decision tree)

```
Q-C2-1 P token
├─ P-VOID / P-NO-RECORD ── R4.3's backaction is unvalidated. 4a holds; 4b and 4c still depend on C.
├─ P-RECORD-WITHOUT-SUPPRESSION ── B admits reads without backaction. 4a's disturbance is not universal over the
│                          read class. Record it, and require ABL-SA1c's reading before 4c.
└─ P-COMPLEMENTARITY ──── R4.3 is validated (at Level 1). 4a is a reuse of P's apparatus.

Q-C2-1 C token (governs 4c and 4b)
├─ C-EXPOSURE
│   ├─ STAB(12) true, R60 type {1, e^{±iπ/3}} ── 4c posable with G = that operation. It needs
│   │                          two compositions (A4.5). K₃ depends on the axis and affine part (A4.6), not
│   │                          predicted. INM additionally needs routing (QX-3).
│   ├─ STAB(12) true, S_3 type {−1, ω, ω²} ── improper. 4c posable only for the C₁₂+C₂₃+C₁₃ ≥ −1 form, if
│   │                          the rotation plane contains z, and only if VAL and CONS hold.
│   └─ STAB(12) false ──────── spectrum without an order bound (e.g. arccos(3/5)). 4c posable; K₃ not predicted.
├─ C-SIZE-DEPENDENT ─────── 4c still posable: fixity over 2 compositions suffices (A4.5). Level 4 cannot be
│                          reached from it.
├─ C-NONSTABILIZER ──────── no non-Clifford fixed operation. 4c not posable natively (A4.1, A4.2). 4b may become
│                          posable with non-stabilizer preparations, subject to QX-5's access typing.
├─ C-SURVIVAL ───────────── 4c is benchmark-only (IQ π/3 rotation, labelled). 4a stays at Level 1. 4b's native
│                          fragment stays at stabilizer scope.
└─ C-VOID ───────────────── no reading.

Q-C2-1 B token
├─ B-CONTEXTUAL on B-P, Acc typed CS ── 4b inherits the typing question. Its own fragment needs its own Acc and
│                          completeness check. A result does not transfer between fragments, because
│                          contextuality is not monotone (Q-C2-2 [D]).
└─ B-CLASSICALLY-IMITABLE ── 4b at stabilizer scope is expected to be imitable as well.

Q-C2-1 REP-INV: if L-CAL or L-UPRIME is reclassified as imported, 4c on C's carrier becomes a benchmark result.
```

## 7. Known feasibility obstacles

1. **Invasiveness is constitutive.** Every OI read is a coupling through `φ`. Under SA-1(c) each record comes with a
   kick (`DESIGN-DS.md` §1 [D]). And `Q`, read through a configuration functional, is definite at all times. So OI is
   a macrorealist-per-se, invasive model of `Q`. An OI Leggett–Garg violation cannot refute macrorealism for OI. It
   can only show that OI's invasiveness has the structure the controls test (A4.3, A4.4).
2. **No violation at native scope** (A4.1). `{0, π}` phases and affine `G` give `K₃ ≤ 1`. 4c needs Obligation C.
3. **INM is not posable in the encoded setting** (R4.9). It needs routing, and then null-result invasiveness (A4.4),
   which constrains the routing coupling QX-3 needs.
4. **Adroitness does not discriminate** against epistemically restricted models (A4.3).
5. **Incompatibility at native scope is classically imitable** (§2). Intermediate incompatibility (off the line
   `V + D = 1`) needs C's resource and is still quantum-compatible only.
6. **4b's contextuality is relative to the fragment** and needs an owner-typed access class (Q-C2-1 r6 B3; #1210
   c.6734406842 item 2).
7. **Rational probabilities.** The quantum optimum of 4b, `(1 + 1/√2)/2`, is irrational and exactly unreachable with
   dyadic N2 laws. The quantum optimum of 4c (`3/2` at `π/3`) is rational.
8. **The numbers alone are not new.** Main:486 already gives `K₃ = 3/2` from a classical comb. QX-4c's content is the
   single fixed construction together with the controls.

## 8. Mapping to the significance ladder (no level is awarded from a lower one)

- **Level 1.**
  - 4a: order dependence, loss of repeatability and NSIT violation, with QX-0's validated backaction. This is
    quantum-compatible disturbance.
  - 4c in benchmark form only: not credited.
- **Level 2.** At most one of the following, each printed with the classes it does not exclude (§2):
  - 4b's `P_succ > 3/4`, over an owner-typed access class;
  - 4c's `K₃ > 1` with the adroitness control. It excludes non-invasive macrorealism and the Wilde–Mizel class, and
    construction B itself lies in the class that passes (A4.3).
- **Level 3.** The QX-4c violation is produced with `G` generated natively (C-EXPOSURE, or C-SIZE-DEPENDENT over two
  compositions) and through the shared detectors, and Levels 1–2 hold.
- **Level 4.** Not tested.

## 9. Owner questions (neutral)

- **Q4-1.** Should 4b be run as a QX-5 scenario rather than inside QX-4? (Programme rule 6.) (a) Yes. (b) No: QX-4
  carries it.
- **Q4-2.** Which control counts for 4c at Level 2? (a) Adroitness. (b) INM, which needs QX-3's routing. (c) Both,
  reported separately.
- **Q4-3.** How is a supplied non-Clifford `G` typed for 4c when C does not supply one? (a) An IQ benchmark arm only.
  (b) 4c is deferred.

## 10. References to content off `main` (§A.42 item 8)

| reference | claim | classification |
| --- | --- | --- |
| Main:478-488, :654; `lg_comb_probes.py` | the classical comb reproduces `K₃ = 3/2`; Leggett–Garg belongs to the intervention dilation | on `main` (P, exact probe) |
| AP1 §0 (`apparatus-1-20261107/DESIGN.md`) | the `Z/X` sequential Lüders law at stabilizer scope | on `main` (W), conditional |
| Q-C2-1 r13 drafts (`DESIGN-DS.md` §§1, 4, 5, 6; cone review) | backaction, finding 4, C's spectra and STAB | off `main` (D) |
| Q-C2-2 `ACCESS.md` §5 (Lemma NC-F) | 4b's method and its access-relativity | off `main` (D) |
| Leggett–Garg 1985; Kofler–Brukner 2013; Wilde–Mizel 2012; Knee et al. 2016; Robens et al. 2015; Maroney–Timpson 2014; Spekkens et al. 2009; Busch 1986 | §§1–2 | literature. The Wilde–Mizel and Maroney–Timpson abstracts were read; the others were not read first-hand |
