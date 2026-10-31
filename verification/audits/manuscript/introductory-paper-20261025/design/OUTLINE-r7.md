# Introduction paper: outline, revision 7 (design stage, for owner review)

## Stage

- **Design revision 7.** It applies the re-check of design r6, `S/paper/design-r6-review/RECHECK.md` (ACCEPT WITH
  CHANGES; C1–C6 and nits 1–8), and the Weinberg landing gate. r6 is unchanged. `CHANGES-r7.md` maps each item.
- **Design revision 6, rescoped by the owner on 2026-10-26.** The scope reads: "One fundamental idea with two major
  consequences, rather than a catalogue of possible applications".
- **What it applies.** The owner's scope decision, and every required change of the r5-design review
  (`S/paper/design-r5-review/REVIEW.md`) that touches retained content. `CHANGES-r6.md` maps each item, and marks as
  "moot" the items that touched removed content.
- **What it replaces.** The r5 design files are unchanged. An earlier r6 draft, written before the rescoping, is kept
  for provenance in `S/paper/design-r6/pre-scope/` (scratch; not in the repository) and is superseded.
- **What it is.** There is no paper text. Each claim is given the sentence the draft must use, or the r4 sentence it
  must carry, with its source and verification layer.
- Nothing in the repository was changed.

## Scope

The paper covers three things, and "nothing else unless it is strictly necessary to support one of those three":

- **Quantum emergence** is the central thesis and the foundation (§§1–3).
- **The cosmological constant** is the leading application (§4).
- **Black-hole information**, as preservation versus accessible recovery, is the second application (§5).

**Owner's caution, made explicit in §4, §5, §6 and the abstract:** "neither application currently constitutes a
demonstrated resolution of its respective physics problem."

**Removed from the paper:**
- horizon entropy as an application (no supporting sentence is needed; see §4);
- Cabibbo and JUNO;
- the Page-time fraction and β (not needed for preservation versus recovery);
- the dark sector; echoes; quantum computing;
- PE-01; the arrow of time; the measurement reading.

## Baseline and sources

**Baseline.** `S/paper/draft/Introduction-r4.md`, sha256 `5f9fdcc5…68f6`, accepted. "r4:N" is its line N, and
"verbatim" means that line copied unchanged.

**Sources.**
- `main` at `687e885b`.
- The applications audit, `design/applications-audit/AUDIT.md` on #918.
- R11 `FINDINGS.md` as amended by `REVIEW.md`.
- #936 `DIFF-REVIEW.md` §6 and R1, with `DIFF-RECHECK.md` §2, for A.8's shell scope and H-decouple.

**Claim IDs.** `N-…`, registered in `CLAIMS-r6.md`.

## Page budget

r4's main narrative is 4,739 words on 12 pp, about 395 words per page (review §5). §1 and §3 figures follow the
review's measured r4 sizes; §2 is net of the sketches replaced by citations.

| § | Title | Words | Pages |
|---|---|---|---|
| — | Abstract | 260 | 0.65 |
| 1 | Introduction: Observational Incompleteness and the emergence of quantum behaviour | 550 | 1.4 |
| 2 | Theoretical foundation: the established results and their assumptions | 1,240 | 3.1 |
| 3 | Quantum emergence: what is demonstrated, and what remains open for equivalence with quantum mechanics | 870 | 2.2 |
| 4 | The cosmological constant: how OI might change the interpretation of vacuum energy | 460 | 1.15 |
| 5 | Black-hole information: preservation versus accessible recovery | 480 | 1.2 |
| 6 | Discussion and conclusion: implications, limitations and decisive open tests | 570 | 1.45 |
| | **Main text** | **≈4,430** | **≈11.2** |
| | Of which, the two applications (§§4–5) | ≈940 | ≈2.4 |

- **Outside the count:**
  - code, data and formal verification;
  - Appendix A (kernel declarations, r4:264–277);
  - Appendix B (examples: r4 §4.1, §4.2 and the card table, verbatim);
  - references.
- **Fit (C6).** The figures are the re-check's measurement (`chk/budget.py`, ±5%). The total is about 11.2 pp,
  inside the owner's 10–12, with about 0.8 pp of slack to 12. The proof sketches replaced by citations save about
  140 words net, about 0.35 pp: 310 words removed, 169 added in S-1 to S-5. The applications take about 2.4 pp,
  inside 2–3. No qualification is cut. Appendices A and B are outside the count; Appendix B adds about 550 words.
- **If the build runs over 12 pp,** the first move is r4:226 (the fixed-basis-datum paragraph of §3.2 below) to
  Appendix A. It moves text and cuts no qualification, but it moves §A.34 witness text, so it needs a re-check. Beyond these, nothing is cut: the honest count would be reported instead.

## Results register: exact statements, status, references (owner direction)

Every theorem and result the paper states. The **exact statement** is the r4 sentence named (reviewed against the
source), or the Main sentence quoted, with its hypotheses and quantifiers.
- "K" means machine-checked, with the Lean identifier given; module and line are in Appendix A (r4:264–277).
- For each displayed equivalence, the witness for each direction is given (§A.34).

| ID | Exact statement (where) | Status and layer | Reference | Witnesses |
|---|---|---|---|---|
| T1 | r4:58–62: "For every finite visible alphabet and every finite horizon K, S_K = D_K = Q_K, so each class is the set of all probability laws on C_V^{K+1}" (= Main:526) | K | [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence)] | S_K ⊆ D_K `S_imp_D`; D_K ⊆ Q_K `D_imp_Qfb`; Q_K ⊆ S_K `Qfb_imp_S`; assembled `finite_horizon_equivalence`, with the reverse inclusions as compositions (Equivalence:466–468) |
| PD | r4:66 s4: "A realization whose hidden prior is independent of x₀ exists", for a law with rational multi-time probabilities on a finite horizon, \|C_V\| ≥ 2 (Main:496) | P + exact probes | [Main §3.4, Theorem (finite-horizon process dilation)] (Main:496) | — |
| T2 | r4:86–90: "In every faithful realization: (a) … (b) for histories p, p′ ending at x … (c) M_t ≤ I(X_<t;H_t∣X_t) ≤ log₂\|C_H\|" (= Main:582) | K for a joint law of history, present and hidden state; the time-t identification is not machine-checked (r4:92; Main:99) | [Main §3.4, Theorem (unavoidable hidden predictive memory)]; [CT06] | `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory` |
| C | r4:94 s1: "M_t > 0 holds exactly when every faithful realization carries readout-relevant hidden memory at t" (= Main:99) | P; the CMI vanishing criterion and the time-t identification are not machine-checked | [Main §1.5] | ⇒: T2(a) in each realization; ⇐: T2(a) in one realization, which exists by T1 (`S_imp_D`). Main:99 states both |
| CAP | r4:96 s2: "A realization of a law whose conditional past–future information reaches I* needs \|C_H\| ≥ 2^{I*}" | K | [Main §3.4, Theorem (C3 necessity)] (Main:484, :492) | `c3_necessity`, `card_hidden_ge_two_pow_Istar` |
| PIN | r4:96 s3: "If two visible histories of length k with a common endpoint, each of probability at least p₀, induce next-step laws at total-variation distance at least δ, then I(X_<k;X_{k+1}∣X_k) ≥ p₀δ²/ln 2" | P + exact probes | [Main §2.3]; [CT06] | — |
| SI | "A finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix" (= Main:133; r4:114 s1 with "finite square" restored, C5) | K | [BB12, Problem 23]; [Main §2.3, Lemma (stochastic inverse)] | `isPermMatrix_of_stochastic_inverse` |
| T3 | r4:110: "Let φ be a bijection of a finite set. If two rows of Γ_s overlap in a column and Γ_n = I for some n > s, the family is not P-divisible on {0,…,n}" | K (rooted form) | [Main §2.3]; concurrent [Dou26, Prop. 1] | `pIndivisible_of_rooted_identity_return_of_overlap` |
| RB | Main:137: "For a fixed finite reversible OI representative, genuine C4 history readback implies that the rooted visible stochastic process is indivisible somewhere in its full recurrence cycle" | P from history-level (C4) (Main:139); K from the routed-readback form | [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]; [Main §1.3, the realization clause of (C4)] | `routed_forces_indivisible_somewhere` (routed form only) |
| CP | r4:120, as Main:326: "for the permutation-dilation family, P-indivisibility implies CP-indivisibility" | P | [Main §3.2, Theorem (CP-indivisibility, framework scope)] | — |
| HAD | r4:120: the Hadamard family is CP-divisible with P-indivisible populations | explicit example | [Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)] | — |
| BORN | r4:78: "The relation p=\|U\|² is part of the definition of Q_K … the quadratic exponent is therefore not selected" | P (negative statement) | [Main §3.4; Bar26, Thm 3.1] | — |
| T4 | r4:216: "For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold" | K, both directions | [GR §3.3, Theorem (operational-completion characterization)] | ⇒ `physical_of_exactAll`; ⇐ `exactAll_of_physical_general`; iff `exactAll_iff_physical_general` |
| IND | r4:220: on the qubit each condition is independent of the other four and of a fixed finite observation process satisfying (C1)–(C4); OI alone does not imply QM | K | [GR §3.3] | `five_way_minimality`, `oi_alone_not_qm` |
| REL | r4:224: two coherent lifts can differ by a time-dependent right action and then have different relating evolutions; a constant deformation cancels | K | [Main §3.4, Remark (scope: representability, not selection of the relating evolution)] (Main:624) | `gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative` |
| BR | r4:226: same one-step matrix ⇒ root-conditioned laws agree; rooted families agree ⇒ one-step matrices equal; each law is fixed-basis realizable and stochastic | K, each direction separately (no equivalence is displayed) | Main:624 | `bridge_traj`; `rooted_eq_iff_slice_eq` (forward direction only); `realData_traj_stochastic` |
| FC | r4:230 (R2-2): finite realizations factor through N states; the unboundedness is imported | factorization proved; unboundedness imported | [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)] (Main:538); [GH03; Mon08; Har04 as reported] | — |
| BELL | r4:234 (5) with T1 | Bell-locality proved; H-Bell open | [Bel64; CHSH69; Main §3.3] | — |
| App. | CC and BH results | see `CLAIMS-r6.md` (N-CC…, N-BH…) | | |

## Section plan

Layers:

| Code | Layer |
|---|---|
| K | Lean kernel (machine-checked) |
| P | written proof |
| E | exhaustive finite computation or exact probe |
| A | exact algebra |
| N | numerical |
| L | literature |
| I | interpretation |
| O | open |

### Abstract (240 words)

**Quantum emergence (R16).**
- r4:12 sentences 1–3.
- Sentence 5, the memory and indivisibility sentence, with "(each with one step not machine-checked)".
- Sentence 4 reduced to "and the Born exponent is not selected".
- r4:12's operational sentence and its "Open are …" sentence, both verbatim.

**Two consequences.**
- **N-AB1:**

  > Applied to the cosmological constant, OI places the zero-point sum and the effective cosmological constant at
  > different levels of description; whether the zero-point sum sources curvature depends on covariant field
  > equations that are not derived, so this is a proposal, not a resolution.
- **N-AB2:**

  > Applied to black-hole information, finite computations separate the conservation of information under bijective
  > dynamics from its recovery by an observer with restricted access; the framework's Page curve is not established,
  > and the information problem is not resolved.

**Must not contain:** "dissolve", "resolve" (except negated), "predict", "derivation of quantum mechanics",
"equivalence of quantum mechanics".

**Owner marker.** R11 (r4:14), carried.

### §1 Introduction: Observational Incompleteness and the emergence of quantum behaviour (430 words)

**§1.1** is r4:20–26, verbatim.

**§1.2 The idea and its two consequences.**
- r4:30, verbatim: stochastic laws, memory and indivisibility; the correspondence of §2 is exact and universal.
- **N-INT1**, which replaces r4:30's last pointer sentence:

  > The paper develops one idea, OI, and two of its consequences: the foundation and its quantum-emergence results
  > (§§2–3), and two applications, the cosmological constant (§4) and black-hole information (§5). Neither
  > application is a demonstrated resolution of its problem; §6 states what would decide each.
- **Contributions.** r4:32 adapted to the new scope; every reviewed qualifier is kept.

  > The paper claims no new theorem or physical result; its contribution is expository. It presents the established
  > mathematical results of OI together, separates the mathematical correspondence from its physical interpretation,
  > and states two consequences with their conditions and limitations. The black-hole results of §5 are reported from
  > unpublished repository research records [BHa; BHb], with written proofs and exact or exhaustive checks, whose
  > novelty has not been established.

  The rest of r4:32 is verbatim: the components of Theorem 1, the §2.4 bounds, the recurrence argument, and the
  results proved in [GR] and [Main]. Section numbers are adjusted.
- **Conventions.** r4:34, verbatim. The decision-2 OWNER marker (r4:36) is carried.

**Does not claim:** a new theorem; a new viewpoint; that OI is established or tested.

### §2 Theoretical foundation: the established results and their assumptions (980 words)

**Owner direction, 2026-10-26.** The Introduction cites the full derivations in the technical papers and does not
re-derive them. Each result below is stated exactly, with its hypotheses and quantifiers, its status and layer, and
its reference; see the "Results register". Proof sketches are replaced by citations. At most one or two sentences of
intuition remain, worded so that they cannot be read as a proof.

**Carried verbatim** (statements, hypotheses, status words, references, §A.34 witnesses):
- r4:40–64: the three classes and Theorem 1, with its witnesses.
- r4:70–72: Attribution and Calvo. Attributions are references, not proof.
- r4:74–80: §2.3 scope. The two one-clause reasons (|U|^p at every p > 0; finite order ⇒ periodicity) are statements
  of what the cited results give.
- r4:82–90: Theorem 2 (a)–(c).
- r4:96: the capacity and Pinsker bounds, with their status words. "By Pinsker's inequality" names the tool, not a
  proof. The draft adds "(in bits)" to the Pinsker bound (nit 8; Main:166–170).
- r4:98: (C1)–(C4).
- r4:108: the P-divisibility definition and its criterion sentence. This is the one intuition sentence for Theorem 3,
  cited to [RHP14, Thm 2.4; BD16, Prop. 1].
- r4:110: Theorem 3.

**Sketches replaced by citations:**

| r4 | Removed | Replaced by |
|---|---|---|
| r4:66 Realization | the step mechanics (clock, record, injectivity, extension to a bijection) | S-1: "For $\mathsf S_K\subseteq\mathsf D_K$ the realization stores a sampled trajectory, with a clock, in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]. For a law with rational probabilities, a realization whose hidden prior is independent of $x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation)]; it is proved on paper, with exact probes." The second sentence is r4:66 s4 with Main:496's rationality hypothesis restored (C4) |
| r4:68 Quantum representation | the non-disturbance argument | S-2: "For $\mathsf D_K\subseteq\mathsf Q_K$ the representation is the permutation unitary $U_\varphi\lvert x,h\rangle=\lvert\varphi(x,h)\rangle$, read out in the configuration basis at every step [Main §3.4]; $\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule." |
| r4:92, last sentence | "The proof is the data-processing inequality [CT06] applied to $X_{t+1}=f(X_t,H_t)$." | S-3: "[Main §3.4, Theorem (unavoidable hidden predictive memory); CT06]." r4:92's two status sentences are kept verbatim |
| r4:94 Corollary, direction sentences | "The forward direction applies (a) in each realization. The converse applies (a) in one realization, which exists by Theorem 1. Both directions use …" | S-4, a citation form that keeps a source for each direction (§A.34): "**Corollary** (proved on paper [Main §1.5]). $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward direction rests on Theorem 2(a) in each realization; the converse on Theorem 2(a) in one realization, which Theorem 1 supplies (`S_imp_D`); both use the standard vanishing criterion for conditional mutual information [CT06], which, like the time-$t$ identification, is not machine-checked." |
| r4:112, sentences 1–2 | the overlap-and-return route ("Finite order of φ gives a return … which no stochastic divisor permits") | Removed. The rest of r4:112 is kept, with a referent supplied (nit 2): "Theorem 3 is machine-checked in its rooted form, and Doukas states the same overlap-and-return argument concurrently [Dou26, Prop. 1]. Monotone distance is necessary for P-divisibility but not sufficient [Main §2.3]." |
| r4:114, from "(1) If every …" through "… stochastic inverse of $\Gamma_k$." | steps (1)–(3) | S-5: "On a fixed finite reversible substratum, history readback forces indivisibility somewhere in the recurrence cycle [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]." r4:114 sentence 1 (the stochastic-inverse lemma, machine-checked, [BB12]) is kept with "A stochastic matrix" → "A finite square stochastic matrix" (C5; Main:133; without "square", (1 0)·(1 1)ᵀ = I₁ is a counterexample). Its last sentence (machine-checked from the routed-readback form [Main §1.3, the realization clause of (C4)]; from history-level (C4) proved on paper) are kept verbatim |

**Additions.**
- After r4:72, **N-LIT1:**

  > 't Hooft has argued that quantum mechanics may serve as a tool for analysing a system that is classical at its
  > core, and has discussed how such a view can be reconciled with Bell's theorem [tH14].

  [abs]; no priority is assigned.
- r4:42's lead adds Theorem 3.

**Pointer.** The examples (r4 §4.1–§4.2) and the card table go to Appendix B, verbatim, with one pointer sentence:

> Appendix B works a minimal model of Theorem 3 with six hidden states, a process with memory but no short-window indivisibility,
> and the smallest realization of Theorem 3, a two-card game, with its classical and quantum scope.

**The exception the owner names.** The card table's classical-memory decomposition is the one step not in the corpus.
It stays in Appendix B as r4:164's sentence (the instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$ and the
channels $\mathrm{Ad}_{\sigma_o}$). Its source is ERRATUM-r4, which rests on the one-line Pauli-twirl identity
$\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)I$. The initialized-slot contrast stays cited to [Main §4.5].

**Does not claim:** that representability distinguishes memory; selection of the Born exponent; an all-time
realization; short-window indivisibility.

### §3 Quantum emergence: what is demonstrated, and what remains open for equivalence with quantum mechanics (900 words)

**§3.1 What is demonstrated.**
- r4:118–122, verbatim:
  - the indivisibility is global;
  - the three notions, kept apart, with the Hadamard example and [BLP09; BJA17];
  - Theorem 1 as a representation result.
- The reference "(§4.2)" in r4:118 becomes "(Appendix B)".

**§3.2 What remains open for equivalence with quantum mechanics.**
- **From the correspondence to operational quantum mechanics** (nit 2). r4:210–220, verbatim: Theorem 4 with both
  witnesses; "for every nonempty finite carrier"; qubit independence; OI alone does not imply QM; (iii)–(v) open.
- **The relating evolution is not selected.** r4:222–226, verbatim.
- **No fixed finite carrier reproduces a qubit.** r4:228–230, verbatim (R2-2).
- **The Born exponent.** One sentence pointing to r4:78: the origin of the quadratic exponent is open [Main §3.4;
  Bar26, Thm 3.1]. r4:78 is not repeated.
- **Bell structure.** r4:234 item (5), with T1, verbatim.

**Does not claim:** derivation of QM; equivalence with QM; P-indivisibility = quantum non-Markovianity.

### §4 The cosmological constant: how OI might change the interpretation of vacuum energy (530 words)

This is the leading application. Every sentence is written out below (R6–R9 and r5-review nit 7 applied), so the
outline is self-contained. Item order:

1. **N-CC0 (R9):**

   > Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density some
   > 120 orders of magnitude above the observed one, the exact power depending on the cutoff convention; if that
   > density sources curvature, it must be cancelled to that accuracy.

   **Landing gate (r6-recheck O2):** Weinberg 1989 (*Rev. Mod. Phys.* 61, 1) is read first-hand and cited here.
   Otherwise N-CC0 states a standard number without a citation.
2. **N-CC1 (R8, nit 7):**

   > In OI the zero-point sum of the emergent quantum description and the effective cosmological constant are
   > defined at different levels of description. A uniform shift of the emergent Hamiltonian changes no visible
   > transition probability, so the offset has no content in the visible statistics of the quantum description
   > [GR §6.2].

   Then the qualifier:

   > The invariance is the familiar statement that no non-gravitational measurement sees the absolute vacuum energy;
   > the proposal's content lies in how the two levels couple to geometry.
3. **N-CC2 and N-CC3 (R7):**

   > Whether the offset also fails to source curvature is a separate coupling question. Settling it requires
   > covariant field equations derived from the substratum, with their coupling to sources, which are open [GR §6.2].
   > The quantum description therefore does not decide between gravitational completions that differ by a term
   > $\rho_C\,g_{\mu\nu}$, such as $\mathcal G_{\mu\nu}=8\pi G\,T^{\rm cl}_{\mu\nu}$ and $\mathcal G_{\mu\nu}=8\pi
   > G\,(T^{\rm cl}_{\mu\nu}-\rho_C\,g_{\mu\nu})$ [GR §6.2]. The proposal that the mismatch requires no cancellation
   > is therefore conditional on that open step.

   **Naming rule.** At first use: "the covariant field equations and their coupling to sources (Level G3 of [GR])".
   Never a bare "G3".
4. **N-CC4 (R6):**

   > If the covariant field equations take the form [GR] targets, $E_{\mu\nu}[g,\mathrm{OI}]=8\pi G\,(T_{\mu\nu}-
   > \mathcal F[g,T]\,g_{\mu\nu})$, with the classical stress-energy of the substratum as source, the zero-point sum
   > of the emergent description is not a source and needs no cancellation; the vacuum term that remains, from the
   > substratum's classical energy density and from $\mathcal F$, is not computed.

   Then **N-CC5:**

   > It does not explain the observed value of Λ, which enters as a cosmological input. The scale ρ ~ H²/G is the
   > Friedmann normalization of the total density, and the fraction carried by Λ is an input.
5. **N-CC6 (R9):**

   > With a Planck-scale cutoff the mismatch equals the de Sitter entropy up to a numerical factor fixed by the cutoff
   > convention; this is a dimensional identity, not an independent prediction.

   "The de Sitter entropy" is used as a standard quantity. No claim about the 1/4 is made, and the horizon-entropy
   material is removed (owner scope). No sentence on horizon thermodynamics is needed here.
6. **N-CC7:**

   > How the energy of electroweak and QCD vacuum transitions couples to gravity is not fixed by the descriptive
   > distinction and requires the same open coupling step.
7. **N-LIT2** (r6-recheck nit 7: written out in full; the text is r5's):

   > Removing the vacuum energy of matter as a source of curvature is also the aim of the trace-free Einstein
   > equations, which leave the observed value of Λ unexplained [EvEMU11], and of vacuum-energy sequestering, which
   > extends to the vacuum energy of phase transitions [KP14]; Volovik argues from the thermodynamics of quantum
   > many-body ground states that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]. The present
   > proposal differs in locating the gravitational source in the substratum microstate, and its coupling step is
   > open.

   - At abstract strength, with a VERIFY on each.
   - Padmanabhan is added only after it is read (first on the reading list for §4).
8. **N-CC8, which closes the section and states the owner's caution:**

   > A derivation of the covariant field equations, with their conservation and source coupling, from the substratum
   > would turn the proposal into a theorem or refute it. Until then the proposal reinterprets the problem and does
   > not resolve it.

**Sources:** GR:12 (ladder and target equation); GR:356; GR:360; GR:581 (not repeated); audit `cc.py`; review
`chk/indep.py`.

**Does not claim:**
- dissolution or resolution;
- "no decoupling mechanism is needed";
- "eliminates the cancellation";
- "the value the framework expects";
- ρ ~ H²/G as an output;
- a prediction of Λ or Ω_Λ;
- that the vacuum term of the target equation is small (R6);
- that the completions share partition and calibration (R7);
- convergence language about the de Sitter literature;
- that GR:583's gauge argument settles the coupling;
- anything about the Bekenstein–Hawking 1/4.

### §5 Black-hole information: preservation versus accessible recovery (520 words)

1. **Setting (R3).** r4:172 sentences 1–3 and 5, verbatim. Sentence 4 (the verification layers) goes to §6
   limitation 4.
2. **N-BH1:**

   > Under OI, information is conserved in the global reversible dynamics because the dynamics is a bijection, which is
   > a premise of the framework. Conservation neither implies nor is necessary for recovery from the records an
   > observer can access: finite exhaustive computations exhibit bijections with no accessible advantage and
   > non-injective maps with exact recovery [BHa].

   - Then r4:181's definitions and counts (C2, the re-check's text, plus the 32-map clause the coordinator asks for):

     > Of the 40,320 bijections of $\{0,1\}^3$, 1,376 give zero accessible advantage, the gain in success probability
     > over a blind guess, for a binary message with one register unread after two emissions. For bijective dynamics,
     > complete endpoint access gives exact recovery, and with the joint values $\mathcal U$ of the unread registers
     > inaccessible, $P_{\rm succ}\ge1/|\mathcal U|$; 32 non-injective maps of $\{0,1\}^2$ violate this bound. These
     > endpoint guarantees are sufficient, not necessary.

     The 32-map clause is BH-01 REPORT:21 ("without bijectivity 32 maps violate the bound"), as in r4:181.
   - The [Sha79] sentence is kept, with its VERIFY.
   - Sources: Main:66; BH-01 REPORT:17, :36. Not ch19:72 (R18).
3. **N-BH2 (R1 as corrected by C1):**

   > In the framework's nested-partition construction the Page value enters only through the scrambling hypothesis
   > H-scramble, which no bijection satisfies from a definite configuration with configuration-aligned cuts [BHb, C1,
   > C6(a)–(b)]. H-scramble posits equidistribution of the orbit on an energy shell. The mean entropy of that ensemble is
   > Page's average $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$ [Pag93] when the shell is the full product
   > space; on a smaller shell it differs in general, in a direction that depends on the shell [BHb, C6(c)].

   C1, the re-check's exact text. It follows DIFF-RECHECK §5 N1: the value holds on the full product space and fails
   in general on a proper shell.
4. **N-BH3 (R2, verbatim plus "in a pure joint state", from #936 DIFF-REVIEW R1):**

   > The Page curve of [GR App. A] is not established. Its stated hypothesis H-scramble is open. It also requires that
   > the black hole and its radiation evolve as a closed system in a pure joint state, uncoupled from the sector
   > beyond the cosmological horizon and from the rest of the visible sector, over whole cycles of the dynamics;
   > timescale ordering does not supply this, since $t_{\rm evap}/\tau_B^D \ge 10^{57}$ at 30 solar masses over the
   > assumed parameter intervals [BHa, item F]. Its stated value is established only for a full-product shell, and what the
   > cycle-typicality argument supplies is a time average at a fixed bipartition, so the curve along one trajectory is
   > open [BHb, C6(c)–(d)]. In the dependency ladder of [GR] the Page curve is also conditional on the covariant field
   > equations. The black-hole information problem is not resolved here.

   The label "H-decouple" is used only once #936 lands and the label is adopted.
5. **Open steps (N-BH5)** (one sentence, from r4:201):

   > The generalized second law is not derived [GR App. A.6]; agreement with quantum-extremal-surface computations
   > [Pen20] is not established; the correspondence between islands and substratum cycles is conjectural [Book §7.6].

   The Page time and β are omitted (owner scope). Penington stays only as the QES reference.

**Sources:**
- Main:66;
- BH-01 REPORT:17, :36, :211–241;
- BH-02 REPORT:14, :18–21;
- GR:12, :811, :817, :841;
- REVIEW §1 C.4;
- DIFF-REVIEW §6 and R1;
- review `chk/shell.py`.

**Does not claim:**
- resolution;
- that the radiation carries the information;
- the Page curve, pointwise or as a cycle average on a restricted shell;
- a falsifier;
- QES agreement;
- a change of the external observer's primary partition (GR:603).

**Owner markers.** R11 at r4:178, :187 and :203, with text per the REVIEW verdicts. The R12 marker (Page time) is
dropped, because its content is removed.

### §6 Discussion and conclusion: implications, limitations and decisive open tests (500 words)

**§6.1 Implications** (about 90 words; N-DI1; C3 applied). Three sentences:

> If the hypothesis holds, the fixed-basis statistics of quantum theory are the visible laws of an embedded observer,
> and their departures from Markov behaviour are memory carried in an inaccessible sector; whether the rest of
> operational quantum mechanics follows depends on completion conditions that OI does not imply (§3.2). Two
> long-standing problems would then change form: vacuum energy becomes a question about how two levels of
> description couple to geometry, and black-hole information separates into conservation and accessible recovery.

C3, the re-check's exact text. Bell-violating correlations are not attributed to memory: they need H-Bell (§3.2,
Bell structure).

The sentence is conditional ("if the hypothesis holds") and is built from Theorem 1, r4:122 and §§4–5. It is an
interpretation (layer I) and asserts no resolution.

**§6.2 Limitations** (about 250 words). These are r4:238–243, adapted:
1. r4 item 1, verbatim.
2. r4 item 2, verbatim.
3. r4 item 3, verbatim (pointers adjusted).
4. **R5 adapted.** The Page-time clause is dropped, because that content is removed:

   > No resolution of the black-hole information problem: the Page curve of [GR App. A] needs H-scramble and the
   > closure of the black hole and its radiation, in a pure joint state, over whole cycles; its stated value is
   > established only for a full-product energy shell; and it gives a cycle average rather than a curve along one trajectory; the correspondence with islands is conjectural; the
   > generalized second law is open; and the results of §5 concern finite toy models, each proved on paper or checked
   > exhaustively at small size or by exact arithmetic. No claim is made that information reaches $D$, that [GR, Thm
   > A.7] fails within its stated scope, or that no other decoupling argument exists.

   The R11 marker is carried.
5. r4 item 5, verbatim.
6. r4 item 6, verbatim, pointing to Appendix B.
7. No prediction of the value of Λ or Ω_Λ, and no resolution of the cosmological constant problem: §4 is conditional
   on the covariant field equations.
8. **R12, verbatim:**

   > No claim that the viewpoint is new: deterministic systems analysed with quantum methods have been studied before,
   > for example in [tH14]. The paper's results are the theorems and their scopes.

**§6.3 Decisive open tests** (about 120 words; N-DT1). Each item says what would decide.

> For quantum emergence: whether a physical substratum supplies completion conditions (iii)–(v), and whether
> history readback (C4) holds at the cosmological partition [GR §2.2]; no experiment yet distinguishes OI from
> standard quantum theory, and no memory-witness constraint is established [Main §4.5]. For the cosmological
> constant: a derivation of the covariant field equations with their source coupling. For black-hole information:
> whether H-scramble and the closure condition hold, the Page value on the relevant shell, and, in [GR]'s ladder,
> the covariant field equations. The open problems of
> r4 §6.4 (1)–(4) remain.

- Compress r4:234 items (1)–(4) to a clause list if space requires; keep each item.
- Sources: GR:20, :52; Main:704; GR:12.
- Layer: O.

**§6.4 Conclusion** (about 80 words). One sentence per part: the correspondence; the two consequences as proposals
with their conditions; "neither application is a demonstrated resolution". The R11 marker (r4:251) is carried.

### Back matter (outside the count)

- **Code, data and formal verification.** r4:254–262 (the BH paths kept; the probes path kept for §2). The §A.42
  marker is carried.
- **Appendix A.** r4:264–277, verbatim.
- **Appendix B. Examples.** r4:130–143 (§4.1–§4.2) and r4:145–166 (card table), verbatim. r4:166 already carries the
  Bell non-claim. Placement relative to the approved raw group is checked at build.
- **References.**
  - r4's list, minus [Pag05] and [Pag13]. Keep Pag13 only if r4:172's problem statement still cites it.
  - Plus [tH14], [EvEMU11], [KP14] and [Vol06].
  - [Wei89] and Padmanabhan only once read.
