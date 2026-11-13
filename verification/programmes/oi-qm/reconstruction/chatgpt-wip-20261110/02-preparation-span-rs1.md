**Paper-only writer assessment v1 · 9 November 2026 · NEW MATHEMATICAL LEMMA AWAITING INDEPENDENT REVIEW**

**Primary:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) at equal priority. **Links:** [#1143](https://github.com/amaybaum/incompleteness/issues/1143), [#868](https://github.com/amaybaum/incompleteness/issues/868), [#1220](https://github.com/amaybaum/incompleteness/issues/1220). Companion to [joint milestone v1](https://chatgpt.com/space/page_1a978cad60588191ac7a5aaf5bcefe1d).

**Question:** Does OI itself provide a physically justified reason for the deterministic hidden response of one separated measurement wing to depend on the distant setting, while the full locally accessible record histories remain operationally no-signalling and ordinary classical contexts remain admissible?

**Disposition from existing sources: UNSOURCED.** Main §3.3 already *chooses* the ontic-parameter-dependent option while retaining measurement independence as a posit, and SM §3.1 permits state-dependent graph geometry. Neither text supplies the complete prepared pair, physically executable isolated setting programs, a resulting nonlocal response, full-history balance, or a derived native Born law. The existing reviewed #868 paper identifies the same first pair/preparer source stop. This assessment does not manufacture such a mechanism.

**New bounded contribution in this writer draft:** a quantitative stability version of #868's exact preparation-affine-span diagnostic. It makes a sharp, testable statement about how close to no-signalling a deterministic nonlocal model can be over a sufficiently well-conditioned, affinely full set of admitted preparations. This paper proof is not a claim of independently reviewed mathematics, Lean formalization, empirical result, or universal OI obstruction.

# 1 Source read and outcome ledger

**Source corpus pin:** [main at cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481). The accepted #1143 and #1169 Pages are separate, later paper assessments and must not be described as merged at this commit.

| Source | What it already establishes | What it explicitly does not establish |
| --- | --- | --- |
| [Main §3.3, screened-local Bell theorem and H-Bell](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Main.md#L367) | The local causal-cone + common response-complete source hypotheses give CHSH ≤ 2. The proposed escape keeps setting independence and chooses ontic parameter dependence. The finite arbitrary-law construction can represent even PR behavior. | Neither Bell violation nor quantum-only bound follows from representability. The specific native prepared graph, full-history no-signalling and Bell response are open. |
| [SM §3.1, state-dependent geometry](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/SM.md#L100) | Allows the graph to vary with the actual state. Its explicit reversible ring has a bounded-range selector and admits local conditional coupling. Prepared long edges are a proposed extension, not the ring's existing mechanism. | No demonstrated physically generated distant pair edge, isolated wing instrument or Bell record law; a graph snapshot alone is not a full functional-dependency cone. |
| [Prepared-pair source, #868 §§3–5](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/prepared-pair-source.md) | Existing **balance lemma** gives no-signalling as a linear condition on a common preparation law over complete accessible histories. Existing **exact affine-span diagnostic** implies pointwise ontic parameter independence if no-signalling holds over an affinely full family. | Its pair-preparer and long-edge source stop is still open. Balance equations do not select the physical source or derive the quantum bound. |
| [Pair-operation source, #868](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/pair-operation-source.md) | Changing a configuration update or graph range does not automatically create an executable non-monomial observer operation. The finite configuration/positive-compression ceilings are conditional on the **unchanged operation interface**. | Neither a long-edge update nor a relabelled matrix is automatically a native quantum gate, an available branch, a coherent preparation or a source of Born probabilities. |
| [#1143 reviewed countermodel assessment](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218) | C0 obeys the weak observer baseline; the extra pure-joint/mixed-local condition E excludes full-simplex C0, but restricted affine C1 obeys E and still fails Bell. Ordinary classical observations survive both declared interface classes. | E, affine preparation restrictions and type sealing are not derived from OI. C1's Bell-local failure is not a universal deterministic no-go. |
| [#1220 accepted r1a resource contract](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f) | Source, controller, precision, memory, records and failure costs must be counted separately, across scales, before classifying simulation complexity. | The present BL obstruction and this new condition-number lemma supply no classical runtime lower bound. |

**Status labels:** the already accepted prior results are not reopened; the quantitative lemma below is **NEW / UNREVIEWED**; a physical OI-derived selection principle remains **OPEN / UNSOURCED**.

# 2 The source condition to investigate, not to assume

For each finite resource scale `n`, a prospective native physical tuple must provide:

- a finite response-complete source state `λ∈Λ_n` (with physically relevant preparer, apparatus and controller residuals);

- one fixed reversible update `F_n`, with any state-dependent graph determined by the actual full update, not merely a selected-edge snapshot;

- a family `𝒫_n⊂Δ(Λ_n)` of *physically produced*, setting-independent preparation laws, with producers, failure flags and renewal recorded;

- available local setting policies `x,y` and complete locally accessible histories `H_{A,n}^{xy}(λ),H_{B,n}^{xy}(λ)`, including adaptive continuation and relevant spent apparatus, up to the declared isolation window;

- explicit physical comparison to a classical fragment (repeatable register reads/copies) and to the Bell benchmark, under one common family rather than separate target-fitted laws.

Define the **native preparation-balance question**: is there a physical source restriction, independently established from the OI dynamics and embedded access, under which `𝒫_n` is closed under actually allowed preparations/continuations and every `μ∈𝒫_n` satisfies complete-history no-signalling, while some admitted isolated Bell test has CHSH greater than 2?

Mathematically, for fixed programs, #868 writes the no-signalling constraints as `C_n μ=0`. Replacing this by the *definition* `𝒫_n={μ:C_n μ=0}` would be target-defined fine-tuning, **not** a derivation. A candidate should instead produce `𝒫_n` from an independently justified physical process or conserved structural restriction, and only then prove `C_n μ=0` and the Bell facts.

**Classical preservation:** the common tuple must still support the explicit classical register preparation/measurement fragment. It need not keep all classically conceivable fine-grained hidden preparations available, and must not forbid ordinary classical readout in order to manufacture E or Bell. #1143 C1 proves that a thin set of preparations can preserve classical observations and yet remain Bell-local; thinness alone is not sufficient.

# 3 Definition: quantitative accessibility/spanning factor

Fix a finite response-complete ontic set `Λ` and a finite collection of physically admitted preparation laws `μ₁,…,μ_m∈Δ(Λ)` with full affine span `aff{μ_i}=aff Δ(Λ)`. Define their *affine reconstruction factor* (for this specified collection)

`K(μ₁,…,μ_m) := max_{λ∈Λ} min{∑_{i=1}^m |c_i| : δ_λ=∑_{i=1}^m c_i μ_i, ∑_i c_i=1}.`

As the family spans, every minimum is attained, `1≤K<∞`. The coefficients may be negative: these are **algebraic representations for the proof**, never physically allowed negative preparations. If the family is not affinely full, define `K=∞` for this diagnostic; that marks its **inapplicability**, not an actual infinity of physical resources.

For each wing and any two isolated policies differing only at the distant wing, let `p_{i}` and `p'_{i}` be the probability laws of that wing's **complete accessible history**, generated from the same `μ_i` under the two policies. Define

`η := max_{i, wing, distant-policy comparisons} TV(p_i,p'_i)`.

This is a maximum over a *fixed declared finite policy menu* and the admitted preparation collection. An observed Bell-marginal no-signalling check is weaker than this complete-history condition. The source law must be common across the compared policies; changing it would violate the comparison contract.

No definition above asserts an existing native OI process produces such `μ_i` or policies.

# 4 Proposition: robust affine-span locality threshold

**Proposition RS-1 (new paper proof; independent review PENDING).** Under the §3 finite deterministic-history and common-source hypotheses, if `Kη<1`, then each wing's **complete accessible history map is pointwise independent of the distant policy on all of Λ**.

**Proof.** Fix one wing, two distant policies and their deterministic maps `H,H':Λ→ℋ`. For each `λ`, choose real coefficients `c_i` representing `δ_λ` as in the definition of `K`. Applying the two history pushforwards gives a signed-measure identity

`δ_{H(λ)}−δ_{H'(λ)} = ∑_i c_i (H_#μ_i−H'_#μ_i).`

Taking total-variation norm on the zero-mass signed measures and using its triangle inequality,

`TV(δ_{H(λ)},δ_{H'(λ)}) ≤ ∑_i |c_i|TV(H_#μ_i,H'_#μ_i) ≤ Kη.`

Distinct point masses have TV distance exactly 1; equal point masses have distance 0. Thus if `Kη<1` the two maps must agree at this `λ`. Since `λ` and the comparison were arbitrary, all declared remote-policy changes leave the wing's complete local history unchanged, pointwise. □

**CHSH corollary (conditional).** Suppose the isolated experiment additionally has one response-complete setting-independent preparation, two binary first outcomes for each wing on every run, and policies implementing both setting choices. If RS-1's hypothesis holds for both wings for those policies, there exist `A_x(λ),B_y(λ)∈{−1,+1}` depending only on their local settings and the common `λ`. Then the existing screened-local CHSH argument applies pointwise, giving `|S_CHSH|≤2`. Thus RS-1 plus an affinely full, sufficiently well-conditioned experimentally available preparation family prohibits quantum CHSH, *without requiring that the hidden carrier be small or the computation be fast*.

**Contrapositive useful for selecting sources.** If a deterministic candidate with a common setting-independent preparation family has genuine remote-policy dependence at any response-complete `λ`, then any affinely spanning admitted preparation collection must have

`η ≥ 1/K.`

If a native candidate claims **exact** no-signalling (`η=0`) and Bell violation, the already established #868 exact-span theorem requires that its physically admissible law family not affinely span `Δ(Λ)`. RS-1 makes the finite-error tolerance quantitative. No such family or conditioning factor has been sourced yet.

# 5 Sharpness control and the growing-resource trap

**Algebraic sharpness (not a Bell model):** Set `Λ={0,1}`; for `0<t≤1`, take two admitted laws

`μ_+(0)=(1+t)/2,  μ_−(0)=(1−t)/2`,

with their complementary probabilities on `1`. Define two deterministic one-wing histories under a remote policy switch: `H^0(λ)=λ` and `H^1(λ)=1−λ`. Then for either `μ_±` the observable history TV difference is exactly `η=t`. The affine decompositions of `δ_0,δ_1` into `μ_+,μ_−` have minimal coefficient absolute-sum `K=1/t`. Consequently `Kη=1` even though the history maps differ at every ontic state. The strict inequality in RS-1 cannot be weakened to `Kη≤1`.

Choosing `t_n→0` produces a family with `η_n→0` while `K_n→∞` and ontic remote-policy dependence persists. This does **not** show a quantum violation, no-signalling in the exact sense, or any physically sourced OI process. It shows why small observational signalling error by itself does not select ontic locality without a scale-uniform preparation richness bound.

**Relation to #1216:** If the resource-indexed `K_n` stays bounded and the actual complete-history signalling defect tends to zero, RS-1 eventually enforces pointwise locality, and the [earlier CHSH distribution floor](https://chatgpt.com/space/page_1a978cad60588191ac7a5aaf5bcefe1d) then excludes convergence to the ideal quantum Bell benchmark. If `K_n→∞`, this *particular* theorem gives no such conclusion. Both conditions are mathematical and neither sources a full quantum interface.

**Extra source robustness lemma (elementary).** If a fixed reference law `μ₀` is exactly balanced for the given two history maps and another preparation `μ` satisfies `TV(μ,μ₀)≤δ`, then the corresponding two history laws from `μ` differ by at most `2δ`, by triangle inequality and contraction of TV under a fixed map. This is a sufficient continuity bound only: it does not certify physical preparation of `μ₀`, closure of allowed interventions, or exact no-signalling for all physical preparations.

# 6 Physical screen of the existing OI lead

The proposed state-dependent-geometry route changes the **ontic causal dependencies** if actual prepared long edges carry a distant setting to the other wing's readout within the measurement window. Main §3.3 permits this as a possible branch, but does not derive it from finite observer incompleteness.

The explicit reversible ring in SM §3.1 and the controller-lead loading study are **bounded-range**, with the ring's neighbour selector dependencies included in its functional causal cone. For separated settings/readouts outside one another's whole dependency cones, the screened-local proof applies. Conditional loading of its pre-specified `η` source or longer local memory cannot, by itself, violate CHSH. The arbitrary finite-law response carrier is not interchangeable with this specific ring.

A proposed **native prepared-long-edge** escape has to pass, in order:

| Gate | Required demonstration | Current source state |
| --- | --- | --- |
| **P: producer** | One fixed native update produces and, when required, renews a Bell-relevant pair preparation and any edge/field values; setting loaders draw from a common uncontrolled law | **UNSOURCED**; the ready/request producer, actual pair-preparer and renewal are missing |
| **G: geometric path** | The *full functional dependency graph*, including selector inputs, supports remote setting influence across the actual isolated time window | **PROPOSED**, not proved by a prepared-edge picture or by ring transport |
| **O: available operation** | The setting switches, induced response, meter coupling and record cuts are physically executable under the specified observer-level operation interface | **UNSOURCED**; changing graph range does not alone bypass operation-source ceilings |
| **B: accessible-law balance** | Every admitted physically produced law and every relevant isolated adaptive/local history satisfy actual no-signalling; expose controller/preparer logs, heralds and failures | **OPEN**; #868 provides equations but not physical satisfaction or closure |
| **Q: quantum selection** | Reproduce CHSH quantum benchmark **and** exclude PR/superquantum controls, derive native Born probabilities, valid product tests and composite/reuse closure | **OPEN**; nonlocal response plus no-signalling is insufficient |
| **R: resources** | Bound preparation, source sampling, controller clock, precision, output histories, failure/restoration, and scaling in the succinct target input | **UNDETERMINED**; use #1220 r1a, no efficiency or hardness classification |

A *physical source condition* should be proposed only if gates P/G/O can be independently justified without importing a target table or quantum instruments. Until then B and Q are comparison obligations, not a law to impose by definition.

**Classical-fragment control:** the rule must keep repeatable `q`-register (or other explicitly defined classical-register) preparations/reads and their allowed finite compositions. A Bell-targeted pair configuration can have different access from a classical register, but the distinction must arise from one derived physical apparatus/preparation rule. E alone and an arbitrary sealing contract do not pass this test.

# 7 Main conclusions and precise next proof obligation

**Already supported and not newly proved:** Main's screened-local Bell bound; finite-law representability; selected ontic parameter dependence as an *option* with measurement independence stipulated; SM's reversible state-dependent ring; #868 exact complete-history balance / affine-span diagnostic; #1143 C0/C1 insufficiency; #1220 open resource classification.

**New paper-level conditional argument, review pending:** the finite `Kη<1` threshold forces pointwise independence for a full-affine-span preparation collection. With the declared Bell setting assumptions it implies CHSH≤2; the two-state algebraic example saturates the strict threshold. This is an obstruction for a *specified family with measured/proved `K,η`*, not a universal bound on the OI substratum.

**What OI itself currently supplies:** permission for state-dependent geometry and noninjective embedded observations, but no sourced rule selecting a sufficiently restricted physical preparation family, generating the required pair coupling, or enforcing the complete-history cancellation. The first missing positive physical producer remains the prepared-pair process, with the ready/request source/renewal a separate **controller-lead-specific** gap.

**Next paper proof obligation if authorized:** choose **one already motivated native candidate** (the SM preparation-indexed coupling route is the current source lead), specify `(F_n,𝒫_n,H_{A,n},H_{B,n})` and its classical fragment from independent physical clauses; demonstrate (or explicitly stop at the earliest unavailable step) how the apparatus actually generates the preparation constraint; if sourced, derive a complete local-history balance invariant under available adaptive continuations without choosing `𝒫_n` by solving `C_n μ=0`. Only then test Bell quantum coverage, Born, superquantum exclusion and resource growth. A physically available outcome **UNSOURCED** is a legitimate stop; no new rule is imposed.

Do not reopen #945's finite-bit theorem proof in this unit. #1216's approximation, #1169's physical sourcing and #1220's cost question remain independently classified and equally prioritized where specified.

# 8 Independent review packet

**Independent review status: NOT PERFORMED.** Writer-side algebraic checks and source reading do not constitute independence. No further scientific execution, formal proof run, new GitHub branch/PR, F/E/dispatch, physical-premise adoption, manuscript edits or merge is authorized or performed here.

Request an external/separate reviewer to:

1. Check the exact source quotation and implied status in Main §3.3, especially that *selection of an ontic-parameter-dependent branch is not a sourced mechanism* and measurement independence is a posit.

2. Confirm §4's `K` minimization is finite and attained given affine spanning, that signed affine decompositions work with pushforward and TV, and that the strict threshold `Kη<1` forces equality of deterministic complete-history maps. Check both-wing and all-policy quantifiers, uniformity across resource sizes, and the setting-independence requirement of the CHSH corollary.

3. Check §5's two-state sharpness coefficients, history TV, and the lesson that `K_n` may diverge. Independently challenge any hidden assumption that all mathematically defined preparations are physically produced.

4. Verify any prepared graph used in a later candidate is the **full dependency graph** including state-dependent selector inputs, not a chosen edge snapshot; check the actual causal separation time and whether setting correlations are present in response-complete `λ`.

5. Check no-signalling on **full accessible histories**, including heralds, failures, preparer/controller logs and permitted indirect recovery. Ensure no target-fitted `Cμ=0` is presented as an OI-derived law.

6. Confirm E's insufficiency and classical-preservation control from accepted #1143; keep valid test probabilities, admitted-state closure, native Born and Bell/quantum compatibility separate.

7. Check #1220 accounting is neither omitted nor misused as a claim about BPP/BQP or physical complexity.

Suggested review verdicts: ACCEPT, ACCEPT-WITH-NITS or REVISE, with verbatim blockers and source pointers. An accepted **paper argument** would still not establish a physically sourced Bell mechanism. No user-specific review request was dispatched, no independent reviewer was simulated, and all existing owner/project/repository gates stay unchanged.