# AUDIT-C5 — cross-document consistency (§A.25) and §A.42 item 8 provenance

Snapshot: `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`. All manuscript citations are to
`git show origin/main:<path>` line numbers. Read-only: no repo edits, no builds, no computations. No
replacement wording is drafted; the owner decides corrections.

Abbreviations: Main = `papers/Main.md`, GR = `papers/GR.md`, Sub = `papers/Substratum.md`,
Intro = `papers/Introduction.md`, Comp = `papers/Computation.md`, Cplx = `papers/Complexity.md`,
FULL = `book/The-Incompleteness-of-Observation-FULL.md`, chNN = `book/chNN-*.md`.

Verdict vocabulary (per caller): **confirmed contradiction** / **not a contradiction** /
**needs owner judgement**. "Anchor" = the maintained, most careful statement (§A.25 step 2; rigor decides).
The audit names each defect and its anchor only. It proposes no repair: corrections are the owner's, and
none is authorized.

Revision r2 applies REVIEW-C5 (B1–B3, N1–N9). r1 is kept unchanged as `AUDIT-C5-r1.md`. Every site added in
r2 was re-verified at `5ce4f98e`.

Derived artifacts (§A.25 step 5): every `.md` site listed below has `.tex` and `.pdf` derivatives
(`papers/<X>.tex/.pdf`, `book/The-Incompleteness-of-Observation-FULL.tex/.pdf`) that carry the same text, for
example FULL.tex:17479–17480 (C5-1) and Main.tex:1848 (C5-5). The mirror lists below name `.md` sources only.

***

## C5-1 (MQ-21): composite factorization "derived from coupling-graph locality"

**Side A.** FULL:3714 (= ch14:50, byte-identical paragraph): "with composite-system factorization derived
from coupling-graph locality for spatially separated subsystems ([Main §3.1])".

**Side B.** Main:218 (inside Main §3.1, the section FULL cites): "That kinematic locality does **not**, by
itself, prove local tomography or that all visible composites and coherent interventions belong to one common
tensor-product quantum instrument category. The operational-completion characterization of §3.4 takes the
complex matrix kinematics as given, the tensor-product composite and with it local tomography included, and
deriving that kinematics is open". Main:652 (ii): the dependency graph gives exact dynamical causal
separation; "It does not alone establish statistical product structure after conditioning, local tomography,
or one common tensor-product instrument category."

**What is proved.** The coupling-graph cone lemma (Main:364) proves only that an intervention reading and
writing region A cannot alter components outside `B_G(A,k)` after k steps. The visible–hidden tensor product
is given by the Stinespring construction (Main:650 (i)). No result in the corpus derives visible-subsystem
composite factorization (in the instrument sense) from coupling-graph locality.

**Anchor.** Main:218 and Main:652 (body, scoped, maintained; the very section FULL cites). The anchor supports
side B.

**Classification: confirmed contradiction.** FULL/ch14 cite Main §3.1 for a derivation that Main §3.1
explicitly denies. The weakest reading of "composite-system factorization" (the vector-space identity
ℓ²(C₁×…×C_N) ≅ ⊗ ℓ²(C_k)) is true, but it follows from site factorization of the configuration space (a
posit of the spatial OI constitution, Main:364 "site factorization plus the graph"), not from coupling-graph
locality, so even that reading misattributes its source.

**Mirror sites.** FULL:3714; ch14:50 (identical). Related, different claim: GR:330 ("The tensor product
structure follows from the spatial product structure of the classical configuration space ... a consequence
of spatial locality in the classical substratum") — this is the kinematic Hilbert-space decomposition for the
lattice-regularized QFT, opened by its own scope sentence (operational composites "a separate question");
not a contradiction with Main:218, but it also attributes the product structure to "spatial locality" where
Main treats site factorization as a constitution posit (owner may wish to check). Same FULL paragraph also
says "unitary evolution under the reduced Hamiltonian" without the approximation scope of Main:342 (see C5-2).

***

## C5-2 (MQ-37): visible marginal "unitary (by construction)"

**Side A.** Comp:100: "the dynamics is unitary in the visible-sector marginal (by construction) — type-level
facts that alone do not bound complexity".

**Side B.** Main:342: "Even in the strictly frozen-bath limit (τ_B→∞) the channel is not unitary: it is a
mixture over the bath ensemble of bath-conditioned visible unitaries ... which dephases"; dynamics is
*approximately* Schrödinger only under slow-bath and weak-coupling conditions. Main:650 (i): the visible
channel Φ is a CPTP channel obtained by partial trace. Main:556: what is exact is a fixed-basis unitary/Born
*representation* (Q_fb) of the finite-horizon law, universal, not unitarity of the marginal dynamics.

**Anchor.** Main:342/650 (derivation of the channel). Supports side B. The book counterpart Comp:100 says it
"match[es]", ch14 §14.4 (ch14:68-76, FULL mirror), states the visible description as a density matrix whose
"mixedness" carries the hidden sector and admissible operations as CPTP maps — i.e. the book side is careful.

**Classification: confirmed contradiction** (literal reading). A charitable reading ("the marginal law admits a
unitary representation by the equivalence construction") is supported by Main:556, but that is not what the
sentence says, and the same Comp paragraph treats non-unitary CPTP evolution as ordinary (Comp:100, later
clause; Comp:104), so the paper is also internally inconsistent. Not load-bearing: Comp:100 itself says these
type-level facts do not bound complexity; the conditional BQP theorem (Comp:104) uses the model hypotheses,
not this clause.

**Mirror sites.** Comp:100 only (corpus grep for "unitary in the visible", "unitary (by construction)",
"marginal is unitary": no other site). Adjacent softer form: FULL:3714 / ch14:50 "unitary evolution under the
reduced Hamiltonian" (no approximation qualifier).

***

## C5-3 (MQ-02): unitary QM as "Chapter 1's framework input"

**Side A.** FULL:690 (= ch02:56): "(E1) Unitary quantum mechanics. The observed microscopic physics is described
by states in a complex Hilbert space evolving unitarily, with observables as self-adjoint operators and
measurement outcomes following the Born rule. This is Chapter 1's framework input."

**Side B.** Main:68: "These properties contain no quantum postulates. The claim is that quantum mechanics
*emerges* under the conditions below." FULL:684 (= ch02:50), six lines earlier in the same section: "Chapter 1
took a substratum (S, φ) as input and developed the emergent quantum description from it."

**Anchor.** Sub:76 (E1 as an *empirical input to the reconstruction theorem*, with no attribution to Main) +
Main:68 + Main:556/564 (Main delivers the universal fixed-basis representation; operational QM —
self-adjoint observables, general measurements — only under five completion conditions, none supplied by bare
OI). E1 as an empirical input of the reconstruction is legitimate (QM as comparison target/observed fact).

**Classification: confirmed contradiction**, on either reading of the sentence. Reading (a) "E1 is Chapter 1's
input" contradicts Main:68 and FULL:684. Reading (b) "E1 is what Chapter 1's framework supplies as input to
this chapter" overstates Main: E1 includes self-adjoint observables and full Born-rule measurement, which Main
reaches only under the completion conditions (Main:556, 564) and which FULL:3714 itself says C1–C4 do not
deliver. The sentence dates from the book's first commit (`334eef0a3`, 2026-05-14) and has not been revised.
The correction is the owner's.

**Mirror sites.** FULL:690; ch02:56. Paper counterpart Sub:76 has no such sentence (correct form).

***

## C5-4 (MQ-36): Main:712 drops GR's OI_Q qualifier on the full matrix algebra

**Side A.** Main:712: "the present framework derives the characterization of embedded observation directly from
the deterministic substratum. Its observable algebra on each finite region is the full matrix algebra on the
region's configuration space, and its infinite-region completion is a quasilocal C*-algebra ... (§3.4)."
FULL:2065 (= ch07:199): "The framework ... Its observable algebra on each finite region is a full matrix
algebra ... ([GR §3.3])".

**Side B.** GR:288 (after the boxed completion statement): "where OI_Q denotes the quantum-completed substratum
of the statements above — the current OI substratum together with continuous off-diagonal controllability —
and not bare observation incompleteness." Main's own §3.4 is consistent with GR: Main:584 takes "Hermitian
accessible menus spanning the full matrix algebra" as a hypothesis; Main:590 places the region completion
inside the quantum-complete-extension (OI⁺) discussion and states that the observer-level lift "derives
neither a non-monomial admissible operator nor the layer flow"; Main:592 shows complete passive observation
only for commutative algebras.

**What is proved.** `inclObs_*`, `closure_iUnion_stage`, `quasiState_unique`, `canonEquiv`, `phaseQ_ne_heisQ`
(OIBridge/QuasilocalAlgebra, QuasilocalCharacterization) are pure mathematics about matrix algebras on finite
configuration spaces; their reading as *the observer's observable algebra* requires OI_Q (GR:288).

**Anchor.** GR:288 (the explicit scope sentence) and Main:584/590 (Main's own hypotheses). Supports side B.

**Classification: confirmed contradiction (dropped scope qualifier).** The following sites attribute the full
matrix algebra as "its observable algebra" to the framework or "the present construction" without the OI_Q /
quantum-complete qualifier that GR:288 attaches and that Main:584/590 imply:
- Main:712;
- GR:368;
- FULL:2065 = ch07:199.

The four sites (counting FULL:2065 and ch07:199 separately) are classified alike. Each says "Its observable algebra on each finite region is the full matrix
algebra ... and its infinite-region completion ...". In each, the section citation ("(§3.4)" in Main:712,
"(§3.3)" in GR:368, "([GR §3.3])" in FULL:2065 / ch07:199) attaches to the completion clause only. GR:368 is the
source of the FULL:2065 paragraph and stands 80 lines after its own paper's scope sentence (GR:288), but it does
not repeat that sentence. A purely kinematic reading ("operator algebra on the region's Hilbert space") would be
true, but the reading on the page is "observable algebra" of the framework or construction.

**Stronger paraphrase.** ch09:298 = FULL:2765 (byte-identical paragraph): "The framework's visible-sector
observables form a finite-dimensional Hilbert space at any given time ..., with the observer's accessible
operator algebra being precisely the algebra of observables on this space." This is **confirmed contradiction
(dropped scope)**, and it is stronger than the other sites because it says "accessible". It conflicts with:
- Main:590: the observer-level lift "derive[s] neither a non-monomial admissible operator nor the layer flow";
- Main:592: complete passive observation exists exactly for commutative algebras;
- Main:218 (ii): "The stochastic data directly supply only configuration-diagonal random variables".

The anchor is Main:590/592. The correction is the owner's.

**Mirror sites.** Unqualified: Main:712, GR:368, FULL:2065, ch07:199, and (stronger) FULL:2765 = ch09:298.

Qualified by context (the "finite theory" sentence inside the OI⁺ paragraph): Main:590, FULL:500, FULL:5271,
ch01:165, ch19:126.

The symbol OI_Q occurs in no book file.

**Related sites (N9; overreach is the owner's judgement).** The same Main:712 paragraph also says:
- "the present framework derives the characterization of embedded observation directly from the deterministic
  substratum";
- "exact finite operational quantum mechanics follows only with the added principles of the quantum-complete
  extension (§3.4). The present framework's distinguishing feature is that it derives this content from a
  finite deterministic substratum."

Whether "this content" includes the operational QM, which the preceding sentence says needs the added principles,
is the same scope question as AW-C5-b. Parallel phrasings:
- SM:1472: "In the present framework the observer-essentiality content is derived from a finite *deterministic*
  substratum";
- Structure:108: "the framework's distinguishing feature is producing the consequences from a finite
  deterministic substratum without extra dimensions or stochasticity".

***

## C5-5 (MQ-25): Main:260 vs Main:262 on gap-degeneracy

**Side A.** Main:260 (end): "the idealized permutation dynamics has dilated eigenphases at roots of unity —
equally spaced, hence maximally gap-degenerate — so the lemma's genericity holds for the physical
continuous-time dynamics away from that idealized limit, not at it".

**Side B.** Main:262: "(In particular, single-cycle hidden dynamics does not [force G2 failure]: although the
unitary cycle operator has equally-spaced phases on the unit circle, the Hermitian effective generator Ĥ_eff
has real eigenvalues that are not equally spaced, and retains non-degenerate gaps after the trace-out.)"

**Analysis.** On their face the two sentences concern different operators:
- 260: the *dilated* spectrum used by the ancilla-marginal extension of the lemma, which per 260 is the emergent
  object;
- 262: the n-dimensional bath-averaged effective generator Ĥ_eff = H_V + Tr_H[V_int(1⊗ρ_H)] (Main:342).

**The corpus applies the label "G2" to the cycle operator.** Two code comments on main do so:
- `papers/oi_lattice_code/foundations/source_lift_probes.py:75-77`: "the SINGLE-CYCLE permutation -- the
  framework's idealized hidden dynamics, with its equally spaced eigenphases -- has NO deficit: G2 failure costs
  nothing for source-phase identifiability";
- `verification/lean/bohr_frequency_probe.py:2365-2368`: "its genericity fails AT the permutation limit
  (root-of-unity eigenphases: maximally gap-degenerate)".

Main:262 says single-cycle hidden dynamics does *not* force G2 failure, and "we are not aware of a structural
feature of the substratum that forces such failure systematically". Main:260 names such a feature for the
dilated (emergent) object.

**Findings.**
1. **Unsupported assertion.** 262's parenthetical has no support in the corpus: no proof, probe or kernel theorem
   for "Ĥ_eff retains non-degenerate gaps" under single-cycle hidden dynamics was found. I searched papers, book,
   `verification/`, `papers/oi_lattice_code/` and Lean; the reviewer's independent search agrees.
2. **The emergent object.** The exact reconstruction of the emergent (ancilla-marginal) object uses the dilated
   genericity that 260 says fails at the idealized limit. 262 does not address it.

Related: Main:718 and GR:589 say (G1)–(G4) "hold for all but a measure-zero set". That is true of Hamiltonians
generically, but per 260 the framework's own idealized dynamics lies in that set for the dilated spectrum.

**Anchor.** Main:260 is the better-supported statement. It is explicit, backed by `phaselock_probes.py` for the
witness shapes, and consistent with both code comments above.

**Classification.** The call depends on which operator G2 is read on in 262:
- **On the Ĥ_eff reading** (G2 for the bath-averaged effective generator, as 262's own sentence states): **not a
  contradiction**. Different objects; the unsupported-claim finding (1) stands.
- **On the emergent-object reading** (G2 for the generator whose spectrum the reconstruction of the emergent
  object uses, which is how the two code comments apply the label): **tension**. 262's "does not force G2
  failure" and "not aware of a structural feature" stand against 260 and against the code comments.

Which reading governs is **needs owner judgement**. The INV MQ-25 flag on the G1 sentence ("the partition acts as
a symmetry-breaking mechanism", unproved) also stands. The correction, if any, is the owner's.

**Mirror sites.** Main:260, 262 only (no book/GR mirror of the gap-degeneracy passage). Downstream statements of
genericity: Main:718, GR:20, GR:589, FULL:5852, FULL:6176.

***

## C5-6 (MQ-20 area): Intro:129 "condition 4 fails ... on every system with two or more states"

**Side A.** Intro:129: "Under the observer access stated in [GR §3.3], the operations such a rule supplies also
cannot shift the phase ... and so cannot produce the quarter-turn relative phase that full reversible control
requires; condition 4 therefore fails for them on every system with two or more states [GR §3.3]."

**Side B (as flagged).** `substratumGen_not_control` (OIBridge/StructuralClosure.lean:348) is stated on `Fin 2`;
Main:82, Main:584, GR:228 cite it "on the two-state carrier".

**What is proved.** The two theorems concern different classes:
- `substratumGen_not_control` (Fin 2): the *monomial substratum class with the phase intervention stipulated*
  (`phaseOperator_supplied`, StructuralClosure.lean:333). Failure is by lack of state mixing (`rot`).
- Intro's sentence concerns the class *without* the stipulated phase: "the operations such a rule supplies"
  under the stated observer access = the sourced, ones-fixing class. PhaseSource T1/T2
  (`onesFixing_not_phasesAvailable` at PhaseSource.lean:55, `permTheory_not_phasesAvailable_onesFixing` at :108):
  on every carrier with `2 ≤ card A` the sourced theory fails `PhasesAvailable`, exhibited at level 1.
- `permTheory_not_control [Nonempty A]` (SubstratumInterfaceAudit.lean:708) states the no-control result
  directly for every nonempty carrier. It is `permTheory_not_phasesAvailable` composed with
  `phasesAvailable_of_control` (RouteB.lean:218). The phase failure is exhibited at level 2, so the statement
  covers one-state carriers too; Intro's "two or more states" is weaker and consistent with it.
- `obs_not_control` (:856) is the same statement for `obsTheory 𝒮 = permTheory (Conf 𝒮)`.
- `permTheory_diagonal_only_scalar` (SubstratumInterfaceAudit.lean:675): every diagonal unitary available in
  the sourced theory, at every level n, has weights with pairwise nonnegative products, i.e. it is a global
  phase. This is the kernel statement that matches Intro's wording "cannot shift the phase of one state
  relative to another", for any relative phase and not only the quarter phase.
- GR:260 states the PhaseSource result in prose ("on every finite carrier with two or more states ... fails
  the requirement of a quarter phase"). It covers only the quarter phase, exhibited at level one.

"Condition 4" is `HasCompositeUnitaryControl` (Main:564 (iv)).

**Anchor.** GR:260 together with the kernel results above (PhaseSource, `permTheory_diagonal_only_scalar`,
`permTheory_not_control`). The anchor supports side A for the class Intro names.

**Classification: not a contradiction.** Intro:129 is correct for the sourced class; the Fin-2 theorem is about
the phase-augmented class, on which Intro makes no all-carrier claim. Minor citation gap only: no manuscript
cites `permTheory_not_control`/`obs_not_control`; GR:260 states the phase failure but not the step to (iv),
which Intro supplies by a one-line implication; nor does any cite `permTheory_diagonal_only_scalar` for the
any-relative-phase wording. (The generalization at Main:590, "even with genuine hidden-memory", belongs to
cluster CI, not this item.)

**Mirror sites.** Intro:129 only (Intro has no book mirror). Related: Main:82, Main:584, GR:228 (Fin 2,
phase-augmented class), GR:260.

***

## C5-7 (marker MQ): classical memory equated with interference/coherence

**Sites (side A).**
- Cplx:236: "The framework identifies QM with the statistics of read-write cycling ... the resulting statistics
  are the ones quantum mechanics represents".
- FULL:542 (= ch01:207): "none of the interference phenomenology the framework attributes to hidden-sector
  memory".
- FULL:544 (= ch01:209): "what coupling produces is the memory-bearing quantum phenomenology".
- FULL:546 (= ch01:211): "The apparent quantumness of the world is a signature ... of our non-isolation".
- FULL:548 (= ch01:213): "Quantum mechanics is the dynamics that *embedded* observers see when they are coupled
  to the substructure".
- FULL:568 (= ch01:233, C3 limit): "No memory-bearing sector ... and no interference phenomenology, but for a
  different reason than in the C1 case".
- Structure:887: "Where the main paper identifies QM with embedded observation — 'observation occurs' plus
  structural conditions — ...".
- FULL:560 (= ch01:225): "decoherence is the transition from the memory-bearing regime back toward the C2
  failure limit ... systems isolated from fast baths retain quantum coherence."
- FULL:592-596 (ch01 mirror): "memory-bearing dynamics", hedged by "representation universal" (596).
- Main:674: "averaging over a fluctuating quantity ... yields the memory-bearing non-Markovian statistics that
  quantum mechanics represents."

**Side B (anchor).** Main:340 (three notions kept apart): accessible non-Markovianity "says nothing about a
quantum channel ... No unconditional implication among the three is asserted". Main:326: "(C1)–(C4) ...
neither contain nor imply a coherence requirement". Main:656 (iv): "operational interference and entanglement
predictions require in addition the instrument and observable structure of the operational bridge,
characterized conditionally and with [physical sourcing open]". Main:556: Q_fb is universal — "Markov and
memory-bearing laws alike lie in Q_fb". Main:592: "Passive incompleteness is therefore not evidence for a hidden
ontology, and nothing here says that quantum mechanics rests on observation incompleteness". This is the most
direct anchor against "QM = observation" readings. Main:720: on coherent inputs the memory classification "depends on the
realization rather than on the visible law". Book careful form: FULL:654 (= ch02:20) "The observer-level
statistics of this read-write cycle have an exact finite quantum representation"; FULL:3035 (= ch11:18) "the
read-write cycle as the realization's mechanism picture".

**Classification, per site.**
- FULL:560 / ch01:225 — **confirmed contradiction** with Main:326: "systems isolated from fast baths retain
  quantum coherence" makes slow bath (C2) sufficient for coherence; Main:326 says (C1)–(C4) do not imply it.
- FULL:542 / ch01:207, FULL:544 / ch01:209, FULL:568 / ch01:233 — **confirmed contradiction** with Main:656 and
  Main:340. Interference is attributed to hidden-sector memory: 568 places the absence of interference
  phenomenology alongside the absence of the memory-bearing sector, "for a different reason than in the C1
  case". Main says interference predictions need the operational bridge, which is open and conditional, and
  that accessible memory says nothing about a quantum channel.
- Cplx:236 — **confirmed contradiction** with Main:556 and Main:592. It says the framework "identifies QM with"
  read-write statistics, whereas Main shows only a universal representation (Markov laws included). Main:340
  keeps memory and quantum notions apart, and Main:592 states that "nothing here says that quantum mechanics
  rests on observation incompleteness". No book mirror; the book counterpart ch11:18 is the careful
  "mechanism picture" form.
- Structure:887 — **confirmed contradiction** with Main:556 and Main:592, on the same logic as Cplx:236. This is
  paper-register text attributing to Main ("Where the main paper identifies QM with embedded observation") a
  claim that Main explicitly withholds. It is at least as strong as Cplx:236. No book mirror found.
- FULL:546 / ch01:211, FULL:548 / ch01:213, FULL:592-596 — **needs owner judgement**. These are in essay
  register, and 596 carries the "representation universal" hedge. The readings "quantumness = non-isolation" and
  "QM is the dynamics that embedded observers see when coupled" are unsupported in the strong sense, but they
  are framed as interpretation.
- Main:674 — **not a contradiction** literally ("represents" is true by Main:556's universality), but in the same
  paper Main:684 ("The interference pattern arises because opening or closing the second slit changes the
  boundary conditions of the transition matrix ... eliminating the interference terms") asserts a mechanism for
  interference without a supporting theorem, in tension with Main:656 — **needs owner judgement** (MQ-09).

**Other occurrences to include in any propagation sweep:** Cplx:276, Cplx:348 ("QM is not a fragile state that
biology must protect from decoherence"), Medicine:552, FULL:4868-4876, FULL:6544 (= appendix-c:315, quoted as
an objection), and two softer "memory-bearing quantum phenomenology" sites:
- FULL:2483 = ch09:16 ("... with its universal representation");
- FULL:6337 = appendix-c:108 ("would produce the same memory-bearing quantum phenomenology").

***

## C5-8 (marker PC): per-context realization (Sub:126 vs Intro:137)

**Side A.** Sub:124-126 (Stage 1 Output): "There exists a triple (S, φ, V) ... such that: The observed quantum
dynamics is the reduced description obtained by tracing out S∖V from the deterministic evolution under φ."
Mirrors: FULL:724 (= ch02:90) "The output of Stage 1 is a triple (S, φ, V) ... with the observed quantum
dynamics reproduced as the marginalization of φ over the hidden sector".

**Side B.** Sub:137 (Sub's own Derivation): "The observed quantum dynamics provides, for each finite experimental
context, a stochastic law ... By [Main]'s finite-horizon equivalence ... the temporal law admits a realization";
Sub:141 Status: "Theorem for the scoped finite dilation datum". Intro:133-137: the correspondence "chooses a
hidden world for each finite pattern ... Choosing a separate world for each observed pattern supplies no common
physical interface".

**What Main proves.**
- (a) Exact realization per law: the equivalence, Main:556; Main:733, "per accessible horizon".
- (b) One finite reversible realization at accuracy ε for a fixed finite instrument family and horizon. This is
  the gluing theorem, Main:566-584, and it includes incompatible measurements.
- (b′) One finite reversible realization that is mutually ε-dense at horizon K for **all** instruments on ℂ^d
  with at most m outcomes. This is the uniform continuum theorem, Main:598: an ε-common realization over the
  continuum family, not only over a fixed finite family.
- In (b) and (b′) the quantum structure is supplied, not derived. Main:582: "Quantum mechanics enters as the
  instrument data and as the state held in the hidden register". The common realization therefore stores the
  quantum state as hidden data as well as taking the instruments as input (quantum-import, audit dimension A1;
  this is not the finiteness axiom A1 of Sub:122).
- (c) No fixed finite realization exactly reproduces even one qubit's full theory (Main:560; the unboundedness
  is imported from [55]).
- (d) Main neither proves nor excludes an *exact* common realization for a fixed finite noncommuting family.
  That question is open.

**Anchor.** Sub:137/141, Main:560/566/598 and Intro:133-137, which are consistent with each other. The anchor
supports this scoped statement:
- exact realization per finite context;
- a common realization at finite accuracy only, uniform over all ≤m-outcome instruments at fixed d, K, ε (via
  Main's gluing and uniform-continuum theorems, which Sub's derivation does not invoke), with quantum
  instruments and state held as hidden data;
- an exact common realization for a fixed finite family: open;
- no exact realization of E1 as a whole.

**Classification: confirmed contradiction (scope).** Sub:126, FULL:724 and ch02:90 state a single triple. That
is inconsistent with their own derivation and status lines, and with Main:560 if "the observed quantum
dynamics" means E1 (full QM, Sub:76). It is not a contradiction with Intro:137, which states the anchor's scope.
Which reading of Sub:126 is intended is the owner's judgement; the correction is the owner's.

**Correction to the phase-1 PC marker** (INV-MANUSCRIPT summary item 7, "no common realization across
noncommuting contexts"). The marker is too strong. Main:598 gives one realization that is ε-common over all
≤m-outcome instruments on ℂ^d at horizon K. What Main excludes is exact reproduction of the full theory by one
fixed finite realization (Main:560). An exact common realization for a fixed finite noncommuting family is
neither proved nor excluded: it is open, and this correction is not an exact per-family positive. Every common
realization Main supplies holds the quantum state in a hidden register and takes the instruments as data
(Main:582). The label "PC" is the phase-1 marker name and is unrelated to Sub's axioms.

**Mirror sites.** Sub:126; FULL:724; ch02:90. Related summary: Methodology:339 ("The reconstruction yields ... a
finite set with a bijection ...").

***

## Provenance items (§A.42 item 8)

Reachability checked with `git merge-base --is-ancestor <c> origin/main` and `git branch -r --contains` over the
439 fetched `origin/*` refs (794 refs total). Unfetched PR heads were not searched.

### P1 — composition-access `README.md:10-11, 18-24` (mutable record; not in legacy-records, no receipt)

README (blob `0c0d8b25`, byte-identical to #912's `2af1d5d5`) names `CURRENT-HANDOFF.md` (:10-11, "states the
results and their scope") and seven packages (:18-24: `native-x-v2/`, `tagged-post-y-v3/`, `native-phase-v4/`,
`native-coupling-v5/`, `composition_flag_v6/`, `delayed_history_v7/`, `native_predicate_v8/`) plus their plan
and review commits (`8d1150fe`, `75619cb7`, … `fc452ea8`). None is on main (`git ls-tree`); `2af1d5d5` is NOT
an ancestor of main; it is contained in `origin/pr912`, `origin/draft/oi-composition-access-20261024`,
`origin/pr935`, `origin/research/np-avg-1-plan-20261026`. The directory's own `SCOPE.md:15-22` (on main)
already records exactly this.

- The README's per-package result summaries (e.g. v5 "whole-port leak", v8 "negative", v6 "conditional complete
  pointer/carrier law") and `CURRENT-HANDOFF.md`'s results: **support off main** — results stated on main whose
  content is only on #912's branch. No manuscript (papers/book) uses them (grep). Gap remains open unless the
  owner treats SCOPE.md's "not on main" statement as the narrowing (it states location, not status).
- Incoming use: `substratum/continuous-substates/native-setting-source-feasibility.md:40-41, 50` cites
  `composition_flag_v6/REPORT.md` at `2af1d5d5` ("A supplied logical circuit/compiler target, explicitly without
  native gate compilation ... not an available actuator for this source variant"; "that draft is not adopted
  here"). Its conclusion is scoped to the audited contract that excludes v6 → **provenance**, borderline: the
  characterization of v6's content is itself read from off-main content.
- Incoming use: `oi-qm-ext-1/composition-source-map.md:64` cites `REPORT.md` at `2af1d5d5`, blob `2f77fe2f` =
  main's blob → **support on main**. The same row also characterizes off-main content: "The distinct
  composition_flag_v6/REPORT concerns a logical acceptance circuit" → **provenance**, borderline in the same way
  as the native-setting citation.
- Incoming use: MR-1 records cite #912's top-level `REPORT.md` at `2af1d5d5`:
  - `measurement-record-formation/preregistration.md:87` ("contract (1), freshness condition, countercontrols");
  - `amendments/MR-star.md:827` ("`git show 2af1d5d5:` of #912's `REPORT.md` (equation (1))");
  - `amendments/stage1-log.json:725`.

  That blob (`2f77fe2f`) is on main → **support on main**, consistent with the REPORT-level row below.
- All 18 plan and review commits named at README:17-24 (`a7f22c38`, `8d1150fe` … `fc452ea8`) are not ancestors of
  main (re-checked).
- Top-level `REPORT.md`/`checks.py`/`RESULT.json`/`review/` (used by MR-1 B2 etc., SCOPE.md:54-77): on main,
  same blobs → **support on main** (review is author-posted, SCOPE.md:42-44; a §A.46 status matter, not
  item 8).

### P2 — OI-CHANNEL-1 `result.md:35-38` (inventory said :33-35; frozen record, receipt `verification/receipts/OI-CHANNEL-1.json`)

Cites `research/archive/pt/R6/NOTES.md` at `e7d380fc` and `research/bridge/NOTES-B4.md` at `5f4089a4`. Both
commits NOT ancestors of main (`e7d380fc` ⊂ `origin/research/overview`; `5f4089a4` ⊂ `origin/research/bridge`,
`origin/dev-bridge/*`).

- **R6 NOTES (N2)** — **support on main**, both for the mathematics and for the "historical" identification.
  - The containment at :39-43 ("this cone is contained in the sum of the PSD cone and the conic hull of the four
    defect matrices used by ZF") needs the definitions of `Q3` and `Z_F`.
  - result.md gives only the formula `K(Z_F) = (Q3 ∩ Z_F*) + cone(Z_F)`, and the preregistration and
    `controls.py` define neither `Q3` nor `Z_F`.
  - The probe on main (`verification/lean/oi_channel1_check.py:171-176`) builds the four defect matrices in
    Pauli form, but not their identity with `Z_F`.
  - The generators `z_s = (E00 + s1 E13 + s2 E22 − s1 s2 E31)/4` are stated only in R6 NOTES N2, line 56 of the
    blob (checked with `git cat-file -p 62cdd798`).

  That blob (`62cdd798…`) is retained in main's history at `48b18ac5`, at
  `verification/audits/evidence-retention/objects/loose/62/cdd798…` with manifest entry path
  `research/archive/pt/R6/NOTES.md`. §A.42's closing paragraph designates that archive as read from main's
  history. It is held there as a git loose object, not a plain file; the reviewer inflated it and confirmed it
  byte-identical to `e7d380fc:research/archive/pt/R6/NOTES.md`. No open gap.
- **B4 NOTES** (blob `e44fed13…`, not in the archive manifest) — "used by B4's realization"; :45-46 states B4
  "retains its conditional branch-(a) scope; this citation does not extend it". The result uses no B4 content →
  **provenance**.
- Other off-main ids in the same record (:56-59 `e7d380fc` research/round7-channel/, `78aa5b25` prospective
  registration): content the claims need is on main — probe as `verification/lean/oi_channel1_check.py`, controls
  as `controls.py` (preregistration:47-50 SHA256s), ARGUMENT.md arguments restated inline → **provenance**
  (support on main for the landed files). F `a5aad0c1`, S1 `2d870fc5`, D `9f9f8257` are ancestors of main.
- Note: `bridge-compatibility-audit/result.md:236-246` (on main) records that R6 REASSESSMENT,
  INTEGRATION-NOTE-STAGE6 and `pt/T6/TEST.md` (closedness, CNOT, H3 self-duality for K(Z_F)) are not retained;
  OI-CHANNEL-1 does not use them.

### P3 — o-ret `README.md:40-45` `REVIEW-Q7.md` (mutable record)

`PREREG-PHASE-A.md:12` cites "Q7 review: `REVIEW-Q7.md` (2026-11-04)"; §2.7 (:158) "Q7, frozen wording (from
`REVIEW-Q7.md`; each CONFIRMED WITH NARROWED SCOPE) [U]"; items labelled `[U, Q7 F1/F2/F5]` (:70-81, 269-358).
Independently confirmed: no file matching `*REVIEW-Q7*` in the history of any fetched ref
(`git log --all -- '*REVIEW-Q7*'` empty). The wording that Phase A uses is on main (§2.7 and the [U] items), and
the preregistration labels it **[U] unreviewed** (:14-16), so no claim relies on the review's verdict. Phase A's
earned claim is calibration only (README:8-11). → **provenance** for the review; the specification content used
is **support on main** (as unreviewed text). Residual: "CONFIRMED WITH NARROWED SCOPE" attributes a review
verdict that cannot be verified from main; harmless while every use is labelled [U]. README:40-45 already
states this accurately.

***

## Summary (≤ 25 lines)

Eight candidates and three provenance items, checked at `5ce4f98e` (r2, after REVIEW-C5).

**Confirmed contradictions (5)**
- C5-1: FULL:3714 = ch14:50 cites Main §3.1 for composite factorization that Main:218/652 deny.
- C5-2: Comp:100 "unitary in the visible-sector marginal (by construction)" vs Main:342/650; single site.
- C5-3: FULL:690 = ch02:56 "Chapter 1's framework input" vs Main:68 and FULL:684, or overstates Main:556/564.
- C5-4: Main:712, GR:368, FULL:2065 = ch07:199 drop the OI_Q scope of GR:288 and Main:584/590. The stronger
  FULL:2765 = ch09:298 ("accessible operator algebra ... precisely") conflicts with Main:590/592/218.
- C5-8: Sub:126, FULL:724 = ch02:90 single triple vs Sub:137/141 and Main:560.

**C5-7, per site**
- Confirmed: FULL:560 (vs Main:326); FULL:542, 544, 568 (vs Main:656/340); Cplx:236 and Structure:887 (vs
  Main:556/592). Book mirrors are ch01:225, 207, 209, 233.
- Owner judgement: FULL:546, 548, 592-596 and Main:684. Main:674 is literally consistent.

**Not contradictions, or reading-dependent**
- C5-5: not a contradiction on the Ĥ_eff reading. On the emergent-object reading it is in tension with Main:260
  and two code comments; owner judgement. Main:262's gap claim is unsupported.
- C5-6: Intro:129 is correct for the sourced class (PhaseSource; `permTheory_diagonal_only_scalar`;
  `permTheory_not_control`).

**PC marker.** Overstated. Main:598 gives one realization that is ε-common over all ≤m-outcome instruments at
fixed d, K, with the state in a hidden register and the instruments supplied (Main:582). An exact common
realization for a fixed finite family is open; exact reproduction of the full theory is excluded (Main:560).

**Provenance**
- P1: package summaries and CURRENT-HANDOFF are support off main. The v6 characterizations are borderline
  provenance. REPORT-level uses (MR-1 ×3, composition-source-map) are support on main.
- P2: R6 N2 is support on main (archive `48b18ac5`, blob `62cdd798`), containment step included; B4 is
  provenance. P3: REVIEW-Q7 is provenance; the wording used is on main, labelled [U].

## Cross-cluster assumption-watch markers

- **AW-C5-a (representation ≠ dynamics).** "Unitary" is used for the Q_fb representation and for the visible
  dynamics interchangeably (Comp:100, FULL:3714). Any cluster citing "unitary evolution" from OI should check
  which is meant (Main:342 vs Main:556).
- **AW-C5-b (dropped OI_Q / OI⁺ scope).** Results proved for the quantum-complete extension are restated as
  properties of "the framework":
  - Main:712, GR:368, FULL:2065;
  - "accessible operator algebra" at FULL:2765;
  - "derives this content from a finite deterministic substratum" at Main:712, with parallels at SM:1472 and
    Structure:108.

  Check every downstream use of the region completion, `canonEquiv` and `driveQ_*`. The search must be by
  meaning, not by phrase: FULL:2765 uses neither "full matrix algebra" nor "observable algebra".
- **AW-C5-c (class identity in no-control results).** Sourced (ones-fixing) class vs phase-augmented monomial
  class: carrier generality differs (any carrier vs Fin 2). Clusters on CI/no-go scope should name the class.
- **AW-C5-d (memory → coherence/interference; QM = observation).** Book ch01 §1.10, Complexity, Medicine and
  Structure:887 assert links that Main:326/340/592/656 withhold. Affects A5 assessments of biology, medicine, decoherence readings.
- **AW-C5-e (per-context vs common realization).** Stage-1 Output and similar summaries state a single triple;
  Main supplies per-law exact, ε-common for fixed finite families, and an exact-uniform obstruction. Cite the
  appropriate one.
- **AW-C5-f (genericity at the idealized limit).** "(G1)–(G4) hold except on measure zero" (Main:718, GR:589),
  while the framework's own permutation dynamics lies in the degenerate set for the dilated spectrum. Main:260
  and two code comments say so: `source_lift_probes.py:75-77` and `bohr_frequency_probe.py:2365-2368`. Main:262
  says the opposite for Ĥ_eff, without support.
- **AW-C5-g (common realization stores QM as hidden data).** Every common, multi-context realization Main supplies
  (Main:566-598) takes quantum instruments as data and holds the quantum state in a hidden register (Main:582).
  It is quantum-import (audit dimension A1), not native emergence.
