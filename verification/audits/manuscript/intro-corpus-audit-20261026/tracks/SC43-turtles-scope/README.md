# SC-43: the scope of the "turtles all the way down" argument

Base `main` at `0d917665`; branch `corpus/sc43-turtles-scope`. Line numbers are at the base, and
the book chapter and its `FULL.md` mirror were edited identically (ch03:N is FULL:N+876 in this
section).

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
3. That the four generator families exhaust $\mathcal G_{\rm sub}$ is conditional. Its proof route
   is not established: the kernel refutes the semigroup-transfer step's stated conclusion on the
   tested readings (below).

## Step 1: the status of each ingredient

| Ingredient | Authoritative statement | Status |
| --- | --- | --- |
| $\mathcal G_{\rm sub}$, definition | Substratum:249: "(S, φ) ∼ (S′, φ′) if the two systems produce identical emergent physics — the same transition probabilities $T_{ij}(t)$, the same emergent Hamiltonian (up to D-gauge), and the same ℏ … The set of transformations mapping (S, φ) to an equivalent (S′, φ′) is a group"; ch02:136 is the same. | A definition: all observables-preserving transformations. |
| Theorem 24, the four families lie in $\mathcal G_{\rm sub}$ (soundness) | Substratum:251–:261; ch02:140–:148; Structure:154, :205; Methodology:353. | Proved on paper. (ii) holds under the alphabet-size hypothesis; for the gauge sector, (iv) is restricted to cubic-structure-preserving isomorphisms. In Lean, only the hidden-conjugation part of (i) is kernel-checked at the level of the uniform-prior family (`familyAt_hiddenConjugate`, ST1′, `OIBridge/SemigroupTransfer.lean`). |
| Generator (iii), exact statement | Substratum:257: "Adjoining to $\mathcal C_D$ … additional degrees of freedom that no dynamics couples to $\mathcal C_V\times\mathcal C_B$ — so that the bijection on the enlarged space is $\varphi\times\varphi_{\rm new}$ … — leaves every $T_{ij}(t)$ unchanged at every $t$ … *(Scope.)* An enlargement whose dynamics couples to the boundary layer, even slowly … is not in this family: … $T_{ij}(t)=T^{(B)}_{ij}(t)+\mathcal O(t/\tau_B)$, so such an extension preserves the leading-order transition law $T^{(B)}$ on accessible timescales $t\ll\tau_B$, not the transition probabilities themselves." | The decoupled product case is proved on paper, by the elementary averaging at Substratum:261. Check A1 below confirms it exhaustively and exactly on the stated small instances. Lean: `enlarge` and `visibleBlock_enlarge` exist, but no family-invariance theorem does. The slow-coupling bound is a paper argument (GR:112–:132), and it is an upper bound only. |
| Completeness (the four families exhaust $\mathcal G_{\rm sub}$) | Substratum:271: "The four families exhaust $\mathcal G_{\rm sub}$ conditional on Lemma 24.1's semigroup-transfer step"; Substratum:283: "The framework asserts (2) … it does not here reproduce the GNS uniqueness proof, and (2) is the step to check"; Substratum:293: the completeness is "relative to the observable set $\{T_{ij}(t), H, \hbar\}$ and the substratum ontology of §2". | **Conditional, and its proof route is not established.** `verification/ROADMAP.md`:64 lists P1 as "**OPEN** — the semigroup-transfer route is refuted on the tested readings (`ST2`–`ST4`); the obligation itself is untouched". In the kernel, at level 2 (`OIBridge/SemigroupTransfer.lean`, census family "Substratum Lemma 24.1 — the semigroup-transfer step", kernel-only), `ST3_pairC` gives two six-state substrata. Both have trivial hidden commutant and the same family at every $t$, and no unitary relates them. `ST4_pairC` shows that no visible relabelling and hidden unitary relate them either, after any decoupled enlargement. 24.1A (`WordTraceSufficiency`) proves that word-trace equality is sufficient on the spanning class only; sufficiency in general is undecided. 24.1B and 24.1C are frozen control planes with no result. The round's permitted sentence (`lemma-24-1-semigroup-transfer/result.md`:239) is: "the present completeness proof remains conditional, and repairing its route needs stronger multi-time data or a different argument". |
| The reconstruction theorem's equivalence-class form | Substratum:193 (Theorem 23); ch02:118. Under E1–E7, M1-T, M1-B, A1–A6, C2-mixing and "Lemma 24.1's semigroup-transfer/completeness step", the local propagating lattice/gauge residue is fixed "up to the stated substratum-gauge freedoms". ch02:122: "uniqueness is within the structural class A1–A6". | Conditional on the listed hypotheses, one of which is the completeness step. Bell-inclusive uniqueness is open. |
| The identification "gauge freedom = gauge incompleteness, no fact of the matter" | ch03:154: "treat it as a proposal the framework's structure invites rather than as a load-bearing result"; Methodology:459: "the least settled; … offered as a proposal for scrutiny". | A proposal, resting on an interpretive premise. It is not a theorem. |

## Step 2: the claims corrected (per claim)

The edits are identical in ch03 and in FULL.

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
     - "it is gauge, so the four generators move it" needs completeness, which is conditional.

     The physical/invariant criterion is the framework's structural-realist criterion, not a
     theorem.
   - **Correction.** "physical, on the framework's structural realism, when it is an invariant … and
     gauge when some observables-preserving transformation moves it. The criterion can be applied
     exactly only as far as $\mathcal G_{\rm sub}$ is known explicitly, and the four generator
     families are known to exhaust it only conditionally, on the semigroup-transfer completeness step
     …; a transformation that preserves every observable and lies outside the four families has not
     been excluded."
4. **ch03:220, "Below that line the sortal *turtle* stops being well-formed, and asking … becomes —
   precisely, not loosely — the analogue …".**
   - **Defect.** The sentence stated the conclusion without its premise.
   - **Correction.** "Below that line, on the framework's identification of gauge freedom with gauge
     incompleteness, …". The words "precisely, not loosely" are removed. The owner-designated
     conditional clause ("here the $\mathcal G_{\rm sub}$ invariants do, conditional on the
     semigroup-transfer completeness step …") is kept verbatim.
5. **ch03:220, the simulation-hypothesis sentence.**
   - **Defect.**
     - "there is no physics question there to answer" rests on the identification.
     - "a difference coupled …, however slowly, enters the transition probabilities at
       $\mathcal O(t/\tau_B)$" reads an upper bound as an effect that always occurs.
     - A simulation whose hardware is driven by the simulated state is a one-way-driven extension (a
       skew product). It is not the product extension of generator (iii). Probe A4 below shows that
       such an extension leaves the classical transition law unchanged, can change the channel
       family's coherence entries, and has a cycle type that no product enlargement followed by a
       relabelling reaches.
   - **Correction.**
     - The covered case is narrowed to "deep-sector structure evolving independently of the boundary
       layer … so on the framework's gauge bookkeeping the difference between them is gauge".
     - Two cases are stated as outside it: driven hardware ("not one of the four generator families,
       and that every such implementation preserves every observable is not established"), and
       coupling, which "can change the transition probabilities, at order $t/\tau_B$".
6. **ch03:222 / FULL:1098, the closing two sentences only: "in the deep sector where enlargement is
   pure gauge … it ends where the framework can prove there is nothing left for it to be about".**
   - **Defect.** The sentences claimed a proof of the dissolution.
   - **Correction.** "…where independently evolving enlargement leaves every observable unchanged,
     does *below* stop referring, on the framework's identification of such differences as gauge. …
     on that identification it ends where no observable is left for it to be about — a boundary the
     framework draws explicitly by its four generator families only conditionally on the completeness
     of its gauge classification."
   - **Not touched.** The dark-sector sentences on the same line belong to SC-37 (see the cross-unit
     list).
7. **ch03:226 / FULL:1102, "the gauge boundary is the framework proving where deduction runs out".**
   - **Correction.** "…locating where deduction runs out — exactly for independently evolving
     deep-sector structure, and for the rest conditionally on the completeness of its gauge
     classification —".
8. **ch03:228 / FULL:1104, "theorems for everything in between, and a proof that below a certain
   depth the word *below* stops referring".**
   - **Defect.**
     - What lies between the foundation and the gauge line includes conditional results and named
       hypotheses (H-Bell, H-slope, the coupling step G3, and others).
     - The "proof" covers invariance, not the loss of reference.
   - **Correction.** "derivations for what lies between — theorems, conditional results and named
     hypotheses, each with its stated status — and, below a certain depth, a proof that independently
     evolving structure changes no observable, which the framework's identification of gauge with
     incompleteness reads as the point where the word *below* stops referring; that the boundary is
     drawn exactly by the four generator families is conditional on the completeness step."
9. **ch03:224 / FULL:1100, "the reconstruction exhausts its content — conditional on Lemma 24.1's
   completeness step — exactly where the gauge class begins".**
   - Already conditional, and consistent with the rest. **Unchanged.**

### Downstream sites in the same chain (Step 3)

10. **ch03:208 / FULL:1084 (Worrall), "a completeness theorem conditional on the semigroup-transfer
    step".**
    - **Defect.** There is no completeness theorem.
    - **Correction.** "a completeness argument conditional on …".
11. **ch03:204 / FULL:1080 (Spinoza), "The framework's claims are mathematical theorems rather than
    metaphysical doctrines."**
    - **Defect.** The section's own position rests partly on an interpretive identification.
    - **Correction.** "stated as mathematical results with their hypotheses — theorems, conditional
      results and named hypotheses — rather than as metaphysical doctrines."
12. **ch03:142 / FULL:1018 (§3.6), "where there is, demonstrably, nothing of the matter to be had".**
    - **Defect.** §3.6's closing paragraph calls the identification a proposal.
    - **Correction.** "where no observation, by any observer, could register the difference, and the
      framework's structural realism accordingly holds that there is nothing of the matter to be had."
13. **ch03:154 / FULL:1030, "This identification is recent within the framework's development, …".**
    - **Defect.** This is self-narration (§A.30).
    - **Correction.** "The companion paper presents this identification as the least-settled of its
      contributions, a proposal for scrutiny; …".
14. **Methodology:467 (§19).** Three phrases are corrected.
    - **"The exact extent of the hidden sector … the framework's own gauge classification
      establishes that *no observable depends on the answer*".**
      - **Defect.** The boundary layer's capacity is a class invariant (ch03:220). Only a deep sector
        that no dynamics couples to the boundary layer has an unobservable size.
      - **Correction.** "The size of a deep sector beyond the boundary layer that no dynamics couples
        to it, the labels on hidden-sector states".
    - **"there is no truth there to reach, because a difference that no observation could ever
      register is not a difference in fact".**
      - **Correction.** The premise is stated as the premise: "On the structural-realist premise
        adopted here, that a difference no observation could ever register is not a difference in
        fact, there is no hidden truth the observer is failing to reach."
    - **"the name records the identification, which is a result and not a stipulation".**
      - **Correction.** "Given that premise, this species of incompleteness *is* gauge freedom: the
        identification follows from the premise together with the soundness of the gauge
        generators."
15. **Explainer:946, "the deep-sector cardinality |C_D| … These are … *gauge*. Different values of
    |C_D| produce the same transition data at leading order on accessible timescales … The
    cardinality |C_D| is gauge".**
    - **Defect.** Leading-order agreement is the slow-coupling case, which Theorem 24(iii) excludes
      from the generator. A gauge claim needs the decoupled case, and that case is exact.
    - **Correction.**
      - The sentence is restricted to "a deep sector that no dynamics couples to the boundary layer".
      - It now reads "identical transition data at every time [Substratum §4, Theorem 24(iii)]".
      - The "no fact" step is attributed to the identification.
      - The coupled case is stated separately.

## Site table

| Site | Was | Now | Source |
| --- | --- | --- | --- |
| ch03:142, FULL:1018 | "demonstrably, nothing of the matter" | no observable registers it; structural realism holds nothing of the matter | ch03:154; Methodology:459 |
| ch03:154, FULL:1030 | "This identification is recent …" | "presents this identification as the least-settled …, a proposal" | §A.30; Methodology:459 |
| ch03:204, FULL:1080 | "claims are mathematical theorems" | "mathematical results with their hypotheses" | the corpus's status labels |
| ch03:208, FULL:1084 | "a completeness theorem conditional" | "a completeness argument conditional" | Substratum:271; ROADMAP:64 |
| ch03:220, FULL:1096 | "can prove …"; dichotomy; "line … stated exactly"; iff; "precisely, not loosely"; simulation; "enters … at" | criterion, exact result and conditional rest; three cases; criterion conditional on completeness; identification named; simulation scoped; "can change" | Substratum:257, :261, :271, :293; GR:112; ch03:154; probe A4 |
| ch03:222, FULL:1098 (last two sentences) | "pure gauge"; "can prove there is nothing left" | observables unchanged, on the identification; boundary conditional on completeness | as above |
| ch03:226, FULL:1102 | "proving where deduction runs out" | "locating …, exactly for … and for the rest conditionally …" | as above |
| ch03:228, FULL:1104 | "theorems for everything in between, and a proof that … *below* stops referring" | derivations with stated status; proof of invariance read through the identification; boundary conditional | as above |
| Methodology:467 | extent of hidden sector; "because …"; "a result and not a stipulation" | decoupled deep-sector size; premise explicit; follows from premise and soundness | Substratum:257; ch03:220 |
| Explainer:946 | \|C_D\| gauge at leading order | decoupled \|C_D\|, exact; coupled case separate; identification named | Substratum:257 |

## Evidence level of each corrected claim

- **Invariance under decoupled deep-sector enlargement.**
  - **Level.** Proved on paper (Substratum:261, elementary). It is also checked exhaustively in exact
    arithmetic on small finite instances (A1).
  - **Not Lean.** `familyAt_hiddenConjugate` covers only hidden conjugation.
- **Slow coupling.** A paper argument (GR:112–:132), and an upper bound $\mathcal O(t/\tau_B)$. It
  does not show that an effect always occurs.
- **Completeness of the four families.**
  - **Level.** Conditional, as the corpus states it.
  - **Proof route.** Refuted on the tested readings, kernel-checked at level 2 (ST2–ST4). The
    obligation is OPEN (ROADMAP P1).
  - **Not claimed.** Nothing here says completeness is false.
- **"No fact of the matter" and "below stops referring".** These rest on the §3.6 / Methodology §19
  identification, a proposal. Beyond decoupled enlargement, they are also conditional on completeness.
- **Probe A4 (one-way-driven extensions).**
  - **Level.** Exhaustive and exact on one stated finite instance: a toy carrier, not the framework's
    physical substratum.
  - **Role.** It is a witness that bounds the simulation sentence. It is not a theorem.

## Claims removed or made conditional

- **Removed.**
  - "can prove that the question loses reference";
  - "ends at a line the framework can state exactly";
  - "precisely, not loosely";
  - "it ends where the framework can prove there is nothing left for it to be about";
  - "theorems for everything in between";
  - "a proof that below a certain depth the word *below* stops referring";
  - "the gauge boundary is the framework proving where deduction runs out";
  - "demonstrably" (§3.6);
  - "a result and not a stipulation" (Methodology);
  - the leading-order gauge claim for |C_D| (Explainer).
- **Made conditional on the identification.** The loss of reference, "no fact of the matter", the
  simulation-hypothesis dissolution (for independently evolving structure), and the ending of the
  regress.
- **Made conditional on completeness.** That the gauge line is drawn by the four generator families,
  and that the $\mathcal G_{\rm sub}$ invariants exhaust the physics. The second was already
  conditional and is kept.
- **Kept as proved.** Decoupled deep-sector enlargement leaves every observable unchanged at every
  time. For slow coupling, only the leading-order law on accessible timescales is guaranteed
  unchanged.

## Checks

- **The check script.** `check_turtles.py` is run as `python3 -I check_turtles.py <repo-root>`, and
  its output is `check.out`.
  - **Part A** is exact (integers and `Fraction`) and periodic in $t$, so it covers every $t$:
    - A1, control: 8 product enlargements of a fixed $(V,H)=(2,3)$ substratum leave $T_t$ and
      $\Phi_t$ unchanged.
    - A2, control: an independent replay of the kernel's Pair C. The family is equal at every $t$;
      the fixed-point counts are 2 and 0.
    - A3, countercontrol: a two-way coupled extension changes $T_t$. The check fires.
    - A4, probe: 64 of 64 one-way-driven extensions by one bit preserve $T_t$ at every $t$. Of these,
      48 have a cycle type no product $\varphi\times\varphi_{\rm new}$ has, and the same 48 change
      some $\Phi_t$ coherence entry.
  - **Part B** is the re-grep.
- **Re-grep.**
  - Corrected phrases: 0 remaining across `papers/*.md` and `book/*.md` (15 patterns; before the
    edit: 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1).
  - Surviving context: "conditional on the semigroup-transfer completeness step" 6 (unchanged);
    "Lemma 24.1" 46, up from 44 with the two added ch03 mentions; "turtle" 32, all in ch03 and FULL.
- **Mirror.** No ch03 line is absent from FULL; the release gate's `mirror` step reports 0.
- **Build.**
  - Methodology: 54 → 54 pages, median 3094 characters per page.
  - Explainer: 70 → 70 pages, median 2943.
  - Book: 558 → 559 pages, median 3044.
  - No missing glyphs.
- **Gates.**
  - `tools/release_gate.py`: every step passes except `lean-axioms`, which needs the toolchain.
  - `tools/coverage_check.py`: OK. No edited sentence is a canonical statement in `LEDGER.json`;
    the Explainer entries there concern Main's Lemmas 1–3.
  - `verification/lean/edge_rigidity_probe.py`: all checks pass.
- **Lean.** No Lean file is touched. The census is not touched; no manuscript cites a new kernel
  identifier. **Requires formal change: none.**

## Not a flaw (left unchanged)

- ch02:174 ("which specific substratum representative is real? … has no empirical content") and
  Methodology:359 ("— provably — without empirical content"). Representatives of one class share
  every observable by the class's definition.
- Complexity:206, "No finer distinction between substrata is empirically accessible". This is
  definitional, and the completeness sentence before it is already conditional.
- Complexity:336, "The regress has no bottom". It concerns mathematical existence and agrees with
  ch03:226's justificatory regress.
- Computation:166–:170 and ch14:182 (P vs NP is not gauge).

## Open research questions (for #970)

1. **One-way-driven extensions (NEW).**
   - **Finding.** A skew product $(s,f)\mapsto(\varphi(s), g_s(f))$ preserves every classical
     $T_{ij}(t)$ exactly. Its cycle type is generally outside every product enlargement, so no
     relabelling after a product enlargement reaches it. It can change $\Phi_t$'s coherence entries
     (A4).
   - **Consequence.** $\mathcal G_{\rm sub}$ is defined through $T_{ij}(t)$, $H$ and $\hbar$
     (Substratum:249), while Lemma 24.1 works with the channel family $\Phi_t$. Which data count as
     observables therefore decides whether such extensions are gauge.
   - **Question.** This is the question of the frozen round 24.1B, which asks what the
     observables-preserving hypothesis fixes. It also bears on whether a "simulation" of the
     substratum is gauge.
2. **Lemma 24.1's cyclic subspace.** As written (Substratum:279), the subspace
   $\mathcal C_B=\overline{\rm span}\{\hat\varphi^t(\mathcal C_V\otimes{\rm supp}\,\omega_H)\}$
   contains the whole space at $t=0$, because $\omega_H$ is uniform. The lemma's deep remainder is
   then empty by definition. The 24.1 round records the same point (`result.md`, ST0(c)).
3. **Whether the four families are complete.** The question stays open. The corpus's
   proof-route statements still read "conditional on Lemma 24.1's semigroup-transfer step". That
   step's stated conclusion is refuted on the tested readings, so those sentences need an
   owner-called propagation (cross-unit item C3).

## Cross-unit dependencies

- **C1. SC-37 (`corpus/sc37-g3-conditional`, head `15899d90`).**
  - **Overlap.** It edits ch03:222 / FULL:1098, the "flagship case … energetic content" clause and the
    dark-sector sentence, and ch03:212 / FULL:1088. SC-43 edits the same physical line, ch03:222 /
    FULL:1098, but only its last two sentences ("Only past that first real turtle … to be about."). It
    also edits the adjacent ch03:220 / FULL:1096.
  - **Resolution: keep both.** Take SC-37's line, then replace its unchanged final two sentences
    with SC-43's text.
  - **Wording.** No conflict was found between SC-37's wording and the $\mathcal G_{\rm sub}$
    finding. The boundary entropy's "invisible … *by theorem*" grade is a claim about the emergent QFT
    (GR), not about the completeness of $\mathcal G_{\rm sub}$, and SC-43 did not verify it.
  - **Not checked.** The class-invariant reading of "energetic content" in ch03:220 is unchanged;
    whether it carries SC-37's G3 condition is for SC-37.
- **C2. Shared definitions SC-43 relies on and does not change.**
  - the $\mathcal G_{\rm sub}$ definition (Substratum:249);
  - Theorem 24(iii) and its scope (Substratum:257);
  - the boundary-only dependence lemma (GR:112);
  - the §3.6 / Methodology §19 identification.

  Any unit that strengthens or weakens one of these affects the corrected sentences here.
- **C3. The Lemma 24.1 propagation, which needs an owner call and was not made by SC-43.** The 24.1
  round notes reserve the propagation to the owner (`lemma-24-1-semigroup-transfer/result.md`:247).
  These sites state completeness as conditional on a step whose stated conclusion the kernel refutes
  on the tested readings:
  - Substratum:193 (Theorem 23 hypothesis), :271, :273–:283, :317;
  - Structure:47, :138, :154, and :678. The Remark "why Lemma 24.1 can say more" calls the lemma's
    conjugation conclusion consistent; `ST3_pairC` contradicts that.
  - Methodology:339, :351, :355 ("would be closed outright once that lemma is verified"), :357,
    :359;
  - Complexity:206;
  - ch02:88, :118, :126, :132, :150–:152;
  - ch03:80;
  - FULL mirrors of all of these.

  SC-43's own sentences use the corpus's conditional form, so they stay consistent with these
  sites. The r32 trace below avoids the stale form.
- **C4.** SC-42 edits Explainer:950, adjacent to SC-43's Explainer:946. There is no textual overlap.

## r32 trace

This section is the support r32 traces to. It is not Introduction text.

Wording the corrected sources support, for a two-to-three-sentence paragraph after the card-game
analogy:

> If the substrate is itself built on further structure, the framework can say which such
> differences could ever matter to an observer. Structure added beneath the observer's horizon that
> evolves independently of it changes no observable at all — a proved, elementary result — and on
> the framework's structural realism such differences are gauge freedom rather than further facts,
> in the way a choice of coordinates is not a fact about spacetime. That this gauge classification is
> complete, so that the line between physical and gauge is drawn exactly, is conditional and not
> proved, so the framework does not show that there is no deeper physical reality: it shows that one
> class of candidate deeper differences could never be registered by any embedded observer.

| Clause | Source | Evidence level |
| --- | --- | --- |
| independently evolving deep structure changes no observable | Substratum:257, :261 (Theorem 24(iii)); ch02:144; ch03:220 | proved on paper (elementary); exhaustive-exact on small instances (A1) |
| such differences are gauge freedom, not further facts | ch03:142, :154, :220; Methodology:459–:471 | interpretive identification, offered as a proposal |
| coordinates analogy | ch03:220 | exposition |
| completeness of the classification is conditional and not proved | Substratum:271, :283; ch02:150; ch03:208, :220; ROADMAP:64 (P1 OPEN); kernel ST2–ST4 (route refuted on tested readings) | conditional; proof route not established |
| not "no deeper reality" | ch03:220 (three cases; the classification says nothing outside A1–A6 or outside its ontology); Substratum:293 | scope statement |

Do not use these phrasings:

- "conditional on Lemma 24.1": it is stale (C3);
- "proves there is nothing below";
- "by theorem";
- "the simulation hypothesis is meaningless": only independently evolving hardware is covered, and
  driven hardware is not (A4);
- "any slower coupling would show up at order $t/\tau_B$": this is an upper bound only.
