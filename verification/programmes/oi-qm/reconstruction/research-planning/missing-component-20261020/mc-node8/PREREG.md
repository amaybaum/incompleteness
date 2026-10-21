# Node 8: what independently motivated condition, added to OI, is sufficient to recover the full operational structure of quantum mechanics? Preregistration

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This file is
the node's preregistration. It is written, and its sha256 recorded, before any computation on a candidate. No
operational state space, purification, axiom audit, information quantity, visibility, distinguishability, CHSH value,
macroscopic covariance, NPA membership or derivation-step verdict has been computed under any candidate. The
candidates, the decision criteria, the derivation routes, the assumption ledgers, the controls and the classification
are fixed here. The expected outcomes are not (§A.29).

**Governing question (owner, 2026-10-21).** What independently motivated condition, added to OI, is sufficient to
recover the full operational structure of quantum mechanics? The candidate condition, labelled C5 (candidate) or H-C5,
does not need to be derived from C1–C4 and should not be. Node 8 looks for an independent condition that, added to OI,
bridges to a full equivalence proof between OI + C5 and QM. A model satisfying C1–C4 but violating a candidate is a
positive finding: it shows the candidate adds a genuine restriction. Being an additional assumption is not a defect.

**The approved node questions stay** (`mc-node7` NODE.md §10, reviewed): do OI's existing premises constrain access
across alternative interventions strongly enough to derive information causality (IC) or macroscopic locality (ML)?
Under the redirect these run as the independence test R1 for the information candidate and as its own derivation lines
(§10). The relation between path records and interference is a diagnostic control (§9), not a target.

**Decision criteria for any candidate C5 (owner).**
- **R1 Independence.** C1–C4 do not already imply it. Witness: an admissible C1–C4 model violating it.
- **R2 Physical meaning.** It describes a property of observation, interaction or information access, not "the
  observable laws must be quantum". A candidate failing R2 is circular and classified Reproduction.
- **R3 Sufficiency.** OI + C5 supplies the quantum states, measurements, transformations and composition rules, and
  excludes post-quantum possibilities. This is the central unresolved test.
- **R4 Reverse compatibility.** QM satisfies the condition and fits the corresponding OI realization.

**Candidates, ranked by the owner.**
- Primary, **C5-P**: purification with essential uniqueness [L: Chiribella, D'Ariano and Perinotti, PRA 84, 012311
  (2011)] (§6).
- Secondary, **C5-IC**: the information-consistency measure, retained as a separate constraint; its known limitation is
  that classical theories satisfy it (§7).
- Reference row: node 5's control condition, which fails R2 (§8).

**Both directions, separately (§A.34).** D1: every allowed OI + C5 experiment has quantum statistics. D2: every quantum
experiment in the stated scope has an allowed OI + C5 realization whose operational theory is exactly QM's. D2 is not
the response-table construction alone, which realizes statistics (Main.md:578) while C5-P concerns states,
transformations and composites of the realization's operational theory. Neither direction is established by adopting
C5 (§6.6).

**Depth-first scope (§A.12).** Node 8 does not attempt the CDP reconstruction proof. Its first computation after freeze
is §6.10: the operational state space defined by all interventions for the smallest finite realization classes with an
operational mixture, and whether purification can hold there. Two lemmas of pure mathematics (Lemma T, transitivity from
uniqueness; Lemma K, cardinality) are written with proofs in §6.1 and preregistered as definitions and lemmas, never as
results about OI. Its deliverables: (a) exact
definitions of state, pure state, mixture, transformation, reversible transformation and composite within OI's
operational theory, fixed before any computation (§2.2); (b) the per-axiom audit of CDP's framework and axioms, each
verdict typed (§6.3, §6.4); (c) the controls: real-amplitude QT, Spekkens' toy theory, classical theory,
boxworld/PR, and node 6's A = λ, B = λ ⊕ ab model with K-PR6 (§6.5, §14); (d) D1 and D2 as separately preregistered
questions with status (§6.6); (e) the R1–R4 scorecard for C5-P, C5-IC and node 5's condition (§13.2).

**Working hypothesis, to be tested, not a result.** H-X: OI needs restrictions linking different interventions on the
same system, beyond constraints on individual recorded histories. Its decision rule is §13.4.

**Standing decisions.** (a) Tsirelson's bound, (b) the full quantum set and (b-corr) the quantum correlator set are
separate verdicts (§11). A1 exact stays distinct from A2 (§1). K-PR6 is a mandatory countercontrol on every route, and
K-PROG on every Q2 route (§4). Reproducing established QM is a legitimate success here; the additional-consequence
requirement becomes a postdiction requirement (§12).

**Tags.** [AT] adopted kernel theorem, declaration confirmed by `git grep` at the base; [W] written argument (to be
reviewed); [EC] exact computation (step 2; none run here); [NUM] floating-point evidence, never in a verdict; [L]
literature from memory, not read in full; [L-s] bibliographic data and abstract-level claim checked through a web-search
summary at drafting, the paper not read; [L-c] existence and claims reported by the coordinator or the owner on
2026-10-21, not retrieved at drafting, the paper not read; [rec] recorded in the cited record, not re-derived; [Q]
corpus or thread text quoted verbatim.

***

## 0. Base and drafting state

- Thread: `research/missing-component-20261020` at `a501b4189d7f1ada923d76179fa6a38a1a83b408` (PLAN = `../PLAN.md`; MCk =
  `../mc-nodek/NODE.md`; MC7 also `../mc-node7/PREREG.md` and `../mc-node7/amendments/AMENDMENTS.md`). Node 7's frozen
  records are cited, not changed.
- `main` at drafting: `37e55457e74702356b37a5c134fa7d5510cb2119`; the pre-freeze reviewer confirmed `papers/`, `book/`,
  `FiniteEntropy.lean` and `C3Necessity.lean` identical at `a501b418`, `37e55457` and `origin/main` = `4546099f`. The
  cited Lean files are unchanged across them.
- Every [Q] fragment was checked at `a501b418` by `quotecheck.py` (whitespace collapsed, case-sensitive, within the
  stated line range). Its list is synchronized with this file: fragments the file no longer quotes were removed. The
  count is printed by the script and recorded in NODE.md (I-12).
- Worktree for drafting: a detached checkout of `a501b418`. Nothing was run in it except `git`, text search and the
  quote check. `arxiv.org` was unreachable; no paper was read in full. `sympy` was absent at drafting, so the lemma of
  §9.1 is a written argument here and is re-checked symbolically in step 2 (K-LEM), and a missing dependency fails
  rather than skips (I-37).
- **Node 7's K-10.** At the base, node 7's verdicts are "provisional on K-10 at n = 4" (MC7 NODE.md:82). The owner
  reports that the n = 4 check has since been confirmed in CI (run 39529498293). Node 8 does not rely on it: no node-8
  clause is decided through the 𝒜_CHSH reduction, by choice, and K-10's row (§14) reports its status.

**State of knowledge at drafting, so the freeze can be judged.**
- No computation of §5–§11 has been run. The file was restructured four times before freeze (owner directions of
  2026-10-21 and an independent pre-freeze review of its third version, `review/REVIEW-prefreeze.md`); no computation
  preceded any version.
- Recorded facts the routes are built around, none a result of this node:
  - the adopted Bell branch is ontic parameter dependence (Main.md:392, :82);
  - node 7 recorded [Q, MC7 NODE.md:42–43]: "Every §3.1 reading that admits the counting measure on LE(1,1)'s hidden bit
    admits LE(1,1)." LE(1,1) is the PR box;
  - S ⟺ D ⟺ Q_fb holds for every finite law (Main.md:20, :82);
  - one controlled dynamics with a read-only program register realizes every instrument family (Main.md:560);
  - node 4's E7 [rec, mc-node4/NODE.md:263–272]: the canonical purification with bijective purifier maps does not
    produce a coherent prior; node 3 [Q, mc-node3/NODE.md:232–233]: "Purification is the closest to what OI states.
    None of the three is derivable under κ1–κ4."
- Drafting observations, disclosed because they shape routes, none a verdict: a permutation-conjugated diagonal
  operator stays diagonal (§11.2, V-K); initial measurement independence and ontic parameter dependence are distinct
  properties that both hold on branch (a) (§7.4).
- Expected shapes recorded in advance, not verdicts: local tomography is at best compatible-but-added for OI
  (Main.md:630, §6.4); classical theory violates C5-P (mc-node3:233) and satisfies C5-IC (K-C5+); under full κ2 access
  the operational theory of a finite class is classical probability on its preparable priors (Lemma A, §6.1), so the
  live interface restricts access as §2.2 option (B) states, with access measured per class over composed protocols.
- **Interface choice disclosed.** The pre-freeze review of the fourth version showed that unrestricted κ2 access makes
  §6.10's question decidable at freeze (Lemma A). This file adopts option (B): protocol bijections act on visible cells
  and declared ancillas only, and hidden cells change only through the class's fixed dynamics φ and its declared
  coupling steps. The owner has been told of this choice and may override it before freeze; an override is an
  amendment under `amendments/` before any computation.

### 0.1 Corpus and record claims in the owner's direction, verified under §A.19

| # | claim | text [Q] | verdict |
|---|---|---|---|
| V-1 | the double-slit account is an interpretation within the finite-law representation, not a quantitative law | Main.md:666: "The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events."; "A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms."; "The Born rule, often treated as an independent postulate, is here part of the exact fixed-basis representation dictionary". Main.md:664: "the operational theory's unique selection remaining open (§3.4)" | supported for Main. Explainer.md:566 ("The mystery dissolves not into another postulate but into a derivation: this is what marginal statistics look like when paths through the partition are indistinguishable.") is stronger than Main's support; recorded, not acted on |
| V-2 | classical hidden-memory systems produce nonadditive patterns | book/ch01-observation.md:280–282: "a player who prices hands divisibly loses money at a rate equal to the interference term"; "Interference is not a substance; it is the failure of divisibility". Main.md:20: "it is also universal, so representability alone does not distinguish the memory-bearing sector from an ordinary Markov process" | supported |
| V-3 | C3 is a minimum hidden capacity, not a maximum on accessible information | Main.md:78: "The hidden sector has enough distinguishable states to encode the observed conditional past–future information"; Main.md:486: "I(X_{<t} ; X_{>t} \mid X_t) \leq \log_2 m" | supported; "cannot stand in for IC" is tested at route σ-cap (§10.1), not assumed |
| V-4 | S ⟺ D ⟺ Q_fb holds for all finite laws; C4 does not select QM | Main.md:20: "The discriminating content is history readback."; Main.md:82: "C4 is not needed for the existence of a quantum representation; it is what makes the OI sector nontrivial."; Main.md:578: "the response-table construction realizes arbitrary finite stochastic behavior, quantum or not"; appendix-c:228: "which an ordinary classical stochastic process also reprodu[ces]" | supported |
| V-5 | C4 is the independent structural condition | Main.md:604: "Of the three structural conditions, only (C4) is logically independent."; Main.md:72: "(C1) and (C3) follow from (C4) in any faithful realization, and (C2) is a physical-regime premise"; Main.md:76: "a hidden record of visible history, once written, persists to the readback that uses it" | supported |
| V-6 | C4 needs no write-then-read cycle | Main.md:80: "The condition is operational; it does not by itself assert a causal write-then-read cycle — a pre-sampled hidden variable revealed by the history satisfies it (the response-table construction, §3.4)." | supported |
| V-7 | a definite substratum state does not establish a trajectory through one slit | Main.md:666: "In the double-slit experiment, the particle traverses a single slit in the deterministic substratum." No derivation | asserted without derivation; the node defines path by blocking (§9.2) |
| V-8 | one fixed dynamics can read a setting register and run different response rules | Main.md:560: "The per-instrument family assembles into one map: on the enlarged hidden sector carrying a read-only program register — the protocol table — alongside the visible record, the seeds, and the branch register" | supported; basis of K-PROG |
| V-9 | earlier nodes flagged purification as an added premise needing a source | PLAN.md:121–122: "Purification with uniqueness would cover all three, but only as a posit."; mc-node3/NODE.md:232–233 (as above); mc-node5/NODE.md:263: "The purification uniqueness that would give O-B is not supplied (Main.md:602; MC2 §3)."; mc-node5/NODE.md:344–346: "Each posits continuous reversibility or purification with uniqueness." | supported in nodes 2–5; nodes 6–7 silent |
| V-10 | OI does not alone establish product structure, local tomography or one tensor product | Main.md:630: "It does not alone establish statistical product structure after conditioning, local tomography, or one common tensor-product instrument category." | supported; anchor for §6.4 |
| V-11 | the corpus places the reconstruction axioms beyond any fixed finite carrier, and characterizes the OI-compatible completions by five conditions | Main.md:352: "The purification, continuous-transitivity, and tomographic-locality axioms of the cited reconstructions are hypotheses of their continuum endpoint, which the classical-dimension obstruction places beyond any fixed finite carrier;"; "five conditions hold: valid probabilities, trivial-ancilla consistency, inert spectators, full reversible control, and iterated composition"; Main.md:568: "This is a characterization of a quantum-complete extension of OI, not a claim that bare OI entails the added principles" | supported; bears on the framework audit (§6.3) |
| V-12 | the corpus cites Spekkens' toy theory as a precedent | book/appendix-c-objections.md:232 (mirrored at FULL.md:6470): "an epistemic restriction alone reproduces complementarity, uncertainty-like trade-offs and no-cloning, but not violations of Bell inequalities"; "restricted access does not by itself single out quantum theory" | supported |
| V-13 | node 5's condition gives the formal equivalence inside an operational framework that already describes operations with complex matrices | mc-node5/NODE.md:28–29: "Relative to `SourcedOI`, exact QM holds iff phase-free richness (PFR) holds, one continuously driven pair per level [AT]"; GR.md:216: "(iv) *Full reversible control*: every finite unitary on every composite is available." | supported: the condition is stated on available unitaries of a theory of linear maps (§8) |
| V-14 | the corpus supplies a purification ingredient, not the axiom | Main.md:600: "full completions are NOT claimed unique up to reversible relabeling, and same-law realizations with non-relabel-equivalent fibers exist (`fiber_freedom`, certified)"; Main.md:602: "CDP's uniqueness (any two purifications related by a reversible transformation on the purifier alone) is strictly stronger, and the certified fiber freedom shows completions here are not unique as wholes" | supported |
| V-15 | the corpus has its own information–disturbance statement | appendix-c:226: "An instrument that leaves every state unchanged on average — a passive instrument — learns only about the commutative center of the observable algebra"; "it holds in every finite operational theory with two or more states, whether or not the framework's core conditions hold" | supported; used in §6.7 |

***

## 1. A1 exact, and the role of ε

- Outcome (a) requires the supremum of S_max over admitted boxes to equal 2√2 exactly, the Tsirelson box admitted, and
  every local box admitted. Admitting 2√2 + δ for any δ > 0 fails (i). Exactness also governs the axiom audit: an axiom
  holds on a class iff it holds for every member, decided by exact computation on finite instances and reviewed [W].
- Every no-signalling box is realized by an O-admissible realization whose prior is a realization datum (Main.md:60 [Q]:
  "a realization in the sense of §3.4 carries its own fixed hidden prior $\mu_H$ as part of the realization datum").
  Irrational entries are handled in the stated number field or by exact certificates.
- **ε, a tolerance, never relaxes a clause.** It enters only to make exact statements decidable: rigorous enclosures
  (python-flint `arb` or mpmath `iv`, version printed, refined to 2^−64 then 2^−256; an undecided comparison is
  "undetermined"); exact algebra at boundary cases; finite [EC] instances of a universal clause, which never decide it.
- **A2 rows.** Node 7's ε = 1/100 rule is rerun as separately printed sensitivity rows labelled "A2", excluded from the
  verdict path (I-19).

***

## 2. Condition O, and the frozen operational interface

### 2.1 Condition O (inherited)

Condition O of MC7 PREREG §1 is adopted unchanged: O1 one state space Ω = 𝒞_V × 𝒞_H; O2 one dynamics, a composition of
bijections of Ω; O3 one source of probability, with the visible initial configuration a point mass fixed by the protocol
and μ_H independent of the settings; O4 configuration readout. O does not exclude K-PROG (V-8).
- Copies: an N-copy experiment is one realization on the product carrier with any shared cells; independence of copies
  is an assumption typed per reading (A-3, B-4, D-4).
- Communication protocols: inputs and the message are visible cells; each input value runs as part of the visible point
  mass; μ_H does not depend on inputs (Main.md:82 [Q]: "the Bell-violating branch adopted in §3.3 retains measurement
  independence and relinquishes ontic parameter independence while preserving operational no-signaling"); the message
  moves by a bijection.
- Interferometers: source, phase setting, path openings, marker coupling, recombination and detector ports are visible
  cells; the marker is a register in the same Ω with no quantum rule in the hidden sector; path is defined by blocking.
- Checkpoint I-2 measures O.

### 2.2 The operational interface (deliverable (a)), fixed before any computation

Every candidate is stated on this interface. Where a class of realizations does not make an item well defined, the item
is Parked with the gap named; the definitions are not changed by result.
- **System.** A visible register V (finite configuration set 𝒞_V) together with its accessible protocol class 𝒫(V),
  **option (B)**: the κ2 configuration bijections of Ω selectable by a visible setting that act on visible cells and
  declared ancilla cells only, together with the class's declared coupling steps (bijections of Ω that read or write
  hidden cells, listed per class), and κ4 configuration readouts with feed-forward (P15). Hidden cells change only
  through the class's fixed fundamental step φ (O2) and the declared coupling steps (Substratum.md:44: visible
  operations reach the hidden sector "through the coupling"). Each class states φ, its accessible bijections, its
  coupling steps and its ancilla conventions explicitly (§6.10), printed with digest before any computation (I-52).
  Unrestricted κ2 access is Lemma A's hypothesis (§6.1) and is not the live interface.
- **Access is a property of complete protocols, not of the primitive list.** Restricting the primitives does not by
  itself restrict what the observer can learn: composed protocols that wait on φ can expose hidden cells (K-SWAP, §6.5).
  "Restricted access" is therefore never asserted from the primitive list. For each class, §6.10 computes the access
  class, that is, which hidden distinctions are operationally visible after composition over the protocol class, and
  prints it before any purification verdict (I-58). The restricted interface must admit K-SWAP, and §6.10 must detect
  its full hidden access (operational state = hidden prior).
- **Ancillas.** Visible ancilla cells are visible point masses initialized to 0 (O3). Hidden ancilla cells used for
  mixing are counting-measure cells declared with the preparation and counted in Ω; their number per class is stated.
- **The trivial system.** The empty visible register with one configuration; discarding every cell is the allowed
  operation to it (used by Lemma T).
- **Preparation.** An O-admissible realization datum for V: a hidden prior μ_H and preparation bijections, with the
  visible point mass.
- **Operational equivalence and state (across interventions).** Two preparations are the same operational state only
  when every allowed subsequent experiment gives the same statistics: every protocol of 𝒫(V), every protocol on V
  adjoined to any additional system of the realization class, and every later intervention. A state is an equivalence
  class under this relation. The current visible record is not the state: C4 gives the same record with different
  next-step laws (Main.md:80). The corpus's canonical predictive quotient (P21) is a single-law, future-tail quotient;
  extending it across interventions and ancillas is the specific mathematical task that §6.10 performs on stated
  classes, and nothing in this file assumes its result. Control K-OPSTATE (§6.5) fixes an exact instance: identical
  passive records, different operational states.
- **Mixture (preparable-weight mixture).** The physical operation: m declared hidden ancilla bits under the counting
  measure select among at most 2^m preparations (weights k/2^m), and hidden cells of size n contribute denominators n;
  the weights a class can realize are those its declared ancillas and hidden sizes yield. The state set of a class is
  the set of preparable states under this operation: finite per class, and not closed under real convex combination
  unless the class is extended. K-IF prints the preparable set and the pure set per class under this rule (I-54).
  Lemma K's hypothesis (i) therefore fails by construction on a finite class and holds on its convex closure; Q-PREP
  (§6.1) tests which reading OI's premises select. Statistics are affine in the mixing weight (F-2), which Lemma K uses.
  - *What this costs.* CDP's framework uses all real mixing probabilities and operationally closed state spaces, with
    pure = extreme point of the convex set; a finite grid does not satisfy that framework. The file therefore fixes:
    (a) *embedding*: a preparation of a class embeds into a larger realization by adjoining declared ancillas; a 1/8
    event selected by an independent fair coin becomes a 1/16 event, and the randomizer costs resources, so weights
    are stated with the ancilla budget that realizes them; (b) *budget*: purity is assessed within one declared
    resource budget (the class's ancilla count) and again across the whole declared theory (every class of the
    realization family), and both are printed; (c) *closure*: a completed, convex-closed state space is introduced as a
    separate object (the convex closure of the preparable set), to which transformations extend by affine extension
    where that extension is well defined on classes and to which every readout extends; which operations extend is
    printed per class. Hazard recorded: a state may look pure in a restricted preparation menu only because the
    decomposing preparations are missing.
  - *Fixed in advance.* Finite-grid purification is a legitimate test, and passing it does not establish CDP
    purification or exact QM. Lemma K cannot be applied where its arbitrary-mixture hypothesis fails. Two verdict lines
    are kept apart and the classifier prints both: Pur-E on the preparable set (per budget and across the theory) and
    Pur-E on the convex closure (I-59).
- **Carrier and record, kept apart.** A classical output record and its physical carrier are different objects. A
  random classical bit cannot be purified within classical composites. C5-P applies to the physical systems underlying
  the records (the carriers of the realization class), and a restricted description in terms of records alone need not
  satisfy it. Every statement of §6 names which it concerns.
- **Pure state.** A state that is not a nontrivial preparable-weight mixture of two distinct preparable states of its
  class. The owner's note (i): "pure" means not expressible as a nontrivial random mixture of observable states, not
  "the observer knows every hidden variable". On the convex closure of a class, "pure" means extreme.
- **Transformation.** The map on states induced by a protocol step of 𝒫(V) (a bijection with ancillas, followed by
  discarding, that is, marginalization over the ancilla or over discarded cells). It is a transformation only if it is
  well defined on equivalence classes; the check is per class (I-38).
- **Reversible transformation.** A transformation T with a transformation T′ in the same theory such that T′∘T and T∘T′
  are the identity on states. Under κ2 the inverse bijection is accessible (node 7's PC-4a [rec]), but reversibility on
  states is measured, not assumed.
- **Composite.** The product carrier V_A × V_B with the joint accessible class. A local operation on A is a protocol
  acting on A's cells and A's ancillas only; discarding a factor is an allowed local operation. Whether the joint class
  contains operations beyond compositions of local ones and shared randomness is a property of the realization class,
  recorded per class (this is where branch (a)'s long edges live).
- **Allowed operations** include discarding (marginalization), adjoining an uncoupled ancilla in a fixed state, classical
  coarse-graining of outcomes, and sequential composition with feed-forward (κ4).
- **Record variables of a wing.** In every two-wing scenario, Alice's records are her pointer cells and Bob's are his
  pointer cells. Preparer cells (K-PR6's p₁, p₂) sit at the source and are readable by neither wing. The same
  assignment is used wherever "Bob's records" appears (σ-ons, IC-rec, D-3, K-PR6-C5).
- **Bob's system B and time slices.** t₀ is after preparation and before any input or setting acts; t₁ is after Alice's
  operations and before the message arrives and before Bob's input acts; t₂ is Bob's readout. B_{t₀} is the resource:
  the hidden cells and Bob-side cells of the realization, excluding every input and setting register. B_{t₁} is the same
  cells at t₁. Alice's input or setting cells entering Bob's backward cone are recorded as failure mode (i) at the
  guess step (IC-D3, C5-S1) or mode (ii) at the resource step (IC-D5b, C5-S3b), never at the initial-independence step.
  For K-PR6-C5 and C5-0 the system B is fixed now: Bob's box half as an operational system, that is, the pointer r with
  its setting b and Bob's accessible protocols on them, with p₂ not readable (above).

***

## 3. OI premises available to the derivations

A derivation step cites premises from this list only. Anything else enters an assumption ledger and is typed (§12).

| id | premise | text [Q] | status |
|---|---|---|---|
| C1 | non-zero coupling | Main.md:74: "hidden degrees of freedom affect the visible evolution at some accessible step — the conditional law of some visible transition depends on the hidden state" | diagnostic |
| C2 | memory persistence | Main.md:76 (V-5) | physical-regime premise |
| C3 | sufficient capacity | Main.md:78; Main.md:486–488: "Conditioning on $X_t$: $X_{<t} \to H_t \to X_{>t}$ is a Markov chain. By data processing:" | [AT] `c3_necessity` (C3Necessity.lean:80) |
| C4 | history readback | Main.md:80: "two visible histories with the same current state induce different next-step laws, mediated through the hidden state"; V-6 | the independent condition |
| P1 | Lemma 1 | Main.md:48: "The observer has finitely many distinguishable internal states, so the visible configuration space $\mathcal{C}_V$ is finite, with a discreteness scale $\epsilon$ providing a finite minimal cell volume."; Main.md:62: "Of the structure above, only finite visible resolution is a theorem (Lemma 1)." | theorem (the paper's) |
| P2 | Lemma 2 | Main.md:50: "The observer is a proper subsystem: $V \subsetneq S$. The complement $H = S \setminus V$ is the hidden sector." | definition |
| P3 | Lemma 3 | Main.md:56: "a bijection: distinct states have distinct successors and predecessors"; "globally, the counting measure is selected among invariant measures as the maximal-entropy one"; Main.md:60: "the counting measure is the default, not a constraint on representations"; Main.md:62: "injectivity is the requirement that the dynamics preserve the observer's records" | posits (iii), (iv) |
| P4 | trace-out | Main.md:115–117: "let $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ be a bijection", with "\pi_V(\varphi(x_i, h)) = x_j"; Main.md:522: "arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$" | theorem |
| P5k | the kernel's Shannon layer | FiniteEntropy.lean:383–385, `cmi_le_of_deterministic`: "cmi w a b (fun s => g (b s, c s)) ≤ cmi w a b c"; FiniteEntropy.lean:457–459, `cmi_le_log_card`: "cmi w a b c ≤ Real.log (Fintype.card γ)" | [AT]; natural-log units |
| P7 | the coupling-graph cone | Main.md:358: "Thus a setting intervention supported in region $A$ cannot alter a readout in region $B$ before the corresponding causal cones meet."; relative to Main.md:708: "(viii) site factorization — the configuration space is identified with a product of local configuration spaces over a set of sites" | theorem relative to (viii) |
| P8 | Bell ceiling hypotheses | Main.md:361–365: "(i) the dynamics is deterministic; (ii) the setting operations are"; "(iv) the interventions act on one common"; "pre-setting ensemble, so $p(\Omega\mid a,b)=p(\Omega)$" | theorem. Only (i) and (iv) hold on branch (a); (ii)–(iii) are hypotheses of a no-go that branch (a) evades (Main.md:82, :630) and are not available premises. A route citing (ii) or (iii) rejects TB along with PR (§16) |
| P9 | branch (a) | Main.md:392: "at the microstate level, one wing's response depends on the remote setting. This is not an operational signal"; "a Bell preparation supplies bounded-degree long edges or an equivalent nonlocal response map" | adopted branch |
| P10 | operational no-signalling | Main.md:407: "a later local setting cannot produce an operational signal at the remote wing"; "Dropping that spatial/intervention structure returns the unrestricted OI behavior class, including PR, which is the mandatory negative control." | required; evaluated on the wing records of §2.2 |
| P11 | response-completeness | Main.md:405: "If $\Lambda$ is coarser than the response-relevant microstate, $I(\Lambda;Z)$ alone does not control CHSH" | stated requirement |
| P12 | implementation-fixedness | Main.md:550: "Each labelled instrument is one fixed map, applied whenever chosen, in every context; context enters only through the state." | gluing-theorem clause |
| P13 | reference geometry | SM.md:156: "is a sufficient sparsity condition for *typical local neighborhoods* to retain the reference graph geometry."; "This is not a theorem that $\kappa_{OR}$ converges everywhere" | diagnostic |
| P14 | information conservation and access | Substratum.md:44: "φ is a bijection: *perfect memory* — information is never created or destroyed."; "The partition $V$ defines the observer's *access* — both read and write." | construction premise |
| P15 | condition O and κ1–κ4 | MC7 PREREG §1; `mc-node3` [rec] | thread conditions |
| P16 | scope limits | Main.md:630 (V-10); Main.md:534: "exact coherent/composite compatibility is the residual operational-lifting problem" | stated limits |
| P17 | observer covariance | Main.md:668: "each partition satisfying the characterization conditions produces its own C1–C4-quantum description of the remaining degrees of freedom"; Main.md:674: "exists and is unique given $\varphi$. Its marginals reproduce Wigner's $T_W$ and Friend's $T_F$ respectively." | stated property |
| P18 | permutation unitary | Main.md:716: "the realization's permutation unitary, $\hat{H} = i\log U$, exact at integer horizon times for uniform, slice, and weighted priors" | proved |
| P20 | single controlled dynamics | Main.md:560 (V-8) | corollary |
| P21 | canonical predictive quotient, single-law form | Main.md:600: "**Theorem (canonical predictive quotient — a purification ingredient, substratum form).**", for one finite-horizon law P on visible trajectories, quotienting hidden data by the visible future-tail under that law; no regional or composite form (V-14) | theorem (substratum form) |
| P22 | the five completion conditions and OI⁺ | Main.md:352 and :568 (V-11); GR.md:216 | characterization of completions, not a derivation |

**Barred inputs** (checked by §15): E1 and any posited Hilbert-space, operator-algebra, Born-rule, amplitude or
quantum-instrument structure (ℓ²(Ω) of P18 is admitted, built from the substratum); E3 in its Hilbert-space reading
(Substratum.md:92 [Q]: "E3, with the holographic bound read as a Hilbert-space dimension cutoff"); Computation.md:130
[Q] ("realizable correlations are those approximable by finite-dimensional strategies"); the quantum-shadow
realizations of Main.md:576–578; and, as premises, the quantum set, Q1 or any NPA level, TLM, 2√2, the Tsirelson box,
Tsirelson's vector representation, Born weights, B-VF and V² + D² ≤ 1. Main.md:356 [Q] ("the same reversible
response-table construction that realizes arbitrary finite stochastic laws also realizes PR-box behavior"; "The
selector in a Bell experiment is therefore causal locality, not representability.") is respected, not strengthened.
A candidate stated as "the available operations are the finite unitaries" or "the states are density matrices" fails
R2 (§8).

**Search under §A.19.** No corpus text mentions ML, IC, purification uniqueness as an adopted condition, or
tomographic locality as a satisfied property (`git grep -i -E "information causality|macroscopic locality|local orthogonality|Navascu|Wunderlich|Pawlowski|Pawłowski|tomograph|purification"`
over `papers/*.md` and `book/*.md`; purification hits are Main.md:352, :600–602 and the records of V-9; tomography hits
are Main.md:352 and :630). Relevant corpus text on restricted access and passive observation: appendix-c:226 and :232
(V-12, V-15), neither stating a complementarity law. A reviewer may add premises before step 2 (§19).

***

## 4. Order of work, and the mandatory countercontrols

### 4.1 Depth-first order

C5-P (§6) first, then C5-IC (§7), the reference row (§8), the interference diagnostic (§9), the IC and ML derivation
lines (§10), composites (§11), then classification (§13). Each section has its own decision rule, verdict lines and
stopping rule. A Failure in one does not cancel the others; all are reported. No verdict propagates to another section
except through the named steps listed in I-23. Common stopping rule: a section stops when each verdict line is decided
or Parked with the gap named, or when a required check exceeds §A.40's local bounds (then reported incomplete with its
completed range, moved to CI only with owner approval). Feasibility: enumerations of 𝒜_CHSH(n) are bounded at n ≤ 12
for exact rational checks and n ≤ 6 for exhaustive box listing; anything larger is a CI item from the start.

### 4.2 K-PR6, every route

- **Construction (node 7's LE(1,1) [rec], after node 6's B2).** Visible settings a, b; pointers q (Alice), r (Bob);
  preparers p₁, p₂ at the source; hidden λ ∈ {0, 1}, counting measure. Steps, each a bijection: p₁ ^= λ; p₂ ^= λ; q ^= p₁;
  r ^= p₂; r ^= a·b. Records A = q = λ and B = r = λ ⊕ ab: uniform marginals, no operational signalling on the wing
  records (q; r), CHSH = 4. One reversible global update implements it and its last step reads both settings.
- **K-PR6-RAC.** Box inputs x₀ ⊕ x₁ (Alice) and y (Bob); a ⊕ b = (x₀ ⊕ x₁)y; Alice sends m = x₀ ⊕ a; Bob outputs m ⊕ b =
  x_y: Σ_y I(x_y; G | y) = 2 bits on 1 bit sent.
- **Rule.** Every route carries a K-PR6 line, measured and printed: "rejected by premise X at step s" (premise quoted at
  file:line, violation exhibited exactly, with X holding on branch (a) and the same route admitting K-Q and K-C);
  "rejected only by the added axiom A, which admits K-C's realization: yes/no" (Conditional at best; a "no" marks a
  vacuous rejection, which Q-FIN then carries); "rejected only by a Q-typed premise" (Reproduction); or "not rejected". A route whose conclusion bears on correlations or information, with "not rejected", fails as an OI
  derivation. A rejection by P8 (ii) or (iii) is printed as "rejected only by a hypothesis branch (a) evades" and is
  not an O-typed rejection.

### 4.3 K-PROG, every Q2 route

- **Variants, enumerated now.** PROG-0: the marker copies a perfectly readable path bit while a hidden register, read
  with the phase setting, drives a fringe-shaped output; V = 1, D = 1 at K = 12. PROG-B: PROG-0 that also reads the
  path-blocking settings, so blocked-path runs are θ-independent. PROG-3: a three-path version that reads the masks
  and outputs 𝒮₃ = 0 with 𝒮₂ ≠ 0. PROG-c: a partial marker with programmed V = c and D = √(1 − c²) for c ∈ {1/2, 1/√2},
  which satisfies B-VF numerically.
- **Rule.** A Q2 route must reject every variant, PROG-c included: PROG-c's fringe response is set by the program, not
  by the marker coupling. The marker-responsiveness discriminator fixed now: with the program and every other datum
  fixed, changing the marker coupling (the bijection coupling the marker to the path) changes V in a B-VF-type
  mechanism and leaves V unchanged in PROG-c. A restriction that does not reject PROG-c does not distinguish a genuine
  interferometer mechanism from a programmed one, and fails Q2. A C1–C4 model with sinusoidal statistics shows
  Reproduction only.
- **Admission semantics for the controls K-Q, CC-q and the boundary witnesses.** "The restriction admits control X"
  means: there exists an O-admissible realization that reproduces X's record laws on the stated interventions and
  satisfies the restriction. CC-q is a density-matrix model and is never itself an OI object. A boundary witness must
  satisfy the restriction under test, pass the three discriminators (blocked-path θ-independence; 𝒮₃ = 0 with 𝒮₂ ≠ 0;
  the cos law with V and θ₀ fixed by the architecture before the pattern is computed) and the marker-responsiveness
  discriminator.

***

## 5. Typing added assumptions, and the derivation verdict

- **M** mathematics applied to objects the premises fix ([L] allowed only here). **O** supplied by a step citing §3,
  closed by [AT] or reviewed [W]. **A** physical and not supplied: a named axiom, which makes the result Conditional on
  it. **Q** a barred input or a statement that fails R2, which makes the result Reproduction.
- A parameter OI does not fix and this file does not fix in advance is Failure-as-stated. A parameter fixed here
  (α = 1/2; the measure B-1; the phase alphabet K) is A-typed when OI does not supply it, and Q-typed when its only
  justification is the quantum target.
- A derivation verdict is: derived; conditional on named A-typed assumptions; refuted at step k (every route at k has an
  exact countermodel); Parked at step k. The step ledger (I-14) lists per step and route the premises cited, the type,
  the K-PR6 line (K-PROG for Q2), and the argument or countermodel. Every premise quoted in a ledger passes the quote
  checker (I-39).
- **Axiom-audit verdicts (§6.3, §6.4)**, per framework assumption and per axiom: *supplied by OI* (derived from C1–C4
  and the substratum structure, derivation written and reviewed); *compatible-but-added* (consistent with every control
  OI admits, not derived; named as its own condition C6, C7, … and never folded into "C5"); *contradicted by OI* (an
  O-admissible realization in the interface violates it with no added axiom that could restore it, so the CDP route is
  closed for OI). Undecided after the preregistered checks: Parked.

***

## 6. Primary candidate C5-P: purification with essential uniqueness

### 6.1 Statement

Owner's plain-language statement: "Every observable state can arise by observing part of a larger system in a pure
state. Any two such pure explanations, using the same additional system, must be connected by an allowed reversible
operation on that additional system alone." Two owner notes: (i) "pure" is §2.2's pure state, not "the observer knows
every hidden variable"; (ii) the larger-system explanations must belong to one physical theory with actual reversible
operations connecting them, not unrelated constructions reproducing the same statistics.

**Frozen formulation (owner's wording).** "C5 — Operational purification with reversible uniqueness. Every physically
preparable operational state is the marginal of a physically preparable pure state of a larger system. Any two such
purifications using the same additional system are connected by an available reversible operation on that additional
system alone." Here "operational state" includes all allowed future interventions (§2.2); "available" means physically
realizable within the proposed OI completion; "pure" means not obtainable as a nontrivial mixture of allowed states.

On the interface of §2.2 this reads:
- **(Pur-E, existence)** for every system A and physically preparable state ρ of A there are a system B in the same
  realization class and a physically preparable pure state ψ of the composite AB whose marginal on A (discarding B) is ρ;
- **(Pur-U, reversible uniqueness)** for any two such pure states ψ, ψ′ of AB with the same marginal ρ on A, there is an
  available reversible transformation of the same theory acting on B alone with (id_A ⊗ U_B)ψ = ψ′.

**Lemma T (transitivity from uniqueness) [W, pure mathematics].** Assume the trivial system I (one state; discarding a
system is the allowed operation to I) belongs to the theory (F-3). For a system A and any pure state ψ of A, discarding A
sends ψ to the trivial state, so ψ is a purification of the trivial state with purifying system A. By Pur-U, for two pure
states ψ, ψ′ of A there is an available reversible transformation U of A alone with Uψ = ψ′. So the available reversible
transformations act transitively on the pure states of every system. ∎ Consequence fixed in advance: C5-P requires
physically available reversible access between pure preparations, which is the direct link to the reversible operations
OI lacks (PLAN "Form the missing component", clause U/M [rec]). Limits, fixed in advance: Lemma T does not fix which pure
states exist, nor the full operation set (classical permutations act transitively on classical pure states); the
existence clause does the further restricting. Checkpoint I-48 (K-TRANS).

**Lemma K (cardinality) [W, pure mathematics].** Assume (i) a system A has two perfectly distinguishable states ω₀, ω₁,
and every real mixture ω_p = p ω₀ + (1 − p) ω₁, p ∈ [0, 1], is physically preparable; (ii) the theory has countably many
additional-system types B₁, B₂, …; (iii) each composite AB_k has finitely many pure operational states. Then Pur-E fails.
*Proof.* The distinguishing measurement's outcome probability is affine in the mixing weight (F-2, §2.2's mixture
definition), so it gives p and p′ on ω_p and ω_{p′}, p ↦ ω_p is injective, and the preparable states are uncountably
many. The marginals on A of pure states of the composites AB_k form a countable
union over k of finite sets, hence a countable set. Pur-E would inject the uncountable set of mixtures into that
countable set. ∎ Consequences to preregister, none a result about OI:
- a finite OI realization (finite hidden space, all distributions over it mapped affinely to statistics) has a polytope
  state space with finitely many extreme points, so (iii) holds for finite composites and real-valued probabilities do
  not escape the lemma;
- the escape routes are exactly: restrict the physically preparable mixtures; allow uncountably many system types; or
  allow infinitely many pure states in some composite. Each needs explicit justification; none is assumed;
- **Q-PREP (question).** Which mixtures are physically preparable in a finite OI realization? One hypothesis, to be
  derived from the corpus's premises and not assumed: the preparable states are the rational points with denominators
  from hidden-space sizes, a countable set (node 7's K-10: the observer's preparable boxes in 𝒜_CHSH(n) have entries in
  (1/n)ℤ [rec]; Main.md:60: a realization carries its own fixed hidden prior). If so the cardinality obstruction is
  removed while the exact purification obligation remains on those points. Status: derived / refuted / Parked, with
  the derivation or countermodel.
- **Q-FIN (question, own verdict line).** Purification with Lemma T on a polytope gives a finite reversible group acting
  transitively on the vertices, while QM's pure states form a continuum (CDP's reconstruction yields finite-dimensional
  QM with its Bloch-sphere pure states [L]). So the question: can any finite OI realization satisfy all six CDP axioms
  exactly? If not, the equivalence target must be stated either for the corpus's fixed-basis finite laws (Q_fb,
  Main.md:82) or for a limit of realizations. Status: answered with a written proof, or Parked. The audit table carries
  a "finite model" column for this (§6.4).

**Lemma A (full access with full preparations gives classical probability) [W, pure mathematics; the reviewer's
observation, with the owner's hypotheses].** Hypotheses, each to be checked on a class before the lemma is applied:
(A1) the allowed preparations of a system form the full classical simplex on 𝒞_H (every distribution, or, in the grid
reading, every preparable-weight distribution with the conclusion then restricted to that set); (A2) the interface
distinguishes distributions: for any hidden cell h there is a composed protocol of 𝒫(V) that returns h's value into a
readable cell (under unrestricted κ2 access, x ^= h; under option (B), whatever §6.10's access computation finds, as in
K-SWAP); (A3) the declared composites carry the classical product structure (composite preparations are distributions
on the product hidden space, and local operations act factorwise). Conclusion: the operational state is the
distribution on 𝒞_H, transformations are the induced stochastic maps, composites are distributions on the product, so
the operational theory is classical probability on the preparable priors; its pure states are the extreme preparable
priors; a pure state of a composite has extreme marginals; and Pur-E fails for every preparable non-extreme prior.
*Proof.* (A2) makes two preparations operationally equivalent iff their hidden distributions coincide, so states are
distributions and transformations the induced maps; (A1) makes the state set the stated simplex or grid; (A3) gives the
product form of composites, under which an extreme (point-mass) joint distribution has point-mass marginals. ∎ The
proof does not use recovery of the prior alone: recovering a state by repeated experiments is tomography, which
quantum states also allow; classicality comes from (A1) and (A3) together with (A2). Where a preparation restriction
remains (a grid, Q-PREP), the conclusion is re-checked on that set, not inherited. Consequences, stated as expected
shapes and not verdicts: on a class meeting (A1)–(A3), §6.10's answer for Pur-E is no, C5-P's R1 holds if the class
passes C1–C4, and D2 is refuted on every finite carrier with a mixed preparable state. Sub-class ℛ₁ᵃ (§6.10) is the
intended instance; the computation checks (A1)–(A3) on it and reports the result as Lemma A's instance, never as a
finding.

The exact wording of CDP's axiom is gated on PC-CDP (§6.8); the formal statement above is this node's, and a
discrepancy with the paper's wording found later is recorded as an amendment before any dependent computation.

**What the corpus supplies and does not (V-14).** Main.md:600 gives the substratum-level existence half for one law,
with completions "NOT claimed unique up to reversible relabeling"; Main.md:602 states that CDP's uniqueness is strictly
stronger. Node 4's E7 [rec] shows that bijective purifier maps do not fix purifier phases. So C5-P is not supplied by
the corpus; whether C1–C4 imply it is R1 (§6.2), which is measured.

### 6.2 R1, R2, R4 for C5-P

- **R1.** Witness sought: an O-admissible model that passes K-C1C4 on the interface and violates Pur-E or Pur-U. Candidate
  witnesses, computed exactly: CL-C4, the delay line (x, h) ↦ (h, x) of MC6 P1 [rec], which satisfies C4 exactly and so
  C1 and C3, in its classical operational theory (mc-node3:233 [Q] records "classical theory has no purification", as
  MC2 §3 states; re-derived here, not assumed); K-PR6 (its C1–C4 status computed); the §6.10 classes that pass K-C1C4.
  CL of §6.5 fails C1 and is not an R1 witness. `fiber_freedom` (Main.md:600) is non-uniqueness of completions at the
  substratum level, a different level from Pur-U (Main.md:602, §2.2's carrier/record rule), and is not a witness. R1
  holds iff some witness that passes K-C1C4 violates Pur-E or Pur-U, with the K-C1C4 printout named in the R1 cell
  (I-56).
- **R2.** Pur-E and Pur-U speak of states, composites and reversible operations of the observer interface, not of
  quantum structure. They pass R2 by inspection unless the interface definitions themselves import quantum structure,
  which the circularity review checks (§15 item 1).
- **R4.** QM satisfies purification [L: CDP 2011]. "Fits the corresponding OI realization" is question D2 (§6.6), and
  is not established by the citation.

### 6.3 CDP's framework assumptions, audited against OI

Each receives one of the three verdicts of §5, with the derivation or the countermodel. The list is this node's
reading of the OPT framework; the paper's exact wording is gated on PC-CDP.

| id | framework assumption | OI counterpart to test | expected shape (not a verdict) |
|---|---|---|---|
| F-1 | finite-dimensional systems, each with finitely many perfectly distinguishable states | P1 (finite 𝒞_V); the interface's state set | supplied for a fixed carrier, but V-11: the corpus places the reconstruction axioms' continuum endpoint beyond any fixed finite carrier, so the scope must be stated as fixed-carrier |
| F-2 | states form a convex set; transformations are convex-linear | mixtures by shared randomness (§2.2); whether every transformation of 𝒫(V) is well defined and affine on states | to be measured per class (I-38) |
| F-3 | parallel and sequential composition of systems and transformations, with a trivial system | the product carrier and the κ4 feed-forward class; P16 says OI does not alone establish one common tensor-product category | compatible-but-added at best; the step records exactly what composition structure the interface has |
| F-4 | whether the no-restriction hypothesis (every mathematically admissible effect is an allowed measurement) is assumed, and in which form | the accessible readout class κ4 is restricted by construction (configuration readouts after accessible bijections) | to be read from the paper (PC-CDP); if assumed, likely compatible-but-added or contradicted |

### 6.4 CDP's five axioms, audited against OI

Each receives one of the three verdicts of §5. Wording below is this node's paraphrase, to be checked against PC-CDP.

| id | axiom (paraphrase) | what still needs establishing in OI (owner) | OI test on the interface | finite model (Q-FIN) | expected shape (not a verdict) |
|---|---|---|---|---|---|
| X-1 | Causality | later freely chosen interventions preserve earlier outcome probabilities | O3, P4, κ4 feed-forward | can hold in a finite realization | to be derived or shown added |
| X-2 | Perfect distinguishability | the separating measurements physically exist in the realization class | the interface's state set and readouts | can hold | measured per control class |
| X-3 | Ideal compression | lossless encodings and decodings are available operations | the interface's transformations and systems | to be determined | measured; likely compatible-but-added |
| X-4 | Local tomography | local measurement correlations determine the joint operational state | P16/V-10: "It does not alone establish statistical product structure after conditioning, local tomography, or one common tensor-product instrument category." | can hold | at best compatible-but-added (owner); RQ shows it can fail while purification holds |
| X-5 | Pure conditioning | maximally resolving local measurements preserve conditional purity | the interface's pure states and readouts | to be determined | measured per control class |
| Pur | C5-P itself (Pur-E, Pur-U) | available reversible access between pure preparations (Lemma T); preparable mixtures (Q-PREP) | §6.1 on the interface | Lemma K and Q-FIN: a finite polytope with transitive finite reversible group; a continuum of pure states needs a limit | measured on §6.10's classes |

Neither hidden memory (C4) nor microscopic reversibility (P3) automatically supplies any row; each needs its own written
derivation or is typed added.

A "supplied" verdict needs a written derivation from C1–C4 and the substratum structure (P1–P4, P15), reviewed. A
"compatible-but-added" verdict names the axiom C6, C7, … in the order X-1 to X-5 as they arise. A "contradicted" verdict
needs an O-admissible countermodel inside the interface and closes the CDP route for OI.

### 6.5 Controls for C5-P, computed exactly in house

Roles are explicit per control. An R1 witness ("C1–C4 do not imply C5") must pass K-C1C4; classical negative controls
and quantum positive controls are calibrations of the implementation and cannot serve as R1 witnesses, so K-C1C4 is not
required of them.

| id | role: witness / calibration | control | construction fixed now | expectation / checkpoint |
|---|---|---|---|---|
| RQ | calibration | real-amplitude quantum theory on two rebits | states ρ± = (I⊗I ± Y⊗Y)/4, real symmetric; the product effects, spanned by the 9 product Pauli operators {I, X, Z}⊗{I, X, Z}; the joint observable Y⊗Y; a third rebit as purifier | owner-verified in another session, recomputed here: both PSD with trace 1; equal on every product effect; separated by Y⊗Y, so real QT fails X-4. Purification half, in house: each ρ± is rank 2 with eigenvalues 1/2, so it has a real purification on a third rebit, and any two such are related by a real orthogonal map on the purifier; computed exactly. Checkpoint I-40 |
| SPK-orig | calibration (R1 witness only if K-C1C4 passes on its OI embedding, measured) | Spekkens' toy theory, original (non-convex) form, under this node's combinatorial reading | ontic space ℤ₂^{2n} for n toy bits, with the standard symplectic form ω on it. Valid epistemic states: the uniform distributions on cosets v + W^⊥ for W an isotropic subspace (ω(w, w′) = 0 on W) of dimension k, 0 ≤ k ≤ n; size 2^{2n−k}. Transformations: the affine symplectic maps of ℤ₂^{2n} (they permute the family). Measurements: the partitions of the ontic space into the cosets of W^⊥ for a chosen isotropic W, outcomes the cosets. For n = 1: 6 pure states (size 2) and the fully mixed state. For n = 2: 60 pure states (size 4), 30 states of size 8, one of size 16. This rule is the node's reading, tagged as such; any discrepancy with [L: Spekkens, PRA 75, 032110 (2007)] goes through PC-SPK as an amendment before the SPK verdict is final. Built exactly, finite and rational, an epistemic-restriction theory on a classical ontic space (V-12) | tests Pur-E, Pur-U and X-1 to X-5 on the built spaces and records which hold. The owner's correction: the original states are not convex-closed, so "it satisfies purification" and Lemma K are compatible only because arbitrary mixtures are not preparable there. Literature (purification holds [L: Chiribella and Scandolo 2015]; not QM) gated on PC-SPK; the computation does not depend on it |
| SPK-conv | calibration | the convex closure of SPK-orig | the same ontic spaces with every real convex mixture of valid states admitted as a state | Pur-E fails by Lemma K: hypotheses (i)–(iii) all hold on the convex closure, so this is a theorem, and the computation confirms the lemma's instance (I-51). The pair records which form satisfies purification. This is the sharpest finite test of "purification alone is not sufficient" inside OI's class |
| K-SWAP | calibration; R1 witness candidate | access through composition: the observer reads h by waiting | one visible bit x (initially 0), one hidden bit h, fixed dynamics φ = swap(x, h); no coupling step beyond φ; readouts of x at each step. Visible sequence 0, h, 0, h, …; at step 2 the visible value is always 0 and the history predicts the next value (C4); C1–C3 hold | must-hold: the class admits it under option (B); §6.10's access-class computation reports full hidden access (operational state = hidden prior) for it; K-C1C4 passes. Role: calibration of the access computation, and an R1 witness candidate since it passes C1–C4. Checkpoint I-58 |
| K-OPSTATE | calibration | identical passive records, different operational states | one visible bit x = 0 and one hidden bit h; preparation P₀ sets h = 0, P₁ sets h = 1; the passive dynamics leaves x fixed, so both display 0 and keep displaying 0 under passive observation; the intervention x ^= h followed by readout gives 0 under P₀ and 1 under P₁ | must-hold, exactly: equal passive record laws at every horizon; different statistics under one later intervention; so P₀ ≠ P₁ as operational states (§2.2) while their records coincide. Its realization has zero coupling under the passive dynamics and fails C1: it is a control for the state definition, not a C1–C4 model. Checkpoint I-49 |
| CL | calibration | classical theory, uncoupled | a system with 𝒞_V = {0, 1}, κ1–κ4 with no hidden coupling beyond mixing; composites by product; fails C1, so a control and not an R1 witness | expected shape: Pur-E fails (mc-node3:233 [Q]); measured |
| CL-C4 | R1 witness candidate | classical theory with C1–C4: the delay line | MC6 P1's (x, h) ↦ (h, x) [rec], one visible and one hidden bit, hidden prior a realization datum with denominator ≤ 8; option-(B) access with the swap as the declared coupling step; composites by product | K-C1C4 must pass; Pur-E and Pur-U measured; the R1 witness candidate of §6.2 |
| BW | calibration | boxworld / PR | the gbit and the PR box as a two-system theory (node 7's DR(1,1) and LE(1,1) [rec]) | tested for Pur-E, Pur-U and X-1 to X-5; expected to fail at least one [L: boxworld has no purification]; measured |
| K-PR6 | R1 witness candidate (K-C1C4 measured) | §4.2 | — | its C5-P line as §4.2 |
| QM | calibration (positive) | the stabilizer instance of a qubit, as the positive control | one qubit: states the six stabilizer states and I/2; unitaries the single-qubit Clifford group (24 elements modulo phase); readouts the Pauli measurements. Composite: two qubits, states the 60 two-qubit stabilizer states, the products of a stabilizer state with I/2, and I/4; unitaries the two-qubit Clifford group; purifier of I/2 the Bell states. Field ℚ(i, √2). Closure: the instance is closed under the Clifford unitaries, Pauli readouts with conditioning, and partial trace (a partial trace of a two-qubit stabilizer state is a stabilizer state or I/2), verified by enumeration (I-57) | must satisfy Pur-E, Pur-U and X-1 to X-5 on the instance, as [L] states for QM; computed exactly; classified Reproduction as a control. A failure voids §6, so the instance is fixed to lie in the field |

### 6.6 D1 and D2, preregistered as separate questions

- **D1.** Every allowed OI + C5-P experiment (with whichever of C6… are added) has quantum statistics. Status after the
  node is one of: refuted (an OI + C5-P (+ C6…) model in the interface with non-quantum statistics, the axioms checked on
  that model); Parked (not refuted; the proof is the CDP reconstruction, which this node does not attempt); or
  established only if a reviewed [W] proof exists, which this node does not attempt.
- **D2.** Every quantum experiment in the stated scope (fixed finite carrier, finite horizon) has an allowed OI + C5-P
  realization whose operational theory is exactly QM's: its states, transformations and composites, not only its
  statistics. The response-table construction (Main.md:578) realizes statistics only. D2's refuting test is node 5's G6
  rule [rec, MC5 §7]: a protocol distinguishing the extended OI theory from QM; it can only refute. The establishing
  route is the isomorphism construction. Status: established (a reviewed construction with the interface's operational
  theory shown isomorphic to QM's on the scope), refuted (a quantum experiment with no such realization, exhibited, or
  Lemma A's consequence on a class with full access), or Parked. Under option (B) the expected shape is open.
- Neither direction is established by adopting C5-P, and a Conditional equivalence claim needs both (§13.1).

### 6.7 What C5-P settles, and recorded alternatives

- Fixed now: C5-P alone does not fix the composition structure (X-4 at best compatible-but-added, V-10); classical
  theory violates it (expected, measured); the CHSH boundary is not implied by C5-P without the other axioms (the
  reconstruction's conclusion, not C5-P's).
- **Link question L-PI (owner item 10), preregistered as a question with its own status.** Do purification-based
  operational theories carry an entropy with C5-IC's properties [L: Chiribella and Scandolo, on entropies in
  purification theories], so that C5-P ⇒ C5-IC on the interface? Status: established (a reviewed [W] constructing 𝓘
  from Pur-E/Pur-U on the interface and checking (I1)–(I10)); refuted (a C5-P-satisfying control, SPK or RQ, with no
  such measure); or Parked. Literature gated on PC-CS.
- Information–disturbance, recorded as a weaker alternative: the corpus's own statement is appendix-c:226 (V-15), which
  holds in every finite operational theory with two or more states and fixes neither the amount nor the quadratic law.
  Not pursued as primary.

### 6.8 Amendment gates for C5-P

- **PC-CDP.** The audit runs on this node's paraphrases and prints every row "provisional, pending PC-CDP" until an
  amendment quotes CDP's framework assumptions, the six axioms (purification and the five of §6.4) and the main theorem,
  with page and equation numbers, and maps each onto §6.3 and §6.4. A row whose gate is unmet classifies Parked
  (provisional) and can yield neither a final "supplied by OI", nor Emergence, nor a final C6… label: a derivation of
  this node's paraphrase of an axiom is not a derivation of CDP's axiom until the paraphrase is checked. Checkpoint
  I-53, mutant KM-27. Since `arxiv.org` was unreachable, the gate may stay unmet through the node; the rows then stay
  provisional and the C5-P class is Parked on that account.
- **PC-SPK.** Before SPK's literature claims are used in any verdict text, an amendment quotes the purification statement
  for the toy theory from its source. The exact computation does not depend on it.
- **PC-CS.** Before L-PI cites the entropy result, an amendment quotes it.

### 6.9 Verdict lines and stopping rule

Lines: R1, R2, R4 (§6.2); Q-PREP and Q-FIN (§6.1); the audit table (§6.3, §6.4) with one typed verdict per row; the
control table (§6.5); D1, D2 (§6.6); L-PI; the C5-P class (§13). The section stops when every line is decided or Parked.

### 6.10 First computation after freeze (owner's immediate mathematical target)

Construct the operational state space defined by all interventions, in the sense of §2.2, for the smallest realization
classes that have an operational mixture, and determine whether Pur-E and Pur-U can hold there. Exact arithmetic only.
- **ℛ₁, one hidden bit coupled to a one-bit observer.** Ω = {0,1}_x × {0,1}_h, plus up to two visible ancilla bits
  (point masses at 0) and up to three hidden ancilla bits (counting measure, for mixing). Fundamental step φ = identity
  (no autonomous dynamics; the hidden bit changes only through the declared coupling). Accessible bijections: every
  permutation of the configurations of the visible cells (x and the visible ancillas), selectable by a setting.
  Declared coupling steps, two sub-classes: ℛ₁ᵃ, the clean read x ^= h (Lemma A's instance; expected shape: classical
  probability on the preparable priors); ℛ₁ᵇ, the destructive read x ^= h followed by h ^= r with r a fresh hidden
  counting-measure bit per use (node 6's P5 step [rec]). Preparations: every hidden prior with denominator ≤ 8 (as
  realization data) and every preparation bijection of the hidden cells. Composites: two copies, with shared hidden
  cells allowed and declared.
- **ℛ₂, two hidden bits.** Ω = 𝒞_V × {0,1}_{h₁} × {0,1}_{h₂} with 𝒞_V = {0,1} (one-bit observer) or {0,1}² (two-bit
  observer), ancillas as in ℛ₁. Fundamental step φ = the swap h₁ ↔ h₂ (autonomous hidden dynamics). Accessible
  bijections: every permutation of the visible configurations. Declared coupling steps: x ^= h₁ (one-bit observer), x_i
  ^= h_i (two-bit observer), each in the clean form (ℛ₂ᵃ) and the destructive form with a fresh hidden bit (ℛ₂ᵇ).
  Priors with denominator ≤ 8.
- Each class's inputs (Ω, φ, accessible bijections, coupling steps, ancilla conventions, priors, composites) are printed
  with digest before §6.10 runs (I-52).
- **Outputs, per class:** the equivalence classes (states), the pure states, the transformations well defined on
  classes, the reversible ones, the composites, the preparable mixtures found (Q-PREP's data), and for each state
  whether a purification exists in the class and whether any two are related by an available reversible transformation
  on the purifier. K-OPSTATE is an ℛ₁ᵃ-type instance (with φ = identity and the clean read); it fails C1 and serves the
  state definition only. Each output is printed with its size and digest (I-38, I-50).
- This step decides nothing about QM; it fixes the objects that every later C5-P line is stated on. If 𝒫(V) as fixed
  makes the state space depend on a choice not made here, the step is Parked with that choice named.

***

## 7. Secondary candidate C5-IC: consistent information across interventions and composites

Labelled H-C5-IC. It is a candidate added condition, not an OI premise.

### 7.1 Statement, and the identities the C5 ⇒ IC proof uses

The operational theory of §2.2 admits an information quantity 𝓘(A : B) with, over all states, interventions and
composites of a declared domain 𝔇:
- (C5a) classical agreement: on classical record variables 𝓘 equals Shannon mutual information;
- (C5b) data processing: no allowed local operation on B increases 𝓘(A : B);
- (C5c) consistent composition: the identities below, not the bare phrase "obeys a chain rule";
- (C5d) nonnegativity and symmetry (nonnegativity, not strict positivity: independent systems carry zero information).

This is an existing route to IC [L: Barnum, Barrett, Clark, Leifer, Spekkens, Stepanik, Wilce and Wilke, NJP 12,
033024 (2010); Al-Safi and Short, PRA 84, 042323 (2011)], not a new theorem.

**Identities and inequalities, each a separate checkpoint (I-29).**
- (I1) definition: 𝓘(A : B | C) := 𝓘(A : BC) − 𝓘(A : C). Imposes nothing substantive.
- (I2) decomposition consistency: 𝓘(A : BC) − 𝓘(A : C) = 𝓘(AC : B) − 𝓘(C : B).
- (I3) symmetry: 𝓘(A : B) = 𝓘(B : A).
- (I4) nonnegativity: 𝓘(A : B) ≥ 0 and 𝓘(A : B | C) ≥ 0.
- (I5) data processing: 𝓘(A : T(B)) ≤ 𝓘(A : B) for every allowed local operation T on B, discarding a subsystem of a
  composite included (C5-S2 needs exactly that: dropping X_{<i} from B M X_{<i}).
- (I6) classical agreement: on classical variables 𝓘 equals Shannon information, including 𝓘(M : M) = H(M).
- (I7) classical-target bound: 𝓘(Y : M) ≤ H(M) for classical M and any system Y.
- (I8) independence gives zero: 𝓘(A : B) = 0 for independent (product) systems.
- (I9) the iterated chain rule over the first argument: 𝓘(X : BM) = Σ_i 𝓘(X_i : BM | X_{<i}), from (I1) and (I2) applied
  repeatedly ((I2) with A = X_i, C = X_{<i} gives 𝓘(X_{≤i} : BM) − 𝓘(X_{<i} : BM) = 𝓘(X_i : BM | X_{<i})).
- (I10) composite identifications used by the chain: X_i X_{<i} ≅ X_{≤i} and BM ≅ MB, as systems of 𝔇.

A construction meeting (I1) only by definition and failing (I2) does not satisfy (C5c); control K-I2 and mutation KM-18
check the checker.

### 7.2 IC from C5-IC: the chain to be checked

Setup: independent uniform input bits X = (X_1, …, X_N) for Alice; a shared resource with Alice's part A and Bob's part
B, with B and the slices of §2.2; operational no-signalling; an m-bit classical message M; Bob's guess G_i for index i.
Target: Σ_i I_Sh(X_i : G_i) ≤ 𝓘(X : B_{t₁}M) ≤ H(M) ≤ m.

| step | statement | identities and inputs | type |
|---|---|---|---|
| C5-S1 | I_Sh(X_i : G_i) ≤ 𝓘(X_i : B_{t₁}M): G_i is produced from (B_{t₁}, M) by Bob's local operation for index i. Failure mode (i) shows here if G_i's production reads Alice's cells after t₁ | (I6), (I5) | [W] |
| C5-S2 | Σ_i 𝓘(X_i : B_{t₁}M) ≤ 𝓘(X : B_{t₁}M): by (I9); then for each i, 𝓘(X_i : B_{t₁}M \| X_{<i}) ≥ 𝓘(X_i : B_{t₁}M), using (I1), (I8) for I(X_i : X_{<i}) = 0, (I5) for discarding X_{<i}, and (I10) | (I1), (I2), (I5), (I8), (I9), (I10); D-1 | [W] |
| C5-S3a | 𝓘(X : B_{t₀}) = 0: initial measurement independence of the resource cells from the inputs | (I8); D-2 | [W] |
| C5-S3b | 𝓘(X : B_{t₁}) = 𝓘(X : B_{t₀}): Alice's operationally local intervention is a local channel on B that leaves it unchanged, and B acquires no remote-input information before the message. Failure mode (i) or (ii) shows here | (I5), (I4); D-3 | [W] |
| C5-S3c | 𝓘(X : B_{t₁}M) = 𝓘(X : B_{t₁}) + 𝓘(X : M \| B_{t₁}) | (I1) | [W] |
| C5-S4 | 𝓘(X : M \| B_{t₁}) = 𝓘(XB_{t₁} : M) − 𝓘(B_{t₁} : M) ≤ 𝓘(XB_{t₁} : M) ≤ H(M) ≤ m | (I1), (I2), (I4), (I7), (I10); re-derived in step 2; any further identity becomes (I11) with its own checkpoint | [W] with [L] |
| C5-S5 | with repeated resources and protocol closure, IC excludes every box with S_max > 2√2; the PR random-access code fails IC at N = 2, m = 1 | D-4 to D-7 [L: Pawłowski et al., Nature 461, 1101 (2009)] | [W] with [EC] |

**Typed assumptions.** D-1 independent inputs (M). D-2 initial measurement independence of the resource from the inputs,
P(λ | x, y) = P(λ): O through O3 and P8 (iv); ontic parameter dependence (P9) does not violate it. D-3 locality of
Alice's intervention on the declared B: a local channel on B, and no remote-input information in B before the message;
P10 gives operational no-signalling for the wing records, and whether it gives D-3 for the declared B is the step-2
check. D-4 independent repeated resources (O under P-ctr for the product prior, A under P-dat; non-interaction A unless
derived). D-5 wirings (O, κ4). D-6 shared randomness (O, P3). D-7 n → ∞ (M).

### 7.3 The domain 𝔇 and the constructions

- **Minimum domain, fixed now.** 𝔇 must contain K-PR6 with its copies and wirings, 𝒟_LE, 𝒟_RT (§10.3) and the classical
  controls (K-C). Any exclusion of a realization from 𝔇 effected by the choice of 𝔇 is typed as an added axiom ("domain
  restriction"), and the K-PR6 line then reads "rejected only by the added axiom (domain restriction)". D-1 to D-7 are
  checked on 𝔇 before "IC derived on 𝔇" can print. "C5 established" on a domain containing no post-classical
  correlations is a non-gem (§16).
- **Constructions, neutral names, each tested rather than assumed to fail.**
  - **R-ont**, Shannon information about the entire hidden microstate of B's declared cells. Pre-registered reason it
    may fail: it includes distinctions the observer cannot access. Checks: K-ONT (two O-admissible realizations with
    identical accessible record laws but different 𝓘_ont; a positive outcome means 𝓘_ont is not a quantity of the
    operational theory); C5-S3b on K-PR6 with B = Bob's box half and its hidden cells, recording the failure mode.
  - **R-acc**, accessible information: max over single admissible readouts R of B of I_Sh(A : R). Pre-registered
    reason it may fail: (I2) or (I9) need not hold. Check K-ACC: a triple in 𝒟_LE or 𝒟_RT violating (I2). Quantum
    locking [L: DiVincenzo, Horodecki, Leung, Smolin and Terhal, PRL 92, 067902 (2004)] concerns quantum theory, so
    without an exact OI countermodel the construction is Parked, not refuted.
  - **R-pq**, Shannon information of a cross-protocol regional quotient: hidden data of B's cells modulo distinctions
    that no accessible protocol on B reveals. This is a new construction (typed A unless derived); P21 is its
    single-law ingredient and supplies neither the regional nor the cross-protocol form (V-14). Point judged:
    compatibility of quotients of composites with quotients of parts ((I2), (I10)) and (I5) under local operations.
  - **R-ms**, measured information from the entropies of B's admissible readouts [L: Short and Wehner, NJP 12, 033023
    (2010)]. Point judged: (I2) and (I9); [L] reports they can fail in general theories.
- **C5-0.** An OI-admissible PR-box model obstructs C5-IC only if it also satisfies D-1 to D-7 with B fixed as §2.2 fixes
  it. K-PR6-C5 checks those on K-PR6 itself. If they fail, the failing step and mode are recorded and K-PR6 is not an
  obstruction.

### 7.4 Where a hidden-state construction can fail, named in advance

Initial measurement independence (D-2; IC-D5a; C5-S3a) is P(λ | x, y) = P(λ), and holds on branch (a). Ontic parameter
dependence is b = b(x, y, λ). No step fails on the ground that branch (a) breaks independence of the shared resource.
A hidden-state construction can fail because (i) an operationally local intervention is not a local channel on the
declared B (shows at C5-S1 or C5-S3b; at IC-D3 or IC-D5b), or (ii) B acquires remote-input information before the
message (C5-S3b; IC-D5b). The ledger names B, the slice, the step and the mode.

### 7.5 H-C5-IC's verdict table (an existence claim), and what it settles

| finding | verdict printed | class (§13) |
|---|---|---|
| a construction (any of R-ont, R-acc, R-pq, R-ms, or an amended one) fails a required identity on 𝔇, or fails C5-S3b for its B on a model whose operational B satisfies D-3 | "construction X fails", that construction only | no class by itself |
| K-ONT positive | "R-ont is not a quantity of the operational theory" | as above |
| no construction among the preregistered and amended ones meets every requirement on 𝔇, and no obstruction is shown | "Undetermined" | Parked (gap named); never Failure |
| an OI-admissible model in 𝔇 admits no measure meeting (C5a)–(C5d) and (I1)–(I10), and D-1 to D-7 are checked to hold on that model | "OI does not imply C5-IC", with the model. This is R1 for C5-IC | Conditional for the C5-IC line (R1 holds), provided R2 and R4 hold; the correlation lines read Conditional on C5-IC |
| a construction meets every required property on 𝔇 ⊇ 𝔇_min | "C5-IC established on 𝔇", with 𝔇 and the interface printed | Failure for the C5-IC line (R1 fails: OI implies it on 𝔇, so no gap is bridged); the IC derivation line becomes eligible for Emergence on 𝔇 after D-1 to D-7 on 𝔇 and the circularity review |

- **Joint case.** "C5-IC established on 𝔇" and "OI does not imply C5-IC" can both hold only if the obstruction model lies
  outside 𝔇; since 𝔇 ⊇ 𝔇_min ∋ K-PR6, that happens only through a domain restriction, which is typed as an added axiom
  and printed with both verdicts.
- **Precedence inside the line.** An established obstruction decides "OI does not imply C5-IC" whatever the undecided
  construction routes show; "C5-IC established on 𝔇" decides the line on 𝔇 whatever the other routes show. Parked
  applies only when an undecided item prevents a decision.
- **What C5-IC settles, fixed now.** Excluding PR boxes: yes, wherever D-1 to D-7 hold. The CHSH upper bound: yes, with
  protocol closure. Achievability of quantum boundary values in OI: not settled; needs a construction. The
  interference–path trade-off: not established by this argument. Full operational QM: not established. Classical
  theory satisfies C5-IC (K-C5+), so R3 fails for C5-IC alone: a bound cannot show OI reaches the quantum boundary.

### 7.6 Verdict lines and stopping rule

Lines: the table of §7.5; R1–R4 for C5-IC (R1 from the table; R2 by inspection and the review; R3 from K-C5+ and the
classical control; R4 from QM's satisfaction of IC [L], with the OI fit as D2); the K-PR6 line; the class. Stops when
each is decided or Parked.

***

## 8. Reference row: node 5's control condition

Statement [Q, mc-node5/NODE.md:28–29]: "Relative to `SourcedOI`, exact QM holds iff phase-free richness (PFR) holds, one
continuously driven pair per level [AT]", with the available operations described, as GR.md:216 (iv) states, by "every
finite unitary on every composite is available", and `SourcedOI`/`StructurallyClosed` taken on the extended theory
(mc-node5:33–36). The owner's summary, checked against the record: the condition gives the formal equivalence inside an
operational framework that already describes operations as complex matrices. R2 verdict fixed in advance from the
record: the condition is stated on unitaries and the Lie algebra they generate (GR.md:250–258 [rec]), so it names the
quantum operations rather than a property of observation; it fails R2 and is classified Reproduction as a reference
row. Node 5's G6 rule (no distinguishing prediction, MC5 §5 [rec]) is reused as D2's test. Nothing is computed for this
row; it is a record check (I-41).

***

## 9. Interference as a diagnostic control (Q2, shortened)

Kept only as a control for R2/R3 and K-PROG. It decides no correlation line (§11.4).

### 9.1 The mathematics fact

For equiprobable paths (verified operationally by equal detection rates with each single path open) and a marker
readout R with conditional laws p₀, p₁: D_R = ½ Σ_r |p₀(r) − p₁(r)|, F_R = Σ_r √(p₀(r) p₁(r)).

**Lemma.** D_R² + F_R² ≤ 1. *Proof* [W]. With s_r = √p₀(r), t_r = √p₁(r), Σ s_r² = Σ t_r² = 1, |p₀(r) − p₁(r)| =
|s_r − t_r|(s_r + t_r); Cauchy–Schwarz gives Σ_r |s_r − t_r|(s_r + t_r) ≤ √(Σ(s_r − t_r)² · Σ(s_r + t_r)²) =
√((2 − 2F_R)(2 + 2F_R)) = 2√(1 − F_R²). ∎ [L: Fuchs and van de Graaf, IEEE Trans. Inf. Theory 45, 1216 (1999)]. K-LEM
re-checks the factorization and both expansions symbolically, plus the exact rational instance p₀ = (9/25, 16/25), p₁ =
(16/25, 9/25). Q2's verdicts are suppressed until K-LEM passes (I-42).

### 9.2 Definitions inside the substratum

- Path by blocking: p_j^R is the law of readout R with only path j open, same preparation and marker coupling (V-7).
- V from unconditional counts at K = 12: V := V₁₂ = (P_max − P_min)/(P_max + P_min) over θ ∈ Θ₁₂ at port 0, with θ₀ ∈ Θ₁₂
  required of every realization used; V_K for K ∈ {4, 6, 8} printed as sensitivity rows. Number field for exact
  comparison: ℚ(√2, √3). V is never set equal to an overlap or to F_R.
- D over admissible readouts: D = max over admissible marker readouts R (configuration readouts after accessible
  bijections on the marker and ancillas, κ4; the set enumerated and its size printed) of D_R. Path information available
  in the marker counts whether or not anyone reads it [L: Englert, PRL 77, 2154 (1996)]; concealing a record does not
  restore interference; inaccessible ontic knowledge is not used.
- Eraser fringes (conditioned on a marker outcome) are computed separately as K-ERASE and never enter V.
- Class 𝒟_IF: two- and three-path interferometers with response-table realizations (𝒟_IF-RT) and hidden-memory,
  context-dependent realizations (𝒟_IF-HM), hidden carriers up to 2^12, marker registers up to 4 bits, phase alphabet
  Θ₁₂. No reference-update subclass is used.

### 9.3 The bridge, as an inequality

- **B-VF, to be derived, never assumed:** V ≤ F_R for every admissible R, so V ≤ inf_R F_R; with the lemma at the R*
  maximizing D_R, D² ≤ 1 − F_{R*}² ≤ 1 − V², so V² + D² ≤ 1.
- In quantum theory, for the balanced unconditional two-path setup, V ≤ F_q(ρ₀, ρ₁) = inf over marker POVMs of F_R (root
  fidelity, attained by some POVM). The optimal readout attains the fidelity bound; it does not make the visibility
  equal to it. A pure joint path–marker state is sufficient for V = F_q and is not necessary (an uncoupled marker I/2
  with path |+⟩ gives V = F_q = 1). Node 8 asserts no saturation (I-33); the boundary witnesses of §9.4 are chosen
  pure-marker points, which is a description of the witnesses, not a necessity claim.
- Defining V to equal the overlap, or inserting quantum amplitudes, assumes the bridge (Reproduction).

### 9.4 Q2 decision rule and controls

A candidate restriction (from §6 or §7, entering as a named added axiom unless derived) explains complementarity iff:
it implies B-VF on 𝒟_IF by a reviewed [W] with [EC] instances; it rejects every K-PROG variant (§4.3); boundary witnesses
with V = c and D = √(1 − c²) for c ∈ {0, 1/2, 1/√2, 1} are constructed in its admitted class under §4.3's admission
semantics (ℚ(√2, √3)); and the controls behave as stated:
- CC-hm: hidden-memory model with the path copied to a marker and context-dependent dynamics, V = 1, D = 1 at K = 12;
  its C1–C4 status computed exactly (K-C1C4);
- CC-w: classical two-path wave with polarization marking from exact Jones vectors e₀, e₁; V from intensities, D the
  trace distance of the normalized coherency matrices; the expectation V² + D² ≤ 1 with equality for fully polarized
  light rests on the in-house computation, not on literature;
- CC-q: quantum path–marker model from density matrices, equality at pure marker states [L: Greenberger and Yasin,
  Phys. Lett. A 128, 391 (1988); Englert 1996];
- CC-dec: path |+⟩, marker I/2, coupling I on path 0 and Z on path 1: F_R = 1 for every readout, D = 0, V = 0; the bound
  is reported as not attained;
- K-ERASE: CC-q at c = 0 with the marker read in the conjugate basis: unconditional V = 0, conditional visibilities 1;
- K-FL+: a quantum Mach–Zehnder from 2 × 2 matrices passes the three discriminators; K-FL−: a triangle-wave pattern with
  the same values at K = 4 fails the cos law at K = 12, and a classical three-path hidden-memory model with 𝒮₃ ≠ 0 is
  detected;
- K-VD: V, D_R and F_R by two code paths on a biased two-port splitter (reflectivity 1/3) with a two-bit marker of fixed
  conditional laws.

Verdict line Q2: the class of each candidate restriction with its K-PR6 and K-PROG lines, and the statement of what it
can conclude: a derived B-VF shows OI + the restriction enforces a trade-off that classical waves also satisfy (CC-w),
so it is not QM-selective; a countermodel shows C1–C4 (or the restriction) do not enforce it and names the premise
Main.md:666's which-path statement would need.

***

## 10. The IC and ML derivation lines (the approved questions; R1 tests)

### 10.1 IC from OI premises (3A)

- **IC-Sh.** Σ_{i=1}^{N} I(x_i; G | b = i) ≤ m, Shannon information in bits, N independent uniform input bits x_i, an
  m-bit message, shared resources (corpus-native measure, C3 and P5k; Rényi-2 and min-entropy rows are sensitivity
  rows).
- **IC-G**, distinct and amendment-gated (PC-GM): Gachechiladze and Miklin [L-c] derive the TLM boundary from a
  generalized IC with correlated inputs and full receiver transcripts; the exact-selection result concerns the two-setting
  binary correlator region, zero marginals included; it is not a reconstruction of arbitrary quantum experiments.
- **IC on boxes.** IC-excluded iff a protocol in 𝒫 (P-vD: N = 2, m = 1, K-PR6-RAC's protocol; P-RAC(n), 1 ≤ n ≤ 12;
  each optionally after the twirl, O-admissible by [W]) gives a certified excess; IC-admitted iff local (classical IC
  [W]) or exhibited quantum (quantum IC [L], a control; the verdict text says that (ii-Q) for the IC line holds by the
  quantum-IC theorem, which is mathematics, not OI evidence); otherwise undetermined.
- **Derivation.** B = B_{t₁} as §2.2 fixes it (IC-ont); IC-rec takes Bob's records R_B.

| step | conclusion | premises | type |
|---|---|---|---|
| IC-D1 | H(M) ≤ m | P1, P15 (O4) | [W]; [AT] `cmi_le_log_card` |
| IC-D2 | every record variable and B_{t₁} is a function of the microstate; Shannon information defined for all | P3, P4, P15 | [W] |
| IC-D3 | between t₁ and t₂, G is a function of (M, B_{t₁}, b) alone, so I(x_i; G \| b = i) ≤ I(x_i; M, B_{t₁} \| b = i). Mode (i) shows here | P7, P11; data processing | [AT] `cmi_le_of_deterministic`; [W] |
| IC-D4 | Σ_i I(x_i; M, B_{t₁} \| b = i) ≤ I(x⃗; M, B_{t₁}) | chain rule [W]; independence of the x_i (B-2, D-1); P8 (iv), O3 | [W] |
| IC-D5a | I(x⃗; B_{t₀}) = 0 | O3, P8 (iv); B_{t₀} as §2.2 | [W] |
| IC-D5b | I(x⃗; B_{t₁}) = 0: the record-limitation step. Modes (i), (ii) show here | routes σ-cone, σ-ons, σ-cap, σ-C5P, σ-C5IC | to be decided |
| IC-D5c | I(x⃗; M, B_{t₁}) ≤ I(x⃗; B_{t₁}) + H(M) | Shannon identities, P5k | [AT] with [W] |
| IC-D6 | on i.i.d. copies with wirings, IC-Sh excludes S_max > 2√2 and admits TB | [L: Pawłowski et al. 2009] replayed: the twirl [W], P-RAC closed forms [W], the binary-entropy bound [L, mathematics], exact algebra at 2E² = 1 | [W] with [EC] |

- **Routes at IC-D5b (and IC-D3).** σ-cone: the cones do not meet before t₂ (P7, P8 (i), (iv)); judged on whether any
  step between t₀ and t₂ reads Alice's cells and writes into B or into G's inputs; K-PR6-RAC first. σ-ons: P10 on the
  wing records gives I(x⃗; R_B) = 0; judged on whether R_B may replace B at IC-D3 (P11). σ-cap: a capacity bound (P1,
  C3, P5k) on the cells through which x⃗ reaches B or G; judged on whether OI fixes that number; V-3 tested here.
  σ-C5P: C5-P as a named added axiom, through L-PI if established. σ-C5IC: C5-IC as a named added axiom, through C5-S3.
- **Assumptions.** B-1 Shannon measure; B-2 independent uniform inputs (M); B-3 m classical bits (O); B-4 independent
  copies (O under P-ctr, A under P-dat); B-5 wirings (O); B-6 twirl randomness (O); B-7 n → ∞ (M); B-8 the conclusions
  of IC-D3 and IC-D5b (to be derived; otherwise A; its conditional admitted set is computed, since for a
  response-complete B with deterministic dynamics it may coincide with ontic parameter independence, which
  Main.md:361–365 bounds by 2); B-9 response-completeness (O, P11).
- This line is R1's test for C5-IC: "OI does not imply IC" is witnessed exactly by K-PR6-RAC if the derivation fails at
  IC-D5b with K-PR6-RAC as countermodel; "OI implies IC" would make R1 fail for C5-IC.

### 10.2 ML from OI premises (3B)

- **ML-NW**, coded from the macroscopic covariance: over N i.i.d. copies, normalized count fluctuations have Gaussian
  limits with Var F_{A,a} = P(0|a)(1 − P(0|a)) and Cov(F_{A,a}, F_{B,b}) = P(00|ab) − P(0|a)P(0|b); P satisfies ML-NW iff
  some same-wing covariances make the 4 × 4 matrix PSD. The NPA level-1 moment matrix is a second code path (K-ML); the
  Schur complement makes ML-NW ⇔ Q1 an in-house box-level statement [W].
- **ML-F2**: one record bit per wing per run by thresholds (one per wing and setting, universally quantified) on the
  fluctuations under the fixed-register reading L1-b of Lemma 1.
- **Derivation.** ML-D1 finite record register (P1, P2, P4, P15) [W]; ML-D2 count per port at resolution N^{1/2} (P1;
  A-1, A-2) [W]; ML-D3 i.i.d. copies (P3, P12; A-3) [W]; ML-D4 the limiting macroscopic records admit a Bell-local model,
  the record-limitation step, routes ρ-cone (P7, P8 (i), (iv) applied to macroscopic records, judged against P9; K-PR6
  with N copies first), ρ-geom (P13, judged on whether "typical local neighborhoods" concerns the copies the record sums
  over, each with its own long edge), ρ-read (P15: a joint distribution exists per setting pair; judged on whether one
  follows across setting pairs), ρ-C5P, ρ-C5IC (as named added axioms); ML-D5 Gaussian limit and ML-D4 ⇔ PSD completion
  (CLT [L, mathematics], joint models for Gaussian marginals [W], Schur [W]); ML-D6 PSD ⇒ S_max ≤ 2√2 (exact level-1 sum
  of squares [EC, rec]).
- **Assumptions.** A-1 count map (A unless derived); A-2 α = 1/2 (A; rows at 1/3, 2/3 decide nothing; if its only
  justification is that it makes quantum correlations local [L-s: Gallego and Dakić, PRL 127, 120401 (2021), v1], the
  reading is Reproduction at best); A-3 i.i.d. (O under P-ctr, A under P-dat; load-bearing for quantum admission, since
  non-i.i.d. quantum correlations violate ML [L-s]); A-4 the limit with observers growing with N (M; O under L1-a); A-5
  CLT (M); A-6 the locality claim (to be derived; otherwise A).

### 10.3 Countermodel classes

𝒟_LE: LE(n, k) with N copies, n ≤ 12, N ≤ 6 exactly, with [W] for N → ∞. 𝒟_gate: node 7's long-edge gate class (256
Boolean F, control register n ≤ 12). 𝒟_RT: response-table realizations of 𝒜_CHSH(n), n ≤ 12, with branch-(a) long
edges. IC games embed N ∈ {2, 4}, m = 1. Every realization goes through the condition-O engine.

### 10.4 Verdict lines and stopping rule

Per reading of 3A and 3B, separately: derivation verdict (§5), (a) (§11.1), the (b) lines, the K-PR6 line, the class.
Neither sub-line's result is used in the other's derivation. Stops when the record-limitation step is decided or Parked
for every route and the clauses are evaluated.

***

## 11. Composites: (a), (b-corr), (b) and the branch-4 tests

### 11.1 Outcome (a), Tsirelson's bound

Inherited in structure from MC7 PREREG §4, tightened to A1 (§1), evaluated on each line's admitted set as formalized.
- Scenario: binary settings and outcomes, correlators E(a, b), S_max over the eight orientations. Named boxes: PR
  (K-PR6's box); TB, P(x, y | a, b) = (1 + (−1)^{x⊕y⊕ab}/√2)/4 in ℚ(√2), realized by the maximally entangled two-qubit
  state with A₀ = Z, A₁ = X, B₀ = (Z + X)/√2, B₁ = (Z − X)/√2; T1 = LE(5, 2), correlators (1, 1, 1, 1/5), post-quantum
  [rec, K-7]; LE(√2 − 1), S_max = 2√2, post-quantum; the 16 local vertices; NS.
- Family stage over LE(n, k) (n ≤ 100), LE(w) for real w, and T1: (i) no admitted member has S_max > 2√2 (for IC, every
  such member certified IC-excluded); (ii-S) S_max = 2√2 attained exactly by an admitted member, or else by a box of
  NS; (iii) every classical record law admitted.
- Follow-up on NS, iff the family stage passes: (F1) sup S_max ≤ 2√2 over admitted boxes, reviewed [W] with [EC]
  instances (𝒜_CHSH(n), n ≤ 12; node 7's grid, n ≤ 100); (ii-Q) TB admitted exactly; (iii-𝒜) every local box admitted.
  For IC, admission means certified IC-admission; an undetermined box with S_max > 2√2 makes (i) or (F1) incomplete.
- (a) is established iff all six clauses hold. Classes are never reduced after a result.

### 11.2 Composite routes

- **Q4-VR.** A box is VR-admitted iff its correlator matrix has unit vectors u_x (x only), v_y (y only) in a real
  inner-product space with E_xy = ⟨u_x, v_y⟩. VR ⇒ S_max ≤ 2√2 by Cauchy–Schwarz [W]; VR is exactly the quantum
  correlator set for binary outcomes (quantum ⇒ VR in house [W]; VR ⇒ quantum [L: Tsirelson 1980, 1987]). A joint
  distribution of all records restores 2 [L: Fine 1982] (K-LHV, must under-generate). Routes: V-K (P18: vectors in ℓ²(Ω)
  from √μ; judged on whether u_x can depend on x alone under P9); V-W (P17, P16: a common local operator representation
  is Q-typed unless derived); V-M (via 3B with its own step V-M-1); V-C5P (C5-P with the C6… named, through D1 if
  established). Each carries a K-PR6 line.
- **(b-corr)**: the admitted correlator set equals the quantum correlator set, by a reviewed proof of both inclusions,
  [L] dependence printed. ML and VR can at most reach (b-corr).
- **(b)**: the admitted set of boxes, marginals included, equals Q, by a reviewed proof of both inclusions. Finite tests
  only refute it. (b-corr) is never reported as (b) (I-27). ML-NW = Q1 ⊋ Q with nonzero marginals [L: Navascués,
  Pironio and Acín, NJP 10, 073013 (2008)]; IC's admitted set is unknown [L], so (b) for IC is reported as exclusions.

### 11.3 Branch-4 tests, on every line that established (a), and on K-P

- (b1) zero marginals: T1, the LE members with 0 < w ≤ √2 − 1, the zero-marginal boxes of 𝒜_CHSH(n), n ≤ 12, with
  certified TLM violation [L: Tsirelson 1980; Landau 1988].
- (b2) nonzero marginals: an exact point in Q1 outside Q (exact PSD moment matrix; exact rational NPA 1+AB dual), searched
  over tilted CHSH I_β, β ∈ {1/2, 1} [L: Acín, Massar and Pironio 2012] and 𝒜_CHSH(n), n ≤ 12; else incomplete.
- (b3) chained, three settings: I_ch = E(0,0) + E(1,0) + E(1,1) + E(2,1) + E(2,2) − E(0,2) ≤ 3√3, the bound 2n cos(π/2n)
  at n = 3 certified in house by an exact sum-of-squares decomposition [W, EC]; if the certificate is not found, the
  bound is [L: Wehner 2006] and the line is flagged.
- (b4) the Q1 points violating IC [L-s: Cavalcanti, Salles and Scarani, Nat. Commun. 1, 136 (2010)], gated on PC-CSS
  (an amendment quoting their construction), else "not run (precondition unmet)".
- (b5) Pompili and Weilenmann [L-c]: (b5-IC) each point against every IC-type line; (b5-C5) the full C5-IC requirements
  on the model, with a declared completion (state space, transformations, composites). If the paper fixes a completion,
  the PC-PW amendment quotes it; if not, the amendment declares one, typed A, before execution, and the (b5-C5) verdict
  is scoped to it. The paper reportedly states that its proof needs no entropy with every property of the
  general-theory IC proof, so these sets obstruct IC from selecting QM without settling full C5-IC.
- (b6) POM: node 7's bound and witness [rec]; "silent" for lines not addressing POM. (b7) bipartite scope only [L:
  Gallego, Würflinger, Acín and Navascués 2011].
- **Gates.** PC-PW, PC-GM, PC-CSS, PC-CDP, PC-SPK, PC-CS: each prints "not run (precondition unmet)" until its amendment
  exists; I-28 enforces reading only from a digest-printed amendment file.

### 11.4 The step from single-system results to composites

A complementarity result does not supply composite structure (nonlocality connects to measurement uncertainty and
steering [L: Oppenheim and Wehner, Science 330, 1072 (2010)]). A line using a Q2 result toward composites carries its own
step with named premises and its own K-PR6 line; otherwise Q2 results read "does not bear on correlation limits".

***

## 12. The postdiction requirement (adoption criterion)

Reproducing established QM is a legitimate success; an equivalence proof need not predict a deviation. The
additional-consequence requirement is therefore a postdiction requirement, a verdict-generator clause separate from
mathematical correctness: OI + C5 (with its named added axioms) must derive at least one established quantum feature
not used to motivate C5 and beyond the CHSH target. Candidates that CDP derive [L]: no-cloning,
no-information-without-disturbance, teleportation. The feature must be derived in the node's ledger (a reviewed [W] from
the axioms with OI's premises), not assumed, and its derivation's failure must have been possible (the feature is not
entailed by the motivation of C5). If the full equivalence (D1 and D2) is proved, the requirement is met automatically;
it bites only for partial results, where the line reads "Conditional; postdiction requirement unmet" (the owner's
earlier text "additional-consequence requirement unmet" names the same clause). It need not contradict QM. Checkpoint
I-34; mutation KM-19.

***

## 13. Classification under the redirect

### 13.1 Classes

Each verdict line gets exactly one class, computed from its measured clauses, ledgers and countercontrol lines.
- **Conditional equivalence on {C5-P (or C5-IC), plus the added axioms named}, on a declared domain, both directions
  proved.** The top target: D1 and D2 established on the domain, with every added axiom (C6…) named and typed A, R1–R4
  as the scorecard records, and the postdiction requirement met automatically. The equivalence domain is D2's scope: a
  fixed finite carrier and finite horizon, or, after Q-FIN, the corpus's fixed-basis finite laws Q_fb or a stated limit
  of realizations. It is declared, with digest, before step 3 of §19 (I-55).
- **Conditional** (the general case of a result requiring a new axiom): R1 holds, R2 passes, R4 holds, R3 is neither
  refuted nor proved, or is proved only with named added axioms, on a declared domain; the K-PR6 line names an O-typed
  premise or a named axiom; the postdiction status printed (§12).
- **Emergence.** Only for an axiom actually derived from C1–C4 (an audit row "supplied by OI" whose PC-CDP gate is met,
  or a derivation line "derived" with every assumption M or O, the K-PR6 line naming an O-typed premise holding on
  branch (a), and the circularity review passed). A provisional audit row never yields Emergence (I-53).
- **Reproduction.** R2 fails (circular: the condition names quantum operations or states), or a Q-typed input is used,
  or K-PR6/K-PROG is rejected only by a Q-typed premise, or a parameter or fringe amplitude is fitted ("retrodiction").
- **Failure.** R1 fails (C1–C4 already imply the condition on the domain, so no gap is bridged); or R4 fails (QM violates
  it, exhibited exactly); or R3 is refuted (an OI + C5 model with non-quantum statistics, the axioms checked on that
  model); or, for derivation lines, a required clause fails ((i), (ii-S), (iii), (F1), (ii-Q), (iii-𝒜)); or K-PR6 "not
  rejected" on a correlation route; or K-PROG not rejected on a Q2 route. Sub-labels as before, with the premise named.
- **Parked.** Undetermined after the preregistered routes: a named formalization gap, an unmet amendment gate, an
  incomplete required check (range stated), an unresolvable checklist item, or an undecided route that prevents a
  decision.

**Precedence.** Parked, only when the undecided item prevents a decision (an established obstruction, or an established
result on a domain, decides its line whatever else is undecided); then Failure; then Reproduction; then Conditional
(with the equivalence label when both directions are proved); then Emergence. For every Failure and Conditional the node
states the step and premise responsible. The classifier reads only measured clauses, ledgers, countercontrol lines and
the recorded circularity verdict; no class is a literal; Emergence and Conditional print as provisional until the review
is recorded.

### 13.2 The R1–R4 scorecard (deliverable (e))

| candidate | R1 independence | R2 physical meaning | R3 sufficiency | R4 reverse compatibility |
|---|---|---|---|---|
| C5-P | witness from §6.2 (CL, K-PR6, fiber freedom), exact | inspection and review (§6.2) | the audit (§6.3–§6.4), the controls (§6.5), D1 (§6.6), Q-FIN (finite realizations against a continuum of pure states); not proved by this node; refuted if a control satisfying C5-P and the audited axioms is non-quantum | [L: CDP] for QM satisfying it; D2 for the OI fit |
| C5-IC | §7.5's table; K-PR6 if D-1 to D-7 hold on it | inspection and review | K-C5+: classical theory satisfies it, so R3 fails for C5-IC alone | QM satisfies IC [L]; D2 |
| node 5's condition | [rec] necessary and sufficient relative to `SourcedOI` | fails: stated on unitaries (§8) | [AT] equivalence | [AT] |

Each cell is filled from the measured line it names and printed with that line's checkpoint; the scorecard is generated,
not written (I-43).

### 13.3 The axiom ledger

Every audit row's verdict (supplied / compatible-but-added as C6, C7, … / contradicted / Parked) is printed with its
derivation or countermodel; the set of added axioms accompanying every Conditional label is read from this ledger.

### 13.4 H-X decision rule

- Supported: every premise examined in §10's routes yields "no cross-intervention restriction" with an exact countermodel,
  and no route's K-PR6 line names an O-typed premise that holds on branch (a) while admitting K-Q.
- Refuted: some route's K-PR6 line names such a premise, with K-Q and K-C admitted by the same route.
- Otherwise undetermined. The status is scoped to the routes examined.

***

## 14. Controls and mutation controls

Every control runs before any verdict of the section it serves; a verdict over a failed control is void. A missing
dependency (sympy, python-flint or mpmath) fails the dependent control, with the version printed when present (I-37).

| # | control | serves | type | expectation |
|---|---|---|---|---|
| K-PR6 | §4.2's construction through the condition-O engine, wing records q; r; each route's line | all | must-hold replay; line per route | replays |
| K-PR6-RAC | Σ_y I(x_y; G \| y) = 2 on m = 1, exactly | §7, §10, §11 | replay; rejected by every IC line with the premise named | replays |
| K-PR6-C5 | D-1 to D-7 on K-PR6 with B = Bob's box half (§2.2) | §7 | measured | reported |
| K-PROG | PROG-0, PROG-B, PROG-3, PROG-c through the engine; V = 1, D = 1 at K = 12 for PROG-0 | §9 | replay; line per Q2 route | replays |
| K-9 | condition O on every realization | all | must-hold | holds |
| K-C1C4 | the coin–die example (book ch01 §1.5) satisfies C1 and C4; a Markov chain fails C4; a zero-coupling realization fails C1; the tape-and-ledger fair coin satisfies C1–C3 and fails C4 [rec] | §6, §9, §10 | must-hold both ways | as stated |
| K-IF | the interface of §2.2 computed on CL, QM (qubit), SPK, BW, K-PR6: states, pure states, transformations well defined on classes, reversible transformations, composites; sizes printed | §6, §7 | must-hold (well-definedness) or Parked per class | reported |
| RQ | the two-rebit control of §6.5 | §6 | must-hold: PSD; equal on the span of the 9 product Pauli operators; separated by Y⊗Y; purified on a third rebit with orthogonally related purifications | as stated |
| SPK-orig, SPK-conv | the toy theory in both forms, built exactly; Pur-E, Pur-U, X-1 to X-5 tested on each | §6 | measured; the pair records which form satisfies purification | reported |
| K-OPSTATE | §6.5's two preparations: equal passive laws, separated by x ^= h | §2.2, §6 | must-hold | holds |
| K-TRANS | Lemma T on CL-C4 and the QM instance: the hypothesis (Pur-U on the control, computed) and the conclusion (transitivity of the reversible transformations on the pure states) both checked | §6 | must-hold where Pur-U holds; where Pur-U fails the lemma is inapplicable and the row says so | as stated |
| CL-C4 | the delay line, K-C1C4 passing, Pur-E and Pur-U measured | §6 | measured | reported |
| CL, BW, QM | the controls of §6.5 | §6 | measured; QM must satisfy all | reported |
| K-LEM | the lemma's factorization and expansions symbolically; the exact instance of §9.1 | §9 | must-hold; Q2 suppressed until it passes | holds |
| K-VD | V, D_R, F_R by two code paths on the named splitter model | §9 | must-hold | holds |
| CC-hm, CC-w, CC-q, CC-dec, K-ERASE, K-FL+, K-FL− | as §9.4 | §9 | as stated | as stated |
| K-ONT | two O-admissible realizations with identical accessible laws; 𝓘_ont compared | §7 | countercontrol for R-ont | reported |
| K-ACC | search for an (I2) violation of 𝓘_acc in 𝒟_LE and 𝒟_RT | §7 | countercontrol for R-acc | reported |
| K-C5+ | Shannon information on a classical interface satisfies (C5a)–(C5d), (I1)–(I10) and IC | §7 | must-hold | holds |
| K-I2 | the fixed measure 𝓘′(A : B) := κ(A)·I_Sh(A : B), κ(A) = 2 for a composite first argument and 1 otherwise, with (I1) by definition: it violates (I2) and (I3) on classical triples | §7 | must be flagged as failing (C5c) | flagged |
| K-1, K-7 | node 7's families; LE quantum only at w = 0 | §10, §11 | must-hold | hold |
| K-2, K-3 | PR (LE(1,1)) and LE(2,1) | §10, §11 | must-fail admission under ML-NW, ML-F2, IC, VR and K-P | rejected |
| K-C | classical admission: local vertices, LE at w = 0, rational mixtures | §10, §11 | must-hold | admitted |
| K-Q | quantum admission: TB in ℚ(√2), node 7's v = 12/17 point | §10, §11 | must-hold under ML-NW, IC, VR | admitted |
| K-ML | ML-NW's two code paths agree (local vertices, PR, TB, T1, LE(n,k) n ≤ 12, isotropic v ∈ {j/24}, 𝒜_CHSH(n) n ≤ 6) | §10 | must-hold; disagreement voids ML | agree |
| K-IC | P-vD on PR gives 2 > 1; no protocol exceeds m on local vertices; TB stays ≤ 1 for n ≤ 12; the twirl preserves S_max on 100 fixed rational boxes | §10 | must-hold | holds |
| K-SOS | exact level-1 sum of squares for CHSH; the chained certificate for (b3) | §10, §11 | must-hold | holds |
| K-D+ / K-D− | a valid data-processing step closes; "on branch (a), Bob's readout at fixed microstate does not depend on Alice's setting" is refuted in 𝒟_LE | all | must-hold / must-fail | as stated |
| K-VR± / K-LHV / K-Kq | TB has exact vectors, PR does not; the joint-distribution principle under-generates; in-house quantum ⇒ VR | §11 | as stated | as stated |
| K-10 | node 7's reduction, confirmed in CI (run 39529498293, owner-reported); no clause decided through it, by choice | §11 | reported | reported |
| K-P | the quantum set as a principle (node 7's PC-3b) | classifiers | passes (a), (b-corr), (b1); Reproduction | passes |
| K-N1 to K-N8 | synthetic principles: S_max ≤ 3 fails (i); S_max ≤ 2√2 + 1/100 fails (i) at A1 and passes A2 rows; S_max ≤ 2 fails (ii-S); excluding LE at w = 0 fails (iii); admitting only S_max < 2√2 fails (ii-S), (ii-Q); S_max ≤ 2√2 on every box fails (b1); Q1 membership passes (a), (b-corr) and fails (b2) when its witness exists; "fringe law by response table" classifies Reproduction | classifiers | checker controls | as stated |
| K-N9 | synthetic candidate "the available operations are the finite unitaries on every composite" | §13 | must fail R2 and classify Reproduction | Reproduction |

**Mutation controls.** Each runs only after every unmodified check it depends on has passed, just after its section's
controls; each names its target check and its failing case, and counts as caught only when that check fails cleanly
on that case, judged in the manner of `tools/mutant_verdict.py` (a clean failure whose last line is the check's own
verdict, no traceback).
- KM-1 (I-6; failing case: K-PR6 replay with the a·b step removed) suppresses every verdict K-PR6 serves.
- KM-2 (own-check gate; case: the ML line with K-ML disagreeing) prints "void".
- KM-3 (K-2; case: ML-NW without the PSD constraint) admits PR, label over-generation.
- KM-4 (K-2; case: P-vD with m = x₀) loses PR's exclusion.
- KM-5 (I-14; case: IC-D5b marked closed with K-PR6-RAC as countermodel present) changes the class.
- KM-6 (I-18; case: A-3's type tag deleted) is caught by the ledger check.
- KM-7 (static premise check; case: "S_max ≤ 2√2" inserted as a premise of IC-D5b) is caught mechanically.
- KM-8 (I-4; case: a float comparison at TB's 2E² = 1) is caught by the AST scan.
- KM-9 (I-24; case: V := F_R on CC-dec) is caught.
- KM-10 (I-26; case: σ-cone's K-PR6 line deleted) suppresses that route.
- KM-11 (I-23; case: §11's classifier reading §7's verdict outside the listed steps) is caught.
- KM-12 (I-27; case: a (b-corr) result from Q4-VR printed on the (b) line) is caught.
- KM-13 (I-25; case: CC-hm with the C4 check skipped) prints "unchecked" and suppresses Q2.
- KM-14 (I-29; case: R-acc adopted without (I2) checked) is caught.
- KM-15 (I-30; case: D from the actual readout on a model where the actual readout is a coarse-graining of the optimal
  one) is caught.
- KM-16 (I-31; case: K-ERASE's conditional visibility entering V) is caught.
- KM-17 (I-33; case: "V = F_R" asserted on CC-dec) is caught.
- KM-18 (I-29; case: K-I2's measure accepted by a checker testing (I1) only) is caught.
- KM-19 (I-34; case: a Conditional line with no postdiction in its ledger printing a bare "Conditional") is caught.
- KM-20 (I-35; case: IC-D5a failed on K-PR6-RAC on account of the long edge) is caught.
- KM-21 (I-40; case: RQ with Y⊗Y removed from the joint observables, so the states are reported indistinguishable) is
  caught.
- KM-22 (I-38; case: a transformation defined on preparations and not checked on equivalence classes) is caught.
- KM-23 (§5; case: local tomography folded into "C5-P" instead of named C6) is caught by the axiom-ledger check (I-44).
- KM-24 (I-48; case: Lemma T's printout claiming it fixes the pure-state set) is caught.
- KM-25 (I-49; case: state equivalence computed from passive records only, so K-OPSTATE's P₀ and P₁ are reported equal)
  is caught.
- KM-26 (I-51; case: Lemma K applied to SPK-orig with hypothesis (i) reported as holding) is caught.
- KM-27 (I-53; case: a provisional "supplied by OI" row for X-1 printing Emergence) is caught.
- KM-28 (I-56; case: the R1 cell citing CL, which fails C1, as the witness) is caught.
- KM-29 (I-48; case: K-TRANS reporting transitivity on the QM instance without the Pur-U check) is caught.
- KM-30 (I-52; case: ℛ₁ᵇ run with the clean coupling step substituted, its printed inputs unchanged) is caught by the
  digest mismatch.
- KM-31 (I-58; case: K-SWAP's access class reported as "none" because only one-step protocols were composed) is caught.

***

## 15. Circularity-review checklist (every candidate, every section)

The reviewer records pass, fail or not applicable per line, with the step. A fail on items 1–6, 16 or 18 makes the
line Reproduction unless the step is removed and the derivation still closes; a fail on items 21 or 22 leaves the step
unclosed (refuted or Parked at that step); a fail on any other item makes the line Parked until resolved.
1. No posited Hilbert-space or operator-algebra structure, Born rule, amplitudes, quantum instruments or quantum states,
   in any step or in the interface definitions of §2.2.
2. None of the quantum set, Q1/NPA, TLM, 2√2, TB, VR, B-VF, V² + D² ≤ 1 or the fringe law is a premise.
3. E3 only as a classical count (Substratum.md:92).
4. Neither Computation.md:130 nor the shadow realizations of Main.md:576–578.
5. No parameter fixed by its effect on the result; A-2's justification recorded verbatim.
6. ML-NW coded from the covariance; quantum IC and quantum purification used only as controls.
7. Every premise is in §3, quoted at its file:line, and passes the quote checker (I-39).
8. Every assumption in its ledger with its type; no type changed after a result.
9. Records are visible configurations under O; no box, amplitude or marker state treated as primitive.
10. Operational no-signalling not used where the ontic statement is needed (IC-D3, IC-D5b, C5-S3b, V-K).
11. The Lemma 1 reading stated wherever used.
12. Each favourable branch pressure-tested (§A.31), with the countermodel attempt recorded.
13. Each displayed equivalence has a witness per direction (§A.34): ML-NW ⇔ Q1; VR ⇔ the quantum correlator set; D1 and
    D2 separately; C5 ⇒ IC one direction only.
14. No class, protocol family, tolerance, reading or rule changed after a result (I-15).
15. [L] closes mathematics only.
16. Q2: V from counts at K = 12, D over admissible readouts, path by blocking, eraser fringes separate, no quantum rule in
    the hidden sector, positive controls from their own models.
17. Q2: interferometer parameters, V and θ₀, fixed by the architecture and printed before the pattern is computed.
18. 𝓘 for C5-IC is built from the interface; checking (C5a)–(C5d) and (I1)–(I10) does not assume IC or any bound it
    implies. C5-P's formal statement uses only §2.2's notions.
19. Every route's K-PR6 line (K-PROG for Q2) is present, the premise holding on branch (a), the violation exhibited.
20. No section's verdict used elsewhere except through the steps I-23 lists.
21. Finite memory (C3, P1) does not stand in for IC, ML, C5 or B-VF.
22. Initial independence and parameter dependence kept apart; every hidden-state failure names B, slice, step, mode.
23. C5-IC's identities checked as listed, (I2) independently of (I1); a PR-box model counted as an obstruction only with
    D-1 to D-7 checked on it; a model from a correlation table declares its completion.
24. No saturation of B-VF asserted; V and the fidelity bound reported separately.
25. Each axiom-audit verdict is typed as §5 fixes, with its derivation or countermodel, and no added axiom is folded into
    C5; the paraphrased axioms are checked against PC-CDP before any verdict is final.

Additions before step 2 go under `amendments/`.

***

## 16. Productivity test and G6

**Baseline the findings must exceed:** V-1 to V-15; Main.md:356 and :407 (the unrestricted OI class includes PR);
appendix-c:232 (an epistemic restriction gives complementarity but not Bell violation; "restricted access does not by
itself single out quantum theory"); node 7's AW-MC7-2 (the admitted gate sets the magnitude); Methodology.md:393
(no-signalling does not select the quantum set) [rec]; and the contrapositive of the cited C5 ⇒ IC theorem applied to
Main.md:356.

**The node is a gem iff** one of:
- **C5-P:** the per-axiom audit yields at least one typed verdict with its derivation or countermodel that the corpus
  does not already state (V-10 and V-11 are the baseline), or the SPK or RQ control decides which axiom purification
  alone leaves open inside OI's class;
- **C5-IC:** "C5-IC established on 𝔇" with 𝔇 containing post-classical correlations; or "OI does not imply C5-IC" that
  identifies which interface property fails and why (beyond Main.md:356 plus the contrapositive); or R-pq or R-ms
  decided with the failing identity named;
- **D1/D2:** a status change on either with a reviewed construction or countermodel;
- **a route whose K-PR6 line names an O-typed premise that holds on branch (a) while the same route admits K-Q and K-C**;
- **a Q2 or H-X result** strictly stronger than appendix-c:232 and V-1 to V-8.

A Failure that restates the baseline is a non-gem (record-only), and so is any R1, D2 or §6.10 line that is a corollary
of Lemma A on a full-access class (ℛ₁ᵃ, ℛ₂ᵃ).

**G6 (rule from MC7 PREREG §7):** a finite-precision, raw-direct statistic (§A.24) on which the line's admitted set
differs from QM by more than the stated resolution, of a size fixed by OI quantities, both outcomes possible. Scenarios:
V² + D² > 1 at a fixed size; nonzero 𝒮₃ at a fixed size (against the three-path bounds Structure.md:1312 cites [rec]);
coarse-grained Bell tests on non-i.i.d. sources [L-s]; the Q1 points violating IC (PC-CSS); the three-setting points
(PC-PW); the chained and NPA 1+AB boundaries; the temporal CHSH bound [L-c: Le et al. 2017, Main ref. [26]].

***

## 17. Literature, with what is and is not known

- *Reconstruction:* Chiribella, D'Ariano and Perinotti, PRA 84, 012311 (2011) [L]: purification plus five axioms
  (gated PC-CDP). Chiribella and Scandolo, on entropies in purification theories and on the toy theory's purification
  [L] (gated PC-CS, PC-SPK). Spekkens, PRA 75, 032110 (2007) [L].
- *Real QT and local tomography:* the two-rebit example is standard [L]; recomputed here (RQ).
- *Complementarity:* Greenberger and Yasin 1988; Englert 1996; Jaeger, Shimony and Vaidman, PRA 51, 54 (1995); Fuchs and
  van de Graaf 1999 [L]. *Third-order interference:* Sorkin 1994; Sinha et al. 2010 [L].
- *Nonlocality, uncertainty, steering:* Oppenheim and Wehner 2010 [L].
- *Information route to IC:* Barnum et al. 2010; Al-Safi and Short 2011; Short and Wehner 2010; Dahlsten, Lercher and
  Renner 2012 [L-s]; DiVincenzo et al. 2004 [L].
- *IC:* Pawłowski et al. 2009 [L]; Allcock, Brunner, Pawłowski and Scarani 2009 [L]; Cavalcanti, Salles and Scarani
  2010 [L-s]; Navascués, Guryanova, Hoban and Acín 2015 [L]. *Recent IC [L-c]:* Gachechiladze and Miklin,
  arXiv:2609.10508 (2026); Pompili and Weilenmann, arXiv:2610.06604 (2026); Jain, Gachechiladze and Miklin, PRL (2024),
  arXiv:2308.02478; arXiv:2606.02416; arXiv:2602.10206.
- *ML:* Navascués and Wunderlich 2010 [L-s]; Navascués, Pironio and Acín 2008 [L]; Gallego and Dakić 2021 [L-s].
- *Tsirelson 1980, 1987; Fine 1982; Landau 1988; Acín, Massar and Pironio 2012; Wehner 2006; Collins and Gisin 2004;
  Gallego et al. 2011* [L].
- *Mathematics as [L]:* the CLT; joint models for Gaussian marginals; the CHSH sum of squares (exact in MC7 [rec]);
  1 − h((1 + x)/2) ≥ x²/(2 ln 2).

***

## 18. Invariant→checkpoint table (§A.41)

| # | property | checkpoint |
|---|---|---|
| I-1 | this preregistration preceded every computation and is unchanged | sha256 in NODE.md and the commit message; byte-identical in the step-2 commit; amendments under `amendments/` with time, reason and state of knowledge, before the computation they touch; the probe prints the digest first |
| I-2 | condition O for every realization | realizations as (Ω, bijections, readout projection, prior); exhaustive bijectivity; static test that law code reads nothing else; K-9 count |
| I-3 | each candidate computed by its preregistered formalization | a parameter table transcribed from §2.2, §4.3, §6–§11, compared by the reviewer; admit-functions cite their section |
| I-4 | exact or rigorously enclosed comparisons | rational, ℚ(√2) and ℚ(√2, √3) arithmetic; enclosure widths printed; AST scan for floats on the verdict path |
| I-5 | determinism | two runs byte-identical, `SHA256SUMS`, fixed seeds, no random instance |
| I-6 | no verdict over a failed control | per-section gating; KM-1 |
| I-7 | the checker detects the failure kinds | K-N1 to K-N9, K-P |
| I-8 | universal clauses beyond computed ranges | reviewed [W]; failures by one exact violator |
| I-9 | follow-ups triggered as fixed | probe log with certificates |
| I-10 | (b) apart from (a) | separate blocks |
| I-11 | classification follows §13 | classifier inputs printed beside each class |
| I-12 | quotes verbatim at `a501b418` | `quotecheck.py` with its list synchronized to this file; count printed |
| I-13 | independent review including §15 | review section in NODE.md |
| I-14 | every step closed or refuted as recorded | step ledgers; KM-5 |
| I-15 | nothing changed after a result | parameters and definitions printed with digest before each section |
| I-16 | productivity and G6 follow §16 | table of reasons with their steps |
| I-17 | the classifier maps inputs to classes as fixed | unit tests per class per section; precedence on two-condition vectors; the "prevents a decision" qualifier tested |
| I-18 | ledgers complete and typed before computation | ledgers printed with digest; O/M entries name their step; KM-6 |
| I-19 | A2 rows never decide an A1 clause | separate block; static check; K-N2 |
| I-20 | ML-NW's code paths agree | K-ML |
| I-21 | IC exclusions certified | protocol, value and m printed |
| I-22 | literature dependence visible | each line lists its [L], [L-s], [L-c]; a physical [L] dependence blocks Emergence |
| I-23 | depth-first order; no propagation except through named steps | probe log; static check allowing only: V-M-1; σ-C5P, σ-C5IC, ρ-C5P, ρ-C5IC, V-C5P (added axioms, read from the axiom ledger); Q2's tests of §6/§7 restrictions as named axioms; §11's lines "from §6, §7, §10"; §11.4 steps; KM-11 |
| I-24 | V from counts; not from D, F_R or an overlap | static check; K-VD; KM-9 |
| I-25 | C1–C4 checked in exact statements | per-realization printout; K-C1C4; KM-13 |
| I-26 | every route has its K-PR6 line (K-PROG for Q2) | ledger check; KM-10 |
| I-27 | (b-corr) never reported as (b) | separate lines; unit test; KM-12 |
| I-28 | literature test points and wording enter only through amendments | PC-PW, PC-GM, PC-CSS, PC-CDP, PC-SPK, PC-CS read only from digest-printed amendment files |
| I-29 | each C5-IC property and identity has its checkpoint | (I1)–(I10) per route on 𝔇, (I2) independently of (I1); K-I2; KM-14, KM-18 |
| I-30 | D is the maximum over admissible readouts | readout set enumerated, size printed; KM-15 |
| I-31 | eraser fringes separate | K-ERASE; static check; KM-16 |
| I-32 | B-VF never assumed | static premise check; KM-7 |
| I-33 | no saturation of B-VF asserted | V and inf_R F_R printed separately; CC-dec; KM-17 |
| I-34 | the postdiction requirement applied | every Conditional line prints its postdiction status; unit test; KM-19 |
| I-35 | initial independence and parameter dependence kept apart | IC-D5a and C5-S3a read O3 and the prior only (static); failing step and mode printed; KM-20 |
| I-36 | H-C5-IC's verdict follows §7.5's table | one unit test per row, the joint case included; "Undetermined" maps to Parked |
| I-37 | missing tools fail, never skip | import failures abort the dependent control with its name; versions printed |
| I-38 | the interface is well defined per class before use | K-IF prints states, pure states, transformations (checked on classes), reversibles and composites for each control class, with digest, before any candidate; KM-22 |
| I-39 | every ledger quote passes the quote checker | the step-2 ledgers' quotes are appended to the checker's list and checked |
| I-40 | the real-QT control decides as fixed | RQ: PSD, 9 product effects equal, Y⊗Y separates; KM-21 |
| I-41 | the reference row is a record check | the quoted statement at mc-node5:28–29 and GR.md:216 printed; nothing computed |
| I-42 | Q2 suppressed until K-LEM passes | gate on K-LEM |
| I-43 | the scorecard is generated | each cell names its line and checkpoint; a literal cell fails the build |
| I-44 | the axiom ledger carries every added axiom by its own name | a check that no audit row typed compatible-but-added lacks a C6… label; KM-23 |
| I-45 | B and its slices declared and printed before any route | §2.2's B_{t₀}, B_{t₁} and the K-PR6-C5 system printed with digest |
| I-46 | 𝔇 and the interface declared before C5-IC checks | 𝔇 ⊇ 𝔇_min printed with digest; any exclusion typed |
| I-47 | V and θ₀ predicted before the pattern | printed per realization before the count computation |
| I-48 | Lemma T is applied as proved, with its limits | K-TRANS: on CL and on the qubit control, the reversible transformations are shown transitive on pure states (classical permutations on vertices; unitaries on the Bloch sphere instance), and the printout states that neither the pure-state set nor the operation set is fixed by it; KM-24 |
| I-49 | operational states are classes under all interventions, not records | K-OPSTATE: equal passive laws, separated by an intervention; a static check that the state-equivalence code quantifies over the protocol class with ancillas and later interventions; KM-25 |
| I-50 | §6.10 runs first and fixes the objects | the probe log shows ℛ₁ and ℛ₂ outputs with digests before any C5-P line; every C5-P line cites those digests |
| I-51 | Lemma K's consequences are not asserted of OI without the three hypotheses checked | each use of Lemma K prints which of (i)–(iii) hold on the class, with the preparable-mixture set (Q-PREP) stated |
| I-52 | each §6.10 class's inputs are fixed before it runs | (Ω, φ, accessible bijections, coupling steps, ancilla conventions, priors, composites) printed with digest before §6.10; every later line cites the digest; KM-30 |
| I-53 | a provisional audit row yields no final verdict | rows print "provisional, pending PC-CDP" while the gate is unmet; the classifier maps a provisional row to Parked and refuses "supplied" final, Emergence and final C6… labels; unit test; KM-27 |
| I-54 | the mixture and pure-state definitions are applied as fixed | K-IF prints the preparable set and the pure set per class under §2.2's rule, and states whether the set is closed under real convex combination |
| I-55 | the equivalence domain is declared before step 3 | printed with digest; a line claiming equivalence on another domain fails the build |
| I-56 | every R1 witness passes K-C1C4; calibrations are never used as witnesses | the R1 cell names the witness and its K-C1C4 printout; a witness without one is refused; KM-28 |
| I-58 | access is measured per class over composed protocols | §6.10 prints each class's access class (the hidden distinctions operationally visible after composition) with digest before any purification verdict; K-SWAP's class must print full hidden access; KM-31 |
| I-59 | the two purification readings are kept apart | the classifier prints Pur-E on the preparable set (per budget and across the theory) and Pur-E on the convex closure as separate lines, with Lemma K's hypothesis status beside the closure line; a unit test feeding a grid pass alone cannot print CDP purification |
| I-57 | the QM instance is closed and lies in its field | enumeration: Clifford images, Pauli readouts with conditioning and partial traces of every instance state stay in the instance; every entry in ℚ(i, √2) |

***

## 19. Procedure and freeze

- Step 2 order:
  1. quote check (I-12), condition-O engine (K-9), C1–C4 checker, interface computation on the control classes (K-IF),
     classifier unit tests (I-17, I-36);
  2. common controls K-PR6, K-PR6-RAC, K-PROG; their mutants;
  3. (after the equivalence domain is declared, I-55) C5-P (§6): first §6.10 on ℛ₁ᵃ, ℛ₁ᵇ, then ℛ₂ᵃ, ℛ₂ᵇ (the state
     space across interventions, K-OPSTATE); then controls RQ,
     SPK-orig, SPK-conv, CL, CL-C4, BW, QM, K-TRANS; R1, R2, R4; Q-PREP, Q-FIN; the framework and axiom audits
     (provisional pending PC-CDP, Parked while unmet); D1, D2, L-PI; mutants;
  4. C5-IC (§7): K-C5+, K-I2, K-PR6-C5, K-ONT, K-ACC; R-ont, R-acc, R-pq, R-ms with (I1)–(I10); the chain C5-S1 to
     C5-S5; the verdict table; mutants;
  5. the reference row (§8); 6. Q2 (§9) after K-LEM; mutants;
  7. the IC and ML lines (§10), then V-M-1; 8. composites (§11), gated tests only with their amendments;
  9. classification, scorecard, axiom ledger, H-X, postdiction, productivity, G6;
  10. the independent review including §15.
- Additions before step 2 (a reviewer's premise, route, reading or checklist item; a corrected quote; any PC amendment)
  go under `amendments/` with time and reason, and a new sha256 is recorded. After a section's first computation its
  formalizations, classes, rules and criteria are frozen; a later discrepancy is recorded, not repaired.
- Negative results are acceptable and scoped to the candidates, routes and classes examined. They do not establish that
  observational incompleteness as such cannot explain quantum behaviour; the emergent-QM hypothesis and the A2 programme
  stay open.
