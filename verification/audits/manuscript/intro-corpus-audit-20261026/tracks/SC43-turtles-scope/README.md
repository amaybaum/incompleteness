# SC-43: the scope of the "turtles all the way down" argument

Base `main` at `0d917665`; branch `corpus/sc43-turtles-scope`. There are three commits:
1. the unit's corrections (`896c7ee5`);
2. the independent review's revisions (`04639b2f`; B1–B6, O1–O9; verdict REVISE);
3. the second review's items 1–5 (verdict ACCEPT WITH CHANGES).

Line numbers are at the base. The book chapters and the `FULL.md` mirror were edited identically:
ch03:N is FULL:N+876 in §3.6–§3.8, ch02:44 is FULL:687, and ch19:200 is FULL:5360.

## Finding

This unit is owner-defined (2026-10-28). It has no CON or R id in `FINDINGS.md` at `16fc745d` or in
the #918 consolidated audit at `9dc2b069`: neither file mentions the turtles section. The owner wants
r32's Introduction to give the argument after the card-game analogy. It must keep its
qualifications, and above all the conditional status of the gauge classification's completeness.

The source is ch03 §3.8, "Hawking's turtles and the regress of support" (ch03:218–:228,
FULL:1094–:1104). It said the framework "can prove" that the support question loses its reference,
that the regress "ends where the framework can prove there is nothing left for it to be about", and
that the framework has "a proof that below a certain depth the word *below* stops referring". What is
actually proved is narrower:

1. Adjoining deep-sector structure that evolves independently of the boundary layer leaves every
   observable unchanged. This is proved on paper.
2. "No observable difference, therefore no fact of the matter" is the framework's identification of
   gauge freedom with gauge incompleteness. ch03 §3.6 and Methodology §19 offer it as a proposal,
   not a theorem.
3. That the four generator families exhaust $\mathcal G_{\rm sub}$ is conditional. The argument
   offered for it is not established (below).

## Step 1: the status of each ingredient

| Ingredient | Authoritative statement | Status |
| --- | --- | --- |
| $\mathcal G_{\rm sub}$, definition | Substratum:249: "(S, φ) ∼ (S′, φ′) if the two systems produce identical emergent physics — the same transition probabilities $T_{ij}(t)$, the same emergent Hamiltonian (up to D-gauge), and the same ℏ — for all partitions of the same structural class … The set of transformations mapping (S, φ) to an equivalent (S′, φ′) is a group"; ch02:136 is the same. | A definition: all observables-preserving transformations. |
| Theorem 24, the four families lie in $\mathcal G_{\rm sub}$ (soundness) | Substratum:251–:261; ch02:140–:148; Structure:154, :205; Methodology:353. | Proved on paper. (ii) holds under the alphabet-size hypothesis; for the gauge sector, (iv) is restricted to cubic-structure-preserving isomorphisms. In Lean, only the hidden-conjugation part of (i) is kernel-checked at the level of the uniform-prior family (`familyAt_hiddenConjugate`, ST1′, `OIBridge/SemigroupTransfer.lean`). |
| Generator (iii), exact statement | Substratum:257: "Adjoining to $\mathcal C_D$ … additional degrees of freedom that no dynamics couples to $\mathcal C_V\times\mathcal C_B$ — so that the bijection on the enlarged space is $\varphi\times\varphi_{\rm new}$ … — leaves every $T_{ij}(t)$ unchanged at every $t$ … *(Scope.)* An enlargement whose dynamics couples to the boundary layer, even slowly … is not in this family: … $T_{ij}(t)=T^{(B)}_{ij}(t)+\mathcal O(t/\tau_B)$, so such an extension preserves the leading-order transition law $T^{(B)}$ on accessible timescales $t\ll\tau_B$, not the transition probabilities themselves." | The decoupled product case is proved on paper, by the elementary averaging at Substratum:261. The independent review confirmed the proof. Check A1 below confirms it exhaustively and exactly on the stated small instances. There is no Lean theorem: `enlarge` and `visibleBlock_enlarge` exist, but no family-invariance theorem does. The slow-coupling bound is a paper argument (GR:112–:132), and it is an upper bound only. |
| Completeness (the four families exhaust $\mathcal G_{\rm sub}$) | Substratum:271: "The four families exhaust $\mathcal G_{\rm sub}$ conditional on Lemma 24.1's semigroup-transfer step"; Substratum:283: "The framework asserts (2) … it does not here reproduce the GNS uniqueness proof, and (2) is the step to check"; Substratum:293: the completeness is "relative to the observable set $\{T_{ij}(t), H, \hbar\}$ and the substratum ontology of §2". | **Conditional; the argument offered for it is not established; neither proved nor refuted.** See the four points below the table. |
| The reconstruction theorem's equivalence-class form | Substratum:193 (Theorem 23); ch02:118. Under E1–E7, M1-T, M1-B, A1–A6, C2-mixing and "Lemma 24.1's semigroup-transfer/completeness step", the local propagating lattice/gauge residue is fixed "up to the stated substratum-gauge freedoms". ch02:122: "uniqueness is within the structural class A1–A6". | Conditional on the listed hypotheses, one of which is the completeness step. Bell-inclusive uniqueness is open. |
| The identification "gauge freedom = gauge incompleteness, no fact of the matter" | ch03:152: "treat it as a proposal the framework's structure invites rather than as a load-bearing result"; Methodology:459: "the least settled; … offered as a proposal for scrutiny". | A proposal, resting on an interpretive premise. It is not a theorem. |

The completeness row in detail:

- **ROADMAP.** `verification/ROADMAP.md`:64 lists P1 as "**OPEN** — the semigroup-transfer route is
  refuted on the tested readings (`ST2`–`ST4`); the obligation itself is untouched".
- **The kernel contradicts Lemma 24.1's stated conclusion.** In `OIBridge/SemigroupTransfer.lean`
  (level 2; census family "Substratum Lemma 24.1 — the semigroup-transfer step", kernel-only),
  `ST3_pairC` gives two six-state substrata. Both have trivial hidden commutant and the same family
  at every $t$, and no unitary whatsoever relates them. `ST4_pairC` shows that no conjugation of the
  form $P_\sigma\otimes W$ relates them either, after any decoupled enlargement.
- **Completeness itself is neither proved nor refuted.** The review's `pairc.py`, which I rerun,
  shows that after enlargement of both sides by a transposition, Pair C is conjugate by a
  visible-fibre-preserving relabelling. That relabelling has a hidden part that depends on the
  visible value, so it is not of the form $P_\sigma\otimes W$. Pair C is therefore absorbed by
  (i)+(iii) under the literal fixed-partition reading of (i). The review further reports that under
  the all-partitions reading of the definition at Substratum:249, Pair C is not an equivalent pair
  at all.
- **Exhaustive evidence on small carriers.** The review's `tvspath3.py`, which I rerun, enumerates
  every permutation on carriers with $(|V|,|H|)\in\{(2,2),(2,3),(3,2)\}$. On these, equal $T$ at
  every $t$ implies equal visible path statistics up to visible relabelling: 0 classes split.
- **Further rounds.** 24.1A (`WordTraceSufficiency`) proves that word-trace equality is sufficient
  on the spanning class only. 24.1B and 24.1C are frozen control planes with no result.

## Step 2: the claims corrected (per claim)

Edits are identical in ch03 and FULL, and the "Now" text is what stands at the head.

1. **ch03:220 / FULL:1096, "because it can prove that the question loses reference before it needs
   an answer".**
   - **Defect.** What is proved is invariance under generator (iii). The loss of reference rests on
     the §3.6 identification, which is a proposal.
   - **Correction.** "What it offers instead is a criterion for when the question has lost its
     reference, an exact result for one class of candidate answers, and a conditional result for the
     rest."
2. **ch03:220, the two-way dichotomy "Either it is more structure … or it is deep-sector content".**
   - **Defect.** The dichotomy was presented as exhaustive. It leaves out slowly coupled structure,
     which is not gauge. It also leaves out structure outside A1–A6 or outside the dilation-datum
     ontology, which the completeness scope excludes (Substratum:293).
   - **Correction.** The dichotomy becomes three cases, and the third case is stated as one about
     which the classification says nothing.
3. **ch03:220, "it ends at a line the framework can state exactly, … physical if and only if it is
   an *invariant of the gauge class* … and it is gauge exactly when the group's generators move it".**
   - **Defect.** The displayed biconditional ran in two directions (§A.34):
     - "the generators move it, so it is gauge" is soundness, which is proved;
     - "it is gauge, so the four generators move it" needs completeness, which is not established.

     The physical/invariant criterion is the framework's structural-realist criterion, not a
     theorem.
   - **Correction (review B1).** "…physical, on the framework's structural realism, when it is an
     invariant … and gauge when some observables-preserving transformation moves it. The criterion
     can be applied exactly only as far as $\mathcal G_{\rm sub}$ is known explicitly, and the four
     generator families are not known to exhaust it: their completeness is conditional, and the
     argument offered for it (Substratum §4, through its semigroup-transfer step) is not
     established; a transformation that preserves every observable and lies outside the four
     families has not been excluded." The parenthesis gives the owner's clause, which names "the
     semigroup-transfer completeness step", an antecedent inside the section.
4. **ch03:220, "Below that line the sortal *turtle* stops being well-formed, and asking … becomes —
   precisely, not loosely — the analogue …".**
   - **Defect.** The sentence stated the conclusion without its premise.
   - **Correction (with review O3).** "Below that interface, on the framework's identification of
     gauge freedom with gauge incompleteness, …". The words "precisely, not loosely" are removed.
     The owner-designated clause ("here the $\mathcal G_{\rm sub}$ invariants do, conditional on the
     semigroup-transfer completeness step (that exhaustion is what the reconstruction theorem's
     equivalence-class form, read through §3.6's identification, conditionally asserts)") is kept
     verbatim.
5. **ch03:220, the simulation-hypothesis sentence.**
   - **Defect.**
     - "there is no physics question there to answer" rests on the identification.
     - "enters the transition probabilities at $\mathcal O(t/\tau_B)$" reads an upper bound as an
       effect that always occurs.
     - A simulation whose hardware is driven by the simulated state is a one-way-driven extension (a
       skew product), not the product extension of generator (iii). Probe A4 shows that such an
       extension leaves every transition probability unchanged and can change the coherences of
       the channel family $\Phi_t$.
     - At equal size, 48 of the 64 cases have a cycle type no product enlargement has. That
       obstruction disappears after a further decoupled enlargement: by A5, all 64 become conjugate
       to an enlarged $\varphi\times{\rm id}$ by a visible-fibre-preserving relabelling. That
       relabelling preserves every $T_{ij}(t)$, but by A6 it does not in general preserve $\Phi_t$
       (24 of 36 such relabellings of the A4 base change it).

     So whether the driven-hardware difference is gauge depends on whether the coherences count
     among the observables.
   - **Correction (review B2).** "…so on the framework's gauge bookkeeping the difference between
     them is gauge. Two cases fall outside it. Hardware whose state is driven by the simulated state
     without acting back on it leaves every transition probability unchanged, but it is not
     deep-sector enlargement and can change the coherences of the visible-sector quantum channels,
     so whether that difference is gauge depends on whether those coherences count among the
     observables; a difference coupled to the boundary layer, however slowly, can change the
     transition probabilities, by an amount the boundary-only dependence lemma bounds at order
     $t/\tau_B$ on accessible timescales."
6. **ch03:220, "the hidden sector's capacity, timescales, coupling structure, and energetic content
   are class invariants — every representative carries them, which is why they can be deduced"
   (review O2).**
   - **Correction.** "…which is why the first three can be deduced, and the fourth conditionally on
     the open matter-to-boundary coupling step ([GR §6.2])". This is SC-37's own descriptor and
     citation at its ch03:212 (head `e5684370`), so the phrase has an antecedent within SC-43's own
     text and the two units read consistently once merged. "G3" is not written here, because
     Structure uses "G3" for a gauge level. See cross-unit item C1.
7. **ch03:222 / FULL:1098, the closing two sentences only: "in the deep sector where enlargement is
   pure gauge … it ends where the framework can prove there is nothing left for it to be about".**
   - **Defect.** The sentences claimed a proof of the dissolution.
   - **Correction (with review O1).** "…where independently evolving enlargement leaves every
     observable unchanged, does *below* stop referring, on the framework's identification of gauge
     freedom with gauge incompleteness. … on that identification it ends where no observable is left
     for it to be about — a boundary the framework draws explicitly by its four generator families
     only conditionally on the completeness of its gauge classification."
   - **Not touched.** SC-37's sentences on the same line.
8. **ch03:226 / FULL:1102, "the gauge boundary is the framework proving where deduction runs out".**
   - **Correction.** "…locating where deduction runs out — exactly for independently evolving
     deep-sector structure, and for the rest conditionally on the completeness of its gauge
     classification —".
9. **ch03:228 / FULL:1104, "theorems for everything in between, and a proof that below a certain
   depth the word *below* stops referring".**
   - **Defect.**
     - What lies between the foundation and the gauge line includes conditional results and named
       hypotheses.
     - The "proof" covers invariance, not the loss of reference.
   - **Correction (with review O4).** "derivations for what lies between, each with its stated
     status — theorems, conditional results and named hypotheses — and, below a certain depth, a
     proof that independently evolving structure changes no observable, which the framework's
     identification of gauge with incompleteness reads as the point where the word *below* stops
     referring; that the boundary is drawn exactly by the four generator families is conditional on
     the completeness step."
10. **ch03:224 / FULL:1100.** Already conditional. **Unchanged.**

### Downstream sites (Step 3)

11. **ch03:208 / FULL:1084, "a completeness theorem conditional".**
    - **Correction.** "a completeness argument conditional on the semigroup-transfer step (Substratum
      Lemma 24.1)". This sentence keeps the corpus's stale form; see C3, class (ii).
12. **ch03:204 / FULL:1080, "The framework's claims are mathematical theorems rather than
    metaphysical doctrines."**
    - **Correction (with review O4).** "The framework's claims are stated mathematically, each with
      its status — theorem, conditional result or named hypothesis — rather than as metaphysical
      doctrines."
13. **ch03:142 / FULL:1018, "where there is, demonstrably, nothing of the matter to be had".**
    - **Correction (with review O7).** "where no observation, by any observer, could register the
      difference, and the framework's structural realism accordingly holds that there is nothing of
      the matter to be had. Hidden-sector relabelings, decoupled deep-sector enlargement and, …".
14. **ch03:152 / FULL:1028, "This identification is recent within the framework's development, …"
    (§A.30 self-narration).**
    - **Correction.** "The companion paper presents this identification as the least-settled of its
      contributions, a proposal for scrutiny; …".
15. **Methodology:459 (review O6).**
    - **Was.** "*This section is the most recent addition to the paper and the least settled;"
    - **Now.** "*This section is the least settled in the paper;"
16. **Methodology:467.** Three phrases are corrected.
    - "The exact extent of the hidden sector, the labels on substratum states" becomes "The size of a
      deep sector beyond the boundary layer that no dynamics couples to it, the labels on
      hidden-sector states".
    - "there is no truth there to reach, because a difference … is not a difference in fact" becomes
      "On the structural-realist premise adopted here, that a difference no observation could ever
      register is not a difference in fact, there is no hidden truth the observer is failing to
      reach."
    - "the name records the identification, which is a result and not a stipulation" becomes (with
      review O5) "Given that premise, this species of incompleteness *is* gauge freedom: the
      identification follows from the premise and the definition of $\mathcal{G}_{\text{sub}}$ as
      the observables-preserving transformations."
17. **Explainer:946.**
    - **Defect.** |C_D| was called gauge on the strength of leading-order agreement.
    - **Correction.**
      - The sentence is restricted to "a deep sector that no dynamics couples to the boundary layer".
      - It now reads "identical transition data at every time [Substratum §4, Theorem 24(iii)]".
      - The "no fact" step is attributed to the identification.
      - The coupled case is stated separately.
18. **Explainer:976 (review B5).**
    - **Was.** "This gauge group has four generators: … The reconstruction theorem establishes this
      list for the state-channel content via Stinespring uniqueness; …"
    - **Defect.** This is an unconditional completeness claim.
    - **Correction.** "This gauge group contains four families of generators: … That these exhaust
      the gauge group is conditional: the completeness argument for the state-channel content, via
      Stinespring uniqueness extended to the whole channel family [Substratum §4], is not
      established; the graph generator carries the cubic-structure qualification just noted."
19. **ch02:44 / FULL:687 (review B4, a missed site).**
    - **Was.** "The cardinality of the deep hidden sector beyond the partition boundary is *gauge* …
      Different deep-sector cardinalities — including infinite ones — produce the same visible
      transition data at leading order on accessible timescales … A gauge quantity has no answer to
      find, because the question is empty."
    - **Now.** "The cardinality of a deep hidden sector that no dynamics couples to the boundary
      layer is *gauge* rather than undecidable, and so is the alphabet size $q$ at each lattice site
      under the alphabet-size hypothesis of Chapter 5. Different cardinalities of such a sector —
      including infinite ones — produce identical visible transition data at every time (§2.5,
      generator (iii)); a deep sector coupled to the boundary layer, however slowly, is not covered,
      since the boundary-only dependence lemma of Chapter 7 guarantees only the leading-order law on
      accessible timescales. Under the hypothesis, different values of $q$ produce identical
      observables. … On the identification of Chapter 3 §3.6, a gauge quantity has no answer to
      find, because the question is empty."
20. **ch19:200 / FULL:5360 (same defect as 19, found in the round-2 re-grep).**
    - **Was.** "The deep hidden sector's cardinality is gauge in the framework."
    - **Now.** "The cardinality of a deep hidden sector that no dynamics couples to the boundary
      layer is gauge in the framework."
21. **Structure:53 (review O8).**
    - **Was.** "The hidden sector beyond the boundary layer admits arbitrary cardinality."
    - **Now.** "A deep sector that no dynamics couples to the boundary layer admits arbitrary
      cardinality."
22. **GR:136 (review O8), not applied.**
    - **Proposed.** Rename the title to "(deep-sector cardinality is unobservable at leading order)".
    - **Why not.** GR:136 is a canonical coverage statement, `GR:C-deep-sector-cardinality-gauge`
      (fingerprint `b0887eff73117a38`, GAP). The census derives the id from the title, so the rename
      moves the id (to `GR:C-deep-sector-cardinality-unobservable-at`). The unit brief requires the
      id to be kept, so I reverted the rename. The fingerprint is unchanged and `coverage_check`
      passes.
    - **What was done instead.** GR:142 carries the fix (item 23). The GR:136 title and statement are
      untouched, and the id and fingerprint are preserved. A rename together with a ledger id change
      remains an owner decision.
23. **GR:142, the leading-order overclaim (second review, item 3).**
    - **Was.** "The cardinality of the deep hidden sector is gauge in the scope of this corollary:
      two systems with the same … Exact invariance of every $T_{ij}(t)$, the gauge enlargement of
      [Substratum §4], Theorem 24(iii), holds for a deep sector that no dynamics couples to the
      boundary layer."
    - **Now.** "In the sense of $\mathcal{G}_{\rm sub}$, which requires exact invariance, the
      cardinality of the deep hidden sector is gauge when no dynamics couples the deep sector to the
      boundary layer ([Substratum §4], Theorem 24(iii)); the corollary's sense is leading-order: two
      systems with the same …". The later sentence, now redundant, is deleted.
    - **Coverage.** `coverage_check` passes with `GR:C-deep-sector-cardinality-gauge` at fingerprint
      `b0887eff73117a38` unchanged. GR:142 is commentary after the proof, not part of the
      fingerprinted statement.
    - **Mirrors.** None: no book site restates GR:142.
    - **Overlap.** SC-37's GR hunks at its head `e5684370` are at GR:26–:30, :326–:374, :404–:468,
      :490, :526, :545, :573–:575, :597, :625, :637 and :707. None touches GR:142.

## Site table

| Site | Was | Now | Source |
| --- | --- | --- | --- |
| ch03:142, FULL:1018 | "demonstrably"; "the deep-sector enlargement" | no observable registers it; structural realism; "decoupled deep-sector enlargement" | ch03:152; Methodology:459 |
| ch03:152, FULL:1028 | "This identification is recent …" | "presents … as the least-settled …, a proposal" | §A.30 |
| ch03:204, FULL:1080 | "mathematical theorems" | "stated mathematically, each with its status" | status labels |
| ch03:208, FULL:1084 | "completeness theorem" | "completeness argument" | Substratum:271 |
| ch03:220, FULL:1096 | "can prove …", dichotomy, exact line, iff, "precisely", simulation, "enters … at", energetic content deduced | three cases; criterion; completeness "not known … not established"; identification named; driven hardware and coherences; bound; fourth invariant conditional on the matter-to-boundary coupling step; "through its semigroup-transfer step"; "Below that interface" | Substratum:257, :261, :271, :293; GR:112; ch03:152; A4–A6; ROADMAP:64 |
| ch03:222, FULL:1098 (last two sentences) | "pure gauge"; "can prove there is nothing left" | observables unchanged, on the identification; boundary conditional | as above |
| ch03:226, FULL:1102 | "proving where deduction runs out" | "locating …" | as above |
| ch03:228, FULL:1104 | "theorems for everything in between …" | derivations with status; invariance proof, read through identification | as above |
| ch02:44, FULL:687 | gauge cardinality at leading order | decoupled sector, exact; coupled not covered; identification named | Substratum:257 |
| ch19:200, FULL:5360 | "deep hidden sector's cardinality is gauge" | decoupled sector | Substratum:257 |
| Methodology:459 | "most recent addition … least settled" | "least settled in the paper" | §A.30 |
| Methodology:467 | hidden-sector extent; "because …"; "a result and not a stipulation" | decoupled deep-sector size; premise; follows from premise and definition | Substratum:249, :257 |
| Explainer:946 | \|C_D\| gauge at leading order | decoupled, exact; coupled separate | Substratum:257 |
| Explainer:976 | "has four generators … establishes this list" | "contains four families …; exhaustion conditional, argument not established" | Substratum:271, :283; ROADMAP:64 |
| Structure:53 | "The hidden sector beyond the boundary layer admits arbitrary cardinality" | "A deep sector that no dynamics couples to the boundary layer admits arbitrary cardinality" | Substratum:257 |
| GR:142 | "is gauge in the scope of this corollary"; separate exact-invariance sentence | gauge in the $\mathcal G_{\rm sub}$ sense only when decoupled; the corollary's sense is leading-order; redundant sentence deleted | Substratum:257; GR:136 (id and fingerprint unchanged) |

## Evidence level of each corrected claim

- **Invariance under decoupled deep-sector enlargement.**
  - **Level.** Proved on paper (Substratum:261, elementary; confirmed by the review). It is also
    exhaustive and exact on small instances (A1).
  - **Not Lean.**
- **Slow coupling.** A paper argument (GR:112–:132), and an upper bound $\mathcal O(t/\tau_B)$.
- **Completeness of the four families.**
  - **Level.** Conditional; the argument offered for it is not established; neither proved nor
    refuted. Lemma 24.1's stated conclusion is contradicted in the kernel (ST3, ST4).
  - **Pair C.** It is absorbed by a visible-fibre-preserving relabelling after enlargement under the
    fixed-partition reading (review, `pairc.py`).
- **"No fact of the matter" and "below stops referring".** These rest on the identification, a
  proposal. Beyond decoupled enlargement, they are also conditional on completeness.
- **Driven hardware (A4–A6).** Exhaustive and exact on one stated finite instance (a toy carrier):
  - every transition probability is preserved;
  - the channel-family coherences can change;
  - after a further decoupled enlargement, every case is related to $\varphi\times{\rm id}$ by a
    visible-fibre-preserving relabelling, and such relabellings preserve $T$ but not, in general,
    $\Phi_t$.

  These are witnesses, not theorems.

## Claims removed or made conditional

- **Removed.**
  - "can prove that the question loses reference";
  - "ends at a line the framework can state exactly";
  - "precisely, not loosely";
  - "it ends where the framework can prove there is nothing left for it to be about";
  - "theorems for everything in between";
  - "a proof that below a certain depth the word *below* stops referring";
  - "the gauge boundary is the framework proving where deduction runs out";
  - "demonstrably";
  - "a result and not a stipulation";
  - the leading-order gauge claim for |C_D| (Explainer:946, ch02:44, ch19:200, Structure:53);
  - the unconditional "establishes this list" (Explainer:976).
- **Made conditional on the identification.** The loss of reference, "no fact of the matter", the
  simulation-hypothesis dissolution (independently evolving hardware only), and the ending of the
  regress.
- **Stated as not established.** That the four families exhaust $\mathcal G_{\rm sub}$ (ch03:220,
  Explainer:976). The owner's clause "the $\mathcal G_{\rm sub}$ invariants do, conditional on the
  semigroup-transfer completeness step" is kept verbatim.
- **Made conditional on the coupling step.** That the hidden sector's energetic content can be
  deduced (ch03:220).
- **Kept as proved.** Decoupled deep-sector enlargement leaves every observable unchanged at every
  time.

## Checks

- **The check script.** `check_turtles.py` is run as `python3 -I check_turtles.py <repo-root>`, and
  its output is `check.out`. Part A is exact (integers and `Fraction`) and periodic in $t$, so it
  covers every $t$.
  - A1, control: 8 product enlargements leave $T_t$ and $\Phi_t$ unchanged.
  - A2, control: a replay of Pair C. The family is equal at every $t$; the fixed-point counts are 2
    and 0.
  - A3, countercontrol: a two-way coupled extension changes $T_t$. The check fires.
  - A4: 64 of 64 one-way-driven extensions preserve $T_t$. 48 have a cycle type of no equal-size
    product $\varphi\times\varphi_{\rm new}$, and the same 48 change some $\Phi_t$ entry.
  - A5 independently verifies the review's reachability claim. Cycles are grouped by the set of
    rotations of their visible word, unlike the review's minimal-rotation canonical form.
    - 16 of 64 are fibre-conjugate to a product at equal size.
    - All 64 become fibre-conjugate to $(\varphi\times{\rm id}_2)\times C_N$ after enlarging both
      sides by an $N$-cycle, $N\in\{6,12\}$. Each relabelling is built and verified pointwise, and
      $T$ is re-checked.
    - 48 of these are $\Phi$-changing.
  - A6: 36 visible-fibre-preserving relabellings of the A4 base on the fixed carrier. All 36
    preserve $T_t$; 24 change some $\Phi_t$ entry. This agrees with the review's `a4reach.py`.
  - A6 negative control (must fail). The fibre-mixing relabelling `[0,1,3,2,4,5]` changes $T_t$, and
    288 of all 720 relabellings of the base change $T_t$. A6's invariance count therefore cannot
    pass vacuously.
  - The review's `pairc.py` and `tvspath3.py` were also rerun, and their outputs are as reported in
    Step 1.
- **Re-grep.**
  - Corrected phrases: 0 remaining across `papers/*.md` and `book/*.md` (23 patterns).
  - Surviving context: "conditional on the semigroup-transfer completeness step" 6, all class (ii),
    including the owner's clause; "Lemma 24.1" 44, the base count; "turtle" 32, all in ch03 and FULL.
- **Mirror.** No ch03 line is absent from FULL; the release gate's `mirror` step reports 0.
- **Build, page counts and gates.** The current figures are in the round-2 report. Methodology,
  Explainer, GR, Structure and the book were rebuilt.
- **Lean and census.** No Lean file and no census entry is touched. **Requires formal change:
  none.**

## Not a flaw (left unchanged)

- ch02:174 and Methodology:359 ("without empirical content"): definitional.
- Complexity:206, "No finer distinction … is empirically accessible": definitional.
- Complexity:336: a regress about mathematical existence.
- Computation:166–:170 and ch14:182.
- Substratum:60: already scoped to the decoupled case for exact gauge. (GR:142 was corrected in item 23.)

## Open research questions (for #970)

1. **One-way-driven extensions (NEW).**
   - **Finding.** A skew product $(s,f)\mapsto(\varphi(s), g_s(f))$ preserves every classical
     $T_{ij}(t)$ exactly and can change $\Phi_t$'s coherence entries (A4). At equal size its cycle
     type is generally outside every product enlargement. After a further decoupled enlargement of
     both sides, though, it is conjugate to an enlarged $\varphi\times{\rm id}$ by a
     visible-fibre-preserving relabelling (A5). Such relabellings preserve $T$ but not, in general,
     $\Phi_t$ (A6: 24 of 36).
   - **Consequence.** Whether such extensions are gauge depends on three things:
     - which data count as observables: $T_{ij}(t)$, $H$ and $\hbar$ (Substratum:249) or the channel
       family $\Phi_t$ that Lemma 24.1 uses;
     - which relabellings generator (i) contains: any visible-fibre-preserving $\pi$, or only those
       preserving $\Phi_t$, such as $P_\sigma\otimes W$;
     - the partition quantifier in the definition ("for all partitions of the same structural
       class").
   - **Question.** This is the question of the frozen round 24.1B. It also decides whether a
     "simulation" of the substratum is gauge.
2. **Lemma 24.1's cyclic subspace.** As written (Substratum:279), the subspace
   $\mathcal C_B=\overline{\rm span}\{\hat\varphi^t(\mathcal C_V\otimes{\rm supp}\,\omega_H)\}$ is
   the whole space under the uniform prior. The lemma's deep remainder is then empty by definition.
   The 24.1 round records this (`result.md`, ST0(c)), so the item is CONFIRMING.
3. **Whether the four families are complete.** The question stays open; see C3.

## Cross-unit dependencies

- **C1. SC-37 (`corpus/sc37-g3-conditional`, now `59e5962c`; its ch03 is unchanged since
  `23f0fc97`).**
  - **Overlap.** It edits ch03:222 / FULL:1098, the "flagship case … energetic content" clause and
    the dark-sector sentence, and ch03:212 / FULL:1088. SC-43 edits only the last two sentences of
    ch03:222 / FULL:1098, and the adjacent ch03:220 / FULL:1096.
  - **Resolution: keep both.** Take SC-37's line, then replace its unchanged final two sentences
    with SC-43's text.
  - **O2 on ch03:220.** This edit makes "energetic content" deducible "conditionally on the open
    matter-to-boundary coupling step ([GR §6.2])", which is SC-37's descriptor at its ch03:212 and
    aligns with SC-37's condition on ch03:222.
  - **GR.** SC-37's GR hunks at `e5684370` do not touch GR:142 (item 23).
  - **Wording.** No conflict was found between SC-37's wording and the $\mathcal G_{\rm sub}$
    finding. The "invisible … *by theorem*" grade is a GR emergent-QFT claim, and SC-43 did not
    verify it.
- **C2. Shared definitions SC-43 relies on and does not change.**
  - the $\mathcal G_{\rm sub}$ definition (Substratum:249), including its observable set and
    partition quantifier;
  - Theorem 24(iii) and its scope (Substratum:257);
  - the boundary-only dependence lemma (GR:112);
  - the §3.6 / Methodology §19 identification.
- **C3. The proposed SC-44 scope.** The Lemma 24.1 sites go to the owner and are not edited here,
  except Explainer:976 (review B5). This is the reviewer's reconciled list, adopted as is.
  - **(iii) False as stated** (they assert Lemma 24.1's contradicted conjugation conclusion, its
    single-channel form, or closure upon verifying it):
    - Substratum:273, :279, :281, :283, :287, :291, :298;
    - ch02:152 / FULL:795; ch02:158 / FULL:801;
    - Structure:678;
    - Methodology:353, :355, :357, :359.
  - **(ii) Stale but harmless** (conditional on "Lemma 24.1's (semigroup-transfer) completeness
    step"):
    - Substratum:16, :24 (twice), :189, :193, :271, :293, :317, :498;
    - Structure:47 (first mention), :138, :154, :205;
    - Methodology:13, :33, :333, :339, :351, :365, :425, :437, :569;
    - Complexity:206;
    - ch00:95; ch02:88, :118, :126, :132, :150;
    - ch03:80, :208, :220 (the owner's clause) and :224;
    - their FULL mirrors.
  - **(i) Accurate.**
    - Substratum:32, and :195. :195 is borderline: it presupposes the lemma for the dilation datum.
    - Structure:47 (second mention), :659, :668, :770.
    - Methodology:359's "provably without empirical content", which is definitional.
    - Explainer:976 after B5.
    - ch03:228.
    - `verification/ROADMAP.md`:64.
  - **Theorem hypotheses.** Substratum:189 (Lemma 23.0), Substratum:193 (Theorem 23) and ch02:118
    (the Reconstruction Theorem) carry "Lemma 24.1's semigroup-transfer/completeness step" as a
    hypothesis. A hypothesis that names the lemma itself is vacuous, because the lemma's stated
    conclusion is contradicted in the kernel. When propagated, these should read "the completeness
    of the four families".
- **C5. SC-44 (`corpus/sc44-lemma241-core`, drafted at `1576a261`).** SC-44 replaces Substratum
  §4's Lemma 24.1 with the restricted block-word trace theorem (`WT3_spanning_iff`) and states that
  generator completeness is open. Once it lands, Substratum §4 contains no "semigroup-transfer step".
  - **Affected text.** ch03:220 / FULL:1096 must then be reconciled with SC-44. Two phrases refer to
    the step SC-44 removes: the owner's clause ("conditional on the semigroup-transfer completeness
    step") and SC-43's bridging phrase ("Substratum §4, through its semigroup-transfer step").
  - **How it is resolved.** The joint wording comes from the SC-44 review. The owner's clause
    changes only by the owner's decision.
  - **Other references.** The same applies to SC-43's ch03:208 ("conditional on the
    semigroup-transfer step (Substratum Lemma 24.1)") and to the Explainer:976 citation
    "[Substratum §4]". SC-43 does not edit Substratum.
- **C4.** SC-42 edits Explainer:950, adjacent to SC-43's Explainer:946 and :976. No other branch
  touches a round-2 target line (checked by hunk intersection).

## r32 trace

This section is the support r32 traces to. It is not Introduction text.

Wording the corrected sources support, for a two-to-three-sentence paragraph after the card-game
analogy:

> If the substrate rests on further structure, the framework can say of one class of such structure
> that it could never matter to an observer. Structure added below the hidden sector the observer is
> coupled to, evolving independently of both, changes no observable at all — an elementary result
> proved on paper — and on the framework's structural realism such differences are not further
> facts but gauge freedom, in the way a choice of coordinates is not a fact about spacetime. That
> this gauge classification is complete, so that the line between physical and gauge is drawn
> exactly, is conditional and not proved, so the framework does not show that there is no deeper
> physical reality: it shows that one class of candidate deeper differences could never be
> registered by any embedded observer.

| Clause | Source | Evidence level |
| --- | --- | --- |
| structure added below the hidden sector the observer is coupled to, evolving independently of both, changes no observable | Substratum:257, :261 (Theorem 24(iii)); ch02:44, :144; ch03:220 | proved on paper (elementary); exhaustive-exact on small instances (A1) |
| such differences are gauge freedom, not further facts | ch03:142, :152, :220; Methodology:459–:471 | interpretive identification, offered as a proposal |
| coordinates analogy | ch03:220 | exposition |
| completeness of the classification is conditional and not proved | ch03:220 (B1); Explainer:976; Substratum:271, :283; ROADMAP:64; kernel ST3–ST4 | conditional; the argument offered is not established; neither proved nor refuted |
| not "no deeper reality" | ch03:220 (three cases; silent outside A1–A6 or the classified ontology); Substratum:293 | scope statement |

Do not use these phrasings:

- "conditional on Lemma 24.1": its stated conclusion is contradicted in the kernel (C3);
- "proves there is nothing below";
- "by theorem";
- "the simulation hypothesis is meaningless". Only independently evolving hardware is covered.
  Hardware driven by the simulated state preserves every transition probability but can change the
  channel coherences, so whether it is gauge depends on what counts as observable (A4–A6). Do not
  say it is "unreachable by the generators" either: after a further enlargement it is reachable by a
  visible-fibre-preserving relabelling.
- "any slower coupling would show up at order $t/\tau_B$": this is an upper bound only.
