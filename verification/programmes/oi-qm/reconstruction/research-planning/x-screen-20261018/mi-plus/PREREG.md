# MI+ screen: native meter coupling and an observer-level update constraint — preregistration

Research only. No native round, no F or E, no merge, no adoption of any X, no status change, no full-equivalence
claim. This is consistency-axis work (§A.23). Parent: `../REPORT.md` S2 (MI) at `451f2590`, with G5 read in
D1's standalone sense (applied on the branch at `4c7d5c30`). Scope: owner decisions D1 and D2, PR #864, comment 6248203342
(2026-10-18T09:23:49Z).

**The question (D2).** Does OI's native read-write/meter coupling, together with a specifically named and
independently derived observer-level measurement/update constraint, entail a non-definitional restriction on coherent
joint states and operations stronger than `CNOT(ρ⊗|0⟩⟨0|) ∈ K`? Does it exclude K(Z_F) and Γ(Q3) under fixed tests
and native operations? It must do so without assuming PSD, without assuming closure under quantum instruments, and
without taking the needed compatibility as a definition.

**Tags.** [AT] is a kernel declaration on main `b96662e6`; every cited kernel file is unchanged at main `415fc868`
(drafting check X3). [CD] compiled design. [WA] written argument. [EC] exact computation, replayable, exact
arithmetic. [UP] unsourced: assumed, introduced or external. [MP] manuscript exhaustive probe. [L] literature.
[NUM] numerical; it is never evidence of exactness. Lean paths are under `verification/lean-mathlib/OIBridge/`.
`x-screen-20261018/` is under `verification/programmes/oi-qm/reconstruction/research-planning/`. Inside it, `../` and
`op-fork/` written from this file both denote paths in `x-screen-20261018/`.

## 0. Chronology and amendments

- **C_P, the preregistration commit.** This file is committed alone. That commit changes no other path, and in its
  tree `mi-plus/` contains this file and nothing else. No file under `mi-plus/probes/`, `mi-plus/runs/` or
  `mi-plus/check/` exists before C_P.
- **After C_P.** Every later `mi-plus/` commit descends from C_P and leaves this file's blob unchanged.
- **Amendments.** An amendment is a new file under `mi-plus/amendments/`. Amendments that change a candidate, a
  predicate, a control or the rule are admissible only before the first commit that adds a file under
  `mi-plus/probes/`. After that commit, no premise, candidate or test is added. A source found after computation
  starts is recorded as input for a separate preregistration and changes nothing here (D2, early stop).
- **Drafting-time knowledge.** No MI+ clause was evaluated while drafting. The facts used are recorded results (§1)
  and the drafting checks of §14. The source ledger (§2) and the SRC column of §4 are written determinations [WA]
  made before computation. They fix which branch of §5.3 the screen can reach (stated there), and they are subject to
  independent review (§12).

## 1. Inputs that stand and are not re-screened

These are inputs, not outputs. No probe re-measures them as a finding. K3 and K4 (§6) re-derive some of them with
new code as method controls only.

- On SEP ⊆ K ⊆ maxCone, PC ⇒ MI for every cone, since ρ⊗P₀ ∈ SEP ⊆ K [WA; EC instance, `op-fork/audit-931d5eda/AUDIT.md`
  F7].
- K(Z_F) and maxCone satisfy MI; Γ(Q3) and K_B fail it [EC, `../runs/p3_fixtures_op.out`, digest `7d1d1db9…`].
- K(Z_F) and L = Q3 ∩ Z_F\* are invariant under all 24 native pair permutations [EC, `op-fork/RESULT.md` N7;
  audit F1(d)]. maxCone fails PC [EC, p3].
- REPORT S2: G2 FAIL (borderline), G4 FAIL, G5 FAIL (standalone, D1: K(Z_F) survives), G6 OPEN.

## 2. Source ledger: what OI supplies about readout, meters and update

Searched: `papers/` (Main, GR, SM, Substratum), `book/`, `verification/lean-mathlib/OIBridge/`, `verification/lean/`,
`verification/ROADMAP.md`, `verification/programmes/oi-qm/` on main, and the research records the memo cites. The
word "meter" occurs nowhere on main except in unrelated prose (drafting check X7). The meter vocabulary is the
screen's own name for an ancilla register in a configuration-ready state.

| # | object | location | tag | cone-level content on SEP ⊆ K ⊆ maxCone |
|---|---|---|---|---|
| S1 | read-write family: a selectable local coupling whose value at each parameter is a bijection fixing every state outside one pair; its operator is a permutation matrix | `ReadWriteFamily` ReadWriteControl.lean:86; `readWriteOperator_monomial` :100 | [AT] | none (an operation) |
| S2 | the native coupling: CNOT (control token 1) is the read-write operator of `memorySwap (1,0) (1,1)` at parameter 1; read-write operators are available at every level | `memorySwap` ReadWriteControl.lean:188; `permClass_readWrite` SubstratumInterfaceAudit.lean:412; `obs_readWriteAvailable` :811 | [AT]; the CNOT instance by definitional unfolding [WA], X5 | none (an operation) |
| S3 | native readout: id ⊗ Lüders in the configuration basis, derived from spectator independence | `readout_is_localLuders` OperationalAssembly.lean:658; `localLuders` :191; `MapSpectatorIndependent` :151 | [AT] | a map on the matrix algebra; says nothing about K |
| S4 | ready meter \|0⟩: a pure seed is preparable given ancilla swaps; the sourced class contains every permutation | `pureSeedPrep_available_of_swap` OperationalAssembly.lean:675; `permTheory_avail_conj` SubstratumInterfaceAudit.lean:611; `permClass_permMatrix` :406 | [AT] parts; the composition for the sourced theory [WA], X6 | none (a preparation) |
| S5 | embedded observation (regrouping, relabelling, ambience) holds for the observer theory | `EmbeddedObservation` EmbeddedObservation.lean:123; `obs_embeddedObservation` SubstratumInterfaceAudit.lean:819 | [AT] | an availability statement about maps; it mentions no state cone |
| S6 | every available operation of the observer theory preserves entrywise-nonnegative matrices | `obsTheory_nonnegBounded` FrozenSourcing.lean:84 | [AT] | independent of K |
| S7 | a passive internal observer only reads an existing record; the recorder writes, dephases and is not passive | `internal_branch_eq_blockPart` InternalObserver.lean:137; `recordInstr` :249; `recordInstr_not_passive` :290 | [AT] | recorder outputs are configuration-diagonal |
| S8 | passive incompleteness is theory-insensitive and does not discriminate the OI core | `passive_nondiscriminating` PassiveIndependence.lean:269; `complete_passive_iff_commutative` CentralObservation.lean:620; Main.md:570 | [AT] | none |
| S9 | Lüders update as Bayesian conditioning, for the represented diagonal sector only; the coherent extension belongs to the operational bridge | Main.md:632 | [WA] | diagonal-sector only |
| S10 | monitored law: the trajectory object, and the retained-protocol instance at q = 3 | `RevReal.traj` Equivalence.lean:174; `../probes/p5_m1_retained_law.py` | [AT]; [EC] | a law of retained protocols (M1) |
| S11 | LC: for every block-positive X, a local rank-one filter output lies in SEP | `bridge-compatibility-audit/source-assessment.md` @ `1d4606b2` :15–32 (SA) | [WA] | holds on every domain cone |
| S12 | DT: complete dual-test closure is preservation in dual language | SA :48–59 | [WA] | a restatement of preservation |
| S13 | "valid measurements" (`hvalid : prep ⊆ maxConeOf avail`) is introduced and unsourced; the F2 row places it in X (X-5) | thread I @ `804843f1` :220, :341, AW-I5 :527 | [UP] | a positivity statement, unsourced |
| S14 | composite operational validity: available branches send PSD to PSD and are trace-preserving in sum; treated as admissibility, with no source proposed | `CompositeOperationalValidity` OperationalValidity.lean:88; EmbeddedObservation.lean header "WHAT IS NOT CLAIMED" | [AT] definition | presupposes PSD |
| S15 | symplectic embedded-meter registration (thread H, R): disturbing; the native read-write copy has no Weil image; E1-L fails the monitored law 27/27 | H @ `804843f1` :114–124, AW-H5 :416; check B `634e1639…` | [WA], [NUM]; [EC] | a replacement interface (memo §2.4, §3.2) |
| S16 | #831 `PrimitivePreservation`: the readout field is a separate preservation premise | P831 @ `65b85147` :74–88 | [CD] theorem; premises [UP] | a preservation premise |
| S17 | purification ingredient and `fiber_freedom` | Main.md:600–602; `purification_probes.py` | [MP] | OP-fork scope; not used here |

**Finding.** No candidate MI+ clause with an independent OI source was found. Each clause built from S1–S16 falls
into one of three classes:

- **(a)** it has an [AT] or derived source, but its cone-level content holds on every domain cone, or it does not
  mention K at all (S3, S5–S9, S11);
- **(b)** it has cone-level content, but that content is a membership "native coherent output ∈ K", the unsourced
  compatibility assertion MI already carries, or the unsourced validity premise S13;
- **(c)** it is a replacement interface that conflicts with M1 (S15).

The screen does not test this finding as a theorem. §4 turns it into a closed candidate list, and §7 certifies the
per-candidate countercontrols. The dichotomy is stated as node hypothesis H-DICH (§7), scoped to that list. It is not
a no-go for observer-level extensions in general.

## 3. Domain, operations, tests, readout identification

**3.1 Domain.** Pair tables ω ∈ W 3, identified with 4×4 Hermitian X = dict ω (`dict` BridgeDictionary.lean:36,
`dictEquiv` EqvK2Schema.lean:216 [AT]). Token states are ρ = tokMat(hom x) with x ∈ eball 3, and \|0⟩⟨0\| =
tokMat(1, 0, 0, 1). K is a closed convex cone with SEP ⊆ K ⊆ maxCone: the premises `hH1`, `hadd`, `hsmul` and `hmax`
of `pairCone_eq_Q3_of_drive_maxCone` EqvK2MaxCone.lean:153 [AT]. maxCone is `maxCone` CompositeDimension.lean:186
[AT]. K is never assumed PSD, CNOT-invariant or closed under any instrument class. Three-token objects enter only
through native discard to pairs (C9, C10, Δ1). No three-token cone is posited.

**3.2 Native operations.** An operation is native iff each Kraus branch is a contractively scaled partial permutation
matrix (`IsScaledPartialPerm`, `permClass` SubstratumInterfaceAudit.lean:231, :236 [AT]). This is the class whose
conjugations the observer theory makes available: `obsTheory_eq_permTheory` :774, `permTheory_avail_conj` :611 [AT].
The native list:
- the 24 pair permutations, including CNOT (S2), SWAP and the local X's;
- the native readout id⊗ℒ_k and ℒ_k⊗id (S3), with the non-selective sums;
- configuration filters and partial permutations (single branches);
- attaching a ready meter \|0⟩⟨0\| (S4) or a uniform meter (`prepAvail_uniform` [AT]);
- discard (`ptraceAnc` OperationalAssembly.lean:453 and the discard field [AT]);
- the 8! three-token permutations, Toffoli among them, which is the read-write operator of a pair swap on `Fin 2³`
  (S1).

Non-native, and excluded from every clause and witness:
- local phases diag(1, e^{iθ}) with θ ∉ πℤ;
- Hadamard;
- `actT (rotLin t)` and `cycEquiv`;
- the stopped maps Φ_k, whose D = diag(1, (3+4i)/5) is not a scaled partial permutation;
- every fullClass or Kraus-family availability (`instAvail_fullClass_of_krausFamily`).

Uniformity (memo §3.3, CRIT :60–64): any architecture containing the exchanges contains `permClass`
(`permClass_le_of_exchanges` :464 [AT]). That is conditional on the inventory being such an architecture, a retained
premise.

**3.3 Fixed tests.** Product effects e⊗f with e and f effects on eball 3, the family that defines maxCone. The
configuration effects P_a⊗P_b are the native subfamily. The same test family is used, unchanged, for every fixture
and every candidate. In particular, no relabelling B ↦ Bᵀ is applied for Γ(Q3), which is what "fixed identification"
means in G3 (memo Fact B). The availability of the token effects is the retained premise `avail_eq_fullEffects`
EffectSpace.lean:727 [AT, conditional on its hypotheses].

**3.4 Readout identification.** Meter reading k corresponds to the effect I⊗P_k on (system, meter) after coupling.
Pulled back through CNOT and the ready meter, it is the system effect P_k:
Tr[(I⊗P_k) CNOT(X_S⊗P₀)CNOT] = Tr[P_k X_S] for every 2×2 Hermitian X_S. This is a matrix identity [WA], certified
symbolically in N1. In ball coordinates P₀ and P₁ are the effects (1 ± x₃)/2.

**3.5 Identification premises, retained and unsourced.**
- Carrier identification: a token is a two-configuration register, and the pair is the configuration carrier
  Fin 2 × Fin 2 of the observer theory (memo §2.1, H-CAR, Γ13) [UP].
- The ready-meter attachment acts on tables as X ↦ X⊗P₀ [WA].

## 4. Candidate clauses (closed list)

Notation: CN = cnotMat (control token 1); P_σ the permutation matrix of σ; ℒ_k^{(i)} the native readout on token i,
Δ^{(i)} = Σ_k ℒ_k^{(i)}; Tr_j the discard of token j. CN_{13} is CNOT with control token 1 and target token 3, on
three tokens. "Native protocol" Π means a finite composition of native single branches on the pair; native ready
meters may be attached and discarded within it.

| id | clause on K | ingredients and tags | SRC |
|---|---|---|---|
| C0 | **MI** (reference, MI-only): ∀ρ, CN(ρ⊗P₀)CN ∈ K | S2, S4 [AT]; the membership [UP] | FALSE |
| C1 | **RO**, readout compatibility: ∀X ∈ K, i, k: ℒ_k^{(i)}(X) ∈ K | S3 [AT]; the membership holds on the domain by S11 | DERIVED |
| C2 | **RO∘MI**, the meter read after coupling: ∀ρ, k: ℒ_k^{(2)}(CN(ρ⊗P₀)CN) ∈ K and Δ^{(2)}(·) ∈ K | S2–S4 [AT]; S11 | DERIVED |
| C3 | **REP**, record consistency: ∀X ∈ K, k: Tr[(I⊗I⊗P_k) CN_{13}(X⊗P₀)CN_{13}] = Tr[(P_k⊗I)X] | S2–S4 [AT]; a matrix identity | DERIVED |
| C4 | **EO ⊕ B**: embedded observation, plus the bridge B "every native operation on the regrouped carrier preserves its cone", restricted to the pair | S5 [AT]; B is S16's premise set [UP] | FALSE |
| C5 | **DIAG**, native statistics: ∀X ∈ K, native Π, a, b: Tr[(P_a⊗P_b)Π(X)] ≥ 0 | S6, S9 [AT, WA]; diagonal autonomy (N3) | DERIVED |
| C6 | **NS**, no-signalling of the meter: ∀X ∈ K and every trace-preserving native Φ on token 2: Tr₂ Φ^{(2)}(X) = Tr₂ X | Main.md:358–373 [WA]; a matrix identity | DERIVED |
| C7 | **REC**, the recorder: ∀X ∈ K, a: `recordInstr a` (X) ∈ K, register token 2 | S7 [AT] | DERIVED |
| C8 | **MI-24**: ∀σ ∈ S₄, ρ: P_σ(ρ⊗P₀)P_σᵀ ∈ K and P_σ(P₀⊗ρ)P_σᵀ ∈ K | S1, S4 [AT]; the membership [UP] | FALSE |
| C9 | **MI-ent**, premeasuring one token of a joint state: ∀X ∈ K, j ∈ {1, 2}: Tr_j[CN_{13}(X⊗P₀)CN_{13}] ∈ K (remaining tokens in index order) | S2, S4 [AT]; the membership [UP] | FALSE |
| C10 | **MI-3**: ∀σ ∈ S₈, ρ₁, ρ₂, j ∈ {1, 2, 3}: Tr_j[P_σ(ρ₁⊗ρ₂⊗P₀)P_σᵀ] ∈ K | S1, S4 [AT]; the membership [UP] | FALSE |
| C11 | **OV-nat**, valid statistics after native protocols: ∀X ∈ K, native Π: Π(X) ∈ maxCone | S13 [UP]; S14 would import PSD | FALSE |
| C12 | **MI ⊕ OV-nat**: C0 ∧ C11 | as C0, C11 | FALSE |
| C13 | **SYM**: the native readout is replaced by symplectic embedded-meter registration | S15 [WA, NUM]; R [UP] | FALSE |

Not candidates, recorded: S5 alone and S6 alone (they mention no cone); S8 (the kernel proves it
non-discriminating); S17 (OP scope, settled by the OP fork).

```mi-plus-ledger
C0 FALSE
C1 DERIVED
C2 DERIVED
C3 DERIVED
C4 FALSE
C5 DERIVED
C6 DERIVED
C7 DERIVED
C8 FALSE
C9 FALSE
C10 FALSE
C11 FALSE
C12 FALSE
C13 FALSE
```

SRC = DERIVED means the ledger holds that the clause is true on every domain cone by a written argument (§7). If N2–N5
refute that argument for a candidate, its SRC becomes FALSE: a refuted derivation leaves the clause unsourced.
`probes/verdict.py` parses the block above. It refuses any candidate id or SRC value that is not in it.

## 5. Predicates, disguise tests and decision rule

**5.1 Predicates per candidate Cj** (each value TRUE / FALSE / UNDECIDED, each with its evidence level):
- **SRC**: from the ledger, subject to the refutation clause of §4.
- **QM**: Q3 satisfies Cj [WA + EC].
- **EXZ, EXG, EXB**: K(Z_F), Γ(Q3) and K_B, respectively, violate Cj. Each needs an exact witness that uses only
  native operations (§3.2) and the fixed tests (§3.3), certified by an exact separating functional in the fixture's
  dual.
- **STR**: some exact domain cone satisfies PC and violates Cj. EXZ ⇒ STR, since K(Z_F) satisfies PC [EC, §1].
- **D1–D7**: the disguise flags of 5.2.
- **M1OK**: the M1 checkpoint of §8 passes for Cj.

**5.2 Disguise tests.** A flag is raised by its stated check, never by judgement alone. Each test carries
known-answer controls (K6); a known-answer failure voids the screen.

- **D1, merely restates PC.** Flag if PC24 (invariance under all 24 native pair permutations, which contains PC)
  implies Cj on the domain, by a written argument [WA] with exact instances on every fixture satisfying PC24
  (Q3, L, K(Z_F)). A D1-flagged clause cannot exclude K(Z_F). Record-only: whether Cj ⇒ PC, checked on maxCone
  (maxCone fails PC). An equivalence with PC is stated only with a witness for each direction (§A.34).
  - Must flag: PC; C0 (§1).
  - Must not flag: the clause "K ⊆ Q3", since K(Z_F) satisfies PC24 and is not contained in Q3 [EC, recorded].
- **D2, assumes compatibility or is definitional.** D2 is raised if any one of three checks fires.
  - (a) Operational shadow. Form Cj^op: replace every conclusion "Y ∈ K" by "Y ∈ maxCone", that is, all fixed tests
    give nonnegative values on Y. Fire if Cj^op holds on every domain cone [WA + EC on maxCone] while Cj itself is
    violated by some fixture. The exclusion power then comes from asserting that a native output is a physical state.
  - (b) Stated membership. Fire if Cj's own statement, not a consequence derived from other premises, is
    "Φ(Y) ∈ K" for a native Φ with Φ(Y) ∉ SEP for some admissible Y.
  - (c) Definition. Fire if Cj defines K, or a sub-cone it relies on, as an orbit, a reachable closure, or the dual of
    an available-test family (CRIT :32–36; SA :48–67).
  - Must flag: C0, by (a), since CN(ρ⊗P₀)CN is PSD, hence in maxCone, while C0 excludes Γ(Q3); PC, by (b), since
    CN(\|+0⟩⟨+0\|)CN = B ∉ SEP.
  - Must not flag: C11, whose shadow is itself and which fails on maxCone (CN Γ(B) CN ∉ maxCone [EC, p3]); and
    OP-weak's existence clause E, which has no conclusion of form (b) and excludes K_B [EC, recorded].
- **D3, assumes PSD.** Flag if Cj, or the validity argument of any of its exclusion witnesses, uses positive
  semidefiniteness of an element of K, imports S14, or implies K ⊆ Q3 [WA].
  - Must flag: "K ⊆ Q3"; S14 imported as a clause on K.
- **D4, assumes a continuous phase or a non-native resource.** Flag if any operation in Cj or in its witnesses fails
  the nativity checker [EC].
  - Must reject: diag(1, i), Hadamard, Φ₁, and a partial permutation with two distinct nonzero entries (1 and ½).
  - Must accept: CN, SWAP, Toffoli, P₀⊗I, the filter onto {00, 11}.
- **D5, assumes closure under quantum instruments.** Flag if Cj quantifies over CP maps, Kraus families or fullClass.
  - Must flag: "every CP instrument preserves K".
  - Must not flag: C11.
- **D6, no independent OI source**: SRC = FALSE.
- **D7, conflicts with M1**: M1OK = FALSE (§8).

**5.3 Rule.** The outcome labels are mutually exclusive and are assigned in this order.
1. **VOID**: any method control of §6 fails.
2. **EARLY-STOP: insufficient alone / unsourced**: no candidate qualifies. Cj qualifies iff
   SRC ∈ {TRUE, DERIVED} ∧ ¬D1 ∧ … ∧ ¬D7 ∧ M1OK ∧ QM ∧ STR. The record lists, for every candidate, every predicate
   value with its exact countercontrol, and names the first failing predicate in the order SRC, D1, D2, D3, D4, D5,
   D7, QM, STR.
3. **UNDECIDED**: no candidate qualifies, but some candidate has no decided failing predicate.
4. **QUALIFIES, INSUFFICIENT**: some candidate qualifies, but none has EXZ ∧ EXG ∧ EXB.
5. **QUALIFIES, EXCLUDES THE NAMED FIXTURES**: some qualifying candidate has EXZ ∧ EXG ∧ EXB.

Under the ledger every candidate has SRC = FALSE, or SRC = DERIVED together with a D1 flag (a DERIVED clause holds on
every domain cone, so PC24 implies it). So the reachable outcomes are VOID and EARLY-STOP. Branches 4 and 5 are
reachable only through a pre-probe amendment that adds a sourced candidate. The computation's content is therefore:
- the exact countercontrols attached to EARLY-STOP;
- the node results N2–N5 (H-DICH);
- the record-only diagnostics Δ1 and Δ2.

EARLY-STOP is therefore a ledger outcome, not a computed one.

**5.4 Verdict text.** `probes/verdict.py` generates the verdict from the `RESULT` lines the probes print. Every
sentence in it is conditioned on measured or ledger values; there are no fixed conclusion strings. In self-test mode
it applies mutations, and each must change or reject the verdict: flip one SRC to TRUE; flip one D-flag; remove one
witness line; fail one control. It prints VOID if any control line is FAIL.

## 6. Fixtures and controls

| fixture | definition and source | role |
|---|---|---|
| Q3 | {X ⪰ 0} (`Q3` EqvK2Schema.lean:239 [AT]) | **must-pass** (QM): a candidate that fails on Q3 gets QM = FALSE |
| Γ(Q3) | partial transpose on token 2 of Q3 (memo Fact B) | **must-be-excluded** (G3, §3.3): EXG |
| K(Z_F) | (Q3 ∩ Z_F\*) + cone(Z_F), with z_k = 4e(s,t) = I/2 − P_{m}, m = (1, b, −bd, d)/2 (`../probes/p3_fixtures_op.py`:49; #820 stage 6; X8) | **must-be-excluded** (§3.3): EXZ |
| K_B | SEP + ℝ₊B, B the Bell projector (#820) | **must-be-excluded** (§3.3): EXB |
| maxCone | block-positive tables | **diagnostic**: the largest domain cone; the D1 and D2(a) checks |
| SEP | conv(products) | **diagnostic**, the vacuity floor: a clause "Φ(S) ⊆ K" with fixed inputs S holds on every domain cone iff it holds on SEP |
| classical | the diagonal cone with monomial operations (CRIT :159–160) | **must-pass for the native class**: native operations preserve it (N3). It is not a ball-token fixture, and no candidate is required to hold on it (memo §3.3) |
| L, K_Γ | Q3 ∩ Z_F\*; Q3 + ℝ₊Γ(B) (`op-fork/`) | **diagnostic**, record-only |

The fixture roles are candidate-level. A must-pass or must-be-excluded fixture that a candidate misses sets that
candidate's predicate (QM, EXG, EXZ, EXB); it does not void the screen. Only a method control below voids it.

**Method controls** (all must be green, or the screen is VOID):
- **K1 membership, positive.** Certified members: B ∈ Q3; each z_k ∈ K(Z_F); Γ(B) ∈ Γ(Q3); B ∈ K_B; Γ(B) ∈ maxCone.
- **K2 membership, negative**, each with an exact separator:
  - B ∉ Γ(Q3);
  - Γ(B) ∉ Q3;
  - P_{m_k} ∉ K(Z_F), via z_k ∈ K(Z_F)\* (audit F1(c));
  - the QM purification of diag(1/4, 3/4) ∉ K_B (p3).
- **K3 MI replay, new code.** K(Z_F) satisfies MI symbolically over the ball, the defect pairings being (1 ± x)/4
  (audit F7); maxCone satisfies MI; Γ(Q3) and K_B fail it. Any disagreement with §1 is VOID.
- **K4 PC replay, new code.** CNOT permutes Z_F; maxCone fails PC; Γ(Q3) fails PC.
- **K5 nativity checker**: the D4 accept/reject lists.
- **K6 disguise known-answer controls**: as in 5.2.
- **K7 M1**: §8, M1-CP1 to M1-CP4.
- **K8 determinism**: every probe runs twice under `python3 -I -B`, with rc 0 and byte-identical stdout.
- **K9 upstream integrity**: the scripts' digests are checked before they run, and outputs must match their recorded
  digests (sha256):
  - `../probes/p3_fixtures_op.py`: script `e23172053d6a579b4365faca4a2412afbf644e3380abf883c9b42c062c7236d7`, output
    `7d1d1db99ad26054f0e6b7a4960cd39ce95151d0f5765bad6b05caed81e538e1`;
  - `../probes/p5_m1_retained_law.py`: script `5c5673511a26948a21e1f93551173cfff87f94de5e1a9886895962582bf34993`, output
    `ad2e371cfeb37691cb49657107b82534dcebf59c58dfc321e6e51464a0097906`;
  - `op-fork/audit-931d5eda/tools/audit_exact.py`: script `e728f6c2246e60b8ae91f47156807d9f44013ba789fd2e6fc1c6c18ac57c987b`,
    output `61ffe323b9e4f3f32de9b2cde342eaea91869f8cea9e373fc1e39b3716509219`;
  - check B, compared by digest only (C13): `634e1639637e9e803f9d6a65786023cba47f2f9362aec358118d53f48ffdac5d`
    (`../runs/replay_checkB.out`).

A failed control means VOID; no candidate value is reported over it. A harness, disk or timeout failure is an
infrastructure event. It is kept in `runs/runN-harness-error/`, never deleted, and has no scientific reading.

## 7. Nodes (depth-first; each closed by an explicit check)

- **N0 anchors.** Every [AT] citation in §2–§3 resolves to the declaration at the stated file and line in the
  working tree [EC, mechanical].
- **N1 identities.** The readout pullback of §3.4, C3's identity and C6's marginal identity, each symbolic over
  generic Hermitian inputs [EC].
- **N2 readout collapse (S11 applied).** For X ∈ maxCone, ℒ_k^{(i)}(X) ∈ SEP, and so Δ^{(i)}(X) ∈ SEP [WA, SA :15–32].
  - [EC]: the conditional blocks are PSD symbolically for generic block-positive parametrizations, and on every
    fixture generator.
  - Closes C1 and C2, and C7: the recorder output is a nonnegative multiple of \|aa⟩⟨aa\| [EC symbolic].
- **N3 diagonal autonomy.** For every native single branch Q X Q†, diag(Q X Q†) depends only on diag(X) [WA].
  - [EC]: all 209 partial-permutation matrices on four configurations; the scalar c enters only as \|c\|².
  - Every domain cone has the classical cone as its set of diagonals [WA]: products give every nonnegative diagonal,
    and the configuration tests are product tests.
  - Closes C5.
- **N4 pair reduction.**
  - Tr₂[CN_{13}(X⊗P₀)CN_{13}] = CN(m₁(X)⊗P₀)CN. This is an MI input, the token-1 marginal of a domain cone element
    being a ball multiple [WA].
  - Tr₁[CN_{13}(X⊗P₀)CN_{13}] is classical on the meter, hence in SEP.
  - [EC] symbolic. Places C9 under C0.
- **N5 PC24 ⇒ C8.** ρ⊗P₀ ∈ SEP ⊆ K and K is P_σ-invariant [WA]. [EC]: the K(Z_F) and maxCone instances.
- **N6 per-candidate table.** All predicates of 5.1 and flags of 5.2 for C0–C13, with witnesses. The C13 row uses the
  recorded check B (E1-L fails the monitored law) by digest `634e1639…` [EC-up] and S15; no new symplectic
  computation is run.
- **H-DICH**, closed by N2–N6. For every candidate in §4, one of two cases holds.
  - (i) SRC = DERIVED and D1 is flagged: the clause holds on every domain cone.
  - (ii) SRC = FALSE, and the clause's exclusion power, where it has any, rests on one of three things: a stated
    membership of a coherent native output (D2), the unsourced validity premise S13 (C11, C12), or a replacement
    readout (D7).

  Scope: the closed list only. Classification under §A.31 is fixed in advance by
  outcome:
  - confirmed: ELABORATING (it extends AW-X2 from Γ to every domain cone for native-statistics clauses);
  - refuted at a candidate: NEW, recorded at that candidate.

**Record-only diagnostics.** Neither enters 5.3, and neither can be cited as sourced. Each has its own exclusive
rule: EXCLUDES needs one exact certified witness; DOES-NOT-EXCLUDE needs a universal written argument with exact
certificates; UNDECIDED otherwise. A finite non-finding is never reported as non-exclusion.

- **Δ1, MI-3 against K(Z_F).** Inputs: ρ₁, ρ₂ ∈ {\|0⟩, \|1⟩, \|±⟩, \|±i⟩} (rational Gaussian density matrices);
  σ ∈ S₈; meter token 3 in \|0⟩; j ∈ {1, 2, 3}.
  - A witness is an output X ∉ K(Z_F), certified by W = P + Σ d_k z_k, with P ⪰ 0, d ≥ 0, Tr(W z_j) ≥ 0 for all j,
    and Tr(W X) < 0, all exact.
  - Run for L and K_Γ as well.
  - Runtime bound 30 minutes; beyond it, an infrastructure stop.
- **Δ2, OV-nat against K(Z_F) at pair level.**
  - Since Kraus branches preserve PSD and K(Z_F) = L + cone(Z_F) with L ⊆ Q3, C11 on pair-level single branches
    reduces to Q z_k Q† ∈ maxCone for the 209 partial permutations Q and the four defects [WA].
  - Each image is certified either by an exact decomposition P + Γ(Q′) (P, Q′ ⪰ 0, Størmer–Woronowicz [L]) or by an
    exact product vector with negative value.
  - Exhaustive at pair level without ancillas, so DOES-NOT-EXCLUDE may be stated for that class only.
  - Ancilla-assisted native protocols: UNDECIDED unless argued.

## 8. M1 handling

OI's original non-disturbing monitored protocols keep their law. Every candidate C0–C12 uses only native operations
and the native readout, so it adds no protocol; C13 replaces the readout. A newly disturbing meter protocol carries its
own operational law, stated as a prediction (memo §3.2). It is never counted as an already-sourced OI monitored
protocol. Checkpoints:

- **M1-CP1.** Replay `../probes/p5_m1_retained_law.py` (K9): the q = 3 retained law is reproduced entrywise from
  diagonal and coherent starts, and the RR and NEW controls separate.
- **M1-CP2.** Every operation named by C0–C12 or by their witnesses passes the nativity checker. Every readout used is
  `localLuders` in the configuration basis, and its non-selective channel leaves the configuration diagonal unchanged:
  diag(Δ^{(i)}(E_pq)) = diag(E_pq) on all 16 matrix units [EC].
- **M1-CP3.** A candidate whose readout fails M1-CP2's non-disturbance identity, or that replaces the readout (C13),
  gets M1OK = FALSE and D7.
- **M1-CP4, the pair instance.** Token 1 is visible and token 2 hidden.
  - The dynamics is each σ ∈ S₄, the start a registered value with the hidden token uniform, and the readout ℒ^{(1)}
    at t = 0, 1, 2.
  - The classical trajectory law must equal the description-level law from the diagonal start and from the coherent
    start (hidden \|+⟩).
  - A registered start is P_a⊗τ with τ ⪰ 0 on every domain cone (block-positivity), so no non-PSD registered start
    exists. Off-diagonal content is exercised instead by unregistered starts: every generator of every fixture,
    including Γ(B) and the four defects, read at t = 0, 1, 2. The law from X must equal the classical law from
    diag(X) (N3).
  - Two controls must change the law for some (σ, a):
    - a re-randomizing readout, ℒ^{(1)} followed by resetting token 2 to uniform. This protocol is native and
      disturbing, and so is a new protocol with its own law;
    - an inserted non-native Hadamard on token 2.

## 9. G6

G6 stays OPEN. No candidate has an independent source (§2), so no prediction or postdiction is attempted, and none
may be chosen after results. Two kinds of statement are excluded from G6: a consequence of K = Q3 such as the
Tsirelson value, which follows from cone selection itself and is a retrodiction on the consistency axis; and any
statement about Δ1 or Δ2.

## 10. Gate mapping (memo §2.3, §3.2, §3.3; G5 standalone per D1)

| gate | what the screen measures | evidence |
|---|---|---|
| G1 | each candidate is stated in OI terms (readout, meter, coupling, native operations) and lists no matrices as members of 𝓘 | §4 [WA] |
| G2 | (i)–(ii) SRC and D1–D6; (iii) consequence beyond compatibility: not addressed (G6) | ledger [WA], N6 [EC] |
| G3 | EXG under the fixed tests and native operations | N6 [EC] |
| G4 | whether a candidate adds an operation: by §3.2 none does, so G4 FAIL for C0–C12 is fixed in advance; C13 is a replacement and fails G4 (memo §2.4) | K5 [EC], [WA] |
| G5 | headline: §3.3 exclusion of K_B, K(Z_F) and Γ(Q3) by the candidate itself (EXB ∧ EXZ ∧ EXG). Separate subfinding: control preparation per §2.3 (this §6). Preparation alone is never a G5 PASS | N6 |
| G6 | not addressed; OPEN (§9) | — |
| G7 | no knobs: control token 1, meter in \|0⟩, configuration-basis readout, CNOT orientation, Δ1 inputs and runtime bound all fixed here | chronology (§0) |
| G8 | A1/B1 fixed by the memo (2026-10-17) | memo |
| M1 | M1-CP1 to M1-CP4 | §8 |

## 11. Invariant → checkpoint (§A.41)

| invariant asserted | checkpoint |
|---|---|
| this file precedes every probe | at C_P, `git ls-tree -r C_P -- mi-plus/` lists only PREREG.md; `git diff --quiet C_P HEAD -- mi-plus/PREREG.md`; RESULT records C_P, this blob id and the first probe commit |
| no rule change after the first probe commit | `git log --format=%H -- mi-plus/amendments/` lists only ancestors of the first probe commit |
| the frozen OP-fork and parent records are untouched | `git diff --quiet 451f2590 HEAD --` over `op-fork/PREREG.md`, `op-fork/probes/`, `op-fork/runs/`, `op-fork/runs-check/`, `op-fork/check_verdict.py`, `op-fork/audit-931d5eda/`, `../probes/`, `../runs/`, `../src/`. The mutable `../REPORT.md` and `op-fork/RESULT.md` are excluded; they take forward-only corrections (D1) |
| the closed candidate list | `verdict.py` parses the `mi-plus-ledger` block and refuses unknown ids; `check_verdict.py` checks the parsed list against this file's blob |
| only native operations in clauses and witnesses | K5, with every witness's Kraus operators passed through the checker and printed |
| one fixed test family for all fixtures | the probes print the digest of the serialized test list once per fixture; all digests are equal |
| exact certificates | certificate code admits only `Fraction`, Gaussian rationals or SymPy algebraic numbers and raises on `float`; a numeric search may propose a witness, never certify it |
| verdict generated from measurements | `verdict.py --selftest` mutations (§5.4) each change or reject the verdict |
| no verdict over a failed control | `verdict.py` prints VOID when any K-line is FAIL; this is one of the self-test mutations |
| evidence levels distinct | every RESULT line carries `level=` ∈ {EC, WA-on-EC, WA, LEDGER, DERIVED-CHECK}; `check_verdict.py` rejects a WA conclusion labelled EC and any shared certificate bucket feeding more than one key |
| determinism | K8; `runs/SHA256SUMS` identical across two full replays |
| M1 not broken | M1-CP1 to M1-CP4 |
| infrastructure kept apart | harness-error runs kept under `runs/runN-harness-error/`, never deleted |
| G5 standalone headline | the gate table generator requires both §3.3 and §2.3 entries and prints the §2.3 entry as a separate subfinding |

## 12. Evidence plan

Files are planned under `x-screen-20261018/mi-plus/`. None is written before C_P.

| path | content | level |
|---|---|---|
| `PREREG.md` | this file | — |
| `probes/n0_anchors.py` | N0 | EC (mechanical) |
| `probes/n1_fixtures.py` | fixtures, membership oracles with certificates, K1–K4, N1 | EC |
| `probes/n2_native.py` | nativity checker K5, N3, M1-CP2 | EC |
| `probes/n3_candidates.py` | N2, N4, N5, N6, D1–D7 with K6 | EC + WA-on-EC |
| `probes/n4_m1_pair.py` | M1-CP4 | EC |
| `probes/n5_diagnostics.py` | Δ1, Δ2 (record-only) | EC + WA |
| `probes/replay.py` | runs n0–n5 twice each, compares, writes `runs/<probe>.out` and `runs/SHA256SUMS`; K9 upstream replays into `runs/upstream_*.out` | — |
| `probes/verdict.py` | §5.3 from RESULT lines and the ledger block; `runs/verdict.out`, `runs/verdict.selftest.out` | derived |
| `check/check_verdict.py` | imports nothing from `probes/`; authenticates `runs/` against `SHA256SUMS`, re-applies §5.3, checks levels; writes `runs-check/` | derived consistency check |
| `RESULT.md` | the generated verdict and the gate table; written arguments tagged [WA] | — |

- **Independence.** The probes import nothing from `../probes/`, `op-fork/` or the audit. Fixtures are re-implemented
  from their definitions.
- **Dependencies.** Python 3 standard library plus SymPy (X9); versions printed in each output.
- **Replay.** From the repository root:

  `python3 -I -B verification/programmes/oi-qm/reconstruction/research-planning/x-screen-20261018/mi-plus/probes/replay.py`

  then `sha256sum -c runs/SHA256SUMS` inside `mi-plus/`, then the same with `check/check_verdict.py`. Digests are
  recorded in `runs/SHA256SUMS` and `runs-check/SHA256SUMS` at the run, and quoted in RESULT.
- **Independent review before RESULT is called final.**
  - The §2 ledger and the SRC column, including a fresh corpus search for a missed source.
  - The universal written arguments of N2–N5 and the Δ2 reduction.
  - The D1–D3 written determinations.
  - The independent exact re-derivation of at least the N6 witnesses for C0 and C11, and every Δ1 or Δ2 witness, by
    code that shares nothing with `probes/`.

## 13. Scope guards

- Research only: no adoption of X, no native round, no F or E designation, no merge, no status, ROADMAP, programme,
  manuscript or theorem change, and no full-equivalence or iff claim.
- The OP-fork's frozen files are untouched: PREREG, probes, runs, runs-check, the audit and `check_verdict.py`. So are
  the parent `../probes/`, `../runs/` and `../src/`. The N6 maxCone paragraph of `op-fork/check_verdict.py` is not
  cited as evidence (D1).
- A negative outcome is stated for the closed candidate list and the native class of §3.2 only, never for
  observer-level extensions in general.
- No composite with OP, OP-strong or PC is screened.
- The collector (#862) and retention (#860) gates are unchanged.

## 14. Drafting checks (non-decisive)

- **X1.** Read D1/D2 in full. Read REPORT, `src/`, op-fork PREREG and RESULT, and the audit at `451f2590` with
  `git show`. Read the G5 diff `451f2590..4c7d5c30` (two files, text only).
- **X2.** Read the F2 memo at `acfef447`, §2.1–§3.3 and §4.
- **X3.** `git diff --quiet b96662e6 415fc868` holds for every cited kernel file: ReadWriteControl,
  SubstratumInterfaceAudit, OperationalAssembly, EmbeddedObservation, EqvK2MaxCone, EqvK2Schema, FrozenSourcing,
  InternalObserver, PassiveIndependence, CentralObservation, OperationalValidity, BridgeDictionary,
  CompositeDimension, EffectSpace, Equivalence. It also holds for `papers/Main.md`, `Substratum.md`, `SM.md`,
  `purification_probes.py` and `verification/ROADMAP.md`.
- **X4.** The declarations exist at the cited lines: `ReadWriteFamily`, `readWriteOperator_monomial`, `memorySwap`,
  `permClass_readWrite`, `obs_readWriteAvailable`, `obs_embeddedObservation`, `obsTheory_eq_permTheory`,
  `permTheory_avail_conj`, `permClass_permMatrix`, `permClass_le_of_exchanges`, `IsScaledPartialPerm`, `permClass`,
  `readout_is_localLuders`, `localLuders`, `MapSpectatorIndependent`, `pureSeedPrep_available_of_swap`, `ptraceAnc`,
  `obsTheory_nonnegBounded`, `recordInstr`, `recordInstr_not_passive`, `internal_branch_eq_blockPart`,
  `passive_nondiscriminating`, `complete_passive_iff_commutative`, `CompositeOperationalValidity`, `RevReal.traj`,
  `dict`, `dictEquiv`, `Q3`, `maxCone`, `pairCone_eq_Q3_of_drive_maxCone`, `avail_eq_fullEffects`,
  `instAvail_fullClass_of_krausFamily` (ImplementationLocality.lean), `rotLin`, `cycEquiv` (KInfFoundations.lean:386,
  :416). The line anchors in CRIT, SA, thread I, thread H, P831 and Main.md were also checked.
- **X5.** By reading the definitions: `memorySwap a b` at parameter 1 is `Equiv.swap a b`, and CNOT with control
  token 1 is the swap of configurations (1,0) and (1,1). Confirmed exactly in X8.
- **X6.** No named theorem states pure-seed availability for `permTheory` (grep). S4's composition is therefore
  tagged [WA].
- **X7.** A corpus grep for "meter", "premeasur", "measurement as interaction" and "ready state" over papers, book,
  `verification/programmes`, ROADMAP and OIBridge finds no hit on the meter notion.
- **X8.** Fixture well-formedness only; no clause evaluated. A SymPy script in the drafter's scratch (script
  `a79df8fc…`, output `31d368ab…`) confirmed:
  - 4e(s,t) = I/2 − P_{m(b,d)} with m = (1, b, −bd, d)/2, the map (s,t) ↦ (b,d) being (1,1)↦(1,1), (1,−1)↦(−1,−1),
    (−1,1)↦(−1,1), (−1,−1)↦(1,−1);
  - {m} is orthonormal and maximally entangled (CC† = I/2);
  - e(s,t) is Hermitian;
  - cnotMat = P₀⊗1 + P₁⊗X equals that configuration swap.
- **X9.** `python3 -I -B -c "import sympy"`: SymPy 1.14.0, Python 3.11.15.
- **X10.** Read the recorded digests from `runs/SHA256SUMS`, `op-fork/runs/SHA256SUMS` and the audit's `SHA256SUMS` at
  `451f2590`.
