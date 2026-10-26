# Introductory paper: contribution statement (design stage, for owner review)

Main commit `687e885b`. Claim IDs are those of `OUTLINE.md` and `SOURCES.md`. The wording is meant
for the paper's own technical register (§A.32/§A.33): it states content and status, not the
framework's merits. Originality labels:
- **KNOWN**: AUDIT r4 gives KNOWN, on full text;
- **covered in kind**: AUDIT r4 gives PARTLY KNOWN or REFRAMING, or the source package itself
  labels the item a finite form of a known fact;
- **candidate**: NOVEL-CANDIDATE, novelty unverified;
- **unverified**: no literature was examined.

Correctness and originality are separate columns. A kernel proof does not establish originality,
and KNOWN does not count against correctness.

## Draft contribution paragraph, for the paper

> This paper presents observational incompleteness (OI) as a physical hypothesis — that the
> statistics an embedded observer records are the visible marginals of a finite reversible
> deterministic system of which the observer is a proper part — and states which of its
> consequences are theorems at the level of finite-horizon observable laws. At any finite horizon,
> finite stochastic laws, visible marginals of finite reversible dynamics, and fixed-basis Born
> records of finite unitary systems are the same class of laws; the class contains the Markov laws,
> so representability alone carries no discriminating content, and the Born dictionary is part of
> the definition of the quantum class rather than an output. The components of this equivalence
> are known (Egri et al. for the trajectory-labelling realization; Barandes for permutation
> dynamics as unistochastic processes); it is given here with a machine-checked (Lean 4/Mathlib)
> proof of each direction. The discriminating content is stated in two elementary forms: by the
> data-processing inequality, every deterministic completion carries the visible predictive
> information in its hidden state; and on one finite reversible representative, finite recurrence
> together with the contraction property of stochastic maps (Rivas, Huelga and Plenio 2014,
> Thm 2.4; Buscemi and Datta 2016) makes history readback force stochastic indivisibility within
> the recurrence cycle. The paper separates three statuses: finite observable-law representability
> (proved), exact finite operational quantum mechanics (characterized under five completion
> conditions, each independent of embedded observation, none supplied by it), and selection of the
> evolution relating two times (open). A bounded application treats black-hole information
> recovery as a question about an observer's access class: in finite reversible models, global
> bijectivity neither implies nor is necessary for recovery from accessible records, and the Page
> entropy enters the framework's argument through a scrambling hypothesis, not through bijectivity.

This paragraph is adapted from AUDIT r4's surviving novelty statement (AUDIT:1983–2016) and narrowed
to the recommended scope. The C8-R sentence is removed (Alt-X only). The wording "machine-checked"
has two conditions:
- It must be backed by a Lean build and axiom report at the drafting commit. AUDIT §0.3 records
  that no build was observed in the audit (AUDIT:277).
- The paper must list the unformalized steps beside it (OUTLINE §8-d).

## (a) Contribution as exposition and perspective

1. **The hypothesis, stated with its status.** It is a hypothesis about nature. The physical
   identification is a representation choice, and no ontology-level falsifier is established
   (§1-a; Main:62, :702–704).
2. **One consolidated statement of the finite correspondence**, E1, at its proved scope: finite
   horizon, fixed basis, initial law on $V\times H$, Markov laws included. It is assembled from
   statements spread across Main §1.5 and §3.4 (§3-a to §3-h).
3. **Where the discriminating content lies.** This is hidden predictive memory (§4-a, §4-b) and
   recurrence indivisibility (§5-c, §5-e), with the scope limit set by the XOR family (§5-f) and
   by the Hadamard family (§5-g).
4. **The boundary between reproduced behaviour and a derivation**, drawn in four results:
   - representation is not explanation (§6-a);
   - the visible law does not select the relating evolution (§6-b);
   - operational QM is reached exactly under five named conditions that bare finite OI does not
     supply (§6-d);
   - no fixed finite carrier reproduces a qubit exactly (§6-e).
5. **A bounded application**: black-hole information as an observer-access problem, with every
   conditional step named (§7).
6. **An explicit list of open problems** (§8).

## (b) Mathematical components stated with proof or kernel citation

"Correctness layer" gives what establishes the statement in this repository: kernel, exact
computation, prose proof or literature.

| ID | Component | Correctness layer | Originality |
|---|---|---|---|
| §3-a | $S\iff D\iff Q_{\mathrm{fb}}$ at finite horizon (E1) | kernel, all six directions (`finite_horizon_equivalence`) | covered in kind: PARTLY KNOWN, components known; packaging of the multi-time fixed-basis three-way identification not located, PROVISIONAL (comb-realization literature unread) |
| §3-b | S⇒D, one iterated bijection, correlated initial law | kernel (`S_imp_D`) | covered in kind: PARTLY KNOWN (EG Prop. 13; elementary strengthening) |
| §3-c | S⇒D with hidden prior independent of $x_0$ | prose proof + exact probes; not formalized | covered in kind: PARTLY KNOWN (EG Prop. 16; LPW Prop. 1.5) |
| §3-d | D⇒$Q_{\mathrm{fb}}$ (permutation unitary) | kernel | KNOWN (Barandes B25, B23, B26) |
| §3-e | $Q_{\mathrm{fb}}$⇒S | kernel | covered in kind: REFRAMING (Strasberg–García Díaz Eq. (3)) |
| §3-g | Born form internal; exponent not selected | prose + probe | KNOWN, non-discriminating (B26 Thm 3.1) |
| §4-a | Unavoidable hidden predictive memory (a)–(c) | kernel for the joint law; time-$t$ reading not formalized | covered in kind: REFRAMING (DPI); attribution PROVISIONAL |
| §4-b | Memory biconditional (prose, directions named) | kernel components + prose; two links not formalized | covered in kind: REFRAMING |
| §4-c | Capacity bound $\log_2 m\ge I^*$ | kernel | covered in kind: REFRAMING; PROVISIONAL |
| §4-d | Readback lemma $I\ge p_0\delta^2/\ln2$ | prose proof (Pinsker) + exact probe | covered in kind: REFRAMING; PROVISIONAL |
| §4-e | (ii) ⟺ (iii), corrected (iii) (F29), prose only | prose proof, both directions; finite acceptance test | covered in kind: REFRAMING, near-definitional |
| §5-b | Minimal model with non-stochastic $\Lambda(2,1)$ and memory witness | exact computation | unverified (illustration; not examined) |
| §5-c | Non-permutation step + recurrence ⇒ P-indivisible | kernel (rooted form) + prose | KNOWN (RHP 2014 Thm 2.4; BD Prop. 1) |
| §5-e | Stochastic-inverse lemma; readback ⇒ indivisibility in the recurrence cycle | kernel (lemma; routed level); history-level step prose | KNOWN |
| §5-f | XOR family: memory without short-window P-indivisibility | exact probe | KNOWN (RHP 2014 Eq. (15)) |
| §5-g | Population P-indivisibility ≠ quantum non-Markovianity outside the diagonal-preserving class | prose proof + exact probe | unverified (not examined) |
| §6-b | Visible law does not fix the relating evolution (kernel-backed clauses) | kernel | unverified (not examined) |
| §6-d | Operational-completion characterization (E2); independence of (i)–(v); bare OI ⇏ QM | kernel | unverified (not examined in AUDIT r4) |
| §6-e | No fixed finite carrier reproduces a qubit exactly | prose (factorization) + imported unbounded-rank result | covered in kind: REFRAMING (Hardy-type); PROVISIONAL |
| §7-c, §7-d | Bijectivity vs accessible recovery: counterexamples; complete-access sufficiency; $P_{\mathrm{succ}}\ge1/\lvert K\rvert$ | written proof + exhaustive exact enumeration (finite toy access model); separate-agent internal review ACCEPT | covered in kind (the package itself labels C2 and C4 classical forms of known facts); not literature-mapped, so unverified beyond that |
| §7-e | Nested trace-out consistency is a Fubini identity | written proof + exhaustive check; reviewed | unverified |
| §7-f | GR A.7's decoupling support reversed by ≥ $10^{57}$ | exact interval arithmetic; reviewed independently | not an originality item (audit observation) |
| §7-g, §7-h | Permutations on configuration states make no entanglement; the Page value enters only through H-scramble | proofs + exhaustive exact sweeps; reviewed | covered in kind (elementary); not literature-mapped |
| §7-i | Page-time fraction $1-(\beta/(1+\beta))^{3/2}$ and its β-dependence | exact algebra + literature | KNOWN (Page 2013 Eq. (8); Page 2005) |
| Alt-X: C8-R | Rooted families realizable by one finite permutation with a shared prior = `PPer` | kernel (`finiteRootedRealizable_iff_pper`), finite visible only, zero-prior padding used | **candidate**: NOVEL-CANDIDATE, novelty unverified. Sufficiency half PARTLY KNOWN (EG Props. 16–18); necessity folklore; **no priority sentence**. It would be new manuscript content: no statement on `main` (AUDIT:938–946) |

## (c) Explicit non-claims

The paper should state these in its own voice, at the sites given.

1. **No derivation of quantum mechanics.**
   - E1 is a representation equivalence. It contains every finite law, Markov laws included.
   - The Born dictionary is part of the definition of $Q_{\mathrm{fb}}$, and its exponent is not
     selected (Main:534).
2. **No unique selection of the operational theory.**
   - Exact finite operational QM follows only under the five completion conditions, each
     independent of the others and of the C1–C4 process, and bare finite OI supplies none of them
     (GR:220–226; Main:352).
   - The ε-realization theorems are not uniqueness theorems (Main:562).
   - The visible law does not fix the relating evolution (Main:624).
3. **No claim that the physical hypothesis is established or tested.** The theorems are
   mathematical, and no ontology-level falsifier is established (Main:704).
4. **No characterization of non-Markovianity by the existence of a realization.** That form is
   false (Main:596–598), and (ii) ⟺ (iii) is near-definitional (Main:608).
5. **No identification of stochastic P-indivisibility with quantum non-Markovianity** (Main:330,
   :334). No claim that (C4) forces indivisibility on short windows (Main:141).
6. **Black hole.** The paper claims no resolution of the information paradox. It also claims none
   of the following:
   - a derivation of the Page curve: under H-scramble only, and H-scramble fails for bijections
     acting on configuration states;
   - a universal 0.646 Page time: conditional on β = 1;
   - a microscopic realization of islands: conjectural;
   - a proof of the generalized second law: open;
   - decoupling of the trans-cosmological sector over the evaporation: its stated support is
     reversed (BH01 item F).

   Every black-hole computation is a finite toy model. Its reviews are separate-agent internal
   reviews, not external validation or owner adoption.
7. **No priority or novelty sentence.** In particular, none for C8-R, nor for the XOR example. The
   XOR example is RHP 2014 Eq. (15), and the paper makes no claim about who stated it first.
8. **No statement of the ≤ n³ compressed bound** (F13 unresolved).
