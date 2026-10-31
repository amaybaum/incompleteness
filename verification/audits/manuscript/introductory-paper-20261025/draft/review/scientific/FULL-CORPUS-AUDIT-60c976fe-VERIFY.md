## Independent verification of the full-corpus audit of PR #918 (Introduction at 60c976fe)

I worked read-only. I made no push, commit, comment or edit. I used a detached worktree at fc6ebc70, where the Introduction is byte-identical to 60c976fe, and removed it afterwards with `git worktree remove`, without gc or prune. All scripts ran as copies under `python3 -I`.

At this head, Main, GR, the book, `verification/lean-mathlib`, the census registry and the census tool are identical to main 0d917665. The newest SC-32 head is 6d32ce51, which is newer than 2bd0bc0f.

Line numbers below are the Introduction at 60c976fe unless a file is named.

**Sources read first-hand for this check:**
- Mon08: the arXiv v2 full text.
- Pag93: the arXiv v2 full text.
- Page, "Information in black hole radiation" (hep-th/9306083): the abstract only.

### Task 1: mapping table

Status codes: **A** = APPLIED, **PA** = PARTLY APPLIED, **NA** = NOT APPLIED, **SUP** = SUPERSEDED, **OBS** = OBSOLETE.

| Item | What it requires of the Introduction now | Status at 60c976fe | Corpus change / PR |
|---|---|---|---|
| R-01 (+O-7) | L298, L300, L308. State three things: Theorem A.8 counts configuration initial states with the bipartition aligned to them, so it has no instance; the Page value enters only through H-scramble; and BHb C2's bound. | **PA.** L298 has "fails for every bijection acting on a definite configuration with the bipartition aligned to the configuration coordinates [BHb]". L300 has "H-scramble requires an initial superposition of configurations or a split not aligned with them". L298 still leads with "Under them, for all but an exponentially small fraction of initial conditions … equals the Page value". The no-instance statement, C2 and "enters only through" are all absent. | GR App. A.8 plus mirrors (PR-E, CON-01/OD-9). **No PR.** |
| R-02 | L200: remove the false "holds", and state the proved direction (positive-probability roots: P-indivisible ⇒ M_t>0). | **PA.** Now reads "no unconditional implication among them is asserted". The proved direction is not given at L200; L148 gives only the full-support case with n=L. | CON-42, Main:334 against :606 (PR-C). No PR. Not a precondition. |
| R-03 | L41: narrow the definition. L120: drop "with exact probes". L75 is then true. | **NA.** | Main:170 "Certified exactly" (PR-F, CON-25). **No PR.** |
| R-04 | L166: drop the size claim. | **PA.** "smallest realization" is gone. The label "**A minimal model.**" remains. | Main:178 heading and ch01:273 (PR-F, CON-24). No PR. |
| R-05 | L308: "at every finite horizon". The old L189 half asks for "finite" operational QM. | **PA.** The finite half is SUP, by L304's "on a nonempty finite system … finite Kraus instruments". L308 still says "are the visible laws of an embedded observer". | — |
| R-06 (OD-2) | Abstract L17 (last sentence), L226 (last sentence), L304, L312 item 1, and Appendix A plus axiom reports. | **NA.** L226: "Which of (iii)–(v) a physical substratum supplies is the open step toward full operational equivalence." | None: GR:260–262 states it, and the families are `current`. The paper side needs the OD-15 regeneration. |
| R-07 + R-40 + O-12 (OD-3) | §3.4 heading (L240); ε-realization paragraph after L244; abstract clause. | **NA.** The r16 record, item I-12, says "No change". | Done in the corpus: SC-1, #947, merged (Main:560–596). |
| R-08 | L75. | **A** (SC-2 form): "Every law also has a realization whose hidden prior is independent of $x_0$, by the finite-horizon process dilation for rational conditional kernels at positive-probability histories, … and by its response-table extension for arbitrary kernels". | SC-2, #948, merged. |
| R-09 | L315. | **NA.** Still "exact gluing of per-horizon realizations for recurrent target families". | Interim text needs no corpus change. The full form needs PR-G (rooted classification into Main:618). No PR. |
| R-10 | Open-problem list, L312–316. Stage 1: the infinite-dimensional extension. | **NA.** | Stage 2 needs PR-B, CON-15. No PR. |
| R-11 | L37, L39. | **NA.** L39 now reads "The results of §§3.2–3.5 are proved in [GR] and [Main]". This is broader than before: §3.2–3.3 are proved in Lean, and §3.4's unboundedness is imported. | — |
| R-12 | L142. | **A:** "with one hidden prior shared by every root and drawn independently of it". Main:137, as corrected by SC-3, supports the statement on paper. | The "machine-checked" claim needs the PR-G anchor. No PR. |
| R-13 (OD-5) | Appendix A L340: cite `routedAtStorage_forces_indivisible_somewhere`. | **NA.** | PR-G census families and OD-15. No PR. |
| R-14 | L288: [Pag93]. | **NA.** | — |
| R-15 | L160: Doukas. | **PA.** "overlap-and-return" was dropped, but "Doukas states the same argument concurrently [Dou26, Prop. 1]" still attributes the overlap-plus-return argument. | — |
| R-16 | L136: RHP14 only-if half; BD16 Cor. 1. | **NA.** | — |
| R-17 | L244: Montina. | **NA.** | — |
| R-18 | L81. | **PA.** $n$ is now $|\mathcal C_V|$, but "is that of [Bar26, Thm 3.3; Sch21, Thm 2]" remains. | — |
| R-19 | L292: Sha79. | **SUP.** r17 E2 changed it to "as in perfect secret sharing, of which Shamir's threshold scheme is the standard example [Sha79]", and auditor C records a first-hand read of Sha79 (the OD-8 read option). | — |
| R-20 | L290–292: BHa prior, population. | **A/SUP** (r16 toy-model definition). L290: "A message $m$, drawn uniformly … every other register is uniformly random and independent of $m$, or blank". L292: "with a two-bit message occupying both registers and one register read". | — |
| R-21 | L39, L288–292. | **PA.** "exact or exhaustive checks" and "the layout is that of the Page-curve setup … at small size" are present. "Arbitrary bijections in place of the substratum dynamics" is not stated. | — |
| R-22 | L120. | **A** in substance: "With $I^*=\max_t I(X_{<t};X_{>t}\mid X_t)$, a realization of the law needs $|\mathcal C_H|\ge2^{I^*}$". The Corollary locator is not attached. | SC-29, #961, open (joint-law scoping in Main). |
| R-23 | L114, L122. | **A**, through the memory-witness definition: "a pair of positive-probability histories ending at the same $x_t$". | — |
| R-24 | L17. | **A:** "every faithful realization carries the law's conditional memory in its hidden state". | — |
| R-25 | Abstract parenthetical. | **OBS** (removed in r16, D1). | — |
| R-26 | L315. | **A:** "the hidden-sector mixing hypothesis … under which observed conditional memory gives a lower bound on the hidden sector's coarse-grained mixing time". | SC-20, #953, merged. |
| R-27 | L316. | **NA.** Still "machine checks of the steps of §§2.2–2.5 proved on paper". It omits §3's paper-only results. | — |
| R-28 | L230 heading. | **NA.** | — |
| R-29 | L282, L308. | **A/SUP** (r16 §4 restructure): "which [GR] calls the G3 coupling theorem". | — |
| R-30 | L29. | **PA.** "can send it to different futures, so the visible sector evolves stochastically". | Main:105 (PR-H). No PR. |
| R-31 | — | **A** (deleted in r16). | — |
| R-32 | L188. | **NA.** | ch01:286 and FULL:630. #968 does not touch them. **No PR, and not in the PR-A…G plan.** |
| R-33 | — | **OBS.** r16 (M2) deleted the open item; L120 states the proved condition. | CON-26 (PR-F). Not a dependency. |
| R-34 | Narrative. | The phrase is **OBS**. Its substance, the ε-reach, is **NA** and rides on R-07. | — |
| R-35 | L290–292. | **A.** L290: "One map is applied at every step … keeps every read". L292 gives the counts with their layout. | — |
| R-36 | L116, L122. | **PA.** The (C3) part is applied at L122: "(C3) holds by the capacity bound". The abstract count is OBS. L116 lacks the common endpoint (see A-B2). | Main:72/78 and GR:52, "(C3) follows from (C4)" (SC-19). No PR. Low priority. |
| R-37 | L17, L136–160. | **A.** L148 and L158: "does not separate them from memory-bearing laws at accessible orders". A conflict remains at L37 (see A-B5). | SC-3 (#949, #951), merged. |
| R-38 | L47, L120. | **A:** "$\|\mu-\nu\|_{\mathrm{TV}}=\tfrac12\sum_k|\mu_k-\nu_k|$". The stated ≥ needs no positivity qualifier. | — |
| R-39 | L252–256. | **A** (r16, D6). Residues: B-B4 and B-B5. | SC-4, #950, merged. SC-33, #968, is open for Main's compressed summaries. |
| R-40 | With R-07. | **NA.** | SC-1, merged. |
| O-7 / O-12 | Inside R-01 / R-07. | **NA.** | — |
| OD-1 | Cite Main's title as it stands. | **A** (L353). | Retitle (PR-B, CON-16). No PR. Not blocking. |
| OD-2 / OD-3 | = R-06 / R-07 (full forms). | **NA.** | As above. |
| OD-4 | PR-G before landing; add the Introduction to the census. | **NA.** | **No PR.** |
| OD-5 | Cite the storage-time declaration as primary. | **NA.** | — |
| OD-6 | Do not name the Characterization theorem. | **A** (not named). | — |
| OD-7 | = R-03. | **NA.** | PR-F. No PR. |
| OD-8 | Pag93; Sha79; CT06/Har04. | **PA.** Sha79 is satisfied by auditor C's first-hand read. Pag93 is not applied. CT06 is still unread. Mon08 does report Hardy's result (I read this first-hand, p. 2: "He proved that the number of ontic states can not be finite"). | — |
| OD-9 | GR A.8 in PR-E; R-01 must not wait for it. | **NA**, both. | **No PR.** |
| OD-10 | No minimality claim. | **PA** (the L166 label remains). | — |
| OD-11 | State that no established discriminating experiment exists. | **PA.** L314 lists "an experiment or memory-witness test distinguishing OI from standard quantum theory" as open, and L71 says "it does not show that nature is such a world". The abstract's open list omits it. | — |
| OD-12 | Omit OI⁺; O-1 optional. | **A.** | — |
| OD-13 | Do not trade required content for length. | **NA** in effect: the content it protects (R-01, R-06, R-07) is absent. | — |
| OD-14 | PR-B (CON-15), then R-10. | **NA.** | No PR. |
| OD-15 | Regenerate `introduction_repro` with the new declarations. | **NA.** The JSON carries `routed_forces_*` only; it has no `routedAtStorage_*` and no R-06 declarations. | — |

### Task 2: blocker verdicts

- **A-B1: CONFIRMED.**
  - `c4_backflow_probes.py` builds `Fraction` laws, but `I_cond` accumulates `float(p)*log2(float(…))`, and `gap_and_bound` returns `float(best)/LN2` with `LN2=log(2.0)`. Its asserts use tolerances (`abs(I-1.0)<1e-12`, `1e-9`).
  - It runs on five hand-built families. The process-dilation probes (P1–P6) and `review4` P-G are exact `Fraction` checks on named instances.
  - None of these is exhaustive over a class, so L41's definition makes L75 and L120 false.
  - Main:170's "Certified exactly … in `c4_backflow_probes.py`" is unrepaired, and no open PR touches it. SC-28 and SC-31 edit Main:174/176, not :170.
- **A-B2: CONFIRMED.** I checked an exact counterexample: φ = identity, $|\mathcal C_H|=1$, $X_0$ uniform, so $X_{t+1}=X_t$.
  - No common-endpoint pair exists, so $M_1=0$.
  - The histories ending at 0 and at 1 have pushforwards $\delta_0\neq\delta_1$.
  - So L116's "that is, a pair of posteriors with different pushforwards" makes the converse false.
  - L99's $\mu_\omega$ supplies positive probability but not the shared endpoint. Main:99 has it through "such".
- **A-B3: CONFIRMED.**
  - Main:356 says globally coupled setting-dependent reversible dynamics realizes PR-box behaviour.
  - Even a static deal correlated with the settings breaks the bound.
  - Main:360's theorem needs (ii), (iii), (iv) and a ±1 outcome in every run.
  - The book's own ch01:286 says "a card mechanism is a local classical toy". The Introduction drops "local" and gives no setting-independence condition.
  - ch01:286 and FULL:630 are untouched by #968.
- **B-B4: CONFIRMED IN PART.**
  - L256 omits the Corollary's hypothesis of one-step, own-wing interventions (Main:410), which #968 adds to the book.
  - Mitigation: L252 defines the cone through interventions that read and write only their own region. Read with that definition, the "update alone" sentence is not false.
  - It is still a scope omission against the cited Corollary.
- **B-B5: CONFIRMED.** L250's "For any such explanation … at most 2" is false without measurement independence: Main §3.3(b) shows measurement-dependent models exceeding 2. L252 then states (iv), so this is a short clause fix in the framing paragraph.
- **A-B4: CONFIRMED IN PART.**
  - Under the paper's own coordinates (burn card b, with L130's "two different deals, not one rule"), $b=1-x$ has no shared root-independent prior, so $\Gamma_1$ at L186 is undefined.
  - **However**, an exact check shows the conclusion holds after re-coordinatizing the hidden sector as $c=x\oplus b$:
    - the dynamics becomes φ′(x,c) = (x⊕c, c), with the shared, root-independent prior δ_{c=1};
    - this gives $\Gamma_1$ = swap (a permutation) and $\Gamma_2=I$;
    - the control is green: uniform b gives ½J, as the paper states.
  - So L186's conclusion is recoverable, but L186 conflicts with L130.
  - Assumption-watch marker (new): whether the hidden prior is "shared and independent" depends on how the hidden sector is coordinatized, which L130's narrative treats as fixed.
  - Fix: either the auditor's wording, or state the re-coordinatization.
- **A-B5: CONFIRMED.** L37 places discriminating content in "what the world's eventual return … does with it". L158 and Main:141 say the cycle indivisibility follows from any non-deterministic step, Markov-on-window laws included, and "does not separate them".
- **A-B6 / B-B7: CONFIRMED.**
  - The PhysicalC4Discharge header (:27–35) records that its `rootedPosterior` conditions the initial seed, and that this "is not the same predicate" as the storage-time clause.
  - Its `RoutedReadback` even propagates `(x, h₀)` with the initial seed.
  - PhysicalC4StorageReadback §CS5 proves the two predicates **incomparable**: `storageReadback_not_implies_routedReadback`, and `routedReadback_not_implies_storageReadback` at :689. The sealed core satisfies the storage-time reading but not round 1's (`core_not_routedReadback`).
  - `routedAtStorage_forces_indivisible_somewhere` exists (:256, `#print axioms` at :709) but is not in the retained result.
  - Locator note: the clause's wording is verbatim at GR:52. Main §1.3's (C4) text says it "does not by itself assert a causal write-then-read cycle".
- **B-B3: CONFIRMED** (first-hand read of Mon08).
  - Mon08 proves that Markovian ontological theories need at least 2N−2 continuous variables. It contains no task.
  - It does report Hardy's result, so "Montina reports Hardy's result" is supported.
  - Main:554 cites HKLP24 [55] and Garner–Müller, not GH03 or Mon08.
  - Caution: the auditor's replacement "[HKLP24, Thm 4]" reinstates a pinpoint that r16 dropped as unread. Use "[HKLP24]" unless Thm 4 is read.
- **B-B8: CONFIRMED IN PART.**
  - `FiniteOperationalTheory` (OperationalAssembly:594) has `avail` over `Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ`, and `availExt` over `A × Fin n`, so complex-matrix kinematics is assumed.
  - L214 leaves it implicit, behind "positive states", "unitary" and "Kraus". A one-clause fix is warranted.
  - B-O6 is also confirmed: `prepAvail_post` admits only a `Unit`-outcome (deterministic) operation.
- **B-B9: CONFIRMED** as R-28, required and not applied. Severity is low: the body scopes it.
- **B-B6 / A-B9: CONFIRMED IN PART.**
  - RecurrenceHorizon, PhysicalC4Discharge and PhysicalC4StorageReadback are `kernel-only`, with `manuscript: []`. So are CausalReadback and RootedClassification.
  - The registry's `manuscripts` list omits the Introduction. **But no tool reads that list.** `lean_manuscript_census.py` globs every `papers/*.md`, so it does scan the Introduction for supersession and for `kernel:` parentheticals.
  - The Introduction has 0 `kernel:` parentheticals, so none of its 29 Appendix A identifiers is resolved.
  - I ran the tool from a copy: it passes, with 209 cited identifiers.
  - Main §2.3 (L139) understates the kernel. It names only `isPermMatrix_of_stochastic_inverse` and calls "its composition with P-divisibility" paper-only. `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148) proves overlap plus return ⇒ not P-divisible.
- **C-B1: CONFIRMED.**
  - GR:841 counts "initial conditions on Σ_E", over configurations s ∈ C_j, with Σ_E = C_B × C_R aligned.
  - GR:833–835 and BHb C1/C6(a) prove that every orbit state is a product basis state there, so H-scramble fails and A.8 has no instance.
  - BHb C2 gives $S(\rho_R)\le H(p_0)$, which supports the proposed $e^{S_{\rm Page}}$ / basis-entropy wording.
  - No open PR touches GR App. A, appendix-a G11 or ch19:72.
- **C-B2: CONFIRMED.**
  - GR:344 ("the metric evolves via Einstein's equations *before* the trace-out … never encounter the zero-point sum") and GR:573 ("denies … because gravity operates at the logically prior classical level") are unconditional, against GR:356.
  - The mirrors are mixed:
    - ch07:177 (FULL:2056): the first clause is unconditional, the rest is marked as a proposal;
    - Explainer:543 is unconditional;
    - Explainer:551's "predicts the observed value" contradicts Explainer:549's "a normalization, not a prediction";
    - Explainer:579 is unconditional.
  - **No PR.**
- **C-B3: CONFIRMED** (first-hand). Pag93 mentions black holes only by citing refs [4] and [5] (Page's own "Black hole information" and "Information in black hole radiation"). PRL 71, 3743 (hep-th/9306083) is the right source.
- **B-B1 / A-B8 (R-06): CONFIRMED.**
  - All cited declarations exist at the stated lines, with `#print axioms`:
    - `realizesSealedOICore_of_control` (OIRealization:252, on `Fin 2`);
    - `permClass_onesFixing` (PhaseSource:79), `onesFixing_not_phasesAvailable` (:52);
    - `monomialSource_not_control` (SubstratumInterface:186);
    - `readWriteSourced_not_control` (ReadWriteControl:169);
    - `substratum_residual` (StructuralClosure:383), `substratum_plus_control_qm` (:414, needs ExtendsSubstratum, StructurallyClosed, DrivesElementary, Nonempty).
  - Their families are `current`.
  - Pressure test: GR:258 says "the quarter phase is dispensable". Prefer A-B8's form, which treats the phase as a stated assumption and the missing resource as continuous state-mixing, over a form that lists "the phases" as a missing resource.
- **B-B2 / A-B7 (R-07): CONFIRMED.**
  - Main:560 (ε-form), :576 (single controlled dynamics), :592 (mutual ε-density) and :596 Summary (4) exist.
  - After SC-1 the scope is "proved in exact arithmetic", and "the bound on the realized law is open" at finite $b$, as R-40 requires.

### Task 3: corpus dependencies under owner policy 1

1. **PR-G (no PR):**
   - Main:137–139: state the rooted overlap-plus-return theorem, and routed readback in both readings (storage-time primary), with kernel anchors.
   - Census: move "recurrence horizon", "physical C4 discharge" and "physical C4 round 2" to `current`, with anchors. Do the same for "rooted classification" if R-09's full form or O-6 is used.
   - Make the Introduction's Appendix A identifiers resolvable, through the `kernel:` form or a tool change. Adding the Introduction to `manuscripts` is informational only.
2. **PR-E (no PR):** GR App. A.8–A.9 (GR:817–841); book ch07 §7.6, ch19:72 (also "Resolved…", CON-02) and :334, appendix-a G11 (:111) and :102, with their FULL mirrors.
3. **PR-A in part (no PR):** GR:344, GR:573; ch07:177 and FULL:2056; Explainer:543, :551, :579. The GR §6 heading "Dissolution…" (CON-04) was flagged in r16.
4. **PR-F in part (no PR):** Main:170 "Certified exactly"; also Main:178 and ch01:273 "minimal", if the Introduction drops the label.
5. **Card-Bell, book (no PR, not in the plan):** ch01:286 and FULL:630. ch03:188 and FULL:1064 already give locality, but not setting independence.
6. **PR-B CON-15 (no PR):** a kinematics clause in GR §3.3 and Main §3.4. It is needed for R-10 stage 2 and pairs with B-B8; CON-48 (GR:216) is recommended alongside.
7. **Main:465 (no PR, not in the plan):** the contrapositive uses $I^*$ where only $M_k$ is bounded. The Introduction's L122 has the correct $M_k$.
8. **Main §4.5 (no PR):** it lacks the Pauli-twirl classical-memory decomposition that L204 cites to it (B-O5). The mathematics checks out. Either add it to Main, or stop citing Main for it.
9. **SC-19, low priority (no PR):** Main:72 and :78, and GR:52, "(C3) follows from (C4)". This is not false, but it misattributes the reason.
10. **Existing open PRs that should land with or before #918:** #961 (SC-29, joint-law scoping in Main:510/608/610) and #968 (SC-33, Main's compressed Bell ceilings at :22, :82, :558, :646, :700, :766). #962, #964, #967 and #969 are not dependencies. #963 is recommended for consistency.

### Summary

**Blocking #918's text:**
- *False or overclaiming as written:*
  - R-01 (the Page conditional has no instance);
  - R-03 / OD-7 (exact probes);
  - A-B2 (L116 common endpoint);
  - R-32 / A-B3 (L188);
  - B-B5 (L250);
  - R-13 / OD-5 / A-B6 (wrong readback predicate; incomparable);
  - R-14 (Pag93);
  - R-17 (Mon08);
  - A-B5 (L37);
  - A-B4 (L186, internal inconsistency).
- *Required omissions under the owner's decisions:* R-06 / OD-2, R-07 + R-40 + O-12 / OD-3, and OD-15.
- *Lesser required items still open:*
  - not applied: R-11, R-16, R-27, R-28, and R-10 stage 1;
  - partly applied: R-02, R-04, R-05, R-15, R-18, R-21, R-30 and R-36;
  - confirmed in part: B-B4 and B-B8.

**Missing corpus PRs:**
- PR-G (Main §2.3 and the census);
- PR-E (GR A.8 and its mirrors);
- PR-A part (GR:344/:573, ch07:177, Explainer);
- PR-F part (Main:170);
- book ch01:286 card-Bell;
- PR-B CON-15;
- Main:465 $I^*$→$M_k$;
- Main §4.5 Pauli twirl.

No open PR (#961–#969) covers any of these. #961 and #968 exist and should land with #918.