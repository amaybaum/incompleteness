# Audit: the ħ "derived" framing and the θ₀ match figure

Read-only audit of `amaybaum/incompleteness` at origin/main `c967d6a9` (the merge of PR #937). Nothing in the repository was edited.

- **Snapshot:** `git archive c967d6a9 papers book` and `git show` of the #937 record, extracted under `S/hbar-theta/snap/`.
- **Owner decision being implemented (2026-10-26):** "Correct the remaining 'ħ is derived' claims to distinguish genuine derivations from calibration or consistency relations. Reconcile θ₀ against one authoritative definition."
- **Line numbers** are source lines at `c967d6a9`. `[F n]` is the mirror line in `book/The-Incompleteness-of-Observation-FULL.md`. `scripts/mirror.py` checked every book hit: each chapter line has a byte-identical FULL line, and the FULL file has no unmatched hit.
- **Scripts** are in `S/hbar-theta/scripts/`: `kwic.py`, `sentence.py`, `mirror.py`, `koide_theta0.py` (+ `.out`) and `koide_closure.py` (+ `.out`).

***

## Task 1: the ħ framing

### 1.1 What the corpus derives about ħ, and what it calibrates

The anchor is GR §3–§4, with GR:551 and appendix-a:117 (#937) as the status surfaces.

**Derived, structurally.** All of these items are conditional where marked.

| # | Result | Status | Anchor |
|---|---|---|---|
| D1 | ħ is the action scale $a_*$ that converts the emergent inverse-time generator into energy. By partition-relativity it is fixed by the partition and is not a free parameter of the emergent description. | Derived | GR:78; GR:108 (Step 1) |
| D2 | Boundary-only dependence: ħ depends on the $V\times B$ dynamics only, up to $O(\tau_S/\tau_B)$. | Lemma | GR:110–134 (Step 2) |
| D3 | Dimensional reduction to $\hbar = \beta c^3\epsilon^2/G$. $A$ is excluded by observer-universality. $\kappa$ is excluded on universality grounds and cancels again in Step 4. | Derived | GR:144 |
| D4 | Thermal matching fixes $\beta = 1/(4\sigma)$, giving the functional form $\hbar = c^3\epsilon^2/(4G\sigma)$. | **Conditional** on H-slope (GR:74) with the horizon and frame conditions: H-Hawking and H-spectrum (GR:148, §8.5) | GR:148: "a conditional infrared calibration, not a theorem within the derived QFT" |

GR:76 adds that H-slope is not supplied by finite realization or reversibility. It is "a horizon-specific selection test on that open lift."

**Not derived: the value.** "$\epsilon$ is the free geometric input, $\hbar$ is the output" (GR:158). Rearranged, the relation gives $\epsilon = 2\sqrt{\sigma}\,l_p$. That is "algebraically equivalent to the formula for ħ … a self-consistency condition, not an independent determination", and with σ undetermined it "fixes only the ratio $\epsilon/\sqrt\sigma = 2\,l_p$" (GR:310). The number $1.055\times10^{-34}$ J·s therefore enters from measurement, and only $\epsilon/\sqrt\sigma$ follows from it. The calibration is not counted as a prediction (GR:551; appendix-a:117; ch07:305; G1 and G3 retired in #937).

**Classification rule used below.**

| Class | When it applies |
|---|---|
| CORRECT | The site claims D1–D4, the relation $\hbar = c^3\epsilon^2/(4G\sigma)$, or a dependence or universality statement. Any condition the context needs is stated. |
| OVERSTATED | The site claims the **value** of ħ ("the value of ħ", "predictions … the value of ℏ", "the emergent value of ħ"), or uses bare "derives ħ" / "derivation of Planck's constant" with neither the relation nor its scope. It also covers presenting the calibration as an unconditional derivation, including by dropping H-slope from a statement that lists other conditions. |
| INCORRECT | The site contradicts the derivation chain itself. Examples: quantities the chain excludes from ħ; "a theorem within the derived QFT", against GR:148; detailed balance "from the bijection", against GR:76; "Status: Theorem". |
| CONTEXT-OK | The wording read alone sounds like a value claim, but the sentence or paragraph scopes it, e.g. "ħ is derived, not free" in Step 1 of a chain that states ε is free. |

Formula uses such as $T = \hbar\kappa/2\pi c k_B$, $\hbar\omega/2$ and $e^{-iHt/\hbar}$ were excluded as not being status claims about ħ.

### 1.2 OVERSTATED and INCORRECT sites, with minimal replacements

**Search.** The corpus was grepped for `ħ`, `ℏ` (U+210F, used in Explainer, SM:1378, Computation and Substratum:46, which an `ħ`-only grep misses), `\hbar`, "Planck('s) constant", "action scale", "gap equation", "derives/derivation/determin*/value of/predict*" near ħ, "emergent ħ" and "ħ emerges". This covered `papers/*.md`, `book/*.md` (FULL included) and the root README, which has no hits.

**Replacement conventions.** Each replacement keeps the sentence and changes only what is overstated. It uses the anchor wording (GR:310, GR:551, appendix-a:117, ch07:305) and adds no history narration (§A.27/§A.30/§A.33).

#### Book (each also edited in FULL)

| Site [F] | Class | Exact text (excerpt) | Support | Defect | Minimal replacement |
|---|---|---|---|---|---|
| ch07:10 [F1889] | INCORRECT | "The horizon's geometric and thermodynamic properties — surface gravity $\kappa$, area $A$, Hawking temperature $T$ — fix the values of the emergent physics: the action scale $\hbar$, the Bekenstein-Hawking entropy with its $1/4$ coefficient, the form of the dark-energy equation of state." | GR:144 and ch07:48/54 exclude $A$ and $\kappa$ from ħ; GR:310 | Names $\kappa$ and $A$ as fixing ħ when the derivation excludes both, and claims the value | "…, Hawking temperature $T$ — fix the Bekenstein-Hawking entropy with its $1/4$ coefficient and the form of the dark-energy equation of state, and the horizon thermodynamics relates the action scale $\hbar$ to the discreteness scale $\epsilon$, with $\kappa$ and $A$ dropping out of it." (The dark-energy clause is a separate overclaim; see §4.) |
| ch07:36 [F1915], opening | OVERSTATED | "The most distinctive content … is the derivation of Planck's constant $\hbar$ as an emergent quantity determined by the cosmological horizon's thermodynamic properties. The standard view treats $\hbar$ as a fundamental constant of nature whose value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ is measured rather than derived." | GR:158, GR:310 | Contrasts "measured" with "derived" for the value, then withdraws it in the paragraph's last clause (assert-then-qualify, §A.30) | "The most distinctive content of the framework's gravitational sector is the treatment of Planck's constant $\hbar$ as an emergent action scale whose relation to the boundary geometry is fixed by the cosmological horizon's thermodynamics. The standard view treats $\hbar$ as a fundamental constant of nature, its value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ measured." The rest of the paragraph stays, including "…not an independent determination of the value of $\hbar$." |
| ch07:50 [F1929] | INCORRECT | "a QFT on a bifurcate Killing horizon, under the H-Hawking conditions, background must be periodic … giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$. This is a theorem *within* the derived QFT, not an external import — the regularity requirement follows from the Wick rotation's analytic structure." | GR:148: "The equality below is therefore a conditional infrared calibration, not a theorem within the derived QFT"; GR:148 also gives H-spectrum | Contradicts GR verbatim and omits H-spectrum. The sentence is also garbled ("horizon, under …, background") | "a QFT on this bifurcate Killing horizon background is periodic in imaginary time with period $\beta = 2\pi c/\kappa$ under the H-Hawking conditions, giving a KMS state at temperature $T_Q = \hbar\kappa/(2\pi c k_B)$ when the emergent state belongs to that KMS class (H-spectrum). The step is therefore a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2])." |
| ch07:82 [F1961] | OVERSTATED (ε side of the same calibration) | "This is not an additional empirical input but an algebraic consequence of the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ together with the definition of $l_p$." | GR:310; Explainer:507: "Given the measured value of ℏ … the discreteness scale is determined" | The numerical $\epsilon = 2\sqrt\sigma\,l_p$ uses the measured ħ through $l_p$. Calling it "not an additional empirical input" hides that the value of ħ is the input | "It adds no relation beyond the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ and the definition of $l_p$, and its numerical value takes the measured $\hbar$ as input." |
| ch01:87 [F431] | OVERSTATED | "Chapter 7 shows that the cosmological partition produces $\hbar$ as a thermodynamic identity at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following under the horizon conditions named there" | GR:148 (conditional calibration), GR:310 | "Thermodynamic identity" makes a conditional calibration unconditional, and the conditions attach only to the 1/4. The earlier clause "with value set by the partition's geometric and thermodynamic features" is D1 and CONTEXT-OK | "Chapter 7 shows that, under the horizon conditions named there, the cosmological partition relates $\hbar$ to the discreteness scale through a thermal self-consistency condition at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following" (rest unchanged) |
| ch02:22 [F665] | OVERSTATED (status) | "The action scale $\hbar$ is the conversion factor … Chapter 7 develops each of these as theorems;" | GR:148 (not a theorem); GR:24 (CC dissolution conditional) | Calls the ħ calibration, the 1/4 and the CC compression ratio theorems | "Chapter 7 develops each of these under the conditions it names;" |
| ch02:110 [F753] | OVERSTATED | "Stage 3 takes Stage 2's output and derives the emergent value of $\hbar$. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics — forces the relation" | GR:310; GR:74/148 | Claims the value and omits H-slope | "Stage 3 takes Stage 2's output and derives the emergent action-scale relation. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics, conditional on H-slope with the horizon and frame conditions named there — forces the relation". Optional at ch02:112 [F755]: after "as the unique simultaneous solution" add ", which fixes only the ratio $\epsilon/\sqrt{\sigma} = 2\,\ell_P$". |
| ch02:228 [F871] | OVERSTATED | "the boundary thermodynamics, the value of $\hbar$, the Bekenstein-Hawking $1/4$ factor" | GR:310, GR:551 | Value claim | "the boundary thermodynamics, the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking $1/4$ factor" |
| ch00:97 [F333] | OVERSTATED | "the Bekenstein-Hawking $1/4$ factor and the value of $\hbar$ from horizon thermodynamics under named horizon conditions" | GR:310, GR:551, appendix-a:117 | Value claim | "the Bekenstein-Hawking $1/4$ factor and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ as consistency relations of horizon thermodynamics under named horizon conditions" |
| ch04:204 [F1323] | OVERSTATED | "the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from horizon thermodynamics are conditional on the named horizon, frame, state and calibration assumptions" | as above | Value claim | "the Bekenstein-Hawking $1/4$ coefficient and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ from horizon thermodynamics are consistency relations conditional on the named horizon, frame, state and calibration assumptions" |
| ch06:348 [F1874] | OVERSTATED | "the value of $\hbar$ from horizon thermodynamics," | as above | Value claim. The 1/4 in the same list is already labelled a consistency relation | "the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ relating the action scale to the discreteness scale (a self-consistency condition, §7.4)," |
| ch09:14 [F2494] | OVERSTATED | "Some predictions are *universality-class* results (… the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry conditional on the horizon conditions named in Chapter 7; …)" | GR:551; ch07:305 | Value claim, and consistency relations listed as "predictions" | "Some results are *universality-class* results (… the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$ from partition geometry, consistency relations conditional on the horizon conditions named in Chapter 7; …)" |
| ch09:48 [F2528] | OVERSTATED | "the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry sit at the same level conditional on …" | as above | Value claim | "the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, consistency relations, sit at the same level conditional on …" |
| ch09:71 [F2551] | INCORRECT (status surface) | Table "Predictions stratified by hierarchy level", row "Level G4 (universality class) \| $S = A/(4 l_p^2)$, CC dissolution, $\hbar$ from partition geometry, RVM form \| structural ($1/4$ untested directly)" | #937 removed the same items from the ch09 Tier-1 table (F2), the ch07 §7.10 table and GR §7.4, as consistency or descriptive relations | A "Predictions" column still lists two consistency relations and the descriptive CC distinction | Row cell: "$S = A/(4 l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ (consistency relations), CC dissolution (descriptive), RVM form". Owner may prefer to drop them from the row instead (decision O3). No count is attached to this table. |
| ch09:92 [F2572] | OVERSTATED (heading) | "*The value of $\hbar$ from partition geometry.*" | The body already says "The functional form is universal…" | Heading claims the value | "*The action-scale relation from partition geometry.*" |
| ch09:118 [F2598] | OVERSTATED | "Bekenstein-Hawking $1/4$ and $\hbar$ from partition geometry under the horizon conditions of Chapter 7" | as above | Bare "ħ from partition geometry", listed among results "unconditionally / under conditions" | "the Bekenstein-Hawking $1/4$ and the action-scale relation for $\hbar$ as consistency relations under the horizon conditions of Chapter 7" |
| ch12:197 [F3449] | OVERSTATED | "the further observer-independent structures — the value of $\hbar$, the Standard Model, …" | GR:310 | Value claim | "— the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the Standard Model, …" |
| glossary:73 [F6673] | OVERSTATED | "The framework's derivation of Planck's constant from horizon thermodynamics." | GR:148, GR:310 | Bare derivation of the constant, with no condition | "It relates Planck's constant to the discreteness scale, conditional on H-slope, and fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$: a self-consistency condition, not an independent determination of the value of $\hbar$." |
| readers-guide:77 [F177] | OVERSTATED | "the gap equation deriving $\hbar$" | GR:158 | Bare "deriving ħ" | "the gap equation relating $\hbar$ to the discreteness scale" |
| appendix-b:16 [F5783] | OVERSTATED | "The framework derives Planck's constant $\hbar$ from a thermal self-consistency argument …" | GR:158, GR:310 | Bare derivation of the constant | "The framework relates Planck's constant $\hbar$ to the discreteness scale through a thermal self-consistency argument …" |
| appendix-b:173 [F5940] | OVERSTATED | "The framework derives Planck's constant $\hbar$ as the unique self-consistent value matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory." | GR:148, GR:74, GR:310. B.4 never names H-slope: 0 hits in appendix-b | Claims the value, and the whole of B.4 omits the condition | "The framework derives the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ between Planck's constant and the discreteness scale by matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory, conditional on H-slope with the horizon and frame conditions of Chapter 7 §7.3; with $\epsilon$ not independently known, it fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ (Chapter 7 §7.4), not the value of $\hbar$." |
| appendix-b:211 [F5978] | INCORRECT | "with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import." | GR:148 (verbatim contrary) | As ch07:50 | "with $\hbar$ unknown. The periodicity holds under the H-Hawking conditions and the KMS identification requires the emergent state to belong to that class (H-spectrum), so the matching below is a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2])." |
| appendix-b:471 [F6238] | OVERSTATED | "B.4 establishes the gap equation determining $\hbar$ from horizon thermodynamics" | GR:158, GR:310 | Value claim | "B.4 establishes the gap equation relating $\hbar$ to the discreteness scale through horizon thermodynamics" |
| appendix-c:236 [F6482] | OVERSTATED (heading) | "## C.10 Circularity concerns: the gap equation deriving $\hbar$" | as above | Bare derivation | "## C.10 Circularity concerns: the gap equation for $\hbar$" |
| appendix-c:238 [F6484] | OVERSTATED | "the framework's gap equation in Chapter 7 §7.4, which derives the Planck constant $\hbar$ from the cosmological horizon's geometric properties." | as above. The gap equation is ch07 §7.3; §7.4 is the discreteness scale | Value claim and wrong section | "the framework's gap equation in Chapter 7 §7.3, which relates the Planck constant $\hbar$ to the discreteness scale through the cosmological horizon's thermodynamics." Also at appendix-c:242 [F6488]: "Chapter 7 §7.4" → "Chapter 7 §7.3" (reference only). |
| appendix-c:257 [F6503] | OVERSTATED | "- Classical-temperature matching → $\hbar$ fixed." | GR:148, GR:158. C.10 never names H-slope | Unconditional, with no "in terms of ε" | "- Classical-temperature matching → $\hbar$ fixed in terms of $\epsilon$ (conditional on H-slope, Chapter 7 §7.3)." |
| appendix-c:263 [F6509] | OVERSTATED | "The framework's derivation of $\hbar$ is therefore consistent with the lattice structure" | as above | Bare derivation | "The gap equation is therefore consistent with the lattice structure" |

#### Papers

| Site | Class | Exact text (excerpt) | Support | Defect | Minimal replacement |
|---|---|---|---|---|---|
| GR:18 | OVERSTATED | "The cosmological observables that most resist explanation within standard physics — the value of $\hbar$, the Bekenstein-Hawking area law, … — are treated here as consequences of a single structural fact" | GR:310 (in the same paper) | The value is not a consequence | "— the origin of the action scale $\hbar$, the Bekenstein-Hawking area law, … —" |
| GR:336 | OVERSTATED (classification) | "The framework's predictions in Part II ($\hbar$, $S_{\text{dS}}$, the Type II RVM form of the dark energy) depend on partition geometry" | GR:551 (calibration not a prediction) | Lists ħ as a prediction | "The framework's Part II results (the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, $S_{\text{dS}}$, the Type II RVM reading of the dark energy) depend on partition geometry" |
| Main:684 | OVERSTATED | "the framework derives $\hbar$ and the Bekenstein–Hawking coefficient downstream, and the derived bound is compatible with the finiteness assumed here" | GR:310, GR:551 | Bare derivation of ħ, and the 1/4 called derived when it is a consistency relation | "the framework relates $\hbar$ to the discreteness scale and recovers the Bekenstein–Hawking coefficient downstream, as consistency relations of its horizon calibration [GR], and the derived bound is compatible …" |
| SM:1350 | OVERSTATED | "including the derivation of $\hbar$, the Bekenstein-Hawking area law, …" | GR:310 | Bare derivation | "including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking area law, …". The same sentence's unconditional "the dissolution of the cosmological constant problem" is listed in §4. |
| SM:1576 | OVERSTATED | "including the derivation of $\hbar$ from the cosmological horizon and the Bekenstein-Hawking area law including the $1/4$ coefficient (both conditional on the horizon conditions recorded there)" | GR:310, GR:551 | Bare derivation | "including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking area law with its $1/4$ coefficient (consistency relations, both conditional on the horizon conditions recorded there)" |
| SM:1378 | INCORRECT (status) | §8.3 **Structural predictions**: "… unique hypercharges from anomaly cancellation, ℏ = c³ε²/(4G), the Bekenstein-Hawking formula, and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems." | GR:148 (not a theorem), GR:551 (not predictions); σ missing (GR:156) | Two consistency relations are listed as structural predictions and called theorems | Delete "ℏ = c³ε²/(4G), the Bekenstein-Hawking formula," and add after the list: "The horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking coefficient it matches hold for the same class as consistency relations conditional on H-slope [GR §3.2, §4–§5]." No count is attached to this list. "These are theorems" is also questionable for the generations (SM:32 Tier 2); see §4. |
| Substratum:22 | OVERSTATED | "the framework determines $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, for an entropy $\sigma$ per boundary mode, the Bekenstein-Hawking entropy with the $1/4$ coefficient, and the dissolution of the cosmological constant problem." | GR:310, GR:148 | Substituting the second relation into the first gives the identity $\hbar = c^3 l_p^2/G$, which is presented as a determination; no condition is stated | "the framework relates the action scale to the discreteness scale through the calibration $\hbar = c^3 \epsilon^2 / (4G\sigma)$, which fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ for an entropy $\sigma$ per boundary mode, and recovers the Bekenstein-Hawking entropy with the $1/4$ coefficient as a consistency relation of that calibration, both conditional on H-slope [GR §3.2], and proposes a dissolution of the cosmological constant problem conditional on the covariant coupling step [GR §6.2]." The CC clause is outside the ħ scope; see §4. |
| Substratum:178 | OVERSTATED | "**Output:** The emergent value of $\hbar$ is $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length …" | GR:310 | Same identity, presented as "the value" | "**Output:** The emergent action-scale relation $\hbar = c^3 \epsilon^2 / (4G\sigma)$, equivalently $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]); it fixes only $\epsilon/\sqrt{\sigma}$, not the value of $\hbar$ ([GR §4])." |
| Substratum:180 | INCORRECT | "…, detailed balance (consequence of $\varphi$ being a bijection). No new structural assumptions beyond Stages 1–2." | GR:76: "finite realization, reversibility and finite intervention statistics do not give H-balance, and … the failure already occurs at H-slope"; H-slope is "a horizon-specific selection test on that open lift" | States the opposite of GR on the load-bearing condition | Replace both clauses with: "and the infrared detailed-balance condition H-slope with the horizon and frame conditions ([GR §2, §3.2, §8.5]), which does not follow from $\varphi$ being a bijection ([GR §3.2]) and is an assumption beyond Stages 1–2." |
| Substratum:182, 184 | INCORRECT (status) | "…admits a unique solution under the stated inputs ([GR §3, Theorem])." / "**Status:** Theorem." | GR §3 has no such theorem; GR:148 calls the step a conditional calibration, not a theorem | The status label contradicts the anchor | :182: "([GR §3.2])". :184: "**Status:** Conditional on H-slope with the horizon and frame conditions ([GR §3.2])." This is a status reclassification: decision O1. |
| Substratum:192 (Theorem 23) | OVERSTATED (conditional → unconditional by omission) | "… and $\hbar=c^3\epsilon^2/(4G\sigma)$, with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork." | GR:148, GR:74 | The theorem enumerates its qualifications and omits H-slope for the ħ clause | "… and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope with the horizon and frame conditions of [GR §3.2], with the same qualifications stated in [SM] …" (O1). Dependants: Substratum:188/190/194 then inherit the condition (CONTEXT-OK); ch02:118 [F761] and ch02:88 [F731] already say "with the qualifications carried by the cited derivations" (CONTEXT-OK). |
| Structure:47 | OVERSTATED (as Substratum:192) | "…, with the qualifications stated in [SM], and $\hbar=c^3\epsilon^2/(4G\sigma)$, $\sigma$ the entropy per boundary mode [GR §3.1]." | as above | Same omission | "…, and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope [GR §3.2], $\sigma$ the entropy per boundary mode [GR §3.1]." |
| Methodology:339 | OVERSTATED (as above) | "The reconstruction yields, as forced outputs rather than fitted parameters, … three generations (physical reading conditional on H-spin' …); … and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ tying Planck's constant to …" | as above | Qualifies the other conditional outputs but not ħ | "… and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$, conditional on H-slope ([GR §3.2]), tying Planck's constant to …" |
| Explainer:411 | OVERSTATED | "The value of ℏ is determined by the partition geometry — which is what Section 5 derives." | GR:158, GR:310 | Value claim | "The action scale ℏ is fixed by the partition geometry in terms of the discreteness scale — which is what Section 5 derives." |
| Explainer:477 | OVERSTATED (condition omitted) | "**What the gap equation fixes.** The gap equation relates one free geometric parameter (ε), at given σ, to one output (ℏ)." | GR:74/148. The Explainer §5 derivation (:439–:475) never names H-slope | Unconditional calibration | "…The gap equation, conditional on the infrared detailed-balance condition H-slope with the horizon and frame conditions [GR §3.2], relates one free geometric parameter (ε), at given σ, to one output (ℏ)." |
| Explainer:662 | OVERSTATED | "It makes quantitative predictions — the value of ℏ and dark energy evolution — that interpretations do not" | GR:551 (not a prediction), GR:310 | Value claimed as a prediction | "It makes a quantitative prediction — dark energy evolution — that interpretations do not, relates ℏ to the discreteness scale, and accounts for …". "Dark energy evolution" is itself a separate question: GR §7.1 says the form is not a derived law (§4). |
| Explainer:992 | OVERSTATED | "[GR], which derives ℏ, the Bekenstein-Hawking area law, and dark-sector phenomenology" | GR:310, GR:551 | Bare derivation | "[GR], which relates ℏ to the discreteness scale, recovers the Bekenstein-Hawking area law, and develops dark-sector phenomenology". The quoted GR title does not match GR:1 (§4). |

### 1.3 CORRECT and CONTEXT-OK sites, kept as they are (§A.25 step 4)

**CORRECT (34).** These sites claim the relation, D1–D4, or universality, and state any condition the context needs.

- **GR:** :12 (conditions stated), :24, :28, :30 ("not 'OI predicts ħ uniquely'"), :164 ("derives ħ from G and ε"), :310 (anchor), :551 (anchor), :629, :655, :705 ("with ε the one free geometric input").
- **ch07:** :12, :16, :22, :57 ("a genuine determination of ħ in terms of the discreteness scale"), :63, :65, :305, :307, :313.
- **Other book:** ch02:192, ch05:41, appendix-a:117 (anchor), readers-guide:15.
- **Other papers:** SM:90; Substratum:46, :116, :324 (conditions stated); Explainer:298, :399, :507, :900, :974, :1043, :1055.

**CONTEXT-OK (56).** These sites use "derived/determined" for ħ in the sense of D1–D2 (fixed by the partition, depends only on boundary data) or for gauge invariance ("the same value of ħ" across equivalent substrata).

- **GR:** :1 (title), :32, :42, :90, :108 ("ħ is derived, not free": Step 1; optionally "ħ is fixed by the partition, not a free parameter of the emergent description"), :134, :158 ("a genuine determination": ε is stated free in the same paragraph; optionally align with ch07:57's "of ħ in terms of the discreteness scale"), :228, :296 (but see §4: "§3.4" does not exist), :352, :440, :565, :605, :753.
- **ch07:** :48, :61 (the relation is stated in the same sentence), :71, :86, :124, :185, :187.
- **ch02/ch03:** ch02:88, :112, :114, :118, :120, :134; ch03:80, :220.
- **Other book:** book/README:98 (states the relation); appendix-b:195, :199, :219, :221; appendix-c:244, :246, :259.
- **Explainer:** :417, :439, :449, :475, :545, :699 ("treats ħ as an unexplained input": the contrast is with ħ as a postulate, and the sentence already carries #937's "relates ħ to the discreteness scale"), :1024.
- **Other papers:** Computation:70; Structure:154, :647; Substratum:26, :188, :190, :194, :248, :260, :284, :290, :292.

### 1.4 Task 1 counts

| Class | Book sources (each + FULL) | Papers | Total |
|---|---|---|---|
| OVERSTATED | 23 (ch00:97, ch01:87, ch02:22, :110, :228, ch04:204, ch06:348, ch07:36, :82, ch09:14, :48, :92, :118, ch12:197, glossary:73, readers-guide:77, appendix-b:16, :173, :471, appendix-c:236, :238, :257, :263) | 14 (GR:18, :336, Main:684, SM:1350, :1576, Substratum:22, :178, :192, Structure:47, Methodology:339, Explainer:411, :477, :662, :992) | **37** |
| INCORRECT | 4 (ch07:10, ch07:50, ch09:71, appendix-b:211) | 3 (SM:1378, Substratum:180, Substratum:182/184) | **7** |
| CORRECT | | | 34 |
| CONTEXT-OK | | | 56 |

FULL mirror edits needed: 27 lines (23 + 4), plus appendix-c:242 [F6488], a reference-only fix.

The caller's list included ch02:110 (in the CHANGE-NOTE §9 list, not in the brief). Every listed site falls in OVERSTATED or INCORRECT except ch02:228, whose CHANGE-NOTE line number is unchanged; it is OVERSTATED.

**Counts.** No Task 1 change alters a prediction count. The calibration is already outside every count (GR:551, appendix-a:117, ch07:305), and SM §8.3 (SM:1378), ch09:71 and GR:336 carry no totals. One change is a status reclassification, not a count: Substratum §3.4 "Status: Theorem", which feeds Theorem 23 (O1).

***

## Task 2: θ₀'s figure

### 2.1 The authoritative definition

**SM:903** (§7.2, the body derivation; harmonized in `bd7ae77c`, 2026-08-11, "θ₀ observed harmonized; τ input refreshed"):

> Observed: $\theta_0 = 0.222225 \pm 0.000006$ — the three charged-lepton pole masses determine $(\mu, A, \theta_0)$ exactly (PDG 2024/25; uncertainty from $m_\tau = 1776.93 \pm 0.09$ MeV). Match: $0.001\%$ ($0.4\sigma$).

The definition has four parts.

- **Parametrization (SM:895):** $\sqrt{m_k} = \mu\,(1 + A\cos(\theta_0 + 2k\pi/3))$, with $k = 0$ (τ), 1 (e), 2 (μ).
- **Extraction:** all three of $(\mu, A, \theta_0)$ are solved from the three masses. $A$ is **not** fixed to $\sqrt2$, so θ₀ (the phase) and $Q = \tfrac13 + A^2/6$ (the amplitude) are independent observables (SM:895: "Both Koide degrees of freedom").
- **Masses:** PDG 2024. SM cites only "PDG 2024/25" and $m_\tau = 1776.93 \pm 0.09$ MeV. I used $m_e = 0.51099895000(15)$ MeV and $m_\mu = 105.6583755(23)$ MeV (PDG 2024), whose errors are negligible.
- **"Match":** the relative deviation $(\theta_0^{\rm obs} - 2/9)/(2/9)$, with the pull against the $m_\tau$-propagated error.

### 2.2 Recomputation (`scripts/koide_theta0.py`, mpmath at 50 digits)

**Controls (all PASS):**

| Control | Check |
|---|---|
| C1 | Masses rebuilt from the extracted $(\mu, A, \theta_0)$ equal the inputs (< 1e-40) |
| C2 | $Q = 1/3 + A^2/6$ identity |
| C3 | The exact Koide point ($A = \sqrt2$, $\theta_0 = 2/9$) returns $Q = 2/3$ and $\theta_0 = 2/9$ |
| C4 | Cyclic relabelling shifts θ₀ by $2\pi/3$; reflection gives $-\theta_0$ |

**Results.** The figures are generated from the measurements.

| Input | θ₀ | (θ₀ − 2/9)/(2/9) | pull | Q | (Q − 2/3)/(2/3) | pull |
|---|---|---|---|---|---|---|
| **PDG 2024** ($m_\tau$ 1776.93 ± 0.09) | **0.2222248 ± 0.0000063** | **+0.00114 %** | **0.41σ** | 0.6666645 ± 0.0000051 | −0.00033 % | 0.43σ |
| PDG 2016–22 ($m_\tau$ 1776.86 ± 0.12) | 0.2222296 ± 0.0000084 | +0.0033 % | 0.89σ | 0.6666605 ± 0.0000068 | −0.00092 % | 0.91σ |
| PDG 2012–14 ($m_\tau$ 1776.82 ± 0.16) | 0.2222324 ± 0.000011 | +0.0046 % | 0.92σ | 0.6666583 ± 0.0000090 | −0.0013 % | 0.93σ |

**Predicted masses** ($Q = 2/3$, $\theta_0 = 2/9$, $m_\tau$ as input):

| $m_\tau$ input | $m_e$ | $m_\mu$ |
|---|---|---|
| 1776.93 | 0.510983 MeV (−0.0031 %) | 105.6561 MeV (−0.0021 %) |
| 1776.86 | 0.510963 MeV (−0.0070 %) | 105.6520 MeV (−0.0061 %) |

`scripts/koide_closure.py` gives the Koide closure for $m_\mu$ from observed $m_e$ and $m_\tau$ at Q = 2/3: 105.6558 MeV (−0.0024 %). It also gives $m_e/m_\tau$ = 2.8757e-4 against $1/(36\pi^4)$ = 2.8517e-4 (−0.84 %).

**Verdict (printed by the script over green controls):** θ₀(PDG 2024) deviates from 2/9 by 0.00114 % (0.41σ). SM:903's "0.001% (0.4σ)" reproduces. "0.02%" is inconsistent with it.

### 2.3 Where each figure comes from

| Figure | Origin |
|---|---|
| **0.001 % (0.4σ)** | Correct for θ₀ under the SM:903 definition. |
| **0.02 %** | The pre-`bd7ae77c` text: "Observed: $\theta_0 = 0.22227$. Match: $0.02\%$" (`git show bd7ae77c -- papers/SM.md`). $(0.22227 - 2/9)/(2/9) = 0.0215\%$. `bd7ae77c` updated SM:903, the §7.2 uniqueness table and the §7.6 θ₀ row, but not SM:14, :928, :1318, :1329, :1572, Juno:401 or any book/Substratum site. The old observed value 0.22227 is not reproduced by any PDG edition tested (0.222225–0.222232). It is not θ₀'s deviation, and not the deviation of a derived mass. |
| **0.2 % and "observed 0.2227"** | SM:928, SM:934 and SM:940 use 0.2227, a misprint or rounding of 0.22227 that drops a 2: $(0.2227 - 2/9)/(2/9) = 0.215\%$. SM:940's "$0.2\%$ agreement" and its bound "$\delta m/m \lesssim 8 \times 10^{-5}$" are built on it: $0.002/(35 \times 0.76\text{–}0.78) = 7.3\text{–}7.5\times10^{-5}$. |
| **ch06:171 "θ₀^obs = 0.222220"** | Not reproduced by any edition. |
| **$m_e$ 0.51096 MeV (0.007 %), $m_\mu$ 105.652 MeV (0.006 %)** | Predictions from $m_\tau$ = 1776.86 (PDG 2016–22). Current with 1776.93: 0.51098 (0.003 %) and 105.656 (0.002 %), as SM:977–978 already have. |
| **$m_\mu$ 105.74 MeV (0.07 %), "Koide closure"** (ch06:190, :218, :305) | Not reproduced. The closure gives 105.656 MeV (0.002 %). |
| **Koide Q 0.666661 ± 0.000007 (0.8σ)** (ch00:77, glossary:97, set in #937) | The PDG 2016–22 $m_\tau$ value. Under SM:903's PDG 2024 basis it is 0.666664 ± 0.000005, 0.0003 %, 0.4σ. The "better than 0.001 %" wording holds either way. |

### 2.4 θ₀ sites and replacements

**Rule:** θ₀ = 2/9 is matched to **0.001 % (0.4σ)** against $\theta_0^{\rm obs} = 0.222225 \pm 0.000006$ (PDG 2024). "Koide relation" names Q; θ₀ is "the Koide angle".

**Already correct (keep):** SM:903, SM:907–909 (uniqueness table), SM:1268 (§7.6 row), Juno:55, Juno:379, ch04:134 [F1253]. appendix-a:80 [F5617] "Within 1%" is true but coarse beside entry 10's "<0.001%"; optionally "**0.001%**".

| Site [F] | Exact text | Replacement |
|---|---|---|
| SM:14 | "the Koide angle $\theta_0 = 2/9$ to $0.02\%$" | "… to $0.001\%$" |
| SM:928 | "which misses the observed $0.2227$ by a factor of four … The empirical match at $0.02\%$ does not *select* …" | "the observed $0.2222$" … "The empirical match at $0.001\%$ …" |
| SM:934 | "$2/9 = 0.2222$ (observed $0.2227$)" | "(observed $0.222225$)" |
| SM:940 | "The $0.2\%$ agreement of $\theta_0 = 2/9$ bounds … by $\delta m/m \lesssim 8 \times 10^{-5}$; a second-order lepton-Yukawa loop supplies $\sim 10^{-6}$." | Numeric value changes: **O4** |
| SM:1318 (§7.7 table) | "\| Koide $\theta_0$ \| $C_2/d^2 = 2/9$ \| 0.2222 \| 0.2222 \| 0.02% \|" | "\| … \| 0.22222 \| 0.222225 \| 0.001% \|" |
| SM:1329 | "the two tightest ($\lambda$ at $0.04\%$, $\theta_0$ at $0.02\%$)" | "… $\theta_0$ at $0.001\%$)". See O5 on "two tightest". |
| SM:1572 | "the Koide angle from the cubic-group quadratic Casimir to $0.02\%$" | "… to $0.001\%$" |
| Juno:401 | "Koide θ₀ (0.02%)" | "Koide θ₀ (0.001%)" |
| Substratum:446 | "the sharpest empirical match in the framework (0.02%)" | "(0.001%)". O5 on "sharpest". |
| book/README:62 | "Koide $\theta_0 = 2/9$ at $0.02\%$" | "… at $0.001\%$" (book/README is not in FULL) |
| ch05:196 [F1525] | "the Koide relation $2/9$ matched to $0.02\%$" | "the Koide angle $\theta_0 = 2/9$ matched to $0.001\%$" (label and figure) |
| ch06:171 [F1697] | "which is the angular form of the $Q = 2/3$ relation under the standard $\mathbb{Z}_3$-symmetric parametrization of three masses by an angle. The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222220$ at $0.02\%$ — the sharpest empirical agreement in the framework." | INCORRECT, because θ₀ is independent of Q (SM:895). Replace with: "which is the phase of the standard $\mathbb{Z}_3$-symmetric parametrization of three masses, whose amplitude $Q = 2/3$ fixes independently (SM §7.2). The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222225 \pm 0.000006$ at $0.001\%$ ($0.4\sigma$)." O5 covers whether to keep "the sharpest …". |
| ch06:303 [F1829] (§6.8 table) | "\| Koide angle $\theta_0$ \| $C_2(T_1)/d^2$ \| $2/9$ \| $0.22222$ \| $0.02\%$ \| **C** \| **A** \|" | "… \| $0.222225$ \| $0.001\%$ \| …" |
| ch08:68 [F2271] | "the Koide angle at $0.02\%$" (label fixed in #937; figure remains) | "the Koide angle at $0.001\%$" |
| ch08:177 [F2380] | "the Koide angle at $0.02\%$" | "… at $0.001\%$" |
| ch08:210 [F2413] | "the Koide angle at $0.02\%$" | "… at $0.001\%$" |
| ch03:42 [F918] | "the Koide relation $2/9$" | "the Koide angle $2/9$" (label) |
| ch03:118 [F994] | "the Koide relation as $2/9$ from a cubic-group Casimir" | "the Koide angle as $2/9$ from a cubic-group Casimir" (label) |
| ch06:320 [F1846] | "Koide $Q = 2/3$ (and equivalently Koide $\theta_0 = 2/9$ — the same prediction in dual form), … These seven relations are tested through five empirical channels" | INCORRECT, since the two are independent (SM:895; the ch06 table tags both Cat A). Correcting it **changes the count** "seven" → "eight" relations: **O2** |

**Related stale mass figures** (same θ₀ chain; PDG 2016–22 $m_\tau$ or unreproduced):

| Site [F] | Exact text | Replacement |
|---|---|---|
| SM:1269–1270 (§7.6) | "$m_e$ … 0.51096 MeV … 0.007%"; "$m_\mu$ … 105.652 MeV … 0.006%" | "0.51098 MeV … 0.003%"; "105.656 MeV … 0.002%" (as SM:977–978) |
| ch06:12 [F1538] | "… $\theta_0 = 2/9$ — at $0.007\%$." | "… at $0.003\%$." |
| ch06:181 [F1707] | "(the tau mass $m_\tau = 1776.86$ MeV) … $m_e = 0.51096$ MeV and $m_\mu = 105.652$ MeV … ($0.007\%$ and $0.006\%$; SM §7.2)" | "$m_\tau = 1776.93$ MeV … $m_e = 0.51098$ MeV and $m_\mu = 105.656$ MeV … ($0.003\%$ and $0.002\%$; SM §7.2)" |
| ch06:189–190 [F1715–1716] | "$0.51096$ MeV \| $0.5110$ \| $0.007\%$"; "$m_\mu$ \| Koide closure with $m_e$, $m_\tau$ \| $105.74$ MeV \| $105.66$ \| $0.07\%$" | "$0.51098$ MeV \| $0.51100$ \| $0.003\%$"; "$105.656$ MeV \| $105.658$ \| $0.002\%$". ch06:192 [F1718] ("$m_\mu/m_\tau = 0.0595$ … ($0.07\%$) … RG running" explanation) rests on the unreproduced 105.74: O6. |
| ch06:304–305 [F1830–1831] (§6.8 table) | "$0.51096$ MeV … $0.007\%$"; "Koide closure \| $105.74$ MeV \| $105.66$ MeV \| $0.07\%$" | "$0.51098$ MeV … $0.003\%$"; "$105.656$ MeV \| $105.658$ MeV \| $0.002\%$" |
| ch06:217–218 [F1743–1744] (six-mass chain table) | "$0.51096$ MeV \| $0.511$ \| $0.007\%$"; "$105.74$ MeV \| $105.66$ \| $0.07\%$" | These rows sit in the chain from predicted $m_\tau$ = 1755. SM's chain table (SM:983–984) has 0.505 MeV and 104.4 MeV, both 1.2 %: O6. |
| ch06:344 [F1870] | "($m_e$ at $0.007\%$ and $m_\mu$ at $0.006\%$ via $Q$ and $\theta_0$)" | "($m_e$ at $0.003\%$ and $m_\mu$ at $0.002\%$ …)" |
| ch06:179 [F1705] | "constrains it to $\delta m/m \lesssim 8 \times 10^{-5}$, which a lepton-Yukawa loop satisfies" | Mirrors SM:940: O4. |

**Task 2 counts:**

| Category | Sites |
|---|---|
| θ₀ figure corrections | 15: SM:14, :928, :934, :1318, :1329, :1572; Juno:401; Substratum:446; book/README:62; ch05:196; ch06:171, :303; ch08:68, :177, :210 |
| Label-only | 2: ch03:42, :118 |
| INCORRECT equivalence statements | 2: ch06:171 (counted above), ch06:320 |
| Stale mass rows | 7 sources: SM:1269–1270, ch06:12, :181, :189–190, :304–305, :344 |
| Owner-decision rows | 3: SM:940 with ch06:179; ch06:192; ch06:217–218 |
| Already correct | 6 |

FULL mirror lines to edit: ch03:42/118, ch05:196, ch06:12/171/181/189–190/303/304–305/320/344 and ch08:68/177/210.

**Counts:** only ch06:320 touches a count ("seven relations"), and only if θ₀ is separated from Q (O2). No S/C/L/R/P/M/E classification changes: θ₀ stays **C** everywhere.

***

## 3. Decisions for the owner

- **O1 — the status of Substratum §3.4 Stage 3 and Theorem 23's ħ clause.**
  - "**Status:** Theorem" and "No new structural assumptions beyond Stages 1–2" contradict GR:148 (conditional calibration) and GR:76 (H-slope is not given by the bijection).
  - Proposal: mark Stage 3 conditional on H-slope and add H-slope to the ħ clause of Theorem 23 (Substratum:192), Structure:47 and Methodology:339.
  - This is a theorem/status reclassification, though not a prediction count, so it needs the owner's word. Check the Lean census registry (§A.35) for any kernel anchor carrying "Theorem 23"; none was checked here.
- **O2 — ch06:320, Category A.** θ₀ and Q are independent (SM:895), so "equivalently … the same prediction in dual form" is wrong. The choices:
  - (a) list θ₀ as its own Category A relation, making it "eight relations" (a count change);
  - (b) keep seven, with Q and θ₀ named as two relations of one Koide entry. This needs a sentence and no count change.
- **O3 — ch09:71 (Level G4 row).** Either relabel the consistency relations inside the "Predictions" cell, as proposed, or remove them, as #937 did for the Tier-1 table.
- **O4 — SM:940 and ch06:179, the dressing bound.**
  - The bound is built on the stale 0.2 %.
  - With the PDG 2024 θ₀ (deviation 1.1e-5, σ 2.8e-5 relative) and $|d\theta_0/\theta_0| \approx 27\,\delta m/m$, the bound is $\lesssim 4\times10^{-7}$ at the central deviation and $\lesssim 2.5\times10^{-6}$ at the 2σ envelope.
  - The "lepton-Yukawa loop ~1e-6 satisfies it" margin shrinks from ~80× to ~2.5× (2σ), or fails at the central value.
  - The owner should fix the bound rule (central or 2σ) before the number is regenerated. Do not pick it to keep the conclusion.
- **O5 — "the sharpest empirical agreement."** It is claimed for θ₀ at ch04:134, ch06:171 and Substratum:446, and for Q at ch06:12. On PDG 2024, Q (0.0003 %, 0.43σ) is tighter than θ₀ (0.001 %, 0.41σ) in relative terms, with equal pulls. SM:1329's "two tightest (λ, θ₀)" omits Q. Choose one statement.
- **O6 — ch06 chain rows.**
  - The ch06 tables quote $m_\mu$ = 105.74 MeV (0.07 %) for "Koide closure"; this is not reproduced (closure gives 105.656 MeV, 0.002 %). ch06:192's RG-running explanation of that 0.07 % depends on it.
  - The six-mass chain table (ch06:217–218) uses observed-$m_\tau$ values where SM's chain table uses the predicted $m_\tau$ (0.505 MeV and 104.4 MeV, both 1.2 %).
- **O7 — Koide Q basis (optional).** ch00:77 and glossary:97 (0.666661 ± 0.000007, 0.8σ, set in #937) use the PDG 2016–22 $m_\tau$, while the authoritative θ₀ (SM:903) uses PDG 2024. Harmonizing would give Q = 0.666664 ± 0.000005 (0.4σ). SM:1267 shows "0.66666, < 0.01%" and ch06:302 shows "0.66667, 0.001%".

## 4. Noticed, outside the two tasks

These were not classified above.

- **GR:296** cites "§3.4's determination of ħ". GR has only §3.1–§3.3, and the determination is in §3.2.
- **Substratum:182** cites "[GR §3, Theorem]", which does not exist.
- **Unconditional CC "dissolution"** in sentences carrying ħ sites: SM:1350 ("the dissolution of the cosmological constant problem"), Substratum:22 ("and the dissolution of the cosmological constant problem"). Compare GR:24 ("conditional on the G3 coupling theorem").
- **Dark-energy form presented as fixed or predicted:** ch07:10 ("fix … the form of the dark-energy equation of state"), Explainer:662 ("quantitative predictions — … dark energy evolution"), and "dynamical dark energy prediction" (SM:1350). Compare GR:12 and §7.1 ("a structural reading, not a derived law").
- **SM:1378 "These are theorems."** The same list includes "three generations", which SM:32 places on the conditional Tier-2 branch (H-spin').
- **Explainer:992** gives [GR] the title "The Gravitational Sector from the Cosmological Horizon"; GR:1 is "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon".
- **ch09:92** body: "the specific value of $\epsilon$ would vary across alternative substrata, with self-consistency requiring $\epsilon = 2\sqrt\sigma\,l_p$ for any member of the class" is internally strained (vary / required).
- **SM §7.6 Koide Q** "< 0.01%" against SM:895 "0.001%".

## 5. Scripts

All are in `S/hbar-theta/scripts/` and run with `python3 -I`.

- `kwic.py ROOT REGEX [WIDTH] [globs…]`: keyword-in-context grep.
- `sentence.py ROOT REGEX file:line…`: prints the matching sentences.
- `mirror.py ROOT REGEX`: maps chapter lines to identical FULL lines and lists FULL-only hits. It found none for either task's patterns.
- `koide_theta0.py`: θ₀ and Q from PDG masses at 50 digits, with controls C1–C4 and a generated verdict. Output is in `koide_theta0.out`.
- `koide_closure.py`: closure $m_\mu$ and $m_e/m_\tau$ check, with its control. Output is in `koide_closure.out`.
