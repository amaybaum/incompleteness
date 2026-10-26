# Independent review of R11/R12 FINDINGS.md

This review covers `r11/FINDINGS.md`, read against `main` at `687e885b` (worktree `mainwt`). It is
read-only: no repository file was changed. My own probes are in `r11/rev/`:

- `evap.py`: τ_evap against τ_B^D.
- `page.py`: Page's exact mean entropy plus a Haar Monte Carlo.
- `r12.py`: an ODE integration of the Page-time fraction.
- `rep/`: fresh BH-01 and BH-02 replays from the main blobs.

## 0. Checks I re-ran

| Check | Result |
|---|---|
| The 11 quoted lines at 687e885b | All verbatim, at the stated line numbers |
| The 9 book↔FULL mirror pairs (ch07:110/1987, :126/2003, :159/2036, :161/2038, ch18:130/4950, :146/4966, :148/4968, :158/4978, ch19:334/5510) | Byte-identical (shell string equality) |
| BH-01 replay (a full copy of the directory from main, including `review/`) | `result.json` byte-identical (52 s); `SHA256SUMS` all OK |
| BH-02 replay | `checks.py` stdout is identical to `result.json` (30 s); `SHA256SUMS` all OK |
| **FINDINGS "BH-01 … SHA256SUMS passes"** | **Only partly true.** `r11/replay-bh01/` has no `review/` subdirectory, so 6 of the listed entries fail to open there. My full replay passes. Process note only; no verdict depends on it. |
| GR:811 arithmetic (my own code, GR's α with Γ=1, 30 M☉) | t_evap = 1.79×10⁷⁹ s. Against τ_B^D = 10¹⁷ s the ratio is 1.8×10⁶²; against 1/H = 4.6×10¹⁷ s it is 3.9×10⁶¹. t_P/τ_B^D ≈ 1.2×10⁶². Crossover mass (Γ=1, τ=10¹⁷ s) is 1.06×10¹¹ kg. This agrees with the investigator's and BH-01's conservative interval of [1.785×10⁵⁷, 1.786×10⁶⁵], whose Γ runs over [10⁻², 10³] and τ over [10¹⁶, 10¹⁹] s. |
| Page mean (exact rationals) | S(2,2) = 1/3, confirmed by Monte Carlo (0.3329±0.0009). At m=n the deficit ln m − S is 0.360, 0.436, 0.464, 0.491, 0.498, 0.4994, 0.49986 for m = 2, 3, 4, 8, 16, 32, 64, so it tends to ½. At fixed m it is ≈ (m²−1)/(2mn), polynomial in n (m/(2n) is only the large-m form, a slip in FINDINGS A.2 that does not affect the conclusion). The Monte Carlo standard deviation falls ≈ ×2 per doubling of m, which is concentration. |
| R12 | t_P/t_evap = 1 − 2^{−(3+p)/2} for α∝M^{−p}, β=1. Exact derivation: M^{3+p} is linear in t and the turnover is at M₀/√2. Simpson integration of the ODE agrees to 8 digits at p = 0, ½, 1, 2 (0.64644661, 0.70269822, 0.75, 0.82322330). |
| Provenance claim in proposal 8 / A.9 ("ch07:147 was already corrected in the same commit 6adfff0e") | **Wrong.** `git log -S` shows that ch07:147 dropped "only … no ergodicity assumption" and gained H-scramble in **3fe27778 (2026-08-23)**. 6adfff0e (2026-10-25) only scoped the Penington citation in both files. GR:869 has lagged the book since 2026-08-23. This affects only the change note, not the verdict. |
| ch18:130 (8cada745, 2026-10-16) and ch18:146/:158 (334eef0a, 2026-05-14) dates | Confirmed |

## 1. Per-site verdicts

| # | Site | FINDINGS verdict | Review | Reason |
|---|---|---|---|---|
| 1 | ch07:110 / 1987 | SITE-ERROR | **CONFIRMED** | Read adversarially, the colon does scope "at the structural level" to conservation, so this is not a contradiction (FINDINGS §B agrees). But "resolves the paradox" refers to the paradox as defined at :112, which asks whether the *radiation* carries the information. Bijectivity is an imported premise (Main:66, ch01:41) and allows the information to end in D (BH-01 claim A, which also follows from a one-line example: a bijection that never moves the message out of an unread register). So the sentence claims more than its support. The proposed wording is acceptable: it reuses ch19:72's status phrase and ch07:157's sentence. Optional alternative in §2. |
| 2a | ch07:126 s1 | SITE-ERROR | **CONFIRMED** (mild) | The milder reading "runs through" = "the route passes through the cycle decomposition" is literally true. However, the italic *combinatorial* together with "rather than through the gravitational path integral" assigns the source of the result. GR:831 itself states that "finite bijectivity, energy conservation and uniform cycle counting together do not give Page typicality". BH-02 C6(b): the value enters through H-scramble's Haar ensemble. The proposed replacement is accurate and adds no assumption. |
| 2b | ch07:126 s2 | SITE-ERROR | **CONFIRMED WITH CHANGES** | The verdict holds. The mean deficit tends to ½ nat at equal dimensions and is polynomial in the larger dimension. The only reading that survives is "exponential in the larger subsystem's *mode count* at fixed smaller subsystem", and it fails at the turnover, which is the point the Page curve needs. **The replacement misattributes:** Popescu–Short–Winter bound the *trace distance of the reduced state from the canonical state*, with deviation probability ≤ 2exp(−C d_R ε²). They do not state Page's mean. Page's mean is Page (1993), and entropy concentration about it is Lévy's lemma as in Hayden–Leung–Winter (2006). The replacement's "in the dimension" is also ambiguous. Corrected wording in §2. |
| 3 | ch07:159–161 / 2036–2038 | SITE-ERROR | **CONFIRMED WITH CHANGES** | As written, the falsifier's example excludes no outcome. Bijectivity together with any unread sector reproduces any deficit (claim A), and nested-trace consistency is a Fubini/partial-trace identity that holds for every map (claim E; GR:739, :747). The replacement's "a remnant" could be read as admitting remnants into OI's own model, whose GR A.7 trajectory evaporates completely, so I drop it. I take no position on a new falsifier (O-4). Wording in §2. |
| 4 | ch18:130 / 4950 | CONSISTENT | **CONFIRMED** | The same line scopes "the same structural resolution" ("framework-level interpretations and conditional results … the Page curve conditional"), and it matches ch19:30. |
| 5 | ch18:146 / 4966 | SITE-ERROR | **CONFIRMED WITH CHANGES** | The verdict holds: GR A.1–A.4 are consistency identities with no recovery content, and the Page curve is stated unconditionally. **The replacement's last clause, "the Page curve at the emergent level follows under the scrambling condition H-scramble", repeats a sufficiency overclaim.** Under item F, A.8–A.9 also need D decoupled over the evaporation, and A.9 rests on an unproved step from time average to pointwise value (§4 below). Use a form that holds whatever condition list is settled. Wording in §2. |
| 6 | ch18:158 / 4978 | SITE-ERROR | **CONFIRMED WITH CHANGES** | Both readings of "(which it does, through the nested partition)" are unsupported (claim E), and the parenthetical also undercuts the sentence's own "as if" framing. The replacement is correct but awkward; tightened in §2. |
| 7 | ch19:334 / 5510 | SITE-ERROR | **CONFIRMED** | "Resolved (Page curve from typicality)" contradicts ch19:72, ch09:127 and appendix-a G11 ("C", "Scrambling condition open"). The parenthetical names the Page curve as the means, which excludes the preservation-only reading. "Conditional (H-scramble)" fits the table's register (cf. "Conditional ($a_0 = cH/6$)"), but it becomes an incomplete list once O-1 is applied. I recommend "Preserved; Page curve conditional", which mirrors ch19:72 and ch09:127 and holds under any O-1 outcome. The choice is O-6. |
| 8 | GR:811 | SITE-ERROR (false inequality) | **CONFIRMED WITH CHANGES** | Independently confirmed. At GR's own values the ratio τ_evap/τ_B^D ≈ 10⁶² and is ≥ 10⁵⁷ over the full assumed intervals; the inequality is reversed by ≳ 57 orders. The book itself (ch07:159) says astrophysical evaporation times "vastly exceed the age of the universe" (≈ 1/H). My corpus search finds no other decoupling argument (§3). The replacement needs three fixes. (i) "Theorem A.7 therefore holds on t ≪ τ_B^D" overclaims: A.7 states an error O(τ_S/τ_B^D), whereas A.5(i) supplies O(t/τ_B^D) (BH-01 assumption watch). Its proof also passes from a pure \|ψ_VB⟩ to a pure ρ_BR with R ⊊ V, which needs V∖R unentangled with B∪R and is not argued (new, §3 M6). Say "is stated for". (ii) "τ_evap ≫ τ_B^D for every black hole heavier than about 5×10¹² kg" is false at its own threshold, where worst-case parameters give τ_evap ≈ τ_B^D. Use ">" or GR's central values. (iii) The citation should be A.5's step (i) (GR:769), because Theorem A.5 as a whole also needs t ≪ τ_B^B ~ 10⁻³ s. Wording in §2. |
| 9 | GR:869 | SITE-ERROR | **CONFIRMED WITH CHANGES** | "Invokes only Popescu-Short-Winter" contradicts the theorem's own label (GR:817) and GR:831–833. "No ergodicity assumption" is true only in the narrow classical sense; H-scramble is *stronger* than ergodicity (a quantum equidistribution or design condition), so the phrase misleads. The replacement is correct. Fix the provenance in the change note to **3fe27778**, not 6adfff0e. The last sentence cannot simply be kept: it cites undefined "horizon-factorization hypotheses" (O-5), and after GR:811 is corrected it must carry the decoupling condition (O-1). Wording in §2. |
| 10 | ch18:148 / 4968 (R12) | SITE-ERROR (conditions level) | **CONFIRMED** (non-blocking) | The formula is verified exactly and by ODE. Scale note: physically, α varies with M only through species thresholds, so for M₀ ≫ M_* the fraction differs from 0.646 by O((M_*/M₀)³), negligible for astrophysical holes. The condition matters for masses near thresholds. p=½ is an illustrative toy model, not a physical value. The replacement is correct. |

**§C.4 (GR:841–847, Thm A.9 "direct substitution"). I reclassify it from UNDETERMINED to SITE-ERROR
(proof scope, claim stronger than its proof).**
- **What A.8 proves.** Under H-scramble, the *full-cycle time average* of S(ρ_R) at a *fixed* bipartition
  (d_B, d_R) equals S_Page (GR:825–839). The cycles have lengths up to |Σ_E| ~ e^{e^{10⁷⁷}}, far longer than
  t_evap.
- **What substitution yields.** Substituting d_B = q^{n_B(t)} into A.8 gives "the cycle average at the frozen
  bipartition of stage t equals S_Page". It does not give S_rad(t), the instantaneous entropy along one
  trajectory with a moving bipartition from a definite initial state. That trajectory starts at S = 0 (BH-02 C1).
- **The symptom is already in A.8.** Its statement defines d_B = |C_B(t)| inside a time-averaged theorem.
- **The error is settled; only the repair is a choice.** Either (a) restate A.9 as the curve of A.8's cycle
  averages at the stage-t bipartition, which needs no new assumption, and state that the pointwise reading is
  open (as the Introduction r2:205 already does); or (b) keep the pointwise statement and add a named
  pointwise-typicality hypothesis, which is a new assumption and so the owner's decision. Until one is chosen,
  "Proof. Direct substitution" presents an open step as proved.

## 2. Corrected wording (where I change a proposal)

**ch07:110 (optional alternative to the accepted proposal)**
- Sentence 3: "The framework's answer separates two questions. Information is never lost from the substratum
  bijection $\varphi$, because $\varphi$ is bijective — the premise of information conservation the framework
  shares with standard physics (Chapter 1). How much of that information an observer can recover from the
  radiation is a separate question, which bijectivity alone does not settle; the Page-curve derivation below
  addresses it under its own conditions."
- Sentence 4 is kept.
- The proposal as written is also acceptable. It repeats ch07:157's closing sentence almost verbatim.

**ch07:126 sentence 2** (replaces "The relevant result is … larger subsystem.")
> The relevant results are Page's mean entropy and measure concentration (Popescu-Short-Winter): for a bipartite
> quantum system in a Haar-random pure state, the entanglement entropy of the smaller subsystem lies close to
> Page's mean, about $\ln d_{\min} - d_{\min}/(2d_{\max})$ — within half a nat of the maximum $\ln d_{\min}$ when
> the two dimensions are equal, and closer as the larger one grows — with deviations from that mean exponentially
> unlikely in the dimension of the smaller subsystem.

- "Exponentially unlikely in d_min" matches GR:829's bound e^{−c d_min ε²} and is implied by the stronger
  total-dimension bound.
- The book bibliography has no entry for either Popescu–Short–Winter 2006 or Page 1993. Both are needed (M8).

**ch07:132** (the "exponentially small" family, FINDINGS C.1/D.3)
> … dimension $q$, with a correction of at most about half a nat, reached at the turnover and exponentially small
> in $|n_R(t) - n_B(t)|$ away from it.

**GR:611**
- Replace "plus exponentially small corrections" with "up to a correction of at most $\tfrac12$, reached at
  $n_R = n_B$ and exponentially small in $|n_R - n_B|$ away from it (Theorem A.9)".
- For the attribution clause, use FINDINGS D.2's text. Splice it so that the existing "conditional on … H-scramble
  … which is not established there" is not duplicated:
  > — from Popescu-Short-Winter typicality [29] carried to the orbit by the scrambling condition H-scramble of
  > Appendix A, which is not established there (uniformity over classical microstates is not uniformity over
  > quantum pure states), the cycle decomposition on the finite energy shell supplying exact time averages.

**ch07:159–161**
- 159: "The framework's resolution" → "The framework's account" (as proposed).
- 161, sentences 1–2:
  > Bijective dynamics is compatible with radiation that carries less information than the matter that formed it,
  > the remainder being held in sectors the observer does not read, and the nested trace-out is consistent for
  > every dynamics; a measurement of the radiation alone therefore does not test the conservation claim, which
  > rests on bijectivity as a premise (Chapter 1). The QES + islands computations, which obtain a unitary Page
  > curve from semiclassical gravity by an independent route, support unitary evaporation without depending on
  > the framework.

  The rest of 161 is unchanged.

**ch18:146**
> **The second dissolution: the black hole information paradox.** Chapter 7 §7.6 developed the framework's
> account of the information paradox. Information is never lost from the substratum bijection $\varphi$ because
> $\varphi$ is bijective; whether the radiation carries it is a separate question, which bijectivity alone does
> not settle. The apparent information loss in Hawking radiation is an artifact of the trace-out — the same
> mechanism that produced the cosmological constant dissolution. The framework's nested-partition formalism (two
> coexisting causal boundaries: cosmological horizon plus black hole horizon) provides a self-consistent emergent
> quantum description when the two boundaries coexist; the Page curve at the emergent level is a conditional
> result (Chapter 7 §7.6).

**ch18:158 parenthetical**
> (the substratum preserves it, by bijectivity; whether the radiation carries it is the separate question of
> Chapter 7 §7.6)

**ch19:334 cell (O-6):** "Preserved; Page curve conditional". "Conditional (H-scramble)" is acceptable only if
O-1 leaves the H-scramble-only label standing.

**GR:811**
> Step (i) of Theorem A.5 freezes $D$ only on timescales $t \ll \tau_B^D$, with $\tau_B^D \sim 1/H \sim 10^{17}$ s
> (§A.5). The evaporation is far longer: the trajectory below gives $t_{\text{evap}} \sim 10^{79}$ s for a
> $30 M_\odot$ black hole at $\Gamma \sim 1$, so $t_{\text{evap}}/\tau_B^D \sim 10^{62}$, and
> $t_{\text{evap}} > \tau_B^D$ for every black hole heavier than about $10^{11}$ kg. Theorem A.7 is stated for
> $t \ll \tau_B^D$; applying it at the Page time and over the evaporation, as Theorems A.8–A.9 do, assumes in
> addition that $D$ stays decoupled from $B \cup R$ over the evaporation, which timescale ordering does not supply.

- If the conservative form is preferred: "$t_{\text{evap}}/\tau_B^D > 10^{57}$ at $30 M_\odot$ for any
  $\Gamma \in [10^{-2}, 10^{3}]$ and $\tau_B^D \le 10^{19}$ s".
- Do not write "≫ … above 5×10¹² kg".

**GR:869**
- Accept the FINDINGS replacement for sentence 1.
- Last sentence:
  > What the present derivation establishes — under H-scramble, with $D$ decoupled from $B \cup R$ over the
  > evaporation, at the G1 register — is that a cycle-averaged Page curve with turnover at $d_R = d_B$ is
  > reproducible from a finite deterministic substratum without invoking the replica machinery.
- "Cycle-averaged" follows §C.4 repair (a). Adjust it if the owner takes repair (b). The undefined
  "horizon-factorization hypotheses" is removed (O-5).

## 3. Missed sites and further observations

**Decoupling-argument search (task 3).** I grepped the whole corpus for decoupl, frozen, trans-cosmological,
deep sector, evaporat and τ_B^D. What exists:
- the boundary-only lemma, GR:118–120, which holds at O(t/τ_B) for t ≪ 1/Δ_D ≤ τ_B;
- Substratum:256 and :280, which cover only a deep sector coupled at no order and explicitly limit a slowly
  coupled one to O(t/τ_B);
- Explainer:445/:1055, restatements of the lemma;
- ch01:227, about record persistence rather than decoupling.

No other argument supports decoupling over the evaporation. FINDINGS' corpus claim is confirmed. BH-01 itself
correctly says only that item F does not *exclude* one, and the manuscript replacement correctly asserts nothing
stronger.

**Missed sites**

| ID | Site | Problem |
|---|---|---|
| M1 | GR:605 | "the nested formalism … shows … that the Page curve follows under the scrambling condition H-scramble". This attributes the Page curve to the nested formalism (claim E) and is sufficiency-form (D.2 and D.5). It is absent from every FINDINGS list. |
| M2 | book/README.md:64 (no FULL mirror) | "the Page curve from nested trace-out, conditional on … H-scramble". The D.2 family (claim E). Absent. |
| M3 | ch07:149 / 2026 | "under H-scramble, a Page curve … is reproducible …; the scrambling condition and the radiation's entropy per boundary mode lost are the open steps". An *exhaustive* list of open steps that omits D-decoupling (item F), the A.8→A.9 step (§C.4) and shell factorization (BH-02 C6(c)). FINDINGS lists it only under "if O-1"; the correction is mandatory (see O-1). |
| M4 | ch07:116 / 1993 | "Under that condition the two derivations give a Page curve of the same form". Sufficiency-form, so the same as M3. FINDINGS lists it as Keep. |
| M5 | GR:717 | "deriving the Page curve under the scrambling condition H-scramble". Sufficiency-form. FINDINGS lists it as Keep; it needs the same treatment as GR:841. |
| M6 | GR:813–815, Thm A.7 (new observation, not in BH-01 or BH-02) | Beyond the error-term mismatch BH-01 noted, the proof's step "Restricting to the B ∪ R subsystem (where R ⊂ V): ρ_BR ≈ \|ψ⟩⟨ψ\| is pure" is a non sequitur. A pure state on V⊗B restricts to a mixed state on B⊗R unless V∖R is unentangled with B∪R. This is a second implicit decoupling assumption. Record it as an assumption-watch marker. It is why "Theorem A.7 therefore holds" must not appear in the GR:811 replacement. |
| M7 | GR:829 | "By Popescu-Short-Winter [29], the set of atypical states — those with \|S − S_Page\| > ε — has measure at most e^{−c d_min ε²}". [29] bounds trace distance, not entropy about Page's mean; the entropy statement is Lévy's lemma (Hayden–Leung–Winter 2006), which implies the stated bound. Citation accuracy only; low severity. |
| M8 | book/bibliography.md | No entries for Popescu–Short–Winter (2006) or Page (1993), although ch07:114 and :126 cite them. Low severity. |
| M9 | ch18:156 / 4976 | "removes the non-renormalizability problem at the level of interpretation … as the two-level description does for the cosmological constant and information paradox problems". This is a D.1-family paraphrase (the two-level description does not settle recovery). Add it to D.1. |
| M10 | ch07:130 / 2007 | "typical … applied to the bijection's cycle structure, which is what H-scramble supplies", followed by an instantaneous S_rad(t). This is both the attribution in ch07:126 s1 and the pointwise reading of §C.4. Propagate it with those. |
| M11 | Count check | ch19:370 "joint explanation of ten disparate hard problems" and the heading "19.2 Problems resolved". The heading is already broad (ch19:10). Recheck the "ten" after the ch19:334 change (§A.30 count rule); it is probably unaffected. |
| M12 | §C.5 and BH-01's coupling-chain note | GR A.5 / §3.2's chain V↔B↔D uses B for the boundary layer, while Appendix A's B is the black-hole interior, where spatial locality gives B↔V↔D. BH-01 records this; FINDINGS §C omits it. Record only. |

**Spot-check of the §D propagation lists**
- D.6's count "5 book + 5 FULL" is right for the literal patterns "mass-independent" and "independent of mass".
- ch07:139 ("independent of the black hole's mass") is a sixth hit for a wider pattern. It is a correct keep,
  scoped by :137.
- D.1 and D.2 otherwise check out, with the additions M1, M2, M4, M5, M9 and M10.

## 4. Owner decisions O-1 to O-6

- **O-1. Partly settled by the evidence.**
  - *Settled.* Once GR:811 states that A.8–A.9 assume D decoupled over the evaporation, every **sufficiency-form**
    statement ("under H-scramble, X follows/is established"; "Theorem A.9 (conditional on A.8, hence on
    H-scramble)") turns a two-condition result into a one-condition one. That is conditional → stronger
    (claim/evidence rule), and it contradicts the corrected GR:811 within the same paper. These must carry the
    condition:
    - GR:841, GR:717, GR:605, GR:611, GR:869 (last sentence);
    - ch07:116, ch07:149, ch19:72;
    - the replacement text for ch18:146, as worded in §2.
  - *Owner's choice.* Whether to give the condition an H-label, and how to word it in **necessity-form** mentions
    ("requires H-scramble": ch07:126 s3, :288, appendix-a:103) and in two-word status cells (G11, ch09:127,
    ch19:334).
  - *No new physical assumption.* Naming the condition makes explicit an assumption A.8–A.9 already use. It
    introduces nothing new, and it is the opposite of silent.
- **O-2. Fact settled; extension is the owner's.**
  - *Settled.* In the configuration factorization from a definite configuration, *every* bijection visits only
    product states. This is a one-line proof (BH-02 C1/C6(a)), and GR:831 shows it already for one long cycle. So
    ch07:126 s3's "can" understates the case, though the sentence is not false.
  - *Owner's.* Stating that H-scramble needs a superposed initial state or a non-aligned factorization means
    choosing which ingredient the framework adopts, which is a physical-modelling choice. Note that BH-02 C3 shows
    permutations *can* produce Page-like states from a supplied superposition, so ch07:151/GR:871 ("it can be
    combinatorial") is not refuted, only incomplete ("on the substratum side" fails once the superposition is
    supplied).
- **O-3. Genuinely the owner's**, but the change must not leave both accounts unscoped. A minimal, evidence-safe
  scoping of ch18:150: "inaccessible at the emergent level while it resides in the sectors the emergent
  description traces out".
- **O-4. Genuinely the owner's.** A new falsifier would be a new claim. Removing the empty one is settled.
- **O-5. Removal settled, definition the owner's.** An undefined term a reader cannot resolve violates the
  manuscript-voice rule (§A.27). The safe fix replaces it with the conditions actually used (§2, GR:869).
  Defining a new "horizon-factorization" hypothesis would be a new assumption.
- **O-6. Genuinely the owner's (register).** The choice must hold under O-1; see §2.

## 5. Overall verdict

- **The findings are substantively correct.** All nine SITE-ERROR verdicts are confirmed, and the CONSISTENT
  verdict at ch18:130 is confirmed. GR:811 is independently confirmed as false, by ~62 orders at GR's own
  values and ≥ 57 orders over the full conservative intervals. The ch07:126 s2 and R12 mathematics are
  independently confirmed. Each error is established independently of BH-01/BH-02's unadopted status: by
  arithmetic, by the manuscripts' own text, or by one-line proofs.
- **The proposals are not ready to apply verbatim.** Required changes:
  - the ch07:126 s2 attribution and dimension wording;
  - ch18:146's "follows under H-scramble";
  - in GR:811, "Theorem A.7 therefore holds" and "≫ above 5×10¹² kg";
  - the last sentence of GR:869;
  - dropping "a remnant" at ch07:161.
- **§C.4 is a site error (proof scope), not undetermined.** Only its remedy is a choice.
- **O-1 is mandatory for sufficiency-form statements.**
- **Process fixes in the change record:** the 6adfff0e attribution (it should be 3fe27778), the incomplete BH-01
  replay directory, and the (m²−1)/(2mn) asymptotic.
- **Add the missed sites M1–M5, M9 and M10 to the propagation lists**, and record M6 as an assumption-watch
  marker.
- With these changes the correction set fits one separate, reviewed manuscript-consistency change. It must not
  claim full OI–QM equivalence, and it introduces no physical assumption beyond naming the one A.8–A.9 already
  use.
