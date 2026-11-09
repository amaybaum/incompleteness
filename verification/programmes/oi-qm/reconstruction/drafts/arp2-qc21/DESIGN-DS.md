# ARP-2 (Q-C2-1) r13: the double-slit model, constructions A and B, and what each test can state

**Status.** WIP / UNVERIFIED design note for preregistration draft r13. Model-written. r13 changes only the QM-P
comparison of finding 6 (the slot map and the QM counterpart of each arm; preregistration *Test B*, r13 item 12). r12 is
kept as `r12/DESIGN-DS-r12.md`.

From r11:
- REP-INV's frame transport (`S P S⁻¹`) and its stated scope (re-review R10-B3, R10-B4);
- the UPR-BC test for L-UPRIME;
- the modelling note on registration (r10-N2).

The execution design (D12 waived, c.6735159962) is in the preregistration only. r10 is kept as
`r10/DESIGN-DS-r10.md`.

From r10:

r10 records the owner's freeze decisions (#1169 c.6735014875) and adds three things:
- the representation ledger (prereg *The representation ledger*);
- the attribution field `ATTR`;
- the three A/B report fields.

**r12.** The proof reviews are recorded in prereg *Proof reviews*. Lemma P: PROVED, conditional on Theorem C(ii) and the
link hypotheses L1–L3. The cone argument: PROVED UNDER STATED EXTRA HYPOTHESES (STAB). r11b is kept as
`r11b/DESIGN-DS-r11b.md`.

From r10: Lemma P and the cone argument were sent for independent review (owner, c.6735014875). r9a is kept as `r9a/DESIGN-DS-r9a.md`.

Earlier status: r9 applies the r8 re-review
(`review/REVIEW-QC21-r8.md`, `32bec1f0…`, REVISE (minor), with the design-level fixed point reached). It makes only the
edits listed in PLAN §12. r8 is kept as `r8/DESIGN-DS-r8.md`.
- **Review history.** r6 was reviewed REVISE (`review/REVIEW-QC21-r6.md`, `facdd215…`). r7 (`r7/DESIGN-DS-r7.md`,
  `eea5553b…`) was re-reviewed REVISE (`review/REVIEW-QC21-r7.md`, `a9488c6f…`; R7-B1–B5, r7-N1–N6). r8 applies the
  re-review (PLAN §11). r8 has not been re-reviewed.
- **Method.** Paper only, plus exact toy probes on paper-sized examples (§10; controls, not evidence). No test rule's
  orbit was evaluated, and no B fragment built from OI data.
- **Snapshot.** `main@fd539e150759a6ea51ab279aeeac80fc06050ade`.

**Terminology (owner, #1169 c.6734304025).** Designs no longer say "native OI dynamics". They use the owner's phrase:
"OI substratum plus independently justified observational-incompleteness principles, with every additional assumption
identified and tested separately". **Construction A** is the deterministic substratum alone: one fixed bijective rule
on finite cells. **Construction B** is A plus the named observational-incompleteness principles of §2, each typed as
established native, candidate strengthened (with its justification status) or imported. Imported quantum structure
appears only in labelled controls and comparators, never in A or B.

**Central question (owner, c.6733711272).** "Can OI's own hidden dynamics generate quantum-specific operational behavior
that an observer detects indirectly, without importing the quantum mechanism being investigated?"

***

## 1. Structure and the two layers

| item | question | decided from | maps to |
| --- | --- | --- | --- |
| **P** (primary) | the owner's question (c.6733825267), restated as class-level complementarity: does the marker record and suppress, and over construction B's admissible arms does every recording arm also disturb and suppress? | screen statistics (observer layer); `D`, `K` and the admissible class (validation layer) | Level 1 at most |
| **B** (secondary) | Does the detector-record table of P's setup admit a noncontextual model over the fragment's own operational equivalences, and is the access class that makes it fail an owner-typed principle? | detector-record tables; the access class `Acc` | Level 2, only with P, on P's setup |
| **C** (secondary; obligation) | Does a non-affine bounded gadget on a two-cell encoded carrier, composed with itself, act on detector records as an operation outside the Clifford class? | detector-record tables | Level 3, only with Levels 1–2 |

Each test reports constructions A and B and the per-principle ablations (§8), with the owner's three cases: both
succeed; A fails and B succeeds; B fails.

**The observer layer.** The detector records the modelled observer holds: the screen port; marker-detector outcomes
(the eraser, B); coincidences; conditioning on recorded outcomes. Every OI detector is a meter cell that copies a
functional of what it couples to, and is then registered (AP1 SA-1). So "indirect" here means **through registered
detector cells**, never by registering a carrier, path or hidden slot. It does not mean "through interference statistics
only". Marker reads, coincidences and the eraser are admitted under every option (c.6733711272 item 3; c.6733796760
element 3; D8(a)). D16 concerns only C's end-of-run meters that copy a carrier functional without recombination. The
screen itself is such a meter after recombination.

**The validation layer.** Properties of the apparatus computed from the construction by the round's controls, never
observer data: `D` over all held unregistered cells, the kick law `K`, NONABS, SPI, COMP, TOMO.

**Identifiability: what P can and cannot state (finding; reviews B1 and R7-B1).**
- **Screen statistics depend only on the arm's system-level channel.** In construction B that channel is the kernel
  `K` of the encoded `x`; in QM and in classical waves it is the reduced channel on the path. A record-free arm with the
  same channel suppresses identically. **No single suppression can be attributed to recording rather than disturbance,
  in any theory**: dephasing is an equally valid explanation of each.
- **Every recording comes with a kick in construction B.** Under SA-1(c), every fresh cell that records the path
  (`D = 1`) has its other slot unknown, and that unknown is a uniform kick. All nine single-cell supplies are enumerated
  (§10).
- **"A path-correlated record or not" is relative to access** (re-review r7-N3).
  - In QM, purified dephasing (environment `|+⟩`, CZ) leaves a record in the environment's conjugate basis (`D = 1`).
    Only the mixed environment of classical noise has `D = 0` (`review/probes-r7/qm_sham_frame.py`).
  - In construction B, the dephasing arm's `D = 0` holds only because its second slot `w′` is unknown under N2. In the
    substratum, the bijection and RET-w keep everything.
- **What P can state.**
  - Fringes with the detector off.
  - A validated path record in the on arm (`D`) and the disturbance it induces (`K`).
  - **The class-level relation**: over construction B's admissible arms, every arm that records also disturbs and
    suppresses. This is complementarity, and it is the token.
  - That the record is erasable by conditioning on the held cells.
- An observer who reads the marker (M2 under `Z±`) sees `D`.
- This is the standard complementarity and decoherence equivalence at the level of dilations (Englert, Scully and
  Walther; Storey et al.; not read first-hand). The finding concerns what the round may state, not a defect of the
  model.

***

## 2. Construction A, construction B, and the typing

"A" marks the substratum. The typing is the reviewer's proposal; the owner decides it (D18 for the identifications).

| ingredient | ledger id | A or B | three-way type | justification status | kind (for ablations) |
| --- | --- | --- | --- | --- | --- |
| bijective second-order step, symmetric class-N coupling, free tick | L-BIJ, L-SYM, L-SYMP, A4 | **A** | established native | Main:44-46, 62; AP1 §4.1 | dynamics |
| `q = 2`; affine update | L-Q2, L-AFF | A (rule choice) | established native for the reference branch; L-AFF partly derived | r5 ADA | dynamics |
| uniform law on unknown slots and hidden cells (N2) | L-N2 | B | candidate strengthened | "native measure, applied through H-PREP" (QA:777); close to native for Main's hidden sector `H`, supplied for apparatus cells | state restriction (measure) |
| half-known ready cells, SA-1(c) | L-P2 | B | candidate strengthened | **posited, not derived** ("new physical posit", AP1 §3.1; AP1:347) | state restriction |
| known value 1; QA family as preparations (H-PREP) | L-HPREP | B | candidate strengthened | open hypothesis | state restriction (supply) |
| terminal registration, SA-1(b) | L-REG, L-P1 | B | candidate strengthened | OICORE-1 RET-s: an imported idealization below recurrence | access restriction |
| per-tick, per-edge arming (P3) and isolation (E-iso) | L-ARM | B | candidate strengthened, in tension with FIX | "per-tick, per-edge arming is not native" (AP1:288-296); E-iso "is not derived" (AP1:305-309) | **dynamics (control of couplings)**: it changes which step applies per tick, and the detector switch is a P3 switch; credited with a different mechanism (re-review R7-B2) |
| held, unread marker | L-HOLD | retention is A; holding it decoupled and unread is B | retention: established native (RET-w); unread and isolated: candidate strengthened | OICORE-1 §2 | access restriction |
| hidden-sector cell (both slots unknown) | L-N2 (environment) | B | candidate strengthened | an N2 environment supply; its link to Main's `H` is plausible, not stated | state restriction |
| observer interface restriction (no carrier slot registered) | L-ACC | B | candidate strengthened | ACC-R2-type; OICORE-1 types ACC_op as CX† with consistency with the core open | access restriction |
| forward conditioning; refilled mediators | L-FWD, L-REFILL | B | candidate strengthened | access convention; supply | access restriction; supply |
| NNB coupling for `Λ_{y,b}` | L-NNB | B | supplied conditional premise | QA node 8 | dynamics (an added coupling) |
| path = encoded `z`; ports = values of one bit; frame calibration; U′ functionals | L-PATH, L-PORT, L-CAL, L-UPRIME | neither | **imported representation**: identifications, not OI principles and not quantum structure | the owner types them (D18) | — |
| Englert bound; the Clifford class; QM-P; supplied gates | E-COMPL, C-class, controls | — | imported quantum structure, confined to comparators and controls | — | — |
| non-affine rule `g` in C's gadget | L-AFF removed | **a change of dynamics**, not a principle | — | — | dynamics |

**Crediting rule (owner, c.6734374076).** Every ablation reports three fields:
- **`pred_change`** (computed): whether the reachable observables change.
- **`mech_change`** (computed): the validation cells `(V, D, K)` whose set of realizing mechanisms changes. The frozen
  grain is supply × coupling type (re-review r8-N4).
- **`dynamics_credit`** (the row's kind): a state or access restriction is never credited with new dynamics.

**Construction A cannot be "the substratum alone" for P** (finding; re-review R7-B2).
- Without N2 there are no probabilities.
- Without P3 arming and E-iso there is no detector switch: under FIX the coupling is fixed and translation-invariant,
  so the off arm does not exist.
- Without H-PREP there is no `X−` and no `φ = π`.
- Without L-PATH and L-PORT there is no path and no port.

The A that can be posed is `A_P` = construction B minus SA-1(c). The shared scaffolding it keeps is untested in this
round: P3, E-iso, N2, H-PREP, the terminal screen registration, L-PATH and L-PORT. P under FIX is NR-16.

***

## 3. The model of P

The step on armed edges is `u_i' = Σ_{j armed with i} u_j + v_i`, `v_i' = u_i`. An unarmed cell swaps its slots. Every
supplied cell is stated at its coupling tick. The encoded frame is `(z, x) = (u, v)` at even ticks and `(v, u)` at odd
ticks (AP1 §4.2).

| element | realization | A/B |
| --- | --- | --- |
| two alternatives | the two values of the carrier cell's `z` (L-PATH) | identification |
| coherent source `X±` | carrier with `x` known, `z` unknown | B (SA-1(c), N2, H-PREP) |
| single-path sources `Z±` | carrier with `z` known, `x` unknown | B |
| probabilities | configuration counting under N2; no amplitude, Born rule or comparator | B (N2) on A |
| phase | at `t = 0`, coupling to a phase cell `(φ, ·)`. It adds the known bit `φ` to `x`: the toy analogue of `Z^φ`, a deterministic flip. **Two settings, `{0, π}`** | A step; B supply and arming |
| propagation | `t = 1`, a free tick | A |
| arm tick | `t = 2`, the carrier coupled to one fresh arm cell, or the edge unarmed | A step; B arming |
| screen | `t = 3`, an X read by a screen cell `(w_s, 0)`; its `u` slot is registered as the port | A step; B registration and supply |
| held cells | the arm cell and the phase cell, decoupled and unread in P | A retention; B isolation and access |

**Arms** (same source, phase cell, schedule, screen and cell count throughout):

| arm | arm cell at `t = 2` | coupling | carrier effect | record |
| --- | --- | --- | --- | --- |
| off | `(w, 0)` | unarmed | free tick | none |
| on (marker) | `(w, 0)` | armed | `x ↦ x + w` (uniform kick) | `z` in the arm cell |
| SH-0, coupling-matched null sham | `(0, w′)` | armed | `x ↦ x` (**identical to the free tick**; it is the phase cell at `φ = 0`) | `z + w′`, masked |
| SH-K = dephasing, disturbance-matched | `(w, w′)`, a hidden-sector cell, outside SA-1(c) | armed | `x ↦ x + w` (uniform kick, the same `K` as the marker) | the noise value `w` is held (a physical trace); no path-correlated record (`D = 0`) |

In construction B, the disturbance-matched sham and the dephasing control are the same supply. Both shams are reported
as a decomposition and gate nothing (D14(d), drafted). D14's gating options would let the choice fix the token (PLAN
D14).

**`Adm_A` and `Adm_B` are generated by rule from the frozen alphabet `Σ`** (re-review r8-N3). `Σ` contains the
slot-wise cells `(a, b)` with `a, b ∈ {0, 1, w}`, plus the `u + v`-known cells `(w, w)` and `(w, w + 1)`.
- **`Adm_B`**: off; every cell of `Σ` with exactly one slot known and the other an independent unknown (the four ready
  cells); and the N2 environment cell. Each is coupled reciprocally.
  - The `u + v`-known cells are excluded, by SA-1(c)'s "its other slot is unknown" and by AP1's type grading. They also
    record and suppress (`review/probes-r8/adm_closure.py`), so the outcome is unaffected.
- **`Adm_A`** (`A_P`): off and every cell of `Σ`, with B's scaffolding kept.

## 4. Quantities, references and the paper expectation

Observer layer, exact:
- `s(arm, src, φ) = P(port 0)`;
- `V(arm) = |s(arm, X+, 0) − s(arm, X+, 1)|`, over two settings;
- `Δ(arm, φ) = s(arm, X+, φ) − ½(s(arm, Z+, φ) + s(arm, Z−, φ))`.

**Eraser (required; owner element 3).** For each arm and each slot of the held arm cell, the screen is sorted by that
slot's value. The conditional visibilities are computed over both phases, together with the unsorted `V`.

Validation layer:
- `D(arm)`: total variation over the joint law of **all** held, unregistered cells, given `Z+` against `Z−`, maximized
  over phases. The phase cell's `D` is reported separately (review N5).
- `K(arm)`: the **transition kernel** of the encoded `x` across `t = 2`, the law of `x_after` given `x_before`, from
  `X+` and `X−` at both phases (re-review R7-B4). It is the identity for off and SH-0 and uniformizing for on and SH-K. A
  reset (PL-SPI) gives the constant kernel. The r7 definition, the law of `Δx`, gave PL-SPI `δ0`, the same as off.
- NONABS and SPI. SPI is non-discriminating in construction B, since under `Z±` `x` is uniform whatever the arm; it gets
  teeth from PL-SPI (review N4).
- The shams' validity flags (`D(SH-0) = 0`, `D(SH-K) = 0`, `K(SH-K) = K(on)`): reported in the decomposition. They
  gate nothing.
- `CPL = V(on)² + D(on)²`. This is an imported comparator, Englert's bound, applied to a classical total variation.
  Under SA-1(c) it cannot exceed 1, so it is unreachable in construction B (review N6).

| arm | QM reference | classical-wave reference | construction B (paper; AP1 §4.5; probe `probes-r8/p_native.py`) |
| --- | --- | --- | --- |
| off | `V=1, D=0`; port `= x + φ` | same | `V=1, D=0, K` = identity |
| on | `V=0, D=1`; eraser: sorted by the conjugate record, conditional `V=1`; sorted by the path record, `0` | same (polarization marker; diagonal analyser) | `V=0, D=1, K` uniformizing; eraser: kick slot `1, 1`, record slot `0, 0`, unsorted `0` |
| SH-0 | `V=1, D=0` | same (the same rotation on both arms) | `V=1, D=0, K` = identity |
| SH-K / dephasing | `V=0, D=0`; sorting by the recorded noise value gives conditional `V=1` | same (a recorded random `0/π` phase) | `V=0, D=0, K` uniformizing; eraser: noise slot `1, 1`, other slot `0, 0`, unsorted `0` |
| single-path | `s=½` | same | `s=½` |

Tolerances are exact. Three facts follow on paper:
- **P excludes no classical explanation.** The table has classical models: the classical wave, and construction B
  itself, an epistemically restricted classical model. The latter is noncontextual at stabilizer scope (OICORE-1 §5(b);
  AP1 §0; Catani, Leifer, Schmid and Spekkens 2023, not read first-hand).
- **The eraser does not separate recording from dephasing.** The marker's and the dephasing arm's eraser tables are
  equal up to which slot carries `z`.
- **P's paper expectation, disclosed (owner element 6; §A.23 consistency axis).**
  - The token is P-COMPLEMENTARITY, under every D14 option, since the shams gate nothing (D14(d) drafted).
  - **A/B existence**: both succeed. The `(w, 0)` marker is admissible in `A_P` and in B, so observational
    incompleteness is not necessary for the transition's existence.
  - **A/B universality**: `A_P` fails and B succeeds. `A_P` admits four sharp supplies that record without
    suppressing. This is carried by SA-1(c), a posit that is not derived: the owner's case "A fails and B succeeds",
    which "would still need to determine whether the relevant conditions are genuinely implied by OI".
  - The decomposition: the coupling alone does not suppress (SH-0); the disturbance alone does (SH-K).

## 5. Feasibility findings (paper unless marked; none adopted)

1. **Two alternatives.** A spatially routed single excitation needs a controlled swap, which is not affine over `F_2`.
   A spatial ring version is a classical `F_2` wave (anticorrelation `α = 2`).
2. **Probabilities** are N2 configuration counts.
3. **Phase.** It takes two settings, the deterministic flips `φ ∈ {0, π}`. Quarter phases need U′ with NNB (AP1 Lemma 5,
   type grading). Owner element 2 is met minimally (review B2).
4. **Marker strength.** `V, D ∈ {0, 1}` in B: the laws given `Z±` are translates of one coset. Intermediate values arise
   only as mixtures on `V + D = 1`.
5. **Anticorrelation** is fixed by L-PORT and does not discriminate.
6. **B's contextuality is relative to the fragment (review B3).**
   - A classical two-bit register read one bit at a time violates preparation noncontextuality over its own equivalence
     (`review/probes-r6/b_incomplete.py`: parity-oblivious multiplexing success 1 against 3/4). This is the `(1, 1)`
     point of the writer's own `pusey_probe`.
   - Every OI table comes from a configuration model. By Lemma NC-F, every B-CONTEXTUAL on OI data is a degenerate
     pairing on the configurations: contextuality relative to reads that do not span them.
   - B's honest scope is therefore "no noncontextual model over the fragment's own equivalences".
   - Its significance depends on whether the restriction producing the degeneracy is an owner-typed OI principle (D15),
     a chosen read set, or an imported identification (L-UPRIME).
   - With complete access, the reads span. Lemma NC-F needs `d = r_S = r_E`, and the preparation side need not span:
     B-P has `r_S ≤ 32` against up to `2⁸` charged configurations. So construction A's B result is measured, not
     predicted (re-review R7-B3; r7's "imitable by Lemma NC-F" is withdrawn).
   - B's LP reads its whole owner-typed `Acc`, nine measurement settings for B-P, justified by SA-1(b) and AP1's type
     grading. A B-REG-type artefact inside `Acc` is therefore excluded.
   - Under D15(a) no setting reads both slots of one held cell, so `Acc` spans at most 18 of the 32 functions on the
     five read slots, and is not tomographically complete for them. A B-CONTEXTUAL is then relative to SA-1(b)'s
     one-functional-per-cell restriction.
   - TOMO, as frozen (`d = r_S = r_E`), is red when `r_S > r_E` or the pairing is degenerate. Which of these holds for
     B-P is not computed before `F` (re-review r8-N6, in corrected form).
   - B-P's comparison with QM-P is restricted to the `p`-free settings M00, M10 and M20, since QM-P has no phase
     register (re-review R8-B1, fix 2).
   - On those settings the slots are read at registration, after `t = 3`. For a coupled arm cell supplied as
     `(u_a, v_a)`, slot 0 holds `u_a` (the kick) and slot 1 holds `z + v_a`, and the port follows `x + φ + u_a`.
     Under the map slot 0 ↔ a CNOT marker's `X` readout and slot 1 ↔ its `Z` readout (fixed by the on arm), with the
     marker prepared in `|0⟩` (on), `|+⟩` (SH-0) and the maximally mixed state (SH-K), and no coupling for off, the
     two tables agree column by column for all four arms (QM side: `probes-r13/qmp_marker.py`, exact). A
     classical-noise `Z^w` arm with `w` held in the `Z` basis is not SH-K's counterpart under this map. Whether the
     comparison uses this map and these arms is the preregistration's owner decision D22, not adopted here.
7. **The triangle cannot host P** under `XOR` (`probes-r6/tri_affine.py`).
8. **Dephasing** is the native step with a supplied N2 environment cell, both slots unknown and outside SA-1(c) (review
   N12).
9. **A record without suppression** needs a P2 departure, or a non-reciprocal copy (AP1 C3; probe: `V = 1`, `D = 1`).
10. **Record and kick are confounded in construction B** (§1; review B1). This is the identifiability limit made
    concrete.
11. **The eraser is not a discriminator here** (§4; review B5).
12. **No substratum-only P** (§2; re-review R7-B2). P3 arming is the detector switch and is a dynamics row.
13. **Both A/B readings** (§4): existence, both succeed; universality, `A_P` fails and B succeeds (SA-1(c)). Beyond
    single cells, `D = 1 ⇒ V = 0` for every SA-1 protocol is AP1 Lemma 3 [W], a paper extension, labelled (re-review
    r7-N6).

## 6. The model of C

- **Setup.** r5's gadget acts on a two-cell encoded carrier (U′, cells 0–1 of the triangle `Z_3`), on the seven QA
  source states. It is not P's apparatus: it has no screen, phase cell or marker (review B4). It is composed `j = 0 … K`
  times, `K ∈ {6, 12}`, with a fresh mediator each time.
- **Detectors.** `S_Z`, `S_X` and `S_Y` read `f_z`, `f_x` and `f_y`, the U′ functionals. **L-UPRIME is therefore used**
  in C and B-C: the detector set is U′'s functionals (review B7). Meters on cell 1 exist and could extend the set (D15).
  The detectors use the native rule in every arm (L-HET, D5).
- **Constructions.**
  - **C-A** is the rounds with `reg = none`: no record-dependent access.
  - **C-B** adds forward conditioning on terminal heralds and refilled mediators.
  - The affine/non-affine comparison (ABL) is labelled a **change of dynamics**, not a principle ablation.
  - The `reg = none` ablation on the same `(g, m, k)` is reported for every flagged instance (review N10).
- **Witness W-CL.**
  - It is computed on both the fixed-slot linear part `β` and the encoded `P^k β` (`P` the transposition `x ↔ z`, `k`
    the round's ticks). It fires if either fires. This is sound because `P ∈ O_h`, and both spectra are reported.
  - It is invariant under linear recalibration, not "frame-free" (review B6).
- **Lemma CL (paper).** For a linear part in `conv(O_h)`, the unit-modulus eigenvalues form a sub-multiset of one signed
  permutation's spectrum. Proof: strict convexity of the Euclidean ball.
- **Lemma P (independently reviewed: PROVED, conditional on Theorem C(ii) and the link hypotheses L1–L3;
  `review/proofs/REVIEW-LEMMA-P.md`; the complete proof is there).** Every affine self-map `Φ` of the octahedron `O` has unit-modulus
  spectrum (of its linear part, with multiplicity) contained in some signed-permutation spectrum.
  1. *Power-boundedness.* `Φ^n(O) ⊆ O`, and `O` is bounded and full-dimensional, so the linear parts `β^n` are bounded.
  2. *Semisimplicity.* A power-bounded matrix has no Jordan block at a unit-modulus eigenvalue. So the unit-modulus
     spectrum of `β`, with multiplicity, equals the spectrum of `β` restricted to its peripheral spectral subspace,
     which is the range of the limit projection below (re-review r7-N5).
  3. *The limit idempotent.* Along a subsequence on which the unit-modulus phases tend to 1 (compactness of the torus),
     `Φ^{n_k} → Ψ`. `Ψ` is affine and idempotent, and `ΦΨ = ΨΦ`. `Φ` maps the polytope `Ψ(O)` into itself and is
     invertible on its affine hull, with unit-modulus spectrum there. An affine injection of a polytope into itself with
     `|det| = 1` on its hull preserves volume, so it is onto. `Φ` therefore permutes the vertices of `Ψ(O)`.
  4. *Cases by `rank Ψ`.*
     - Rank 3: `Ψ = id` and `Φ` permutes `{±e_a}`, so `Φ ∈ O_h`.
     - Rank 2: `Ψ(O)` is a centrally symmetric polygon with at most six vertices. Its centre-fixing automorphisms are a
       subgroup of `D_4` (parallelogram) or of `D_6` (hexagon). A non-affinely-regular centrally symmetric hexagon has a
       subgroup of these, so no new spectra arise. The spectra are `{±1}`-sets, `{±i}`, `{ω, ω²}` and `{e^{±iπ/3}}`,
       each a sub-multiset of an O_h spectrum.
     - Rank 1: `{±1}`. Rank 0: empty.

  The affine rules' induced maps are self-maps of `O` because `conv R(Q) = O` (L2: `R(Q) = V₀`, which needs `Λ_{y,b}`,
  hence H-PREP and NNB) together with `R(πQ) ⊆ O` (Theorem C(ii)). `O = conv R(L)` is neither needed nor sufficient,
  because CONS constrains `Φ` only on the orbit of `Q` (LP-1). CC-NAT's expectation rests on Theorem C (conditional)
  and Lemma P (proved, conditional on Theorem C(ii) and L1–L3), and its route to failure includes their failure (review
  N8).
- **What can be found (the cone argument; `review/proofs/REVIEW-CONE.md`: PROVED UNDER STATED EXTRA HYPOTHESES).**
  - **Under `STAB(K)`** (`span O_K = span O_{K−1}`), with a constant herald, unit-modulus eigenvalues are roots of unity.
    With rational reach their orders are 1, 2, 3, 4 or 6, so a positive can only be of the R60 type
    (`{1, e^{±iπ/3}}`) or the `S_3` type (`{−1, ω, ω²}`). For such instances, C cannot instantiate OICORE-1's ENC-G.
  - **Without `STAB(K)`** the review gives exact counterexamples in the abstract class: at `K = 1, 2` with VAL, and at
    `K = 3` without it, with an eigenvalue pair at `arccos(3/5)`. The spectrum is then reported without the bound.
  - r6's "a rotation by `arccos(3/5)` is excluded on paper for this protocol class" is **withdrawn**.
  - `STAB(K)` is reported per instance (prereg *Obligation C*).
  - **Remark (review R1; its finite-order scope applies to instances with `STAB(K)`).** `O_h` together with an
    R60-type map generates an infinite subgroup of `O(3)`. No finite subgroup of `SO(3)` properly contains `O`, so the
    closure contains `SO(3)`. A finite-order positive would therefore
    bear on density. It would still need a bridge theorem (the kernel's dense route takes an infinite-order fixed gate)
    and a native supply of the octahedral part, which AP1 Lemma 5 does not give under R1.

## 7. Relation to M-ARC and Theorem C (§A.34)

**M-ARC.** ARP1-MARC-SURVIVAL landed at `fd539e15` (#1208; receipt `verification/receipts/ARP-1-MARC.json`, `Q` =
`e064e766`; `E` = `c95e5c34`; results review #1208 c.6732612066, CONFIRMED WITH QUALIFICATIONS).
- *Different objects.* M-ARC tests determination of `Q* = 1` functionals on a window (knowledge). P, B and C measure
  record statistics (mixing).
- *The true direction.* Non-determination by full records implies non-determination by any coarse-graining of the same
  records. The converse does not follow.
- *Why it does not transfer.* The double-slit records come from other cells under another access pattern.
- *Qualifications carried.* The results review gives three: the protection is of the window, through L-ACC (finding 9);
  D's window knowledge is contained in I's (finding 10); the two sizes carry the information of one (finding 11). Its
  finding 8 states that SURVIVAL "is not a proof of inaccessibility". The owner's characterization restates this: "its
  survival result establishes no exposure under a specific mathematical test. It does not prove that indirect
  interference measurements cannot reveal relevant information" (c.6733711272).
- *Scope.* M-ARC is affine `N_1` only, and its variant D removes P1's isolation, which this round keeps.

**Theorem C.**
- *Direction that holds.* With detectors that factor through `R` (true of `S_Z`, `S_X`, `S_Y`), the calibrated records
  of the affine rules lie in `O`. Every composition-consistent record operation is a self-map of `O`, so W-CL does not
  fire (Lemma P, proved, conditional on Theorem C(ii) and L1–L3), and W-OCT does not fire.
- *What it does not cover.* Non-affine rules, detectors that do not factor through `R`, and P.
- *Indirect against direct.* For C, indirect access through these detectors equals direct access. For detector
  families reading less than `R`, indirect access is a coarse-graining, and confinement transfers from direct to
  indirect only.

## 8. A/B and per-principle ablations

Each row reports `pred_change` and `mech_change` (both computed) and `dynamics_credit` (the frozen label). The
expectations below are on paper or from the probe (§10), and are disclosed.

| test | arm or ablation (fixture frozen) | kind / credit | expectation |
| --- | --- | --- | --- |
| P | `A_P` = B minus SA-1(c) (`Adm_A`: off plus all of `Σ`) | — | existence: succeeds; universality: fails (four sharp supplies) |
| P | construction B (`Adm_B`) | — | existence and universality: succeed |
| P | ABL-SA1c: `Adm_A` | state restriction / none | P-RECORD-WITHOUT-SUPPRESSION; `mech_change`: the sharp mechanisms join two `(1, 1)` cells |
| P | ABL-SA1b: the observer registers both slots of the held marker and the screen | access restriction / none | token "not applicable (access ablation)". `OLC`: every joint subset has conditional `V = 1` and path predictability `Pz = 1`, so `OLC.joint` is true. SA-1(b) carries observer-level complementarity (re-review R8-B2) |
| P | ABL-RECIP: `Adm_B` plus copy-only couplings | dynamics / a different mechanism | copy-only `(w, 0)` gives `V = 1`, `D = 1`; `mech_change` adds the copy mechanisms |
| P | ABL-ENV-u: the environment cell `(0, w′)` | state restriction / none | `V = 1`, `D = 0`, `K` identity (it becomes SH-0) |
| P | ABL-ENV-v: the environment cell `(w, 0)` | state restriction / none | `V = 0`, `D = 1`, `K` uniformizing (it becomes the marker) |
| P | ABL-P3 (FIX) | dynamics | not posable: no off arm without arming (NR-16) |
| B | construction A: `Acc_A` = every slot of every cell | — | measured; Lemma NC-F applies only if `d = r_S = r_E` |
| B | construction B: `Acc` owner-typed (D15), read in full | access restriction / none | measured |
| C | C-A (`reg = none`) | — | measured |
| C | C-B (forward conditioning, terminal heralds, refills) | access restriction; supply / none | measured |
| C | affine `g` / zero-tick (ABL) | dynamics / a different mechanism | Theorem C with Lemma P: no W-CL |

There is no level-3 benchmark arm. Imported quantum structure appears only as controls (QM-P, C-STAB, C-R60, C-R60-ODD,
C-35, C-S3) and comparators (Englert's bound, the Clifford class).

## 9. Controls with teeth

The full table is in the preregistration.
- **New in r7:** PL-CONFOUND, PL-SPI, B-REG, C-R60-ODD, CW-P's eraser and AB-P-FIX.
- **New or changed in r8:**
  - MECH-FIX, for the computed `mech_change`;
  - B-REG extended to a subset of `Acc` (`lp_reads_equal_acc`);
  - QM-P's purified-dephasing arm, for the access-relativity of `D`;
  - PL-SPI under the kernel `K`;
  - AB-P-FIX with both readings.

## 10. Probes (controls, not evidence)

| file | sha256 | content |
| --- | --- | --- |
| `probes-r9/olc.py` | `991b5219b565276515aa59171415b2ebb9c6bc925eb425de0dc452aab312200f` | loads `probes-r8/p_native.py` unchanged. It computes `OLC` for ABL-SA1b: all four joint subsets give `(V, Pz) = (1, 1)`. It also generates the slot-wise part of `Adm_A` and `Adm_B` by rule: B has no record without suppression; A has four. The `u + v` cells are in the reviewer's `adm_closure.py` |
| `probes-r8/p_native.py` | `72c4db13ad50c8a3172bb08480493a95d9983a007504ef15077796631f0bb8e6` | r7's probe plus the kernel `K` (PL-SPI: constant reset kernel), the computed mechanism sets for ABL-SA1c and ABL-RECIP, ABL-ENV-u and ABL-ENV-v, and ABL-SA1b (both slots read: conditional `V = 1` with `D = 1`). From r7: construction B's arms, PL-CONFOUND, PL-SPI and the copy-only ablation; `D` over all held cells; `K`; the eraser by slot content over both phases; the A/B predicate (A: not implied; B: implied). It evaluates P's decided instance (disclosed). Replaces `probes-r6/p_native.py`, whose eraser labels were read before the final free tick and which used `φ = 0` only (review B5) |
| `probes-r6/tri_affine.py` | `d6c3b1fb…` | unchanged |
| `probes-r6/pusey_probe.py` | `b7526d68…` | unchanged; read together with B3 (the `(1, 1)` point) |
| `review/probes-r8/adm_closure.py` | `479a10c2…` | the reviewer's: the `u + v`-known cells give `V = 0`, `D = 1` |
| `review/probes-r7/qm_sham_frame.py` | `65524ef2…` | the reviewer's: stabilizer QM under P's protocol (purified dephasing `D = 1`); C-R60-ODD's polynomials |
| `review/probes-r6/p_arms_indep.py`, `b_incomplete.py` | `1e351a74…`, `f02aeaeb…` | the reviewer's: an independent re-implementation of P, the nine supplies, the eraser on both arms and PL-CONFOUND; the classical register |

## 11. Additions on the owner's freeze decisions (c.6735014875)

- **Level 1 presentation.** Level 1 (L(i), P-COMPLEMENTARITY) records that the run reproduces a known paper construction
  (AP1 §4.5 with SA-1(c); AP1 Lemma 3). It is a consistency check, not a new derivation and not an independently
  generated mechanism.
- **`ATTR`.** It is computed from the validation layer and printed beside the token, never folded into it. It reads
  "attributable to which-path recording" only if the marker records and suppresses while the valid kick-matched sham
  SH-K retains the interference. Since in every channel-determined model (construction B, QM, classical waves) the
  kick-matched sham suppresses in every case in which the marker does, `ATTR` reads "not attributable" there. This is a
  disclosed structural fact (§1).
- **The representation ledger.**
  - Each of L-PATH, L-PORT, L-CAL and L-UPRIME is recorded with what it identifies, why it supplies no dynamics,
    probabilities or outcomes, and its admissible alternatives.
  - REP-INV recomputes the token inputs under each alternative, with the encoded transposition transported to
    `S P S⁻¹` under a recalibration `S`. It tests outcome-neutrality within each symmetry class only.
  - For L-UPRIME the non-symmetric test is UPR-BC. If a B-C fragment is contextual, and the completion "every slot of
    every cell" restores a model, L-UPRIME is reclassified as imported for B-C.
  - L-PATH, L-PORT and L-CAL are confirmed on paper to supply no resource.
  - An identification whose variation changes a token, a witness, a contextuality verdict or P's class predicate is
    reclassified as imported, and the tokens depending on it become benchmark results.
  - On paper every alternative is a symmetry of the construction, and REP-INV is expected to read `invariant`.
  - REP-PLANT, an identification that XORs the screen with the marker's kick slot, gives the check teeth.
- **The three A/B fields.** Every ablation, and the comparison of `A_P` against B, reports `pred_change`, `mech_change`
  and `access_only`.
  - `access_only` is computed: the full world laws must be identical, with only the registered or unread records
    differing. Registration is modelled as a read without meter cells. Arms present in both classes are compared;
    an arm in only one makes `access_only` false.
  - Expected: ABL-SA1b is access-only. ABL-SA1c, ABL-RECIP and ABL-ENV-u/v, and `A_P` against B, are not.

