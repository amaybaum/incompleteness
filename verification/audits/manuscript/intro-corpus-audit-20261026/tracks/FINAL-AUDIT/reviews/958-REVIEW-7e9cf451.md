## PR #958 review, head 7e9cf451 vs base 55e3217b

**Verdict: BLOCK.** The blockers are narrow and small. Most hunks are correct, and several fix real errors at base:
- C3 is no longer made conditional on mixing.
- The C2/C3 framing of "approximately frozen" is corrected.
- Bidirectionality is no longer attributed to C1.
- "ETH-conditional C2 bound" is replaced.
- "ETH holds" becomes "standard assumption".

Three problems remain:
- One rewritten sentence still asserts something stronger than its support (Substratum :137).
- The same section leaves a paragraph that contradicts the new text (Substratum :135).
- The new Substratum :129 states the slow-bath form in its weaker, benchmark currency. It also leaves out the strongest result the corpus proves without a hypothesis.

With findings 1–3 fixed, I would accept.

**Setup.** I used a detached worktree at 7e9cf451 with 23 GB free; it has now been removed. Anchors checked at base:
- Main §1.3 (:76, the C2-structural and C2-slow definitions).
- §3.4 (:439–:457, :490–:510).
- The status-table row Main :736.
- `OIBridge/C3Necessity.lean` (`c3_necessity`, `card_hidden_ge_two_pow_Istar`, `c3_necessity_and_capacity`; `Realization.step : V × H ≃ V × H`).

### Findings

**1. Required (overclaim).** papers/Substratum.md:137
- Current text: "every realization of the resulting dynamics satisfies … C2 …, C2 in its persistence form without further hypothesis and in its slow-bath form conditional on the hidden-sector mixing hypothesis".
- Problem: "Satisfies C2 in its slow-bath form" means τ_S ≪ τ_B is forced. Under the mixing hypothesis the proved result is weaker: ε_min(I*, n_V) lower-bounds the relaxation residue at the coupling time, and hence the bath's conditional mixing time.
  - Main §1.3 :76 calls this "a lower bound on bath persistence".
  - Main §3.4 Remark "(C2)'s role" says "it lower-bounds the bath's mixing time".
  - Nothing proves the ≪ separation. This is the "τ_S ≪ τ_B forced" claim, still present in an edited line.
- Strength problem in the same sentence: it omits that C2-structural holds by reversibility in every bijective realization (Main :76; Theorem statement (2); :736).
- Proposed replacement: "The necessity analysis of [Main §3.4] establishes, for every faithful realization of the resulting dynamics, C3 (the data-processing bound $\log_2|\mathcal{C}_H| \geq I^*$, with no mixing hypothesis) and (C2-structural) (retention of the record of visible history to its readback, supplied by reversibility); in the coupling-step model of [Main §3.4], observed conditional memory keeps some realized hidden conditional at least $\varepsilon_{\min}(I^*, n_V)$ from the reference prior at the coupling time (C2's persistence form, with no mixing hypothesis), and under the hidden-sector mixing hypothesis ([Main §3.4]; ETH its physical motivation) this lower-bounds the bath's conditional mixing time (the slow-bath form)."
- The C3 clause in the PR is correct: the Lean `c3_necessity` uses only determinism and data processing, with no mixing hypothesis. Optionally add the kernel citation.

**2. Required (stale contradicting site, §A.25).** papers/Substratum.md:135, not edited by the PR.
- Current text: "the conditional attaches only to the *necessity* direction of C2 … ETH is required for the necessity direction … A referee skeptical of ETH may therefore read the reconstruction's uniqueness as holding within the class of ETH-satisfying (equivalently, non-integrable, non-MBL) hidden sectors".
- Problem: this now contradicts :129, which says the persistence form holds without any hypothesis. It also contradicts Main's Remark (role of ETH) at ~:494, which says the slow-bath form rests on the mixing hypothesis, "not on ETH itself", and that "a hidden sector failing ETH but satisfying the mixing bound still delivers the necessity direction".
- Other problems in the paragraph:
  - "equivalently, non-integrable, non-MBL" is an unsupported equivalence.
  - "A referee … may therefore read" is reader-instruction (§A.32).
- Proposed replacement: "Second, the conditional attaches only to the slow-bath (timescale) form of C2's necessity direction; C2's persistence form and the sufficiency direction — C1–C4 realization yields the memory-bearing non-Markovian phenomenology, whose finite law universally admits the quantum representation — are unconditional, so the framework's positive predictive content does not rest on ETH. The mixing hypothesis, for which ETH is the physical case, is used only to convert observed memory into a lower bound on the bath's conditional mixing time; the reconstruction's uses of that form hold within the class of hidden sectors satisfying the mixing hypothesis, which by the argument above includes generic interacting hidden sectors at $d = 3$."

**3. Required (strength, scope and currency).** papers/Substratum.md:129
- Current text: "C2 takes the two forms of [Main §1.3]. Its persistence form holds without further hypothesis: observed conditional memory places some realized hidden conditional … at least $\varepsilon_{\min}$ … Its slow-bath form is conditional on the quantitative mixing hypothesis … under which the departure from the homogeneous Markov benchmark obeys … $(k-1)\varepsilon$, so that a departure $\delta$ forces $\varepsilon \geq \delta/(k-1)$; without it, accessible conditional memory does not bound the bath's mixing time."
- What is right:
  - "ε ≥ δ/(k−1)" follows verbatim from Main's theorem at :453.
  - No τ_S ≪ τ_B forcing remains.
  - "Observable P-indivisibility requires τ_S ≲ τ_B" is gone.
- Problem (a), naming: Main §1.3's two named forms are C2-structural and C2-slow. The ε_min statement is the persistence form of the *necessity theorem* (§3.4). The hunk conflates the two.
- Problem (b), omitted result: the strongest unconditional result is left out — C2-structural holds by reversibility in every bijective realization (Main :76, :736).
- Problem (c), scope: the anchor (:736) scopes the persistence form "in the coupling-step model of §3.4"; the hunk drops that.
- Problem (d), currency: the slow-bath consequence is stated only in benchmark currency, then followed by a sentence about conditional memory.
  - Main says the benchmark bound "is blind to conditional memory" (:457 Remark).
  - Main says "the operative contrapositive in condition (ii)'s currency is the physical-memory theorem's ε ≥ ε_min(I*, n_V)" (:453, :492).
- Proposed replacement: "C2 takes the two forms of [Main §1.3]. (C2-structural), retention of the record of visible history to its readback, holds by reversibility in every bijective realization. C2's necessity holds in its persistence form without further hypothesis: in the coupling-step model of [Main §3.4], observed conditional memory $I^* > 0$ places some realized hidden conditional at the coupling time at least $\varepsilon_{\min}(I^*, n_V)$ from its reference prior (the physical-memory theorem). Its slow-bath form is conditional on the quantitative mixing hypothesis of [Main §3.4] — uniform total-variation closeness of the hidden sector's post-relaxation conditionals to a single bath distribution — under which the same bound makes $\varepsilon_{\min}(I^*, n_V)$ a lower bound on the relaxation residue at the coupling time, hence on the bath's conditional mixing time, and a departure $\delta$ from the homogeneous Markov benchmark at step order $k$ forces $\varepsilon \geq \delta/(k-1)$ (the bound $\|T^{(k)} - T^k\|_{\mathrm{TV}} \leq (k-1)\varepsilon$, constant optimal); without it, accessible conditional memory does not bound the bath's mixing time."

**4. Optional (strength).** book/glossary.md:27 and FULL:6627
- The PR changed only the title, to "C2 (Memory persistence)", which matches Main §1.3.
- Problem: the defining sentence still states C2-slow's criterion ("coarse-grained mixing time exceed the accessible window") and then says "fast conserved dynamics serve equally". Main §1.3 says that for the shift-register bath (C2-slow) fails while (C4) holds. The two named forms are never given.
- Proposed opening: "Stated in two forms ([Main §1.3]): (C2-structural), that a hidden record of visible history persists to the readback that uses it — supplied by reversibility in every bijective realization, so as a condition it bears on coarse-grained descriptions of the hidden sector; and (C2-slow), $\tau_S \ll \tau_B$, one sufficient mechanism, fast conserved dynamics being another (`fastbath_probes.py`)." Keep the rest of the entry. Mirror the change into FULL.

**5. Optional (strength).** papers/GR.md:20; also GR:565
- Current text: "C2 lying outside that equivalence and the slow-bath form of its necessity … conditional on the hidden-sector mixing hypothesis".
- Problem: the unconditional persistence form is omitted.
- Proposed: append ", its persistence form holding without it". This matches Substratum:112 and ch02:90.

**6. Optional (missed related sites carrying the unsupported τ claim).** None is in an edited line.
- Main.md:439: "observable P-indivisibility in an ETH hidden sector requires $\tau_S \ll \tau_B$".
- Main.md:447: "observable P-indivisibility requires $\tau_S \lesssim \tau_B$"; and "For the strong, persistent memory … the separation must be $\tau_S \ll \tau_B$".
- Explainer.md:357: "P-indivisibility requires τ_S ≪ τ_B".
- Main's own remark (:455) says the mixing bound is "not itself a measure of P-indivisibility". :439 (≪) and :447 (≲) are also inconsistent with each other.
- Proposed (Main :447 / Explainer :357): "within the mixing class, observed conditional memory $I^* > 0$ requires that the hidden conditionals not have relaxed to within $\varepsilon_{\min}(I^*, n_V)$ of the reference prior by the coupling time" (the physical-memory theorem's timescale form). Drop the "must be τ_S ≪ τ_B" sentence, or label it as motivation.
- Separately, SM.md:296 says "the ETH-conditioning of the slow-bath form". The slow-bath form is conditioned on the mixing hypothesis, which ETH motivates. Proposed: "the mixing hypothesis (ETH-motivated) conditioning the slow-bath form".

**7. Optional (physics nuance).** Main.md:336, appendix-b:98, FULL:5865
- Change: "(conditions (C2)–(C3))" becomes "(the slow-bath regime, (C2-slow))".
- This is correct: C3 as defined (log|C_H| ≥ I*) does not make the bath frozen.
- If the old C3 reference meant the bath's imperturbability, that belongs to the N_H ≫ N_V realization clause (Main :78). It can be cited as such: "(the slow-bath regime, (C2-slow), with the bath imperturbable under the $N_H \gg N_V$ hierarchy)".
- Nit: the parentheses differ between Main "((C2-slow))" and the book "C2-slow".

**8. Confirmed correct, no change needed.**
- **Main :99:** "(C2): persistence form without a mixing hypothesis, slow-bath form conditional on it" matches the physical-memory theorem (~:457).
- **Main :109:** "(C2-slow) inverts this" is right, and so is separating C1 (hidden → visible influence) from the bidirectional slow-bath mechanism; §1.3 and the influence Remark (:436) support it.
- **Main :652, content check:**
  - "has narrowed as the internal results grew" → "is load-bearing only where the internal results stop", consistent with the paragraph's "and nothing else".
  - "A referee … should direct that skepticism … specifically; … no longer route" → "Skepticism … therefore bears on … only; … do not route". Content preserved; the reader-instruction and history voice are removed.
  - A third change in this paragraph is a claim change, not voice: "ETH-conditional C2 bound" → "C2 physical-memory bound (persistence form without a mixing hypothesis; slow-bath form conditional on the mixing hypothesis, which ETH motivates)". It is correct and strengthens the text in line with Main §3.4.
- **GR :20 and ch07 :32 / FULL:1911:** "holds for" → "is the standard assumption for" matches Main Remark (Status of ETH). This is a justified weakening, since ETH is a conjecture.
- **C3 hypotheses:** C3 is stated without the mixing hypothesis at every edited site. That is correct: the Lean `c3_necessity` uses only the deterministic step and data processing.
- **Hypotheses moved between theorems:** none.

### Checks
- **Mirrors:** glossary:27 = FULL:6627, ch07:32 = FULL:1911 and appendix-b:98 = FULL:5865, all byte-identical. `mirror_check` reports 0 lines absent.
- **Voice:** the added lines have no history voice ("now", "no longer", "formerly", …) and no mid-sentence caps; `voice_check` passes.
- **Generated files:**
  - The source-sha256 stamp in each .tex matches its .md for Main, Substratum, GR and the book.
  - Page counts are unchanged from base: Main 96, Substratum 53, GR 87; the book is 557.
  - `sh ./build.sh Main` gave 96 pages, no dropped glyphs, a .tex byte-identical to the committed file, and PDF text identical to the committed file. The rebuilt PDF was reverted.
- **Local release gate:** every step passes except `lean-axioms` (no lake locally, as expected). That includes staleness, voice, claims, mirror, lean-manuscript, legacy-records, v3-self-test, v3-corpus and v3-receipts.