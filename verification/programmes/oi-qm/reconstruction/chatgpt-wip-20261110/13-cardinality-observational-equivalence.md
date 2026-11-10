# CARD-GAUGE-1 — Effective cardinality undecidability and observer-relative hidden-sector equivalence

**Paper-only research WIP · 10 November 2026 · INDEPENDENT REVIEW PENDING**

**Home and standing:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) conditional OI–QM equivalence; coordinates with the existing [observer-relative finiteness dependency audit](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/audits/manuscript/observer-relative-finiteness-20261030/DEPENDENCY-AUDIT.md) and its #1007/#1015 source boundaries; [#1216](https://github.com/amaybaum/incompleteness/issues/1216) equal priority for arbitrary finite-precision *complete-history* equivalence. Physical preparation, native controls and source-selection gates remain unchanged. This is a proposed mathematical clarification, not a new physical premise.

**Scope of this file:** source-pinned read-only audit plus mathematical proofs with explicit model representations; no experimental/numerical/Lean execution, new physical claim, manuscript amendment, F/E designation, dispatch or merge. The previous Codex [ACCEPT WITH NITS](https://chatgpt.com/space/page_2f791d4a97fc8191ade6141a5ed9bdfe) at archive head 6879c7c0 covers only the original eleven documents. [PREP-HIST-4](12-prep-history4-and-finite-decision.md) and this new file are **not independently reviewed**. PR #1222 remains **draft/unmerged**.

## Answer in one paragraph

Finite resolution at an observer cut is not a theorem of finite total substrate cardinality. From a computable description of an arbitrary *decidable* carrier, distinguishing finite from infinite carrier is undecidable in general; this is established by a reduction from the Halting Problem **under a specified effective-description representation**, not by inferring properties of the actual physical universe. Independently, for any fixed, fully specified observer/protocol family there exist finite, countably infinite and uncountably infinite deterministic reversible completions with **identical accessible complete-history laws**, by adjoining a normalized, dynamically decoupled hidden factor. The suitable relation is *observer-relative operational or stable hidden-ancilla equivalence*. It does not supply a cardinality-changing bijective gauge transformation, prove all possible hidden factors are gauge, or remove any QM physical sourcing requirement.

**Three propositions to review:** CARD-COMP (computational undecidability), CARD-OBS (exact observable-law preservation under decoupled enlargement), and CARD-SCOPE (failure of unrestricted cardinality gauge when additional interactions are admitted).

## 1. Source audit: what OI already earns and what is not yet extended

Historical main pin: [cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481).

1. [Main §1.2](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Main.md) distinguishes a finite set of distinguishable states for a given observer from the **additional posit** that the entire substratum is finite.
2. The [observer-relative finiteness audit](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/audits/manuscript/observer-relative-finiteness-20261030/DEPENDENCY-AUDIT.md), section "Owner direction — foundation versus implementation", explicitly permits finite, countably infinite and continuous total carrier candidates *provided their dynamics, measurable readouts and normalized laws are specified*. It retains the old finite theorem branch and warns that finite visible resolution requires an observer resource/information premise, not embedding alone.
3. [Substratum Theorem 24(iii)](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md) establishes **finite** independently prepared, exactly decoupled normalized ancillary enlargement as a fixed-interface invariance. It does **not** prove arbitrary interacting deep-sector enlargement, infinite ancillary extension or a bijection between carriers with different cardinalities.
4. [Substratum Proposition 24.4/24.5](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md) distinguishes the finite *predictive quotient* under specified full passive word access from arbitrary invisible microscopic fibres. A record can determine a hidden variable if it is constant on its record fibre; no general opacity/undecidability of all hidden variables is claimed.
5. The [infinite-tape XOR counterexample](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/substratum/continuous-substates/infinite-xor-counterexample.md) supplies a particular uncountable reversible measurable carrier with finite-bit observation, full normalized product law and accessible memory. It does not establish operational QM, a native control interface or cardinality uniqueness.
6. Our [PREP-HIST-4](12-prep-history4-and-finite-decision.md) finite-state decision threshold uses the finite ring cardinality 2^(2L). It is *not* a theorem about infinite carriers, even though a specially constructed infinite extension may share every visible history of the finite ring.

The present mathematical extension is intentionally narrower than a universal "hidden cardinality is gauge" slogan. It must not rewrite A1 of the existing finite structural reconstruction, which has its own separate physical and theorem status. The finite-carrier theorem and its recurrence consequences are retained as conditional mathematical results.

## 2. Exact observer-relative operational equivalence

Fix an observation/interface specification O consisting of:

- a measurable configuration space (S,Σ), a deterministic measurable reversible evolution φ:S→S (with measurable inverse when required), and a normalized preparation family {μ_p};
- a family of physically admitted interventions/protocols a, including adaptive choices determined by previously available records; their implementation is included in the described full world rather than presumed;
- a finite or finitely resolved visible readout alphabet V per step, with measurable observation map π:S→V; optional failure/herald/read-clock symbols are **part of V or the declared full record**, not removed by conditioning.

A protocol produces a probability law P^a_p on **all complete accessible finite histories** (including every actually accessible controller/preparer/outcome/failure log and any allowed terminating/stopping symbol). When histories have varying lengths, compare on a common tagged disjoint-union alphabet.

**Definition (fixed-interface operational equivalence).** Two models M and N are O-equivalent, written M ≡_O N, if for *every admitted preparation p*, *every admitted finite protocol a*, and *every complete accessible history h*,
    
    P^a_{M,p}(h) = P^a_{N,p}(h).

A probability measure on an infinite record space is compared by equality of measures, not pointwise density. If an admitted family contains protocols that actually access a proposed added factor, the identity condition cannot be assumed. Likewise, equal one-time marginals or a single finite horizon is not a substitute for equality under the declared full protocol family.

This relation is an **equivalence relation** for a fixed common protocol/record dictionary and model class; it may be coarser than isomorphism of total deterministic systems. Additional resource-sensitive equivalence (memory, time, cost, failure or communication budgets) would require those observables/budgets in the dictionary. Equality of output laws alone does not establish equal efficiency of the realizations.

## 3. CARD-OBS: exact arbitrary-cardinality invisible-factor extension

**Proposition CARD-OBS.** Suppose M=(S,φ,π,{μ_p},{I_a}) is a well-defined deterministic reversible observer model. Let (K,κ) be any nonempty standard measurable probability space with **normalized** probability κ(K)=1, and let ψ:K→K be an invertible measurable map preserving κ. Construct

    S' = S×K,
    φ'(s,k)=(φ(s),ψ(k)),
    μ'_p=μ_p⊗κ,
    π'(s,k)=π(s),
    I'_a=I_a×id_K

for the entire admitted read/write/protocol repertoire (or its correspondingly independent local instrument). All allowed adaptive control and readouts must depend only on S-sector records. Then M' ≡_O M for **every finite complete accessible-history experiment** in the stated protocol class. Equality also holds on the sigma-algebra generated by the entire infinite passive visible sequence, wherever that process is defined, because all finite cylinder measures agree.

**Proof (passive case).** For a length-T readout cylinder C (or a measurable complete-history event), the corresponding event in S' is π/φ's original S-sector inverse image B_C times all K. Under the product input law its probability is

    (μ_p⊗κ)(B_C×K)=μ_p(B_C) κ(K)=μ_p(B_C).

The K evolution does not couple into S, and κ is preserved. **Adaptive case:** the selected next admitted intervention is a function of the already read S-history; by induction every possible branching history, its probability and all failure/abort statuses equal those of M, since every admitted instrument acts as the original S operation tensored with identity on K. Hence the complete accessible-history measures coincide. □

**Important assumption:** A finite readout is not necessarily a *subsystem factor*. If the observer projection is not a physical product readout or the actual intervention touches K, the tensor construction is a **new model and protocol restriction** whose source must be demonstrated; it cannot be imposed on a given interacting world by gauge vocabulary.

**Concrete cardinality controls (take any fixed nonempty finite S):**

- **Finite comparator:** K={★}, κ=δ_★, ψ=id.
- **Countably infinite comparator:** K=ℕ, κ(n)=2^(-n-1), ψ=id. This κ is normalized and has full support on the discrete countable factor.
- **Uncountably infinite comparator with nontrivial hidden motion:** K={0,1}^ℤ, κ the two-sided fair Bernoulli product measure, and ψ the bilateral shift. The carrier is uncountable, κ is normalized, ψ is an invertible measurable measure-preserving map, and its visible dynamics remains completely decoupled.

All three produce *the same* law for every admitted complete history, not just an approximation or one selected horizon. Their total state-space cardinalities differ. No uniform counting probability is used on the countable or uncountable comparator.

**Interpretive status:** CARD-OBS is a straightforward general measure-theoretic extension of the finite decoupled-factor identity in Substratum Theorem 24(iii), not a claim of discovery of a new physical symmetry group. Its scientific consequence is **nonidentifiability of total carrier cardinality from the fixed admitted operational data in this model class**.

## 4. CARD-COMP: Turing undecidability under an explicit effective description

The Halting Theorem does *not* state that the real universe has undecidable cardinality. The following separate statement concerns a specified input representation.

**Proposition CARD-COMP.** There is no total algorithm that, for every index of an effectively described *decidable* countable configuration space H with computable membership test, always answers whether |H| is finite or infinite. The same holds for a family of computably represented reversible substrate models on S_0×H with a fixed nonempty finite visible base S_0, a computable full-support normalized hidden preparation law and a computable bijective update.

**Proof by explicit halting reduction.** For any Turing machine M (with a fixed standard input), define a subset of ℕ:

    H_M = {0} ∪ {n+1 : M has NOT halted within the first n steps}.

Given n, bounded simulation of M for n steps decides membership of n+1. If M halts, H_M is finite; if M never halts, H_M is infinite. Therefore an algorithm deciding finiteness from the membership program would decide whether M halts, contradicting the Halting Theorem. □

**Normalized, uniformly computable full-support source (to rule out a vacuous missing-measure objection).** Let weights q_n=2^(-n-2) for n≥0, with sum 1/2. Define

    ν_M(n+1) = q_n if M has not halted within n steps (otherwise n+1∉H_M),
    ν_M(0) = 1/2 + Σ_{n≥0: M has halted within n steps} q_n.

These probabilities sum to one. Every element of H_M receives strictly positive mass. Each ν_M(n+1) is computable by bounded simulation; ν_M(0) is **uniformly computable as a real**: truncate at n=N and bound the remaining tail by 2^(-N-1). For the full world choose any fixed finite base model (S_0,φ_0,μ_0,π_0), give S_0×H_M the product law μ_0⊗ν_M, update (φ_0,id), and read only the base projection. The update and inverse are computable and bijective, and the hidden source is a normalized, computable probability law. Membership of the product carrier is decidable uniformly from M. Total finiteness is nevertheless equivalent to the uncomputable halting predicate.

This proves a **uniform decision impossibility for descriptions in this class**, not that a model whose full finite carrier and cardinality are explicitly listed has an undecidable cardinality. It does not by itself prevent a physically accessible experiment from revealing a difference in other model classes. The observational result CARD-OBS is logically independent and stronger than algorithmic undecidability for its fixed protocol family.

**Known theorem attribution:** this is a direct halting reduction of a nontrivial semantic cardinality property; it is not a new OI proof of the Halting Theorem. No unsupported conclusion about a hypercomputer, physical computability, or an embedded observer's ability to inspect arbitrary computer descriptions is drawn.

## 5. CARD-SCOPE: why unrestricted cardinality gauge does not follow

**Proposition CARD-SCOPE (simple countercontrol).** The statement "any enlargement of a hidden sector is gauge for every future observer" is false without a restriction on admissible interactions.

Start with a visible bit v and hidden bit h initially fair. For a two-bit world, consider a reversible SWAP of v and h; reading v after SWAP reveals h. Compare with an alternative realization having an additional hidden bit k, initially fair, and a permitted later reversible SWAP of v and k. If k is independent of h, protocols that are allowed to prepare, set, correlate or query k can have different complete histories from the old model. A more elementary deterministic control: if one new permitted setting "read k" has a readable output in the enlarged model but no corresponding port in the original model, the protocol dictionaries are not the same, so the claim of unrestricted equivalence is not even well typed.

**Classification:** a new sector which is exactly decoupled for *all* admitted observation protocols is operationally inert at that interface. A sector which later couples or whose initialization can affect accessible histories must be included in the operational model and tested. "Hidden at one moment" is not the same as "inaccessible under every permitted finite protocol."

**Gauge terminology.** An ordinary invertible gauge automorphism maps a carrier to itself (or to an isomorphic carrier), and so does not provide a bijection between a finite and an infinite set. CARD-OBS establishes instead a **stable equivalence under ancillary enlargement** or the broader observational-equivalence **relation** on models. Calling total hidden cardinality "gauge" is justifiable only as shorthand for *unfixed under a specified observer-relative quotient*, not as a newly established cardinality-changing element of the existing group 𝒢_sub. A groupoid or equivalence relation induced by adjoining/forgetting observationally inert factors may be a future formalization; no completeness theorem of those transformations is claimed.

The observable predictive quotient can have fixed finite size even when the complete ontology is larger or infinite. Conversely the true physical preparation/control interface could discriminate the models; the distinction is empirical and protocol-relative, not decided by philosophical argument alone.

## 6. Effect on OI–QM programme and prior finite proofs

**#1169 main target.** A unique physical hidden-state cardinality need not be reconstructed if two physically sourced realizations give *one complete quantum-operational history family* across all admitted classical and quantum measurement contexts. This does not show that any such family is sourced from OI. The failure to supply common preparation, native controllability, interference/Born selection, composite closure and Bell-compatible, no-signalling records remains **OPEN**.

**#1216 approximation.** A finite/infinite O-equivalent extension has exactly zero accessible-history total-variation distance, **within the fixed admitted interface**. However a claim of arbitrarily accurate quantum approximation still needs one physically sourced uniform scalable interface across horizon, precision, composition and adaptivity. One finite-horizon representation cannot replace that criterion. A changed measurement port can invalidate equivalence.

**#1220 complexity and resources.** Mathematical equality of output laws is not equality of physical implementation costs, algorithmic sampling time, apparatus memory or energy. A fully decoupled infinite hidden factor can make the state-space ontology infinite without providing an efficient or physically supplied simulator. Any efficiency-aware equivalence must extend the comparison to the ledger and prove corresponding cost bounds.

**Finite ring and PREP-HIST-4.** The exact finite-state stopping bound T≤2^(2L)-1 is a **finite-representative** theorem and need not apply to an arbitrary infinite system. A decoupled infinite factor can nevertheless leave the finite-ring observer histories unchanged, so those observable properties can survive in an infinite representative *for a reason other than global finiteness*. The general infinite case needs separate dynamical/measure and access hypotheses.

**Theorem 24 and finiteness-audit preservation.** Retain finite A1 where it is a stated hypothesis of Substratum's finite reconstruction and its Lean proofs. Do not infer total finiteness from finite observer resolution; do not call normalized counting on infinite carriers. Theorem 24(iii)'s reviewed finite ancilla identity remains unchanged. CARD-OBS is a separate **unreviewed** standard-measure extension, not an amendment of the historical theorem or its gauge group's proven completeness.

**Classical preservation:** admitting a classical observable law in an OI model is not evidence against the target hypothesis; one common source must allow both classical and quantum regimes under permitted measurements. CARD-OBS says nothing about the adequacy of the underlying quantum repertoire. The C0/C1 reviewed nonquantum countermodels remain substantive controls.

## 7. Exact independent review and future proof obligations

**Independent review: NOT PERFORMED in this writer session.** The manuscript text is meant to be criticized, not adopted as an OI result or scientific publication proof.

A separate reviewer should check:

1. Main and finiteness-audit status: finite observable alphabet as the specified interface premise; total finite S not logically forced; A1 finite branch and exact theorem scopes preserved.
2. **CARD-OBS:** measurable product law, normalization, all-time deterministic factorization and adaptive protocol induction. Confirm that failure, controller, preparer, stop and resource records belong to the observable alphabet if accessible. Check arbitrary countable/uncountable examples against their measures and ψ-invariance, especially bilateral Bernoulli shift.
3. **CARD-COMP:** uniform effective membership decision for H_M, finite iff M halts, normalized ν_M, full support on H_M, and uniform computability of ν_M(0) using a geometric tail. Check that φ_M and inverse are computable and that the algorithmic statement applies only to effective input representations.
4. **CARD-SCOPE:** distinguish invertible internal gauge changes from a relation across differently sized carriers. Explain why expanding the allowed intervention family may distinguish the models, rather than equating all hidden states by decree.
5. **Theorem 24(iii) attribution:** do not misstate the finite-ancilla result as an already accepted all-infinite theorem. Existing predictive-quotient and arbitrary-hidden-readback counterexamples remain binding.
6. **Scientific firewall:** O-equivalence neither proves Born, physical source, Bell/CHSH, coherent instruments, quantum closure, scalable approximation nor computational efficiency; #866 gate remains NOT PASSED. No false conclusion "Halting Theorem makes the actual physical substratum unknowable" is permitted.
7. Attribution and novelty: separate standard Halting theorem, standard ancillary-system projection and stable equivalence vocabulary from any potentially new OI-specific interpretation.

Suggested disposition: ACCEPT / ACCEPT-WITH-NITS / REVISE **for bounded mathematical/source claims only**; if accepted, review whether its terminology belongs in #1169's dependency matrix before any formal integration. Scientific execution, physical-premise adoption, manuscript change, F/E, dispatch, publication and merge remain separately gated.

**Next scientific question (not answered here):** Can a *physically justified* OI extension couple a deep sector nontrivially while remaining operationally indistinguishable for all physically admitted classical/quantum protocols and satisfying a meaningful resource-cost equivalence? That is stronger and more relevant than adding a freely decoupled tape as a mathematical spectator.