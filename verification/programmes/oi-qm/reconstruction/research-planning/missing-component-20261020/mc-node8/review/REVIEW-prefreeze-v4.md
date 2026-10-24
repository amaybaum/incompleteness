# Node 8 preregistration: independent pre-freeze review, version 4

- File reviewed: `mc8/PREREG.md`, 1172 lines, sha256
  `e1c0994e9d24cc58475cb3c6d2202ee7b83a9e400ac355e335ab1c429f9bc32a` (re-verified). Line numbers refer to this file.
- Previous draft diffed: `.PREREG.rev3.md`, sha256 `86d06afd…` (re-verified); previous review `review/REVIEW-prefreeze.md`.
- Corpus: worktree `mc8w`, detached at `a501b418`, clean. Node records read under
  `verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/`.
- Nothing was computed under any candidate. Run: `quotecheck.py` (84 fragments, 0 failing, reproduced); `git`; text
  searches. Checked by hand: Lemma T, Lemma K, the two-rebit algebra, the D_R² + F_R² ≤ 1 proof and the saturation
  statement, the C5 ⇒ IC identity chain, K-PR6 / RAC algebra, K-OPSTATE.

## Verdict: REVISE

The file fixes the nineteen prior blockers (table below). Its mathematics is correct. The owner's Round 5 requirements
are present concretely: the frozen C5 wording with its three glosses, Lemma T and Lemma K with proofs, Q-PREP and
Q-FIN, the carrier/record distinction, Spekkens in both forms, the per-axiom audit with three typed verdicts, D1/D2
separate, the postdiction requirement, the R1–R4 scorecard, the H-X rule.

Seven changes block the freeze. The first is the important one: as §2.2 and §6.10 now stand, the first computation's
headline question, C5-P's R1 and D2 on finite carriers are all decidable by hand today, and the file frames them as
open. None of the seven requires a computation.

***

## Blocking changes

1. **Full κ2 access makes ℛ₁ and ℛ₂ classical, so §6.10's purification question is decided at freeze (l. 167–169,
   180–181, 499–511; also l. 400–403, 461–466).**
   - §2.2 defines 𝒫(V) as "the κ2 configuration bijections of Ω selected by visible settings, with ancilla cells".
     Condition O2 (MC7 PREREG l. 42–43) and node 3's κ2 (mc-node3/NODE.md:69–70, "bimeasurable bijections of C × X …
     any setting value selecting the bijection") place no restriction on which bijections a setting may select.
     ℛ₁ then says "𝒫(V) all κ2 bijections of Ω selectable by a visible setting" (l. 501–502).
   - Two-line argument. With every bijection of Ω accessible and a visible cell to read, the protocol x ^= h followed
     by readout returns the hidden prior exactly (K-OPSTATE is this protocol). So two preparations are operationally
     equivalent iff their hidden priors coincide: the operational state *is* the distribution on 𝒞_H, transformations
     are the induced stochastic maps, composites are distributions on the product. The operational theory of every such
     class is classical probability on the preparable priors. Its pure states are the extreme preparable priors; a pure
     state of any composite has point-mass or extreme marginals. Hence Pur-E fails for every preparable non-extreme
     prior (every denominator-≤ 8 prior other than δ₀, δ₁ in ℛ₁), in ℛ₁, in ℛ₂, and in every class with full access.
   - Consequences, all deducible now: §6.10's "whether Pur-E and Pur-U can hold there" has the answer no for Pur-E;
     C5-P's R1 (l. 400–403) holds for any such class that passes C1–C4; D2 (l. 461–466) is refuted on every finite
     carrier with a mixed preparable state, since no classical operational theory is "exactly QM's". A node that
     reports any of these as findings reports a corollary of its own interface definition. Under §16 the C5-P gem
     criterion is not met by them, but the R1 line and D2 would print as decided results.
   - Fix, one of:
     - (A) keep full access and write the argument above into §6.1 as a third lemma (pure mathematics, with K-OPSTATE
       as its instance), state its consequences for §6.10, R1 and D2 as expected shapes, and move the live C5-P content
       to Q-FIN (finite polytope versus continuum; Q_fb or a limit) and the audit; or
     - (B) restrict 𝒫(V) per realization class to a stated sub-class — protocol bijections act on visible cells and
       ancillas, hidden cells change only through the realization's fixed dynamics φ and its declared coupling steps
       (Substratum.md:44: visible operations write into the hidden sector "through the coupling") — and list the
       accessible bijections of ℛ₁ and ℛ₂ explicitly. Only under (B) can the state space across interventions be
       anything but a simplex, which is what the owner's first computation is meant to probe.
   - Either way: the fundamental step φ of ℛ₁ and ℛ₂ is not specified (O2 requires one). K-OPSTATE uses φ = id on x.
     State φ per class (identity, or enumerated), and add an I-row that each class's (Ω, φ, accessible bijections,
     ancilla states, priors, composites) is printed with digest before §6.10 runs (I-50 prints outputs, not inputs).
   - Also state whether ancilla cells are visible (point mass) or hidden (counting measure); both are used (l. 168,
     179–180, 199, 502) and the reversible set depends on it.

2. **"Pure", "mixture" and "the state set is convex over the preparable mixtures" are ambiguous, and Lemma K's
   hypothesis (i) and Q-PREP hinge on the reading (l. 179–181, 186–188, 347, 365–367).**
   - §2.2 defines mixing physically: "a hidden ancilla bit under the counting measure selecting between preparations"
     (weights 1/2, dyadic with more ancillas). The frozen wording says "pure means not obtainable as a nontrivial
     mixture of allowed states" (l. 347). But "Pure state" at l. 186 reads "not a nontrivial convex mixture of two
     distinct states", with no restriction on the weights.
   - These disagree on finite classes. In ℛ₁ the preparable priors have denominators ≤ 8. Under real weights, only δ₀
     and δ₁ are pure and the state set must be convex-closed, so Lemma K (i) holds and Pur-E fails by Lemma K in every
     class. Under preparable weights (ancilla mixing), the state set is finite, Lemma K (i) fails by construction, and
     which states are pure depends on which half-sums land in the set.
   - "The state set is convex over the preparable mixtures" (l. 181) does not say whether the set is the convex hull of
     the preparable states or the preparable states themselves.
   - Fix: define mixture as the physical operation (ancilla of stated size and prior; the weights it yields), define
     pure relative to that operation, state whether the state set is closed under real convex combination, and give
     the definitions a checkpoint (K-IF prints the preparable set and the pure set per class under the stated rule).
     Then say which reading Lemma K (i) and Q-PREP use.

3. **R1's witnesses: C1–C4 not required, one witness is at the wrong level, and the conclusion is pre-stated
   (l. 393–396, 400–403, 904).**
   - R1's definition is "an admissible C1–C4 model violating it" (l. 22). §6.2 lists CL, K-PR6 and the fiber-freedom
     realizations and says "R1 holds iff some witness is exhibited exactly", without requiring the witness to pass
     K-C1C4. CL as defined ("no hidden coupling beyond mixing", l. 450) fails C1 (Main.md:74) and is not a C1–C4 model;
     exhibiting Pur-E's failure on it does not establish R1. Require: R1 holds iff some witness that passes K-C1C4 on
     the interface violates Pur-E or Pur-U, with the K-C1C4 printout named in the R1 cell (l. 904).
   - `fiber_freedom` (Main.md:600) is non-uniqueness of *completions* at the substratum level. Pur-U is a statement
     about pure operational states of a composite and available reversible operations on the purifier. The file's own
     carrier/record rule (l. 182–185) and Main.md:602 ("an ingredient, not the axiom") say these are different levels.
     Either translate the witness onto §2.2's interface (two pure states of AB, equal marginal, no available reversible
     on B relating them) or drop it from the witness list.
   - l. 393–396 concludes "So C5-P is an added condition in OI, as the owner intends." The corpus shows the axiom is not
     *supplied* by the corpus (V-14); it does not show C1–C4 do not imply it. That is R1, which §6.2 measures. Write
     "not supplied by the corpus; independence is R1 (§6.2)".

4. **SPK-orig's two-toy-bit state set is defined by literature from memory (l. 447).**
   - The one-toy-bit construction is fully written. For two toy bits the valid states are "the knowledge-balance subsets
     of size 4 and the allowed coarser ones, as [L: Spekkens 2007] defines them". That leaves the state set, and hence
     the transformation set ("knowledge-balance-preserving permutations"), to be fixed at execution from memory of a
     paper not read. The owner's rule bars quoting as if from a paper; PC-SPK gates only the literature *claims*
     (l. 488–489), not the construction.
   - Fix: write the rule this node adopts (which subsets of the 16-point ontic space of sizes 4, 8, 16 are valid, as a
     stated combinatorial condition; the transformations as the permutations preserving that family; the measurements
     as the stated partitions), tag it as this node's reading, and route any discrepancy with the paper through
     PC-SPK as an amendment before the SPK verdict is final. SPK-conv is then determined by it.

5. **The QM positive control's finite instance is not fixed, and a wrong instance voids §6 (l. 453, 943, 942,
   1145).**
   - "States, unitaries and projective readouts of a qubit, exact in ℚ(√2)" and "computed on the finite instance" name
     no state set, no unitary set and no purifier. Pur-E for a qubit state with eigenvalue p needs √p: p = 1/2, 1/4 lie
     in ℚ(√2), p = 1/3 does not. An instance containing ω_{1/3} fails Pur-E for field reasons, the must-hold control
     fails, and I-6 voids every §6 verdict. Conversely an instance containing only states whose purifications and
     connecting unitaries lie in ℚ(√2) passes.
   - Fix now: list the states (for example the six stabilizer states and the mixtures with dyadic eigenvalues), the
     unitaries (a stated finite group, with the purifier unitaries that Pur-U needs), the composite (two qubits) and
     the field, and state that the instance is closed under the operations the audit applies to it.
   - K-TRANS (l. 942, I-48) "unitaries on the Bloch sphere instance" has the same gap. K-TRANS also tests only the
     lemma's conclusion; it should check the hypothesis (Pur-U holds on the control) and the conclusion (transitivity),
     so that it tests Lemma T rather than a known fact about CL and the qubit.

6. **PC-CDP: §6.8 contradicts itself, and a provisional audit row can still feed Emergence (l. 485–487, 880–882,
   893–898, 1035–1036).**
   - l. 485 says no axiom audit prints a verdict before the amendment exists; l. 487 says the audit prints "provisional,
     pending PC-CDP" until then. One of these holds.
   - `arxiv.org` was unreachable at drafting (l. 82), so PC-CDP may stay unmet through the node. §13.1 gives Emergence
     to "an audit row 'supplied by OI'" with no mention of the gate; §13.1's Parked clause names "an unmet amendment
     gate" but the precedence rule (l. 893) applies Parked only when the undecided item prevents a decision, and the
     classifier is not told that a provisional row prevents one. A derivation of this node's paraphrase of Causality is
     not a derivation of CDP's axiom unless the paraphrase is checked.
   - Fix: a row whose PC gate is unmet classifies Parked (provisional) and can yield neither "supplied by OI" final nor
     Emergence; add the I-row and a mutant (a provisional "supplied" row printing Emergence is caught). The same
     applies to a "compatible-but-added" C6… label, which names an axiom whose wording is unconfirmed.

7. **§7.5 rows 4 and 5 still name no §13 class (l. 612–613; prior item 4(f)).**
   - Row 4's class column reads "the R1 witness …"; row 5's reads "… R1 then fails". §13.1 maps R1–R4 to classes, so
     the mapping exists, but I-36's "one unit test per row" cannot be written against a column that names no class.
   - Write: row 4 → "Conditional for the C5-IC line (R1 holds), provided R2 and R4 hold; the correlation lines read
     Conditional on C5-IC"; row 5 → "Failure for the C5-IC line (R1 fails); the IC derivation line becomes eligible
     for Emergence on 𝔇 after D-1 to D-7 and the circularity review".

***

## The nineteen prior items, verified at the cited lines

| # | prior item | status | where |
|---|---|---|---|
| 1 | saturation sentence wrong | fixed; sufficient-not-necessary stated with the I/2 counterexample | l. 682–686 |
| 2 | (I9) from (I1) alone; composite identifications; (I5) discarding; conditional (I5) | fixed: (I9) cites (I1) and (I2) with the instance; (I10) added; (I5) includes discarding; conditional form dropped | l. 536–543 |
| 3 | IC-D4 omits input independence | fixed: B-2, D-1, P8 (iv), O3 | l. 739 |
| 4 | H-C5 table incomplete, precedence | (a)–(e), (g), (h) fixed; (f) half-done, see blocker 7 | l. 607–620, 893, 1133 |
| 5 | 𝔇 chosen at execution | fixed: 𝔇_min, exclusion typed, D-1 to D-7 before "IC derived", non-gem, interface frozen, I-46 | l. 573–577, 1143 |
| 6 | "PR: yes" unconditional | fixed | l. 621 |
| 7 | B and slices | fixed: B_{t₀} excludes inputs; one t₁; mode (i) at C5-S1; K-PR6-C5's B fixed; I-45 | l. 204–210, 556, 602, 1142 |
| 8 | preparer cells and wings | fixed | l. 201–203, 278–281 |
| 9 | K-PROG variants, admission semantics | fixed: PROG-0/B/3/c; PROG-c must be rejected; marker-responsiveness discriminator; "admits" defined | l. 293–309 |
| 10 | V depends on K; field | fixed: V := V₁₂ with θ₀ ∈ Θ₁₂; V_K sensitivity rows; ℚ(√2, √3) | l. 666–668 |
| 11 | 𝒟_IF undefined; fringe-law controls dropped | fixed: 𝒟_IF-RT, 𝒟_IF-HM; K-FL+, K-FL−; P19 gone from file and checker | l. 674–676, 705–707 |
| 12 | K-ERASE, CC-w, K-I2, K-VD unfixed | fixed | l. 697–699, 704, 708–709, 950 |
| 13 | missing tools skip; K-LEM gate; seed | fixed: I-37, I-42, exact rational instance | l. 82–84, 659–661, 927–928 |
| 14 | mutants without cases, before controls | fixed: every KM names a case; run after the section's controls; `mutant_verdict.py` manner | l. 965–997, 1157–1163 |
| 15 | P21 overstated | fixed: single-law form; R-pq typed A | l. 242, 587–590 |
| 16 | (b5-C5) completion; (b4) gate; 3√3 | fixed: PC-PW declares a completion typed A; PC-CSS; in-house SOS | l. 832–841 |
| 17 | productivity test | fixed: baseline extended; K-PR6 gem requires branch (a) and K-Q, K-C; P8 (ii)–(iii) marked | l. 230, 1044–1061 |
| 18 | H-X rule | fixed | l. 916–921 |
| 19 | circularity classes; I-23 exceptions; checkpoints | fixed: items 21–22 leave the step unclosed; I-23 lists the routes; I-45, I-46, I-47, I-39 | l. 1003–1005, 1120, 1136, 1142–1144 |

Prior notes also taken up: K-10 recorded (l. 85–87, 960); feasibility (l. 273–274); Spekkens control (l. 447–448);
equiprobable paths verified operationally (l. 654); (ii-Q) by the quantum-IC theorem stated in verdict text (l. 730);
appendix-c:226 cited (l. 479–480); the narrower MC7 NODE.md:42 quote (l. 95–96); stale checker fragments removed (84,
synchronized: every [Q] in the file has a checker entry and the checker has no entry the file does not quote).

## Owner's Round 5 requirements

| requirement | status | where |
|---|---|---|
| C5 independent, not derived; violating model a positive finding | met | l. 10–14 |
| governing question | met | l. 10–12 |
| R1–R4 as stated; R2 failure = Reproduction | met | l. 21–27, 883 |
| C5-P primary with owner's wording and three glosses | met, verbatim | l. 343–347 |
| C5-IC secondary; node 5 reference row failing R2 | met | §7, §8 |
| CDP's five axioms audited one by one, three verdicts, C6, C7… never hidden in C5 | met in form; see blocker 6 for the gate | l. 325–329, 426–440, 1141 |
| Main.md:630 on local tomography | quoted correctly; X-4 row | l. 121, 431 |
| real-amplitude control | met; algebra correct (below); its purification half is [L], see note 1 | l. 446 |
| D1/D2 separate (§A.34); D2 not the response-table construction | met | l. 36–40, 457–467 |
| classification: Conditional for new axiom; top target; Emergence only if derived; Parked only when it prevents a decision | met | l. 874–898 |
| postdiction requirement | met | §12 |
| owner finding (1) operational state across interventions with the display-0 control | met: K-OPSTATE correct | l. 172–181, 449 |
| owner finding (2) Lemma T with proof and limits | met; proof correct | l. 355–363 |
| owner finding (3) Lemma K with escapes, Q-PREP, Q-FIN | met; proof correct; see blocker 2 for hypothesis (i) | l. 365–388 |
| carrier/record | met | l. 182–185 |
| Spekkens, both forms | present; see blocker 4 | l. 447–448 |
| first computation: state space across interventions, exact | present; see blocker 1 | §6.10 |
| K-PR6 and RAC mandatory with rejecting premise; K-PROG; (a)/(b)/(b-corr); A1/A2; IC and ML own derivations; mutants after controls; exactness; literature tagged and gated | met | §4, §10, §11, §14, §1 |

## Mathematics checked by hand

- **Lemma T (l. 355–363)** is correct given the trivial system I with IA ≅ A (F-3). Discarding A sends every state to
  I's one state, so any pure ψ of A purifies it with purifier A; Pur-U gives U on A with Uψ = ψ′. The stated limits are
  right: permutations act transitively on the vertices of a simplex, so transitivity alone fixes neither the pure-state
  set nor the operation set. The interface (§2.2) does not define the trivial system; see note 3.
- **Lemma K (l. 365–371)** is correct. p ↦ ω_p is injective because the distinguishing measurement's outcome
  probability is affine in p (this uses F-2 / the mixture definition; say so). A countable union of finite sets is
  countable; Pur-E would inject [0, 1] into it. The polytope bullet is right: an affine image of a simplex has finitely
  many extreme points. Q-FIN's "finite reversible group acting transitively on the vertices" is right: an affine
  automorphism of a full-dimensional polytope permutes its vertices and is determined by that permutation.
- **Two-rebit control (l. 446).** ρ± = (I⊗I ± Y⊗Y)/4. Y⊗Y is real symmetric with eigenvalues ±1, each of multiplicity
  2, so ρ± are real, PSD with spectrum {1/2, 1/2, 0, 0}, trace 1. For P, Q ∈ {I, X, Z}: tr(ρ± P⊗Q) = (tr P tr Q ±
  tr(YP) tr(YQ))/4, and tr(YP) = 0 for all three, so ρ+ and ρ− agree on the span of {I, X, Z}⊗{I, X, Z}, which contains
  every product effect of real QT. tr(ρ± Y⊗Y) = ±1 separates them. Correct. (The §14 row's "9 product effects" should
  read "the 9 product Pauli operators spanning the product effects"; X is not an effect.)
- **D_R² + F_R² ≤ 1 (l. 657–659)** is correct: Σ(s − t)² = 2 − 2F, Σ(s + t)² = 2 + 2F.
- **Saturation (l. 682–686)** is now correct: for a pure balanced path–marker state the coherence term is ⟨m₀|m₁⟩ and
  V = F_q; the uncoupled I/2 marker gives V = F_q = 1 with a mixed marker. V ≤ F_q by positivity of the joint state.
- **C5 ⇒ IC chain (l. 554–562).** S2: 𝓘(X_i : BM | X_<i) = 𝓘(X_i : BM X_<i) − 𝓘(X_i : X_<i) [I1] = 𝓘(X_i : BM X_<i)
  [I8, D-1] ≥ 𝓘(X_i : BM) [I5 discarding], with (I10) for the regrouping. S4: [I1], then [I2] with (A, B, C) =
  (X, M, B_{t₁}), then [I4], [I7]. S3c is (I1). All premises now cited correctly.
- **K-PR6 / RAC (l. 278–283)** unchanged and correct; K-OPSTATE (l. 449) correct; CC-dec (l. 702–703) correct.

## Corpus spot-checks (§A.19, review point 7)

Read in full, not only string-matched, at `a501b418`: Main.md:20, :56, :60, :62, :72, :74, :76, :78, :80, :82, :352,
:356, :358, :361–365, :392, :405, :407, :560, :568, :578, :600, :602, :604, :630, :666; appendix-c:226–232;
GR.md:216, :250–258; mc-node5/NODE.md:28–36, :263, :344–346; mc-node3/NODE.md:66–73, :232–233; mc-node4/NODE.md:263–272;
mc-node7/NODE.md:38–50, :82, :104–111; MC7 PREREG l. 35–56, 60–70, 242–247, 654–672; MC7 AMENDMENTS A-2; PLAN.md:121–122;
Substratum.md:44, :92; Computation.md:130; SM.md:156; Methodology.md:393; Structure.md:1312; Explainer.md:566;
FiniteEntropy.lean:383–385, :457–459; C3Necessity.lean:80.

- Every quoted fragment is verbatim and its use matches the source's meaning. In particular: Main.md:630 supports V-10
  and X-4 as used; Main.md:560 supports V-8 and K-PROG; Main.md:600–602 support P21 and V-14 in the narrowed single-law
  form; Main.md:80 supports V-6 and the state/record distinction; Main.md:60 supports the prior as a realization datum;
  Main.md:356 and :407 are quoted as baseline, not strengthened; Main.md:578 supports "statistics only" for D2.
- **Node 5's condition.** mc-node5/NODE.md:28–29 is quoted exactly. GR.md:216 defines the operational theory as
  "finite outcome families of linear maps" with (iv) "every finite unitary on every composite is available", and
  GR.md:250–258 states phase-free richness through the special-unitary Lie algebra. The owner's summary, "already
  describes operations with complex matrices", matches the record. The R2 verdict fixed in advance (l. 640–643) is
  supported.
- **Node 7's K-10.** NODE.md:82 and :110 say "provisional on K-10 at n = 4" and "n = 4 pending (CI)"; AMENDMENTS A-2
  matches. The CI confirmation is owner-reported (run 39529498293) and so tagged (l. 86, 960); nothing in the worktree
  records it. Fine as stated, since no clause depends on it.
- l. 95 cites "MC7 NODE.md:42" for a fragment spanning lines 42–43; cite 42–43.
- The §A.19 search statement (l. 256–260) is accurate: purification hits are Main.md:352, :600–602 and the node
  records; tomography hits Main.md:352, :630.

## Circularity (review point 6)

- No route uses Hilbert-space structure, amplitudes, Q, Q1, Tsirelson or a measure defined to have the tested
  properties as a premise. ℓ²(Ω) of P18 is admitted as built from the substratum and V-K is judged on whether u_x can
  depend on x alone (l. 816–817). VR and Q1 appear as characterizations of the admitted set's target, not as premises.
  RQ, QM, CC-q, K-Q are controls and so labelled.
- The interface (§2.2) imports no quantum structure. Checklist item 1 covers it.
- K-I2 is a mutant measure, correctly flagged as failing (C5c).

## §A.41 and gates (review point 8)

- Every gate prints "not run (precondition unmet)" and reads only from a digest-printed amendment (I-28). PC-SPK and
  PC-CS block exactly the literature uses; PC-PW, PC-GM, PC-CSS block their test points. PC-CDP: see blocker 6.
- Properties asserted without a checkpoint: the inputs of each §6.10 class (blocker 1); the state-set convexity rule
  (blocker 2); the C1–C4 status of R1 witnesses (blocker 3); the QM instance's closure (blocker 5); the provisional
  status of audit rows (blocker 6). Everything else in the table has a measuring checkpoint, and I-17 now tests the
  "prevents a decision" qualifier.

## Register (review point 9)

- All-caps tokens are identifiers only (PROG, NODE, CHSH, PREP, OPSTATE, PREREG, ERASE, TRANS, PLAN, REVIEW, POVM,
  IEEE, FULL, AMENDMENTS); "NOT" occurs only inside a [Q] fragment.
- Route names are neutral (R-ont, R-acc, R-pq, R-ms).
- Claims stronger than their evidence: l. 393–396 (blocker 3); l. 446's "satisfying purification" rests on [L] while
  the sentence reads as a computed result (note 1). No revision-history or meta-commentary phrases.
- l. 864 still says "additional-consequence requirement unmet" where §12 renamed it the postdiction requirement.

***

## Notes (non-blocking)

1. **RQ's purification half.** Both ρ± are rank-2 real symmetric with eigenvalues 1/2, so each has a real purification
   on a third rebit, and any two are related by a real orthogonal map on the purifier. This is a finite exact check;
   compute it in house rather than resting the §16 gem clause ("the SPK or RQ control decides which axiom purification
   alone leaves open") on [L].
2. **SPK-conv is decided by Lemma K.** Its hypotheses (i)–(iii) all hold on the convex closure, so "Pur-E fails" is a
   theorem, not a measurement. Say so, and let the measurement confirm the lemma's instance (I-51 already prints the
   hypotheses).
3. **The trivial system.** Lemma T assumes it; §2.2 does not define it. Add "the trivial system is the empty visible
   register with one configuration; discarding every cell is the operation to it".
4. **Lemma K (i)** uses that measurement statistics are affine in the mixing weight; cite F-2 or the mixture
   definition in the proof.
5. **The equivalence domain.** §13.1's top target is "on a declared domain"; nothing fixes when it is declared. Tie it
   to D2's scope (fixed finite carrier, finite horizon; or Q_fb / a limit after Q-FIN) and declare it before step 3,
   with an I-row like I-46.
6. **K-OPSTATE's realization fails C1** (zero coupling under the passive dynamics). It is a control for the state
   definition, not a C1–C4 model; say so where it is called an ℛ₁ instance (l. 509).
7. **D2's test as "node 5's G6 rule"** can only refute. The establishing route is the isomorphism construction; the
   sentence should not suggest G6 can establish D2.
8. **Expectations.** "which is not expected and not attempted" (l. 460) and the "expected shape" columns are disclosed
   as non-verdicts, consistent with §A.29. After blocker 1 is resolved, the expected shapes for §6.10, R1 and D2 should
   be stated or the classes changed so that they are open.
9. **K-PR6's C5-P line** will read "rejected only by the added axiom C5-P" for the same reason C5-P rejects every
   classical realization (under full access). Add to §4.2's "rejected only by the added axiom A" the datum "A admits
   K-C's realization: yes/no", so a vacuous rejection is visible; Q-FIN then carries the consequence.
10. **Bibliographic data** in §17 are consistent with my knowledge (CDP PRA 84 012311; Spekkens PRA 75 032110; Barnum
    et al. NJP 12 033024; Al-Safi–Short PRA 84 042323; Short–Wehner NJP 12 033023; DiVincenzo et al. PRL 92 067902;
    Pawłowski et al. Nature 461 1101; Fuchs–van de Graaf IEEE TIT 45 1216; Oppenheim–Wehner Science 330 1072;
    Jaeger–Shimony–Vaidman PRA 51 54; Greenberger–Yasin PLA 128 391; Englert PRL 77 2154). The arXiv identifiers tagged
    [L-c] remain unverifiable here.
