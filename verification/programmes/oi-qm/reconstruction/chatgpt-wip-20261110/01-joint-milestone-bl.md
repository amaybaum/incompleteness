**Writer draft v1 · 9 November 2026 · PAPER ONLY · NOT INDEPENDENTLY REVIEWED**

**Issues:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169), [#1143](https://github.com/amaybaum/incompleteness/issues/1143), [#1216](https://github.com/amaybaum/incompleteness/issues/1216), [#1220](https://github.com/amaybaum/incompleteness/issues/1220). **Equal foundational emphasis:** #1169 and #1216. Complexity is the parallel accounting track, not a reason to prefer exact or approximate equivalence.

**Scope:** focused additive amendment to the already independently accepted [#1169 dependency matrix](https://chatgpt.com/space/page_9580d355639c81919a21ae4d8af34201), incorporating the later independently accepted [#1143 countermodel assessment](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218), the already accepted #1216 r4a assessment (off main), and the accepted [#1220 r1a resource contract](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f). The earlier [selection addendum](https://chatgpt.com/space/page_844e90bfb4708191a4d3917c5278bf63) also remains accepted in its narrower planning scope.

**New claim in this draft:** a fixed, analytically derived operational distance from the ideal CHSH experiment for the setting-independent Bell-local class; a matching outcome-only local example shows the constant is optimal for that comparison class. This is a scoped mathematical obstruction, not an OI-to-QM derivation, empirical finding, native mechanism, numerical run, formal kernel theorem, or complexity separation. Independent mathematical and source review remain **PENDING**. No GitHub content or existing accepted artifact is changed by this draft.

# 1 Decision question and preserved starting point

The physical hypothesis under investigation is selection of admissible **dynamics–preparation–controller–measurement–access tuples** inside one deterministic substratum, with embedded observers seeing incomplete information. Different actual measurements can yield classical or quantum operational behavior. A successful principle must preserve honest classical-register operations and their histories, produce quantum test families through one sourced law, and survive adaptive switching and joint composition. It must not hard-code a quantum probability table or exempt a classical-only model by fiat.

The already reviewed #1143 assessment shows:

- **C0 (full classical-simplex swap-memory completion):** satisfies the stated finite observer/record baseline B0, retains ordinary classical contexts, and does not cover the target Bell experiment.

- **E (existence of an operationally pure composite with a mixed local marginal):** excludes C0's full classical-simplex completion, but is only a proposed preparation condition and is **not derived from OI**.

- **C1 (uniform restricted affine-symplectic model):** satisfies B0 plus E, admits a consistent classical fragment and finite-size compositions and an interference-like analogue, yet remains Bell-local under explicitly local separate-wing operations and setting-independent hidden preparation. Thus it does **not** cover the specified quantum Bell target. The typed sealing/access rules protecting its restricted preparation space are **posited**, not sourced by OI.

These results test insufficiency, not the impossibility of deterministic quantum-capable physics. In particular, ordinary classical observed behavior is a required subtheory, not a pathology to be excluded.

# 2 Focused amendment to the #1169 matrix

This table is **an additive draft amendment, not a replacement or retroactive re-review** of the accepted D0–D11 matrix. Status words describe evidence, not owner authorization.

| Proposed row | Condition, scope, and carrier | Status after the accepted #1143 finding | Missing physically sourced obligation |
| --- | --- | --- | --- |
| **D12: observer-selection baseline** | B0 on finite reversible world, embedded visible read, memory, one declared program family, histories and finite compositions | **DISPROVED AS SUFFICIENT** for QM target: explicit C0 and C1-style classical countercontrols | A new independently derived admissibility restriction; noninjective present read alone is insufficient |
| **D13: relational preparation E** | Accessible operational purity of an admitted joint preparation with mixed one-wing restriction | **CONDITIONAL separator; DISPROVED AS SUFFICIENT**: it excludes full-simplex C0 but is satisfied by restricted C1 | Physical availability and production of such preparations; no quantum purification theorem is mistaken for an OI-preparation theorem |
| **D14: Bell-locality + setting independence (BL)** | Two separated local readout wings; shared `λ` distributed independently of later independent settings; wing outputs depend only on local setting and `λ` | **PROVED scoped obstruction in this draft, PENDING independent review**: ideal CHSH histories are at least `(√2−1)/4` TV away on the specified setting/output marginal | If a candidate seeks quantum CHSH, it must identify which premise of BL ceases to apply and physically source that change while preserving operational no-signalling |
| **D15: approximation/coverage bridge** | #1216 Level B common native family, complete accessible histories, arbitrary finite precision and uniform growth | **CONDITIONAL negative implication** from D14: no vanishing complete-history error for any family whose identified CHSH marginal remains BL at each size. Does not constrain general OI families | A sourced correspondence across sizes, explicit available branches, coverage/soundness, Born law and composition; #945 finite-bit repair remains separate |
| **D16: cost crosswalk** | #1220 two ledgers for same actual proposed native interface and full records | **OPEN for native complexity**; the D14 obstruction is representational/operational and independent of run time | Physically generate ready/request precursor, clock/herald, repeatable supply, complete records, precision, and bound all failure/renewal costs |

**Lead-specific source stop, not a universal no-go:** the existing controller/preparation-loading lead generates the required output only with a **supplied shared ready/request precursor**. Its physical producer and regeneration/renewal are missing. This is separate from the broader D12–D15 question of which OI-derived selection condition could exclude both C0 and C1. A proposed native non-monomial operation also leaves native Born probabilities and composite closure independently open.

**Retained prior rows:** D2 exact level-one FI-1 is not obtained from mere bare-system operator admissibility; D3 phase is not independent of every possible mixing route; D4 H-Bell remains separate; D5 Born exponent is conditional on imported hypotheses; D6 product-test validity, closure and quantum compatibility are different; D8 Level A simulation is not Level B sourcing, with fixed-b realized-law constants still open; D9 complexity remains undetermined. No older status is promoted here.

# 3 A declared quantitative benchmark and model class

Fix a single nonadaptive two-wing CHSH test. Settings `x,y∈{0,1}` are sampled uniformly and independently after the joint preparation; outcomes `a,b∈{−1,+1}`. Take the quantum target `Q` to have a Bell-pair preparation `|Φ⁺⟩`, A's measurements `Z,X`, and B's measurements `(Z+X)/√2,(Z−X)/√2`. The declared Born-rule *comparator* has

`s₀₀=s₀₁=s₁₀=+1, s₁₁=−1` and `E_Q[ab|x,y]=s_xy/√2`, so `S_Q=E₀₀+E₀₁+E₁₀−E₁₁=2√2`.

A candidate class `BL` has one setting-independent joint hidden-variable law `ρ(λ)` and local response kernels `P_A(a|x,λ), P_B(b|y,λ)`, with

`P(a,b|x,y)=∫ρ(dλ) P_A(a|x,λ)P_B(b|y,λ)`.

All local apparatus seeds and retained local memory may be absorbed into `λ`. Deterministic responses are a special case. Each candidate may use an arbitrarily large shared hidden space, finite controller, local adaptive machinery and local record retention; the stated one-shot Bell test still factors if no between-wing influence during the choices/reads and no setting dependence of `ρ`. Every relevant failure must be exposed in a **complete history**, not removed by postselection. A missing outcome can be assigned a fixed local `±1` value for this witness; the missing-outcome flag remains an accessible part of the full history.

**Important classification:** BL is a **conditional test-class hypothesis**, not a theorem of observational incompleteness or of every deterministic substratum. If native OI yields ontic parameter dependence, retrocausal/setting correlations, or another non-BL interface, that family is outside this obstruction's hypotheses and must be analyzed in its own complete-history/no-signalling scope.

# 4 Proposition: a nonvanishing approximation obstruction

**Proposition P-BL (paper proof; independent review pending).** Let `P_H` be the complete accessible-history law of any BL model with the declared uniform setting distribution, and let `Q_H` be a quantum benchmark history law with the declared CHSH setting/outcome marginal and the same setting distribution. The record alphabet may contain additional information, resets and explicit failure flags. Suppose the outputs used in the witness are available local functions of each wing's records, with missing outcomes filled by a fixed local convention. Then

`TV(P_H,Q_H) ≥ (2√2−2)/8 = (√2−1)/4 ≈ 0.10355339.`

Here `TV(P,Q)=½∑|P(h)−Q(h)|` on the common countable history alphabet; for continuous extensions the usual supremum-over-events definition applies.

**Proof.** Extend local response randomness into `λ`. For each `λ`, four counterfactual response values `A₀,A₁,B₀,B₁` exist on one joint probability space. The pointwise CHSH expression `A₀(B₀+B₁)+A₁(B₀−B₁)` is `+2` or `−2`, so averaging with the **same** `ρ` for every setting gives `S_P≤2`. On the setting/output joint law define `f(x,y,a,b)=4s_xy ab` (range `[−4,4]`). Uniformity gives `E_Q f=2√2` and `E_P f=S_P≤2`. For any bounded `f`, `|E_Qf−E_Pf|≤(sup f−inf f)TV(P,Q)`. Thus `2√2−2≤8TV(P_{xyab},Q_{xyab})`. Projection from complete histories to `(x,y,a,b)`, including the fixed local failure-filling map where needed, cannot increase total variation. The claim follows. □

**Uniformity in growing resources.** If every realization at resource index `n` has this Bell-local marginal, the same lower bound holds for every `n`, no matter how `|λ_n|`, the controller tape, hidden memory, tick budget or simulator time grow. Hence `TV(P_{H,n},Q_{H,n})→0` is impossible for this benchmark under **unchanged BL assumptions**. This is not an obstruction to a larger class that sources genuinely different setting dependence or nonlocal hidden responses.

**Robust extension.** If the candidate's setting/output law is within `κ` in TV of some BL law with uniform settings, then by the triangle inequality it is at least `max{0,(√2−1)/4−κ}` away from the ideal quantum law. The amount `κ` must be independently bounded; it is not a surrogate for an unmeasured physical mechanism.

# 5 Sharpness and relation to the tested countermodels

The constant is **optimal for the one-shot 2×2 setting/output comparison against the full Bell-local class**. Define for the same setting convention

`Q_v(a,b|x,y)=¼(1+ab·v·s_xy)`.

The ideal quantum target is `v=1/√2`. A Bell-local box `L=Q_{1/2}` is obtained by uniformly mixing the eight deterministic strategies that attain CHSH `+2`: choose one of four cells to be the unique losing setting pair, and choose one of the two simultaneous output-sign flips. Each strategy is a pair of local preassigned response tables; the mixture gives correlation `s_xy/2` and zero single-wing means. For each setting, `TV(Q_{1/√2}(·|x,y),Q_{1/2}(·|x,y))=(1/√2−1/2)/2`. Uniformly averaging the settings yields precisely `(√2−1)/4`.

This supplies a constant-size **mathematical local-box sampler** using three shared fair random bits for the strategy index, plus the independently supplied setting draws. It does **not** establish that the particular C0 or C1 interactions produce this optimal box, and does **not** establish any native physical source for the shared random bits.

The accepted #1143 paper already establishes that C0 and C1 lie in the BL class for the specified *separate-wing, setting-independent* experiment. P-BL adds a **robust quantitative impossibility of arbitrary-precision coverage** under those same hypotheses, rather than merely restating the exact CHSH failure. The result does not show that all C0/C1 complete histories are incompatible with quantum subtheories, or that there are no other quantum-capable deterministic OI realizations.

# 6 Resource-accounting implications for #1220

For the actual candidate interface, the accepted #1220 r1a contract requires **separate physical and algorithmic ledgers**. A physical implementation's site/supply/memory/tick cost is not interchangeable with a classical algorithm's preparation-sampling/runtime cost.

| Term | BL countermodels and P-BL | Pending native OI source |
| --- | --- | --- |
| Preparation `T_prep`, source draws, `ρ(λ)` | Mathematical law specified; the sharp local-box control admits a constant-bit sampler | Physical preparation of the declared source and its distribution across actual wings not established |
| Ready/request and renewal | Not needed for the abstract one-shot Bell-local inequality | For the current controller lead, shared precursor production and valid renewal are **ABSENT/UNSOURCED** |
| Native update/control `T_update,T_ctrl` | Any complexity and state-space size allowed without improving BL's approximation floor | Specific physically executable program family and across-size compiler unproved |
| Readout, local failure flags, records `T_read,T_record` | Observed outcomes must be available locally; failures counted rather than postselected | Complete apparatus/preparer/controller/history interface remains necessary |
| Accuracy `ε`, arithmetic precision `b`, resources `N,T,H` | For `ε<(√2−1)/4`, BL fails **even at unlimited cost** under its assumptions | No bound on `N(L,ε)`, `T(L,ε)`, `b(L,ε)` for an OI-derived quantum-complete family |
| Born, composition, scalable coverage | Local hidden priors and a matched marginal are not native Born derivation; BL is a negative quantum-coverage test | Native Born rule, two-system closure and all-history soundness remain distinct open obligations |

**Separation of operational and algorithmic outcomes.** P-BL is a lower bound on the **distance of attainable observable laws**, not on classical computation time. A BL model might be efficiently or inefficiently simulated and still miss the target quantum law. The three #1220 alternatives—efficient native weak simulation, a scoped complexity obstruction under its explicit assumptions, or undetermined—therefore remain legitimate for differently specified interfaces. No implication `BQP⊆BPP`, unconditional hardness, or hardware obsolescence follows.

For a proposed sourced Level-B family, use the accepted error budget

`TV(Q_H,S_H) ≤ Δ_cov + η₀ + ∑_j η_j + η_D + δ`

only when each component is actually established: `Δ_cov` for physical coverage, `η₀` initial sampler, `η_j` per-step kernels under the retained adaptive context, `η_D` decoder, and `δ` explicit stop/truncation. For a **BL** candidate targeting this CHSH test, `Δ_cov≥(√2−1)/4`; reducing arithmetic or finite-bit error cannot erase that physical gap. This does **not** settle #945's separate clipped-and-normalized finite-bit proof defect.

Do not infer expected preparation attempts from a conditional ensemble mass alone: the source must supply a physically accessible success flag, renewal, and a uniform conditional success bound before a geometric-cost estimate is valid. No such certificate has been identified for the ready/request source.

# 7 What remains for a positive selection principle

This draft gives a **negative**, rather than a positive, milestone for the condition BL. Any candidate intended to cover quantum CHSH must show *where and why* BL ceases to apply to a native realization. It may not simply attach a target-specific nonlocal response table or assume Born probabilities. The next independently sourceable obligation is therefore:

> Starting with the declared finite OI update and embedded apparatus, identify one physical preparation/controller/read-access mechanism which (i) preserves the classical-register fragment, (ii) admits the declared separate-wing Bell experiment under one common scalable tuple, (iii) supplies an independently motivated reason that one BL premise is inapplicable, (iv) still proves operational no-signalling on complete accessible local histories, and (v) specifies native record probabilities, heralds and reuse with costs.

Failure to identify such a mechanism should be reported **UNSOURCED**, not counted as proof of a universal OI no-go. Breaking BL is **necessary only for the declared Bell-violating benchmark** and not sufficient for all QM. H-Bell, Born exponent 2, coherence, joint-state closure, experiment switching, and all-history soundness remain separate work.

The current controller-lead precursor gap should be tracked as **lead-specific**: source one shared ready/request producer plus renewal before treating the already modeled local loading as a reusable physical device. This cannot be promoted to a unique earliest gap for the whole selection programme.

# 8 Independent-review request and exact acceptance criteria

**Review state: NOT YET REVIEWED.** The new proposition and crosswalk were composed in ChatGPT against the cited accepted Page/GitHub source snapshots. The writer's own proof check is **not** an independent review.

Request an independent reviewer to assess:

1. **Quantifier and locality audit:** does the #1143 accepted C0/C1 Bell-local source cover the exact setting-independent two-wing class here? Are remote influences, apparatus-access restrictions, postselection, and exogenous settings exposed rather than silently excluded?

2. **Mathematical proof:** check the `f=4s_xy ab` range and expectation, total-variation dual inequality, complete-history data processing, sharpness of the eight-strategy local mixture, and the `κ` robust extension. Look for a stronger counterexample when the full history includes failures.

3. **Scope under growth:** verify that the bound is only for families staying BL at every resource size, and that no direct/encoded carrier or bare-system/level-one FI-1 transport is assumed.

4. **Provenance:** ensure D12–D16 are clearly **new draft rows**, older accepted D0–D11 unchanged, #1143's E and C1 are not claimed physically sourced, #1216 r4a is not called integrated, and #1220 resource classifications are preserved.

5. **Costs and independence:** verify that a fixed probability distance is not mislabeled a time lower bound; physical source, success flags, Born rule, complete-history no-signalling, and quantum composition remain unsolved. #945 remains outside this unit.

**Suggested verdicts:** ACCEPT / ACCEPT-WITH-NITS / REVISE with exact blocker locations and assumptions. No reviewer acceptance or publication is represented by this writer draft.

**Owner and execution gates:** unchanged. No scientific or numerical experiment, Lean/kernel proof, native dispatch, F/E, freeze, changed physical-premise adoption, GitHub branch/PR, manuscript change or merge is performed here.

**Source ledger:** [reviewed #1169 matrix](https://chatgpt.com/space/page_9580d355639c81919a21ae4d8af34201); [reviewed #1143 C0/C1/E study](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218); [accepted #1220 r1a](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f); [#1216 issue and r4a handoff](https://github.com/amaybaum/incompleteness/issues/1216); [#1143 Bell/Born corrections](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6682500558); [baseline Main at the accepted matrix's pinned SHA](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Main.md). General CHSH comparator check: [IBM Quantum tutorial](https://quantum.cloud.ibm.com/docs/en/tutorials/chsh-inequality) and [Wolfram MathWorld](https://mathworld.wolfram.com/CHSHInequality.html).