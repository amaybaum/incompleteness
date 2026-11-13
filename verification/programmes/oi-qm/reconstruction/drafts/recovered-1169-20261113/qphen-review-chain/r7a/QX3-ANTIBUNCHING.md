# QX-3: single-quantum statistics and antibunching — Phase 1 experiment specification (draft r7)

## 0. Standing

- **Authority.** #1210, Phase 1: paper-only design of QX-3, QX-4 and QX-6 (owner authorization recorded in #1210
  c.6736966265, amaybaum, 2026-11-09).
  - Not authorized and not done here: mechanism construction; computation on any proposed OI mechanism; frozen
    acceptance criteria; execution.
  - Exact checks of paper claims on generic mathematical objects are allowed when labelled as such: "Allowed: generic
    checks" (#1210 c.6739250392, owner, 2026-11-09). The checks cited here (probes P1–P6 under `review/probes/`) are
    of that kind, and a result supported only by such a check is marked computation-supported in
    `SHARED-MECHANISM.md` §8.
  - Owner records governing these specifications, quoted where used: the five acceptance criteria (#1210 c.6738145827,
    amaybaum, 2026-11-09T10:48:39Z); the three questions for restrictions and the rule that the Bell lemma is proved
    only once its proof is complete and its assumptions are checked against Main (#1210 c.6738337450, amaybaum,
    2026-11-09T10:58:24Z); decisions O1 and O2 (#1210 c.6738866690, amaybaum, 2026-11-09T11:25:06Z); generic checks
    and O1/O2 confirmed (#1210 c.6739250392, amaybaum, 2026-11-09T11:45:26Z); the r4 requirements on Bell locality
    as a design assumption, counterexample membership and the Leggett–Garg configuration (#1210 c.6739286623,
    amaybaum, 2026-11-09T11:47:25Z); the instruction that every conclusion in a summary or dependency table has the
    same scope and status as its supporting proof or counterexample (#1210 c.6739311717, amaybaum,
    2026-11-09T11:48:47Z); the three distinctions: configuration carriers versus encoded carriers, mathematical
    availability of an operation versus its derivation from OI, and generating coherent mixing versus establishing
    the complete quantum probability and composition rules (#1169 c.6740778880, amaybaum, 2026-11-09T13:05:46Z);
    the direction to "preserve the distinction between necessary physical conditions and assumptions built into the
    design" (#1210 c.6741117489, amaybaum, 2026-11-09T13:22:24Z).
- **Status.** Model-written and paper-only. It adopts no premise, freezes no rule and changes no scientific status
  (§A.45 rule 1). Every rule below is an outline: where a rule is stated, it is a candidate for a later
  preregistration, not a frozen criterion.
- **Revisions.** Earlier texts are kept under `r1/`, `r2/`, `r3/`, `r4/`, `r5/` and `r6/`. The revision record is
  `DISPOSITIONS-r7.md`.
  The reviews and their exact probes are under `review/`.
- **Claim status** of this file's claims (proved, disproved, open) is given in `SHARED-MECHANISM.md` §8, and the
  restrictions it uses in §9.
- **Snapshot.** The corpus is read at `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`. The session drafts
  are read as they stood on 2026-11-09:
  - Q-C2-1 preregistration draft r13 (`fefd3b6e…`), with r12 (`38c27d3a…`) and the text accepted at r11b (`f0436d4a…`);
  - `DESIGN-DS.md` r13 (`fbfbd9fa…`);
  - `DECISIONS.md` (`df4b5d78…`);
  - `oicore/OICORE-1.md` (`9b82ecc2…`). This file carries r6's content; the separately kept `oicore/OICORE-1-r6.md`
    (`ec7966c9…`) differs from it in one table cell, "ε-route" against "Route".
- **Evidence layers** (as in OICORE-1 §0):
  - **K**: kernel;
  - **P**: a paper proof on `main`;
  - **W**: a reconstruction record on `main`, model-reviewed only and never an established premise (§A.46 item 7);
  - **D**: an off-`main` draft or session record;
  - **X**: an exact finite computation on generic mathematical objects, re-runnable from its script under
    `review/probes/` (off `main`) and independently reproduced, at its stated scope (SHARED §8);
  - **A**: a derivation in these files, on paper, unreviewed unless stated;
  - **L**: literature, not read first-hand unless stated.
- **Requirement typing**, with type and dependency kept as separate columns.
  - **Type** (owner, #1169 c.6734304025):
    - **EN**: established native;
    - **CS**: candidate strengthened, with its justification status;
    - **IQ**: imported quantum assumption, allowed only in a labelled benchmark arm;
    - **IR**: imported representation. For path, port, calibration and U′ the owner decided Q-C2-1's D18 as option
      (a), conditional: "Permit explicitly identified representation choices, but verify they introduce no quantum
      dynamics, probabilities, or desired outcomes", recorded with a separate representation ledger (#1169
      c.6735014875, amaybaum, 2026-11-09T07:52:50Z). Identifications outside those four are not covered by that
      decision;
    - **untyped**: a dynamics element not yet typed by anyone, which needs independent justification before it can be
      typed CS.
  - **Dependency:**
    - **MC**: dependent on the missing coherent-mixing mechanism (Q-C2-1 Obligation C, or OICORE-1's drive clause,
      §8.4);
    - **MECH-OPEN**: whether OI's step supplies the element is an open mechanism question, not evaluated here;
    - **—**: none.

***

## 1. The phenomenon and its operational observables

**Phenomenon.** A source emits one excitation per trial. The excitation meets a 50:50 splitter whose two outputs go to
detectors `D_A` and `D_B` (the Hanbury Brown–Twiss arrangement). For a single-quantum source the two detectors do not
fire in the same trial. The same source, sent instead into a two-path interferometer, shows phase-dependent
interference. Grangier, Roger and Aspect combined the two (Europhys. Lett. 1, 173 (1986); L).

**Observer access.** Detector records only. Per trial the observer holds:
- the herald bit `h`, if a herald detector `D_H` is used;
- the setting `s ∈ {split, recombine}`, and in the recombine configuration the phase setting `φ`;
- the click bits `a` and `b` (split), or the port bit `p` (recombine).

No carrier slot, path variable or hidden cell is registered (L-ACC, as in Q-C2-1).

**Full-mass accounting.**
- Every trial is counted, including trials without clicks.
- The only conditioning admitted is on the herald, and only when the herald is registered before the setting is
  applied and its law does not depend on the setting.
- Detection-based postselection is not admitted.

**Observables** (exact rationals in every construction considered):
- `P_A = P(a = 1 | h = 1)`, `P_B` and `P_AB = P(a = 1, b = 1 | h = 1)`;
- `α = P_AB / (P_A P_B)`, Grangier's anticorrelation parameter (the heralded `g⁽²⁾(0)`). Its unheralded form drops `h`;
- `V = |P(p = 0 | φ = 0) − P(p = 0 | φ = π)|` over the two native phase settings;
- `N_0 = P(a = 0, b = 0 | h = 1)`, the heralded no-click mass. A low `P_AB` obtained through missing clicks is a loss
  artefact, not exclusivity;
- an optional extension: Hong–Ou–Mandel coincidence visibility, with two sources and one splitter (§3, R3.10).

**Validation layer.** These fields are computed from the construction. They are never observer data and never an
import of quantum behaviour.
- `NCONS`: whether the splitter dynamics conserves the number of excitations. **Its domain is a declared choice**
  (§3, A3.1):
  - `NCONS_ready`: on the ready support (the supplies the protocol admits);
  - `NCONS_global`: on the whole configuration space of the cells involved.
  Both are reported.
- `NONABS`: no absorption of the excitation before detection.
- `CLICK`: whether each detector's registered functional is the occupation of its own cell. This is the click
  identification, R3.5.
- `D` and `K` for the interferometer arms, as in Q-C2-1.

## 2. QM's predictions and the classical alternatives each witness excludes

**QM's predictions** (comparators only; IQ):
- An ideal one-photon Fock source gives `α = 0` and `N_0 = 0`. Independent detector efficiency `η < 1` leaves
  `α = 0`.
- A Fock-`n` source gives `g⁽²⁾(0) = 1 − 1/n`. A coherent source gives `1`; a thermal source gives `2`.
- In the recombine configuration, the same Fock-1 source gives `V = 1` at `φ ∈ {0, π}`.
- Hong–Ou–Mandel: two indistinguishable single photons on a 50:50 splitter give coincidence probability 0, and fully
  distinguishable photons give `1/2`. The visibility is `1`.

**The witnesses and the classes each excludes.**

| witness | excludes | does not exclude |
| --- | --- | --- |
| **W1**: `α < 1` | classical fields with square-law, independent detection. The Cauchy–Schwarz inequality gives `α ≥ 1` (Clauser, Phys. Rev. D 9, 853 (1974); L) | classical particle models, for which `α = 0` is trivial; classical fields read by non-square-law or correlated detectors; deterministic hidden-variable models, Bohmian ones and OI's configuration model among them |
| **W2**: `α < 1` and `V > 0` on one source preparation, selected by the setting | W1's class, and particle models with no wave-like phase variable | epistemically restricted classical models. The toy field theory of Catani, Leifer, Schmid and Spekkens (Quantum 7, 1119 (2023); abstract read) gives modes an occupation number and a phase, and reproduces Mach–Zehnder interference, the bomb tester, delayed choice and the eraser. Construction B of Q-C2-1 is itself an epistemically restricted classical model, noncontextual at stabilizer scope (`DESIGN-DS.md` §4 [D]; OICORE-1 §5(b) [D]) |
| **W3** (optional): Hong–Ou–Mandel visibility `> 1/2` | classical fields, whose visibility is at most `1/2` (L, standard) | not determined here whether an epistemically restricted discrete model reproduces the full dip. A literature check is needed before W3 is designed |

**Consequence for the ladder.** The strongest classical class QX-3 can exclude is W2's: classical fields under
square-law, independent detection, together with particle models with no wave-like phase variable. It excludes no
epistemically restricted model and no deterministic hidden-variable model, OI's included. Whether this meets the
ladder's Level 2 ("excludes a defined class of classical explanations") is an owner decision (§9, Q3-1).

## 3. What the experiment needs from an OI construction

| # | requirement | type | dependency | status in the current toolkit |
| --- | --- | --- | --- | --- |
| R3.1 | one bijective second-order step on finite cells (L-BIJ, L-SYM) | EN | — | available (Main:44-46, 62) |
| R3.2 | probabilities from configuration counting (N2) | CS (Main's posit (iv) for `H`, not derived; supplied for apparatus cells) | — | available; rational only (dyadic at `q = 2` without conditioning) |
| R3.3 | a single-excitation source: a location-known, phase-unknown cell (`Z±`-type), and its phase-known form (`X±`) for the recombine setting | CS (SA-1(c), H-PREP) | — | available in encoded form (Q-C2-1 P) |
| R3.4 | splitter and recombiner | EN in encoded form (free ticks; affine) | — | encoded: available. Spatial: R3.6 |
| R3.5 | detectors as meter cells with terminal registration, and the click identification "a click is the occupation of the detector's own cell" | CS (SA-1(b)); the click identification is IR | — | meters: available. The click identification (L-CLICK) is **not covered** by the D18 decision, which concerns path, port, calibration and U′; it needs owner typing (Q3-3) |
| R3.6 | **routing**: one excitation reaches exactly one of two spatially separate cells, each read by its own detector as its own occupation, conserving excitation number on the declared `NCONS` domain | untyped (dynamics) | MECH-OPEN | an affine linear map achieves it with `NCONS_ready` (A3.1(b)). Under `NCONS_global` it must be non-affine (A3.1(c)). Whether OI's step supplies either is not evaluated |
| R3.7 | phase settings `{0, π}` | EN step, CS supply (phase cell) | — | available; enough for `V` over two settings |
| R3.8 | splitting ratios other than 50:50, and phase scans beyond `{0, π}` | — | MC | not available. Native phases are `{0, π}` and intermediate strengths are mixtures (`DESIGN-DS.md` §5 findings 3–4 [D]). W1 and W2 do not need it |
| R3.9 | heralding by forward conditioning on a registered herald | CS (L-FWD) | — | available |
| R3.10 | two independent sources and exchange symmetry of excitations (W3 only) | untyped | MECH-OPEN | absent (the corpus search found no treatment) |
| R3.11 | validation fields `NCONS_ready`, `NCONS_global`, `NONABS`, `CLICK`, `D`, `K` | method (construction-internal) | — | definable; the `NCONS` fields are new |

**A3.1 [A, with the reviewer's exact probe P2 (X)]. What the affine class can and cannot do for `α`.**

(a) *Case analysis.*
- Let unknown supply bits be uniform on a coset (N2).
- Let two detector cells register affine functionals `f_A = a·s + c_A` and `f_B = b·s + c_B` of the supply, with a
  click meaning value 1.
- If `a` and `b` are linearly independent on the coset, `α = 1`.
- If they are equal and non-constant, either `f_A = f_B`, giving `α = 2`, or `f_B = f_A + 1`, giving `α = 0`.
- If either is constant, `α` is 1 or undefined.

So `α ∈ {0, 1, 2}`, and `α = 0` holds iff `f_B = f_A + 1` with `f_A` non-constant. P2 confirms this exhaustively over
every coset of `F_2⁴` and every pair of affine functionals (314,368 cases).

The symmetric spatial ring gives `f_A = f_B`, so `α = 2` (Q-C2-1 r6 finding 5 [D]).

(b) *Complementary values need not be an identification artefact.* The functionals are functionals of the whole
supply, the known cells included. Affine dynamics can therefore write complementary values into two separate cells,
each read as its own occupation.
- Example (P2): the linear bijection `L(s, c₁, c₂) = (s, s + c₁, s + c₂)` on the ready support `c₁ = 1`, `c₂ = 0`, with
  `s` uniform. It maps the support to `(0, 1, 0)` and `(1, 0, 1)`.
- One excitation is routed by the unknown bit `s` into field cell `c₁` or field cell `c₂`.
- Own-cell reads give `α = 0`.
- Total weight is conserved on the ready support.
- `L` coincides with the Fredkin gate on the single-excitation sector.

In the encoded setting of Q-C2-1, by contrast, the two ports are the two values of one bit, and `α = 0` is fixed by
the identification L-PORT (r13 B1 field [D]).

(c) *Global conservation forces non-affinity.* Weight here counts every coordinate, the control `s` included. Let
`T(y) = My + b` be an affine bijection of `F_2ⁿ` that preserves Hamming weight everywhere.
- `T(0) = b` has weight 0, so `b = 0`.
- Each `M e_i` has weight 1, and `M` is invertible, so `M` is a permutation matrix.

So the globally weight-preserving affine bijections are exactly the coordinate permutations. P2 counts 6 of them on
`F_2³`, all permutations. Permutations transport exclusivity but cannot generate it: they cannot route an excitation
according to an unknown bit. Under `NCONS_global`, routing is non-affine; the Fredkin gate is the minimal example.
P2 counts 48 affine bijections of `F_2³` that route on the ready support as `L` does.

The conclusion is the same if only the field cells' weight counts. An affine map's field part is `Mc + us + b`. If it
preserves the field weight for both values of `s`, then `us + b = 0` for both, and `M` is the identity or the swap,
the same for both values of `s`; so it cannot route. Exhaustively, the 64 bijections of `F_2³` that preserve field
weight everywhere and route on the ready support are all non-affine (reviewer probe `p6_r3rev_qx3.py` (c);
computation-supported).

(d) *Which domain applies is a declared choice, not a derived one.*
- `NCONS_ready` is a property of the protocol's admitted supplies.
- `NCONS_global` makes number conservation a property of the law.

QX-3 reports both, and the owner decides which one a W2 credit requires (Q3-2). Non-affine dynamics is therefore not
established as necessary for antibunching: a router must be non-affine under `NCONS_global` and need not be under
`NCONS_ready`. Which additional physical constraints, if any, make non-affinity necessary is open. No principle of OI with a reason independent of
QM is identified that requires `NCONS_global` (SHARED §9). Whether OI's step (the second-order
symplectic rule, with P3 arming) admits an `L`-type map, or a non-affine routing map, is a mechanism question and is
not evaluated here (MECH-OPEN).

*Scope.* Affine dynamics with N2 only. Non-uniform full-support laws (N2 relaxed) give other values of `α` without
changing (b)–(d).

**A3.2 [A]. A hazard any routing map brings into QX-0, already present as the copy-only case.** A detector that
copies its cell's occupation without a reciprocal back-coupling records the path without acting on the phase, which
gives `D = 1` together with `V = 1`: P-RECORD-WITHOUT-SUPPRESSION.
- This is the existing copy-only hazard: `DESIGN-DS.md` §5 finding 9 and ablation ABL-RECIP [D]. In the affine class,
  complementarity comes from the reciprocal symplectic coupling, which writes the record together with a kick from
  the meter's unknown slot (AP1 §3.2 item 1 [W]).
- Routing matters to it only because a routing rule outside the affine-symplectic class need not be symplectic or
  reciprocal. `G_SM`'s edges are not reciprocal for `L ≥ 5` (M2D §0 item 1 [W]).
- So any routing map adopted into the shared construction carries reciprocity of detector couplings as a control
  preserving QX-0's universality reading (§A.29; programme rule 1).

**Coherent mixing.** W1 and W2 do not depend on Obligation C or on OICORE-1's drive clause. They need `{0, π}` phases,
a 50:50 split and recombination, and routing (R3.6). All of these lie in the stabilizer-and-classical-reversible
class. Only R3.8 is MC.

**Corpus search (§A.19).** A search of `papers/*.md`, `book/ch*.md` and `book/appendix*.md` at `fd539e15` for
`antibunch`, `Hanbury`, `g^{(2)}`, `g⁽²⁾`, `single-photon`, `Grangier`, `second-order coherence` and `sub-Poisson`
finds no OI treatment of single-quantum statistics.
- The hits are GR.md:198 (`G^{(2)}` labels a second menu) and book/ch15:197-210 (a BEC density autocorrelation).
- The OI-specific findings are in Q-C2-1's drafts only [D]: r6 finding 5; r13's B1 field "`α = 0`, fixed by L-PORT";
  NR-13, the spatial `F_2` ring double slit; NR-14, a native two-detector screen with measured anticorrelation.

## 4. Reuse of the single shared construction

**Shared with QX-0, QX-1 and QX-2.** These are the same objects, not reconstructed:
- the step, N2, the SA-1(b) and SA-1(c) supplies, and H-PREP;
- P3 arming, or its FIX-compatible replacement (NR-16);
- the phase cell with `{0, π}`;
- the recombiner and screen, and the held-cell machinery;
- L-PATH and L-PORT, with their D18 ledger and REP-INV status.

The recombine setting of QX-3 is QX-0's off arm.

**Shared with QX-4.**
- The routing map of R3.6 and the location-reading detectors. QX-4's ideal-negative-measurement variant needs the
  same objects (QX-4 R4.9).
- A3.2's reciprocity control.

**Shared with QX-6.** W3 needs two sources and a two-system structure, the same composite objects as QX-6.

**Specific to QX-3.** The split/recombine setting, the coincidence register (`a`, `b`), the herald, and the `NCONS`
fields.

**Flagged experiment-specific assumptions.**
- The click identification (R3.5, IR) needs owner typing (Q3-3) and a REP-INV-type test. If varying it between
  occupation reads and complementary reads changes `α`, it is imported and `α` becomes a benchmark value.
- A Fock-1 source law, if used, is IQ and appears only in the benchmark arm.
- Detector efficiency and dark counts come from the construction (validation layer). A supplied loss model is IQ.

## 5. A/B arms and candidate ablations (outline only; not frozen)

**Arms.**
- **`A_3`**: the substratum with the B scaffolding any detector needs. As in Q-C2-1, no substratum-only arm can be
  posed: N2, P3, terminal registration and the identifications are needed for probabilities, settings and clicks
  (`DESIGN-DS.md` §2 [D]). In the symmetric spatial ring the paper expectation is `α = 2`.
- **`B_3-enc`**: construction B with encoded ports. Paper expectation `α = 0`, `V = 1`. This is a representation
  result: `α` is fixed by L-PORT.
- **`B_3-route`**: construction B with a routing map (R3.6) and spatial detectors reading their own cells' occupation.
  Paper expectation `α = 0`, `V = 1`: classical-particle-with-phase behaviour. It is reported with `NCONS_ready`,
  `NCONS_global` and A3.2's control.
- **Comparators** (gate nothing):
  - CF-3, a classical field with square-law detectors: `α ≥ 1`;
  - CP-3, a classical particle without phase: `α = 0`, `V = 0`;
  - ER-3, the toy field theory: `α = 0`, `V = 1`;
  - QM-3, a Fock-1 source (IQ).

**Candidate ablations.** Each reports three fields separately:
- `pred_change`: do the reachable observables change?
- `mech_change`: do the realizing mechanisms in the validation cells change?
- `access_only`: are the full world laws identical, with only the registered or unread records differing?

`dynamics_credit` is printed beside them.

| ablation | kind | paper expectation |
| --- | --- | --- |
| ABL-ROUTE: routing replaced by the symmetric splitter (`f_A = f_B`) | dynamics | `pred_change` true (`α` from 0 to 2); `mech_change` true; `access_only` false |
| ABL-NCONS: an affine router (`NCONS_ready` only) against a non-affine router (`NCONS_global`) | dynamics | on the ready support `α` and `V` are expected to agree. The two differ off the support, which is reported |
| ABL-CLICK: click identification varied (occupation against complement) | representation (REP-INV) | if `α` changes, the identification is imported and `α` is a benchmark value |
| ABL-SA1c: a supply with both slots known | state restriction; credit none | `α` unchanged (location is the known slot); the `V` half and QX-0's complementarity change |
| ABL-SA1b: both slots of each detector registered | access restriction; credit none | `α` unchanged; `access_only` true |
| ABL-HERALD: unheralded against heralded | access (conditioning) | reported; `access_only` true if the world laws are identical |
| ABL-N2: a non-uniform full-support supply | state restriction | `α` takes other values; exclusivity under routing on the ready support is unchanged |
| ABL-RECIP: copy-only detectors without the kick | dynamics | P-RECORD-WITHOUT-SUPPRESSION on QX-0's apparatus (A3.2; Q-C2-1 ABL-RECIP); `pred_change` true |

## 6. Dependence on Q-C2-1's outcomes (decision tree)

Tokens are those of Q-C2-1 r13's `decide-p`, `decide-b` and `decide-c` [D].

```
Q-C2-1 P token
├─ P-VOID ─────────────── QX-3 keeps its design; the shared interferometer module is unvalidated.
│                          W2 is held; W1 can be designed alone, at classical-field scope.
├─ P-NO-FRINGES ────────── the recombine half fails, so W2 cannot be posed on the shared module.
│                          QX-3 reduces to W1, which classical particle models pass trivially.
├─ P-NO-RECORD ─────────── no effect on α; the validated marker is absent, so A3.2's control has no reference.
├─ P-RECORD-WITHOUT-SUPPRESSION ── SA-1(c) does not carry universality in B. A3.2's hazard is already realized
│                          before any routing map; W2 is unaffected.
└─ P-COMPLEMENTARITY (Level 1) ── the module is validated; QX-3 reuses it, and A3.2 is a preserved control.
    │
    ├─ D18 ledger / REP-INV reclassifies L-PORT as imported ── B_3-enc is a benchmark arm; only B_3-route is
    │                                              creditable.
    └─ C token (bears on QX-3 only through the choice of the shared rule)
        ├─ C-EXPOSURE or C-SIZE-DEPENDENT, non-affine g* ∈ {AND, NAND, OR, NOR}
        │    The shared construction would carry g*. Under NCONS_global, ask whether g* (under FIX)
        │    supplies routing (MECH-OPEN):
        │      yes → one rule serves Obligation C and QX-3.
        │      no  → routing is a separate element, justified and evaluated against QX-0 (programme rule 1).
        │    Under NCONS_ready, an affine routing map may suffice (A3.1(b)); whether the step supplies it is
        │    MECH-OPEN.
        ├─ C-NONSTABILIZER ── as above; W1 and W2 unaffected.
        ├─ C-SURVIVAL ──────── no non-affine rule is selected. Routing is affine (NCONS_ready) or the first
        │                      non-affine element (NCONS_global). QX-3 stays informative at W2's scope (§2).
        └─ C-VOID ──────────── no reading.
    B token
        ├─ B-CONTEXTUAL on B-P (Acc typed CS by D15(a)) ── a candidate extension adds QX-3's coincidence table to
        │                      a fragment under the same typing. This is not a QX-3 witness.
        └─ B-CLASSICALLY-IMITABLE ── confirms that W2's best case is the epistemically restricted class.
```

## 7. Known feasibility obstacles

1. **L-PORT exclusivity.** In the encoded setting `α = 0` is fixed by identifying the ports with the two values of
   one bit. Every classical particle model shares this, and it excludes only classical fields (Q-C2-1 r6 finding 5
   [D]; A3.1(a)).
2. **The symmetric spatial ring is wave-like.** The affine `F_2` wave copies the field to both detectors, so `α = 2`
   (Q-C2-1 [D]).
3. **Routing.** Affine routing with own-cell reads exists on the ready support (A3.1(b)). Routing that conserves
   number globally must be non-affine (A3.1(c)). Which conservation domain QX-3 requires is an owner decision (Q3-2).
   Whether OI's step supplies either kind is open. Any routing element must be part of the one fixed law (FIX,
   OICORE-1 §2), not a per-tick switch beyond P3.
4. **Reciprocity.** Copy-only detection already threatens complementarity, and a routing rule outside the
   affine-symplectic class need not be reciprocal (A3.2).
5. **Intermediate `α`.** Under N2 with affine functionals, `α ∈ {0, 1, 2}` (A3.1(a)). Intermediate values, such as
   the 0.18 measured by Grangier, Roger and Aspect, therefore need non-uniform laws, mixtures, or non-affine detector
   functionals. Rationality of the probabilities is not the obstacle: the dyadic law `P_AB = 9/256`, `P_A = 5/8`,
   `P_B = 5/16` (cells `9, 151, 71, 25` out of 256) gives `α = 9/50 = 0.18`. W1 and W2 are unaffected.
6. **Loss accounting.** A low `P_AB` with a high `N_0` is a loss artefact. `N_0` and `NONABS` are reported, and loss
   must come from the construction.
7. **The witness class is narrow.** The best outcome excludes only W2's class: classical fields under square-law,
   independent detection, and particle models with no wave-like phase variable (§2). Construction B remains an
   epistemically restricted classical model.
8. **W3 needs objects absent from the corpus**: two sources and exchange symmetry (R3.10). Its exclusion of any class
   beyond classical fields is not established here.

## 8. Mapping to the significance ladder (no level is awarded from a lower one)

- **Level 1.** Phase-dependent interference from the same source (`V > 0` at `{0, π}`), reusing QX-0's Level-1
  condition, together with single-event statistics. This is quantum-compatible behaviour.
- **Level 2.** W2 on `B_3-route`, if the owner accepts W2's class (Q3-1) and the `NCONS` domain (Q3-2).
  It is printed with the classes it does not exclude (§2). On `B_3-enc` it is a representation result and is not
  creditable.
- **Level 3.** Not addressed. QX-3's operations (`{0, π}` phases, the 50:50 split, routing) are stabilizer or
  classical reversible, and no coherent operation of the kind Level 3 concerns is generated.
- **Level 4.** QX-3 contributes compatibility only: the same source, interferometer and detectors serve QX-0, QX-2
  and QX-3 under one rule.

## 9. Owner questions (neutral)

- **Q3-1.** Does excluding W2's class (classical fields under square-law, independent detection, and particle models
  with no wave-like phase variable; §2) qualify as Level 2?
  - (a) Yes, printed with its excluded and non-excluded classes.
  - (b) No: Level 1, with W2 as a reported field.
  - (c) W3 is added as the Level-2 candidate, after a literature check of its classical-class status.
- **Q3-2.** Which conservation domain does W2's credit require?
  - (a) `NCONS_ready`: affine routing admissible.
  - (b) `NCONS_global`: non-affine routing required.
  - (c) Both, reported, with no credit difference.
- **Q3-3.** How is the click identification (R3.5) typed? It is outside the D18 decision's four mappings.
  - (a) IR under the D18 condition, entered in the representation ledger with a REP-INV test.
  - (b) A separate owner decision.

## 10. References to content off `main` (§A.42 item 8), traced one by one

| reference | claim it is attached to | classification |
| --- | --- | --- |
| #1210 c.6736966265 (owner authorization) | §0 scope | provenance (authority); quoted |
| #1169 c.6734304025 (typing; A/B) | §0 type column | owner record of direction; defines the categories; quoted |
| #1169 c.6735014875 (D18(a), conditional) | §0 IR; R3.5; Q3-3 | owner decision; quoted with author and time |
| `arp/qc21/DECISIONS.md` (D15, D18 drafts) | §6 (D15(a)); Q3-3 | off `main` (D); provenance for the options; the decisions themselves rest on c.6735014875 |
| Q-C2-1 r13 drafts: `DESIGN-DS.md` §2, §4, §5 findings 1, 3–5, 9; r13 B1 field; ABL-RECIP | A3.1(a) context; A3.2; §5 `A_3`; §7 items 1, 2, 4 | support off `main` (D): a planning input, not an established premise |
| Q-C2-1 NR-13, NR-14, NR-16 (r13 Appendix D.8) | §3 corpus note; §4 | off `main` (D); provenance (named candidate rounds) |
| `review/REVIEW-PHASE1.md` and probe `review/probes/p2_alpha_affine.py` (`312620b0…`) | A3.1(a)–(c): the case count, the map `L`, the counts 48 and 6 | off `main` (D); an exact finite computation on generic `F_2` objects. A3.1(c)'s general statement is proved here (A) |
| AP1 (`verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`) §3.2 | A3.2's reciprocity mechanism | on `main` (W), model-reviewed, conditional |
| M2D (`mechanism-2-20261108/DESIGN.md`) §0 item 1 | A3.2: `G_SM` is non-reciprocal | on `main` (W) |
| `oicore/OICORE-1.md` §§2, 5(b) | FIX; noncontextuality of construction B at stabilizer scope | off `main` (D) |
| writer's probe `review/probes/p5_r3_qx3.py` | A3.1(b)–(c): `L` equals Fredkin on the sector `c₁ + c₂ = 1`; the counts 6 and 48; the 8 globally weight-preserving routing bijections of `F_2³`, none affine | off `main` (D); exact, exhaustive over `F_2³` |
| `review/REVIEW-PHASE1-r3.md` (`448614ea…`); reviewer probe `review/probes/p6_r3rev_qx3.py` | A3.1(c), field-only weight: the 64 routing bijections, none affine; reproduction of A3.1(a)–(c) | off `main` (D); exact, exhaustive over `F_2³` and `F_2⁴` |
| #1210 c.6738145827, c.6738337450, c.6738866690, c.6739250392, c.6739286623, c.6739311717, c.6741117489; #1169 c.6740778880 (amaybaum, 2026-11-09) | §0 | owner records; quoted with author and time |
| Catani et al. 2023; Clauser 1974; GRA 1986 | §2 | literature. The Catani et al. abstract was read; the others were not read first-hand |
