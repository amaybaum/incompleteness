*Recorded by the coordinator from the independent reviewer's report, verbatim, because the reviewer's tool refused report files. `S` in paths below is the session scratch directory, not retained.*

# Independent review of the Introduction corpus audit (#942, `audit/intro-corpus-20261026` at `d9e0e02f`)

**Reviewer:** independent agent. I took no part in steps 1–5 of the audit.
**Objects:**
- `papers/Introduction.md` at `4a260ca9`. I re-hashed it: sha256 `beb0a520…b936feb8`, which matches.
- Corpus at `eae01647`. Read from `S/tree939`, with `git show eae01647:` for `verification/programmes/**` and for `papers/oi_lattice_code/foundations/*`, which are missing from the extraction.
- `main` is now `02e73e56`. The only change from `eae01647` is AGENTS.md (+40 lines, "Whole-framework scope"). No manuscript, Lean or programme file differs, so the audit's corpus commit is still current.

**Rules applied:** AGENTS.md at `02e73e56`: Code Review Rules (Whole-framework scope, Claim/evidence boundary, Exactness and controls, verification layers), §A.19, §A.25, §A.30, §A.32–§A.34.

**How I checked:**
- I re-opened every cited source myself rather than using the audit's quotations.
- I did not build Lean or LaTeX. I made no commits, pushes or edits.
- Scripts that write files were run on a scratch copy at `S/rv/audit`.

## Verdict: ACCEPT WITH CHANGES

The audit is thorough and mostly correct:
- The claim inventory is complete.
- The matrix merges and renders reproducibly.
- Every Appendix A declaration is at its stated line.
- I confirm 44 of the 47 non-FAITHFUL verdicts in substance, and all 40 sampled FAITHFUL rows.

Five scientific defects must be fixed before the audit drives the revision of #918:
1. **R-01 (Page curve).** GR Theorem A.8, as stated, has no instance. R-01's replacement text still leads with the quantified Page-value conclusion as a conditional result.
2. **R-02 (memory vs indivisibility).** The replacement swaps an overbroad negative ("no unconditional implication") for an overbroad positive ("(2) implies (1)"). The implication needs assumptions that the text omits.
3. **R-07 (ε-realization).** The domain and construction are under-specified, and "Approximately, the converse holds" misdescribes the result.
4. **R-06 (substratum results).** The modelling premise is not stated: a bijective intervention acts as a permutation operator, or a monomial one once the phase is stipulated. The machine-checked label covers the substratum class as formalized, and the text should say so.
5. **Missed: I-291** asserts "the fixed-dimension form is false" on numerical evidence that does not cover the claim's scope.

There are also four audit-internal consistency defects (RC-9 to RC-12). The exact list of required changes is at the end.

***

## 1. Reproducibility and coverage

**Scripts.**
- `matrix/scripts/merge_matrix.py`, run on the scratch copy, gives `rows 409 want 409 missing [] extra []`. The duplicates are I-123 and I-124 (B2 kept). The regenerated `matrix.json` is byte-identical to the committed one.
- Verdicts: FAITHFUL 362, IMPRECISE 36, UNDERCLAIM 6, MISCITED 3, UNSUPPORTED 1, OVERCLAIM 1.
- `render_matrix.py --check` reports "MATRIX.md matches matrix.json".
- `scripts/C-render-md.py`, run into scratch, reproduces CONSISTENCY.md exactly. COMPLETENESS.md differs at line 168: the generator `scripts/C-completeness-data.py:232` still has "CON-04 … CON-05 … CON-06" for CMP-10. The committed JSON and MD were corrected to CON-17–19 by hand. Regenerating would bring the defect back (RC-10).

**Claim inventory.** I read the Introduction line by line against `claims.json`. I found no omitted substantive claim. The CLAIMS-README exclusions are justified (titles, notation, signposts, metadata, HTML comments). Two of them are worth noting:
- L36, |C_V| ≥ 2: carried as a hypothesis note and O-18.
- L261, Main's title: carried as OD-1.

All 43 "Current (Lnn)" spans in FINDINGS are verbatim substrings of their lines; I checked this mechanically.

**Direction sub-claims.** The 24 sub-claims cover every displayed equivalence:
- the set equalities I-002 and I-063;
- the iffs I-011, I-100, I-105, I-132, I-139 and I-336;
- the "exactly" restatements I-296 and I-297;
- the "conversely" pair I-153.

For I-153 I checked that the two cited declarations compose to an equivalence:
- `bridge_traj` gives: same one-step matrix ⇒ same root-conditioned trajectory laws.
- Equal trajectory laws give equal rooted families.
- `rooted_eq_iff_slice_eq`.mp then gives equal matrices.

**Sample selection** (FAITHFUL ids, `random.Random(20261026)`):
- Kernel stratum: FAITHFUL rows with proof_status proved-kernel, section Appendix A or §2–§3, and a `lean:` chain source. There are 87. I took 15 with `rng.sample`:
  - I-061, I-068, I-072, I-082, I-097, I-117, I-144, I-145, I-149, I-153.b, I-320, I-328, I-334, I-340, I-344.
- Then 25 from the remaining FAITHFUL rows, with the same generator continued:
  - I-028, I-036, I-069, I-081, I-115, I-126, I-154, I-163, I-175, I-183, I-184, I-192, I-193, I-212, I-213, I-226, I-228, I-237, I-244, I-250, I-288, I-290, I-303, I-349, I-355.

***

## 2. Owner priority 1: the Page curve (GR App. A, Thms A.7–A.9; BHb C1, C2, C6)

**What GR proves.**
- **A.7** (GR.md:811–813). An effective-purity estimate for ρ_VB on t ≪ τ_B^D, starting from "a definite initial state" (a configuration).
- **A.8** (GR.md:817–841) has two parts:
  1. A cycle-counting lemma, proved on paper and unconditional: if at most a fraction η of shell states are atypical, then at most (ln d_min/ε)·η of initial conditions on Σ_E lie on bad cycles.
  2. The step "atypical fraction ≤ η = e^{−c d_min ε²}", which is H-scramble. GR:831–835 itself says this does not follow from bijectivity or uniform cycle counting.
- The counting runs over configurations s ∈ Σ_E = C_B × C_R (GR:837–841, "initial conditions on Σ_E"). The B|R bipartition is aligned with those coordinates.

**What holds unconditionally in that setting.**
- Every orbit of a configuration consists of configuration basis states, which are product states across the aligned cut. So S(ρ_R) = 0 at every step, for every bijection. Sources: GR:833; BHb C1, a one-line proof: P_π maps basis vectors to basis vectors.
- Hence:
  - H-scramble fails for every bijection;
  - the atypical fraction is 1;
  - the counting lemma's bound is vacuous;
  - A.8's conclusion is false for every counted initial condition (time average 0 ≠ S_Page > 0 for d_B, d_R > 1).
- A.8 is therefore true only vacuously. It has no instance in the setting it counts, and the same holds for A.9, which inherits A.8.
- Also unconditional:
  - **BHb C2:** for any initial state, the entanglement under any permutation at an aligned bipartition is at most H(p₀). A Page-level value therefore needs an initial superposition over at least e^{S_Page} configurations, or a non-aligned bipartition.
  - **BHb C6(b):** S_Page enters only through the Haar ensemble that H-scramble posits.
  - **BHb C6(c):** the full-dimension Page value is wrong on proper energy shells, and the direction of the error depends on the shell.
- GR:835 attributes the failure only to "the setting of Theorem A.7's proof". The anchor is A.8's own counting (CON-01, correct, high).

**Is R-01's replacement accurate?** It is true sentence by sentence but presents the result wrongly:
- It leads with "Under H-scramble … equals the Page value … for all but an exponentially small fraction of the initial conditions the theorem counts".
- It then says H-scramble fails for exactly those initial conditions.
- So the reader receives a conditional whose antecedent is false wherever it is evaluated, framed as a result.
- It omits the stronger unconditional fact, that the conclusion itself fails on every counted orbit (S = 0).
- It omits the quantitative content that survives, BHb C2.

Under the Claim/evidence boundary (conditional vs vacuous) and §A.30 (remove the assertion; keep the derivation), the Introduction should not state A.8's quantified conclusion as a result.

**Matrix errors on this point.**
- **I-225** has a `refuted` link in its chain, yet proof_status is "conditional" and the verdict IMPRECISE. That violates the weakest-link rule. It should be OVERCLAIM, with status "unsupported as stated (vacuous conditional)".
- **I-223** ("is a conditional result") and **I-286** ("whether H-scramble … hold[s]", in §6.3) are rated FAITHFUL. Both should be IMPRECISE: in the counted setting H-scramble is settled false, not open. The open question is whether the substratum supplies a superposition or a non-aligned cut on which it could hold.
- CMP-25 (BHb C2) should be required, not optional.

**Required R-01 text (L162, replacing the two sentences):**
> Theorem A.8 of [GR] derives the Page value $S_{\rm Page}(d_B,d_R)$ for the full-cycle time average of the radiation's entanglement entropy, at the bipartition of each stage held fixed and up to its correction term, from the scrambling hypothesis H-scramble, that the orbit ensemble equidistributes over quantum pure states on the shell; the Page value enters only through that hypothesis [Pag93; GR, Thms A.8–A.9; BHb, C6(b)]. The theorem counts initial configurations, with the bipartition aligned to the configuration coordinates; every state on such an orbit is a product state, so the radiation entropy is zero at every step, H-scramble fails for every bijection, and the theorem has no instance in that setting [GR App. A.7; BHb, C1, C6(a)]. Under a bijection, the entanglement at an aligned bipartition never exceeds the entropy of the initial configuration distribution [BHb, C2], so a Page value requires an initial superposition over at least $e^{S_{\rm Page}}$ configurations or a bipartition not aligned with them; neither is specified, and H-scramble is not established.

**Consequential edits:**
- I-223, L162: "…addresses recovery under its own conditions, which are not established".
- I-286, L183: "whether the substratum supplies an initial superposition or a non-aligned bipartition on which H-scramble holds, and whether H-decouple holds".
- The abstract's "the framework's Page curve is not established" stays accurate.
- OD-9 (restating A.8 in GR) remains the right corpus fix. R-01 does not depend on it.

***

## 3. Owner priority 2: memory and non-Markovianity (R-02)

**Definitions in force.**
- Intro L72: M_t := I(X_{<t}; X_{t+1} | X_t).
- Main's Characterization theorem, condition (ii) (Main:518 area): "non-Markovian … at some order k … I(X_{<k}; X_{k+1} | X_k) > 0".
- By Main's own definition, then, non-Markovian on a horizon is the same as M_t > 0 for some t in it. That M_t = 0 for all t is the Markov chain property is the standard conditional-independence reading, via the vanishing criterion [CT06], which is not machine-checked. **So "M_t > 0 at some t" and "non-Markovian" coincide under the Introduction's and Main's definitions.** Either wording is licensed, provided M_t is used as defined at L72.
- Divisibility (Intro L90 and the kernel `CausalReadback.PDivisible`): rooted at 0. Γ_t has rows indexed by x₀, and for all s < t ≤ n there is a row-stochastic Λ with Γ_t = Γ_s Λ.

**The direction R-02 needs, with its assumptions.**
- Let a multi-time visible law on {0,…,n} be given over a finite alphabet, and let every initial value x₀ in the rooted family have positive probability.
- Suppose M_t = 0 for all 0 < t < n (Markov).
- Then for s < t ≤ n, P(x_t | x₀) = Σ_{x_s} P(x_s | x₀) P(x_t | x_s), with stochastic Λ = P(x_t | x_s) on supported x_s and arbitrary stochastic rows elsewhere.
- So the family is P-divisible on {0,…,n} (Main:606, "Markov implies P-divisible (chain factorization)"; RHP14 Cor. 2.1 per the mapper).
- Contrapositive: P-indivisible on {0,…,n} ⇒ M_t > 0 for some 0 < t < n. The rooted form is fine, since the two-time Λ(t,s) of a Markov chain composes from time 0.

**The assumptions are load-bearing.**
1. *Positive-probability roots.* The kernel's `rootedMap` (CausalReadback:188) defines a row for every root from (φ, prior), whatever the law of x₀. Counterexample with a zero-mass root: take the two-card game with x₀ fixed at a. The rooted family is P-indivisible (Γ₁ = ½J, Γ₂ = I), but the process from a (X₁ uniform, X₂ = a) is Markov, with every M_t = 0.
2. *The family must come from a multi-time visible law.* §3.1's notion (2) also covers population families of quantum channels; the Hadamard family at L106 is one. Such families have no multi-time law, so M_t is undefined for them.
3. *Time range.* The memory is somewhere in (0, n). For Theorem 3, n is the return time, so this memory need not lie in Main's "accessible" window (k τ_S ≪ t_R).

**R-02's finding is correct**: "no unconditional implication holds among them" is false. **Its replacement is not.** "(2) implies (1) at some time" omits assumptions 1–3.

**Required R-02 text (L106):**
> Three notions are distinct [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. For the rooted family of a visible law in which every initial value has positive probability, a law with $M_t=0$ for every $0<t<n$ is P-divisible on $\{0,\dots,n\}$, so P-indivisibility there implies $M_t>0$ for some $0<t<n$ [Main §3.4, Remark (two notions of memory)]; the converse fails (Appendix B.2).

This states exactly the direction that holds, and nothing about (3).

***

## 4. Owner priority 3: quantum reconstruction (R-06, R-07, and the §3.4 obstruction)

**Kernel statements, read and confirmed at `eae01647`:**
- `realizesSealedOICore_of_control` (OIRealization:252). On `FiniteOperationalTheory (Fin 2)`, (iv) implies the sealed core. The sealed core is defined only on the qubit (OIRealization:234), so "every qubit theory satisfying (iv)" is exact. GR:228's unqualified "every theory with full reversible control" is a minor corpus imprecision (new; low).
- `permClass_onesFixing` (PhaseSource:79), `onesFixing_not_phasesAvailable` (:52, carrier with ≥ 2 states), `substratumClass_not_onesFixing` (:196). The stated access fixes the all-ones ray, so it supplies no quarter phase; the phase is stipulated in the substratum class.
- `substratum_residual` (StructuralClosure:383). The substratum class is an architecture, context-stable, label-invariant and dagger-stable, does not drive the elementary transitions, and its generated theory on Fin 2 is not exact QM.
- `monomialSource_not_control` (SubstratumInterface:186) and `readWriteSourced_not_control` / `_not_qm` (ReadWriteControl:169 ff.). On the qubit, a theory whose conjugations are monomial or permutation has no composite unitary control and is not QM.
- `substratum_extension_quantum_iff_drives` and `substratum_plus_control_qm` (StructuralClosure:405, :414). A structurally closed extension of the substratum class is quantum exactly when it drives the elementary transitions. When it does, it generates `ExactAllFiniteEndomorphicQuantumOps` on every nonempty finite carrier. This is the same predicate as Theorem 4 (`exactAll_iff_physical_general`, GeneralCarrier:100), so "exact finite operational QM" names one object throughout.
- GR:228–:266 states all of this in prose. The census families "substratum source", "phase source" and "completion classification" are `current`; FrozenSourcing is `kernel-only`.

**The modelling premise.**
- The negative results follow almost immediately from modelling reversible interventions as bijections of configurations, which act as permutation operators (monomial ones once the phase is stipulated). A continuously tunable mixing operator is not monomial (`offDiagonal_interp_not_monomial`).
- This is an exact account of what the stated architecture lacks. It is not a physical no-go for richer substrata, and GR says so ("anything about a richer substratum ontology … not claimed", PhaseSource header).
- The identification of the Lean `substratumClass`/`permClass` with the manuscripts' stated substratum is a paper-level modelling step.

**ε-realization (Main:544–580).** All of it is proved on paper; none is kernel:
- the gluing theorem;
- the single-controlled-dynamics corollary (Main:560);
- the uniform continuum / mutual ε-density theorem (Main:576);
- the finite-test density corollary (Main:578);
- the Rounding Lemma;
- the intervention dilation (Main:460).

No `OIBridge` module formalizes the gluing. `opglue_probes.py` (at `eae01647`) computes laws exactly (Fraction, ℚ(√2)) on named qubit instances, but compares total-variation distances in floating point with tolerances 1e-15 and 1e-12 (lines 161, 176, 181, 193, 282, 308). That is numerical evidence on instances, not certification. R-07 correctly drops "exact probes".

**The §3.4 obstruction** (Main:538). The factorization half is proved on paper; the unbounded nonnegative-rank half is imported [HKLP24, Thm 4].

**Assessment of R-06.**
- **Content.** Accurate. Each clause maps to a declaration I read. The scope split (negative half on the qubit, positive half on every nonempty finite carrier) is correct. Leaving out kernel-only `frozen_sourcing_verdict` is correct under §A.35.
- **What it lacks:**
  - The modelling premise.
  - An accurate label. "(All machine-checked)" should read "machine-checked for the substratum class as formalized in [GR §3.3]".
- **Required insertion in L120**, before "The substratum as stated": "Because a bijective intervention acts on configurations as a permutation operator, …".

**Assessment of R-07.** The finding is correct (CMP-01, high): the positive realization result is missing. Owner emphasis: a positive realization theorem must appear with its domain, assumptions and strength, not as secondary to the obstruction. Measured against that, the proposed text has four problems:
- "Approximately, the converse holds" is wrong. It is not the converse of the obstruction; it is a finite-accuracy realization at a fixed instrument family.
- It omits the fixed initial state; alternative preparations enter as channels in the family.
- It omits what the realization is: one fixed bijection per instrument, with a digitized copy of the unnormalized quantum state in the hidden sector. This is a finite reversible simulation, which matters for reading it correctly.
- It omits that one autonomous dynamics for all protocols needs a program register that grows exponentially with K for arbitrary adaptive policies (Main:560).

**Required R-07 text (L130, appended after the obstruction):**
> At finite accuracy the realization direction holds. Fix a $d$-dimensional system with an initial state, a finite family of instruments with finitely many Kraus operators (preparations entering as channels), a horizon $K$ and an accuracy $\varepsilon$: one finite reversible realization, which applies one fixed bijection per instrument to a digitized copy of the unnormalized quantum state held in its hidden sector, reproduces the outcome law of every adaptive protocol over the family within $\varepsilon$ in total variation, and for instruments with at most $m$ outcomes the realized and quantum operational theories are mutually $\varepsilon$-dense at horizon $K$ (proved on paper) [Main §3.4, Theorems (finite operational realization and gluing — ε-form) and (uniform continuum realization — mutual ε-density)]. A single autonomous dynamics serving every adaptive protocol needs a program register that grows exponentially with $K$ [Main §3.4, Corollary (single controlled dynamics)]. This is density, not identity: the construction also realizes non-quantum instrument families, and no fixed finite realization reproduces the exact theory. Classical action-labelled interventions are realized exactly by one fixed realization [Main §3.4, Theorem (intervention dilation: the finite classical action-labelled comb)].

Also required:
- Use the full form (reverse OD-3's "short form if budget").
- Add an abstract clause (O-12): "Finite reversible realizations reproduce every finite quantum experiment to any stated accuracy (proved on paper); exact finite operational quantum mechanics is characterized by five completion conditions, none implied by OI alone."
- The heading change in R-07 is correct.

***

## 5. Owner priority 4: minimality (R-04)

**Re-derived by hand.** The three-hidden-state model (h = 1 flips x; h = 2, 3 swap at fixed x; h uniform) gives:
- Γ₁ = [[2/3, 1/3], [1/3, 2/3]] and Γ₂ = I;
- P(x₂=0 | x₁=1, x₀=0) = 1;
- P(x₂=0 | x₁=1) = 1/3, and a/(2−a) for P(x₀=0) = a.

So "a minimal model … with six hidden states" is false as a size claim. This is a demonstrated construction, not a lower bound. I did not establish that three is minimal for those numbers, and R-04 does not claim it.

**"The smallest realization of Theorem 3".**
- A trivial lower bound holds: two rows are needed, so |C_V| ≥ 2; with |C_H| = 1 every Γ_s is a permutation matrix, so there is no overlap.
- No corpus document states it.
- The realization is not unique.

**R-04's replacement is correct**, and so is OD-10's recommendation (no minimality claim). It names sizes and asserts no minimality.

**Where "minimal" survives:**
- Intro L185 ("minimal hidden predictive memory"): an infimum, legitimate.
- `five_way_minimality` in Appendix A: an identifier, glossed as independence.
- Main §2.4's heading "A Minimal Model" and ch01:273: corpus side, CON-24 / PR-F.
- **matrix.json rows I-123/I-124.** After the resolution, I-124's `proposed_fix` still asserts "the smallest realization … (with one hidden value every Γ_s is a permutation)", and I-123's note still reads "minimal" as "simple". MATRIX.md renders both, contradicting R-04 (RC-11).

***

## 6. Owner priority 5: proof-status labels

**Proposed texts.**
- R-03, R-08, R-13, R-20–R-27 and R-32 label correctly.
- R-01, R-02, R-06 and R-07 need the changes above.
- R-10's kinematics clause cites [GR §3.3], which does not state it until CON-15 lands (RC-7).

**Matrix labels in error:**
- **I-225:** conditional → unsupported as stated (refuted link).
- **I-223, I-286:** see §2.
- **I-291**, "(the fixed-dimension form is false)", FAITHFUL/numerical:
  - Main:594's evidence, `memory_probes.py`, searches the uniform prior only, with floating-point entropies. The claim ranges over all realizations of fixed hidden dimension.
  - B4's countercheck over arbitrary priors is a Nelder–Mead optimization.
  - The Introduction states the falsity flatly, with no label. It needs either "(false in numerical probes [Main §3.4])" or an exact certificate in Main.
  - This is a new finding (R-33, low). The count discrepancy, Main's "1 of 15" against B4's "2 of 16", remains unresolved (CON-26).
- **I-212 against I-213:** the same kind of evidence, BHa's exhaustive exact enumeration, is labelled proved-paper in one row and numerical in the other. The matrix's "numerical" class merges exhaustive exact enumeration with floating-point numerics. The layer column separates them, but the status column should too, or the README should say it does not (RC-12).
- **I-123:** verdict UNSUPPORTED but proof_status proved-paper. The resolution changed the verdict only (RC-11).

**Kernel labels.** Every Appendix A identifier is at its stated `module:line`. I checked all 28 at `eae01647`; the sources are byte-identical to `17b830bc` per the audit. The statements I read match their glosses: Equivalence, HiddenMemory, RecurrenceHorizon, TrackBQfbBridge, GeneralCarrier, PhysicalCharacterization, RootedClassificationAllTime. The census confirms:
- RecurrenceHorizon, PhysicalC4Discharge, PhysicalC4StorageReadback and RootedClassification* are `kernel-only`;
- `papers/Introduction.md` is not among the census manuscripts.

The current Introduction therefore already cites kernel-only families in Appendix A (L211–L212), independently of R-12 and R-13. OD-4 / PR-G is needed for the Introduction as it stands.

***

## 7. Re-verification of the 47 non-FAITHFUL rows and the 4 resolutions

✓ = verdict and evidence confirmed from the source. "Lit." = external literature I did not re-read; accepted on the mapper's first-hand read.

| Row | Audit verdict | My result |
|---|---|---|
| I-008 (res.) | IMPRECISE | ✓ Content is Thm 2(c), Main:582/:97. "Deterministic completion" is undefined, and L136 uses it in the Bell sense. R-24 fine. |
| I-010 | IMPRECISE | ✓ The Corollary has two unchecked ingredients (L82; Main:580). |
| I-013 (res.) | UNDERCLAIM | ✓ GR:260–266; kernel as in §4; ROADMAP:1521–1538. |
| I-015 | IMPRECISE | ✓ Main:702–704; book appendix A lists application falsifiers. |
| I-025 | IMPRECISE | ✓ The universal reading is false (constant f_x). |
| I-042 | IMPRECISE | ✓ |
| I-052 | MISCITED | ✓ GR:218 cites kernel declarations; no written proof. |
| I-054 | IMPRECISE | ✓ `c4_backflow_probes.py`:23, :52 use floats and tolerances. |
| I-071 | UNDERCLAIM | ✓ Main:498 Extension, a paragraph argument; P-G is one exact instance. Main:496's statement still says rational only (corpus tension). |
| I-078 | IMPRECISE | ✓ in structure (Main makes no coincidence claim). Lit. Bar26/Sch21. |
| I-102 | IMPRECISE | ✓ Main:492; C3Necessity:117. |
| I-103 | IMPRECISE | ✓ The bound is right; the probe is floating-point. |
| I-105, I-105.a | IMPRECISE | ✓ Positive-probability histories and time index. |
| I-113 | IMPRECISE | ✓ logically (the contraction is the "only if" half). Lit. RHP14, BD16. |
| I-114 | IMPRECISE | ✓ Main:115 is the s = 1, uniform-prior case; the general form is kernel-only. |
| I-116 | IMPRECISE | Lit. Dou26; accepted. |
| I-121 | MISCITED | ✓ PhysicalC4Discharge:27–29; StorageReadback:256. |
| I-123 (res.) | UNSUPPORTED | ✓ in substance (my 3-state recomputation). Row fields stale (RC-11). |
| I-124 (res.) | IMPRECISE | ✓ Proposed_fix stale (RC-11). |
| I-127 | OVERCLAIM | ✓ Finding correct; replacement needs the §3 assumptions (RC-2). |
| I-146, I-258, I-281 | UNDERCLAIM | ✓ (§4) |
| I-147 | IMPRECISE | ✓ Main:624. |
| I-159 | IMPRECISE | ✓ |
| I-162 | IMPRECISE | ✓ against Main:538 [55] = HKLP24. Lit. Mon08. |
| I-182 | IMPRECISE | ✓ GR:12 ladder against the gauge-axis usage. |
| I-206 | MISCITED | ✓ Pag93 is "Average entropy of a subsystem". |
| I-208, I-209 | IMPRECISE | ✓ BHa REPORT ("tested finite toy classes"). |
| I-217–I-220 | IMPRECISE | ✓ BHa P_succ formula (uniform prior); table rows 0/32; necessity diagnostics 36,416 / 14,496. |
| I-222 | IMPRECISE | ✓ verdict, but R-19's evidence is misstated: BHa's C4 proof says "This is the linear secret-sharing threshold", without a source (RC-6). |
| I-225 | IMPRECISE | ✗ Should be OVERCLAIM; status unsupported as stated (§2). |
| I-246, I-300 | IMPRECISE | ✓ L68; Main:618; GeneralCarrier:100. |
| I-265 | IMPRECISE | ✓ |
| I-277 | IMPRECISE | ✓ GR:356. |
| I-280 | IMPRECISE | ✓ §A.32 self-description. |
| I-289 | IMPRECISE | ✓ |
| I-292 | UNDERCLAIM | ✓ `finiteRootedRealizable_iff_pper` (RootedClassificationAllTime:192), kernel-only. |
| I-294 | IMPRECISE | ✓ Main:433, :447. |
| I-299 | IMPRECISE | ✓ |
| I-383 | IMPRECISE | ✓ Main:356 (PR-box), :360 (ceiling). |

**Result:** 44 confirmed and 1 changed (I-225). Two are confirmed with corrections to their row fields or evidence (I-123/I-124, I-222). Three rest on literature I did not re-read (I-078, I-113, I-116), and I confirmed their logic.

## 8. FAITHFUL sample (40 rows)

| Row | Result |
|---|---|
| I-061 | ✓ `RevReal` (Equivalence:157) has an `init` law on V × Hid, which may correlate. |
| I-068 | ✓ Equivalence:462–468, compositions. |
| I-069 | ✓ Takes only `P`; no construction hypothesis. |
| I-072 | ✓ `D_imp_Qfb`:294. |
| I-082 | ✓ Markov laws lie in S_K, hence in all three classes. |
| I-097 | ✓ HiddenMemory:83, :114, :170, :185, for a joint law. |
| I-115 | ✓ |
| I-117 | ✓ `tv_mul_le` (CausalReadback:96). |
| I-144, I-145 | ✓ `oi_alone_not_qm` (GeneralCarrier:160), qubit scope stated in the preceding sentence. |
| I-149 | ✓ Existential; "can" is read correctly. |
| I-153.b, I-334 | ✓ `rooted_eq_iff_slice_eq`.mp (TrackBQfbBridge:180). |
| I-154 | ✓ `realData_traj_stochastic` gives QfbRealizable ∧ Stochastic. |
| I-320 | ✓ |
| I-328 | ✓ RecurrenceHorizon:148 matches Theorem 3 exactly (`PDivisible` = L90's definition). |
| I-340 | ✓ Line confirmed. |
| I-344 | ✓ |
| I-028 | ✓ Main:704. |
| I-036 | ✓ Unit row sums and not stochastic ⇒ a negative entry. |
| I-081 | ✓ |
| I-126, I-355 | ✓ B.2 re-derived: Γ₁ = Γ₂ = ½J, divisor I, I(X₀; X₂ \| X₁) = 1 bit. |
| I-163 | Lit. Mon08; accepted. |
| I-175, I-184 | ✓ GR:356. |
| I-183, I-288 | ✓ GR:12; ROADMAP P2 G3 OPEN. |
| I-192 | ✓ GR:358 ("partly definitional"). |
| I-193 | ✓ GR:366. |
| I-212, I-213 | ✓ BHa table (60; 1,376). Label inconsistency noted in §6. |
| I-226, I-228 | ✓ GR:835. |
| I-237 | ✓ GR:843. |
| I-244 | ✓ |
| I-250 | ✓ Main:22, :360. |
| I-290 | ✓ Main:594. |
| I-303 | ✓ |
| I-349 | ✓ Γ₁⁻¹ = [[2, −1], [−1, 2]]. |

**Result:** 40 of 40 confirmed. No hidden overclaim, apart from the adjacent I-291 (§6), which fell outside the sample.

***

## 9. Completeness and consistency

**High and medium CMP rows.** CMP-01, -02, -03, -05, -08, -10, -17, -22 and -23 are confirmed at source; the recommendations follow. Two changes:
- **CMP-25** (BHb C2) should rise to required (§2).
- **CMP-01** should be added in full form with the abstract clause (§4).

**High and medium CON rows.** I spot-checked the sites of CON-01, -07, -09, -10, -19, -21, -25, -32, -39 and -42, and all read as recorded. For example:
- SM:14 and Juno:140 give "0.23σ", against (0.826 − 0.8165)/0.012 = 0.79σ;
- appendix-b:280 has the drafting residue "no, let me reorganize";
- GR:330: "Part I delivers QM on a finite-dimensional Hilbert space";
- appendix-c:317: "the proofs are complete";
- Methodology:235: "bijectivity follow as lemmas";
- Main:170: "Certified exactly".

The anchors and resolutions follow. The CON-01 resolution should add that A.8's *conclusion* fails for every counted configuration, not only its hypothesis.

**What the audit missed:**
- **The vacuity of A.8 as a status matter.** Found as a fact, but not carried into the matrix status or into R-01's text.
- **I-291's unlabelled numerical claim.** The fixed-dimension falsity rests on floating-point probes; Main's probe covers the uniform prior only.
- **I-040 / L26** ("results … which stop short of operational quantum mechanics"), rated FAITHFUL. Once R-06 and R-07 land, this sentence understates and should change (§12).
- **GR:228's** "every theory with full reversible control realizes the sealed core": the kernel statement and the sealed core are qubit-only (low, corpus).
- **Main:496 against :498.** The theorem statement still says "the equivalence is between rational laws and finite realizations with rational priors", while the Extension removes the restriction (low, corpus; PR-C).

***

## 10. FINDINGS.md: R-01 to R-32

| R | Finding correct? | Proposed text | Register |
|---|---|---|---|
| R-01 | Yes | **Revise** (§2). It presents a vacuous conditional as a result. | OK after revision |
| R-02 | Yes | **Revise** (§3). The positive statement is overbroad. | OK |
| R-03 | Yes | OK | OK |
| R-04 | Yes | OK | OK |
| R-05 | Yes | OK | OK |
| R-06 | Yes | OK, plus the modelling-premise clause and the "as formalized" label (§4) | OK; technical |
| R-07 | Yes | **Revise** (§4) | OK |
| R-08 | Yes | OK (paper-level Extension, one exact instance) | OK |
| R-09 | Yes | OK as an interim | OK |
| R-10 | Yes | **Mis-cites** until PR-B states the kinematics clause in GR §3.3. Land PR-B first, or drop "the complex matrix kinematics" from (5) until it does. | OK |
| R-11 | Yes | OK | OK |
| R-12 | Yes | OK, conditional on PR-G (or the interim citation) | OK |
| R-13 | Yes | OK | OK |
| R-14 | Yes | OK | OK |
| R-15 | Yes (lit.) | OK; attributes the argument, not the theorem | OK |
| R-16 | Yes (lit.) | OK | OK |
| R-17 | Yes | OK | OK |
| R-18 | Yes | OK | OK |
| R-19 | Yes, but the evidence is misstated (BHa does name the threshold, without a source) | OK ("a rank bound"; better "a rank law") | OK |
| R-20 | Yes | OK | OK |
| R-21 | Yes | OK | OK |
| R-22 | Yes | OK | OK |
| R-23 | Yes | OK | OK |
| R-24 | Yes | OK | OK |
| R-25 | Yes | OK | OK |
| R-26 | Yes | OK | OK |
| R-27 | Yes | OK | OK |
| R-28 | Yes | OK | OK |
| R-29 | Yes | OK | OK |
| R-30 | Yes | OK | OK |
| R-31 | Yes | OK (deletion) | Resolves a §A.32 hit |
| R-32 | Yes | OK | OK |

None of the texts uses §A.33 history phrases, capitals for emphasis, or assert-then-qualify, once R-01 is revised.

***

## 11. Owner decisions (FINDINGS (c))

| OD | My recommendation | Interactions |
|---|---|---|
| OD-1 Main's title | Agree: retitle in a corpus PR. Not blocking: the Introduction must cite the title as it stands. | I-145, I-252 |
| OD-2 Substratum results | Agree: full form, with my two additions (premise; "as formalized"). | OD-13, OD-15 |
| OD-3 ε-realization | **Disagree with the short-form fallback.** Use the full revised text (§4) and add the abstract clause (O-12). | OD-13 |
| OD-4 Kernel-only results | Agree: PR-G before landing. It is needed for the current Introduction too (L211–L212). Add the Introduction to the census manuscripts. | R-09, R-12, R-13, O-6 |
| OD-5 Readback declaration | Agree. | OD-15 |
| OD-6 Characterization theorem | Agree: do not name it. | — |
| OD-7 "Exact probe" | Agree: narrow the definition. | R-03, R-07, R-08 |
| OD-8 References | Agree: drop Pag93 at L156, or add Page's PRL 71, 3743 after a first-hand read. Read Sha79 or drop it. | R-14, R-19 |
| OD-9 Restating A.8 | Agree: a corpus PR. R-01 must not wait on it (§2). | R-01, PR-E |
| OD-10 Minimality | Agree: no claim. | R-04 |
| OD-11 Empirical record | Agree. | R-06 abstract wording |
| OD-12 OI⁺ and coherent completions | Agree to omit OI⁺. O-1 recommended if space allows, with its existence caveat. | OD-13 |
| OD-13 Length | Required content (R-01, R-06, R-07 in full) must not be traded for budget. Take cuts C-1 to C-8 first; build and measure. Do not defer R-10 for length; defer it only for its citation. | all |
| OD-14 ROADMAP-only items | Agree: land CON-15 (PR-B), then R-10. | R-10 |
| OD-15 Retained Lean result | Agree: regenerate in the same revision (§A.42). | R-06, R-13, O-5 |

**The eight corpus PRs.**

| PR | Needed for the Introduction's scientific accuracy? |
|---|---|
| PR-E | **Needed in part:** CON-01, A.8's restatement, makes R-01 final. CON-02 and CON-03 are independent improvements. |
| PR-A | Independent improvement. |
| PR-B | **Needed in part:** CON-15 (the kinematics clause) for R-10's citation. The rest, including CON-16 (the title), is independent. |
| PR-C | Independent. Add the Main:496/:498 tension. |
| PR-D | Independent. |
| PR-F | Independent (R-03 and R-04 are self-contained). Recommended so that the source the Introduction cites stops calling its model "minimal". |
| PR-G | **Needed.** A precondition for R-09, R-12 and R-13, and for census coverage of the existing Appendix A. |
| PR-H | Independent. |

***

## 12. The central narrative

**What the whole framework establishes:**
1. **Kernel.**
   - S_K = D_K = Q_K, universal, so representability does not discriminate.
   - Theorem 2 for a joint law; the capacity bound.
   - Theorem 3, and readback ⇒ indivisibility somewhere in the cycle (routed form).
   - Theorem 4, both directions.
   - Independence on the qubit; OI ⇏ QM.
   - (iv) ⇒ OI core on the qubit.
   - The stated substratum class supplies no phase from its access and no continuous mixing.
   - Substratum + driven transitions ⇒ exact finite QM on every finite carrier.
   - Non-selection of the relating evolution.
2. **Paper.**
   - The time-t identification; the Corollary.
   - The ε-realization and mutual ε-density at fixed (d, m, K); the classical comb.
   - The factorization half of the obstruction.
   - (C2) necessity under the mixing hypothesis.
3. **Open.**
   - Whether a physical substratum supplies the phases and continuous control.
   - The complex matrix kinematics (K) and H-∞.
   - Selection of the relating evolution; the Born exponent; H-Bell; (C4) at physical cuts.
   - Any discriminating experiment.
   - G3 (and with it the cosmological-constant proposal).
   - A Page curve. GR's A.8–A.9 have no instance as stated.

**Where the current narrative is out of step:**
- **"Which of (iii)–(v) a physical substratum supplies is open"** (abstract, §3.2, §6.2, §6.3). The corpus has narrowed this to one named missing resource, continuous state-mixing control, given the stipulated phase. The open question is whether a physical substratum supplies it.
- **"Stop short of operational quantum mechanics"** (L26) and the §3.4 obstruction-only framing. The corpus proves an ε-realization of every finite quantum experiment, density not identity, alongside the exact-theory obstruction. The narrative should read: exact at the fixed-basis level; ε-exact for every finite operational experiment; exact operational QM exactly when one control resource is added, which OI does not supply. Each claim with its proof strength.
- **§5.** The established content is BHa's conservation/recovery separation (proved and exhaustive, in toy models) and BHb's entanglement budget. The Page-curve calculation should appear as a theorem with no instance in its stated setting, not as a conditional result.

**Recommended scope of revision:**
- Apply R-06, R-07 and R-01 as revised.
- Rewrite L26's clause, for example: "…its foundation and quantum-emergence results, which reach the fixed-basis statistics exactly and every finite quantum experiment to any stated accuracy, while exact operational quantum mechanics needs completion conditions OI does not imply."
- Align §6.4's second sentence and the abstract with that wording.

No other change to the central narrative is warranted. The memory-centred thesis, the representation-not-derivation stance, and the cosmological-constant conditionality are all faithful.

***

## 13. Method

- **Layers kept distinct.** Yes, in the layer column. The status column conflates exhaustive-exact with numerical (RC-12).
- **"Proof missing" against "proof outside Main".** Kept apart. Examples: I-052 and R-11 (the proof is in Lean), I-124 ("proved nowhere"), I-071 (Main's Extension rather than its theorem).
- **"Rigor, not detail".** Applied: OD-6, the kernel over GR prose in R-06, the anchor choices in CON rows.
- **Status of every dependency.** The dependency blocks do report each link, including the refuted A.8 link. Row I-225 does not apply the weakest-link rule (RC-1).
- **Honesty of stated limits.** Mostly honest. Two exceptions:
  - FINDINGS' header says the two internal defects were corrected, while (f) still lists them as "not corrected here".
  - The Summary and (e) give "364 of 409 FAITHFUL / 45 others", but the committed `matrix.json` has 362 and 47 after the resolutions (RC-9).
- **PLAN.md's "Objects"** still names `b64919cd` as the corpus. The matrix header explains why `eae01647` was used; `main` (`02e73e56`) differs only in AGENTS.md.
- **Hygiene.** An untracked `matrix/scripts/b4probe/__pycache__/gen_b4.cpython-313.pyc` sits in the worktree. It must not be committed.

***

## 14. Required changes (exact list)

**Scientific, in FINDINGS.md and matrix.json:**
- **RC-1.** Replace R-01's proposed text with the §2 text. Fold CMP-25 into R-01. Add I-223 and I-286 to R-01 with the §2 edits. Re-rate I-225 as OVERCLAIM with status "unsupported as stated (vacuous conditional)", and I-223 and I-286 as IMPRECISE (via `resolutions.json`).
- **RC-2.** Replace R-02's proposed text with the §3 text. State the assumptions (positive-probability roots; a family that comes from a multi-time law; 0 < t < n) and the equivalence of "M_t > 0 at some t" with Main's non-Markovianity.
- **RC-3.** Replace R-07's proposed text with the §4 text. Change OD-3 to the full form plus the abstract clause O-12.
- **RC-4.** Amend R-06's L120 text: add the permutation-operator premise, and change "(all machine-checked)" to "machine-checked for the substratum class as formalized in [GR §3.3]".
- **RC-5.** Add R-33 for I-291, with its label (or an exact certificate in Main).
- **RC-6.** Correct R-19's evidence: BHa's C4 proof names the linear secret-sharing threshold without a source.
- **RC-7.** Make R-10 explicitly two-stage. Do not cite [GR §3.3] for the kinematics clause until PR-B lands.
- **RC-8.** Add a narrative finding for I-040 (L26) and the abstract and §6.4 alignment (§12).

**Audit-internal:**
- **RC-9.** Make FINDINGS' counts agree with `matrix.json` (362 / 47 after resolutions). Remove the stale "not corrected here" items from (f).
- **RC-10.** Fix `scripts/C-completeness-data.py` (CMP-10: CON-17–19) so that regenerating reproduces the committed `completeness.json` and COMPLETENESS.md.
- **RC-11.** Extend `resolutions.json` and `merge_matrix.py` so that a resolution also overrides `proof_status` and `proposed_fix` (or marks them superseded). Fix I-123 and I-124: no minimality claim survives in the matrix.
- **RC-12.** Distinguish exhaustive exact enumeration from floating-point numerics in the status column, or document the merge. Make I-212 and I-213 consistent.

**Record in OD-4 and the PR plan:**
- PR-G is a precondition for the Introduction as it stands.
- PR-E's CON-01 and PR-B's CON-15 are the only other corpus changes the Introduction's accuracy depends on.

## 15. Limits of this review

- **Literature not re-read:** RHP14, BD16, Dou26, Bar26, Sch21, Mon08, HKLP24, Pag93, Sha79, CT06. Rows resting on them (I-078, I-113, I-116, I-162, I-163) are judged on internal logic and on the mappers' first-hand reads.
- **No Lean build.** Kernel statements were read from source at `eae01647`. Axiom reports were taken from the audit's account of the retained record, which exists only on #918's branch.
- **Main's Rounding Lemma** (the finite-b half of the ε-theorem) was not re-proved. R-07 does not rely on it; the exact-arithmetic regime it does rely on I checked in outline.
- **CON rows** were spot-checked at their sites, not every row re-derived. Low-severity CON rows and low-priority CMP rows were not reviewed.
- **CON-26's count** was not reproduced.
