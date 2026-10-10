# T6 — NOTES (stage 6, Q-EX-FULL, step 4: the test of (b) against the complete applicable premise set at L)

Running record. Times are UTC from `date -u` at the moment of writing each entry (never estimated).
Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, read-only at `pt/base/`. Working directory `pt/T6/` only.

## N0 — 18:50:48Z start; 18:51:23Z governing texts read

- `pt/T6/` absent at launch; created; `.start_marker` written first (18:50:48Z): six manifests exit 0,
  `ns.manifest.sha256` exit 0, HEAD = L, porcelain empty, 0 bytecode under `pt/base`, twelve protocol files at
  their prefixes with sidecars OK, `ls -la pt/` recorded.
- Read in full, in the prescribed order: PROTOCOL-STAGE6 (b277b7c1), -AMENDMENT-1 (59019538), -AMENDMENT-2
  (748f1764), AUDIT-I (845bd662), AUDIT-G (3fd6763d), AUDIT-R (04308355) [prefixes computed 18:50:54Z],
  PROTOCOL-STAGE5 (9e01f098) + amendment 1 (1f639115), PROTOCOL-STAGE4 (d3da2811), PROTOCOL (239dc123),
  PROTOCOL-AMENDMENT-1 (b41aa0e7), -2 (2a2f78f3), INTEGRATION-NOTE-STAGE5, INTEGRATION-NOTE-STAGE4;
  pt/base/AGENTS.md lines 41–94, §A.21 (line 436), §A.26 (lines 223–246), §A.31 (lines 306–342).

## N1 — fixed BEFORE the first node (18:51Z)

### N1.1 The target, (b) in its weakest sufficient form (INTEGRATION-NOTE-STAGE5 §2; A1.6)

Two forms, either suffices for `K = Q3` by stage 4 (given H1–H3):
- **(b_FJ)** — (b) for {flow, J} on one token: the idle extension to one token of the pair (`actC` or `actT`; for
  mixed placement only flow-on-control with J-on-target) of the native drive's one-parameter rotation group and of
  its J-conjugate preserves the pair cone `K ⊆ W 3`;
- **(b_Dφ)** — (b) for the drive together with the substratum phase flow (about z) on one token.
The test: does Π_app(L) (R6's 199 items at their actual status) force (b_FJ) or (b_Dφ) for every closed
`K ⊆ W 3` that the applicable items admit?

### N1.2 Decision vocabulary (base protocol amendment 2; stage-6 A2.4)

- **DERIVED** (= the stage-6 outcome DERIVATION): a chain from inventory items at status *proved* [K] (or
  refuted-not-used) to (b_FJ) or (b_Dφ), every step [K] (file:line at L) / [W] (complete written argument) /
  [X] (exact computation in `pt/T6/`, replayed), every premise passing the disguise test of PROTOCOL-STAGE5; no
  do-not-assume item except as the item under test, named.
- **CONDITIONAL(item; status)**: the chain uses an inventory item at status assumed / conditional / open /
  empirically motivated; the item is named at its status (as stage 5's α–δ). A restatement of (b) as the item
  does not make the verdict CONDITIONAL — it is recorded as circular.
- **INDEPENDENT** (= INDEPENDENCE): an exact countermodel satisfying every item reaching the pair cone at L, cited
  row by row against R6's audited table for that alternative (SATISFIES or NOT REACHED on every non-hypothesis
  item), every R6 row the verdict leans on re-verified by my own exact check, violating (b_FJ) and (b_Dφ) by an
  exact witness; the missing assumption isolated as exact content, with its disguise test. Scope: "independent of
  the premises at L as stated", never of every extension of the framework.
- **UNRESOLVED**: failed derivation without countermodel, or a countermodel without the row-by-row check; both
  failures recorded. A failed derivation alone is never INDEPENDENT.

### N1.3 Productivity test (§A.31, fixed now)

A node is a **gem** iff it yields a fact strictly stronger than the obvious restatement of the records already
audited (AUDIT-I/G/R, the stage-4/5 notes) AND either (1) is an exact certificate at a stated instance (a
derivation with every step checked, or an exact countermodel with every applicable row checked), (2) is an exact
obstruction for a stated class of routes, or (3) exposes a hidden assumption. Otherwise record-only (coherence
relabelling). Gem classes: NEW (structural blind spot not previously characterized) / POSITIVE (validates an
inheritance or assumption) / ELABORATING / CONFIRMING / BORDERLINE.
Fixed point: stop after 3–4 consecutive passes with no NEW finding, at a genuine wall, or when the question is
answered.

### N1.4 Skepticism rules (fixed now)

- A branch favourable to the framework (a derivation step) is pressure-tested: is the premise at status proved,
  at level P or carried to P by a bridge proved at L (named, file:line, verified by reading), does it pass the
  disguise test, does the step hold on a countercontrol (K(Z_F) must fail any exclusion claimed; Q3 must pass).
- An independence branch is pressure-tested equally: every applicable row cited by id; every row the verdict
  leans on re-checked by my own exact code; the countermodel must be shown to violate the precise weakest form,
  not a stronger one.
- Level separation: an H-, M- or G-level item reaches the pair cone only through a bridge proved at L; I verify
  the absence of a bridge for each route I try (by reading the item's statement and the kernel's import/type
  structure), not by citing AUDIT-I §2 alone.

### N1.5 Planned node order (depth-first; derivation first)

- D1 — the H/M/G-level items: for each route, does a bridge to `W 3` exist at L? (verify per route)
- D2 — the kernel-completed (KC) dependencies and the kernel theorems quantifying over pair cones (I3 B1–B7,
  `no_candidateCone_cnot_reflY`, DIM-1 / K2-GUARD / COMP-1 / NB-1 / EFF-1).
- D3 — the object-specific discharges (ContextStable / StructurallyClosed for the substratum class,
  HasParallelReferenceExtension for the full theory, LayerFlowExecutable under composite unitary control,
  implementation locality and embedded observation for exact QM, DerivedOI for the substratum theory): do any
  reach the composite cone in `W 3`?
- C1 — the countermodel (K(Z_F) first: explicit; then K(E0)), row by row against R6's table, with my own exact
  re-checks; exact witnesses against (b_FJ) and (b_Dφ).
- M1 — the missing assumption isolated, with its disguise test.

## N2 — 18:51:23Z–18:58:41Z inputs read (before the first node) [stamp corrected 19:22:56Z: first written "18:52Z–18:58Z", whose start was estimated; the bounds are now the two `date -u` readings around the reading]

R6: RESULT.md, REASSESSMENT.md (all tables), r1_inventory.out (199 APPL lines: id | bearing | level | status | flag |
name), r2_cones.py header and lines 1–170 (conventions). G6: RESULT.md, GRAPH.md §3 (discharges), §4 (Anc(P), NO-MEET),
graph.tsv format. I3: RESULT.md in full (bridges B1–B7, absent A1–A13, exposed facts). I4 records.txt (lines of
I4.22, I4.36, I4.39, I4.46, I4.57, I4.136). Kernel at L: K2Guard.lean (whole), CompositeDimension.lean:80–254,
:730–869, KInfFoundations.lean:250–309, :395–504, CompositeInterface.lean:200–274, :436–450, the root OIBridge.lean
head. PROTOCOL-STAGE3.md:30–69 (levels (i)/(ii)); pt/X/RESULT.md:170–209 (SD2 proof sketch, the K4 instance, G16).
Not read: anything under pt/audit/ other than the three named audits; no OWNER file; no evidence/ copy.

Conventions fixed from the kernel: W 3 index 0 = unit, 1,2,3 = the ball's coordinates x0,x1,x2 (Pauli X,Y,Z);
`actT N ω = ω·Hom(N)ᵀ`, `actC N ω = Hom(N)·ω` (Hom(N) = 1 ⊕ N); `nflip = diag(1,−1,−1)` = R_x(π), axis `z3 = e_z`;
`ball3Drive`: flow `rot3 t` = R_z(t), NOT `rot3 π` = diag(−1,−1,1), J = `cyc3` (x,y,z) ↦ (z,x,y) (a rotation by
2π/3 about (1,1,1)); J R_z(t) J⁻¹ = R_x(t) (the "drive through the NOT"); J R_x J⁻¹ = R_y.
So the two weakest sufficient forms of INTEGRATION-NOTE-STAGE5 §2 are (b) on one token for two of the three
coordinate rotation flows: {R_x, R_y} (drive through the NOT with its J-conjugate), {R_x, R_z} (drive with the phase
flow about z; equally ball3Drive's flow with its J-conjugate), and A1.6's {flow, J} forms add J = cyc3 itself.
A countermodel violates every one of them, on either token and in the mixed placement, as soon as on EACH token it
leaves itself under some member of R_x AND under some member of R_z (then every form containing R_x or R_z fails;
{R_x, R_y} contains R_x). I also test R_y and cyc3^{±1} directly.

## N3 — node D1 (19:01:27Z–19:04:06Z): H-, M-, G-level items — is there a bridge at L? [X t1 + W] [stamp corrected 19:22:56Z: first written "19:01Z–19:03Z", whose end was estimated; now the `date -u` readings of the t1 and t2 headers]

`t1_bridges.py` run 1 (kept: `.run1.*`): VERDICT NO-BRIDGE-AT-L, but the P-name `W` also matched
`def W (u : PS s) : Matrix …` (WeylTwirl.lean:151, a Weyl operator) — a false P-anchor that can only enlarge MEET;
it inflated B4. Run 2 (amended in the header, 19:02:29Z): P-anchors CompositeDimension, K2Guard; 16 HMG anchors
(OperationalAssembly, ReferenceExtension, ImplementationLocality, StructuralClosure, LiftAudit, RouteB,
EmbeddedObservation, CompletedOI, CarrierGeneralOIPlus, OIRealization, SubstratumSource, PhysicalCharacterization,
GeneralCarrier, TypedCompletion, PairFlowEquivalence, SpectatorBridge). MEET = {OIBridge} (the root); the root's 65
declarations carry no P-token and no HMG-token; SHARED = 17 infrastructure modules with no Prop-valued
structure/class; the modules that import CompositeDimension are 11 K-cluster modules and the root. Countercontrols:
one synthetic import edge makes MEET 12 modules; a synthetic two-vocabulary declaration is flagged. Manuscript and
roadmap co-occurrence: one line, ROADMAP.md:68 (the P1 row), which states the lift from the elementary d = 3 system to
the matrix carriers as OPEN (Kₙ "no theorem lifts…"; K2 OPEN) — an obligation, not a bridge.
Reading [W]: a Lean declaration can name only what its module's import closure defines, so no declaration at L can
state a fact relating an H/M/G object to W 3. Verdict D1: NO BRIDGE AT L, verified per route (α
HasParallelReferenceExtension, β ImplementationLocality/ContextStable, γ StructurallyClosed, δ LayerFlowExecutable,
ζ EmbeddedObservation/ObserverRecursion, DerivedOI, CompletedOI/OIPlus, the sealed core and its realizations) —
each is defined in an HMG-anchor module whose closure excludes CompositeDimension. Gem: CONFIRMING (AUDIT-I §2, G6
NO-MEET) with a stronger mechanical form (declaration-level, not only record-level).

## N4 — nodes D2, D3 (19:04Z–19:06Z): pair-cone theorems, KC edges, discharges [X t2 + W]

`t2_pairthms.py` run 1 (kept): ANC-PO False from a mis-parse (capitals inside backticked identifiers in the level
strings); run 2 (header amendment 19:05:07Z): every other line identical.
- (a) Declarations binding a set of pair vectors: 7 definitions (maxCone, jointStates, maxConeOf, jointStatesOf,
  CandidateCone, productSet, cnotOrbit) and 2 theorems, both the reflY no-go (`no_candidateCone_cnot_reflY`
  K2Guard.lean:143 and its restatement in `k2guard_orientation` :277). No other theorem at L quantifies over a pair cone.
- (b) 39 theorems mention actC/actT: 33 equalities (carrier identities, gate relations with involutions, the
  product identities B4), 1 False (the no-go), 4 memberships, 1 other. Of the memberships: `reflY_mem_productSet`
  (the product set is closed under actT reflY — a fixed set, not a cone variable), `k2guard_orientation` (actT reflY
  invariance appears only as the antecedent of → False), `c5_sep` and `relT_not_dimension_selecting` (d = 5
  controls; the ∈ concerns products and maxCone). Reading: NO THEOREM AT L CONCLUDES THAT ANY PAIR CONE IS INVARIANT
  UNDER actC g OR actT g, for any g. (b) can enter a derivation only as a hypothesis.
- (c) Anc(P) over R/RA/RN/KC: 25 nodes (21 records, 4 kernel declarations), every record at level P or O; the only
  KC edge inside Anc(P) is I3.12 → I3.1 (the gate theorems depend on the carrier). The kernel completion adds no
  H/M/G premise to any pair object. Countercontrol: synthetic I3.1 → I1.1 brings an H node in.
- (d) The ten object-specific discharges (substratumClass_contextStable, mixC_contextStable,
  substratumClass_structurallyClosed, hcompRealized_consistent_with_parallelReferenceExtension,
  layerFlowExecutable_of_control, implementationLocality_of_qm, reversibleImplementationLocality_of_qm,
  embeddedObservation_of_qm, genTheory_embeddedObservation, substratumTheory_derivedOI): none of their modules reaches
  CompositeDimension; their statements name substratumClass, MixC, FiniteOperationalTheory (with
  ExactAllFiniteEndomorphicQuantumOps or HasCompositeUnitaryControl), genTheory, substratumTheory; no P-token.
Verdict D2: the P-level kernel content constrains K only by H1/CandidateCone, cnot-invariance as a hypothesis, the
reflY no-go, and identities on products — no route to (b). Verdict D3: every discharge is a closed statement about
one object off the pair carrier; none reaches the composite cone in W 3. Gem: ELABORATING (an exhaustive list of the
pair-cone and actC/actT theorems at L, with conclusion shapes) — the derivation's wall is located exactly: the first
step that needs actC/actT of a flow member or of J on a non-product vector has no premise at L.

## N5 — node D4 (19:06Z–19:08Z): the derivation attempt closed [W]; verdict of the derivation side

With D1–D3 the derivation side has no route left that stage 5 did not have, and the complete premise set adds
none: (i) the H/M/G items reach the cone through no bridge at L (declaration-level, t1); (ii) the KC edges add no
H/M/G premise to Anc(P); the only theorems at L quantifying over pair cones are the reflY no-go (t2); the bridges
B1–B7 transfer effect availability, products, carrier identities on products, the Lorentz cone, the π-rotation NOT
and eball_three — never an operation on non-product vectors; (iii) every discharge is a closed statement about one
object off the pair carrier (substratum class, MixC, exact QM, genTheory, substratum theory). The remaining routes
are CONDITIONAL-shaped and not admissible at L: λ (KT4Core with tok, [D] steps, no ≥3-token structure at L),
homogeneity H (PT-record candidate, [W + L]), the spectator clauses α–δ (level M, need an M→P bridge that L lacks; their
transcription to W 3 is (b) for the class, a do-not-assume clause), K2's clause and P-ACT2's idle-extension reading
(do-not-assume). Derivation side: FAILED (no chain from items at L to (b)); the wall: the first step that needs
actC/actT of a flow member or of J on a non-product vector has no premise at L. A failed derivation alone would be
UNRESOLVED; the countermodel follows.
Skepticism applied to the favourable branch: none arose (no candidate step survived); the one kernel theorem that
quantifies over pair cones was checked for a hidden positive content — its conclusion is False under reflY-invariance,
i.e. it forbids an operation and forces none.

## N6 — node C1 (19:08Z–19:12Z): the countermodel K(Z_F), my own exact construction [X t3 + W]

Pre-run edits of `t3_countermodel.py` recorded in its header (19:11Z: Z4 weights; faster tableOf, same values); one
inline `python3 -` stdin helper was used to apply the two header/code replacements (an editing helper, no import
beyond the standard library; recorded as a deviation). Run 1, 6.7 s: 17/17 checks PASS, VERDICT C1-KZF-EXACT.
- Dictionary checks D0a–D0d (cnot = Ad(CNOT); actC/actT R(U) = Ad(U⊗I)/Ad(I⊗U) for X, Y, Z, U_J (R(U_J) = cyc3),
  the three quarter-turns and Rx(cos 3/5); transpose; tr(M(a)M(b)) = 4 ipW(a, b)).
- Z1–Z2, Z6: M(z_s) = I/2 − P_s, P_s the four orthogonal Bell-type projectors (joint eigenprojectors of X⊗Z, Y⊗Y);
  ipW(z_s, z_t) = [s=t]/4; K ≠ Q3 (eigenvalue −1/2).
- Z3 H1: 4 ipW(prodState x y, z_s) = 1 + x·M_s y with M_s a signed permutation; SOS over the whole ball.
- Z4 H3: my own proof [W] (TEST.md §C1.3: one-correction lemma for orthogonal Bell-type defects, Schur complement),
  instance-controlled on 600 rational PSD matrices (278 with a negative pairing, all corrected into Q3 ∩ Z_F*);
  countercontrol: for the non-orthogonal family {z_s, actC Rx(3/5) z_s} a pure state has two negative pairings.
- Z5 H2 level (ii): Gbig = ⟨cnot, 32 even signed-diagonal locals⟩ of order 64 (the X record's number) permutes
  Z_F, fixes (0,0), and lies in Aut(Q3) (16 conjugations, 16 transpose-conjugations, cnot = Ad(CNOT)); G16 ⊆ Gbig
  since its generators are among Gbig's.  SWAP also permutes Z_F (record).
- Z7: actT reflY z_(−1,−1) pairs −1/8 with z_(1,−1) ∈ K — consistent with `no_candidateCone_cnot_reflY` [K].
- Z8: product effects span W 3 (rank 16): LT on the carrier.
- B: every tested map moves K(Z_F) out, on each token: R_x, R_y, R_z quarter-turns (−1/8), R_x and R_z at
  cos t = 3/5 (−1/10), cyc3 and cyc3⁻¹ (−1/8); witnesses are rotated Bell-type pure states in Q3 ∩ Z_F* (all 64
  certified). Flow law (symbolic): ipW(R_a(t)_τ z_s, R_a(π/2)_τ p_s) = −sin(t)/8 for a ∈ {x, y, z}, τ ∈ {C, T}.
- Countercontrols: nflip and rot3 π (symmetries of K(Z_F)) give no negative pairing over the 104-element pool; every
  rotated pure state is a trace-one projector (the modeled operations preserve Q3, §A.21).
Gem: ELABORATING (an elementary, self-contained H3 proof and an explicit witness family with a closed-form flow law;
agrees with R6 r2 values up to its 4× table normalization: −1/8 vs −1/2).

## N7 — nodes C2, C3 (19:12Z–19:16Z): the row-by-row check and every axis

- `t4_rows.py` (binder test fixed before its first run, recorded in its header): 199 rows; T6 verdicts SATISFIES 115,
  SATISFIES (vacuous) 3, NOT REACHED 68, FAILS [hyp] 13 — R6's tally; every K-blind row with a kernel declaration
  binds no `Set (W …)` variable; 16 rows have no kernel declaration (NO-DECL: W d, NativeGateBall.parity, the [D]
  NClass/EvenCycle/ipW-dualW, the ROADMAP K1/K∞ rows, the truncated I3.185 names, I4.236) and are read in TEST.md;
  every cone and kthm row is backed by a PASS of t3; every I4 hmg row's declaration lives in a module whose closure
  excludes CompositeDimension; every FAILS row has a hypothesis status (not at L [D], PT-record, open) or the
  do-not-assume flag. Countercontrol: the binder test fires on `no_candidateCone_cnot_reflY` and not on `maxCone`.
  VERDICT ROWS-OK.
- `t5_axes.py`: for a symbolic unit axis n, both tokens, all four s: ipW(R_n(t)_τ z_s, R_n(π/2)_τ p_s) = −sin(t)/8
  modulo the sphere, the witness is a pure state in Q3 ∩ Z_F* (pairings (1 − n_i²)/8 ≥ 0 and 0); countercontrols at
  n = e_x and at the half-turn. VERDICT C3-ALL-AXES: K(Z_F) admits no one-parameter rotation subgroup of either
  token; every member with sin t ≠ 0 moves it out. Gem: ELABORATING (re-derives R6's (b_n)/(b_S4) rows for every axis
  at once with one witness family; consistent with stage 4 Z z1's stabilizer).

## N8 — 19:17Z–19:21Z TEST.md, replays, fixed point, verdict

- TEST.md written in three parts (≤ 250 lines each): §0 verdict, §1 target, §2 derivation attempts D1–D4 with the
  step table and the CONDITIONAL-shaped routes, §3 the countermodel with the complete H3 proof, §4 the row-by-row
  table (all 199 ids cited by class, per-row lines in `t4_rows.out`), §5 the missing assumption with its disguise
  test, §6 level distinction, §7 pressure tests, §8 gems, §9 not claimed.
- Replays 19:20Z: t1–t5 replayed into `.replay.{out,err}`, all five byte-identical (cmp). No bytecode in `pt/T6`.
- Fixed point (§A.31): the passes D1 (CONFIRMING), D2 (ELABORATING), D3 (CONFIRMING), D4 (closure of the derivation
  side), C1 (ELABORATING), C2 (POSITIVE), C3 (ELABORATING) gave no NEW finding; the question is answered.
- Verdict: **INDEPENDENCE** (A2.4): derivation failed with the wall located (no premise at L for the composite action
  of a flow member or of J on a non-product vector); countermodel K(Z_F) satisfies every non-hypothesis item reaching
  the cone (115 + 3 vacuous SATISFIES, 68 NOT REACHED) and violates every weakest sufficient form of (b) by exact
  witnesses (flow law −sin(t)/8, every axis, both tokens; cyc3^{±1}). Missing assumption: A_miss = (b) for {R_x, R_z}
  (= ball3Drive's flow and its J-conjugate) on one token; fails the disguise test (restates I3.153, I3.165's clause,
  and the drive instance of I4.3/I4.82); the disguise-passing closers λ and H are not items at L.
- Deviations so far (for RESULT §5): one `python3 -c` version check without -I -B (19:08Z; no file under pt/ written);
  one inline `python3 -` stdin helper applying two exact replacements to t3 before its first run (19:11Z).
