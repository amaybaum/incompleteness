# SC-17: Explainer Bell summaries, the selector paragraph and the center-independence chain (#942 / #946)

Base: `main` at `0d917665`. Each site is restated at the strength of its anchor. No claim is strengthened. The Bell
anchor is Main §3.3, Theorem (Bell ceiling for a screened local completion), with the either/or that follows it: given
determinism and a ±1 outcome in every run, a completion reproducing quantum Bell correlations gives up ontic parameter
independence ((ii) and (iii) with the cone lemma) or measurement independence ((iv)). The framework gives up the first.
Measurement independence is a posit about the initial condition. Compatibility of preparation-indexed adjacency with
operational no-signaling and the continuum-curvature limit is the open hypothesis H-Bell (Main §3.3, Corollary). The
selector and chirality anchors are SM §4.1 (form lemma and its Remark (scope); "Center independence: exact scope after
projection"; "Linearity and coefficient selection: revised scope") and SM §4.3 (Theorem 3, its Remark, "Scope in the chain").

| Site | Was | Anchor | Now |
|---|---|---|---|
| Explainer :709 | entanglement is the encoding of correlations "written into the hidden sector during preparation and haven't been read back yet" (a pre-setting local record) | Main §3.3 theorem and either/or; Corollary (H-Bell) | Correlations carried by the shared preparation and the indivisible joint process. Bell-violating ones are not a locally read preparation record: under determinism and a ±1 outcome in every run, ontic parameter independence plus measurement independence gives \|S\| ≤ 2, so a completion reproducing quantum Bell correlations gives up at least one. The framework drops the first. Whether the SM/GR substratum supplies that dependence, through preparation-indexed adjacency, while preserving operational no-signaling and its continuum-curvature limit is H-Bell, open. |
| Explainer :767 (the selectors) | "The dynamics is unique"; CI, isotropy and linearity "select exactly one"; CI "necessary for emergent QM", "proven analytically … via an information-screening mechanism"; linearity selected by maximum propagation speed, unique maximization of P-indivisibility, and Unruh equilibrium | SM §4.1 form lemma (form fixed up to one coefficient α; nearest-neighbor range assumed); SM §4.1 CI scope (CI does not imply statistical independence after projection; memory from the readback lemma, P-indivisibility from finite recurrence, without CI); SM §4.1 linearity scope (the speed and P-indivisibility arguments "do not hold as selectors"; Unruh and Lorentz are downstream tests of the observer-level operator); no information-screening result exists in the corpus | Form fixed up to α, at either level, any q and d. Nearest-neighbor range is an assumption. CI is a condition on the update and does not carry the reduced memory or P-indivisibility. Its descent to a zero observer-level self-weight is open. Linearity rests on the amplitude-scale-gauge lemma. The lift is stable exactly for α ≤ 1/d, and α = 1/d, the largest stable value, makes its spectrum gapless (SM §4.1, Remark on the coefficient). The bijection-to-operator map is open, so Lorentz and Unruh are tests, not selectors. |
| Explainer :769 | wave equation "selected solely by the QM requirement plus symmetry" | as :767 | form fixed by CI, isotropy and linearity at nearest-neighbor range |
| Explainer :771 | "**No free parameters.** The wave equation is selected, not chosen. The lattice spacing is fixed by the gap equation. The entropy coefficient is determined by thermal matching. … There is nothing to tune." This contradicts :477, :769 and :1043. | as :767; GR §4 ("one free geometric parameter (ε)"; "with σ undetermined it fixes only the ratio ε/√σ = 2 l_p"; conditional on H-slope, GR §3.2); GR §5 (the 1/4 is fixed by thermal matching, whatever σ); SM §2.7 (the alphabet-size hypothesis does not fix σ) | "**Few free parameters.**" Form fixed up to α, with α = 1/d the largest stable value of the lift, where its spectrum is gapless. One free geometric parameter, ε. σ is undetermined: the gap equation (conditional on H-slope with the horizon and frame conditions) fixes only ε/√σ = 2 l_p. The BH 1/4 is fixed by the same thermal matching, under the same conditions, whatever σ. The dispersion relation is an identity of the observer-level operator, and its correction amplitude 4σ/45 carries σ. |
| Explainer :773 | "Seven passed checks with no free parameters" | as :771 | The paragraph is restated as consistency checks: the quantum description and the GR inputs come from different arguments on the same dynamics, each of the seven checks could have failed, and they are consistency checks with one free geometric parameter (ε) and σ undetermined, not proof. The favourable self-assessment ("what rigidity looks like", "distinguishes a framework describing something real") is removed (§A.23, §A.32). |
| Explainer :818 | "the specific lattice dynamics selected by the QM and GR requirements" | as :767 | "the specific lattice dynamics of the center-free branch" |
| Explainer :820 | "The wave equation selected by the QM requirement" | as :767 | "The wave equation of the center-free branch" |
| Explainer :974 | "the dynamics selection theorem pins the wave equation — it's the unique dynamics consistent with QM emergence, isotropy, and linearity" | as :767 | for a rule assumed nearest-neighbor, center-free, isotropic and linear, the form lemma fixes the wave equation up to one coefficient; those conditions are inputs of the lemma and are not derived from observed QM or GR [SM §4.1]. The earlier framing "if your physics includes Einstein gravity …" is removed, since the lemma takes no input from GR |
| Explainer :826 (contradiction with SM) | "The Higgs mechanism from one condition": the CI condition "($\alpha = 0$)" that "produces the quantum phenomenology's memory structure" also enforces chirality; "One algebraic condition … simultaneously produces the quantum phenomenology, chiral fermions, and the necessity of a Higgs boson" | SM §4.3 "Revised chain" ("Any claim that one algebraic CI condition simultaneously forces memory and chirality is therefore unavailable"); SM §4.1 CI scope; SM §4.3 Theorem 3; SM §4.11; SM §4.7 Theorem 11 Scope (Higgs doublet is phenomenological input). SM's body is right. | On the staggered branch with the normalization α = 1/d, CI (no center coupling; α is the neighbor coefficient) gives exact staggered chiral symmetry; the correspondence between center couplings and staggered masses holds at that normalization (SM §4.3). With the center-independent gauge sector, explicit masses are forbidden in the emergent theory, and the Higgs is the unique renormalizable, unitarity-preserving mechanism (SM §4.11). The doublet is input, which the singlet taste accommodates under H-spin' (SM §4.7, Theorem 11 and its proof). CI is not the source of the memory structure. |
| Book ch05 :95 (+FULL :1424) | chiral symmetry "equivalent to" CI: "any non-zero center coupling would produce a non-zero fermion mass term"; CI "the structural feature that produces the memory-bearing sector" is "the same commitment that produces exact chiral symmetry"; "chiral fermions that center independence forces" | SM §4.3 Theorem 3 proof (a staggered mass term squares to a center coupling); SM §4.3 Remark (C = 2(1−d) is not a mass term; its 4D staggered factorization is chiral); SM §4.3 "Revised chain" | On the staggered branch with the normalisation α = 1/d, CI gives exact chiral symmetry. Off that normalisation not every non-zero center coupling is a mass term: at α = 1, C = 2(1−d) is the massless 4D Laplacian's diagonal. CI does not produce the memory-bearing sector, and the claim that center independence alone forces both memory and chirality is not available (SM §4.3, at the scope of "is therefore unavailable"). The Higgs mechanism acts on the chiral fermions of this branch. |
| Book ch03 :186 (+FULL :1062) | entanglement "in the framework's mechanism proposal" is the "encoding of correlations written into the shared hidden sector at preparation and not yet read back" | as Explainer :709 | Mirrors the Explainer :709 text. The Bell-violating completion is ontically parameter-dependent since it retains measurement independence. The coherent/composite-lifting clause and the closing sentence are kept. |
| Explainer :58 | MI + ontic PI ⇒ Bell-local, "so the framework retains MI and takes ontic parameter dependence" (no ±1-every-run hypothesis; no H-Bell) | Main §3.3 | Adds a ±1 outcome at each wing in every run. A reproducing completion gives up at least one of the two. H-Bell is stated as the open compatibility condition: whether the SM/GR substratum supplies that dependence, through preparation-indexed adjacency, while preserving operational no-signaling and its continuum-curvature limit. |
| Explainer :300 | "pointwise graph locality plus a measurement-independent pre-setting ensemble gives a Bell-local model"; "therefore takes the ontic-parameter-dependent branch" | Main §3.3 (ii)–(iv) and either/or | Graph locality spelled out: own-wing read/write interventions, and ±1 outcomes in every run read before the remote cone arrives. A Bell-violating completion gives up ontic PI or MI, and the framework gives up the first. |
| Explainer :338 | ceiling from response-fixing microstate, common ensemble and "coupling range does not connect the wings before readout" | Main §3.3 (ii), (iii), ±1 in every run | Adds own-wing read/write interventions and a ±1 outcome in every run, read before the remote setting reaches it through the coupling graph. |
| Explainer :563 | "measurement independence plus parameter independence would force Bell factorization" | Main §3.3 | Adds a ±1 outcome at each wing in every run. The independence is ontic parameter independence. |
| Explainer :665 | "measurement-independent and parameter-independent … Bell-local" | Main §3.3 | Adds "ontically" and a ±1 outcome in every run. |
| Explainer :1017 (table) | "quantum CHSH therefore requires ontic parameter dependence with operational no-signaling" (either/or omitted) | Main §3.3; Main :22 | Adds ±1 in every run. Quantum CHSH requires ontic parameter dependence (the branch taken; whether preparation-indexed adjacency supplies it with no-signaling and the continuum-curvature limit is the open hypothesis H-Bell) or measurement dependence. |

Sites in the class checked and left unchanged:

- **Explainer :340, :342.** They state the declined measurement-dependent horn, preparation-indexed adjacency, H-Bell, the 0.0309-bit
  bound and the stochastic Tsirelson layer at Main's scope. :340 carries the all-caps "FAILS" (§A.33), which is outside this unit.
- **Explainer :970, :976.** H-Bell and non-uniqueness of the Bell-inclusive completion are stated.
- **Explainer :828.** The matrix wave equation follows from "the selection criteria". This matches ch05 :99 ("sole free parameter of
  this branch"), with the nearest-neighbor range left implicit. It was not in the audit item.
- **Book compressed Bell ceilings.** These sites state the either/or and ontic parameter dependence but omit own-wing read/write
  interventions or the ±1-every-run hypothesis, or both: ch00 :55, ch01 :16, :169 and :183, ch02 :188, ch03 :162, :164 and :180,
  ch04 :90 and :92, ch18 :110, appendix-c :32 and :34, glossary :19, and their FULL mirrors. Main's own summaries (:22, :646, :766,
  :770) carry the same compression. These are the audit's book and Main SC-17 sites, and they are left to that unit.
- **Book appendix-c :38, :42 and :230, ch03 :182.** They name ontic parameter dependence and operational no-signaling. No ceiling is
  stated beyond Main.
- **ch01 :217, ch02 :20 ("written into the hidden sector").** These concern (C2) persistence of a temporal record, not Bell.

Re-grep over `papers/*.md`, `book/*.md`:

- **Zero hits remain** for each of: "written into the hidden sector during preparation", "written into the shared hidden sector at
  preparation", "selected solely by the QM requirement", "selected by the QM requirement", "information-screening", "select exactly
  one", "uniquely maximizes P-indivisibility", "The dynamics is unique", "simultaneously produces the quantum phenomenology", "that
  center independence forces", "produces the memory-bearing sector", "unique dynamics consistent with QM emergence", "selected, not
  chosen", "Higgs mechanism from one condition", "encoding of correlations", "selected by the QM", "selected by QM", "QM and GR
  requirements", "QM requirement" and "no single condition forces". "No free parameters" and "nothing to tune" have 0 hits in the
  Explainer. Their book hits concern other quantities: Tully-Fisher, the $\mathcal N_{\max}$ expression, hypercharges and Layer-1
  derivations.
- **"selected by the"** has 16 surviving uses, none of them the QM-selector claim. Complexity :27 says "the dynamics selected by the
  framework's additional structural requirements determines the Standard Model's complete structure". That is a different claim, and it
  is listed below as a follow-up. The other 15 concern other selections: GR :202, Main :576, Methodology :503, SM :60 and :1398,
  Substratum :22 and :203, preface :7, ch04 :192, ch10 :28, ch19 :222, and FULL :78, :1311, :2850 and :5382.
- **"maximum propagation speed"** has 1 surviving use, SM :240. It is the retraction itself.
- **"therefore requires ontic parameter dependence"** has 2 surviving uses, Main :558 and :766. Both are Main-side sites: :558
  scopes it to the adopted branch, and :766 is in the compressed-summary list above.
- **"written into the hidden sector"** has 4 surviving uses, ch01 :217, ch02 :20 and FULL. All concern (C2) persistence.
- **New text:** "encoding of the correlations" and "not a record written at preparation" have 3 uses each, in Explainer :709,
  ch03 :186 and FULL :1062.

The Introduction (`papers/Introduction.md` on `draft/oi-introductory-paper-20261025` at `bace5ef8`, read only) states the Bell
ceiling with all four hypotheses and ±1 in every run (§3.5). It states the either/or, ontic parameter dependence and H-Bell
(§3.5 and the conditional-interpretations paragraph). It makes no pre-setting-record, selector or center-independence claim.

Follow-ups outside this unit, in the same selector class, for #946:

- **Substratum :48.** "the unique second-order reversible nearest-neighbor dynamics compatible with center independence, isotropy, and
  linearity" leaves out the coefficient α.
- **Substratum :159 and :323.** These say "uniquely select" and "uniquely selected".
- **SM :110.** It says "the dynamics selection theorem applies at each step".
- **SM :291.** This is the line number from the review. On this tree, the "wave-equation uniqueness (§4.1)" sentence is at :296.
- **Complexity :27.** It says "the dynamics selected by the framework's additional structural requirements determines the Standard
  Model's complete structure".

Regenerated: Explainer and the book (`.tex` and `.pdf`).
