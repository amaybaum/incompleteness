# Independent full-text review of APPROX-UNIT1 r4

**Publication copy.** Two session-specific location references are described generically. The unaltered original review is retained at `4e526de57b0a4fedf7821d63722a1733c0f49298`, SHA-256 `e2749ff93827e368d375e0329fa9f70804fb6b4099ae5114c13f894dd707cb5a`. Verdict, findings and scientific content are unchanged.

**Verdict: ACCEPT WITH NITS, for this paper-only assessment. No blocking scientific finding remains.**

Reviewer: fresh independent non-author Codex task `review_approx_r4`, 2026-11-09. I authored none of r1–r4 or the disposition ledger. I read all 913 lines of r4 and all 26 lines of its ledger, then examined the supporting statements, proof bodies, recorded scripts and outputs described below. The writer's disposition claims were review targets, not evidence of acceptance.

This verdict accepts the assessment at its stated precision, carrier, access and evidence levels. It does not accept an OI derivation of quantum mechanics, settle the open fixed-b bound, certify a new kernel theorem, authorize computation, adopt a physical premise, or authorize a manuscript/repository/GitHub change, freeze, designation, dispatch or merge.

## Reviewed identity and comparison limit

| Input | Lines read | Independently measured SHA-256 |
| --- | ---: | --- |
| `APPROX-UNIT1.r4.md` | 913 | `cb5c4c6a37d3a5ab321b4ad0aba464104aeed4b1d9c57c298704b376b2269b44` |
| `DISPOSITIONS-APPROX-UNIT1.r4.md` | 26 | `ef669e30e72c71e17db058081c05934abab098d4561aa60c4599a43fd982897a` |

The manuscript/formal-source pin reviewed was **`fd539e150759a6ea51ab279aeeac80fc06050ade`**, read using `git show`/`git grep` at that commit. In particular, pinned `papers/Main.md` has SHA-256 **`6144cd4a6324599d5178f844201551670ef470d4ed130c0b6ce23622a3be6366`**. I did not substitute the mutable checkout for that source. The checkout remained at `c10609e6c85b332f725f490b969e23de16a1109c`, with no tracked working-tree or index changes from this review.

The off-main handoff evidence was read at **`820519cf011c09b37690213a758106ed3aa15cc2`**, and the MATH-CON-1 control plane at **`a44c0206f2c3519944eb31a5eca361eeff2c4be8`**. The earlier epsilon proof review was fetched at the distinct ref `6d494e30` and its actual migrated repository path.

The r3 artifact and its original independent review were not supplied. I therefore do **not** certify a byte-diff against r3, the hashes of those unavailable files, or exact fidelity of the writer's R1–R6 descriptions to that unavailable review. This does not prevent an independent full-text scientific assessment of r4 and of the six resolutions the supplied ledger actually states.

## Blocking findings

**None.** The main conclusions have adequate paper/source support on their expressly restricted scope. The three local issues below should be corrected in a subsequent writer pass, but none changes the Level-A result, the failure to meet OI-derived Level B, or the repaired implications and metric distinctions.

## Nonblocking corrections

### N1. One bracket still ambiguously attributes the two-outcome numbers to the earlier proof-review commit

**r4 anchor:** lines **245–251**, specifically line **247**: `[OFF: #945 c.6567879503 §2, record at 6d494e30]`.

The immediately following lines 249–251 correctly distinguish the two sources, as do the reference table at 203–207 and D4a at 668. Nevertheless, the bracket at 247 still invites the exact misattribution the revision says it corrected.

**Source check:** [#945 c.6567879503](https://github.com/amaybaum/incompleteness/issues/945#issuecomment-6567879503), §2, gives the d=4, b=24, two-outcome assessment instance, **6.9063 versus 4.0000**, and explicitly credits its assessment-review checks R-1/R-2. The fetched comment's lines 35–37 contain that attribution. Its lines 50–51 distinguish the invalid per-parent step from reachability and the final TV bound. The earlier [proof review at `6d494e30`](https://github.com/amaybaum/incompleteness/blob/6d494e30/verification/audits/manuscript/intro-corpus-audit-20261026/proofs/eps-realization/REVIEW.md), lines 146–160, instead records an outcome-free d=4, b=16 example with **8.0022 versus 4.0016**. The assessment also identifies the older d=4 parent's non-dyadic entries; that older number must not silently become a certified fixed-point witness.

**Safe correction:** remove `record at 6d494e30` from the bracket at 247, leaving the assessment comment as the source of the quoted pair. Keep the separate sentence identifying the earlier review and its different figures.

**Why nonblocking:** r4 already gives the correct source and the correct distinction several times. This is a residual local citation ambiguity, not an unsupported new numerical conclusion.

### N2. The uniform-theorem probe instances are numerical, although their evidence tag is defined as exact

**r4 anchors:** definition of **[X] at line 120**; A3 evidence at **231**; D6 at **672**.

The A3/D6 cells cite `opglue_probes.py` checks 8–9 under [X], whose definition is “exact computation recorded on main.” Those particular checks use floating-point arithmetic.

**Pinned source check:** `papers/oi_lattice_code/foundations/opglue_probes.py` at `fd539e15`, lines **256–309**. Lines 262–270 convert the ring matrices to floats and compute a floating-point operator norm; line 279 computes TV using floats; lines 285–287 build the off-net target using `math.atan2`, `math.cos` and `math.sin`; lines 282 and 308 use a `1e-12` tolerance. The exact ring used in other parts of the script does not make these computations exact.

**Safe correction:** label checks 8–9 as numerical instance checks, retaining **[P]** for Main:596–600's paper proof. Introduce a numerical tag if desired, or state the numerical qualification directly in those two cells. Reserve [X] for the checks whose deciding arithmetic is exact.

**Why nonblocking:** the uniform realization and adaptive telescoping conclusions have independent paper proofs, checked below. These floating-point instances are not needed to certify an exact identity, exact rank, or universal error bound. Relabelling their evidence does not narrow the proved theorem.

### N3. The CM witness is admissible; it is not generated as an available branch

**r4 anchor:** lines **477–479**, especially “so K enters genTheory CM only through products and ancilla blocks”.

The countermodel correctly needs only a nonmonomial **admissible** operator for FI-1. The quoted sentence suggests that this particular K is nevertheless generated through the remaining constructors. That suggestion is false on the definitions being used.

**Source/hand check:** `InstAvail.op` requires an isometry (`ImplementationLocality.lean:271–272`). A square column-monomial isometry is monomial: orthonormal columns cannot share their single nonzero row, so those rows form a permutation and the entries have unit modulus. The other primitives are readout projectors. Products, scalar multiples and ancilla blocks of monomial operators remain monomial (`StructuralClosure.lean:197–238`), while coarse-graining sums branches rather than operators. Induction over `InstAvail` therefore gives a monomial Kraus representation for every available branch in `genTheory CM`.

For K=|0⟩(⟨0|+⟨1|)/√2, `Ad K(|0⟩⟨1|)=|0⟩⟨0|/2`. Every conjugation by a monomial operator sends an off-diagonal matrix unit to an off-diagonal matrix unit or zero; every finite sum of such conjugations has zero output diagonal on that input. Thus this K's conjugation is unavailable as a branch, even though K belongs to CM. No computation or enumeration is needed for this distinction.

**Safe replacement:** “K is an admissible nonmonomial FI-1 witness. It is not an isometric primitive, and no availability of its conjugation is claimed or needed. Every available branch of genTheory CM preserves diagonals.” Removing the assertion that K enters the generated theory preserves the countermodel conclusion.

**Why nonblocking:** FI-1 was explicitly defined at lines 450–452 by admissible-operator membership, and the countermodel at 468–476 proves precisely the claimed failure of sufficiency. That proof survives intact; the extra availability explanation is unnecessary.

## R1–R6 resolution assessment

| Ledger item | Independent assessment of r4 |
| --- | --- |
| **R1: the existing target is OI-derived Level B** | **Resolved.** Lines 60–72 and 292–303 clearly distinguish a reusable supplied simulator from the accountable target. Lines 719–747 require a single physically sourced operational recipe across resources. OQ1 at 834–837 concerns evidence for implementation, not a decision to add derivation to the target. This matches the central question and Levels in #1216. |
| **R2: the exact FI-1 implication needs level-one transport** | **Resolved in substance.** Lines 453–467 prove the bare-S implication and explicitly retain the missing relabelling/`SystemToLevelOne` seam. Lines 480–500 separate level-one availability from full layer-flow executability and from native OI sourcing. The CM countermodel remains valid; N3 corrects its incidental availability sentence. |
| **R3: matrix distances versus complete-record distances** | **Resolved.** Lines 374–421, 566–602 and 749–759 repeatedly state the metric and interface limitations. The H/H,Z witness is a genuine recorded-law result on its fully identified two-configuration Markov interface, with the correct constant. Fixed-frame CNOT negativity is a conditional channel exclusion, not an all-entangling or observable-history theorem. |
| **R4: legal instruments, branch linearity and separate outcomes** | **Resolved.** Lines 364–387 and 528–558 distinguish linear subnormalized branches, legal coarse-graining and positive-mass normalization. The outcome table distinguishes native record validity, classical posterior closure, PSD closure, quantum compatibility and coverage. Product identification/H-LIFT are carried through the frame argument. Broader native product-test validity is not inferred from a few positive frequencies. |
| **R5: scaling recipe, complete histories and the existing rounds** | **Resolved.** Lines 707–765 distinguish the three test scopes, coverage over quantum targets and soundness over all admitted native uses. Detector-off/on is Q-C2-1 P's primary contrast; the shams have the correct control role. Q-C2-2 F1 is a one-read prepare–measure fragment. MATH-CON-1's first stage establishes no CT, spectator-form or approximation result by itself. D10 is explicitly carrier/horizon dependent. |
| **R6: finite-b limitations and witness provenance** | **Resolved in substance.** Lines 241–256, 543, 603–612 and D4–D5 preserve the exact-regime theorem and leave the fixed-b law bound open. N5 is a reachable one-step exact-PSD failure, not a law-level or asymptotic-closure counterexample. The two numerical records are correctly distinguished overall; N1 removes the remaining ambiguous bracket. N2 separately corrects the numerical/exact probe label. |

The ledger can therefore be accepted as an account of substantive repairs, with these local qualifications. This is not certification of the unavailable r3 comparison history.

## Scientific and source audit

### 1. Level A survives, with its exact precision and resource scope

I checked the pinned comb construction, gluing proof, single-dynamics corollary, telescoping lemma and uniform/density statements rather than treating their summaries as sufficient.

**A1.** Main:482–484 gives one independent response coordinate for each action/history context, with its marginal equal to the prescribed conditional. A coordinate used at a later, longer context is independent of the previously exposed coordinates. The chain-rule argument therefore covers adaptive choices as well as fixed action sequences. Main:520 allows arbitrary real priors, so exact finite-law realization is not restricted to rational quantum probabilities. Loading quantum conditionals is still loading quantum data. It is a representation/control result, not an OI selection argument.

**A2.** In Main:566–580 the exact branch matrix is updated by the supplied CP branch. Its trace ratios are the true quantum conditionals. A finite uniform seed grid changes an m-outcome conditional by at most `(m−1)/G` in TV; summing conditional errors over a depth-K adaptive tree gives `K(m−1)/G`. The predecessor stack supplies reversibility even for noninjective multi-Kraus updates. Finite injective dynamics on the well-formed reachable domain can be completed to a finite bijection. This argument does not require a continuum of primitive coherent controls.

For exact PSD closure, each selected branch is CP, legal coarse-grainings are sums of branches of one instrument, and division by a positive branch probability preserves PSD. A zero-probability quantum branch is not a normalized heralded state. These facts justify the exact-regime cells at r4:542 and 544 independently of any claim about the fixed-point implementation.

**A3.** Main:596 views each instrument as a channel into a classical–quantum record. A hybrid argument bounds the final classical TV error by the sum of instrument diamond errors uniformly over retained side systems and adaptive continuations. With `δ=ε/(2K)` and `G≥max(1,ceil(2K(m−1)/ε))`, net rounding and seed rounding cost at most ε in total. Conversely, a simulator protocol uses genuine net instruments and is close to the corresponding quantum protocol. This supports the fixed-(d,m) finite-test density statement. It does not establish exact identity of the full deterministic class with quantum theory.

The source's stated bit budget and r4:232 also keep transition-description size separate from hidden-register capacity. An exact reachable-set alphabet is finite, but this is not a bound on the computational bit complexity of arbitrary real input data. For an existence-style capacity bound, unused stack slots can be padded with a fixed reachable value and their active length read from the visible counter; a separate empty symbol is not essential. The autonomous read-only policy is additional **hidden** state, correctly charged at r4:228 and 340–342.

The K≥1 and G≥1 conventions and the m=1 repair are sound. As usual, the logarithmic resource asymptotics concern the nontrivial small-error regime; an ε>1 request can use a construction for a smaller error. Nothing in the unit warrants retracting the established exact-regime Level-A claims because the fixed-b proof is open.

### 2. Level B: one physical recipe, two different worst-case obligations

#1216's central question already requires a mechanism derived from OI with independently justified observer access. The reusable quantum simulator has the operational shape described at r4:275–288, but its state register, Kraus dictionary, Born traces and tensor rule are supplied by QM. Main:582, 584, 598 and 602 support the negative Level-B verdict at r4:292–303.

The quantifier order in r4:719–747 is appropriate. One physically sourced rule for operations, access, preparations, system identification, history decoding and resource scaling must be fixed first. The quantum formulas may specify the benchmark; they must not supply the physical dictionary. A resource-dependent encoding is permitted when the common rule determines it, rather than being fitted separately to a target or tolerance.

For a fixed declared experimental envelope E, let `Q(E)` be its target protocols and `N_r(E)` its admitted native uses at budget r. A predeclared correspondence can be expressed as `Γ_r⊆Q(E)×N_r(E)`. The coverage obligation is the worst quantum target's best admissible match:

`C_r = sup_{q∈Q(E)} inf_{n:(q,n)∈Γ_r} TV(P_q^Q, P_{r,n}^N)`.

An empty matching set is failure, not zero error. Soundness is a separate worst case over **all** `n∈N_r(E)`, compared with the quantum law assigned by the same recipe. An admitted native use without a comparator is failure. The family must supply, for each E and ε>0, a budget with both errors ≤ε. This is the draft's proposed assessment of the existing target, not a proved OI premise.

The complete-record requirement includes observable failed attempts, heralds, resets, continuations, settings and stopping/abort events. It prevents conditional-only agreement or deletion of failed uses from becoming an apparent success. The inequalities at r4:749–765 are correct: bounded statistics are Lipschitz in TV; two local-history laws each ε-close to the same quantum marginal differ by at most 2ε; a conditional witness without a herald-mass floor need not give a full-law floor; adaptive telescoping needs uniform bounds in the retained context and side systems.

These quantifiers neither show an OI realization nor prove a resource-uniform obstruction. The missing sourcing and uniform bounds remain missing. #945's implementation-specific repair is not a logical prerequisite for investigating other sourced families.

### 3. NX-1, bare-system soundness and the exact FI-1 seam

The actual formal sources support r4's narrowed implication.

- `ImplementationLocality.lean:250–253` defines `Realized` as a finite sum of conjugations by admissible operators.
- `Architecture` at 506–516 has identity, multiplication, contractive scalar, ancilla-projector and ancilla-block fields. It has **no** relabelling field.
- `realized_of_instAvail` at 530–538 proves branch soundness from those fields.
- `genTheory` at 852–884 makes bare-system availability `InstAvail` on S. Its preparations are a uniform attachment followed by an available one-outcome level operation, and its preparation/discard rule is explicitly built using `InstAvail.discard`.
- `discardWith_uniform_conjChannel` at `AncillaClosure.lean:461–480` gives the `1/n`-weighted sum over ancilla blocks.

Consequently, a **system-induced available branch on bare S** that breaks diagonal preservation has a nonmonomial bare-S admissible Kraus witness: if every soundness witness were monomial, each conjugation and their sum would preserve diagonals. This is a valid hand composition of the cited kernel lemmas. It is not a new kernel-certified theorem.

Moving that witness to the exact FI-1 carrier `S×Fin 1` needs a transport hypothesis. `LabelInvariant` is a separate predicate at `ImplementationLocality.lean:364–366`; `SystemToLevelOne` is the opposite-direction availability principle at `LevelOneSeam.lean:117–119`. The structural direction from level one down to the system alone does not supply the converse. Alternatively, a higher-level coherent output may lose its off-diagonal terms under partial trace, so an arbitrary higher-level witness first needs a system reduction that detects its coherence. Lines 461–467 correctly retain both limitations.

The CM countermodel is mathematically valid at the declared admissibility/architecture level. Products, scalar multiples, projectors and ancilla blocks preserve “at most one nonzero entry per column.” For diagonal D, the off-diagonal entry of KDK† is a sum of products from two different rows of a common column, all zero. The displayed rank-one K is CM but not monomial. Thus FI-1 alone need not give a non-diagonal-preserving available branch. N3 removes an unnecessary false suggestion about that K's availability.

`ExecSource.lean:52–70` uses an available half-time gate flow **at level one** and a moved configuration to infer a nonmonomial admissible operator there. `LiftAudit.lean:112–120,155–178` supplies the availability predicate and half-time diagonal-breaking witness. Its unitarity statement also needs the involution hypothesis, which r4 explicitly carries at 480–484. The necessity cited in D15 must be read with that nontrivial/moved-point setting, not as a claim about a singleton bare carrier.

The polarized separation is likewise correct and scoped: `C5Discovery.lean:325–333` makes the half-time swap flow available in `polarizedTheory (Fin 2)`, while `PolarizationClosure.lean:379–398` excludes full layer-flow executability through countability up to scalar. The added shear/Hadamard images are not sourced by native OI. R4 does not convert this comparison of predicates into an OI mechanism or an unconditional strict ordering of all obligations.

### 4. Matrix separation and the narrow observable-law witness

The trace-norm witnesses are correct. For any diagonal D, `tr((|+⟩⟨+|−D)X)=1`, so the trace norm is at least 1 and trace distance at least 1/2. The same argument applies to x+⊗z+ with X⊗Z, and to y+⊗z+ with Y⊗Z. A real symmetric state has zero Y expectation, yielding the corresponding reality-preservation separation. These statements concern the declared matrix identification; native accessibility of X, Y or the joint effects does not follow.

The separate H/H,Z argument at r4:404–416 is a genuine observable-law calculation. With exact preparation 0, exact Z read, and one two-state stochastic map T reused without retained memory, write `p=T(0|0)` and `q=T(0|1)`. The two TV errors are

`e1=|p−1/2|`, and `e2=1−p²−(1−p)q≥p(1−p)`.

For `g=(√2−1)/2`, `g=1/4−g²`. If `|p−1/2|<g`, then `p(1−p)>g`; otherwise `e1≥g`. At `p=1/√2,q=1` both equal g. Thus the minimax floor and its constant are correct for the stated stochastic class. That class includes the more restrictive two-point permutation implementations; the attaining stochastic map is not asserted to be a native shuffle.

The proof does not extend when the carrier itself hides more configurations under a coarse readout, when preparation/readout change, or when memory correlates repeated uses. R4 expressly says so. An injective encoding or an inaccessible mathematical separating functional alone is also insufficient for a complete-history floor at growing resources.

D10's separate periodicity argument is sound: every permutation of a fixed S has order dividing `L=lcm(1,…,|S|)`. A fixed repeated implementation therefore gives the same terminal read law at L and 2L, whereas the admitted rotation by π/L gives probabilities 0 and 1. At least one TV error is ≥1/2. The target operation and horizons depend on S; this proves no fixed-depth floor as resources increase, as r4:313–319 and D10 explicitly acknowledge.

### 5. R1, SIC and the conditional CNOT channel exclusion

I checked the definitions against AP1/MECH-2 and the recorded frame scripts. In AP1's `(Z,X,Y)` component order, write `v(z,x)=((-1)^z,(-1)^x,(-1)^(z+x))`. The R1 reconstruction is `(I+v·σ)/2`, with dual functional `(I+v·σ)/4`; its reconstruction frame is orthogonal but its duals are not positive. The SIC dual is the positive effect `(I+v·σ/√3)/4`, with reconstruction `(I+√3v·σ)/2`, which is not orthogonal. R4 keeps these frames distinct.

For a single-qubit rotation O, the reciprocal scales cancel, so both frame matrices are `(1+v_i·Ov_j)/4`. The 12 tetrahedron rotations give permutations. The other half of the octahedral group maps the tetrahedron to its opposite and has an inner product −3, producing an entry −1/2. This supports the Hadamard/S and 12-versus-12 claims without identifying the two product-frame representations of every composite channel.

There is also a short exact CNOT certificate independent of the recorded minimum search. Let the reconstruction scale be s, with s=1 for R1 and s=√3 for SIC, and use its reciprocal in the dual. For input frame point `(00,00)` and output dual point `(01,10)`, Pauli conjugation by CNOT gives the entry

`M = (1−s−1/s)/4`.

It equals **−1/4** under R1 and **1/4−√3/3** under SIC. These are the exact minima reported in `r2_frames.py/.out`; negativity itself, which is what the exclusion needs, follows already from this one entry. Reversing CNOT orientation is a permutation of product-frame indices. SWAP and local tetrahedron rotations give the stated nonnegative countercontrols.

The fixed-frame state gaps also have the claimed normalization. The pure state `r=−v0/√3` has R1 coordinate `(1−√3)/4`; a Bell state has a product coordinate −1/8. The corresponding dual operator norms are `(1+√3)/4` and `(2+√3)/8`. Hölder's inequality therefore gives **trace-norm** separation `2−√3` in both cases, or half that in trace distance. R4 correctly calls this a trace-norm bound.

MECH-2 Lemma F's proof at 307–347 consists of nonnegative maps on signed laws, conditional on its operation set and H-LIFT. Its (a)–(b) proof does not need frame orthogonality; linear invertibility suffices for uniqueness, so the stated SIC extension is a valid paper extension. Orthogonality is used in U2's unitary/permutation argument at 441–453, and r4 correctly does not export U2 to SIC.

At every relevant cut the same product identification and the stated attachment/discard rules are needed, or correlated systems must remain in the carrier. Under those conditions, nonnegative frame matrices form a closed compositional class. A fixed negative CNOT entry excludes convergence to that channel in any fixed finite-dimensional channel norm. It does **not** exclude all entangling channels, production of a particular entangled state, or accessible CNOT correlations under a weaker menu. The distinction is carried at r4:595–602 and in D21/D27.

Every quantum joint state does have nonnegative product-SIC coordinates, as these are product POVM probabilities. Arbitrary classical point laws need not reconstruct PSD operators. Representation of states therefore does not supply a quantum effect menu, valid continuations, physical preparation or coverage. Main:562's sharp-effect response failure is an appropriate control.

### 6. The owner outcomes and finite-b evidence remain separate

For configuration-level generated theories, the normalization half is not inferred from CP: `instAvail_trace` at `ImplementationLocality.lean:317–345` proves it separately, and `cp_of_instAvail` at 540–545 proves CP. Monomial conjugations, uniform attachments and partial traces preserve diagonality (`SubstratumInterface.lean:126–144`; `DiagonalTheory.lean:193–236`). Thus the restricted quantum diagonal state space is exactly closed under the permitted normalized instruments. Lack of coherent-state coverage is a different conclusion.

For A1 there is a classical posterior state, not a decoded quantum joint state. For exact A2/A3, PSD branch closure follows from the imported instrument rule, while realized laws have the seed-grid error. Neither case derives the physical quantum structure from OI.

For QP node 10, the source reports XX=ZZ=1 and YY=0. Any PSD unit-trace state with the first two expectations is supported on the common +1 eigenspace, which is Φ+, and `YY=−(XX)(ZZ)` then forces YY=−1. This rules out a quantum completion of that table without assuming the other correlators. Positivity of finitely many Pauli probabilities is not the proof of a quantum state.

There is a useful stronger mathematical fact in the cited A868 draft, conditional on its zero completion: `W=(I+X⊗X+Z⊗Z)/4` gives product-effect values proportional to `1+a_x b_x+a_z b_z`, nonnegative for Bloch vectors of norm ≤1, yet W has an eigenvalue −1/4. This strengthens the distinction between matrix product-test positivity and PSD. It still supplies no physical availability of a full Bloch-effect menu, no general validity of other native preparations, and no continuation/coverage theorem. I read r4's “unrestricted product-test validity unassessed” as referring to that broader native operational obligation; the mathematical zero-completion fact need not be withdrawn.

MECH-2:642–650 reports P★'s valid record masses 5/8 and 3/8, with record-1 decoded Bloch vector `(1/3,−1/3,−1)`. Its squared norm is 11/9, so the decoded matrix is not PSD. This does not make the native record frequencies negative. The source's broader process claims remain [W]; my review does not independently certify that native construction by running it. A Y-sensitive comparison is required for the stated diagnostic, as MECH-2:690–694 and r4 explain.

For N5, I statically inspected both writer and reviewer scripts and their recorded outputs. The b=12 register is

`[[437/512,181/512],[181/512,599/4096]]`.

Its determinant is `(3496·599−1448²)/4096² = −325/2097152`, and its trace is 4095/4096. The b=12 choice lies inside the stated one-step window. This is a reachable exact-PSD failure for the specified round-to-nearest digitized rotation from the exact initial register. The unrounded Kraus product is PSD, while clipped/normalized Z-record probabilities are nonnegative. These facts support the distinctions at r4:543 and 609–612. They prove neither a nonvanishing asymptotic distance from the PSD cone nor a counterexample to a complete-law TV estimate.

The clipped/normalized finite-b bound remains open in Main:568, 578, 580, 598 and 602. The old per-parent estimate can fail because `s/Q` amplifies retained negative mass. A parent with that pathology has not thereby been proved reachable from the exact initial register in the counterexample used for the old ledger, and no recorded example cited here refutes the final law bound. The proposed stopping-time repair remains Motivated, with `Kη≤1/64` and an exact initial register, not an adopted theorem. D5 correctly reports Main's instrument-level proof status and separately records the off-main complex-constant qualification; this review does not settle that distinct #945 repair question.

### 7. Existing-round crosswalk and continuous-control claims

I read the relevant scope, access, decision-rule and limitation passages in the pinned preregistrations.

**Q-C2-1 r14c:** its question at 673–692 and decision rule at 879–936 make detector-off/on interference and the admitted-arm complementarity predicate primary. The shams have separate validation/attribution roles; they are not a replacement primary contrast. The `ATTR` field may report non-attribution when the kick-matched sham suppresses too. Its observer/validation split is explicit at 694–718; owner-typed B access at 1033–1075 and bounded C orbits at 1141–1184 do not grant arbitrary access to validation variables. R4's row 709 faithfully retains those limits.

**Q-C2-2 r14b:** the model at 264–349 has one read per run, 36 finite binary reads, a stated herald and conditional preparations. Its completions are separately supplied. R-S enlarges the charged configuration space and has a separate pre-F scope decision; see 601–622 and the scope text at 846–882. This is a prepare–measure fragment, not unrestricted longitudinal history access or an all-depth transformation theorem. R4:710 correctly requires a robust full-law margin, herald masses and an explicit varying-equivalence treatment before any scaling inference.

**MATH-CON-1:** the scope at 169–187 limits the stage to O-1, O-2 and O-3a–e. It explicitly excludes CT/O-8 and spectator-form O-9, and a successful stage supplies only the stated witness and finite-depth availability form. It establishes no general native dense control, adaptive error bound or OI sourcing of the polarized generators. R4:711 and 761–765 neither assume a result nor promote this stage to Level B.

The exact layer-flow/source theorems remain exact theorems with their stated hypotheses. Their uncountability/countability arguments concern exact availability at every time. They do not imply that an approximate target requires a continuum of primitive gate times. Conversely, words in a fixed finite permutation group give only finitely many terminal permutations; merely increasing word length cannot make them dense in an infinite target group. Fresh supply, retained records, changed carriers, or other access are extra resources to source and count. R4:627–649 makes both points correctly.

The reality condition is properly formulated as preservation of real states by preparations and branches. A complex Kraus representation alone does not show escape from that invariant. Finally, `obligations_independent` at `C5Discovery.lean:59–67` separates phase availability and layer-flow executability on Fin 2. It is not an independence theorem for H-Bell or for every notion of mixing. GR:250–260's complex drive carries phase under its specified control package. R4 does not infer that OI supplies it.

## Evidence actually inspected and verification limits

I read the full repository `AGENTS.md` (1368 lines). All scientific repository reads used the designated pin; no scientific program, probe, simulation, enumeration, Lean import, kernel build or workflow was executed. The work consisted of source reading, hand algebra, static textual searches and byte hashing. Working copies and this report were written only in a session temporary directory. There were no input, repository, ref, branch, GitHub or Page writes by this reviewer.

The material source inspection included:

- Main:482–520, 538–606 and 640; its exact/arithmetic/gluing/resource/status distinctions; GR:248–272; Substratum:123–133; the cited line-shift history at `7c6ceaaa` and `02009693`.
- `ImplementationLocality`, `AncillaClosure`, `ExecSource`, `SubstratumInterface`, `DiagonalTheory`, `ManuscriptAxioms`, `RouteB`, `SubstratumInterfaceAudit`, `LiftAudit`, `C5Discovery`, `PolarizationClosure`, `StructuralClosure`, `LevelOneSeam`, `CoherentContinuumSource`, `Equivalence`, `GeneralCarrier` and `RankGapTheory`: the definitions, statements and relevant proof bodies identified above. This is inspection of the existing formal proof source, not a fresh kernel check.
- MECH-2 standing and nodes 2, 3, 6 and 7; the R1/AP1 source and its state-representation example at 872–878; QP's U′ definition and node-10 correlators. I independently checked the matrix consequences, not the native process by execution.
- All four writer scripts named in r4 §12 and their complete recorded `.out` files. I also read the four `rv_*` recorded outputs, the finite-b reviewer script, and relevant definitions/logic in the other reviewer scripts. The [RV] files corroborate; they were not treated as a substitute for proof or for this review.
- Pinned `opglue_probes.py`, including exact core/multi-Kraus/single-dynamics logic, the numerical nature of checks 8–9, and the distinction between checks 14–16 and a general fixed-b theorem. Other Main probe claims retain their manuscript evidence status; I did not replay the Main suite.
- #1216's central question/Levels and the five #945 comments, especially the actual assessment and final-check records; the original `6d494e30` epsilon proof review and `neg_parent4.py`, read statically.
- The scope/access/decision/limitation sections of Q-C2-1 r14c, Q-C2-2 r14b and the MATH-CON-1 control plane, not every implementation/CI appendix of those long preregistrations.
- The relevant summaries and joint-test/bridge passages of the A868, A1059 and BRIDGE handoff drafts. Their broader claims and any SHM premises are not independently certified here; r4 labels these sources [D] or [W] and does not use their asserted acceptance as scientific evidence.
- For the imported dimension result, the qubit classical-dimension separation and finite coordinated-resource statement in Heinosaari–Kerppo–Leppäjärvi–Plávala, [arXiv:2308.07727v4](https://arxiv.org/html/2308.07727v4), including its rank argument and Theorem 6. The import supports exact fixed-carrier obstruction, not an arbitrary-resource approximate no-go. I also checked the bibliographic/ontic-model terminology against Harrigan–Spekkens, [arXiv:0706.2661](https://arxiv.org/html/0706.2661), §II. R4's “ρ-ontic” qualification accurately describes the supplied register more precisely than an unrestricted identification of its mixed states with ψ.

The eight r4 §12 script/output digests were independently checked against bytes fetched at the immutable handoff pin:

| Artifact under `handoff-20261109/1216-approx/` | SHA-256 |
| --- | --- |
| `probes/approx_generic_checks.py` | `12aac10f6e8f8d6a7bfb7603b35aac8253132534e353791508c3cda443f172c0` |
| `probes/approx_generic_checks.out` | `4337d4afc70c4fdd22deafda2eefeaa926abe044f3b7993ad47b37e9d2865c35` |
| `probes/r2_frames.py` | `aa02e479a0d93ba7ccb6ccb5f9a40c7b0e2065e5f3d7c30d3bdbb2d78010548a` |
| `probes/r2_frames.out` | `a116e91999a566f9d409f857325be4e1d94a47c24da62f7ec6eb73e491be0209` |
| `probes/r2_routeC.py` | `b71749e47f742338d6373aaccae08bdaa96c985c29172b36ba1267e60ac72f97` |
| `probes/r2_routeC.out` | `5626b5a8db40d7ade57542ea297c1c6afb2da32bcd5838ed013d9b02d2e538ec` |
| `probes/r2_finiteb.py` | `383c21567671c73e9565b65c8846dfdc4ab385bf285321cd22b83b72c9b6e07c` |
| `probes/r2_finiteb.out` | `6350b5c11822166bff80b9eacde330a14513390cbda0dc117cc45f26ed4df7b1` |

Matching a digest establishes artifact identity, not correctness or replay. The recorded checks' results remain inherited evidence unless independently supported by the hand arguments in this report. I did not certify uninspected external literature, unavailable r3 bytes, native scientific execution, or pending-round outcomes.

Off-main support is not required to be merged merely to obtain this non-landing WIP review. Its actual support and verification limits have been identified. Nothing in this verdict closes the sourcing, correspondence, accessible-history or resource-uniform error obligations that r4 leaves open.

**Final disposition: ACCEPT WITH NITS.** R1–R6's scientific repairs hold on the stated scope; apply N1–N3 as local prose/evidence corrections. No additional computation or new physical premise is needed for those corrections.
