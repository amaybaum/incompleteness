# Auditor A2: scientific audit of papers/Introduction.md L1–L189 (abstract, §1, §2.1–§2.6)

**Target:** `draft/oi-introductory-paper-20261025` at `60c976fec83677ee4bb6496bf48b03f2bc76823a`.
**Corpus read at:** the same head, including Main, GR, book ch01/ch03, the Lean `OIBridge` sources (byte-identical at `17b830bc`) and `papers/introduction_repro`.
**Open source-correction heads:** SC-29 `823d6a80`, SC-28 `7a4e4a8d`, SC-17 `e316cf92`, SC-22 `621fbf2c`, SC-31 `4fdcf52a`, SC-33 `387dcfb9`, SC-32 `4f7ca2d1`.
**Audit branch:** `16fc745d` (FINDINGS.md, CORRECTIONS-LEDGER.md, proofs/README.md).
**Mode:** read-only. Nothing was committed, pushed or commented, and the worktree was removed.

## Verdict: ACCEPT WITH CHANGES

It is not mergeable until B1–B9 are applied. Each blocking item is a local text fix. The exceptions are B8, which needs added text in §3.2/§3.4 (other slices), and B9, which needs the census step that the owner's disposition OD-4 places before landing.

## Blocking findings

**B1. Evidence class of "exact probes" (audit R-03, S9-D1; owner disposition OD-7 not applied).** Lines L41, L75, L120.
- **Current text:**
  - L41: "an "exact probe" is an exhaustive computation in exact rational arithmetic at small size"
  - L75: "(proved on paper, with exact probes)"
  - L120: "by Pinsker's inequality (proved on paper, with exact probes)"
- **Source:**
  - `papers/oi_lattice_code/foundations/c4_backflow_probes.py` lines 17–24 and 52 (the Pinsker probe) builds `Fraction` laws, but it accumulates the conditional mutual information as `float(p)*log2(float(…))` and asserts with `abs(I-1.0)<1e-12`. That is floating-point evidence on three hand-picked families.
  - `process_dilation_probes.py` and `review4_probes.py` P-G are exact `Fraction` checks on named instances, not exhaustive over a class.
  - Main.md:170 says "Certified exactly" for the floating-point probe. This is a corpus error with no PR yet (the SC-5 residue).
- **What is wrong:** no cited probe is exhaustive, and the Pinsker probe is not exact. The Code Review Rules forbid presenting floating-point evidence as exact certification.
- **Proposed replacement:**
  - L41: "an "exact probe" is a computation in exact rational arithmetic on stated small instances".
  - L120: "by Pinsker's inequality (proved on paper) [Main §2.3, Lemma (accessible conditional memory from readback); CT06]".
  - L75 is then true as written.
- **Corpus side (outside slice):** Main.md:170 "Certified exactly" should become a numerical statement.

**B2. The Corollary drops the common-endpoint hypothesis (audit R-36, S9-A4).** Line L116.
- **Current text:** "…every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards."
- **Source:** Main.md:99 (§1.5): "a pair of such posteriors with different pushforwards", where "such" means positive-probability histories ending at the same $x_t$.
- **What is wrong:** read literally, the converse is false. For the Markov law $X_{t+1}=X_t$, posteriors of histories ending at 0 and at 1 have pushforwards $\delta_0\neq\delta_1$, yet $M_t=0$. Positive probability is supplied by the definition of $\mu_\omega$ at L99, but the common endpoint is not.
- **Proposed replacement:** "…that is, a pair of posteriors of histories ending at the same $x_t$ with different pushforwards."

**B3. The Bell sentence for the card game is unrestricted (audit R-32; inconsistent with Main §3.3 and with SC-33's corrected ceilings).** Line L188.
- **Current text:** "no card arrangement violates a Bell inequality [Book §1.11; Main §3.3]."
- **Source:**
  - Main.md:356: with globally coupled setting-dependent hidden dynamics, the reversible response-table construction "also realizes PR-box behavior".
  - Main.md:362–375: the Bell-local conclusion needs (i) determinism, (ii) own-region interventions, (iii) local ±1 readouts outside the cone, (iv) a setting-independent ensemble, and a ±1 outcome in every run.
  - The SC-33 branch makes every compressed ceiling carry these qualifiers.
- **What is wrong:** a deck can encode any finite reversible dynamics, so the unqualified claim contradicts the section it cites.
- **Proposed replacement:** "On card inputs the game is a classical stochastic process; a card arrangement whose moves and setting choices act only on each player's own cards, with each outcome read from that player's cards, a ±1 outcome in every run and settings chosen independently of the deal, violates no Bell inequality [Main §3.3, Theorem (Bell ceiling for a screened local completion); Book §1.11]."
- **Corpus side (outside slice):** book ch01:286 ("no arrangement of cards on a table violates a Bell inequality") is not touched by SC-33 and should be scoped the same way. ch03:188 already supplies locality inline.

**B4. $\Gamma_1$ is used outside its own definition (internal inconsistency with §2.5).** Line L186.
- **Current text:** "With anticorrelated cards ($b=1-x$), $\Gamma_1$ is a permutation and the game is divisible."
- **Source:** Introduction L136 and Main.md:137 define $\Gamma_t$ only for one hidden prior shared by every root and drawn independently of it. L130 says that if the dealer puts the opposite colour face down, the forecasts "would describe two different deals, not one rule started in two ways".
- **What is wrong:** with $b=1-x$ the hidden card depends on the root, so the rooted family is undefined. The permutation matrix here is the matrix of root-conditioned forecasts, which §2.5 says is not a property of one rule.
- **Proposed replacement:** "With anticorrelated cards ($b=1-x$) the face-down card is not dealt independently of the visible one, so the rooted family of §2.5 is not defined; the forecasts conditioned on the visible start then form a permutation at step 1 and chain step by step." Deleting the sentence is the alternative.

**B5. §2.5 is presented as discriminating content (audit S9-I1/R-37; contradicts L158).** Line L37.
- **Current text:** "the discriminating content lies in where the memory of a pattern must be kept (§2.4) and in what the world's eventual return to its starting configuration does with it (§2.5)."
- **Source:**
  - Main.md:141 (Scope): the cycle indivisibility holds "for every representative with such a step, laws that are Markov on every accessible window included".
  - Introduction L158 says it "does not separate them from memory-bearing laws at accessible orders".
  - proofs/README S9-I1 says the memory-discriminating framing of the recurrence result is not supported.
- **Proposed replacement:** "…the discriminating content lies in where the memory of a pattern must be kept (§2.4); the world's eventual return to its starting configuration makes the forecasts fail to chain somewhere in its cycle for memoryless and memory-bearing patterns alike (§2.5)."

**B6. The routed-readback machine-check claim is glossed with a predicate it does not check (audit R-13, OD-5).** Line L162, with Appendix A L340.
- **Current text:** "Indivisibility at some return horizon is also machine-checked from the *routed* form of (C4), the realization clause in which a record of the visible history written into the hidden state is routed back into later visible conditionals within the window [Main §1.3]."
- **Source:** the cited `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) uses the frozen "seed-posterior" spelling. The module's own header (PhysicalC4Discharge.lean:27–35) records that this "is not the same predicate" as the storage-time clause the gloss describes. The storage-time reading is `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256, present at `17b830bc`). It is not in the retained `introduction_repro` result.
- **What is wrong:** the verification claim is attached to a statement stronger than the one checked.
- **Proposed fix:** either cite the storage-time declaration and regenerate the retained axiom report (OD-15), or narrow the gloss to "…routed form of (C4), in its reading conditioned on the initial hidden state".

**B7. The abstract omits the strongest proved operational-realization result (audit R-07/R-40/R-34; owner OD-3 not applied).** Line L17.
- **Current text:** the abstract goes from Theorem 4 straight to applications and has no ε-realization clause. The body has no ε-realization text either (CHANGES-r16, I-12).
- **Source:** Main.md:596, Summary (4): "Every $d$-dimensional quantum experiment of horizon $K$ has a finite reversible deterministic ε-realization — proved in exact arithmetic … at finite $b$ … the bound on the realized law is open."
- **Proposed replacement (abstract, after the Theorem 4 sentence):** "Every quantum experiment of finite dimension, with finitely many outcomes and a finite horizon, has a finite reversible realization reproducing it to any stated accuracy (proved on paper, in exact arithmetic), while no fixed finite realization reproduces a qubit exactly."
- **Dependency:** the matching §3.4 text is in another auditor's slice.

**B8. The abstract understates what is known about substratum sourcing (audit R-06; owner OD-2 not applied).** Line L17.
- **Current text:** "Open are the completion conditions a physical substratum supplies, the Born exponent and the gravitational field equations."
- **Source:**
  - GR.md:260–262, the substratum-source form: the phase intervention "enters as an assumption", and the concrete substratum "supplies every structural requirement … but not continuous state-mixing controllability".
  - The supporting declarations are present: `permClass_onesFixing`, `onesFixing_not_phasesAvailable` (PhaseSource:79, :52), `monomialSource_not_control` (SubstratumInterface:186), `substratum_residual`, `substratum_plus_control_qm` (StructuralClosure:383, :414) and `realizesSealedOICore_of_control` (OIRealization:252).
- **Proposed replacement:** "The finite bijective substratum with the observer's stated access supplies no quarter phase and, with a phase intervention assumed, no continuously tunable state mixing; adding that control yields exact finite operational quantum mechanics (machine-checked for the substratum class as formalized [GR §3.3]). Open are whether a physical substratum supplies it, the Born exponent and the gravitational field equations."
- **Dependency:** the same understatement appears at L228 and L312 (other slices).

**B9. Census coverage of the cited kernel results (owner disposition OD-4/OD-15; AGENTS.md §A.35).** Lines L142, L160–L162.
- **Current state:** Theorem 3 (`RecurrenceHorizon`) and the routed result (`PhysicalC4Discharge`, and `PhysicalC4StorageReadback` if adopted) belong to census families marked `kernel-only`, with no manuscript anchor. `verification/lean-manuscript-census.json` does not list `papers/Introduction.md`.
- **What is wrong:** the Introduction would be the only publication-facing site for these results, outside the census contract. The retained `introduction_repro` result does cover every declaration Appendix A cites, and the mathematics is correct.
- **Fix:** before landing, a corpus step anchors these families (PR-G) and adds the Introduction to the census manuscripts.

## Optional findings

- **O1. L81, attribution (R-18).** Current: "is that of [Bar26, Thm 3.3; Sch21, Thm 2]". Main makes no such identification, and the audit reports that Bar26 fn. 1 notes an apparent error in Schmidt's construction. Suggested: "has the form of the dilations of [Bar26, Thm 3.3; Sch21, Thm 2], for a stochastic matrix on $|\mathcal C_V|$ states".
- **O2. L136, attribution (R-16).** Current: "This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1]." The criterion is an equivalence and only its necessary half is used, as L160 itself says. Suggested: "the 'only if' half of the divisibility criterion of [RHP14, Thm 2.4] … [BD16, Prop. 1 and Cor. 1]".
- **O3. L160, attribution (R-15).** Current: "Doukas states the same argument concurrently [Dou26, Prop. 1]". Per the audit's first-hand reading, Prop. 1 is a no-revival (contraction) obstruction without overlap or return. Suggested: "Doukas states the contraction argument concurrently, as a no-revival obstruction [Dou26, Prop. 1]".
- **O4. L37, where the proofs are (R-11).** Current: "Proofs, the status ledger and the probe code are in [Main]". L39 places the proofs of §§3.2–3.5 in [GR] and the §5 results in [BHa; BHb]. Suggested: "The status ledger and the probe code are in [Main], which this paper introduces; written proofs are in [Main], [GR] and [BHa; BHb], and the machine-checked declarations are listed in Appendix A".
- **O5. L120, joint-law qualifier (SC-29).** Current: "the lower bound is machine-checked for bijective realizations". Corrected Main:610 on the SC-29 branch says "in joint-law form", and Appendix A L338 already says so. Suggested: "machine-checked for bijective realizations in the joint-law form of Theorem 2". SC-29 also lists reading $\max_t$ as one finite family over a single history type as a step not formalized; an optional clause could name it.
- **O6. L166, "A minimal model" (R-04, CON-24).** I checked exactly that a model with 2 hidden states (h=1 flips, h=2 fixes) already gives $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$, and a 3-hidden-state model reproduces every number of this example. "Minimal" is therefore false as a size claim; it follows Main §2.4's heading, which carries the same issue. Suggested: "A six-hidden-state model."
- **O7. L29, universal reading (R-30).** Current: "so the visible sector evolves stochastically". Suggested: "so the visible sector can evolve stochastically".
- **O8. L101–L110, time range.** Theorem 2 does not state $1\le t\le K-1$ (Main.md:598); stating it is optional.

## Claims checked and found correct

**Abstract**
- The OI hypothesis is correctly stated.
- Theorem 1 is correctly described as machine-checked, and the attribution to Egri et al. and Barandes is in place.
- The memory sentence is Theorem 2(c).
- The recurrence sentence holds with rows for every root, the shared independent prior, the non-permutation trigger, and the "not predictable from the current observation" trigger (if every $\Gamma_t$ is a permutation then $X_{t+1}$ is a function of $X_t$). The full-support equivalence holds.
- Theorem 4's "if and only if" has separate kernel witnesses for each direction (Appendix A), so §A.34 is met.

**§1**
- The triple $(S,\varphi,V)$ (Main §1.2).
- The bijection as representative and finiteness as a posit (Main:62).
- The prior as a realization datum (Main:60).
- No uncertainty relation constrains fixed-readout visible laws (Main:588).
- The card description in §1.1 agrees with the exact table.
- The Conventions' commit `17b830bc`: OIBridge sources are identical to the head, and all 15 checked module:line citations resolve.

**§2.1**
- The definitions of $\mathsf S_K$, $\mathsf D_K$ (correlated initial law) and $\mathsf Q_K$ (diagonal initial state, every-step projective readout, fixed record function) match the Lean `Stochastic`, `RevReal` and `QfbReal`.
- Total variation is defined as $\tfrac12\|\cdot\|_1$ (resolves R-38).

**§2.2**
- Theorem 1 matches `finite_horizon_equivalence`, which takes no construction as a hypothesis.
- The clock-and-trajectory carrier matches the `S_imp_D` construction.
- The independent-prior realization agrees with post-SC-2 Main.md:512–514: rational conditional kernels at positive-probability histories, an arbitrary visible initial law, and the response-table Extension for arbitrary kernels.
- The permutation-unitary representation of $\mathsf D_K\subseteq\mathsf Q_K$ is correct.

**§2.3**
- Markov laws lie in all three classes (Main:550).
- $p=|U|^2$ is definitional, and the exponent is not selected because the unitaries are permutations (Main:550).
- The $L$-periodic law and the absence of an exact all-time realization of a nonperiodic law (Main:634).

**§2.4**
- Theorem 2(a)–(c) match `HiddenMemory` and Main:598–604. The joint-law form and the time-$t$ identification on paper agree with the SC-29 branch.
- The memory-witness definition is correct, as is the Corollary's evidence split apart from B2.
- $|\mathcal C_H|\ge2^{I^*}$ (`card_hidden_ge_two_pow_Istar`).
- The variational facts are correct: $\inf=I(X_{<t};X_{>t}\mid X_t)$, equality with $M_t$ by the chain rule, and $H(X_{<t}\mid X_t)$ for bijective realizations (Main:610).
- I re-derived the Pinsker floor $p_0\delta^2/\ln2$ with total variation as $\tfrac12\|\cdot\|_1$.
- (C1)–(C4): (C1) follows from (C4); (C3) holds unconditionally; the two forms of (C2) match Main:76; the coupling-step contrapositive uses $M_k$, which is correct (Main:465).
- The fair-coin separation (Main:172).

**§2.5**
- The P-divisibility definition matches Lean `PDivisible`.
- Theorem 3 matches `pIndivisible_of_rooted_identity_return_of_overlap` exactly.
- "Two rows share a positive column iff not a permutation" was re-proved.
- The stochastic-inverse lemma route matches Main:133–139.
- The Corollary's supply clause, the full-support equivalence and both converse steps match Main:139–141.
- "Monotone distance is necessary, not sufficient" (Main:117).
- "Accessible windows are by definition short compared with $L$" (Main:532).
- The different-deck example: I constructed an exact instance with order 3, $\Gamma_1=\begin{pmatrix}1&0\\\tfrac12&\tfrac12\end{pmatrix}$ and $\Gamma_2=\Gamma_3=I$, whose overlap comes only through the never-dealt root.

**§2.6, recomputed exactly in rational arithmetic**
- Six-state model:
  - $\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}$, $\Gamma_2=I$.
  - $\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$.
  - $\Gamma_1^2$ has diagonal 5/9 and off-diagonal 4/9.
  - $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$, $P(x_2{=}0\mid x_1{=}1)=1/3$, and $a/(2-a)$ in general.
- XOR example: every two-time matrix is $\tfrac12J$, and $I(X_0;X_2\mid X_1)=1$.
- Four-bit example: $M_1=0$, $M_2=1$, and $I(X_{<2};X_{>2}\mid X_2)=1$.
- Card table: 1/2, 1, 1/2, 1/2, with the reveal-only and replace-hole variants both equal to 1.

**Open PRs and register**
- **SC-28 / SC-31 / SC-22 / SC-32:** the slice relies on no text they remove or weaken. It makes no Poincaré, type II, period-growth, 𝒩 or SM Theorem 3 claim.
- **SC-17 / SC-33:** they touch only L188 (B3).
- **Register (§A.32/§A.33):** no caps emphasis, reader instructions or revision-history phrases in L1–L189.

## Outside the slice (labelled)

- **Main §1.3 (L72, L78), corpus error SC-19, no PR:** Main says "(C1) and (C3) follow from (C4)", with the reason "the observed conditional information must pass through the hidden sector". The audit shows (C3) holds unconditionally by the whole-future bound (S9-A5). The Introduction is correct here, so under the owner's policy Main needs the matching correction.
- **Main §1.3 (L76) and §3.4 (L465, L470), notation error:** the C2 contrapositive is written "$I^*>0$ … $\varepsilon_{\min}(I^*,n_V)$", while Main defines $I^*=\sup_t I(X_{<t};X_{>t}\mid X_t)$. The theorem bounds only $M_k$. Since $I(X_{<k};X_{>k}\mid X_k)\le\sum_j M_j$, the stated form with $I^*$ does not follow. The Introduction's $M_k$ form (L122) is correct; Main should be corrected to match.
- **Main.md:170:** "Certified exactly" for a floating-point probe (see B1).
- **Book ch01:286:** the unrestricted card Bell sentence (see B3).
- **Main §2.4 heading and ch01:273:** "minimal" (see O6).
- **Introduction L201 (§3.1, R-02):** the proved direction, that with every root of positive probability P-indivisibility implies $M_t>0$ for some $t$, is omitted. The current wording ("no unconditional implication … is asserted") is not false.
- **Introduction L228 and L312:** carry the same substratum-sourcing understatement as B8. The §3.4 body needs the ε-realization text that B7 depends on.