# F2 target, extension criterion and necessity scope: decision memo

## How to read this memo

**What it covers.** This memo answers the first review milestone of the planning note
[`f2-target-extension-scope.md`](f2-target-extension-scope.md) (:48–53). That milestone has five parts: (a) target
statement, (b) extension criterion, (c) preserved-law checklist, (d) necessity scope, (e) dependency order.

**What it does not do.** It is research planning. It adopts no physical extension X, designates no F, and changes no
theorem, manuscript, ROADMAP or programme classification. It is consistency-axis work and moves no correctness band
(§A.23).

**Decision status.** The owner adopted the four recommended choices on 2026-10-17, explicitly and choice by choice:
- §1 target: A1 exact, B1 qubit-power registers (F2-reg); F2-fin stays the named later obligation Γ11;
- §2 the strict extension criterion, with gates G1–G8 fixed exactly as written in §2.3;
- §3.2 M1: the monitored law must survive on the retained original protocols only;
- §4 the narrowed necessity scope: N1 and N3′; N2 (B24) stays open.

These fix the criteria a candidate X is screened against. No X is adopted, and no screening result exists yet. The
items in §6 stay open.

**Base.** main `b96662e6`. The F2 research text is cited at `804843f1`.
- #857 shows as merged at `804843f1` because the research branch `research/f2-extension-candidates-20261014` was
  fast-forwarded to exactly that commit.
- That fast-forward is why GitHub reports the PR as merged. No merge into main occurred.

**Evidence classes.** Every entry below carries one tag. Where an entry is a decision rather than a claim, it is tagged
as a decision.

| tag | meaning |
|---|---|
| **[AT]** | adopted theorem: a kernel declaration on main `b96662e6` |
| **[CD]** | compiled design: built green on a named design run, not adopted |
| **[WA]** | written argument |
| **[EC]** | exact computation: replayable, with exact arithmetic |
| **[UP]** | unsourced premise: assumed, introduced, or an external postulate |
| [NUM] | numerical float evidence. This is none of the five classes and is never evidence of exactness |
| **DEC-OPEN** | an owner decision not yet taken |
| **DEC-ADOPTED (owner, 2026-10-17)** | adopted by the owner explicitly, choice by choice, on that date |
| **recommended (owner), open** | the owner has recommended it but not adopted it |

**Citation abbreviations.**

| short | object |
|---|---|
| RM | [`verification/ROADMAP.md`](https://github.com/amaybaum/incompleteness/blob/b96662e6be4f537502c772db369ea32a35b213a8/verification/ROADMAP.md) @ `b96662e6` |
| PG | [`verification/programmes/oi-qm/PROGRAMME.md`](https://github.com/amaybaum/incompleteness/blob/b96662e6be4f537502c772db369ea32a35b213a8/verification/programmes/oi-qm/PROGRAMME.md) @ `b96662e6` |
| AG | [`AGENTS.md`](https://github.com/amaybaum/incompleteness/blob/b96662e6be4f537502c772db369ea32a35b213a8/AGENTS.md) @ `b96662e6` |
| SM | [`papers/SM.md`](https://github.com/amaybaum/incompleteness/blob/b96662e6be4f537502c772db369ea32a35b213a8/papers/SM.md) @ `b96662e6` |
| H | [`…/f2-research-threads/H-extension-candidates.md`](https://github.com/amaybaum/incompleteness/blob/804843f16b67061ac258ce00cefa2425d1b688c2/verification/programmes/oi-qm/reconstruction/f2-research-threads/H-extension-candidates.md) @ `804843f1` |
| I | [`…/f2-research-threads/I-f2-sufficiency-target.md`](https://github.com/amaybaum/incompleteness/blob/804843f16b67061ac258ce00cefa2425d1b688c2/verification/programmes/oi-qm/reconstruction/f2-research-threads/I-f2-sufficiency-target.md) @ `804843f1` |
| F25 | [`…/f2-5-operational-dictionary/RESULT.md`](https://github.com/amaybaum/incompleteness/blob/804843f16b67061ac258ce00cefa2425d1b688c2/verification/programmes/oi-qm/reconstruction/f2-5-operational-dictionary/RESULT.md) @ `804843f1` |
| CB | [`…/f2-census-checks/monitored_law.py`](https://github.com/amaybaum/incompleteness/blob/804843f16b67061ac258ce00cefa2425d1b688c2/verification/programmes/oi-qm/reconstruction/f2-census-checks/monitored_law.py) / [`.out`](https://github.com/amaybaum/incompleteness/blob/804843f16b67061ac258ce00cefa2425d1b688c2/verification/programmes/oi-qm/reconstruction/f2-census-checks/monitored_law.out) @ `804843f1` (check B) |
| CRIT | [`…/physical-state-operation-compatibility/preregistration.md`](https://github.com/amaybaum/incompleteness/blob/1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37/verification/programmes/oi-qm/reconstruction/physical-state-operation-compatibility/preregistration.md) @ `1d4606b2` (#820) |
| SA | [`…/bridge-compatibility-audit/source-assessment.md`](https://github.com/amaybaum/incompleteness/blob/1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37/verification/programmes/oi-qm/reconstruction/bridge-compatibility-audit/source-assessment.md) @ `1d4606b2` |
| BCR | [`…/bridge-compatibility-audit/result.md`](https://github.com/amaybaum/incompleteness/blob/1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37/verification/programmes/oi-qm/reconstruction/bridge-compatibility-audit/result.md) @ `1d4606b2` |
| SPR, SPN | [`…/spectrality-preservation-research/result.md`](https://github.com/amaybaum/incompleteness/blob/f48b11fddbbfd7eea1185518210becf75b49e8e2/verification/programmes/oi-qm/reconstruction/spectrality-preservation-research/result.md), [`…/next-result.md`](https://github.com/amaybaum/incompleteness/blob/f48b11fddbbfd7eea1185518210becf75b49e8e2/verification/programmes/oi-qm/reconstruction/spectrality-preservation-research/next-result.md) @ #832 `f48b11fd` |
| R6 | [`research/round6-transfer/RESULTS.md`](https://github.com/amaybaum/incompleteness/blob/694219a43bc9af449784c2b4dbc5b38b44df96a2/research/round6-transfer/RESULTS.md) @ `694219a4` |
| OV | `research/OVERVIEW.md` on `research/overview` @ `8b95068a` |
| BL | [`research/bridge/LOG.md`](https://github.com/amaybaum/incompleteness/blob/029cb5e0e55049016504a6380fba6d6651262001/research/bridge/LOG.md) @ `029cb5e0` |
| P829, P831, P822 | the preregistrations at `625f853f`, `65b85147`, `90c72640` |
| N833, N836 | the planning notes `physical-drive-source.md` (#833 `9fc5ec2e`) and `joint-test-validity-source.md` (#836 `0e0b3ddc`) |

`…` stands for `verification/programmes/oi-qm/reconstruction`. Lean paths are under `verification/lean-mathlib/OIBridge/`.

***

## 0. Summary of the recommendations

**(a) Target.**
- Recommended: **exact finite QM on qubit-power registers (F2-reg)**.
- All finite local dimensions (F2-fin) stays a named later obligation.
- A dense endpoint is admissible only if it is defined *before* any candidate is screened.
- Status: DEC-ADOPTED (owner, 2026-10-17).

**(b) Extension criterion.** The strict criterion and the gates G1–G8 of §2.3, as written: DEC-ADOPTED (owner, 2026-10-17).
- An equivalence with cone selection is allowed.
- Renaming preservation, or defining states or operations so as to obtain it, is not.

**(c) Preserved laws.** Three laws are checked separately: rooted, monitored and back-acting.
- Recommended: the monitored law must survive on the **retained original protocols only**.
- The laws of new protocols are stated as predictions.
- Status: DEC-ADOPTED (owner, 2026-10-17).

**(d) Necessity.** The narrowed scope: DEC-ADOPTED (owner, 2026-10-17). It covers holds-in-QM and drop-one checks only.
- Global minimality is not established.
- Independence from the complete OI framework is not established.
- B24 is kept only in re-posed form, after X is fixed.

**(e) Order.** #829 → #831 → #822 for kernel landings.
- #836, #833 and #832 are parallel source investigations, each gated on (b).
- Compatibility, carrier identification and test availability stay three separate obligations.

***

## 1. (a) The target statement

The F2 row requires "finite operational quantum mechanics: normalized probabilities, available tests tied to the stage
data, and arbitrary finite composites" (RM:1130–1132). Thread I's single target is F2-fin(X):
`OIStated ∧ Origin ∧ X ∧ Res ⇒ QMfin` (I:45–52) [WA]. Its conclusion is fixed by clauses (T1)–(T6) and (Corr)
(I:124–132) [WA].

### 1.1 Exact or dense

| option | content | consequence | evidence |
|---|---|---|---|
| **A1 exact** | `QMfin`: `ShadowQuantum` (TypedCompletion.lean:291), characterized by `typed_determined_iff` (:850) | Any X whose operations form a countable set fails. So X must name an uncountable resource, such as a real duration or a real coupling | The endpoint objects are [AT]. Countable sets fail: `mixTheoryR_not_qm` StateMixingCoupling.lean:679, `countable_not_pairFlowSourced` PairFlowEquivalence.lean:218, `fixedGateTheory_not_qm` DiscreteCompletion.lean:1948, `uncountable_of_layerFlowExecutable` PolarizationClosure.lean:135 [AT]. Substratum-sourced maps are countable: H:46–55 [WA]. Summary at I:513–518 [WA] |
| **A2 dense** | (T5) "onto a dense subset", plus a density endpoint (I:141–143) | A countable X becomes admissible | A density endpoint exists only on `Fin 2`: `DenseFiniteQM` DiscreteCompletion.lean:59 and `fixedGateTheory_denseFiniteQM` DenseInstrumentBridge.lean:521 [AT]. No endpoint is defined on all carriers (I:543–544) [WA]; it would have to be defined first |

**Recommendation: A1, exact (DEC-ADOPTED (owner, 2026-10-17)).**
- **It gives the sharpest kill criterion.** A countable X fails A1 by an adopted theorem, not by judgement.
- **A2 sits too close to excluded ground.** It admits "one irrational fixed gate" candidates, which are close to the
  excluded "gate as a premise" reading (H:273–278).
- **A2 would need an endpoint built first.** That endpoint must be defined and fixed before any screening. PG:513
  requires the endpoint to be decidable in advance.
- **If the owner chooses A2,** the definition comes first: which instruments, which carriers, and which topology.

### 1.2 Qubit-power registers or all finite local dimensions

| option | content | consequence | evidence |
|---|---|---|---|
| **B1 F2-reg** | (T6) restricted to local dimension 2^k (I:131); drops H26 and Γ11 (I:545) | Composites of the elementary system are covered. Other dimensions are excluded from the claim's wording | The elementary system is the d = 3 ball: the selector under K1 is CONDITIONAL (RM:68). The pair theorem is [AT] (EqvK2MaxCone.lean:153, :174). The k-token theorem is [CD] (#829's design run, see §5). Descent on the operation side: KN-DESC (#823) [CD] |
| **B2 F2-fin** | every nonempty finite cardinality (I:131) | Needs a subspace principle (types as compressions of registers) or cone families beyond qubit powers | Γ11 "local dimensions ≠ 2^k as types": no evidence exists (I:410) [WA]; L10 is open |

**Recommendation: B1, F2-reg first, with B2 kept as the named later obligation Γ11 (DEC-ADOPTED (owner, 2026-10-17)).**
- **Wording.** Results are worded "qubit-power registers", never "finite QM".
- **Interaction with candidates.** E1-type candidates have odd-prime local dimension and do not supply other
  dimensions (F25:181 [WA]; H:349–351 [WA]). So the choice of target constrains which candidates make sense, and it
  must be fixed before screening.

***

## 2. (b) The extension criterion (strict: DEC-ADOPTED (owner, 2026-10-17))

### 2.1 Three obligations, kept separate (planning note :26–27)

| obligation | what must be supplied | present evidence |
|---|---|---|
| **compatibility** | Physical states are preserved by the physical operations. Thread I's names are H-COMPAT and `PairCompat` (X-4); OI's are (T)/(T^ch) and A_miss | No derivation from the inventory: R6:9–10, :14, :16 [WA]. Availability does not imply preservation: BCR:7–12, :57–67 [EC] and [WA]. Conditional induction from primitive operations to protocols: #831 [CD]. Status: [UP] |
| **carrier identification** | The physical system's state space is identified with the carrier the theorems use. This is `Origin` and `StageIso`, H-CAR, H0 and H27 (I:189–196, Γ13 I:412) | No predicates exist (I:412) [WA]. Under the K route the carriers are premises of #829 and the pair theorem. Status: [UP] |
| **test availability and validity** | Tests are identified, available and valid on the physical pair, without assuming the quantum conclusion (#836, N836:9–20). This is X-5 / H22v and H11b | Sharp tests: `SharpTests.lean` [AT]; `sharpFamily_subset_avail` EffectSpace.lean:374 and `avail_eq_fullEffects` :727 [AT], both on the single ball. On the pair: Γ7 and Γ9 (I:406, :408) [CD]/[WA]. Status: [UP] |

### 2.2 Two facts the gates rest on (revised)

**Fact A: an equivalence that is the reconstruction, not a circularity.**
- *The premises.* Retain products (H1), addition, nonnegative scaling and K ⊆ maxCone.
- *Pair case [AT].* Invariance of the cone under CNOT, the **full rotation flow** `actT (rotLin t)` for all t, **and**
  the **cyclic action** `actT cycEquiv` is equivalent to K = Q3. Witnesses: `pairCone_eq_Q3_iff_drive_maxCone`
  EqvK2MaxCone.lean:174, from `pairCone_eq_Q3_of_drive_maxCone` :153 and `driveInvariant_of_eq_Q3` :165.
- *k tokens [CD].* The same holds for K = QK k, with CNOTs into later tokens and `actK j (rotLin t)`, `actK j cycEquiv`
  off token 0 (P829:67–75; #829's design run).
- *How to read it.* Under the retained premises, selecting the quantum cone is *equivalent* to invariance under those
  three operation families. A physically meaningful principle may be equivalent to that selection; such an equivalence
  *is* the reconstruction result and is not circular by itself.
- *What is excluded.* A principle that merely renames the invariance, such as a bare transfer clause stating that these
  operations preserve physical states. It is excluded because it restates preservation, not because it is equivalent
  to the conclusion. So is a principle that *defines* states or operations so that invariance follows (CRIT:32–36,
  :136–141).

**Fact B (narrowed): the partial-transpose ambiguity.** Γ is the partial transpose on the second token.
- *Exact facts [EC]* ([`f2-decision-memo-factB_check.py`](f2-decision-memo-factB_check.py), run with `python3 -I`; it needs SymPy):
  - Γ(Bell) has eigenvalues {1/2, 1/2, 1/2, −1/2}, so the Bell projector lies outside Γ(Q3);
  - CNOT maps the element Γ(Bell) of Γ(Q3) outside Γ(Q3);
  - Γ maps a test product state to a product state.
- *Written argument [WA]:*
  - Γ preserves SEP and the maxCone window, provided the local tests are relabelled B ↦ Bᵀ;
  - it preserves normalization;
  - it preserves spectrality, because it is a trace-preserving order isomorphism;
  - it preserves self-duality, because Γ preserves the trace inner product, Tr(Γ(X)Γ(Y)) = Tr(XY). This is not a
    property of arbitrary order isomorphisms;
  - it carries local CP maps to local CP maps under the relabelling φ ↦ φ′, φ′(ρ) = φ(ρᵀ)ᵀ;
  - SPN:44–47 and SPN:189–195 give the same facts for this instance.
- *What follows [WA]:* any proposed principle that is invariant under Γ, *together with* the corresponding relabelling
  of local tests and local operations, cannot tell Q3 from Γ(Q3).
- *What this does not show:* that every principle about states fails.
- *The justified conclusion:* X must break this ambiguity *relative to the fixed physical identification of operations
  and tests*. Constraining how an entangling native operation acts on physical states is one route ("a source has to
  fix the state cone and the entangling operations together", H:71 [WA]). It is not proved to be the only route.

### 2.3 Gates, fixed as written (DEC-ADOPTED (owner, 2026-10-17))

| gate | requirement | sources |
|---|---|---|
| **G1 operational statement** | Stated in OI's own terms, at the observer/operational level. It does not list chosen matrices as members of 𝓘 | RM:1125; H:273–278; I:546–548 [WA] |
| **G2 explanation, not renaming** | (i) An independently meaningful physical statement, (ii) its own sourcing argument, and (iii) at least one consequence beyond compatibility (see G6). Being equivalent to cone selection under the retained premises is **permitted** (Fact A). **Rejected:** a principle that renames preservation (LO, DT, a bare transfer clause), or that obtains preservation by how it defines states or operations (reachable closure, `C = PSD` by fiat, PS-type saturation) | CRIT:91–146, :176–181; SA:41–59, :108–111 [WA] |
| **G3 breaks the Γ ambiguity** | X distinguishes Q3 from Γ(Q3) relative to the fixed identification of native operations and tests. Constraining an entangling operation is one route, not a required form | Fact B [EC]+[WA] |
| **G4 neither redundant nor contradictory** | Not derivable from OI's stated premises: the core of R_X must break `NonnegBounded` *and* the uniform-ray and reality invariants. It does not contradict an adopted theorem; a "replacement" interface fails here | `obsTheory_nonnegBounded` FrozenSourcing.lean:84 [AT]; I:264–282, :531–533 [WA]; F25:174 [WA] |
| **G5 controls, by kind** | Preservation, exclusion and positive controls are listed separately and fixed in advance (§3) | AG:32–35; CRIT:47–68, :166–175 |
| **G6 beyond the resource** | At least one independent prediction or postdiction, with its decision *rule* preregistered | RM:1127–1128; AG:21–35 |
| **G7 no knobs** | Every branch, parameter or frame is fixed in X's statement before testing: logarithm branch, alphabet, prior | H:168–173 [WA] |
| **G8 target fixed first** | §1's choices (A1/A2, B1/B2) are fixed before any screening | PG:513; I:513–518 [WA] |

The F2 row names the K route as the assembly route (Origin_K, RM:1131–1132), so **compatibility (X-4) and test validity (X-5) are substantive
obligations**, not consequences (I:527–530 [WA]).

### 2.4 Readings already failed or open

| reading | outcome | evidence |
|---|---|---|
| the gate, flow or phase as a premise (E0) | excluded: states the resource without sourcing it | H:273–278 [WA]; RM:1128–1129 |
| LC, rank-one filter/readout consistency | too weak | SA:15–32 [WA]; fixture separators −1/4 and −1/16 [EC] |
| LO, local operations preserve states | renames preservation (G2) | SA:34–46 [WA] |
| DT, dual-test closure | dual restatement of preservation (G2) | SA:48–59 [WA] |
| PS, product-test saturation | quantum inclusion it has not earned | SA:61–67 [WA] |
| H-OI_g / H-T | assumed; fails the disguise test | OV:150–151, :161–162 [WA]; status [UP] |
| (T)/(T^ch) derived from the inventory | no derivation | R6:9–10 [WA] |
| availability ⇒ preservation | false | BCR:57–67 [EC] |
| E3 (R alone), E4 (T alone), E5, E6 | fail the barrier invariants | H:220–271 [WA]; E4's flow facts `gateFlow_half_not_preservesDiag` LiftAudit.lean:155 [AT]; P-probes [NUM] |
| E1-L (R ⊕ T) | fails G4: not a conservative extension (F25:174 [WA]; exclusions F25:168–172, [EC] at q = 3). Fails the monitored-law control on retained protocols (CB [EC], q = 3, N = 1). T's status as "control by another name" is BORDERLINE (H:301–313 [WA]) | — |
| SP on the tilted-coPSD family | holds, and that family preserves every Φ_k; SP adds nothing to the classification | SPN:37–53 [WA] + [EC] certificates |
| SP on centrally symmetric bases | excluded from the native product domain | #832 body [WA] |
| SP in general ⇒ local preservation by Φ_k | OPEN | SPR:3–4, :132–139 [WA]; SP itself is an external postulate [UP] (SPN:27–31) |

One correction concerns thread H's q-gauge objection (H:163–164, :323–326; AW-H6 :418–419).
- **What it cited.** It quoted SM as of `5bfdaba6` ("no prediction depends on q").
- **What main says now.** SM.md:90–92 explicitly allows results that depend on q. SM.md:94 treats full alphabet
  independence as the *alphabet-size hypothesis*, "not proved for every observable" [WA].
- **The objection needs revision.** "Contradicts SM's q gauge" no longer holds.
- **The specific q = 2 findings stand as separate findings.** These are the failure of `H·S²·H = X` against the visible
  law (P1.d [EC]), the exhaustive failure of layer images (P1.f [NUM]), and probe_H2 [NUM] (H:150–157, :429–431).

### 2.5 What #832's spectrality screen tests under these gates

The screen asks one narrow, decidable question: on the common domain SEP ⊆ C ⊆ maxCone, does SP entail preservation by
the uniformly guaranteed *local* stopped maps Φ_k? The J-conjugate clause is a separate question (SPR:132–139;
CRIT:120–128).

- **The screen cannot settle G3.** Γ(Q3) satisfies SP and fails CNOT [EC]+[WA], so even a positive general theorem
  makes SP at most a component of X.
- **What a positive result still needs:**
  - an OI-level source (G2 (ii));
  - a G6 consequence;
  - the disguise audit of the full third-axis flow it would entail (SPR:136–138);
  - §A.31 maximum skepticism (AG:335).
- **A negative result** is a common-domain SP cone that breaks Φ_1. SP is then labelled INSUFFICIENT (CRIT:180–181).
- **Suggested re-posing.** Pose the screen against #831's primitive list (P831:74–88) as well as against Φ_k.

***

## 3. (c) The preserved-law checklist (G5)

### 3.1 Three laws, never interchangeable

In each case X's new law must equal the OI law on the scope chosen in §3.2. A match on one law never counts for
another.

| law | definition | status of existing candidates |
|---|---|---|
| **rooted** | P(x_t \| x₀) for a registered start, with the hidden half uniform and no intermediate reading (CB docstring; F2-1 RESULT:105) | E1 reproduces it at odd q: [EC] q = 3 in CB; [NUM] elsewhere (H P2.a) |
| **monitored** | OI's trajectory law P(x₀, x₁, x₂), with intermediate values read *without disturbance*. Kernel trajectory object `RevReal.traj` Equivalence.lean:174 [AT]; [Main] §3.4 class (D) | E1 fails it: all 27/27 entries differ, and x₂'s dependence on x₀ given x₁ is lost (CB.out [EC], q = 3, N = 1) |
| **back-acting** | The two-time law when the intermediate registration re-randomizes the hidden half, as with an embedded symplectic meter (CB "RR"; H:118–122) | E1's quantum law equals RR (CB.out [EC], q = 3, N = 1; P6.b [NUM]). An OI-side embedded-meter protocol realizing RR is not identified [UP] |

### 3.2 Where the monitored law must survive (M1: DEC-ADOPTED (owner, 2026-10-17))

| option | requirement | consequence |
|---|---|---|
| **M1 retained protocols only** | The original OI protocols, with OI's non-disturbing configuration readout (`readout_is_localLuders` OperationalAssembly.lean:658 [AT]), keep their monitored law inside the extended theory. New measurement protocols introduced by X carry their own laws, stated as predictions (G6) | Admits extensions that add disturbing measurements and keep the old readout. Excludes extensions that *remove* the non-disturbing readout (E1-L, F25:171) |
| **M2 also on new protocols** | Every measurement protocol of the extended theory reproduces the monitored law | Excludes every extension whose new tests disturb, which in effect excludes quantum measurement. It also imposes an unspecified requirement on every candidate |

**Recommendation: M1.** The back-acting law is then an obligation only where X claims that a new measurement *models* an
existing OI embedded-meter protocol. In that case it must match that protocol's OI law, and that protocol must first be
identified ([UP] at present).

### 3.3 The other controls, by kind (all to be fixed before any test)

**Preservation controls: X must leave each true.**
- The no-go for the unextended interface: `frozen_sourcing_verdict` FrozenSourcing.lean:318 and
  `obsTheory_nonnegBounded` :84 [AT].
- Finite-protocol availability: `finite_protocol_spectator` BridgeFiniteProtocol.lean:269 [AT].
- The pair theorem as a conditional statement: EqvK2MaxCone.lean:153–174 [AT].
- The rooted law, and the monitored law on the scope from §3.2.

**Exclusion controls: the complete extension X must itself exclude each.**
- The fixtures K_B and K(Z_F), each at a named clause, using uniformly available operations only (CRIT:47–68). K_B's
  depth-one witness is [EC]; K(Z_F)'s historical certificates keep their evidence levels.
- Γ(Q3), by G3 [EC]+[WA].

**Positive controls for the conditional mathematics: not targets of the extension.**
- Quantum PSD with ordinary instruments.
- The classical diagonal cone with monomial operations (CRIT:159–160, :171–175).
- The classical theory validates the conditional theorems and the interface. It is *not* required to satisfy the
  complete extension that selects QM, and a principle that excludes it is not thereby rejected.

***

## 4. (d) Necessity scope (narrowed: DEC-ADOPTED (owner, 2026-10-17))

### 4.1 Three questions, never merged

| question | meaning | what it does *not* show | present evidence |
|---|---|---|---|
| **N1 holds in QM** | each conjunct of X holds in QMfin under the identification; X is compatible with the target | neither necessity nor minimality | cone level: `driveInvariant_of_eq_Q3` :165 [AT]; `driveInvariantK_of_eq_QK` (P829:74) [CD]. Theory level: the `.mp` direction of `sourcedOI_qm_iff_phaseFree` SubstratumInterfaceAudit.lean:654 [AT] |
| **N3′ drop-one** | each conjunct is needed *relative to the remaining assumptions*: dropping it leaves an exact countermodel of the rest that fails QMfin | global minimality, and independence from the complete OI framework | relative to E1: R and T are each needed given the other (H:332–334) [WA]. Fixtures: K_B [EC], K(Z_F) [historical], Γ(Q3) [EC]+[WA], `permTheory_not_phaseFree` :711 [AT]. Uniform ray and reality: I:264–282 [WA] |
| **N2 full-model independence (B24)** | a model of the complete OI framework in which the clause fails | — | never started: deferred to round 7 and not run (BL:1233). "Independence from the complete OI framework is OPEN" (OV:149) |

**What F2 may claim.** Every clause below is conditional on the witness actually being obtained.
- "OI + X + Res ⇒ QMfin" (sufficiency).
- "Each conjunct of X holds in QMfin."
- "Each conjunct is needed relative to the others and to OI's kernel premises."
- "Global minimality and independence from the complete OI framework are open."

What it may not claim:
- The display is an implication. Never "iff", "minimal", "necessary and sufficient" or "characterizes" (§A.34,
  AG:555–576).
- Result notes quote PG:537 ("sufficiency first"), never PG:533 alone.

### 4.2 B24 re-posed (planning note :28–30)

- **The exact unfinished node.**
  - B24 is defined as "a full model satisfying the 68 NOT REACHED rows … in which (b) or (T) fails, or a precisely
    scoped OPEN" (OV:1209–1210).
  - Nothing was written: no S0, notes, script or run (BL:1233).
  - Its planned reliance on HO-43 item 2 uses H1–H3 (BL:1189–1191). That predates the adopted maxCone theorem, which
    needs no H3.
- **Re-posed form (recommended, run only once X is fixed).**
  - *Premise set:* main's kernel-stated OI, that is `OIStated` with the `permClass` interface (I:94–110, :157–158) [WA],
    plus the adopted finite-protocol results.
  - *The question, with the two readings kept apart:*
    - **availability:** the CNOT, rotation-flow and cyclic operations are not available physical operations. This is
      #833's question and K∞-Drive's.
    - **invariance:** they are available, yet do not preserve the physical cone. This is the content of the pair
      theorem's hH2 and hA (OV:99–104 [WA]).
  - The archive's 68-row inventory stays deferred: those rows are not main's premise set.

***

## 5. (e) Dependency order

### 5.1 What each PR carries

| PR | content | class | depends on | must keep explicit |
|---|---|---|---|---|
| **#829 KTOKEN-MAXCONE-1** | the *conditional characterization of the k-token cone*: given products, cone and maxCone, K = QK k ⟺ invariance under CNOTs into later tokens, the full rotation flow and the cyclic action, with one witness per direction (P829:67–76) | [CD]: workflow run 39043849411 (`workflow_dispatch`, `success`, head `1ab0fd9d`) | nothing in (a)–(d) | carrier, operation and compatibility premises (planning note :41). Review the run-2 materials before the final design run. Display the iff only with both witnesses and the product, cone and maxCone premises shown |
| **#831 PRESERVE-INDUCT-1** | primitive preservation ⇒ every `InstAvail` family preserves C (P831:74–100). No iff, no source (P831:111–112) | design build e684897d, run 38450187534 [CD]; reconstructed draft (P831:11–17) | becomes the specification for #832 under (b) | For 𝓘 ⊇ `permClass`, `PrimitivePreservation` contains CNOT preservation, so the theorem relocates compatibility and sources nothing [WA]. The primitive premises are [UP] (planning note :42) |
| **#822 KINF-COPY-1** | type covariance of native inversion suffices for DIM-1's selector (P822:45–57) | design runs [CD] (P822:61–63); relative form `RelativeGateTransport` run 38606561330 [CD] | none of (a)–(d) | integration of the relative gate with available tests, and its cone hypotheses (planning note :44). Narrows one of eight K∞ seams (RM:68) |
| **#832** | the spectrality screen (§2.5) | [WA] + [EC] certificates; SP [UP] | gates (b); #831's primitive list | acceptable class and source criterion (planning note :43) |
| **#833** | physical source of the drive (K∞-Drive) | planning only; status [UP] (N833:9) | gates (b); the target (a), since exact targets need a continuum | **a geometric flow is not physical availability.** `finiteOrderOn_of_stagePreserving` CompositionOrder.lean:348 [AT] constrains stage-preserving data; a source must handle crossing stages and not infer a flow from a finite update (N833:9–12) |
| **#836** | joint-test identification and validity | planning only; status [UP] (N836:9–12) | gates (b); carrier identification | **identify tests and their validity independently of the quantum conclusion.** No PSD or maxCone by definition; reject PS and DT (N836:19–26) |

### 5.2 Order

**Kernel landings: #829 → #831 → #822, serialized.** All three edit the same sites on main:
- `OIBridge.lean:268–269` (the last import is now `TurnpikePremiseOrientation`);
- the census tail at `lean-manuscript-census.json:1485–1494`;
- `verify.yml`: a new shard after `probes_bg2` (:443), and the aggregate lines :557, :577, :598 and :618.

Sources: the files on main at `b96662e6`, and the governed paths at P829:17–23, P831:25–33 and P822:17–24.

1. **#829 first.** It does not depend on any decision here and is the most advanced. It is not at F, so its drafting
   snapshot may still be re-cut.
2. **#831 second.** It becomes #832's specification.
3. **#822 last.** It does not depend on (a)–(d) and adds the least to F2. It also collides on `verify.yml` with #824
   and #830.

**Re-cut rule.**
- A round's drafting snapshot D may be re-cut only **before its F is designated**.
- Once frozen, a round follows its lifecycle. Later history enters only by reconciliation after E, resolved by merits
  (§A.39 item 3).
- So #831 and #822, neither of which is at F, may re-cut D after each preceding landing.
- A round already at F does not re-cut.

**Research streams: #836, #833 and #832, in parallel.** They are planning or research notes with no kernel collision.
- Each starts its decisive work only after (b)'s gates are fixed.
- #833 also waits on (a), the exact-or-dense choice.
- #832 waits on #831's primitive list.
- Each stays tied to its own obligation, from the three in §2.1.

***

## 6. Open items and housekeeping

- **DEC-ADOPTED (owner, 2026-10-17):** §1.1 A1, §1.2 B1, §2 the strict criterion with §2.3's gates as written, §3.2 M1, §4 the
  narrowed scope.
- **Recommended (owner), open.**
  - §4.2 B24: run the re-posed investigation after X and its premise set are fixed.
  - E1-L's standing on the research branch: describe it as a replacement-interface construction, outside the
    conservative-extension lane, and keep its scoped results. Its failure there does not exclude other extensions.
    H:78 still headlines it as "rank 1, recommended". The branch can record the new description forward without
    rewriting history.
- **Stale research index (F1 terminology), planning note :31–32.**
  - The research index `research/OVERVIEW.md` uses "F1" for the round-4 bridge finding: OV:80, :262, :276, :762, :777, :860, :881.
  - Main uses F1 for the retired equivalence endpoint (PG:515; RM:1538).
  - The index also predates F2 entirely; its last entry is OV:1242–1261.
  - It must not be used to prioritize or describe F2 until it is reviewed. This stays open.
- **Things that would let X be fitted to any outcome** (all excluded by the gates above):
  - choosing the set of transferred operations (G2);
  - dropping OI content per candidate (G4);
  - untested idle conjuncts (N3′);
  - choosing exact or dense, or Origin, after the results (G8);
  - unfixed branches or alphabet (G7);
  - reading a favourable SP result as "X found" (G3, §A.31).

***

## Appendix A: technical notes

**A.1 Fact A, the hypotheses in full** (P829:67–69; EqvK2MaxCone.lean:153–160):

| hypothesis | k-token form |
|---|---|
| H1 | `∀ x, (∀ i, x i ∈ eball 3) → prodStateK x ∈ K` |
| H2 | `∀ i < j, ∀ ω ∈ K, cnotK i j ω ∈ K` |
| A | `∀ j ≠ 0, ∀ t, ∀ ω ∈ K, actK j (rotLin t) ω ∈ K ∧ actK j cycEquiv ω ∈ K` |

Together with `hadd`, `hsmul` and `hmax : K ⊆ maxConeK (eball 3)`, these give `K = QK k ↔ H2 ∧ A`. In the pair case,
`hA` contains both the rotation flow and `cycEquiv`; the cyclic action is a separate premise and is never absorbed into
"the drive".

**A.2 Fact B, which parts are exact and which are written.**
- *[EC], the three parts in `factB_check.py`:*
  - Bell exclusion;
  - CNOT moving Γ(Bell) outside Γ(Q3);
  - Γ(product) is a PSD product.

  The script prints `{1/2: 3, -1/2: 1}` for both eigenvalue sets, and `True` for the product check.
- *[WA], everything else:*
  - Γ-invariance of SEP, of maxCone and of the product tests under B ↦ Bᵀ;
  - preservation of SP, from the order isomorphism;
  - preservation of self-duality, from Γ being a trace-inner-product isometry;
  - closure under local operations, through φ ↦ φ′.
- *The conclusion is scoped* to principles invariant under Γ together with the relabelling. It does not cover
  principles in general.

**A.3 Thread I map, as it bears on (a)–(e).**
- The obligation rows X-1…X-5 (I:210–221).
- The gap map Γ0–Γ14 (I:397–413). Γ1 is the cheapest step that does not depend on X (I:421–437); Γ10 is #829; Γ11 is
  B2; Γ13 is carrier identification; Γ14 is `X ⊢ R_X`.
- The owner items of I:539–548 are absorbed here: item 1 (Origin_K, as the F2 row states at RM:1131–1132; §2.3), item 2 (§1.1), item 3 (§1.2),
  item 4 (G1).

**A.4 Status.**
- *Rounds:* nothing here designates F or authorizes execution.
- *§A.42:* evidence for any later main-facing package must be retained under §A.42 (planning note :55–56).
