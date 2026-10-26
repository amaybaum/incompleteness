# Introductory paper: contribution statement, revision 4 (design stage, for owner review)

Revision 4. It applies `paper/review/RECHECK-r3.md` (RC-A; nits n-A to n-F). Revisions 1 to 3 are kept
unchanged. Revision 2 applied `paper/review/REVIEW.md`; revision 3 applied `RECHECK-r2.md` and the owner's
decision to replace the Explainer. `CHANGES-r2.md`, `CHANGES-r3.md` and `CHANGES-r4.md` record the changes.

The main commit is `687e885b`, and the claim IDs are those of `OUTLINE-r4.md` and
`SOURCES-r4.md`. The register is the paper's own (§A.32/§A.33).

Originality labels:
- **KNOWN**: AUDIT r4 gives KNOWN, on full text;
- **covered in kind**: AUDIT r4 gives PARTLY KNOWN or REFRAMING, or the source package itself
  describes the item as a finite form of a known fact;
- **candidate**: NOVEL-CANDIDATE, with novelty unverified;
- **unverified**: not classified, because no literature was examined.

Correctness and originality are separate columns.

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
> dynamics as unistochastic processes); each direction is proved here and checked in Lean 4/Mathlib
> at a stated commit. The discriminating content is stated in two elementary forms: by the
> data-processing inequality, every deterministic completion carries at least the visible
> predictive information in its hidden state; and on one finite reversible representative, finite
> recurrence together with the contraction property of stochastic maps (Rivas, Huelga and Plenio
> 2014, Thm 2.4; Buscemi and Datta 2016) makes history readback force stochastic indivisibility
> within the recurrence cycle. The paper separates three statuses: finite observable-law
> representability (proved), exact finite operational quantum mechanics (characterized under five
> completion conditions, each independent of the other four and of one finite C1–C4 observation
> process, by qubit countermodels, and none implied by bare finite OI; which of them a physical
> substratum supplies is open), and selection of the evolution relating two times (open). A bounded
> application treats black-hole information recovery as a question about an observer's access
> class: in finite toy access models, global bijectivity neither implies nor is necessary for
> recovery from accessible records, and the Page entropy enters the framework's argument through a
> scrambling hypothesis, not through bijectivity.

The paragraph is adapted from AUDIT r4's surviving novelty statement (AUDIT:1983–2016) and narrowed
to the recommended scope. It omits the C8-R sentence, which belongs to Alt-X only.

**Black-hole sentence by scope (RC-2).** The paragraph's last sentence carries both §7-c and §7-h.
- **Recommended scope and Alt-L:** as drafted. It meets the R11 sites of §7-c and §7-h, which must
  be corrected first (decision 1(a)).
- **BH-01-conflict-free variant:** the sentence carries only §7-b, §7-h and §7-i. Replacement
  wording:

  > A bounded application treats black-hole information as a question about an observer's access:
  > the global reversible dynamics conserves information, the Page entropy enters the framework's
  > argument through a scrambling hypothesis, not through bijectivity, and the Page-time fraction
  > is conditional on the radiation's entropy per unit of horizon entropy lost, a constant
  > mass-loss coefficient and $S_{\mathrm{BH}}\propto M^2$.

  This still carries §7-h, and so meets ch07:126 s1 / FULL:2003 and GR:869.
- **If §7-h is also dropped** (decision 1(a), option (ii)): the sentence carries §7-b and §7-i
  only, and the clause on the scrambling hypothesis is removed.

The phrase "checked in Lean 4/Mathlib at a stated commit" stands where the earlier draft said
"machine-checked".
- **Evidence observed at `687e885b`.** The `Mathlib bridge` job of the push run on `main` passed.
  Its release-gate step `lean-axioms` reported every cited declaration within `propext`,
  `Classical.choice` and `Quot.sound`. Provenance: run `40291389159`, job `121467032075`, log
  sha256 `e20abaee…5251` (SOURCES-r4, "Kernel").
- **What a run is not.** A run id is not retention, and the log expires (§A.42).
- **Retention is required whatever the wording.** Any statement that the cited declarations are
  checked in Lean at a commit is an enduring certification claim under §A.42, and that holds for
  the sentence above as much as for "machine-checked".
  - Before the paper lands, an expected result for that commit is retained beside the paper. It
    records build success, the gate verdict and each cited declaration's `#print axioms` set, and
    names its recipe and provenance.
  - Alternatively, the commit is shown to fall inside an archive the `evidence-retention` step
    covers.
- **The owner's choice (decision 2) is only the word:** "machine-checked", or "checked in Lean
  4/Mathlib at commit X by recipe Y".
- **In either case** the paper names the commit and the recipe (`lake build` +
  `tools/lean_axiom_check.py`). It does not cite the run as evidence, and it lists the
  unformalized steps beside the claim (OUTLINE-r4 §8-d).

## (a) Contribution as exposition and perspective

1. **The hypothesis, stated with its status.** It is a hypothesis about nature. The physical
   identification is a representation choice, and no ontology-level falsifier is established
   (§1-a; Main:62, :702–704).
2. **One consolidated statement of the finite correspondence**, E1, at its proved scope: finite
   horizon, fixed basis, an initial law on $V\times H$, Markov laws included (§3-a to §3-h).
3. **Where the discriminating content lies**: hidden predictive memory (§4-a, §4-b) and
   recurrence indivisibility (§5-c, §5-e), with the scope limits set by the XOR family (§5-f) and
   the Hadamard family (§5-g).
4. **The boundary between reproduced behaviour and a derivation**:
   - representation is not explanation (§6-a);
   - the visible law does not select the relating evolution (§6-b);
   - operational QM is reached exactly under five named conditions that bare finite OI does not
     imply, independent on the qubit (§6-d);
   - no fixed finite carrier reproduces a qubit exactly (§6-e).
5. **A bounded black-hole application**, with every conditional step named (§7).
6. **An explicit list of open problems** (§8).
7. **An entry document.** As the short-form presentation that replaces the Explainer (owner decision,
   2026-10-26), the paper states its scope and points to Main and the Book for the rest of the
   programme. It inherits none of the Explainer's stale content (paper/explainer/REVIEW.md §3).
8. **The card-table illustration in corrected form** (§5-h): the swap game, its scope, and
   the re-burn rule on which the peek line depends.

## (b) Mathematical components stated with proof or kernel citation

| ID | Component | Correctness layer | Originality |
|---|---|---|---|
| §3-a | $S\iff D\iff Q_{\mathrm{fb}}$ at finite horizon (E1) | kernel, all six directions (`finite_horizon_equivalence`) | covered in kind: PARTLY KNOWN. The components are known; the packaging was not located (PROVISIONAL; comb-realization literature unread) |
| §3-b | S⇒D by one iterated bijection, with a correlated initial law | kernel (`S_imp_D`) | covered in kind: PARTLY KNOWN (EG Prop. 13) |
| §3-c | S⇒D with the hidden prior independent of $x_0$ | prose proof + exact probes; not formalized | covered in kind: PARTLY KNOWN (EG Prop. 16; LPW Prop. 1.5) |
| §3-d | D⇒$Q_{\mathrm{fb}}$ (the permutation unitary) | kernel | KNOWN (Barandes B25, B23, B26) |
| §3-e | $Q_{\mathrm{fb}}$⇒S | kernel | covered in kind: REFRAMING (Strasberg–García Díaz Eq. (3)) |
| §3-g | The Born form is internal; the exponent is not selected | prose + probe | KNOWN, non-discriminating (B26 Thm 3.1) |
| §4-a | Unavoidable hidden predictive memory, (a)–(c) | kernel for the joint law; the time-$t$ reading is not formalized | covered in kind: REFRAMING (DPI); attribution PROVISIONAL |
| §4-b | The memory biconditional, in prose with directions named | kernel components + prose; two links not formalized | covered in kind: REFRAMING |
| §4-c | Capacity bound $\log_2 m\ge I^*$ | kernel | covered in kind: REFRAMING; PROVISIONAL |
| §4-d | Readback lemma $I\ge p_0\delta^2/\ln2$ | prose proof (Pinsker) + exact probe | covered in kind: REFRAMING; PROVISIONAL |
| §4-e | (ii) ⟺ (iii), with (iii) corrected (F29), in prose only | prose proof, both directions; finite acceptance test | covered in kind: REFRAMING, near-definitional |
| §5-b | Minimal model: a non-stochastic $\Lambda(2,1)$ and a memory witness ($x_0$ law stated) | exact computation | unverified (illustration; not examined) |
| §5-c | A non-permutation step together with recurrence gives P-indivisibility | kernel (rooted form) + prose | KNOWN (RHP 2014 Thm 2.4; BD Prop. 1) |
| §5-e | The stochastic-inverse lemma; readback ⇒ indivisibility within the recurrence cycle | kernel (lemma; routed level); the history-level step is prose | KNOWN |
| §5-f | The XOR family: memory without short-window P-indivisibility | exact probe | KNOWN: up to flipping the final bit, RHP 2014 Eq. (15) |
| §5-g | Population P-indivisibility differs from quantum non-Markovianity outside the diagonal-preserving class | prose proof + exact probe | unverified (not examined) |
| §6-b | The visible law does not fix the relating evolution (two lifts with different relative candidates; constant deformations cancel; the quotient by visible equality) | kernel (`gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative`, `bridge_traj` and companions) | unverified (not examined) |
| §6-d | E2 (carrier-general). On the qubit, the independence of (i)–(v) from one another and from the sealed core; bare finite OI ⇏ QM (a qubit countermodel) | kernel | unverified (not examined in AUDIT r4) |
| §6-e | No fixed finite carrier reproduces a qubit exactly | prose (factorization) + the imported unbounded-rank result | covered in kind: REFRAMING (Hardy-type); PROVISIONAL |
| §7-c | Bijectivity does not deliver accessible recovery and is not needed for it; in a bijective instance zero advantage needs $\lvert K\rvert\ge\lvert M\rvert$ | written proof + exhaustive exact enumeration (finite toy access model); separate-agent internal review ACCEPT | unverified: not classified (C16-S; AUDIT r4 did not read the #917 records, AUDIT:1397–1398) |
| §7-d | Complete-access sufficiency; $P_{\mathrm{succ}}\ge1/\lvert K\rvert$ | written proof + exhaustive check; reviewed | covered in kind, per the package's own description of C2 and C4 (BH01 REPORT:110–112, :131–132); not literature-mapped |
| §7-e | Nested trace-out consistency is a Fubini identity | written proof + exhaustive check; reviewed | unverified |
| §7-f | GR A.7's stated decoupling support is reversed ($t_{\mathrm{evap}}/\tau_B^D \ge 1.785\times10^{57}$ at 30 $M_\odot$) | exact interval arithmetic; independently recomputed in review | not an originality item (an audit observation) |
| §7-g, §7-h | Permutations on configuration states create no entanglement; the Page value enters only through H-scramble | proofs + exhaustive exact sweeps; reviewed | unverified: not classified (no literature examined) |
| §7-i | The Page-time fraction $1-(\beta/(1+\beta))^{3/2}$, under its three conditions | exact algebra + literature | KNOWN (Page 2013 Eq. (8); Page 2005) |
| Alt-X: C8-R | The rooted families realizable by one finite permutation with a shared prior are exactly `PPer` | kernel (`finiteRootedRealizable_iff_pper`), finite visible only; uses zero-prior padding | **candidate**: NOVEL-CANDIDATE, novelty unverified. Sufficiency is PARTLY KNOWN (EG Props. 16–18); necessity is folklore. **No priority sentence.** It would be new manuscript content (AUDIT:938–946) |

## (c) Explicit non-claims

The paper states these in its own voice.

1. **No derivation of quantum mechanics.** E1 is a representation equivalence that contains every
   finite law, Markov laws included. The Born dictionary is part of the definition of
   $Q_{\mathrm{fb}}$, and its exponent is not selected (Main:534).
2. **No unique selection of the operational theory.**
   - Exact finite operational QM follows only under the five completion conditions.
   - Bare finite OI implies none of them (GR:220–222; Main:352, :562).
   - Their independence is shown on the qubit, against one sealed C1–C4 core (`five_way_minimality`).
   - Which of them a physical substratum supplies is open (GR:228).
   - The visible law does not fix the relating evolution (Main:624).
   - The paper does not cite GR:226's "OI-compatible + (i)–(v) ⟺ QM" box.
3. **No claim that the physical hypothesis is established or tested** (Main:704).
4. **No characterization of non-Markovianity by the existence of a realization.** That form is
   false (Main:596–598), and (ii) ⟺ (iii) is near-definitional (Main:608).
5. **No identification of stochastic P-indivisibility with quantum non-Markovianity** (Main:330,
   :334). No claim that (C4) forces indivisibility on short windows (Main:141).
6. **No black-hole overclaim.**
   - No resolution of the information paradox.
   - No derivation of the Page curve: only under H-scramble, which fails for bijections acting on
     configuration states.
   - No universal 0.646 Page time: it holds conditional on β = 1, a constant mass-loss coefficient
     and $S_{\mathrm{BH}}\propto M^2$.
   - No microscopic realization of islands (conjectural).
   - No proof of the generalized second law (open).
   - No decoupling of the trans-cosmological sector over the evaporation: its stated support is
     reversed (BH01 item F), with the three limits of what that shows.
   - Every black-hole computation is a finite toy model. Its reviews are separate-agent internal
     reviews, not external validation or owner adoption.
7. **No priority or novelty sentence.** None for C8-R. The XOR example is RHP 2014 Eq. (15) up to
   flipping the final bit, and nothing is said about who stated it first.
8. **No statement of the ≤ n³ compressed bound** (F13 unresolved).
9. **No conclusion rests on the ε-realization and gluing theorems,** and they are not described as
   proved unconditionally (F7; Main:580(4) has no kernel anchor).
10. **Main's descriptions of Calvo, Pimenta and Doukas, its [11]/[12] assignment, its
    Born-equilibrium sentence and its [24] are not carried** (F14–F19). Related work is written
    from the full-text studies.
11. **The "fixed autonomous generator" remark of Main:532 is not carried** (F3 open).
12. **Nothing is inherited from the Explainer's stale list** (paper/explainer/REVIEW.md §3, items 1–11).
13. **The card game is not presented as producing quantum rather than classical statistics.** On card
    inputs its statistics are classical stochastic ones; its one-step channel is entanglement-breaking,
    though its two-step map under the unitary embedding is not (Main:286, :702); and it violates no
    Bell inequality (ch01:286).
