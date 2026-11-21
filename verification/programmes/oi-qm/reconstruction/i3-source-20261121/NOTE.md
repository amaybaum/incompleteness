# I3-SOURCE: what counts as a genuine physical source (research note)

**WIP / UNVERIFIED. Paper research only; not reviewed.** This note walks the nodes fixed in
`PLAN.md` (committed first, at `182eeb21`). It adopts no criterion, premise or extension E,
edits no manuscript or reviewed record, runs no computation and changes no status. Physical source
remains NOT PASSED. D5 stays open (#1169 c.7065620072).

Tracking: Issue #1507; draft PR #1508. Background: GATE-A r5.6 (#1503 at `fd3cb064`, cited `GA §`).
Base: `main` at `df6da1c6`. `Sub:n`, `Main:n`, `Meth:n` are lines of `papers/Substratum.md`,
`papers/Main.md`, `papers/Methodology.md` there. Layers: X exact algebra on paper; P paper
argument; K kernel theorem on `main`, cited and not duplicated.

## 0. Summary and the three questions

**Main findings.**

1. **Lemma S1 (N, X).** Under the single-time interface of `Sub:249`, a permutation dilation with
   **any** hidden state realizes a unitary channel Ad_W only if W is monomial. With `Main:328`
   (diagonal hidden priors, finite or measurable carriers), it follows that **no model whose
   dynamics is a bijection of configurations meets I★_st-coh**. The Hadamard target
   Λ_t = Ad_{H^t} already fails. This covers every D-W variant and every native permutation model.
   At Stage 1-coh, no sourcing criterion is needed to exclude D-W, and no criterion can admit a
   native model of the stated kind. The decisive line is permutation versus non-monomial dynamics,
   that is, FLOW (#1501).
2. **Staging correction (P).** GA §2.4 states that both I★_st variants are "strictly weaker than
   I★". If D-W meets I★, as GA §2.2's sketch holds, then I★ does **not** imply I★_st-coh, since
   D-W fails I★_st-coh by S1. I★_st-coh compares Born-form channels. I★ compares record laws.
3. **R-EX (I: KIN), a criterion that passes the PLAN decision rule.** R-EX is
   *representational exactness*: the model's instruments, written in the Born form of its own
   configuration space and with its hidden state traced out, equal the target's instruments. It
   is the corpus's own `∼` (`Sub:249`, text since `e7ed439d`, 2026-11-11, before D-W), extended to
   instruments. It excludes every C1 variant (S1 and the kernel monomial no-gos), admits the C2
   models that have a configuration basis, and names no OI-specific property. Every **known** C3
   model fails it for a separate reason, its monomial dynamics. A native model passes R-EX iff it
   supplies a non-monomial coherent operation. **D5 under R-EX therefore reduces to O1 (FLOW).**
4. **T-SUB′ clause (iv) fails the acceptance standard in every reading (P).**
   - Read literally, *(iv)-recoverable* applied to instrument labels excludes **every** EP-schema
     model with program-dependent instruments, by EP:79 alone, without PBR (Lemma R2).
   - Repaired to the system's own ontic state, it is ψ-ontology. It then excludes ψ-ontic genuine
     quantum models (de Broglie–Bohm, Everett, GRW) directly, against the owner's requirement.
     With PIP (PBR) or with free choice, i.e. (xiv) beyond its Bell scope (Colbeck–Renner), it
     also excludes every exact model that meets those premises.
   - *(iv)-explicit* is evaded by redescription (Lemma I).
   - At Stage 1-pop the dilemma recurs without PBR (Lemma R1).
5. **N2 survey (P).** Complexity (C-CX), counterfactual linearity (C-LIN), locality (C-LOC),
   thermodynamics (C-TH) and symmetric hard-to-vary (T-HTV′) were each tested on the three
   classes. None passes the decision rule as an independent criterion.
   - Every one that separates C1 from C2 also excludes the known C3 class.
   - C-LIN is decisive only under a counterfactual-law reading, where it coincides with R-EX.
   - T-HTV′ applied symmetrically ranks D-W with axiomatic QM. Its residual content is the
     derivation of complex kinematics (KIN), not the source of operations.
6. **N3 (P).** The distinction is ill-posed **operationally**. For observers inside a D-W-tot,
   no function of their operational data separates it from a genuine quantum model (Lemma O). It
   is well-posed **structurally** (R-EX). The structural pattern found is AW-I3-1: every decisive
   line separating C1 from C2 that was found is one the known C3 class shares with C1, unless FLOW
   holds.

**Established.**
- Lemma S1 and Corollary S1′, (N), layer X.
- Lemmas R1, R2, I and O, and Lemma L1 for injective encodings, layer P.
- The three-class table (§5).
- The staging correction (P), conditional on GA's D-W sketch.

**Assumed.**
- S1: none beyond the `Sub:249` interface. The target I★_st-coh is a D6 proposal, the object
  tested, not an import.
- R-EX as a criterion: KIN (complex Born-form kinematics, decision 4).
- C-CX: H1–H5 (#1498) and BQP ⊄ BPP.
- ψ-ontology horns: the ontological-models framework, plus PIP [PBR] or free choice [CR].
- C-LIN: the counterfactual-intervention reading CI-3 (§4.2).

**Missing.**
- The earliest unsupported step is a **physical mechanism**: an executable non-monomial coherent
  operation on the configuration Born form (FLOW). No criterion found makes a native model pass
  without it.
- One **decision**: whether to adopt R-EX at Stage 2 (owner, D5/D6).
- Open **mathematics**:
  - the characterization of the non-unitary single-time channels reachable by permutations with
    a coherent hidden state;
  - C-LIN for ontological (distribution-level) native models;
  - shielding of registers in universal reversible substrata (CI-2).

## 1. Literature (audit Step 4)

| Topic | Source | Use here |
|---|---|---|
| Ontological models; ψ-complete / ψ-supplemented / ψ-epistemic | N. Harrigan, R. W. Spekkens, Found. Phys. 40, 125 (2010); E. Beltrametti, S. Bugajski, J. Phys. A 28, 3329 (1995) | D-W is the ψ-complete model (#1506 §4.3) |
| PBR | M. F. Pusey, J. Barrett, T. Rudolph, Nat. Phys. 8, 475 (2012) | ψ-ontic under PIP; PIP named as import (§4.5) |
| PIP is load-bearing | P. G. Lewis, D. Jennings, J. Barrett, T. Rudolph, PRL 109, 150404 (2012) (ψ-epistemic models for projective measurements in every finite dimension; extra assumptions are always necessary); M. Schlosshauer, A. Fine, PRL 108, 260404 (2012); J. Emerson et al., arXiv:1312.1345 | without PIP, ψ-epistemic models exist at prepare-and-measure scope |
| Free choice ⇒ ψ-ontic | R. Colbeck, R. Renner, PRL 108, 150402 (2012), arXiv:1111.6597; comment: G. C. Ghirardi, R. Romano, arXiv:1302.1635 | the free-choice premise is (xiv) beyond its Bell scope (AW-I3-3) |
| Other ψ-ontology routes | L. Hardy, Int. J. Mod. Phys. B 27, 1345012 (2013); M. K. Patra, S. Pironio, S. Massar, PRL 111, 090402 (2013); J. Barrett, E. G. Cavalcanti, R. Lal, O. J. E. Maroney, PRL 112, 250403 (2014); M. S. Leifer, PRL 112, 160404 (2014); review: M. S. Leifer, Quanta 3, 67 (2014) | ψ-epistemic overlap bounds without PIP |
| Excess baggage; classical dimension | L. Hardy, Stud. Hist. Philos. Mod. Phys. 35, 267 (2004); E. F. Galvão, L. Hardy, PRL 90, 087902 (2003); A. Montina, PRA 77, 022104 (2008) (Markovian ontological theories need exponentially many variables) | C-LOC, C-CX; L-H, L-H′ (GA §4) |
| Contextuality | R. W. Spekkens, PRA 71, 052108 (2005); M. S. Leifer, O. J. E. Maroney, PRL 110, 120401 (2013) | C-LIN, ontological reading (§4.2) |
| Universal quantum computer; resources | D. Deutsch, Proc. R. Soc. Lond. A 400, 97 (1985); D. Deutsch, *The Fabric of Reality* (1997), ch. 9; R. P. Feynman, Int. J. Theor. Phys. 21, 467 (1982); critics: A. M. Steane, Stud. Hist. Philos. Mod. Phys. 34, 469 (2003); C. Hewitt-Horsman, Found. Phys. 39, 869 (2009); M. E. Cuffaro, Br. J. Philos. Sci. 68, 91 (2017) (Gottesman–Knill); S. Aaronson, arXiv:1108.1791 (2011) | C-CX (§4.1) |
| Constructor theory | D. Deutsch, Synthese 190, 4331 (2013); D. Deutsch, C. Marletto, Proc. R. Soc. A 471, 20140540 (2015) | counterfactual (possible/impossible task) formulation, §4.2 |
| Implementation and triviality | H. Putnam, *Representation and Reality* (MIT, 1988), appendix; D. J. Chalmers, Synthese 108, 309 (1996) | counterfactual conditions on implementation, §4.2 |
| Nonlinearity and signalling | N. Gisin, Phys. Lett. A 143, 1 (1990); J. Polchinski, PRL 66, 397 (1991); S. Weinberg, Ann. Phys. 194, 336 (1989) | justification attempt for C-LIN, §4.2 |
| Quantum non-equilibrium | A. Valentini, Phys. Lett. A 156, 5 (1991) | a falsifiable signature shared by every hidden-prior model, §4.4 |
| Deterministic CA reading | G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*, Fundam. Theor. Phys. 185 (Springer, 2016) | the template (non-ontic basis) loophole to S1, §2.1 |
| Born rule forced by kinematics | A. M. Gleason, J. Math. Mech. 6, 885 (1957); P. Busch, PRL 91, 120403 (2003) | T-HTV′ symmetric, §4.6 |
| Reconstructions, GPTs | L. Hardy, arXiv:quant-ph/0101012 (2001); L. Masanes, M. P. Müller, NJP 13, 063001 (2011); G. Chiribella, G. M. D'Ariano, P. Perinotti, PRA 84, 012311 (2011); J. Barrett, PRA 75, 032304 (2007) | KIN derivation as the residual content of T-HTV′ |
| Reversible computation, Landauer | R. Landauer, IBM J. Res. Dev. 5, 183 (1961); C. H. Bennett, IBM J. Res. Dev. 17, 525 (1973); C. H. Bennett, Int. J. Theor. Phys. 21, 905 (1982) | C-TH, §4.4 |
| Isomorphism invariants | D. Ornstein, Adv. Math. 4, 337 (1970) | Lemma I |
| Extremality of unitary channels | M.-D. Choi, Linear Algebra Appl. 10, 285 (1975), Thm 5 | S1 proof |
| ψ-ontic genuine models | D. Bohm, Phys. Rev. 85, 166 (1952); H. Everett, Rev. Mod. Phys. 29, 454 (1957); G. C. Ghirardi, A. Rimini, T. Weber, Phys. Rev. D 34, 470 (1986) | C2 test class |

Corpus: `Meth:403–405` already records that PBR "cannot simply be imported as a theorem about bare
OI without first establishing its preparation-independence premise". It is followed here.

## 2. N1: Stage 1 (I★_st over the existing single-time interface)

**Reading R-ST (stated, not chosen here).** As in GA §2.4, the single-time family of a model is
computed by the rule of `Sub:249` and `familyAt` (`OIBridge/SemigroupTransfer.lean`:93):
Φ_t(ρ_V) = Tr_H[φ̂^t (ρ_V ⊗ ω_H) φ̂^{−t}], with φ̂ the permutation unitary of the model's bijection
on configurations. The visible alternatives are |A| configurations (enc_A).

### 2.1 N1.1, the coherent variant

**Lemma S1 (N; layer X).** Let C_V be finite and H countable. Let φ be a bijection of C_V × H with
permutation unitary φ̂ on ℓ²(C_V × H), and let ω be any density operator on ℓ²(H), diagonal or not.
If Φ_t = Ad_W for some t ≥ 1 and some unitary W on ℂ^{C_V}, then W is monomial.

*Proof.*
1. Put P = φ̂^t, the permutation unitary of the bijection ψ = φ^t, and write ω = Σ_k q_k |χ_k⟩⟨χ_k|
   with q_k > 0.
2. Then Φ_t = Σ_k q_k Φ^{(k)}, where Φ^{(k)}(ρ) = Tr_H[P(ρ ⊗ |χ_k⟩⟨χ_k|)P†] is a channel.
3. A unitary channel is an extreme point of the channels on a finite-dimensional space [Choi,
   Thm 5]. Splitting off one term at a time gives Φ^{(k)} = Ad_W for every k.
4. Fix χ = χ_k. The map |v⟩ ↦ P(|v⟩ ⊗ |χ⟩) is a Stinespring isometry of Ad_W. Its Kraus
   operators lie in the span of the minimal Kraus set {W}, so P(|v⟩ ⊗ |χ⟩) = W|v⟩ ⊗ |e⟩ for one
   unit vector e and every v.
5. The left side is supported on ψ({v} × supp χ). These sets are pairwise disjoint over v, because
   ψ is injective. The right side is supported on supp(W|v⟩) × supp e, with supp e ≠ ∅.
6. Hence the sets supp(W|v⟩) are pairwise disjoint nonempty subsets of C_V, |C_V| of them. Each
   is therefore a singleton. ∎

**Corollary S1′ (N; layer X, with `Main:328` at layer P).** Take A = Fin 2, trivial K and
Λ_t = Ad_{H^t}, with H the Hadamard matrix (non-monomial: `hadamard_not_monomial`,
`OIBridge/C5Discovery.lean`:162, K). Then I★_st-coh fails for:
- (a) every model (C_V × H, φ, ω) with H countable and ω any density operator (S1 at t = 1);
- (b) every model with a classical hidden prior on a measurable hidden carrier, under the
  conditions of `Main:328`'s corollary. Its channels are diagonal-preserving, while
  Ad_H(|0⟩⟨0|) = |+⟩⟨+| is not diagonal.

Case (b) covers D-W, whose seed tape is uncountable with a product Lebesgue law. Cases (a) and (b)
together cover every C1 variant listed in PLAN §3, since each is a bijection (Bennett-reversible),
and every C3 model of `Sub:249` form.

**What meets I★_st-coh.** The target's own dilation (A ⊗ K, W, σ_K) does, by definition; it is
not a bijection model. So the coherent variant separates by **dynamics type**: permutation, with
any hidden state, versus non-monomial unitary. Within OI this is FLOW (#1501 §0.3). The stated
dynamics provably does not supply it (`substratumTheory_not_layerFlowExecutable`,
`OIBridge/LiftAudit.lean`:200; `substratumGen_not_control`, `OIBridge/StructuralClosure.lean`:330,
both K).

**Answer to N1 (coherent).**
- A T-SUB′-type criterion is moot here. Clauses (i)–(iii) restrict Φ to the substratum update, a
  bijection, so by S1′ no T-SUB′-admissible model meets I★_st-coh for Ad_H, under any reading of
  (iv).
- The legitimate non-native exact model, the target's dilation, fails T-SUB′(ii), and (iv) is
  undefined for it.
- The (iv) dilemma is not reached at Stage 1-coh. The interface alone is decisive.

**Skepticism (favourable branch: "the interface excludes D-W").**
- *Redescription.* A measurable isomorphism maps points to points, so the Born form of a bijection
  stays a permutation. S1's verdict is isomorphism-invariant. The one escape is to declare the
  visible alternatives to be a non-configuration basis ('t Hooft's templates). That violates enc_A
  and the fixed interface of `Sub:249`.
- *Operational force.* Coherences of ρ_V are not preparable or readable through the fixed-basis
  single-time readout. The exclusion is therefore **mathematical, not operational**: D-W meets
  I★_st-pop (GA §2.4).
- *Shaped by D-W?* No. `Sub:249` and `Main:328` are present from `e7ed439d` (2026-11-11). D-W
  enters at #1503 and #1506 (2026-11-21).
- *Cost.* The same interface excludes every native model of the stated kind. The branch is
  favourable to "D-W excluded" and unfavourable to native OI.

**Verdict N1.1: NEW.** GA §2.4 left satisfiability "not examined"; S1′ settles it negatively for
every bijective model with unitary non-monomial targets.

**Staging correction (P, conditional on GA §2.2's D-W sketch).** D-W meets I★ (sketch) and fails
I★_st-coh (S1′). So I★ ⇏ I★_st-coh, against GA §2.4's "Both variants are strictly weaker than
I★". The c.7064942473 sentence GA cites concerns *observational* equivalence. That matches
I★_st-pop, which compares populations, not I★_st-coh, which compares Born-form channels.
- Even for pop, I★ fixes protocol laws, and I★_st-pop fixes the model's autonomous family. An
  implication needs an identification of free evolution with a protocol.
- GA is reviewed and is not edited here. The finding is reported for its reviewer and the owner
  (D6).

### 2.2 N1.2, the population variant

I★_st-pop compares classical stochastic families T(t). D-W meets it, and so do response-table
models (sketch). Response-table models compute their prior from T, so they are comparator-fitted
(I-2★, EP:102).

**Lemma R1 (N; layer P; counting).** Fix one model M* with **one** hidden prior and countably many
encodings, for example finite regions of a countable site set with a finite alphabet. Then M*
realizes at most countably many distinct population families. Hosting the continuum
W_θ = rot(θ), θ ∈ (0, π/2), with distinct T_θ(1), therefore requires one of two things:
- (a) the prior depends on θ, so the label rides in the law. That is the Stage-1 form of GA §2.2's
  "μ_p may depend on p", and a fixed posit-(iv) prior does not allow it; or
- (b) the encoding carries an infinite configuration datum. Then θ is a measurable function of a
  configuration, the setting.

**Consequence for (iv) at Stage 1-pop.**
- The system's preparations are basis states i ∈ A and carry no numeric entries, so (iv) read on
  the system is vacuous.
- Read on every region used, (iv)-recoverable excludes every fixed-prior model in case (b). That
  includes genuine laboratory QM, whose rotation angle is written in its apparatus.
- With unrestricted decoders, a further horn appears. In a translation-invariant ergodic model with
  infinitely many copies of the sector, a decoder that applies the fixed Φ to translates and takes
  limit frequencies recovers T almost surely. So recoverability holds for such models as well.
- Restricting decoders to finite regions or bounded complexity turns (iv) into a resource
  criterion. D-W evades it by degrading its encoding, for example to a statistical one.

**Verdict N1.2: NEW.** The (iv) dilemma persists at Stage 1-pop without PBR. Its horns there are
the counting Lemma R1 and ergodic decoding.

## 3. Lemma R2: clause (iv) on instrument labels (P)

**Lemma R2 (N relative to the EP schema).** Under EP:79, a change of future program loads only
controller fields. If two programs select instruments with different numeric entries and give
different laws, the controller configuration determines the instrument, so the entries are a
function of that configuration. GA §2.2's (iv) forbids "a configuration that encodes the numeric
entries of a state or instrument label" in any region used by the procedure, with setting and
program fields included by (i). Read as recoverability, (iv) is therefore violated by **every**
EP-schema model with two or more program-selected instruments.
- Read as explicit numerals, it is violated by any model whose controller holds the label as a
  numeral. Holding it in any other fixed physical form is recoverable again.

**Repair.** (iv) must exempt controller and setting fields and apply to the system's post-preparation
ontic state only. That is ψ-ontology (§4.5).

**Verdict: NEW.** This is a hidden assumption in GA §2.2's definition, independent of PBR.

## 4. N2: candidate criteria, each with justification and the three-class test

### 4.1 C-CX, resource or complexity separation

- *Justification.* Deutsch 1985 and *Fabric of Reality* ch. 9: physical resources must be
  accounted for. Montina 2008. BQ1 (#1498).
- *C1.* D-W's register has 4ⁿ entries for n qubits. It is excluded only asymptotically, and only
  if BQP ⊄ BPP (imported conjecture). Gottesman–Knill (Cuffaro 2017) shows that resource arguments
  depend on the circuit family.
- *C2.* Admitted: genuine QM hosts BQP polynomially.
- *C3.* Excluded under H1–H5 (BQ1-D, (I)).
- *Scope.* I★ demands exactness at each finite carrier, not efficiency. C-CX addresses a different
  target.
- **Verdict: conditional (I: BQP ⊄ BPP, H1–H5); fails the C3 cell.**

### 4.2 C-LIN, counterfactual or interventional linearity

*Statement.* For every native transformation g of the degrees of freedom that bear the model's
quantum state, there is a CPTP map Γ_g with r(g_*μ) = Γ_g(r(μ)) for every preparable ontic law μ.
Here r maps ontic laws to represented states.

**Lemma L1 (P).** Suppose a model stores an injective encoding of its state (stepwise, enc and tot
variants) or of its preparation parameters and history (lazy variant) in a region R of a
finite-alphabet site set. Suppose the finite-region bijections of R are native transformations.
Then some g has no Γ_g.

*Sketch.* D-W realizes ρ̄ = ½ρ₁ + ½ρ₂ both as δ_{enc ρ̄} and as ½δ_{enc ρ₁} + ½δ_{enc ρ₂}. A Γ_g
would make ρ ↦ dec(g · enc ρ) affine. Two cases follow:
- If g leaves the image of enc, the predictions match no quantum state. Example: a digit flip
  gives ρ′ = (1+ε)|e₁⟩⟨e₁| − ε|e₂⟩⟨e₂|. D-W's cumulative rule gives the law (1, 0) in the e-basis,
  which forces e₁. In the basis cos α e₁ + sin α e₂ it gives cos²α + ε cos 2α ≠ cos²α.
- Otherwise, take patterns a, b on a finite F ⊆ R. With at least three nonempty fibres, some
  transposition of a and b fixes a set that is not contained in a hyperplane (union-of-three-
  hyperplanes argument), and moves a nonempty fibre. That map is not affine.

*Not covered:* a "positive-parametrization" D-W in which every configuration decodes to a valid
state and r is not injective.

**The counterfactual quantifier is the load-bearing premise.**
- **CI-1, loadings of the designated controller.** D-W passes, if it validates instructions and
  ignores invalid ones.
- **CI-2, arbitrary counterfactual configurations around R under the fixed rule.** Whether D-W can
  shield its register in a universal reversible substratum is open.
- **CI-3, counterfactual laws: arbitrary finite-region bijections.** D-W fails (L1).
  - CI-3 does not follow from OI's ontology: one fixed φ, with interventions as loadings
    (EP:75–79).
  - Its justification needs one of three routes: soundness on the carrier (S⇒, left open by
    c.6891338304); constructor-theoretic possible tasks (Deutsch–Marletto); or the
    superposition principle for configurations.
  - Gisin and Polchinski justify linearity through signalling only when g is local to one wing.
    D-W's register is global in the simulated geometry, so the argument does not transfer.
  - Chalmers's counterfactual conditions concern the implemented automaton's own transitions, not
    arbitrary perturbations of the implementer.
- *C2.* Admitted, with each theory's own transformation set.
- *C3, Born-form reading.* Admitted: permutations act by conjugation, which is linear. The model
  then fails exactness (S1, kernel no-gos).
- *C3, ontological reading.* Native models as distributions over configurations, with every
  finite-region bijection available. Whether preparation contextuality [Spekkens 2005] then forces
  a failure is **not settled here**.
- Under CI-3 with the Born-form reading, C-LIN **coincides with R-EX's representation**.
- **Verdict: conditional (CI-3); ELABORATING; its decisive content is R-EX (§5).**

### 4.3 C-LOC, locality and causal structure

- *Criterion.* An exact qubit in a finite region of a finite-alphabet site structure.
- *Ontological reading.*
  - C1 excluded: exact reals need infinitely many sites.
  - C3 excluded: Proposition U (#1504, (I) via (xiv)).
  - C2's ontological models are also excluded (Hardy 2004; Galvão–Hardy; Montina 2008).
  - **Fails the C2 cell.**
- *Born-form reading.* A qubit is two configurations with coherent span, so C1, C2 and C3 all
  pass locality, and exactness again separates (R-EX).
- **Verdict: fails as an independent criterion.**

### 4.4 C-TH, thermodynamic cost

**Lemma E (I: exact comparator law; EP:97).**
- In the EP schema the outcome is a function of (u, p, π). So H(outcomes) ≤ H(ν_p) on the
  variables used, for **every** model: D-W and native alike.
- Records and Bennett history must be retained or uncomputed. QOPS P5 and RES (#1501 §2) bind both.
- Everett consumes no stored randomness. GRW consumes stochastic noise.

**Cells.**
- "No consumed randomness" excludes C1, C3 and GRW, so it **fails the C2 cell**.
- Quantities invariant under measure-theoretic isomorphism (Kolmogorov–Sinai entropy; Ornstein)
  cannot separate D-W from its encrypted copies (Lemma I).
- Valentini non-equilibrium is falsifiable, but it applies to every hidden-prior model, C1 and C3
  alike.

**Verdict: fails.**

### 4.5 ψ-ontology (PBR with PIP named; Hardy; Colbeck–Renner; Leifer)

*(iv)-recoverable, repaired to the system (§3), is ψ-ontology.*
- *C1.* Excluded: D-W is ψ-complete.
- *C2.* **Excluded directly**: Bohm, Everett and GRW are ψ-ontic. The owner's requirement is
  violated even before any theorem is used.
  - With **PIP** [PBR], every exact `J_exact` model whose independently prepared systems satisfy
    PIP is ψ-ontic. `J_exact` contains the two-copy entangled measurements (GA §2.2). (I): PIP and
    the ontological-models framework.
  - With **free choice** [Colbeck–Renner], which is (xiv) applied beyond its Bell scope (`Main:736`),
    the same conclusion follows without PIP. (I): (xiv) beyond scope, plus the premises of their
    framework (Ghirardi–Romano dispute the identification).
  - Without such premises, ψ-epistemic models exist at prepare-and-measure scope [Lewis et al.
    2012]. Overlap bounds hold even then [Barrett et al. 2014; Leifer 2014].
  - At Stage 1 there are no entangled measurements (GA D6), so the PBR horn does not arise there.
    R1 replaces it.
- *C3.* Unknown. No exact native model is known.

**Verdict: fails the C2 cell in every reading. NEW relative to GA §2.2**, which assessed the PBR
horn only.

### 4.6 T-HTV′ applied symmetrically

- D-W's class is easy to vary: swap the register type for a GPT state (Barrett 2007).
- The standard axiomatic presentation of QM is varied in the same way: real or quaternionic
  kinematics, or GPTs.
- Given its Hilbert-space register, D-W's branch rule is forced (Gleason; Busch), exactly as for QM.
- So, applied symmetrically, the criterion ranks D-W with axiomatic QM. What it penalizes is
  **imported kinematics** (KIN) and comparator copying (EP:102), not the source of operations.
- **Verdict: survives only as a judgment on KIN derivation** (reconstructions: Hardy 2001;
  Masanes–Müller; Chiribella–D'Ariano–Perinotti). **ELABORATING.**

## 5. R-EX, the representational form, and the three-class table

**R-EX (proposal; (I): KIN).** For every instrument of the target interface, the model realizes an
apparatus procedure whose Born-form instrument on the carrier's configuration span, with its
apparatus and hidden state traced out, equals the target instrument.
- At Stage 1, R-EX is I★_st-coh.
- At Stage 2, it adds a coherent-lift exactness clause to I★. This changes the target and is an
  owner decision. The comparator's instruments are J-coh-level objects, so Stage-2 results stay
  (I).

**Decisive test.**
- One-outcome unitary instruments: S1.
- Classical hidden priors: the channel is a sum of conjugations by monomial Kraus operators,
  hence diagonal-preserving (`Main:328`, P; `preservesDiag_conj_of_monomial`,
  `OIBridge/SubstratumInterface.lean`:101, and `preservesDiag_sum`,
  `OIBridge/DiagonalTheory.lean`:84, K). At the generated-theory level on Fin 2,
  `substratumGen_not_control` (K) excludes composite unitary control for the monomial class.
  Instruments with several outcomes and classical priors are covered on paper by the same
  diagonal-preservation argument applied branch by branch (P, not kernel-checked).

| Criterion | Independent of D-W | C1 excluded (all variants) | C2 admitted | C3 by its own terms | Verdict |
|---|---|---|---|---|---|
| R-EX | yes (`Sub:249`, 2026-11-11; decision 4) | yes (S1′; K no-gos for classical priors) | yes, with a configuration basis | not excluded; known C3 fails exactness without FLOW | **passes the decision rule; (I): KIN** |
| C-CX | yes (Deutsch, Montina) | asymptotically, if BQP ⊄ BPP | yes | excluded under H1–H5 | conditional; fails C3 cell |
| C-LIN | only under CI-3 | CI-3 yes (L1, injective encodings); CI-1 no; CI-2 open | yes | Born-form yes; ontological open | conditional; content = R-EX |
| C-LOC (ontological) | yes | yes | **no** | excluded (Prop. U, (I)) | fails |
| C-TH | yes | no separation from C3 | GRW excluded | no separation | fails |
| (iv)-recoverable (system) | yes (ψ-ontology) | yes | **no** (Bohm, Everett, GRW) | unknown | fails |
| (iv)-recoverable (literal) | — | yes | no | **every** EP model excluded (R2) | fails |
| (iv)-explicit | — | **no** (Lemma I) | yes | — | fails |
| T-HTV′ symmetric | yes (§A.29) | only through KIN/EP:102 | judgment | judgment | judgment on KIN |

**Skepticism on R-EX (favourable cell).**
- It was not shaped by D-W (vintage above).
- It is redescription-proof (Lemma I, points to points).
- It does not exclude C2 because of what their states encode.
- It is a mathematical criterion, not falsifiable by embedded observers' data at the single-time
  interface. It demands that the quantum dynamics be the linear structure of the actual
  configuration dynamics: a realist reading the corpus already uses for `∼`.
- Its cost is that, for OI's stated ontology of one fixed bijection, R-EX is **unattainable
  without FLOW**. The criterion converts D5 into O1. It does not certify any native model.

## 6. N3: is the distinction ill-posed?

**Lemma O (P; class: criteria that are functions of embedded observers' operational data).**
Consider D-W-tot, which simulates system, apparatus and observers in one register with one fixed
global step. Its observers' operational data equal those of the genuine quantum model it
simulates, by I-4 on `J_exact`. No criterion in this class separates them.
**CONFIRMING**: it restates D-W's existence, as the precise form of "undecidable".

**Lemma I (P; class: criteria invariant under measurable isomorphism of (Ω, Φ, μ, ι, R)).** Such a
criterion gives the same verdict on D-W and on every encrypted, compressed or spread copy of it.
- (iv)-explicit is not invariant, which is why redescription evades it.
- Recoverability and the Born-form permutation property are invariant.
- Locality-based criteria are invariant only under local isomorphisms.

**Answer.**
- The distinction is ill-posed operationally (Lemma O) and well-posed structurally (R-EX).
- Among structural criteria, the decisive ones (R-EX; C-LIN under CI-3) place the known native
  class on D-W's side of the line, because native dynamics is a permutation.
- That is a result about the current construction, stated for its class (permutation dynamics with
  any hidden state). It is not a no-go for observer-level extensions that supply FLOW.

## 7. Assumption-watch markers

- **AW-I3-1.** Every decisive line found that separates C1 from C2 (R-EX, C-LIN/CI-3, C-CX) is one
  the known C3 class shares with C1, unless FLOW holds. A future sourcing claim must say which
  line it crosses and how.
- **AW-I3-2.** Any (iv)-type clause must name its region: system, setting or controller. Otherwise
  it excludes every EP model (R2) or every laboratory with a continuous dial (R1).
- **AW-I3-3.** Colbeck–Renner's free choice is (xiv) beyond its Bell scope. It joins BQ1's H3
  (#1498) and Proposition U (#1504) as the third use of (xiv) outside `Main:736`'s scope.

## 8. Classification (§A.31) and productivity

| Item | Class |
|---|---|
| S1, S1′ | NEW |
| Staging correction (I★ ⇏ I★_st-coh) | NEW (conditional on GA's D-W sketch) |
| R1 | NEW |
| R2 | NEW (hidden assumption in GA §2.2) |
| ψ-ontology C2 failure of (iv) | NEW |
| R-EX | NEW (a criterion passing the decision rule, with its cost) |
| L1, C-LIN | ELABORATING |
| C-CX | CONFIRMING (BQ1) |
| C-LOC, C-TH, T-HTV′ symmetric | ELABORATING |
| Lemma O | CONFIRMING |
| Lemma I | ELABORATING (formalizes GA §2.2's redescription pattern) |

Productivity test (PLAN §4): met through (a) R-EX, (b) for the class of permutation dynamics with
any hidden state, and (c) R2 and the staging correction. The fixed point is not reached. One pass
of a reviewer is needed before further nodes.

## 9. For owner decision (nothing adopted)

- **D5.** Whether to adopt R-EX at Stage 2. If adopted, D-W is excluded by exactness itself and I-3
  needs no further test against C1; D5 then reduces to O1 (FLOW). If not adopted, no criterion
  found here excludes D-W at Stage 2 without failing a C2 or C3 cell.
- **D6.** Note the staging correction: I★_st-coh is not a weakening of I★ as I★ stands. It is a
  representational target. I★_st-pop is the observational one.
- **GA §2.2 (iv).** R2 and §4.5 apply to its reviewer; GA is not edited here.

## 10. What this note does not do

It edits no manuscript, no reviewed record and no Issue body. It runs no computation and
dispatches no workflow. It proposes no E, adopts no criterion and posts nothing on #1169.
