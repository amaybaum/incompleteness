# NATIVE-NONDIO: a native route to non-MIO or non-DIO elements (investigation)

**WIP / UNVERIFIED. Paper-only research; awaiting an independent non-author review.** This note
walks the nodes of `PLAN.md`, committed before it at `f916d2c6`. It runs no computation, edits no
manuscript, Lean module, accepted design or reviewed record, adopts no premise, changes no status
and strengthens no manuscript or kernel theorem. Physical source (I-3) remains NOT PASSED. No
merge is authorized. Pins, definitions and the assumption list are those of `PLAN.md` §1, §3 and
§4, with two premises the proofs use made explicit here: TB and DEC (§0, N6).

Revision r2 answers the independent review of `6bd93ada` (#1544 c.7075473914, verdict REVISE
(minor)): F1–F3 narrow §0, N2, N3 and N6 to what is proved; F4–F9 are applied as nits. r2 has not
been re-reviewed. `PLAN.md` is unchanged.

Labels. **Established**: proved on paper here (layer X, exact algebra), or cited at the source's
own standing (K kernel theorem on `main`; R a record at its stated standing). It means established
within this note, not established in the §A.46 sense. **Assumed**: a named premise. **Missing**: a
gap, stated with the node where the branch stopped. (N) native, (I) imported.

## 0. Outcome

**Answer to Q, on countable carriers, for the class NAT (`PLAN.md` §3), under KIN-B, LIN, TB and
DEC.** Throughout, MIO, DIO and "coherence" are taken in the configuration basis fixed by KIN-B.

| Element | (a) exists in some admissible model | (b) derived from the selected dynamics and interface | (c) operationally accessible |
|---|---|---|---|
| non-DIO (detector) | **no**, in any model of the class (DET, RED) | no | no |
| non-MIO (creator) | only by appending a non-diagonal hidden state, which is a representation choice, not a native state (4d) | no | no: its coherence changes no native record law (IDLE) |

**Blocking premise (Established, X; (N) premises, (I) carrier).** The negative uses:
- total-carrier determinism of native operations: DEF (`Main:42`: S is the total system and the
  dynamics is a map on it), A2's determinism (`Main:54`, `Sub:94`), and NAT's clause that outcomes
  and records are functions of configurations;
- **DEC** (N): every adjoined factor whose dynamics is not a configuration map (a deep factor
  evolved by a unitary or an isometry) is prepared independently and evolves by product dynamics
  (`Main:60`; ledger item (ii), `Main:736`; `Sub:94`). A deep factor evolved by a measurable map
  is a configuration map on an uncountable carrier, which falls under M1;
- KIN-B; positivity and linearity (LIN);
- **TB** (I): the global trace bound Σ_o Tr Φ_o(ρ) ≤ Tr ρ for **all** ρ ≥ 0, coherent inputs
  included. Its configuration-level restriction does not suffice (N6).

It does **not** use injectivity or reversibility, finiteness (A1), complete positivity, the
Koopman lift, or R-READ (N6).

**Missing ingredient, in the configuration basis.** A native element that creates or detects
coherence **in the KIN-B configuration basis** would need, at the total carrier, a
configuration-level randomness that two distinct configurations share within one outcome branch
(necessary for detection, Proposition SHARP), or that one configuration spreads over two outputs
within one branch (necessary for creation), **and** a rule fixing a non-classical extension of
that action, since the classical extension of a random rule is still DIO. The framework's stated
substratum supplies neither, and supplying either is a change of the physical model, which is
outside this investigation's authority. This is a necessary condition for configuration-basis
coherence only. It says nothing about quantum record statistics on an **encoded** carrier: GATE-A
r5.8 §2.2 records (the (iv) dilemma) that T-SUB′ clauses (i)–(iii), the source of NAT, admit a
stepwise D-W hosted inside Φ in a computationally universal substratum, which is deterministic,
configuration-valued and MIO ∩ DIO in the configuration basis. Encoded carriers in the sense of
T-SUB′ (iv) are outside every statement of this note.

**What stays open.** Measurable diffuse carriers (M1); a non-normal hidden state with a countably
infinite visible carrier (M2); nonlinear state assignments (M3); the nativeness criterion itself,
since T-SUB′ is an option under D5 and NAT is a named premise (M4).

**Productivity (`PLAN.md` §5): gem.** Output class ELABORATING, with one BORDERLINE marker (§7).

## 1. Literature and corpus, read first

| Topic | Source | Relation |
|---|---|---|
| MIO, DIO; creating and detecting coherence | T. Theurer, D. Egloff, L. Zhang, M. B. Plenio, PRL 122, 190405 (2019) | definitions used, as in OPRES §2 |
| Operations fixing all incoherent states | J. I. de Vicente, A. Streltsov, J. Phys. A 50, 045301 (2017) | a neighbouring rigidity: genuinely incoherent operations have diagonal Kraus operators. DET is a different statement (deterministic, not identity, configuration action), and is not cited from there |
| Positive contractions | elementary: 0 ≤ F ≤ 1 and ⟨x|F|x⟩ ∈ {0, 1} force F x ∈ {0, x} | the only operator fact DET uses; no source is claimed for DET, and any novelty is relative to the corpus |

Corpus records read in full before the walk: OPRES `NOTE.md` at `24702c1d`; READOUT-ALG `NOTE.md`
at `4554dd63`; QOPS-P4 `NOTE.md` at `f9e564ea` (§A.19: it already proves Kraus rigidity for
injective maps, RIG(a), and for single-branch trace-preserving maps, RIG(b), and names COH-REC as
the exact criterion for a non-DIO multi-branch branch, RIG(d)); GATE-A r5.8 §2 and §2.2 at
`109b9590`. Manuscript sites read in context: `Main:42`–`60`, `Main:274`, `Main:328`, `Main:338`,
`Main:664`, `Main:736` (posit ledger), `Sub:94`, `Sub:208`, `Sub:217`, `GR:213`, `GR:290`.

## 2. N1 (decisive): rigidity of deterministic actions

Setting (CNT, KIN-B, LIN, TB). X, Y countable; (Φ_o)_{o ∈ O}, O countable, normal positive
linear maps from trace-class operators on ℓ²(X) to those on ℓ²(Y), with Σ_o Tr Φ_o(ρ) ≤ Tr ρ for
every ρ ≥ 0 (TB; required on all inputs, not only on configuration states).
p(o, y | x) := ⟨y|Φ_o(|x⟩⟨x|)|y⟩. F_{o,y} := Φ_o*(|y⟩⟨y|).

**Proposition SHARP (necessary conditions; Established, X; (I) on KIN-B, LIN, TB).**
- **(D)** If branch o is not DIO-type, there are y and x ≠ x′ with p(o, y | x) and p(o, y | x′)
  both in the open interval (0, 1).
- **(M)** If branch o is not MIO-type, there are x and y ≠ y′ with p(o, y | x) > 0 and
  p(o, y′ | x) > 0.

*Proof.*
- Positivity and TB give 0 ≤ F_{o,y} ≤ Φ_o*(1) ≤ 1, and
  ⟨x|F_{o,y}|x⟩ = p(o, y | x).
- (D) If every F_{o,y} is diagonal, then Φ_o*(M_g) = Σ_y g(y) F_{o,y} lies in ℓ^∞(X) for every
  g ∈ ℓ^∞(Y) (σ-weak sum, by normality), so branch o is DIO-type. Otherwise some F = F_{o,y} has
  F_{x x′} ≠ 0 with x ≠ x′. Since F ≥ 0, F_{xx} > 0 and F_{x′x′} > 0. Since 1 − F ≥ 0 and
  (1 − F)_{x x′} = −F_{x x′} ≠ 0, also (1 − F)_{xx} > 0 and (1 − F)_{x′x′} > 0.
- (M) Φ_o(|x⟩⟨x|) ≥ 0, so a nonzero off-diagonal entry (y, y′) needs both diagonal entries
  nonzero. If every Φ_o(|x⟩⟨x|) is diagonal, normality gives Φ_o(Δρ) = Σ_x ρ_xx Φ_o(|x⟩⟨x|),
  which is diagonal. ∎

*Attainability (Established, X).* Both conditions can be met by CP extensions:
- the destructive readout ⟨±| (OPRES CC-1, step 3) extends the rule p(±, · | x) = ½ for x = 0, 1
  and is not DIO-type;
- Φ(ρ) = Tr(ρ)|+⟩⟨+| extends the rule p(y | x) = ½ for all x, y ∈ {0, 1} and is not MIO-type.

Whether (D) and (M) are sufficient in general is not shown (Missing M7, minor).

**Lemma DET (Established, X; (I) on KIN-B, LIN, TB).** If the configuration-level action is
deterministic, then every branch of every positive extension is MIO-type and DIO-type. Moreover
F_{o,y} is the diagonal projector onto span{|x⟩ : p(o, y | x) = 1}, and Φ_o(|x⟩⟨x|) is
|f_o(x)⟩⟨f_o(x)| or 0.

*Proof.* With values in {0, 1}, (D) cannot hold, and (M) would need two outputs with p = 1 from
one x in one branch, against Σ_y p(o, y | x) = Tr Φ_o(|x⟩⟨x|) ≤ 1 (TB). For the explicit form: a diagonal
entry 0 of F kills its row (F ≥ 0), and a diagonal entry 1 kills the row of 1 − F, so F|x⟩ is 0
or |x⟩. A positive Φ_o(|x⟩⟨x|) with trace at most 1 and diagonal entries in {0, 1} has at most one
nonzero diagonal entry and is that rank-one projector. ∎

**Verdict N1: YES.** Determinism of the configuration-level action fixes MIO-type and DIO-type
for every positive extension that satisfies TB, with no injectivity, no trace preservation
beyond TB, no complete positivity and no Kraus form. TB cannot be weakened to configuration
inputs: Ψ(ρ) = 2⟨+|ρ|+⟩ |0⟩⟨0| on ℂ² is CP, has the deterministic configuration-level action
x ↦ 0 with trace 1 on each configuration, and is not DIO-type (Ψ*(|0⟩⟨0|) = 2|+⟩⟨+|); it violates
TB on |+⟩⟨+| (review c.7075473914, F1; X).

*Relation to QOPS-P4.* DET contains the MIO and DIO conclusions of RIG(a) (injective maps) and
all of RIG(b) (non-injective, one trace-preserving branch). RIG(a)'s monomial Kraus form needs
complete positivity and injectivity; for CP extensions, DET's rank-one form gives column-monomial
Kraus operators, and row-monomial ones only with injectivity. For RIG(d), SHARP(D) shows that COH-REC needs two colliding
configurations whose weights in the branch are both strictly between 0 and 1. When the branch is
a function of the configuration, COH-REC fails.

## 3. N2: native operations at the total carrier

Each NAT ingredient is read on the total carrier S of DEF. A preparation or prior enters as an
appended state, not as part of the operation (LAW).

| Ingredient | Total-carrier action | Source | Deterministic? |
|---|---|---|---|
| dynamics | the map φ, a bijection in the selected model | `Main:42`, `Main:54`; `Sub:94` | yes (N) |
| non-bijective descriptions | the map f on a finite set, restricted to its eventual image | `Main:60` | yes, non-injective before restriction; DET does not need injectivity |
| readouts and records (R1, R2) | the outcome is a function of a configuration reached by the dynamics | READOUT-ALG RA-1 (items 1–12, 22, primitives of 26) | yes (N) |
| EP-schema histories | p_M(h \| π, p) = μ_p({λ : H_M(λ, π) = h}), H_M a function of the seed | `EP:97`, `EP:92` | yes; the randomness is in μ_p, a state |
| controls, feedforward | configuration controller fields | `EP:75`–`79` | yes |
| classical intervention dilation | bijections | `Main:490`, `:494` (READOUT-ALG item 5) | yes |
| phase intervention | identity on configurations | `GR:213`; `phaseOperator_supplied` (cited in OPRES CC-1) | yes |
| discard | the projection (x, z) ↦ x | — | yes |
| A★2 recording coupling | a joint reversible process on Reg × K; the record is a measurable function of the joint state | `f2-1-coherence-sourcing/amendments/A-star.md`:31–35 (path under `verification/programmes/substratum/recursive-substates/`) | yes; K may be diffuse (N5) |
| adjoined deep factor | a factor of any cardinality adjoined to the hidden sector, prepared independently and evolved by its own dynamics (a unitary, an isometry or a measurable map), with product dynamics | `Main:60`; ledger item (ii), `Main:736`; `Sub:94` | **not** a configuration map when unitary or isometric, so outside NAT (ii); admitted under DEC, which leaves every reduced visible channel unchanged |

**Verdict N2 (Established at the cited sources; (N)).** Apart from the adjoined deep factor, which
NAT (ii) excludes when its dynamics is not a configuration map and DEC decouples, no ingredient
in the sources searched has a non-deterministic total-carrier action. The sources are those listed here and READOUT-ALG's
inventory (its §5). The finding concerns those sources only.

## 4. N3: reduction and record laws

**Corollary RED (Established, X; (I) on KIN-B, LIN, TB).** Let (Φ_o) be any positive extension, on
ℓ²(C_V × Z) → ℓ²(C_V′ × Z′) with Z, Z′ countable, of a deterministic action. Let ω be a normal
state on B(ℓ²(Z)), or any state if C_V is finite. The visible instrument, in Heisenberg form
Φ^V_o*(M_g) := σ_ω(Φ_o*(M_g ⊗ 1)), is DIO-type, whatever ω is. It is MIO-type if ω is diagonal.

*Proof.* M_g ⊗ 1 lies in ℓ^∞(C_V′ × Z′). DET puts Φ_o*(M_g ⊗ 1) in ℓ^∞(C_V × Z). The slice
(σ_ω f)(v) = ω(M_{f(v, ·)}) maps ℓ^∞(C_V × Z) into ℓ^∞(C_V). It is normal for normal ω, and for
finite C_V it is the pointwise slice of OPRES Remark D′, step 3, defined for any state. MIO-type:
for diagonal normal ω, |v⟩⟨v| ⊗ ω is a countable convex combination of configuration states,
and DET(i) and normality apply. ∎

- Protocols: a finite composition of NAT steps, with feedforward, postselection and discard, has a
  deterministic total action, so RED applies to the whole protocol at once. DIO-type is also
  closed under these operations (OPRES Lemma C).
- For CP extensions, OPRES Theorem C(b) then gives ‖Φ^V − Ad_W‖_⋄ ≥ 2κ_row(W) for every
  trace-preserving visible protocol and every unitary W on ℂ^{C_V}. The bound is positive for
  non-monomial W.

**Corollary IDLE (Established, X; (I) on KIN-B, LIN, TB).** For any NAT protocol and any positive
extension of its steps, the probability of every record outcome o is ρ(Φ_o*(1)) with
Φ_o*(1) ∈ ℓ^∞(X). It therefore depends on the initial total state ρ only through the restriction
of ρ to ℓ^∞(X): for a normal ρ, its diagonal. This holds for every state, normal or not.

Consequences:
- Two Born-form assignments with the same configuration diagonal are not distinguished by any
  NAT protocol.
- An appended coherent hidden state, or coherence in the visible preparation, changes no native
  record law. Creation without detection is invisible at the record level. This extends OPRES
  Lemma C's 𝒩⁺ ⊆ DIO from the permutation-lift class to every positive extension of NAT steps
  that satisfies TB.

**Verdict N3: closed.** Native visible instruments are DIO-type for every positive extension
satisfying TB and every hidden state in the stated scope, and native record laws are blind to all
coherence **in the configuration basis** (KIN-B). This does not exclude quantum-like record laws
on an encoded carrier in the sense of T-SUB′ (iv) (the GATE-A r5.8 §2.2 (iv) dilemma, §0), which
are outside this note.

## 5. N4: candidates, with maximum skepticism

Three passes were made over the candidates. Pass 1 took the seven fixed in `PLAN.md` §6.

**4a. The continuous gate path** (`GR:290`; `gateFlow`, `LiftAudit.lean`:47).
- (a) **Yes, mathematically.** For 0 < t < 1, gateFlow σ t is non-monomial
  (`gateFlow_not_monomial`, `CoherentContinuumSource.lean`:74, K). Its conjugation channel is
  therefore neither MIO-type nor DIO-type (OPRES C(c), B(i)).
- (b) **Not derived as an operation.**
  - `Main:274`: "any continuous one-parameter interpolation is additional structure, chosen rather
    than derived". What is derived is the existence of a strongly continuous path of
    *-automorphisms (`driveQ_isContinuousPath`, `SecondOrderDrive.lean`:225, K).
  - The gate flow is fixed by the definition `unit g t = 1 + (e^{iπt} − 1)·proj g`
    (`SecondOrderCircuit.lean`:356), the principal branch. The alternative
    u′(t) = 1 + (e^{3iπt} − 1)·proj g is also a one-parameter group with u′(0) = 1 and
    u′(1) = 1 − 2 proj g = g. At t = ½ it takes the value −i on the range of proj g, where the
    principal flow takes +i (X). So the intermediate points depend on a choice. The searched
    modules (`SecondOrderDrive`, `SecondOrderLayer`, `SwapLayer`, `RegionLimit`) contain no
    uniqueness theorem for the path; `continuous_extension_not_unique` (`RegionLimit.lean`:296, K)
    is the general non-uniqueness.
  - At t = ½ the configuration-level action has weights ½, ½ on a moved pair. It is not a step of
    φ, so it lies outside NAT. Steps of φ are integer ticks in the discrete-time model
    (`Main:44`).
- (c) **Not accessible.** `coherent_continuum_not_sourced` (`CoherentContinuumSource.lean`:328, K)
  shows that no configuration-level class makes conjChannel(gateFlow · ½) available at level one;
  see also `substratumTheory_not_layerFlowExecutable` (`LiftAudit.lean`:200, K).
- **Verdict: a representation, not native.** *Observation W1 (for review, no edit):* `GR:290`
  says "What the substratum does determine is a path". The kernel supports the existence of a
  path built from the principal-branch gate flows. A uniqueness statement for that path is not
  found, and the e^{3iπt} variant shows a second one. This is a wording check on a manuscript
  outside this record's authority.

**4b. The unitary of the stochastic-quantum correspondence** (`Main` §3.1).
- (a) **Yes.** For a unistochastic one-step matrix Γ = |U|² on C_V with U non-monomial, Ad_U is a
  CP map whose configuration-level action is Γ. It is neither MIO-type nor DIO-type.
- (b) **Not derived.** By RED, Ad_U is not the reduction of any positive extension of a NAT
  operation, with any hidden state, since every such reduction is DIO-type (X). It is a different
  extension of the same random visible rule, which SHARP's attainability shows is not unique. The
  corpus states the Born form as the dictionary of Q_fb, not as selected (`Main:18`), places the
  coherent extension in the operational bridge (`Main:664`), and fixes off-diagonal phases only
  from continuous-time data under a chosen interpolation (`Main` §3.1, "Phase uniqueness from
  continuous-time data", with `Main:274`).
- (c) **No.** By IDLE its coherences change no native record law.
- **Verdict: a representation**, consistent with `Main:18` and with §A.29.

**4c. The declared full observable algebra** (READOUT-ALG items 24, 25; `Str:742`, `Str:788`,
`Main:722`, `GR:366`).
- (a) As an algebra it contains non-diagonal elements (READOUT-ALG §2.4).
- (b), (c) **No NAT procedure realizes one** (Established, X; (I) on KIN-B, LIN; countable
  carriers). By RED with g = 1, every effect a NAT procedure induces on the visible input lies in
  ℓ^∞(C_V), under every positive extension of its steps.
- So READOUT-ALG's IMPL-R5, and QOPS-P4's H-R5L (IMPL-R5 ∧ LUD), cannot be met by a NAT procedure
  on countable carriers. ACC-R5 is what NAT delivers.
- This decides nothing between R5a and R5b as readings of the manuscript sentences (READOUT-ALG
  owner question 3). Under R5a, the declared non-diagonal elements would need a procedure outside
  NAT, which is an import.
- **Verdict: not native in NAT.**

**4d. A coherent hidden state, or a non-diagonal representative of a law.**
- (a) **Yes.** Appending a non-diagonal ω can make the visible reduction non-MIO-type (OPRES
  Lemma C).
- (b) **Not derived.** LAW gives laws over configurations (`Main:58`; ledger posit (iv),
  `Main:736`). KIN-B represents a law by its diagonal. A non-diagonal representative with the
  same diagonal is a choice of representation.
- (c) **No.** By IDLE, no NAT protocol distinguishes ω from its diagonal.
- **Verdict: a representation.** It creates coherence that cannot be observed.

**4e. The decoupled deep sector** (`Main:736`, item (ii)).
- (a) Its own dynamics may be a unitary in its own representation.
- (b), (c) It is prepared independently, with product dynamics, and the cited statement records
  that this leaves every reduced visible channel unchanged. It supplies no visible coherence
  operation. Coupling it would violate that statement's hypothesis, which is a change of model.
- Its hypothesis is load-bearing (review c.7075473914, F2; X): a deep qubit evolving by H,
  coupled to a visible qubit by a configuration swap, then H, then the swap again, gives the
  visible channel Ad_H, which is neither MIO-type nor DIO-type. DEC is therefore listed among the
  premises used (§0, N6).
- **Verdict: no route under DEC** (citation check).

**4f. Emergent visible stochasticity and P-indivisibility.**
- Visible non-Markovianity and indivisibility are produced by permutation dynamics with a
  classical hidden prior (`Main:328`, diagonal preservation; OPRES A′, (N) as algebra). They are
  not coherence resources in the MIO/DIO sense.
- **Hidden assumption exposed.** At the visible level the action is random, so SHARP's conditions
  can be met there, and the extension looks underdetermined. That is the setting of QOPS-P4
  RIG(d) and of READOUT-ALG's "Open for O1-D" items. At the total carrier the action is
  deterministic, and DET with RED fixes every derived visible extension as DIO-type. A visible
  extension chosen independently of the total carrier (4b) is not derived from the native action.
- **Verdict: no route; assumption-watch marker AW-1** (§7).

**4g. READOUT-ALG items 11 and 12 under COH-REC** (QOPS-P4 §2).
- **Item 11.** The EP-schema history is a function of the seed (`EP:97`). On a countable seed
  space, DET makes every positive extension on the seed carrier DIO-type. COH-REC at the visible
  level therefore requires a visible update that is not the reduction of any positive extension
  of the schema's action, which is an import.
  - Native non-DIO is excluded for reductions on countable seed spaces.
  - It stays open on measurable seed spaces (`EP:100`), under N5.
- **Item 12.** The A★2 coupling is a joint reversible process on Reg × K with a measurable record
  function. For countable K, the same conclusion holds. For diffuse K (cylinder sets, hemispheres,
  `A-star.md`:33–35), it is open under N5.
- **Items 1, 4, 22.** QOPS-P4 shows DIO under CPX. DET with RED gives DIO for every positive
  extension of the total-carrier action satisfying TB, without CPX's complete positivity.
- **Attribution.** For items 11 and 12 the total dynamics is already a bijection, so QOPS-P4's
  RIG′ covers their reductions under CP (QOPS-P4 `NOTE.md`:73–74). The conclusions here are
  conditional on NAT, under which every update is a reduction by definition; the gain over RIG′ is
  complete positivity weakened to positivity with TB. Dropping injectivity matters only for
  non-bijective descriptions.
- **Verdict: no native candidate on countable carriers, conditional on NAT**; measurable cases go
  to M1.

**Pass 2** (further corpus sources):
- the diagonal phase intervention (deterministic; DET);
- Bell settings under measurement independence (xiv), whose settings are configuration outputs of
  generators (deterministic);
- non-bijective eventual-image descriptions (deterministic; DET);
- `FiniteOperationalTheory` rules (d), a uniformly mixed and so diagonal ancilla, and (e), a local
  Lüders readout with diagonal projectors (`GR:213`), inside the imported completion setting;
- the gluing realization's supplied instrument data (READOUT-ALG item 18) and the OI_Q completion
  (item 16), both imports outside NAT.

No NEW finding.

**Pass 3** (non-NAT items):
- supplied-datum readouts (READOUT-ALG items 13, 19);
- the GPT track (item 17);
- the wave-operator lift (item 20);
- the PC-1 candidate coupling (item 21).

Each is data or an import by its own record, so outside NAT. No NEW finding. With pass 1's only
marker being BORDERLINE, the fixed-point rule (`PLAN.md` §8) stops the walk here.

## 6. N5 and N6

**N5. Carrier scope.**
- **Measurable diffuse carriers.** There are no normal configuration states on a diffuse L^∞(H),
  so p(o, y | x) is not defined at points of H. The two typable readings of "extension of a
  deterministic measurable action" are:
  - in Heisenberg form, Φ_o* acts on configuration functions as composition with T;
  - in Schrödinger form, on normal states, the output configuration law is the push-forward of
    the input configuration law.

  Both make DIO-type hold by definition (OPRES Proposition D, Remark D′). A reading that would
  make the question non-trivial needs non-normal point states and an extension of Φ_o to them,
  which is not defined here. **Missing M1; branch stopped.**
- **Non-normal states on countable carriers.** IDLE holds for every state. RED holds for any hidden
  state when C_V is finite. With C_V countably infinite and ω non-normal the slice is not
  established. **Missing M2**, the same point as OPRES U1′(ii).

**N6. Drop-one check of the premises used** (each line Established, X, or a citation).

| Premise | Dropped | Effect on the negative |
|---|---|---|
| determinism (A2 with DEF and NAT(iii)) | a random total-carrier rule | the negative fails: ⟨±| extends p = ½ and is non-DIO; Tr(ρ)\|+⟩⟨+\| extends p = ½ and is non-MIO (§2). Dropping it makes a native element possible, not present: a non-classical extension rule must still be supplied |
| totality of S (DEF) | randomness from outside S | reduces to the previous row |
| outcomes as configuration functions (NAT(iii)) | an outcome drawn at random given the configuration | reduces to the first row |
| KIN-B (configurations as the basis) | a rotated logical basis | relocates both elements to the interface (OPRES Corollary C1) |
| KIN-B, scope of "coherence" | an encoded carrier X_A (T-SUB′ (iv)) | outside the statement: a stepwise D-W hosted inside Φ is deterministic and MIO ∩ DIO in the configuration basis, and may reproduce quantum record statistics on X_A (GATE-A r5.8 §2.2, the (iv) dilemma) |
| LIN (positive linear) | nonlinear state assignment | outside the result (OPRES B, Scope); **Missing M3** |
| TB (global trace bound, all inputs) | the bound on configuration inputs only | the negative fails: Ψ(ρ) = 2⟨+\|ρ\|+⟩ \|0⟩⟨0\| is CP, deterministic (x ↦ 0) and trace 1 on configurations, and not DIO-type (§2) |
| DEC (decoupled non-configuration factors) | a unitary deep factor coupled by configuration swaps | the negative fails: the visible channel Ad_H (4e) |
| injectivity, reversibility | a non-injective deterministic map | **not used**: every positive extension of x ↦ 0 satisfying TB has Φ*(\|0⟩⟨0\|) = 1, so it is DIO-type and MIO-type (DET) |
| finiteness (A1, ledger item (ii)) | countable carriers | **not used** |
| complete positivity; Kraus form; Koopman lift; R-READ | positivity and TB | **not used** |

**Verdict N6.** The blocking premise is total-carrier determinism: DEF, A2's determinism half and
NAT(iii), given DEC, KIN-B, LIN and TB, and for coherence in the configuration basis.
*Cross-propagation:* retiring A1 (#1477) or replacing bijectivity by REV opens no native coherence
route on countable carriers; only the measurable case (M1) interacts with cardinality. This
covers carriers with countably many configurations (finitely many sites with a countable
alphabet, or finitely supported configurations). An infinite site set with an alphabet of q ≥ 2
symbols has 2^ℵ₀ configurations, so the infinite lattice, the natural carrier once A1 is retired,
falls under M1 and remains open.

*NAT and T-SUB′ (iii).* NAT reads clause (iii) as "functions of configurations"; GATE-A says
"functions of visible-sector configurations". NAT is the broader class, so the negative over NAT
covers T-SUB′ (ii)–(iii).

## 7. Classification (§A.31) and productivity

| Item | Label | Layer | Class |
|---|---|---|---|
| Proposition SHARP | (I): KIN-B, LIN, TB | X | ELABORATING: necessary conditions stated on the configuration-level action alone |
| Lemma DET | (I): KIN-B, LIN, TB; (N) premise: determinism | X | ELABORATING: contains the MIO and DIO conclusions of RIG(a) and all of RIG(b); decides RIG(d) for deterministic branches |
| Corollary RED | as DET, with DEC | X | ELABORATING: extends RIG′ from CP extensions of the injective lift to positive extensions (with TB) of any deterministic action, and any hidden state in scope |
| Corollary IDLE | as DET | X | POSITIVE: coherence in native states is empirically idle, which is §A.29's "representing is not deriving" in this setting |
| 4c (IMPL-R5 not NAT-realizable) | as DET | X | ELABORATING: constrains a named open premise |
| 4g (items 11, 12 on countable carriers) | as DET; conditional on NAT | X | ELABORATING: decides QOPS-P4's open items within reductions; the gain over RIG′ is positivity only |
| AW-1: the visible-level framing | — | P | BORDERLINE; the review (c.7075473914) classes it ELABORATING, as implicit in QOPS-P4's remark that COH-REC implies "not the reduction of the lift" |
| W1: the gate path is a choice | (I) | X, K | BORDERLINE: a wording check on `GR:290` |
| 4a, 4b, 4d, 4e | as cited | X, K, P | CONFIRMING: representations, not native |

**AW-1 (assumption-watch marker).** Native-coherence questions posed at the visible level, where
the action is emergently random, leave extensions underdetermined. Posed at the total carrier,
which DEF makes the only carrier with no outside randomness, they are decided by determinism.
Records that classify an item "open" because its visible update on coherent inputs is undefined
should check whether that item is the reduction of a deterministic total-carrier action.

**Productivity test.**
- *Stronger than the restatements.* DET and RED drop R-READ and the Koopman lift (OPRES §5), and
  weaken complete positivity to positivity with TB (QOPS-P4 RIG′); injectivity is dropped as well,
  which matters for non-bijective descriptions.
- *Constrains (i).* IMPL-R5 under NAT; items 1, 4, 11, 12 and 22 on countable carriers.
- *Exposes a hidden assumption (ii).* AW-1.
- **Gem under `PLAN.md` §5; output class ELABORATING.** The mathematics is elementary. AW-1 is
  BORDERLINE.

*Skepticism applied to the favourable branches.* Every candidate that produced a non-MIO or
non-DIO element (4a, 4b, 4c under R5a, 4d) did so by a choice not fixed by the substratum: an
interpolation branch, a visible-level extension, an undefined procedure, or a non-diagonal
representative. For the negative, the skeptical question is whether NAT smuggles in the
conclusion. It does not fix the extension on coherent inputs, which is what DET quantifies over.
It does fix that outcomes are configuration functions, which is the corpus reading (RA-1). Under
a nativeness criterion other than NAT the negative is not claimed (M4).

## 8. Established, Assumed, Missing

**Established** (this note, X, unreviewed; K and R at their sources' standing):
- SHARP, DET, RED and IDLE;
- the N2 table, at its sources;
- the verdicts of 4a–4g and passes 2 and 3;
- the W1 non-uniqueness example;
- the N6 table.

**Assumed:** KIN-B (I), LIN (I), TB (I), DEF (N), A2 (N), DEC (N), NAT (N, a reading; T-SUB′ not
adopted), LAW (N) and CNT.

**Missing:**
- **M1.** Measurable diffuse carriers. A definition of "positive extension of a deterministic
  measurable action" that does not make DIO-type definitional, and the statement under it. This
  bears on item 11 on measurable seed spaces, item 12 for diffuse K, OPRES U1′, and the
  uncountable configuration set of an infinite lattice once A1 is retired.
- **M2.** A countably infinite visible carrier with a non-normal hidden state (OPRES U1′(ii)).
- **M3.** Nonlinear state assignments.
- **M4.** The nativeness criterion. The negative is for NAT, and D5 is undecided.
- **M5 (physical mechanism).** A native configuration-level randomness at the total carrier of
  SHARP's form, with a non-classical extension rule. Its absence is the answer to Q. Supplying it
  is a change of the physical model and is not pursued.
- **M6.** A uniqueness theorem for the gate path, if `GR:290`'s wording is meant as uniqueness
  (W1).
- **M7.** Sufficiency of SHARP's conditions in general (minor mathematics).

No item here needs computation. None was run.

## 9. What this note does not do

It edits no manuscript, Lean module, accepted design, reviewed record or Issue. It runs,
redesigns and ranks none of H-F1, H-RC or T-WP. It adopts no premise and no nativeness
criterion, and posts nothing on #1169 or #1477.
