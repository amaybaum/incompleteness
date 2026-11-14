# QX-3: single-quantum statistics and antibunching — Phase 1 experiment specification (draft)

## 0. Standing

- **Authority.** #1210, Phase 1 paper-only design of QX-3, QX-4 and QX-6 (owner authorization recorded in #1210
  c.6736966265, amaybaum, 2026-11-09). Not authorized and not done here: mechanism construction, any computation
  (including probes of a proposed OI mechanism), frozen acceptance criteria, execution.
- **Status.** Model-written, paper only, awaiting independent review. It adopts no premise, freezes no rule and changes no
  scientific status (§A.45 rule 1). Every rule below is an outline. Where a rule is stated, it is a candidate for a later
  preregistration, not a frozen criterion.
- **Snapshot.** Corpus read at `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`. Session drafts are read as
  they stood on 2026-11-09:
  - Q-C2-1 preregistration draft r13 (`fefd3b6e…`), with r12 (`38c27d3a…`) and the text accepted at r11b
    (`f0436d4a…`);
  - `DESIGN-DS.md` r13 (`fbfbd9fa…`);
  - `DECISIONS.md` (`df4b5d78…`);
  - `OICORE-1.md` r6 (`9b82ecc2…`).
- **Evidence layers** (as in OICORE-1 §0):
  - **K**: kernel;
  - **P**: a paper proof on `main`;
  - **W**: a reconstruction record on `main`, model-reviewed only and never an established premise (§A.46 item 7);
  - **D**: an off-`main` draft;
  - **A**: a derivation in this file, on paper and unreviewed;
  - **L**: literature, not read first-hand unless stated.
- **Requirement typing** (owner, #1169 c.6734304025):
  - **EN**: established native;
  - **CS**: candidate strengthened, with its justification status;
  - **IQ**: imported quantum assumption, allowed only in a labelled benchmark arm;
  - **IR**: imported representation (an identification typed by the owner under Q-C2-1 D18);
  - **MC**: dependent on the missing coherent-mixing mechanism (Q-C2-1 Obligation C, or OICORE-1's drive clause, §8.4);
  - **NX**: a dynamics extension not yet typed by anyone, which needs independent justification before it can be
    typed CS.

***

## 1. The phenomenon and its operational observables

**Phenomenon.** A source emits one excitation per trial. The excitation meets a 50:50 splitter whose two outputs
go to detectors `D_A` and `D_B` (the Hanbury Brown–Twiss arrangement). For a single-quantum source the two detectors
do not fire in the same trial. The same source, sent instead into a two-path interferometer, shows phase-dependent
interference. Grangier, Roger and Aspect combined the two (Europhys. Lett. 1, 173 (1986); L).

**Observer access.** Detector records only. The observer holds, per trial:
- the herald bit `h`, if a herald detector `D_H` is used;
- the setting `s ∈ {split, recombine}`, and in the recombine configuration the phase setting `φ`;
- the click bits `a`, `b` (split) or the port bit `p` (recombine).

No carrier slot, path variable or hidden cell is registered (L-ACC, as in Q-C2-1).

**Full-mass accounting.** Every trial is counted, including trials without clicks. The only conditioning admitted is
on the herald, and only when the herald is registered before the setting is applied and its law does not depend on
the setting. Detection-based postselection is not admitted.

**Observables (exact rationals in every construction considered).**
- `P_A = P(a = 1 | h = 1)`, `P_B`, and `P_AB = P(a = 1, b = 1 | h = 1)`.
- `α = P_AB / (P_A P_B)`: Grangier's anticorrelation parameter, the heralded `g⁽²⁾(0)`. Its unheralded form drops `h`.
- `V = |P(p = 0 | φ = 0) − P(p = 0 | φ = π)|`, over the two native phase settings.
- `N_0 = P(a = 0, b = 0 | h = 1)`, the heralded no-click mass. It is reported, because a low `P_AB` obtained through
  missing clicks is a loss artefact, not exclusivity.
- An optional extension (§3, R3.10) is Hong–Ou–Mandel coincidence visibility, with two sources and one splitter.

**Validation layer** (computed from the construction; never observer data, and never an import of quantum behaviour):
- `NCONS`: whether the number of excitations is conserved by the splitter dynamics on the ready support.
- `NONABS`: no absorption of the excitation before detection.
- `CLICK`: whether each detector's registered functional is the occupation of its own cell. This is the click
  identification, R3.5.
- `D` and `K` for the interferometer arms, as in Q-C2-1.

## 2. QM's predictions and the classical alternatives each witness excludes

**QM's predictions** (comparators only; IQ):
- An ideal one-photon Fock source gives `α = 0` and `N_0 = 0`. With independent detector efficiency `η < 1` it
  still gives `α = 0`.
- A Fock-`n` source gives `g⁽²⁾(0) = 1 − 1/n`. A coherent source gives `1`; a thermal source gives `2`.
- In the recombine configuration, the same Fock-1 source gives `V = 1` at `φ ∈ {0, π}`.
- Hong–Ou–Mandel: two indistinguishable single photons on a 50:50 splitter give coincidence probability 0. Fully
  distinguishable photons give `1/2`. The visibility is `1`.

**The witnesses and the classes each one excludes.**

| witness | excludes | does not exclude |
| --- | --- | --- |
| **W1**: `α < 1` | classical fields with square-law, independent detection. The Cauchy–Schwarz inequality gives `α ≥ 1` (Clauser, Phys. Rev. D 9, 853 (1974); L) | classical particle models, for which `α = 0` is trivial; classical fields read by non-square-law or correlated detectors; deterministic hidden-variable models, Bohmian ones and OI's configuration model among them |
| **W2**: `α < 1` and `V > 0` on one source preparation, selected by the setting | W1's class, and particle models with no wave-like phase variable | epistemically restricted classical models. The toy field theory of Catani, Leifer, Schmid and Spekkens (Quantum 7, 1119 (2023); abstract read) has modes with an occupation number and a phase, and reproduces Mach–Zehnder interference, the bomb tester, delayed choice and the eraser. Construction B of Q-C2-1 is itself an epistemically restricted classical model, noncontextual at stabilizer scope (`DESIGN-DS.md` §4 [D]; OICORE-1 §5(b)) |
| **W3** (optional): Hong–Ou–Mandel visibility `> 1/2` | classical fields, which are limited to visibility `≤ 1/2` (L, standard) | not determined here whether an epistemically restricted discrete model reproduces the full dip. This needs a literature check before W3 is designed |

**Consequence for the ladder.** The strongest classical class QX-3 can exclude is classical fields under square-law
detection (W1, W2). It excludes no epistemically restricted model and no deterministic hidden-variable model, OI's
included. Whether exclusion of that class meets the ladder's Level 2 ("excludes a defined class of classical
explanations") is an owner decision (§9, Q3-1).

## 3. What the experiment needs from an OI construction

| # | requirement | type | status in the current toolkit |
| --- | --- | --- | --- |
| R3.1 | one bijective second-order step on finite cells (L-BIJ, L-SYM) | EN | available (Main:44-46, 62) |
| R3.2 | probabilities from configuration counting (N2) | CS (close to native for `H`; supplied for apparatus cells) | available; it gives dyadic rationals only |
| R3.3 | a single-excitation source: a cell with the location (path) known and the phase unknown (`Z±`-type), and the phase-known form (`X±`) for the recombine setting | CS (SA-1(c), H-PREP) | available in encoded form (Q-C2-1 P) |
| R3.4 | a splitter and a recombiner | EN in encoded form (free ticks; affine) | encoded: available. Spatial: see R3.6 |
| R3.5 | detectors as meter cells, terminal registration, and the click identification "a click is the occupation of the detector's own cell" | CS (SA-1(b)); click identification IR | available as meters. Click identification: **new**. In Q-C2-1 its role is played by L-PORT, typed under D18 |
| R3.6 | **exclusivity generated by the dynamics**: one excitation reaches exactly one of two spatially separate detectors, each registering its own cell's occupation | NX (non-affine, number-conserving; classical reversible) | **not available in the affine class** (A3.1 below; Q-C2-1 `DESIGN-DS.md` §5 finding 1 [D]) |
| R3.7 | phase settings `{0, π}` | EN step, CS supply (phase cell) | available; enough for `V` over two settings |
| R3.8 | splitting ratios other than 50:50, and phase scans beyond `{0, π}` | MC | not available. Native phases are `{0, π}` only, and intermediate strengths occur only as mixtures (`DESIGN-DS.md` §5 findings 3–4 [D]). Not needed for W1 or W2 |
| R3.9 | heralding, by forward conditioning on a registered herald | CS (L-FWD) | available |
| R3.10 | two independent sources and exchange symmetry of excitations (W3 only) | NX | absent: the corpus search found no treatment |
| R3.11 | the validation fields `NCONS`, `NONABS`, `CLICK`, `D`, `K` | method (construction-internal) | definable; `NCONS` is new |

**A3.1 [A]: in the affine class, sub-unity `α` is fixed by the identification.**
- **Setting.**
  - Let the unknown supply bits be uniform on a coset (N2).
  - Let two detector cells register affine functionals `f_A = a·s + c_A` and `f_B = b·s + c_B`, with a click
    meaning value 1.
- **Cases.**
  - If `a` and `b` are linearly independent on the coset, `f_A` and `f_B` are independent and uniform, so `α = 1`.
  - If they are equal and non-constant, then either `f_A = f_B`, giving `α = 2`, or `f_B = f_A + 1`, giving `α = 0`.
  - If either is constant, `α` is 1 or undefined.
- **Consequence.** Under N2 the affine class gives `α ∈ {0, 1, 2}`, and `α = 0` occurs only when one detector
  registers the complement of the other's functional.
  - In the encoded setting this is L-PORT: the two ports are the two values of one bit (`DESIGN-DS.md` §5 finding 5;
    r6 finding 5 [D]).
  - In a spatial setting it means one detector clicks on the absence of the field at its partner's site, which
    contradicts R3.5's click identification.
  - The symmetric spatial ring gives `f_A = f_B` and `α = 2` (Q-C2-1 r6 finding 5 [D]).
- **Therefore.** Exclusivity generated by the dynamics, with each detector reading its own cell's occupation, needs a
  rule outside the affine class that conserves excitation number. A controlled swap (Fredkin-type routing) is the
  minimal example; its non-affinity is Q-C2-1's finding 1 [D].
  - This is a classical reversible rule, a permutation of configurations. It needs no coherent mixing.
  - Non-uniform full-support laws (N2 relaxed) give other values of `α` without changing this conclusion about
    identification.
- **Status.** Unreviewed paper derivation. It concerns the affine class with N2 only.

**A3.2 [A]: a hazard the routing extension brings into QX-0.** A routed excitation has a definite location. A
detector coupled only when its cell is occupied can register the path without acting on the phase bit, which would
give `D = 1` together with `V = 1`. That is P-RECORD-WITHOUT-SUPPRESSION in Q-C2-1's terms.
- In the affine class, complementarity comes from the reciprocal symplectic coupling: the record is written together
  with a kick drawn from the meter's unknown slot (AP1 §3.2 item 1 [W]).
- So any routing extension must keep detector couplings reciprocal, or QX-0's universality reading
  (P-COMPLEMENTARITY over `Adm_B`) can fail.
- That reading is a control the extension must preserve (§A.29; programme rule 1).

**Coherent mixing.** W1 and W2 do not depend on Obligation C or on OICORE-1's drive clause. They need `{0, π}` phases,
a 50:50 split and recombination, all within the stabilizer and classical-reversible class. This matches #1210's note
that QX-3 may remain informative if Obligation C fails. Only R3.8 is MC.

**Corpus search (§A.19).** A search of `papers/*.md`, `book/ch*.md` and `book/appendix*.md` at `fd539e15` for
`antibunch`, `Hanbury`, `g^{(2)}`, `g⁽²⁾`, `single-photon`, `Grangier`, `second-order coherence` and `sub-Poisson`
finds no OI treatment of single-quantum statistics. The hits are:
- GR.md:198, where `G^{(2)}` labels a second menu;
- book/ch15:197-210, a BEC density autocorrelation.

The only OI-specific findings are Q-C2-1's drafts (r6 finding 5; r13 B1 field "`α = 0`, fixed by L-PORT"; NR-13 and
NR-14) [D].

## 4. Reuse of the single shared construction

**Shared with QX-0, QX-1 and QX-2** (same objects, not reconstructed):
- the step;
- N2;
- the SA-1(b) and SA-1(c) supplies and H-PREP;
- P3 arming, or its FIX-compatible replacement (NR-16);
- the phase cell with `{0, π}`;
- the recombiner and screen;
- the held-cell machinery;
- the identifications L-PATH and L-PORT, with their REP-INV status.

The recombine setting of QX-3 is QX-0's off arm.

**Shared with QX-4.**
- The routing rule of R3.6 and the location-reading detectors. QX-4's ideal-negative-measurement control needs the
  same objects (QX-4 §3, R4.9).
- The requirement of A3.2 that detector couplings stay reciprocal.

**Shared with QX-6.** W3 needs two sources and a two-system structure, the same composite objects as QX-6.

**Specific to QX-3:**
- the split/recombine setting;
- the coincidence register (`a`, `b`);
- the herald;
- `NCONS`.

**Flagged experiment-specific assumptions:**
- the click identification (R3.5, IR). It must pass a REP-INV-type test: varying it between occupation reads and
  complementary reads must not change `α`, or it is reclassified as imported and `α` becomes a benchmark value;
- a Fock-1 source law, if used, is IQ and allowed only in the benchmark arm;
- any detector-efficiency or dark-count model must come from the construction (validation layer). A supplied loss
  model is IQ.

## 5. A/B arms and candidate ablations (outline only; not frozen)

**Arms.**
- **`A_3`**, the substratum with the B scaffolding that any detector needs. As in Q-C2-1, no substratum-only
  experiment can be posed: N2, P3, terminal registration and the identifications are needed to have probabilities,
  settings and clicks (`DESIGN-DS.md` §2 [D]). In the spatial ring, the paper expectation is `α = 2` (wave-like).
- **`B_3-enc`**, construction B with encoded ports. The paper expectation is `α = 0` and `V = 1`. This is a
  representation result: `α` is fixed by L-PORT.
- **`B_3-route`**, construction B plus the routing extension (R3.6, NX), with spatial detectors that read their own
  cells' occupation. The paper expectation is `α = 0` and `V = 1`, the behaviour of a classical particle with a phase.
  It is to be checked against A3.2.
- **Comparators** (gating nothing):
  - CF-3: a classical field with square-law detectors, `α ≥ 1`;
  - CP-3: a classical particle with no phase, `α = 0` and `V = 0`;
  - ER-3: the toy field theory, `α = 0` and `V = 1`;
  - QM-3: a Fock-1 source, labelled IQ.

**Candidate ablations.** Each reports three things separately: `pred_change` (do the reachable observables change?),
`mech_change` (do the realizing mechanisms in the validation cells change?) and `access_only` (are the full world
laws identical, with only the registered or unread records differing?). `dynamics_credit` is printed beside them.

| ablation | kind | paper expectation |
| --- | --- | --- |
| ABL-ROUTE: routing removed, affine splitter | dynamics | `pred_change` true (`α`: 0 → 2); `mech_change` true; `access_only` false |
| ABL-CLICK: click identification varied, occupation against complement | representation (REP-INV) | if `α` changes, the identification is imported and `α` is a benchmark value |
| ABL-SA1c: a supply with both slots known | state restriction; credit none | `α` unchanged (location is the known slot); the `V` half and QX-0's complementarity change |
| ABL-SA1b: both slots of each detector registered | access restriction; credit none | `α` unchanged; `access_only` true |
| ABL-HERALD: unheralded against heralded | access (conditioning) | reported; `access_only` true if the world laws are identical |
| ABL-N2: a non-uniform full-support supply | state restriction | `α` takes other values. Exclusivity under routing is unchanged |
| ABL-RECIP: occupation-controlled detectors without the kick | dynamics | expected P-RECORD-WITHOUT-SUPPRESSION on the QX-0 apparatus (A3.2); `pred_change` true |

## 6. Dependence on Q-C2-1's outcomes (decision tree)

Q-C2-1's tokens are taken from preregistration r13: P is decided by `decide-p`, B by `decide-b` and C by `decide-c`.

```
Q-C2-1 P token
├─ P-VOID ─────────────── QX-3 keeps its design; the shared interferometer module is unvalidated.
│                          Hold W2. W1 can be designed alone, at classical-field scope.
├─ P-NO-FRINGES ────────── the recombine half fails; W2 cannot be posed on the shared module.
│                          QX-3 reduces to W1, which classical particle models pass trivially.
├─ P-NO-RECORD ─────────── no effect on α. The validated marker is absent, so A3.2's control has no reference.
├─ P-RECORD-WITHOUT-SUPPRESSION ── SA-1(c) does not carry universality in B. Before the routing extension is
│                          considered, A3.2's hazard already holds, and W2 is unaffected.
└─ P-COMPLEMENTARITY (Level 1) ── the module is validated. QX-3 reuses it, and A3.2 is a preserved control.
    │
    ├─ REP-INV reclassifies L-PORT as imported ── B_3-enc becomes a benchmark arm. Only B_3-route can be
    │                                              credited.
    └─ C token (bears on QX-3 only through the choice of the shared rule)
        ├─ C-EXPOSURE or C-SIZE-DEPENDENT, with non-affine rule g* ∈ {AND, NAND, OR, NOR}
        │    The shared construction would carry g*. QX-3 must ask whether g* (under FIX) yields
        │    number-conserving routing.
        │      yes → R3.6 is supplied by the shared rule. One extension serves Obligation C and QX-3.
        │      no  → routing is a second extension. It needs separate justification and an evaluation of its
        │            effect on QX-0 and C (programme rule 1).
        ├─ C-NONSTABILIZER ── as above. W1 and W2 are unaffected.
        ├─ C-SURVIVAL ──────── no non-affine rule is selected. Routing becomes the first non-affine extension,
        │                      motivated by number conservation and not by C. QX-3 stays informative at
        │                      classical-field scope.
        └─ C-VOID ──────────── no reading. QX-3's dependency on C is unchanged.
    B token
        ├─ B-CONTEXTUAL on B-P, with an owner-typed Acc ── a candidate extension adds QX-3's coincidence table
        │                      to the same fragment under the same Acc typing. It is not a QX-3 witness.
        └─ B-CLASSICALLY-IMITABLE ── confirms that W2's best case is the epistemically restricted class.
```

## 7. Known feasibility obstacles

1. **L-PORT exclusivity.** In the encoded setting, `α = 0` is fixed by the identification of ports with the two
   values of one bit. Every classical particle model shares it, and it excludes only classical fields (Q-C2-1 r6
   finding 5 [D]; A3.1).
2. **The spatial ring is wave-like.** The affine `F_2` wave copies the field to both detectors, so `α = 2` (Q-C2-1
   [D]).
3. **Dynamical exclusivity needs a non-affine rule.** Number-conserving routing is outside the affine class (A3.1). The
   rule must be part of the one fixed law (FIX, OICORE-1 §2), not a per-tick switch beyond P3.
4. **The routing extension threatens complementarity** unless detector couplings remain reciprocal (A3.2).
5. **Rational probabilities.** N2 gives dyadic rationals. Intermediate `α` values, such as GRA's measured 0.18, arise
   only from non-uniform laws or mixtures. This does not affect W1 or W2.
6. **Loss accounting.** A low `P_AB` with a high `N_0` is a loss artefact. `N_0` and `NONABS` must be reported, and
   loss must come from the construction, not from a supplied efficiency.
7. **The witness class is narrow.** Even the best outcome excludes only classical fields under square-law detection
   (§2). The construction itself remains an epistemically restricted classical model.
8. **W3 needs objects absent from the corpus:** two sources and exchange symmetry (R3.10). Its classical-class
   exclusion beyond classical fields is not established here.

## 8. Mapping to the significance ladder (no level is awarded from a lower one)

- **Level 1.** Phase-dependent interference from the same source (`V > 0` at `{0, π}`), reusing QX-0's Level-1
  condition, together with single-event statistics. It is quantum-compatible behaviour.
- **Level 2.** W2 on `B_3-route`, if the owner accepts the classical-field class (Q3-1). It is printed with the classes
  not excluded (§2). On `B_3-enc` it is a representation result and not creditable, because `α` is fixed by L-PORT.
- **Level 3.** Not addressed. QX-3's operations (`{0, π}` phases, 50:50 split, routing) are stabilizer or classical
  reversible, and no coherent operation of the kind Level 3 concerns is generated. QX-3 does not award Level 3.
- **Level 4.** Contributes compatibility only: the same source, interferometer and detectors serve QX-0, QX-2 and
  QX-3 under one rule.

## 9. Owner questions (neutral; for the shared-mechanism selection)

- **Q3-1.** Does exclusion of classical fields under square-law detection (W1 or W2) qualify as Level 2, or does
  Level 2 for QX-3 require a witness against a wider class? (a) It qualifies, printed with its excluded and
  non-excluded classes. (b) It does not, and QX-3 is reported at Level 1 with W2 as a reported field. (c) W3 is added
  as the Level-2 candidate, after its classical-class status is checked in the literature.
- **Q3-2.** How is the routing extension (R3.6) typed? (a) NX until independently justified. (b) Candidate
  strengthened, if a number-conservation principle is argued from OI's texts.
- **Q3-3.** How is the click identification (R3.5) typed? (a) IR, with a REP-INV test. (b) Merged with L-PORT under
  D18.

## 10. References to content off `main` (§A.42 item 8)

| reference | claim it supports | classification |
| --- | --- | --- |
| Q-C2-1 r6/r13 drafts, `DESIGN-DS.md` §5 findings 1, 3–5 | A3.1's context; the obstacles in §7 | support off `main` (D): a planning input, not an established premise |
| AP1 (`verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`) §3 | A3.2's reciprocity mechanism | on `main` (W), model-reviewed; conditional |
| OICORE-1 r6 §§2, 5(b) | FIX; the noncontextuality of construction B at stabilizer scope | off `main` (D) |
| Catani et al. 2023; Clauser 1974; GRA 1986 | §2 | literature; Catani et al.'s abstract read, the others not read first-hand |
