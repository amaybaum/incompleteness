# I3-SOURCE: what counts as a genuine physical source (research note)

**WIP / UNVERIFIED. Paper research only.** Revision r2 answers the independent review of
`78209347` (#1508 c.7065934065 and addendum c.7065957850; verdict REVISE) and the owner's
assessment #1169 c.7065925731; r2 is not yet re-reviewed. This note walks the nodes fixed in
`PLAN.md` (committed before the derivation, at `182eeb21`; PLAN does not name R-EX). It adopts no criterion, premise or extension E,
edits no manuscript or reviewed record, runs no computation and changes no status. Physical source
remains NOT PASSED. D5 stays open (#1169 c.7065620072).

Tracking: Issue #1507; draft PR #1508. Background: GATE-A r5.6 (#1503 at `fd3cb064`, cited `GA §`).
Base: `main` at `df6da1c6`. `Sub:n`, `Main:n`, `Meth:n` are lines of `papers/Substratum.md`,
`papers/Main.md`, `papers/Methodology.md` there. Layers: X exact algebra on paper; P paper
argument; K kernel theorem on `main`, cited and not duplicated.

## 0. Summary and the three questions

**Main findings.**

1. **Lemma S1 ((I); layer X).** A permutation dilation realizes a unitary channel Ad_W only if W
   is monomial, under the five assumptions (a)–(e) of §2.1: fixed configuration basis, the
   Born-form dilation as the definition of the visible family, preparation independence (one
   hidden state ω for every input), a unitary target on all inputs including coherent ones
   (beyond the native interface), and a countable hidden carrier. The diagonal-prior case is
   already in the corpus (`Main:328`, `:338`, `:340`, `:746`); the extension to an arbitrary
   coherent hidden state on a countable carrier is the added content. **Grade: ELABORATING.**
   S1 rules out only the **representational** target I★_st-coh. It does not rule out classical
   simulators operationally: three countermodels (CM-1 to CM-3, §2.1) show that each of (a), (c)
   and the coherent-input requirement (d) is load-bearing.
2. **Proposition S2, the resource statement at the scope established ((I); layer X).** Under (b),
   (c), (d) and (e), **for every logical encoding** (so without (a)), a one-step unitary channel of
   a permutation dilation has, up to a global phase, only roots of unity as eigenvalues. So an
   exact single-time rotation Ad_{R_θ} with θ/π irrational is not realizable by any bijection with
   any fixed countable hidden state under any encoding. Within that representational scope, a
   native realization needs at least one resource outside the class: a non-monomial operation on
   the configuration span (FLOW), preparation-dependent coherent hidden states (dropping (c)), an
   uncountable hidden carrier with a non-classical hidden state (dropping (e); not treated), or a
   realization by protocol rather than autonomous evolution (dropping (b); Stage 2, where D-W
   shows that operational exactness needs no such resource). **No operational resource statement
   is established**: S2 says what the Born-form target needs, not what an embedded observer's data
   require.
3. **I★ versus I★_st (definitional mismatch, not a logical distinction).** I★ implies the
   operational single-time variant, and so I★_st-pop, under one recorded assumption, ID-FE: the
   free evolution for time t is identified with the requested instrument Λ_t. I★ does not imply
   I★_st-coh because the two definitions impose different realization requirements (Born-form
   lift against record laws; autonomous φ^t against a requested instrument; fixed visible
   configurations against a declared X_A with a label rule). The r1 "GA §2.4 correction" is
   withdrawn as a correction. Two typing defects of GA §2.4 are recorded instead as proposals for
   the owner (§9), and #1503 is not edited.
4. **R-EX is a representational condition, (I) on complex kinematics (KIN), and not an
   independent sourcing criterion.** It is exact agreement in the Born form of the model's own
   configuration span. A D-W whose E posits a quantum register passes it; every bijective dynamics
   with a fixed countable hidden state fails it, native OI included, because of its representation
   rather than for lack of a source. It moves the source question to O1 (FLOW) without answering it,
   and it does not discharge I-3. PLAN.md did not name R-EX, so its scoring under the PLAN decision
   rule (§5) is post hoc for R-EX specifically. It also stands in tension with the bijective form of
   the OI hypothesis (§5).
5. **Clause (iv) of T-SUB′ fails the acceptance standard in every reading.**
   - Read literally, *(iv)-recoverable* applied to instrument labels excludes every EP-schema model
     with program-dependent instruments (Lemma R2, (I) on EP:79).
   - Repaired to the system's own ontic state, it is ψ-ontology. That horn is **decisive** under the
     owner's standard: it excludes legitimate ψ-ontic quantum models (de Broglie–Bohm, Everett, GRW)
     before any theorem is used. The PBR horn (PIP) and the Colbeck–Renner horn ((xiv) beyond its
     Bell scope) are further (I) consequences.
   - *(iv)-explicit* is evaded by redescription (Lemma I).
   - At Stage 1-pop the dilemma recurs without PBR (Lemma R1, ELABORATING on R2).
6. **N2 survey.** Complexity (C-CX), counterfactual linearity (C-LIN), locality (C-LOC),
   thermodynamics (C-TH) and symmetric hard-to-vary (T-HTV′) were scored on the three classes, with
   the C3 cell scored by one standard for all (the hypothetical FLOW member of PLAN §3 counts). None
   supplies an independently justified sourcing criterion. C-CX fails the C1 cell; C-TH fails the
   C3 cell; C-LOC and (iv) fail the C2 cell; C-LIN is conditional on a counterfactual-law reading.
7. **N3.** The distinction is ill-posed **operationally** (Lemma O: for observers inside a
   D-W-tot, no function of their data separates it from a genuine quantum model). The decisive
   structural lines found are representational. Every one found places the known native class on
   the simulator's side unless FLOW holds (AW-I3-1).

**Established.**
- Lemma S1 and Proposition S2, layer X, under the assumptions named in their statements.
- Countermodels CM-1 to CM-3 (from the review addendum, layer X).
- Lemmas R1, R2, I and O, and Lemma L1 for injective encodings, layer P.
- The definitional analysis of I★ against I★_st (P).

**Assumed.**
- S1: (a) fixed configuration basis; (b) the Born-form dilation form; (c) preparation independence;
  (d) a unitary target on coherent inputs beyond the native interface (c.7064942473); (e) countable
  hidden carrier. S2: (b)–(e). (b) is the corpus's representation (KIN, decision 4); (c) and (d) are
  imported operational assumptions; hence (I).
- I★ ⇒ I★_st-pop: ID-FE.
- R-EX: KIN. C-CX: H1–H5 (#1498) and BQP ⊄ BPP. ψ-ontology horns: the ontological-models
  framework plus PIP [PBR] or free choice [CR]. R2: EP:79. C-LIN: CI-3 (§4.2).

**Missing.**
- The earliest unsupported step is a **physical mechanism** for a non-monomial coherent operation
  (FLOW) or for preparation-dependent coherent hidden states; S2 states that one of the listed
  resources is needed, at the representational scope only.
- An operational counterpart of S2 (what embedded observers' data require) is not established;
  at Stage 2 D-W shows none follows from exactness alone.
- Open **mathematics**: the non-unitary single-time channels reachable by permutations with a
  coherent hidden state; uncountable hidden carriers with non-classical hidden states; C-LIN for
  ontological native models; register shielding in universal reversible substrata (CI-2).

## 1. Literature (audit Step 4)

| Topic | Source | Use here |
|---|---|---|
| Ontological models; ψ-complete / ψ-supplemented / ψ-epistemic | N. Harrigan, R. W. Spekkens, Found. Phys. 40, 125 (2010); E. Beltrametti, S. Bugajski, J. Phys. A 28, 3329 (1995) | D-W is the ψ-complete model (#1506 §4.3) |
| PBR | M. F. Pusey, J. Barrett, T. Rudolph, Nat. Phys. 8, 475 (2012) | ψ-ontic under PIP; PIP named as import (§4.5) |
| PIP is load-bearing | P. G. Lewis, D. Jennings, J. Barrett, T. Rudolph, PRL 109, 150404 (2012) (ψ-epistemic models for projective measurements in every finite dimension, ψ-epistemic for some pairs of states; extra assumptions are always necessary); pairwise version: S. Aaronson, A. Bouland, L. Chua, G. Lowther, PRA 88, 032111 (2013); M. Schlosshauer, A. Fine, PRL 108, 260404 (2012); J. Emerson et al., arXiv:1312.1345 | without PIP, ψ-epistemic models exist at prepare-and-measure scope |
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

**Lemma S1 ((I) on (b)–(d); layer X).** Let C_V be finite and H countable. Let φ be a bijection of C_V × H with
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

**The assumptions that make S1 true** (review addendum c.7065957850, §1).

| # | Assumption | Where the proof uses it | Status |
|---|---|---|---|
| (a) | Fixed configuration basis: the logical basis of A is |A| visible configurations (enc_A, R-ST) | step 6 | definition of the target |
| (b) | The visible family is *defined* as the Born-form lift Tr_H[φ̂^t(ρ ⊗ ω)φ̂^{−t}], not an observed quantity | throughout | corpus representation (KIN, decision 4) |
| (c) | Preparation independence: the input is ρ ⊗ ω with one ω for every ρ | steps 2 and 5 | imported |
| (d) | A unitary target on all ρ, coherent ρ_V included; coherent ρ_V are not natively preparable or readable at the single-time interface | step 3 | imported, beyond the native interface (c.7064942473) |
| (e) | Countable H | step 1 | scope |

Auxiliary systems are covered (they are part of H). Observer-controlled permutations are covered
when the controller sits in H in a fixed state; a setting that depends on the preparation falls
under (c). S1 is exact algebra about the representation (a)–(e); with (c) and (d) imported it is
labelled (I).

**Corollary S1′ ((I); layer X, with `Main:328`, `:338` at layer P).** Take A = Fin 2, trivial K
and Λ_t = Ad_{H^t}, with H the Hadamard matrix (non-monomial: `hadamard_not_monomial`,
`OIBridge/C5Discovery.lean`:162, K). Under (a)–(e), the representational target I★_st-coh fails
for every model (C_V × H, φ, ω) with ω any density operator on countable H. For a classical
hidden prior on a measurable carrier the same holds by the diagonal-preservation corollary already
in the corpus (`Main:328`, `:338`; the Hadamard boundary `Main:340`; `Main:746`).

**Scope.** S1′ is a no-go for the representational target I★_st-coh, under (a)–(d). It is not an
operational no-go for classical simulators: it distinguishes a classical simulator from genuine QM
only through the representational requirements (a)–(d).

**Countermodels bounding S1′** (review addendum c.7065957850, §2; layer X).
- **CM-1 (native readout, populations).** On {0,1} × {0,1} with a uniform diagonal prior, the
  involution (v, h) ↦ (v ⊕ h, h) gives T(1) uniform and T(2) = id: exactly the Hadamard
  populations |⟨j|H^t|i⟩|² at every t. A native bijection with a classical prior meets I★_st-pop for
  the Hadamard target; it fails I★_st-coh only through Born-form coherences, which `Main:328` makes
  diagonal. The exclusion is imposed by (b) and (d), not by anything an embedded observer sees.
- **CM-2 (change of logical basis).** H = UZU† with Z = diag(1, −1). With hidden pair {h₁, h₂},
  χ = (|h₁⟩ − |h₂⟩)/√2 and the bijection that fixes (a, h) and swaps the hidden pair at b, the
  channel is exactly Ad_Z, which is Hadamard under the logical encoding U. Consistent with S1 (Z is
  monomial); it shows that S1′ needs (a). With no hidden system at all, the swap X is unitarily
  equivalent to H (both have eigenvalues ±1), so dropping (a) alone already meets the Hadamard
  target, even with a classical prior.
- **CM-3 (preparation dependence).** χ₀ = (|h₁⟩ + |h₂⟩)/√2 with (0, h₁) ↦ (0, g₁), (0, h₂) ↦ (1, g₁);
  χ₁ = (|h₃⟩ − |h₄⟩)/√2 with (1, h₃) ↦ (0, g₂), (1, h₄) ↦ (1, g₂). Then P(|v⟩ ⊗ χ_v) = |±⟩ ⊗ |g_v⟩:
  every configuration preparation goes to the Hadamard output. S1 does not apply, because (c)
  fails. It needs coherent hidden states, which have no meaning as classical laws; with diagonal
  preparation-dependent priors the output stays diagonal.
- **CM-4.** Observer-controlled permutations reduce to S1 (fixed controller state) or to CM-3
  (preparation-dependent controller).

**Proposition S2 (spectral form; (I) on (b)–(d); layer X).** Assume (b), (c), (d), (e), not (a).
If Φ_1 = Ad_W for a unitary W on ℂ^{C_V}, then, up to a global phase, every eigenvalue of W is a
root of unity.

*Proof.*
1. Steps 1–4 of S1 give P(|v⟩ ⊗ |χ⟩) = W|v⟩ ⊗ |e⟩, and steps 5–6 give W monomial:
   W|v⟩ = d_v|σ(v)⟩ for a permutation σ of C_V and unimodular d_v.
2. P maps the basis points {v} × supp χ bijectively onto {σ(v)} × supp e and carries amplitudes
   unchanged. So, as multisets of nonzero amplitudes, {χ_h} = d_v · {e_{h′}} for every v. Hence
   {e} = r · {e} for each ratio r = d_v/d_{v′}.
3. The values of e of maximal modulus form a finite nonempty set (e ∈ ℓ²), invariant under
   multiplication by r. So r permutes finitely many points of a circle, and r is a root of unity.
4. So W = d · D′P_σ with D′ diagonal of roots of unity. On a cycle of σ of length L, the
   eigenvalues λ of D′P_σ satisfy λ^L = the product of the D′ entries on the cycle, a root of
   unity. So λ is a root of unity. ∎

A change of logical basis U changes W to UWU†, which has the same spectrum, so S2 holds for every
encoding. **Consequence.** For R_θ with θ/π irrational, the eigenvalue ratio e^{2iθ} is not a root
of unity, so Ad_{R_θ} is not the one-step channel of any bijection with any fixed countable hidden
state under any logical encoding. The diagonal-prior case gives W proportional to a permutation
matrix (all ratios 1). Relation to the corpus: `Main:650` (finite order of a bijection on a finite
set) and the countable-covering results of `OIBridge/CoherentContinuumSource.lean` are of the same
family; no formal map is claimed. Grade: ELABORATING (pending review).

**What meets I★_st-coh.** For one fixed target family, the target's own dilation (A ⊗ K, W, σ_K)
does; it is not a bijection model. Hosting every family at once needs a sector or setting indexed by
(A, Λ) (§9, typing defect T2).

**Answer to N1 (coherent).** Clauses (i)–(iii) of T-SUB′ restrict Φ to the substratum update, a
bijection; so under (a)–(e) no T-SUB′-admissible model meets I★_st-coh for Ad_H, under any
reading of (iv), and by S2 none meets it for Ad_{R_θ} under any encoding. The (iv) dilemma is not
reached at Stage 1-coh. This is a property of the representational target, not a sourcing test.

**Skepticism.** The exclusion is mathematical, not operational: CM-1 meets the population data
natively. The notion `∼` predates D-W (`Sub:249` at `e7ed439d`, 2026-11-11); its use as a source
criterion through I★_st-coh dates from GA r5.3 (2026-11-21), after D-W. The vintage defence covers
the notion, not its selection for I-3.

**Verdict N1.1.** S1: ELABORATING (the coherent-hidden-state extension; S1′ for diagonal priors is
CONFIRMING of `Main:328`, `:338`, `:340`, `:746`). S2: ELABORATING, pending review.

**I★ and the single-time variants (P; definitional).**
- I★ (GA §2) fixes record laws p(h | π, p) for every protocol of `J_exact(A)`, on a declared X_A
  with a label rule. Each Λ_t is a one-outcome CPTP instrument of `J_exact(A)`, so I★ gives, for
  every ρ and readout E, the law Tr(E Λ_t(ρ)) of the protocol "prepare ρ, apply Λ_t, read E" (the
  operational single-time variant, I★_st-op).
- **I★ ⇒ I★_st-op, and on configuration preparations with fixed-basis readout I★ ⇒ I★_st-pop**,
  given compatible encodings and the assumption **ID-FE**: the single-time family's evolution for
  time t is the requested instrument Λ_t, not the model's autonomous step.
- I★ ⇏ I★_st-coh because the definitions differ in three named respects: (i) realization
  requirement (Born-form lift against record laws); (ii) dynamics (autonomous φ^t against a
  requested instrument); (iii) encoding (visible configurations fixed by R-ST against a declared X_A
  with a label rule). This is a mismatch of definitions, not a logical distinction between targets
  of one kind. D-W illustrates it but does not create it: a genuine quantum model meeting I★ also
  fails I★_st-coh unless its ontic dynamics is a configuration-span unitary.

### 2.2 N1.2, the population variant

I★_st-pop compares classical stochastic families T(t). D-W meets it, and so do response-table
models (sketch). Response-table models compute their prior from T, so they are comparator-fitted
(I-2★, EP:102).

**Lemma R1 ((I) on the target's single-model typing; layer P; counting).** Fix one model M* with **one** hidden prior and countably many
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

**Verdict N1.2: ELABORATING (on R2).** The (iv) dilemma persists at Stage 1-pop without PBR, for
its class. Its horns there are the counting Lemma R1 and ergodic decoding (a plausible sketch, P).

## 3. Lemma R2: clause (iv) on instrument labels ((I) on EP:79; P)

**Lemma R2 ((I) on EP:79, the Gate A contract, as for L-H′).** Under EP:79, a change of future program loads only
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

**Verdict: NEW.** This is a hidden assumption in GA §2.2's definition, independent of PBR. It
also corrects the reading of c.7065260286, which did not restrict the region.

## 4. N2: candidate criteria, each with justification and the three-class test

### 4.1 C-CX, resource or complexity separation

- *Justification.* Deutsch 1985 and *Fabric of Reality* ch. 9: physical resources must be
  accounted for. Montina 2008. BQ1 (#1498).
- *C1.* D-W's register has 4ⁿ entries for n qubits. It is excluded only asymptotically, and only
  if BQP ⊄ BPP (imported conjecture). Gottesman–Knill (Cuffaro 2017) shows that resource arguments
  depend on the circuit family.
- *C2.* Admitted: genuine QM hosts BQP polynomially.
- *C3.* The known native class (H1–H5) runs in BPP (BQ1-D, (I)); the hypothetical FLOW member of
  PLAN §3 is not excluded by C-CX's own terms. Under the single standard used for every criterion
  (the FLOW member counts), the C3 cell passes.
- *Scope.* I★ demands exactness at each finite carrier, not efficiency.
- **Verdict: fails the C1 cell.** The exclusion of D-W is only asymptotic and conditional on
  BQP ⊄ BPP (I), while I★ concerns exactness at each finite carrier.

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
- **Verdict: conditional (CI-3); ELABORATING; its decisive content is R-EX's representation (§5).**

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
- "No consumed randomness" admits Everett (C2 cell passes) but excludes every hidden-prior model by
  its own terms, the hypothetical FLOW member of C3 included, since Lemma E holds for every EP-schema
  model. It **fails the C3 cell**.
- Quantities invariant under measure-theoretic isomorphism (Kolmogorov–Sinai entropy; Ornstein)
  cannot separate D-W from its encrypted copies (Lemma I).
- Valentini non-equilibrium is falsifiable, but it applies to every hidden-prior model, C1 and C3
  alike.

**Verdict: fails the C3 cell.**

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

**Verdict: fails the C2 cell in every reading; the ψ-ontology horn is decisive** under
c.7065620072 ("does not exclude legitimate quantum models merely because their physical states
encode quantum information"): Bohm is ψ-supplemented and Everett and GRW are ψ-complete in the
Harrigan–Spekkens sense, before PBR is invoked. NEW relative to GA §2.2, which assessed the PBR horn
only.

### 4.6 T-HTV′ applied symmetrically

- D-W's class is easy to vary: swap the register type for a GPT state (Barrett 2007).
- The standard axiomatic presentation of QM is varied in the same way: real or quaternionic
  kinematics, or GPTs.
- Given its Hilbert-space register, D-W's branch rule is forced (Gleason; Busch), exactly as for QM.
- So, applied symmetrically, the criterion ranks D-W with axiomatic QM. What it penalizes is
  **imported kinematics** (KIN) and comparator copying (EP:102), not the source of operations.
- **Verdict: survives only as a judgment on KIN derivation** (reconstructions: Hardy 2001;
  Masanes–Müller; Chiribella–D'Ariano–Perinotti). **ELABORATING.**

## 5. R-EX: a representational condition, and the three-class table

**R-EX ((I): KIN; a representational admissibility condition, not a sourcing criterion).** For
every instrument of the target interface, the model realizes an apparatus procedure whose Born-form
instrument on the carrier's configuration span, with apparatus and hidden state traced out, equals
the target instrument. At Stage 1, R-EX is I★_st-coh. At Stage 2 it would add a coherent-lift
exactness clause to I★, which changes the target (an owner decision); its comparator objects are
J-coh-level, so Stage-2 results stay (I).

- **What it requires.** Exact agreement plus a choice of representation ((a)–(b) of §2.1). It says
  nothing about where non-monomial dynamics comes from.
- **What it admits.** Any E that posits a quantum register or flow. A D-W whose register dynamics
  is declared unitary passes, and is rejected only if O1 later rejects that posit.
- **What it excludes.** Every bijective dynamics with a classical prior or with any fixed countable
  hidden state, native OI included (S1, S2, CM-1), because of their representation, not because
  they lack a source.
- **Justification.** The realist reading of `∼` with KIN. That is a choice of representation, not an
  independent physical argument separating source from simulation. Under the owner's standard R-EX
  does **not** supply an independently justified sourcing criterion and does not discharge I-3.
- **Tension with the OI hypothesis.** R-EX requires the quantum dynamics to be a non-monomial
  unitary structure on the model's own configuration span. By S1 and S2 that excludes every
  bijective dynamics with a fixed countable hidden state. It therefore decides against the
  bijective-substratum form of the OI hypothesis (c.6891338304: "Observational incompleteness
  explains our perception of quantum mechanics") unless E extends Φ beyond a bijection.
- **Provenance.** PLAN.md (`182eeb21`) fixed the four-cell rule and the classes before the
  derivation; it did not name R-EX. R-EX's scoring below is therefore post hoc for R-EX.

**Three-class table.** The C3 cell is scored by one standard throughout: the hypothetical FLOW
member of PLAN §3 counts, and a criterion fails the cell only if its own terms exclude that member.

| Criterion | Independent of D-W | C1 excluded (all variants) | C2 admitted | C3 by its own terms | Verdict |
|---|---|---|---|---|---|
| R-EX | the notion predates D-W (`Sub:249`, 2026-11-11); its selection for I-3 does not (GA r5.3) | yes, representationally (S1, S2); a D-W with a posited quantum register passes | yes, with a configuration basis | FLOW member not excluded; every known member excluded | representational condition, (I): KIN; cells met post hoc; **not a sourcing criterion** |
| C-CX | yes (Deutsch, Montina) | **no**: only asymptotically, if BQP ⊄ BPP | yes | FLOW member not excluded | **fails the C1 cell** |
| C-LIN | only under CI-3 | CI-3 yes (L1, injective encodings, P); CI-1 no; CI-2 open | yes | Born-form yes; ontological open | conditional; content = R-EX's representation |
| C-LOC (ontological) | yes | yes | **no** | Prop. U, (I) | fails the C2 cell |
| C-TH | yes | yes | yes (Everett) | **no** (Lemma E binds every EP model) | fails the C3 cell |
| (iv)-recoverable (system) | yes (ψ-ontology) | yes | **no** (Bohm, Everett, GRW) | unknown | fails the C2 cell (decisive) |
| (iv)-recoverable (literal) | — | yes | no | every EP model excluded (R2, (I) on EP:79) | fails |
| (iv)-explicit | — | **no** (Lemma I) | yes | — | fails the C1 cell |
| T-HTV′ symmetric | yes (§A.29) | only through KIN/EP:102 | judgment | judgment | judgment on KIN |

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
- The distinction is ill-posed operationally (Lemma O). The decisive structural lines found are
  representational (R-EX; C-LIN under CI-3), and they separate representations, not sources.
- Both place the known native class on D-W's side of the line, because native dynamics is a
  permutation.
- That is a result about the current construction, stated for its class (permutation dynamics with
  a fixed countable hidden state, under (b)–(e)). It is not a no-go for observer-level extensions
  that supply FLOW or preparation-dependent coherent hidden states.

## 7. Assumption-watch markers

- **AW-I3-1.** Every decisive line found that separates C1 from C2 (R-EX, C-LIN/CI-3) is
  representational, and the known C3 class falls on C1's side of it unless FLOW holds. A future sourcing claim must say which
  line it crosses and how.
- **AW-I3-2.** Any (iv)-type clause must name its region: system, setting or controller. Otherwise
  it excludes every EP model (R2) or every laboratory with a continuous dial (R1).
- **AW-I3-3.** Colbeck–Renner's free choice is (xiv) beyond its Bell scope. It joins BQ1's H3
  (#1498) and Proposition U (#1504) as the third use of (xiv) outside `Main:736`'s scope.

## 8. Classification (§A.31) and productivity

| Item | Class |
|---|---|
| S1 | ELABORATING (coherent-hidden-state extension); S1′ for diagonal priors CONFIRMING (`Main:328`, `:338`, `:340`, `:746`) |
| S2 (spectral resource statement) | ELABORATING, pending review |
| CM-1 to CM-3 | countercontrols bounding S1′ (from the review addendum) |
| I★ against I★_st | ELABORATING (definitional mismatch; conditional implication under ID-FE) |
| R1 | ELABORATING (on R2) |
| R2 | NEW, (I) on EP:79 (hidden assumption in GA §2.2) |
| ψ-ontology C2 failure of (iv) | NEW relative to GA §2.2; decisive |
| R-EX | ELABORATING (a representational condition; not a sourcing criterion) |
| L1, C-LIN | ELABORATING |
| C-CX | CONFIRMING (BQ1) |
| C-LOC, C-TH, T-HTV′ symmetric | ELABORATING |
| Lemma O | CONFIRMING |
| Lemma I | ELABORATING (formalizes GA §2.2's redescription pattern) |

Productivity test (PLAN §4): met through (b) for the class of permutation dilations with a fixed
countable hidden state under (b)–(e) (S2), and (c) through R2 and the definitional analysis of I★
against I★_st. Not met through (a): no independently justified sourcing criterion was found. The
fixed point is not reached.

## 9. For owner decision (nothing adopted)

- **D5.** No independently justified sourcing criterion was found; D5 stays open. R-EX is offered
  only as a representational admissibility condition, (I): KIN, which does not discharge I-3,
  stands in tension with the bijective form of the OI hypothesis, and moves the source question to
  O1 without answering it. The resource statement S2 holds at the representational scope only.
- **D6 (proposals; #1503 not edited).**
  - **T1.** GA §2.4's "Both variants are strictly weaker than I★" is mistyped for I★_st-coh: the
    definitions impose different realization requirements (§2.1). It holds, under ID-FE, for an
    operational single-time variant, which on the native interface is I★_st-pop.
  - **T2.** GA §2.4 gives "the one model M* ... a visible sector V_A encoded by enc_A, with its hidden
    prior" for every family Λ_A. With φ and the prior fixed, a sector indexed by A alone has one
    autonomous family, so both I★_st variants are unsatisfiable by every model, the target's own
    dilation included, unless the sector or a setting is indexed by (A, Λ). R1 reads it that way.
  - Whether to record ID-FE as an assumption of the staging.
- **GA §2.2 (iv).** R2 and §4.5 are for its reviewer; GA is not edited here.

## 10. What this note does not do

It edits no manuscript, no reviewed record and no Issue body. It runs no computation and
dispatches no workflow. It proposes no E, adopts no criterion and posts nothing on #1169.
