# NOTES-O1 — the exact no-go envelope for a discrete coherent mixer

Thread `research/origin`, node O1. Base L = `9f9f8257`; kernel paths are under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels: [K] certified at L (file:line), [D] design module
(kernel-checked on a disposable branch, not certified), [W] written argument (given here), [X] exact
computation in `experiments/` (check id in brackets), [A] audited archive record, [L] literature, not read at
the source. Scripts: `o1_envelope.py` (tier M, 14 checks, 6 countercontrols) and `o1_fieldneutral.py` (tier F,
16 checks, 4 countercontrols), both green on run 1 and byte-identical on replay.

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than "the
substratum class is monomial, so no Hadamard" and either sharpens the boundary every O2 mechanism is tested
against or exposes an assumption hidden in the rung-1 slogan.

## 0. Verdict

The envelope has two tiers and is sharp in both.

1. **Tier M (matrix carrier, configuration frame).** The invariant that excludes a coherent mixer is
   **dephasing covariance**, which for unitaries is exactly **monomiality** — not ones-fixing. Every family
   instrument-realized by a class of submonomial operators (the substratum class, the sourced class, every
   structurally closed sub-architecture) commutes with the configuration dephasing branch by branch, at every
   level; from the available preparations every reachable state is diagonal; so every H-sandwich has
   visibility exactly 0 — for every protocol, ancilla size, readback with feed-forward, coarse-graining,
   mixture and limit.
2. **Ones-fixing is independent of mixing.** All four cells (ones-fixing or not) × (monomial or not) are
   populated by exact unitaries, and the visibility vanishes exactly in the two monomial cells. The landed
   ones-fixing architecture `onesClass` already carries a balanced non-monomial mixer, the layer gate flow at
   time one half (= √X). The chain "permutation classes with readback ⇒ ones-fixing ⇒ no mixer" is correct only
   as "⇒ no `hMat` and no quarter phase"; the no-mixer conclusion for the sourced class follows from
   monomiality.
3. **Tier F (field-neutral).** If the path readout is passive on the reachable body (observe-and-forget is
   idle, as in every tower built by conditioning a classical substratum), every sandwich has visibility 0
   **whatever the mixers are and wherever they come from** — the drive, a completion-valued operation or an
   imported Hadamard included. And when the stated access lets conditioning reach configuration point masses
   (exchanges plus passive readout), the extreme states are outcome-deterministic and no reversible operation
   is a balanced pure mixer.
4. **The boundary, exactly.** Just outside the envelope the owner's numbers (1 and 1/2) are reproduced by
   classical constructions in two ways only: (a) a "dephasing" that erases the readback memory, from a
   non-extreme seed; (b) replacing the passive readout by a knowledge-balance readout (reading the path
   re-randomizes the memory), which yields Spekkens' toy bit — an octahedral body in which a substratum swap is
   a balanced extreme mixer. (b) is outside the stated access: adding back the passive readout destroys it.

## 1. Definitions (fixed for O1–O4)

- Δ: complete dephasing in the configuration frame, X ↦ diag X. On a composite A × Fin n, the **path
  dephasing** of the visible register is Δ_A ⊗ id.
- A linear map Φ is **DC** (dephasing-covariant) if Φ∘Δ = Δ∘Φ; **non-generating** if Φ(E_ii) is diagonal for
  every i; **non-detecting** if Δ(Φ(E_ij)) = 0 for i ≠ j.
- **Sandwich.** Seed ρ₀ (frame-diagonal), mixers M₁, M₂, diagonal readout {P_k}:
  P_coh(k) = tr P_k M₂M₁ρ₀, P_deph(k) = tr P_k M₂ D M₁ρ₀ with D the path dephasing; visibility
  V_k = P_coh(k) − P_deph(k). The owner's witness is P_coh = 1, P_deph = 1/2.
- **Fresh-record path dephasing**: attach a blank register, copy the path value into it, discard it. It is the
  operational content of which-path detection, and it equals Δ_A ⊗ id exactly [X M4a].

## 2. Tier M — the matrix carrier

**T1 (DC characterization).** For every linear Φ: DC ⟺ non-generating ∧ non-detecting. For a unitary channel
Ad U: non-generating ⟺ non-detecting ⟺ U monomial.

*Proof [W].* Φ(Δ E_ij) = δ_ij Φ(E_ii) and Δ Φ(E_ij) = Σ_k ⟨k|Φ(E_ij)|k⟩ E_kk. For i = j equality says Φ(E_ii)
is diagonal; for i ≠ j it says Φ(E_ij) has zero diagonal. For Ad U: U E_ii U† = |Ue_i⟩⟨Ue_i| is diagonal iff
column i has one nonzero entry; ⟨k|U E_ij U†|k⟩ = U_ki conj(U_kj) vanishes for all i ≠ j iff row k has at most
one nonzero entry; a unitary is column-monomial iff it is row-monomial. ∎
Exact: 15 unitaries in dimensions 2 and 3, the four predicates agree on each [X M1]. The non-generating half for
monomials is landed: `preservesDiag_conj_of_monomial` [K SubstratumInterface.lean:126]. The full commutation
for submonomial operators is the design lemma `conj_dephase_of_submonomial` [D, see §6].

**T2 (the sandwich identity).** V_k = tr P_k M₂ (id − Δ) M₁ρ₀. It vanishes if M₁ is non-generating or M₂ is
non-detecting. For a qubit unitary U = [[a, b], [c, d]] with second mixer U†: P_coh(0) = 1,
P_deph(0) = |a|⁴ + |b|⁴, V = 2|a|²|b|². So V = 0 exactly for the monomial U, and the owner's witness (1, 1/2)
holds exactly for the **balanced** ones, |a|² = 1/2.
*Proof [W]:* tr P_k Y = tr P_k ΔY for diagonal P_k; the rest is the 2×2 computation. Exact on 11 qubit
unitaries: the balanced set is {H, rot(π/4), √X, √X†}; the Pythagorean rotations (cos = 3/5) are unbalanced
mixers with V = 288/625 [X M2a–c].

**T3 (the monomial envelope).** Let 𝓘 be an implementation class whose operators are submonomial — the substratum
class `substratumClass` [K StructuralClosure.lean:180], every subclass of it, in particular the sourced class
`permClass` (`IsScaledPartialPerm` includes `IsSubmonomial`, [K SubstratumInterfaceAudit.lean:231]). Then:
1. every branch of every family `InstAvail 𝓘 T O F` commutes with Δ_T, at every carrier T;
2. from the available preparations (uniform attach; the pure seed `pureSeedPrep_available_of_swap`
   [K OperationalAssembly.lean:675]) every reachable state is diagonal;
3. the path dephasing Δ_A ⊗ id, and the fresh-record dephasing, act as the identity on every reachable state;
4. hence every sandwich has visibility exactly 0, for every protocol and level;
5. DC is a linear subspace of the superoperators, of dimension d² + (d² − d)², hence closed under coarse-graining,
   convex combinations (time averaging over a uniform clock register) and limits in any norm (the completion's
   closure).

*Proof.* (1) `realized_of_instAvail` [K ImplementationLocality.lean:530] writes each branch as Σ_i Ad K_i with
K_i ∈ 𝓘, for an architecture (`substratumClass_arch` [K StructuralClosure.lean:231], `permClass_arch`
[K SubstratumInterfaceAudit.lean:350]); each Ad K_i commutes with Δ by T1 extended to submonomial K [W, D];
sums commute. (2) Preparations are diagonal and DC maps preserve diagonality. (3) Δ_A ⊗ id fixes
Δ_T-diagonal states. (4) is (3). (5) [W] + dimension 8 (d = 2) and 45 (d = 3) by exact rank [X M7]. ∎
Exact: 60 deterministic protocols (uniform or pure-seed ancilla, monomial step with Gaussian-rational phases,
Lüders readout of either register, outcome-dependent monomial continuation, coarse-graining, discard): both
branches and the aggregate DC and trace-preserving [X M3]; 2304 composite sandwiches (all 24 × 24 permutation
pairs, both seeds, both ancilla preparations): every state diagonal, visibility 0 [X M4b–c]. Kernel-checked as
design lemmas `instAvail_substratum_dephase`, `instAvail_permClass_dephase` [D, §6].

**What T3 covers, by name.** A2's bijective interventions `bijectiveOperator` and the phase interventions
`phaseOperator` (both monomial, [K SubstratumInterface.lean]), the read-write operators
(`readWriteOperator_eq_perm` [K ReadWriteControl.lean:96]), the readout projectors, the record instrument
`recordInstr` (Kraus operators `|a,a⟩⟨a,b|`, submonomial; [K InternalObserver.lean:249]), every protocol of the
substratum theory `substratumTheory` [K RouteB.lean:279] and of the sourced theory `permTheory`
[K SubstratumInterfaceAudit.lean:606]. It is the kernel's own residual (`substratumGen_not_control`
[K StructuralClosure.lean:348]) stated as an operational no-go with the sandwich as its test, and it is the
single-system face of S2's class `𝒞_mono` [A pt/S2/RESULT.md, Theorem M]: frame-monomial operations create no
coherence in the frame basis.

**The swap with memory, singled out.** Attaching a uniform ancilla and swapping it with the visible qubit twice
returns the seed with probability 1, and with the path dephased between the swaps still 1: the information sits
in the ancilla, which the path dephasing does not touch [X M4d]. Memory is not coherence.

## 3. Ones-fixing is not the no-mixer invariant

**T4.** (a) The four cells are populated, with V = 0 exactly in the monomial cells [X M5a]:

| | monomial | not monomial |
|---|---|---|
| ones-fixing | 1, X (V = 0) | √X, √X†, exp(−itX) at cos t = 3/5 (V = 1/2, 1/2, 288/625) |
| not ones-fixing | Z, S (quarter phase), a phased swap (V = 0) | H, rot(π/4), real rotation cos = 3/5 (V = 1/2, 1/2, 288/625) |

(b) **A landed ones-fixing class carries a perfect mixer.** `onesClass` is an architecture [K
InstrumentRealization.lean:628] and ones-fixing (`isometry_fixes_ones` [K :833]); it contains the gate flow of
every involution (`onesClass_gateFlow` [K :508]); `InstAvail.op` makes the conjugation available
(`genTheory_avail_conj` [K SubstratumSource.lean:103]). At t = 1/2 the gate flow of the site exchange has
entries (1 ± i)/2 (`gateFlow_half_entries` [K LiftAudit.lean:138]): it is √X, non-monomial, balanced, and
passes the owner's test (√X√X|0⟩ = |1⟩ with probability 1, dephased 1/2; with √X† the seed returns) [X M5b].
The packaged statement `onesFixing_class_carries_mixer` is a design lemma [D, §6].
(c) On two points every member of the qubit drive exp(−itX) fixes the all-ones ray; on three points the
transition flow moves it (the kernel's countercontrol `flow_realized_not_instrumentRealized`
[K InstrumentRealization.lean:1176]) while the gate flow, which differs from it by the pair phase e^{iπt/2},
does not [X M5c].
(d) The kernel's exposure of the hidden-coherence surplus (`tauChain_diag`, branches 3/2 and −1/2
[K AncillaInterference.lean:201]) is reproduced exactly with √X in place of `hMat` [X M6]: the mechanism of
`interference_exposes_badOp` needs a balanced mixer, not a non-ones-fixing one.

**Consequence for the rung-1 slogan.** Exact restatement: within the sourced class, `permClass_onesFixing`
[K PhaseSource.lean:79] with `instAvail_unitary_fixes_ones` [K InstrumentRealization.lean:398] excludes `hMat`
(and the quarter phase); the exclusion of every mixer is T3 (monomiality). As a criterion for rung 1,
non-monomiality is necessary and, for unitaries with balance and an inverting second mixer, sufficient (T2);
non-ones-fixing is neither (√X; Z). The owner's own target ("a non-monomial coherent mixer") is the right one;
the necessity clause attached to `instAvail_unitary_fixes_ones` holds for `hMat`, not for coherent mixers in
general.

## 4. Tier F — field-neutral protocol towers

Model [X]: Ω = {0,1}², ω = (z, x), z visible, x a readback memory, μ uniform; the menu (swap, flips, CNOTs)
generates all 24 permutations — the kernel's `ExchangesAvailable` on four configurations [X F0].

**T5 (passivity kills every witness).** If observe-and-forget is the identity on the reachable body, then
P_deph = P_coh for every seed and every pair of operations: the dephased and coherent protocols are the same
operation. Every tower built by conditioning a classical substratum has this property (OI-STAGE A5 [A
research/archive/oistage/RESULT.md §7]); it passes to the completed body by continuity (both sides affine and
continuous in the chart, equal on preparations) [W]. With the path dephasing read as a fresh-register record,
the same holds in every configuration-level model: copying a classical value into a blank register and
discarding it is the identity on the marginal [X F1 (D_fresh), M4a]. Exact: D_pass = D_fresh = id on the 11
reachable posteriors; visibility 0 in 6336 sandwiches; three-bit robustness, generated group of order 1344,
6336 sandwiches [X F1, F5, F9].
*Consequence:* an H-sandwich witness requires **invasive** observation — observe-and-forget ≠ idle on the
reachable body — independently of where the mixer comes from. This is the discrete counterpart of NG2 [A
oistage §7], which required invasive observation for a strictly convex body.
*Scope.* T5 concerns the dephasing realized as which-path recording (observe-and-forget, or a fresh-register
record). A dephasing realized as a twirl over frame-preserving operations is not covered by T5; it is covered by
Lemma P (NOTES-O3 §3): when the native readout is passive and repeatable, every pure state is
outcome-deterministic for it, so no balanced pure mixer exists to be twirled, whatever the dephasing.

**T6 (outcome determinism).** If every extreme point of the body gives the frame readout a value 0 or 1, no
reversible body automorphism maps a pure frame state to a balanced state (automorphisms preserve extremality)
[W]. The hypothesis follows from passivity and repeatability of the readout alone (Lemma P, NOTES-O3 §3). With the stated access (exchanges, passive readout, conditioning on records) every point mass is a
reachable posterior — swap, read, swap back [X F2] — so the extreme points are the point masses, whose readout
is deterministic [X F3], and no permutation is a balanced pure mixer [X F4]. The "balanced" seed (z = 0,
x uniform) is the midpoint of two reachable point masses, not a pure state [X F6, CCF4].

## 5. The boundary — what lies just outside

**T7.** (a) *Memory erasure.* From the seed (z = 0, x uniform) the classical swap gives P_coh = 1; with the
memory re-randomized between the swaps (D_x), 1/2; and the same with the kernel's recorder written into the
memory register (x := z, `recordInstr`'s overwrite), 1/2 [X F6, F7]. Neither is a path dephasing: D_x moves a
pure state of the frame face, and the recorder into a blank register gives visibility 0 (CCF3). **The definition
of "complete path dephasing" is load-bearing**: as a fresh-register record it is the identity on classical
states; as memory erasure it fakes the witness.
(b) *Knowledge balance (KB-D).* Remove the passive readout and read z only together with a re-randomization of
the memory. Then [X F8]: no point mass is reachable (every posterior has all probabilities ≤ 1/2); the reachable
posteriors are exactly the uniform state and the six pair states; these six have affine rank 3 and are each
exposed — an **octahedron**; the swap maps z+ to the balanced extreme state x+; the sandwich gives P_coh = 1,
P_deph = 1/2; D_KB is the frame dephasing r z+ + (1 − r) z− on every reachable state and is invasive; the
z = 0 face is the single state z+. Adding the passive readout back makes point masses reachable again and the
construction collapses to the classical simplex (CCF1). This is Spekkens' toy bit [L, Spekkens, PRA 75, 032110
(2007)]; that interference phenomenology of this kind is reproduced by an epistemically restricted classical
theory is argued in [L, Catani–Leifer–Schmid–Spekkens, Quantum 7, 1119 (2023)].
**Reading.** The field-neutral envelope is sharp: with the stated access it holds (T5, T6); replacing one
element of the access — the passive readout — by a complementarity-type disturbance law suffices for a
classical construction to pass the owner's operational test. Where that leaves the Discrete target is O2's
mechanism M-KB.

## 6. Kernel design module (run on a disposable branch)

`OIBridge/OriginEnvelope.lean` on `dev-origin/envelope`: `conj_dephase_of_submonomial`, `dephase_sum`,
`instAvail_substratum_dephase`, `instAvail_permClass_dephase`, `gateFlow_half_not_monomial`,
`onesClass_mixer_available`, `onesFixing_class_carries_mixer`. Build green in workflow run 38084486326 at dev
commit c3f7fbb2, every declaration on [propext, Classical.choice, Quot.sound]; copied verbatim to
`lean/OriginEnvelope.lean` [D] (not certified). The first run, 38083822302 at 271ba177, failed to parse the scoped
`ᴴ` notation.

## 7. Mechanisms the envelope kills (recorded as FAILED routes; detail in NOTES-O2)

Every mechanism whose operations on the configuration carrier are submonomial and whose readout is passive:
bijective dynamics and selectable permutations (A2), phase interventions, read-write coupling, the record
instrument, ancilla coupling with readout and feed-forward, coarse-graining and time averaging, and the closure
of any of these. Each fails at T3 on the configuration carrier and at T5 field-neutrally.

## 8. Classification (§A.31)

- **NEW, O1-N1.** Ones-fixing is independent of mixing; a landed ones-fixing architecture carries a balanced
  non-monomial mixer (T4). Hidden assumption exposed: the rung-1 slogan's middle link.
- **NEW, O1-N2.** Passivity kills every sandwich witness regardless of the mixer's source (T5): the Discrete
  target needs invasive observation, not only a non-monomial operation.
- **NEW, O1-N3.** The boundary (T7): the definition of path dephasing is load-bearing (fresh record versus
  memory erasure), and a knowledge-balance readout makes a substratum swap a balanced extreme mixer of an
  octahedral body.
- **ELABORATING, O1-E1.** T1–T3: DC ⟺ monomial for unitaries; the monomial envelope for every protocol, with
  closure under mixtures and limits.
- **CONFIRMING, O1-C1.** S2's `𝒞_mono`, the kernel's `substratumGen_not_control`, OI-STAGE's NG2.
