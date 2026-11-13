**Unit 2 / #1169–#1216 critical review and corrected interpretation · 9 November 2026**

**Status: WRITER-SIDE ADVERSARIAL AUDIT COMPLETE; INDEPENDENT REVIEW STILL PENDING.** This is a reproducible source-and-proof critique from the current ChatGPT writer, **not a separate reviewer** and not an ACCEPT verdict. The previous [Unit 2 writer draft](https://chatgpt.com/space/page_c6fc269cb66481919afd4d54807e9c46) remains preserved; this is its v1a scientific attribution/disposition addendum and the review-ready corrected interpretation. Existing pre-v1 independently ACCEPTED #1169 matrix, #1143 countermodel and #1220 resource contract remain unchanged. No branch, PR, GitHub issue, native execution, Lean, gate, merge or manuscript change is performed.

**Internal disposition: REVISE ATTRIBUTION / SOURCE CLAIMS, not a refutation of the displayed bounded inequalities.** The q bound is a special case of known Bell local-content reasoning, and R-CONE specializes existing finite-speed/coupling graph reasoning. The genuinely open research is whether a **single physically sourced OI preparation + available observer-interface family** yields the requisite context-dependent hidden coupling, no-signalling, Born statistics and quantum composition while retaining classical measurements. Mathematics for supplied conditional interfaces ≠ source of those interfaces.

# 1 Adversarial audit outcome (unit-2 v1 → v1a)

| Claim / section in v1 | Writer-side proof check | Necessary correction before independent acceptance |
| --- | --- | --- |
| **W-CHSH: S≤2+2q** | PASS algebraically under one response-complete pre-setting λ, counterfactual outputs for all four setting pairs and μ independent of the settings | **Attribution:** explicitly call this the standard local-content/nonlocal-weight Bell argument in the defined deterministic interpretation, not a novel foundational OI theorem. Its q is test- and response-model-relative, not a frequency of observed signalling or a physical resource |
| **q≥√2−1 (~41.4%)** | PASS for the single two-setting CHSH quantum comparator with ideal S=2√2 | Scope strictly to the **declared two-setting Bell test**; do not assert the same decomposition for every measurement family, or claim deterministic finite counting realizes its irrational mixing fraction exactly |
| **Approximate q≥√2−1−4ε** | PASS where ε is TV on the common complete-history law and setting/output marginal has uniform settings; test function 4s_xy ab spans [−4,4] | Do not apply to rare-herald-conditioned laws by dropping failure symbols. If comparison uses conditional settings probabilities, the simple uniform-setting factor must be rederived |
| **Outcome-only sharpness: Q_v** | PASS: (1−q)Q_(1/2)+qQ_1 = Q_(1/√2) for q=√2−1. Eight deterministic local strategies reproduce Q_(1/2) with balanced marginals | This is a supplied abstract box mixture and a familiar local-content decomposition; **not** a native OI operation, physical source, or all-measurements optimality theorem |
| **R-CONE radius 2 and t-step support** | PASS at the mathematical update `F(u,v)=(f(u)⊕v,u)` with f_i using i−1,i+1,i+2 | Make the causal-cone statement explicitly **conditional on all controller, apparatus and read writes being local in the same complete carrier**. It is a specialization of the existing Main cone, not a source of a prepared long edge or physical-relativity statement |
| **SYM-BAL symmetry suffices for equal local-history law** | PASS by pushforward invariance T_#μ=μ and exact conjugacy of the full local-history maps | Crucial distinction: generic counting-measure invariance of a reversible world does **not** establish the needed Bell-specific relabelling T for actual accessible histories or for all physical preparations/continuations |
| **PR reversible countercontrol** | PASS: global XOR map is an involution, supplied fair r gives b=r⊕xy, and b by itself is no-signalling | This is a **global response table**, not an SM ring or available OI instrument. If Bob can later access r and b in the isolation window, his complete history reveals remote x for y=1; never silently seal that information |
| **Physical source route** | Source verdict **UNSOURCED**, consistent with Main §3.3, SM §3.1 and existing #868 source stop | Avoid presenting a hypothetical prepared long-range edge, fair r, or chosen source symmetry as a derived physical restriction. Classical-register fragment and independently prepared source must remain explicit |
| **#1220 scaling** | Correctly leaves three outcomes possible | No runtime/communication/energy lower bound follows from a counterfactual nonlocal fraction or a TV gap. O(L) update for the given ring means only supplied-state literal-update cost, not scalable QM simulation |

**External novelty correction.** [Chaves et al., “Violations of locality and free choice are equivalent resources in Bell experiments” (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8092485/) explicitly report that for the maximally violated *two-setting* quantum CHSH experiment the local fraction is at most `2−√2≈0.586`; its complement is `√2−1≈0.414`. The v1 inequality is a deterministic-response interpretation of the same local/nonlocal weight argument, not an independent discovery. [Wood–Spekkens (2015)](https://doi.org/10.1088/1367-2630/17/3/033002) explains the causal fine-tuning challenge for Bell-violating no-signalling distributions; merely proposing hidden coupling plus cancellations does not solve this challenge.

# 2 Exact mathematical core retained, with honest provenance

Fix binary settings x,y, outputs a,b∈{−1,+1} and a response-complete λ distributed by one setting-independent μ. For each λ the four counterfactual output pairs A_xy(λ), B_xy(λ) are defined. Let L be states with A_x0=A_x1 and B_0y=B_1y for each x,y. Define q=μ(Lᶜ). For λ∈L, the signed CHSH score is at most 2 by ordinary local decomposition. For λ∉L it is at most 4 because all four signed correlators are in {−1,+1}. Averaging over one μ gives S≤2+2q. Consequently to approximate the quantum S_Q=2√2 within complete-history TV ε on a common alphabet with uniform settings,

`2√2−8ε ≤ S ≤2+2q` and hence `q ≥ max(0, √2−1−4ε)`.

This is a **benchmark constraint** on a candidate model, not a physical construction. The 10.36% local-model TV floor in the prior joint milestone arises from the **same CHSH witness** with q=0 and should not be counted as statistically or logically independent evidence of OI's physical correctness.

If setting independence is unavailable because settings are computed from a deterministically closed universe, a response-complete interventional setting variable or a rigorously declared reference to p(λ|x,y) is required. The current paper assumes the independent setting intervention; it does not derive it.

**Specialized ring consequence.** The SM binary ring has f_i(u)=u_{i−1}⊕(u_{i+1}∨u_{i+2}), and two-slice F(u,v)=(f(u)⊕v,u). The complete step has support within radius 2. The established finite causal-cone induction therefore yields no change outside radius 2t after t full updates when a local setting write changes only an initially local region and every other interface component respects the same locality. Under screened independent settings, sufficiently separated Bell readouts have q=0, and the ideal target is separated in the declared benchmark by the usual Bell TV floor. Beyond that separation window, this cone lemma is silent—not positive evidence of native Bell capability.

**Symmetry source criterion.** A physically generated measure μ invariant under T and an *exact complete-local-history* equality H_remote-change=H_reference∘T suffice for no-signalling by pushing forward μ. But the existence of μ,T is a physical-source hypothesis; a generic microstate-permutation invariance and the bare word “equilibrium” do not supply it.

# 3 A material quantifier trap across #1169 and #1216

The prior [RS-1 quantitative affine-span note](https://chatgpt.com/space/page_66750b14a1dc8191a59a3c3dba1ae8f1) defines K for an affinely full **collection** of physically available preparations and η as a maximum complete-history signalling defect **across that entire collection and a fixed policy menu**. It proves that Kη<1 forces pointwise independence.

**Do not infer η small for that collection merely because one target quantum benchmark is approximated well.** A single approximated singlet law says nothing automatically about signalling from other preparations μ_i, their accessibility, their controller histories, or the scale-dependence of K. Therefore the q≥√2−1 bound and Kη≥1 contrapositive cannot yet be combined into a new sourced OI theorem by replacing η with the one-benchmark ε. Doing so would silently change quantifiers.

Likewise, observed no-signalling after marginalizing away a detector, herald, preparer/controller log or recoverable hidden datum is weaker than equality of the full locally accessible histories. For the PR control b=r⊕xy, access to the pair (b,r) permits remote-setting recovery when y=1. The access boundary must therefore be generated by the physical apparatus, not merely stipulated to fit quantum no-signalling.

This is a **real review blocker for any proposed synthesis** that conflates the single-benchmark error ε with all-preparation η or asserts that an equilibrium relabelling has been sourced without demonstrating its action on full histories.

# 4 Source-gate decision after critical review

The current SM state-dependent-graph line presents a coherent **hypothesis class** but not a qualifying native quantum pair mechanism. The earliest missing fields for the *specific* proposed prepared-edge construction are:

1. **Physical producer and renewal:** an actual deterministic process under the fixed rule that prepares the relevant correlated pair/edge and the shared ready/request state with independent settings, a declared source law, failures, controller/preparer residuals and reusability. The controller ring precursor stop is **lead-specific**, not a universal OI no-go.

2. **Actual remote causal interface:** verify the *full functional dependency* of the selected update including graph-selector inputs, the time interval and all apparatus/controller/read accesses. A chosen long edge alone changes neither physical executability nor the operation algebra.

3. **Complete-history source symmetry or balance:** derive, not impose by fitting the CHSH table, a source-compatible invariant supporting no-signalling for every actually permitted preparation and adaptive continuation.

4. **Quantum selection beyond no-signalling:** exclude PR controls, source Born statistics, joint-state positivity/closure and consistent switching/composition, while preserving classical-register fragments.

A proof of source 1–3 would still be **insufficient** for complete QM. The new q benchmark is useful as an early rejection criterion, not as a selection law. A reviewer should treat all statements of physical availability as **UNSOURCED** until an actual executing process and source contract are supplied.

For #1220, ordinary local update costs and the 41.4% fraction give no native classical weak-sampling hardness and no upper bound for the full generated interface. #945 finite-bit repair remains separate. All three complexity outcomes stay live.

# 5 Independent review request (not yet executed)

A **different reviewer**, with no dependence on the writer's conclusions, should read [Unit 2 v1](https://chatgpt.com/space/page_c6fc269cb66481919afd4d54807e9c46) and this correction packet alongside the pinned Main/SM/#868 sources and the 2021 local-fraction paper. Require an explicit written verdict on:

- the precise response-complete, interventional measurement-independence assumption, rather than hidden full-world deterministic free-choice language;

- correct attribution of q and R-CONE to existing Bell and graph-cone results; falsify any claim of independent novelty;

- CHSH averaging, TV factor, local/nonlocal mixture, and all-histories data processing;

- apparatus/source symmetry and whether preparer/record access supplies a signalling channel;

- the important **single benchmark ε vs all-preparations η** quantifier separation;

- whether a proposed prepared long edge is actually generated and executable by a cited rule;

- classical fragment preservation, Born law, positivity, joint closure, operational no-signalling, resource costs, and no PR overcoverage.

**Suggested reviewer outputs:** ACCEPT, ACCEPT WITH CHANGES, REVISE with the source/section anchors, or an explicit bounded UNSOURCED disposition. No reviewer has returned any verdict in this ChatGPT turn.

**Next writer action after external independent review:** integrate only accepted scoped mathematical facts into the existing #1169 matrix / #1216 crosswalk, and pursue the **single physical precursor/paired-edge producer** only after its existing source and execution authorization gates. Do not invent a new physical posit, native run, PR, or merge to turn an existing negative source result into apparent progress.