# Excerpts of off-main sources cited by this screen

Each block is a verbatim copy of the stated lines of one file at one commit; nothing else of that file is copied, so
the excerpts are not byte-identical to their originals. The blob id and sha256 identify the full original, and
`git show <commit>:<path> | sed -n '<a>,<b>p'` reproduces each block, whose own sha256 is stated with it.

## 1. F2 decision memo

`verification/programmes/oi-qm/reconstruction/research-planning/f2-decision-memo.md` at `acfef447c1ccef6415502bd33a6fc89fcce32bd2`: blob `5448440d2368a36fb238a3bf70c041fa6688b6c0`, sha256 `90ecbae0d71fb849241dd771ef7aece6da471fd31c54fa1b6f32278e6c64e444`, 433 lines.

The owner adopted §1's target (A1 exact, B1 qubit-power registers), §2's criterion with gates G1–G8 as written in §2.3, §3.2's M1 and §4's scope on 2026-10-17 (lines 13–18). This screen applies those criteria as written. The memo is a research specification, not a physical proof: its [WA] entries are written arguments and its [CD] entries (#829, #831) are compiled designs, not adopted theorems. Lines 26–64 resolve the evidence tags and citation abbreviations used in the other blocks.

Lines 13–18 (sha256 of the block's lines, each ending in a newline: `cb665f5b9b6c4044555161ce978f70ec6a34027eb1b11a60b52e6a0fabbd5772`):

~~~~text
**Decision status.** The owner adopted the four recommended choices on 2026-10-17, explicitly and choice by choice:
- §1 target: A1 exact, B1 qubit-power registers (F2-reg); F2-fin stays the named later obligation Γ11;
- §2 the strict extension criterion, with gates G1–G8 fixed exactly as written in §2.3;
- §3.2 M1: the monitored law must survive on the retained original protocols only;
- §4 the narrowed necessity scope: N1 and N3′; N2 (B24) stays open.

~~~~

Lines 26–64 (sha256 of the block's lines, each ending in a newline: `8231c6004c2209f912272e88d128dc8d1a2a44891f72e8dd1584c83622047ec6`):

~~~~text

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
~~~~

Lines 96–131 (sha256 of the block's lines, each ending in a newline: `3e5af928a9f27434cf74eddbb2ef66159f023d55e7c18eb47520bcf3d997f39e`):

~~~~text
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
~~~~

Lines 133–211 (sha256 of the block's lines, each ending in a newline: `2b72f75a470854361aeacf94085ba1c9e37e1819657854d12e8b1eb44a49e4da`):

~~~~text
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
~~~~

Lines 240–284 (sha256 of the block's lines, each ending in a newline: `148999e5bc97ffdcff55a438322af56c898ab25330f4080937b74e982275f0f4`):

~~~~text
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
~~~~

## 2. Thread H

`verification/programmes/oi-qm/reconstruction/f2-research-threads/H-extension-candidates.md` at `804843f16b67061ac258ce00cefa2425d1b688c2`: blob `f742c15edc7792dc41070a7a4a72a685e1c11fbb`, sha256 `1ec01c3be773901cc6ff05fc93c9d6e251164ba6fa7ec0f50c8caee9ce5d2db5`, 451 lines.

Ledger row S15 of `mi-plus/PREREG.md` cites these lines. Their [N P6] marks are thread H's floating-point probes, which this screen neither reproduces nor uses; the monitored-law failure S15 relies on is check B, replayed here.

Lines 114–124 (sha256 of the block's lines, each ending in a newline: `5e75368d6c29fd1bd9774af22fe5dfe2733011180e3776e548717236cb5cb415`):

~~~~text
**(c) Measurements and compatibility.**

- **Tests.** Registration is the native test. A test in another basis is an available unitary followed
  by registration. Validity holds by construction: Born weights of positive descriptions.
- **Registration must be symplectic.** It has to have back-action on the previous component of the
  registered site. The interface's bare read-write copy (`permClass_readWrite`,
  SubstratumInterfaceAudit.lean:412) has no Weil image [N P6.a]. It also keeps a full memory of the
  previous registration, which R forbids [N P6.c]. With a symplectic embedded meter, the two-time law
  coincides with Born statistics [N P6.b].
- **Compatibility.** Operations are conjugations on the same description space, so `PairCompat` holds
  for K = the PSD cone of the registered carrier, and H-CAR is R's tensor product over sites. Both come
~~~~

Lines 416–417 (sha256 of the block's lines, each ending in a newline: `bb6ee01a99cd15f71621c67e8f2e21063fc6b7c4702a61af580da1338fbb26a3`):

~~~~text
- **AW-H5.** The interface's non-disturbing read-write copy is incompatible with any Weil-covariant
  registration (P6). This bears on how C4 readback is modelled under an extension.
~~~~

## 3. Premise memo

`verification/programmes/oi-qm/reconstruction/research-planning/x-screen-20261018/premise-memo/PREMISE-MEMO.md` at `641ae1616752204b311b3f8cbd9e01a5e5f9c7ce`: blob `a6cdcd597950203271b3a36940d84b3852312661`, sha256 `0b663aa4f42f1988cd51dc9bb25271a5e161a2cfcd492eb3f71675345af78266`, 507 lines.

`source-search-20261020/` cites these items: F-α, F-β, F-γ, rows CH and SET, the §4 convention and U1–U3. Its §6(c) (lines 437–443) is quoted in full at `source-search-20261020/SOURCE-CHECKPOINT.md`:143–151 and is not repeated. Each excerpted line stands verbatim, 19 lines later, in the corrected version of the same file, blob `f5cee16980423afe58e5e3c6963f72d6ad042cb5` at `e5c87a25ef149a6c30b68b6b473525902443b2e0`; the lines corrected there are not excerpted.

Lines 77–90 (sha256 of the block's lines, each ending in a newline: `f4d293eb9af52754ac1541d12d7fe31cf56b43326f367782befa73073e46d49e`):

~~~~text
- **F-α.** Native statistics depend only on diagonals across `InstAvail permClass`. This is
  `realized_of_instAvail` (ImplementationLocality.lean:530) [AT] together with the trace identity of MI+ N3 [W, EC rec].
  Every domain cone has the classical diagonal set, and Γ fixes every diagonal.
- **F-β.** Γ(Q3) is invariant under every local unitary, native or not, continuous or not:
  Ad(U⊗V)∘Γ = Γ∘Ad(U⊗V̄) [W]. The set of token effects is closed under f ↦ fᵀ (the ball's y-reflection). So
  any clause over K's order, classical realization, native statistics, all local operations, or the product-test
  family taken as a set holds on Γ(Q3) iff it holds on Q3. Sources: review §1.4 and memo Fact B [W, EC rec].
- **F-γ.** On product tests Γ acts as a mirror reflection of token 2's ball (det −1; op-fork control C5 [EC rec]).
  It flips the sign of det T_X. The Γ ambiguity is therefore the relative orientation of the two token frames,
  which is visible only in joint coherences [W, new].
  - [EC, dc]: T(B) = diag(1, −1, 1), T(Γ(B)) = I and T(singlet) = −I.
  - The four K(Z_F) defects z = I/2 − P_m have orthogonal T with det +1, while each P_m has det −1. The K(Z_F)
    defects carry the same orientation defect as Γ(Q3), consistent with AW-X7 ("Γ-images of four entangled
    stabilizer projectors"). §A.31 class: ELABORATING (it extends AW-X7 and review §1.4).
~~~~

Line 138 (sha256 of the block's lines, each ending in a newline: `4cfb63669537bfea2dc25cafabd569fc5f9ca5bee952bd4caaefd4f8b7258ef1`):

~~~~text
| CH | **Correlation chirality.** No physical pair state has a perfect co-oriented correlation: T_X orthogonal ⇒ det T_X = −1, read from fixed product tests whose cross-token identification is native SWAP transport | (i) | uses no operation; on the domain it is equivalent to K ∩ Γ(ME) = ∅ [W, new], where ME is the maximally entangled pure states | [U]; no OI source; constructed knowing the target |
~~~~

Line 140 (sha256 of the block's lines, each ending in a newline: `542c4e9e1317a6ff25a59fcf7d55d2ca6d8dca0c458ff02882ff0b5e8f041e6c`):

~~~~text
| SET | set-level correlation bounds over all product tests (Tsirelson- or IC-type) | (i) | [I] | [U]; Γ-invariant by F-β |
~~~~

Lines 279–283 (sha256 of the block's lines, each ending in a newline: `9f1b9cab45e522e430660cbf093cdb7b7c382119ed9ad4f979278369ed89789e`):

~~~~text
- SP⊕UPD inherits UPD's use. The CPK row records that its exclusions need PSD imported (D3).

Apart from these rows, no entry uses PSD or CP of a competing cone's elements. Entries that use K_B ⊆ Q3 or L ⊆ Q3
concern a cone's fixed membership, not an import.

~~~~

Lines 469–480 (sha256 of the block's lines, each ending in a newline: `166e3df2ae97db4a3aaeca60339f866f4879abc006b0afbf007222013cf1c20e`):

~~~~text
## 7. Unsourced and unresolved obligations

1. U1: H-CAR. Physical pair descriptions transform by the native conjugation (EA) [U].
2. U2: the source of UPD. The coherent update beyond the diagonal sector [U] (Main.md:632).
3. U3: the classification of UPD. Under the present F2 rules it is a transfer clause on its state-side reading, class
   (iii) (§2). Open [U]:
   - whether a disguise criterion frozen in advance, with no built-in outcome, classifies any statement of UPD's
     content otherwise;
   - whether the restriction to native protocols can be fixed other than as a knob, given that UPD with local
     unitaries admitted is K ⊆ Q3 (§3.2);
   - OVr's class, whose basis is UPD's;
   - the reading of the other class-(i) rows against the transfer-clause form (§2).
~~~~
