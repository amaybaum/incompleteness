# O-A node 1: where an uncountable non-monomial operation family could reach the observer

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to the repository.

**Base.** Kernel and papers at `main` = `ec49d0b41648d8a070179c8fa3aaf20b5c6ff863`; every [AT] name below was confirmed by
`git grep` of its declaration at that commit (Lean paths under `verification/lean-mathlib/OIBridge/`). Paper and audit
line numbers are at the working tree `38e9af32` (research-only commits on top of `ec49d0b4`; `papers/` and the audit
cited are unchanged between them). Thread H (H:n) and thread I (I:n) at `804843f1`; x-screen (XS: `REPORT.md`, SC:
`source-search-20261020/SOURCE-CHECKPOINT.md`) at `research/x-screen-20261018`; ledger (LG) =
`f2-ledger-20261020/LEDGER.md`; MEMO via `x-screen-20261018/sources/EXCERPTS.md`. PG = `verification/programmes/oi-qm/PROGRAMME.md` at `ec49d0b4`;
CTA = `verification/audits/physical-realization/continuous-time-audit.md`.

**Tags.** [AT] adopted kernel theorem on main; [W] written argument here; [EC] exact computation here (replayed twice,
byte-identical); [UP] unsourced premise; [L] literature; [rec] a recorded result of another record, not re-derived.

**Productivity test (fixed before the node).** Gem iff the node yields a fact strictly stronger than "the corpus has
no source for O-A" and either constrains where a source could come from or exposes a hidden assumption in the
obstruction itself.

***

## 1. Inventory

Status codes: **closed-K** (a kernel theorem excludes it as stated), **closed-EC** (exact countermodel/computation),
**closed-W** (written argument only), **posit** (states the resource), **open**.

| # | item | location | what it supplies | status and exact reason |
|---|---|---|---|---|
| 1 | hidden-sector conditions C1–C4, C3 high capacity | `papers/Main.md`:72–80; C4 primitive :604 | finite hidden capacity, readback, coupling | closed-K for operations: diagnostics of the visible law, configuration-diagonal (SC N9 [rec]); any finite capacity is a finite carrier, so `obsTheory_nonnegBounded` FrozenSourcing.lean:84, `readWriteSourced_not_qm` ReadWriteControl.lean:174 apply; the capacity → ∞ limit is row 13 |
| 2 | fixed hidden prior μ_H as a realization datum | Main.md:60 | one real distribution per realization | not an operation; a different prior is a different realization. Mixtures with real weights stay `NonnegBounded` (nonnegativity is preserved by nonnegative combinations) [W]; from one fixed prior, finite protocols reach countably many conditional priors [W] |
| 3 | global lattice orientation | Main.md:656, :658 | a fixed element of the frame group, "not resampled" | not observer-selectable; a single value, no family. An apparatus is a lattice configuration, so its orientations relative to the axes form a countable set [W]. Resampling is an open question (Main.md:658; book ch19) that would produce a mixture, not an operation (row 2). SC N6: does not separate Q3 from Γ(Q3) |
| 4 | antiunitary orientation of coherent completions | `papers/GR.md`:188–190, :200–214 | one global ℤ₂ branch | discrete; not continuous. Conditional on H-BG and reconstruction hypotheses |
| 5 | open purification lift | Main.md:600–602 | existence of a purifying system; canonical predictive quotient | open as a lift. Operations on the purifier are substratum processes, so a substratum-sourced reversible group on it is countable (row R4, CR below); coherent preparations do not give coherent control (LG §3 monomial-branch lemma [W+EC rec]); `fiber_freedom` threatens uniqueness (XS AW-X6 [rec]) |
| 6 | depth-two factorization; per-gate one-parameter groups; norm-continuous path to the update | GR.md:292; Main.md:268 | uncountable family of *-automorphisms (representation level) | the path exists: `driveQ_isContinuousPath` SecondOrderDrive.lean:225, `driveQ_one_eq_heisQ` :829, `layerQ_add_time` SecondOrderLayer.lean:966, `swapQ_add_time` SwapLayer.lean:494 [AT]. Its availability is not implied: `substratumTheory_not_layerFlowExecutable` LiftAudit.lean:200, `configurationLevel_not_layerFlowExecutable` :183, `gateFlow_half_not_preservesDiag` :155 [AT]; GR.md:272 box. Gate flows are ones-fixing: `onesClass` InstrumentRealization.lean:446 contains them, `onesTheory_not_qm` FlowEndpoint.lean:205 [AT] |
| 7 | continuous-time Hamiltonian interpolation; logarithm branch | Main.md:268; GR.md:292; GR.md:332 (H-local-lift) | a one-parameter unitary group with U₁ = U_φ | additional structure, chosen: `continuous_extension_not_unique` RegionLimit.lean:296 [AT]. Uniqueness decided negatively; local static generator CT3 open at width ≥ 3 (CTA:405–680) |
| 8 | continuous-time P-indivisibility; phase uniqueness from continuous-time data | Main.md:151, :222 | continuous T(t) of a Hamiltonian flow; phase retrieval from {T(t)} | presupposes a continuous-time flow (the continuum analogue, or the interpolation of row 7); concerns visible statistics, not operations |
| 9 | stroboscopic time T (E4: on Conf; E1-T: on the Weil carrier) | H:92–95, :238–250, :296–313; XS C11, AW-X5 | flows exp(t log P) at non-integer t | E4 with principal logarithms: closed-EC (XS P4 [rec], replayed here as control POS) and the layer-flow class is ones-fixing [AT, row 6]. E1-T: posits the continuum (H N1: BORDERLINE as explanation); E1-L fails G4 and M1 (MEMO §2.4 [rec]). **Non-primary logarithms: open, examined in §3** |
| 10 | selectable local coupling; state-dependent rule; H-Bell adjacency (E5); A6 gauge (E6) | GR.md:260; SM.md:102; Substratum.md:130–132; H:252–271 | real-parameter or context-indexed dials on the rule | closed-K: a coupling that is a bijection at every parameter value induces permutation operators (`readWriteSourced_not_qm` ReadWriteControl.lean:174, `offDiagonal_interp_not_monomial` :115, `readWriteControl_independent` :216); the observer theory does not see the rule (`sourcing_rule_independent` FrozenSourcing.lean:295, `obsTheory_rule_independent` SubstratumInterfaceAudit.lean:779) [AT]; E6 complex carrier fails A1 (`cx3b_complex_not_A1`, H:270 [rec]) |
| 11 | Weil/symplectic registration R (E3); polarization closure `PolC` | H:82–91, :220–236; PolarizationClosure.lean | Fourier/chirp images, phases at site level | R: Clifford group, finite mod phases → countable, Wigner-positive (I5) [rec, N]; `polarizedTheoryC_not_pairFlowSourced` PairFlowEquivalence.lean:211 [AT]; `PolC` positives rest on unsourced relabellings (AW-H2 [rec]) |
| 12 | Track B lift with a P0 selection (E2); Barandes correspondence | H:189–218; PG:104–112, §3.12 | a unitary lift of each indivisible law; lift gauge is continuous | representability sources nothing (PG:108, Arc D S1 padding theorem, §3.12); induced visible action monomial (`stochasticChannel_kraus_monomial` LiftSource.lean:251 [AT]); no operation map stated (XS C10). Under A1 closed-W by CR (§2) |
| 13 | limit / ensemble / dense closures; infinite-region completion | MEMO §1.1 (A1, A2); XS R5; GR.md:282–294; `ensemble_underdetermined` StochasticInterface.lean:118 | closure points of countable families | A1 adopted: countable sets fail (`countable_not_pairFlowSourced` PairFlowEquivalence.lean:218, `mixTheoryR_not_qm` StateMixingCoupling.lean:679, `fixedGateTheory_not_qm` DiscreteCompletion.lean:1948, `uncountable_of_layerFlowExecutable` PolarizationClosure.lean:135 [AT]); dense endpoint exists only on `Fin 2` (`DenseFiniteQM` DiscreteCompletion.lean:59); every barrier invariant is closed under limits (XS R5, H:34–42 [W rec]); finite-range reversible rules on the infinite lattice are finitely specified, hence countable [W] |
| 14 | K∞-Drive; drive-source plan | KInfFoundations.lean:264; Issue #865 (from #833 @`9fc5ec2e`) | a continuous reversible drive on the elementary body | posit / open: no chain consumer (I:320); finite-orbit bodies have none (`isEmpty_drivability_of_finite_orbits` OrbitNormalization.lean:124 [AT]); #865 states "K∞-Drive remains an unsourced operational premise" |
| 15 | K∞-Trans (transporting group) | OrbitGeneration.lean:79 | uncountable boundary-transitive group | exact form needs an uncountable group (`not_boundaryTransitive_of_countable` EffectSpace.lean:858 [AT]); not implied by a drive (`not_boundaryTransitive_flow` OrbitGeneration.lean:620 [AT]) |
| 16 | phase intervention; controllability resource; layer flow executable | GR.md:260–274; Main.md:568 | phases, the state-mixing operation, one layer flow | posit (E0): sufficient (`substratum_plus_control_qm` StructuralClosure.lean:414, `derivedOI_qm_iff_layerFlowExecutable'` DerivedQ3.lean:222 [AT]), excluded as a source (MEMO §2.4, H:273–278) |
| 17 | Hardy continuity; Masanes–Müller continuous reversibility | XS C5, C6; H:345–347 [L] | continuous reversible group as postulate | posit; G3 FAIL (XS [EC rec]) |
| 18 | swap-drive preservation (N2); exchange continuity (N1) | SC N1, N2 | preservation of K by the kernel's exchange drive | operation side [AT] on the C*-algebra; availability is the layer-flow hypothesis (GR.md:272); G2 FAIL (SC [rec]) |

***

## 2. Routes and their obstructions

### 2.1 The countable-realization lemma (CR) [W from AT]

**Premises.**
- (P1) OI-1: finite configuration spaces, observer a proper subsystem, bijective dynamics (Main.md:44–56). On each
  carrier the set of substratum processes is a subset of the finite group of bijections of a finite set,
  whatever the time model (discrete steps, or a time-indexed family φ_t: its range is still finite) and whatever
  real couplings index the rule (row 10).
- (P2) Supervenience: each available level-one unit conjugation on `Fin 2` is, up to a scalar, `f(π, c)` for a
  function `f`, a substratum process `π` and a context `c` from a countable set (finite protocol words, finite hidden
  contexts, conditioning events, a fixed prior).
- (P3) Countably many carriers.

**Conclusion.** The available level-one unit conjugations lie in countably many rays, so `¬PairFlowSourced T`
(`countable_not_pairFlowSourced` PairFlowEquivalence.lean:218), hence `¬ExactAllFiniteEndomorphicQuantumOps T`
(contrapositive of `derivedOI_pairFlowSourced_of_qm` :93, the `.mp` of `qm_iff_derivedOI_pairFlowSourced` :199).

**Proof.** The domain ⋃_carriers Bij(Conf) × C is countable; the image of a countable set under a function is
countable; take D = that image in `countable_not_pairFlowSourced`. ∎

**Scope.** CR is the counting argument of H:46–55 and of `mixR_countable_upToScalar` StateMixingCoupling.lean:662,
stated for an arbitrary realization function rather than a fixed closure. It covers context-dependent maps (E2),
prior-dependent maps, coupling-indexed and duration-indexed dials, and every finite capacity. It does not use
discreteness of time.

**Consequence.** Under A1, a source for O-A violates at least one of:
- (P2) supervenience: some available operation is not determined by the implementing substratum process and a
  countable context. The time-t operation of a flow at non-integer t has no implementing process of its own
  (row 6, GR.md:272); a description-level choice (lift gauge, logarithm) makes the operation depend on something
  other than the physical process;
- (P1) finiteness or bijectivity of the substratum (A1/A2; the complex field carrier fails A1, row 10).

H:259–260 already records that under E1 "at sub-period times the substratum is no longer the observer's ontic
model": that is a (P2) violation. CR shows it is the only kind of escape that keeps (P1).

### 2.2 Route table

| route | members (rows) | decisive obstruction | level |
|---|---|---|---|
| **R1 continuum from limits or closure** | 1 (capacity → ∞), 13 | A1 + countability: `countable_not_pairFlowSourced`, `mixTheoryR_not_qm`, `fixedGateTheory_not_qm`, `uncountable_of_layerFlowExecutable`; and the barrier invariants are closed under limits (XS R5) | closed-K for availability; the limit-invariance step is [W] |
| **R2 continuous parameter in the substratum's own dynamics** | 6, 7, 8, 9 | intermediate-time executability not implied (`substratumTheory_not_layerFlowExecutable`, GR.md:272); with the gate flows made available, still ones-fixing (`onesTheory_not_qm`); principal-log stroboscopic algebra ones-fixing (XS P4 [rec]) | closed-K for availability; **closed only for primary logarithms** as a ones-fixing exclusion (§3) |
| **R3 observer-side real dial acting through the substratum** | 2, 3, 10, 14, 15 | permutation-valued at every parameter (`readWriteSourced_not_qm`, `obsTheory_rule_independent`, `obsTheory_nonnegBounded`); priors only mix (row 2); CR | closed-K (dials), closed-W (priors, orientation) |
| **R4 description-level / representational** | 5, 11, 12, 18 | PG §3.12 quarantine (representational presence sources nothing); `stochasticChannel_kraus_monomial`; Clifford finiteness; CR when the realization map is a function of physical data | closed-K (quarantine, monomial induced action); closed-W (CR) for E2 and substratum-sourced purification |
| **R5 imported or postulated** | 16, 17, E1-T | E0 exclusion (MEMO §2.4), G3 FAIL for C5/C6 | excluded by gate, not by a theorem |

H:203–205 lists E2 as "structurally able to avoid both a continuum and I5". Under the adopted A1 target that holds
only if E2's induced-operation map takes an uncountable non-substratum input: with a selection rule that is a
function of finite substratum data, CR gives a countable image. [W]

***

## 3. Chosen route: R2 with non-primary logarithms (stroboscopic interpolation)

**Why this route.** It is the one member of R1–R4 not excluded by a kernel theorem or an exact computation as
stated: XS C11/P4 and E4 (H:245–247) test only principal logarithms, and the kernel's ones-fixing results concern
gate flows (primary functions of the gates). XS AW-X5 states "the stroboscopic-time algebra is branch-independent and
ones-fixing"; its probe varies only arg(−1) ∈ {π, −π} (`probes/p4_ones_fixing_lie.py`, KNOB control). CTA:422–423
separates logarithms that are functions of P (R2-A) from generators acting inside degenerate eigenspaces,
H = H₀ + 2πK with [K, P] = 0 and K of integer spectrum (R2-B), and records R2-B as open. The F2 records do not cite
that split.

**Decision rule (fixed before computing).** The ones-fixing exclusion is branch-relative iff (a) a non-primary
logarithm L of a native bijection satisfies exp(L) = P exactly and (b) the Lie algebra of the 24 principal logarithms
plus L is not ones-fixing. It is branch-independent iff (b) fails for every tested K.

**Computation [EC]** — `probe/nonprimary.py`, Fractions over ℚ(√3)(i), `python3 -I -B`, two runs byte-identical
(sha256 of output `23dc753d…9224`, script `8e8bea17…f299`), 14/14 PASS:
- POS: the principal-log algebra of the 24 native pair bijections has real dimension 9 and is ones-fixing (an
  independent code path agreeing with XS P4's recorded value).
- NP1–NP3: K = |00⟩⟨00| commutes with CNOT, lies in its +1 eigenspace, is not a function of CNOT; L_np = L_p + 2πiK
  commutes with K, so exp(L_np) = CNOT·exp(2πiK) = CNOT exactly.
- NP4–NP6: U_np(1/2)² = CNOT = U_p(1/2)²; U_p(1/2) fixes the uniform ray, U_np(1/2) does not; U_np(1/2) is not a
  scalar multiple of a real matrix. It breaks `NonnegBounded`, the uniform-ray invariant and the reality invariant.
- NP7: principal logs plus L_np generate all of u(4) (dimension 16), not ones-fixing.
- NEG: K = J/4 (the uniform projector; also non-primary and admissible) leaves the algebra ones-fixing (dimension 10),
  so the test can return "ones-fixing" on a non-primary logarithm; the outcome depends on K.
- E0: exp(¼·2πi|00⟩⟨00|) = diag(i, 1, 1, 1), the quarter phase.
- IDN: for K = |+⟩⟨+| ⊗ I, exp(¼·2πiK) is non-monomial and its fourth power is I: a non-monomial flow that is a time
  interpolation of doing nothing.
- KNOB: K′ = |v⟩⟨v|, v = (|00⟩ + |01⟩)/√2, is admissible and gives a different half-period flow.

**Kernel cross-check [W from AT].** The witness of `continuous_extension_not_unique` (RegionLimit.lean:296) is
H₁ = `genTwoPi` = diag(2π, 0) on `Fin 2` (:232), a non-primary logarithm of the identity. By `flow_genTwoPi` (:251),
flow H₁ (1/4) = diag(−i, 1), a phase gate outside `PreservesNonneg` (conjugate of `phaseGate_not_preservesNonneg`
SubstratumInterfaceAudit.lean:559). The non-uniqueness the kernel records is the phase resource.

**Pressure test (§A.31), explicit steps.**
1. *Does the route supply a family?* Yes, at representation level: for each fixed L the set {exp(tL)} is uncountable;
   with a non-primary L it is non-monomial, non-ones-fixing and non-real (NP4–NP7).
2. *Is it available?* The integer-time constraint exp(L) = P does not select L. When P has a repeated eigenvalue
   (every native pair bijection except the 4-cycles, and the identity always), the admissible K form a continuum
   (KNOB), so the choice of L is a parameter fixed outside the substratum: a G7 knob unless a stated principle
   selects it.
3. *Unfixed logarithm.* Admitting every logarithm admits, as interpolations of the identity alone, the quarter phase
   (E0) and non-monomial mixing flows (IDN). The stroboscopic clause then constrains nothing at non-integer times; it
   is the flow or phase posited (E0, MEMO §2.4).
4. *Principal logarithm fixed.* Ones-fixing (POS); fails G4 (XS C11 [rec]).
5. *A selecting principle.* The only one in the corpus is CT3, a time-independent local generator (CTA:405–680).
   Its R2-B branch, where non-ones-fixing generators live, is obstructed at width 2 for the corpus rule at L = 5, 6
   and, for q = 2, at every L outside an explicit arithmetic set; width ≥ 3 is open (CTA:606–607, :676–678 [rec]).
   Locality does not exclude NP's K, which is supported on one pair. For the on-site control rules the static
   generator is a sum of on-site terms (CTA:375–376, :457–459); if each term is a primary logarithm of its on-site
   gate it fixes the product uniform vector [W, conditional]. A selecting principle would have to land in R2-B at
   width ≥ 3.
6. *Even with L selected, availability at non-integer t.* The operation at t ∉ ℤ has no implementing substratum
   process (row 6), so by CR it requires a (P2) violation: the continuous evolution of the description is prior to
   the substratum between updates (H N1, BORDERLINE).

**Verdict.** R2 with non-primary logarithms supplies representation, not availability. The route fails F2 at
G7/E0 (unfixed or unselected L) or at G4 (principal L); the open case is a CT3-R2B selection, which would still
need a (P2) violation for availability. The ones-fixing exclusion recorded for stroboscopic time (XS C11, AW-X5;
H:245–247) is relative to the primary-logarithm choice; the exclusion of the route survives, on different grounds.

***

## 4. Hidden-assumption watch

| # | assumption the obstruction relies on | citation | class | finding |
|---|---|---|---|---|
| HA1 | operations supervene on finite substratum processes plus countable context (P2) | `realized_of_instAvail` ImplementationLocality.lean:530; `obsTheory_eq_permTheory` SubstratumInterfaceAudit.lean:774 | theorem for the present architecture [AT]; a posit (c) for extensions | load-bearing for every countability exclusion: CR shows A1 is unreachable under it whatever the time model. Any O-A source must give it up or give up (P1) |
| HA2 | availability is generated by finite protocols over a countable class | `finite_protocol_available` BridgeFiniteProtocol.lean:236; `genM_countable` StateMixingCoupling.lean:560 | theorem for the present architecture [AT]; definitional for `InstAvail` | relaxing it to limit closure is R1 (A1, XS R5); not a hidden escape |
| HA3 | time is discrete at the observer level | Main.md:268; GR.md:292 | not used | CR does not need it: a time-indexed family of bijections of a finite set has finite range [W]. Continuous time helps only by assigning operations to non-integer times without a process (HA1) |
| HA4 | the logarithm in stroboscopic interpolation is primary (principal up to arg(−1)) | XS P4 probe, AW-X5; H:172, :245–247 | unstated in the F2 records; CTA:422–423 states the split | **exposed**: non-primary logarithms break the uniform-ray, reality and nonnegativity invariants (§3 [EC]); the kernel's own non-uniqueness witness is one (`genTwoPi`) |
| HA5 | the observer's operations lie in the closure of `permClass` | OI-3 (LG §2.0); `obsTheory_eq_permTheory` | posit (c) of the stated interface | the barrier theorems are about this class; CR extends the conclusion to any supervenient realization map, so enlarging the class by substratum-realized operations does not help |
| HA6 | a fixed hidden prior, not an observer-controlled one | Main.md:60 | posit (c) | even an observer-controlled real prior enters through convex weights, which keep `NonnegBounded` [W] |
| HA7 | the frame group O(3,1) acting continuously on apparatus | Main.md:644–658 | emergent; lattice orientation fixed | rotations by every real angle are not operations on a lattice apparatus [W]; no exact continuous symmetry is available to the observer |
| HA8 | purification-sourced reversibles are uncountable | XS next step (REPORT:147) | open | if sourced from substratum processes, CR makes the purifier's reversible group countable; OP-strong with an uncountable group cannot come from the substratum alone [W] |

Assumption-watch markers for propagation:
- **AW-OA1.** Under A1 and OI-1, every O-A source is non-supervenient or enlarges the substratum (CR). A candidate
  claiming an OI-internal source of O-A should say which premise of CR it gives up.
- **AW-OA2.** "Branch" in stroboscopic-time records means arg(−1) only. A statement fixing T must fix the full
  logarithm (including K in degenerate eigenspaces), or it admits E0 through interpolations of the identity.
- **AW-OA3.** H:203–205's "E2 may avoid a continuum" predates A1's adoption; under A1 it needs an uncountable
  non-substratum input to the selection.

***

## 5. Not verified

- CR is [W]; its use of `countable_not_pairFlowSourced` is at `Fin 2` only, which suffices for ¬QM at that carrier.
  Not formalized.
- That nonnegativity, ones-fixing and reality are closed under norm limits and under convex combinations is [W]
  (H:42 also marks the ones-fixing case as not a kernel theorem).
- The probe covers the pair carrier (4 configurations) only. It does not test the substratum's own update U_φ or the
  Weil carrier of E1, and does not test locality of K beyond the pair.
- XS P4 was not re-run; POS reproduces its recorded dimension with independent code.
- CTA's CT3-R2B status (width 2 obstructed at the volumes recorded; width ≥ 3 open) is taken as recorded and not
  re-derived. Whether a width ≥ 3 R2-B generator, if one exists, fixes the uniform ray is not examined.
- H, I, XS and SC rows marked [rec] were taken as recorded. Issue #865 was read through the GitHub API (body only).
- Incidental, not a finding about O-A: the "selectable local coupling" sentence quoted by H as GR.md:258 is at
  GR.md:260 on `main`.

***

## 6. Productivity verdict

- **Gem.** Two facts strictly stronger than "the corpus has no source for O-A":
  1. CR: under A1 and OI-1, no supervenient source exists, whatever the time model, couplings, contexts, priors or
     capacity. A source must violate supervenience or OI-1 finiteness/bijectivity. This constrains where one could
     come from: non-integer-time operations with no implementing process (the E1-T shape) or an enlarged substratum.
  2. A hidden assumption in a recorded obstruction: the ones-fixing exclusion of stroboscopic time (XS C11, AW-X5;
     H E4) holds for primary logarithms only. Non-primary logarithms, exact at integer times, reach u(4) and break
     all three barrier invariants [EC]. The route stays excluded, by G7/E0 rather than by G4.
- **Classification: NEW.** HA4/AW-OA2 is not in the F2 records. CR is NEW in form; its counting core ELABORATES
  H:46–55 and `mixR_countable_upToScalar`. No route was opened. The obstruction to O-A stands, and its grounds are
  sharpened.

***

## Independent review outcome (supersedes the classification above)

Review: `probe/review/check.py` (the reviewer's independent SymPy recomputation, copied unchanged; output
`probe/review/check.out`). `probe/nonprimary.run2.out` is a second run, byte-identical to `run1`. The pre-review text is
not kept here; its sha256 is `22a9be748dfb313e6ce9742d960e35b7ce85b1945185286d8b81df4c0db8f460`.

- **Classification: ELABORATING with a CONFIRMING core. Not a gem under the fixed productivity test.**
- **CR, confirmed with corrections.** The logic is valid. P2 must cover every available level-1 conjugation channel
  (`hmem` of `countable_not_pairFlowSourced` quantifies over all V), not only unitary ones. P2 carries the content, and
  thread H:51–58 and LEDGER §5 item 1 already state the argument. The one addition sharpens H's "a real duration or a
  real coupling" clause: under P2 such parameters stay finite, so the only escapes are non-supervenience or an enlarged
  substratum. HA1 is retagged: for the present architecture P2 follows from `obsTheory_eq_permTheory`, where the
  conclusion is already `permTheory_not_qm`; `realized_of_instAvail` is soundness only. "No supervenient source exists"
  is [W] and holds only for P2 as defined.
- **Logarithm choice, mathematics confirmed; "hidden" refuted.** The exact claims recompute: dim 9 and ones-fixing
  for primary logarithms under every arg(−1) choice tested; [L_p, |00⟩⟨00|] = 0, so exp(L_p + 2πi|00⟩⟨00|) = CNOT
  exactly; dim 16 with L added; dim 10 with K = J/4. Adding L is the same as adding the local phase generator, which is
  x-screen P4's own positive control. The choice is not unstated: XS C11 says "principal logs", thread H:172 already
  requires the branch to be fixed in T's statement, GR.md:84 and CTA:419–424 record the freedom. What remains is a
  wording correction: AW-X5's "branch-independent" is broader than its probe (only arg(−1) is varied), and the F2
  records do not cite CTA's R2-A/R2-B split.
- **Correction to §3/§6:** the principal half-period flow already breaks NonnegBounded and reality
  (`gateFlow_half_not_preservesDiag`); only the uniform ray separates the non-primary choice. "Breaks all three" is
  replaced by "leaves the uniform ray".
