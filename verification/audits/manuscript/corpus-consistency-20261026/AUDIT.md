# Independent verification of suspected overclaims (owner scope, 2026-10-26)

Read-only. Corpus: `main` at `687e885b` (worktree `S/cc2/wt`, branch `fix/corpus-consistency-20261026`, full
history of 3,720 commits, not shallow). The audit edited no manuscript; this record was committed afterwards for review. Every git command
ran with `-c gc.auto=0 -c maintenance.auto=false`, and no gc, prune or maintenance was run. Untrusted Python was run
with `python3 -I`. `S` is the session scratch directory (absolute prefix elided).

Input under test: `S/paper/apps/AUDIT.md`, §9 and its hidden-assumption notes. I treated every item there as a claim
to verify, and I did not reuse its scripts. My own checks are committed beside this record in `scripts/`:

| Script | Output | What it settles | Layer |
|---|---|---|---|
| `quarter_indep.py` | `quarter_indep.out` | The Bekenstein–Hawking coefficient under GR §3–§5's calibration, re-derived by a different route (measured ħ held fixed, the calibration solved for the mode density), with 8 controls and countercontrols | exact symbolic (sympy 1.14), plus exact rational spot checks |
| `cc_indep.py` | `cc_indep.out` | ρ ~ H²/G as the Friedmann normalization; the 10¹²² = S_dS relation and its O(1) factor | exact symbolic, plus numerics |
| `cabibbo_cmp.py` | `cabibbo_cmp.out` | 1/(π√2) against PDG 2025 values I read first-hand | numerics |
| `mirror.sh` | — | FULL.md mirror line for a given chapter line (full-line `grep -nxF`) | text |

External source read first-hand: PDG *Review of Particle Physics* 2025, ch. 12 "CKM Quark-Mixing Matrix", revised April
2024 by A. Ceccucci, Z. Ligeti and Y. Sakai. Downloaded from `https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf`
into `S/cc2/pdg/` (sha256 `a0a78578971f38ff89c6fc5579bc608de41ec383a205dc25cba1d26f7145610a`; text extracted with pdftotext). WebFetch could not resolve the host; curl
through the agent proxy reached it.

Ownership: PR #936 (`fix/bh-consistency-20261026`, head `4c0d705e` when this audit ran; `b61cbaa9` also changes ch07:147 and GR:833, which no edit here touches) changes these lines, numbered at `687e885b`:
GR 605, 611, 717, 805–869, 1007; ch07 12, 110, 116, 118, 126, 130–132, 143, 149, 157–161, 288; ch09 108, 127;
ch18 146–158 (even lines); ch19 72, 334; glossary 113; appendix-a 103, 116; book/README 64; and their FULL mirrors
1889, 1987–2038, 2165, 2588, 2607, 4966–4978, 5248, 5510, 5656, 5669, 6735. I propose no edit to any of these lines;
§5 lists the ones my items touch.

***

## 0. Summary table

Defect classes: **INC** = INCORRECT; **OVR** = OVERSTATED; **NQ** = NEEDS-QUALIFICATION; **OK** = CONSISTENT.
"Named five?": **Y** means the item is among the owner's named five. **N** means it is outside them, for the owner to
include or defer.

| # | Site / FULL | Original wording (short) | Support | Defect | Status class (corpus) | Replacement (short) | Named five? |
|---|---|---|---|---|---|---|---|
| 1.1 | GR:12; GR:707; Substratum:324; ch02:112/FULL:755; ch02:192/835; ch03:118/994; ch06:348/1872; ch00:81/317; ch09:88/2568; Structure:452; [ch07:12/1889 is #936's] | "obtains … the 1/4 coefficient by direct boundary-mode counting" | GR §3.2 Step 4 and §5; `quarter_indep.py` | OVR | Consistency, conditional on H-slope and the horizon/frame conditions (C) | "…the mode count reproduces A/(4l_p²) once the calibration fixes ε/√σ = 2l_p; the 1/4 is the ratio 2π/8π of the KMS and first-law normalizations" | Y |
| 1.2 | ch00:21/257; preface:7/78; ch00:89/325; glossary:17/6639; ch00:81/317 (second clause); [README:64 is #936's] | "becomes a derivation rather than a postulate"; "in the standard account the factor is a postulate" | GR:322's own statement that T_H plus the first law fixes it (Hawking 1975) | **INC** (the "postulate" premise) and OVR ("derivation") | Consistency (C) | "The 1/4 is recovered as a consistency relation between the classical and emergent horizon temperatures (conditional on H-slope)" | Y |
| 1.3 | GR:322; ch07:104/1981; GR:707 | "a derived structural constant"; "a structural constant rather than an empirical fit" | GR:320 and GR:104 ("fixed point … regardless") | OVR | Consistency (C) | "…the ratio of the two normalizations the calibration matches, conditional on H-slope; no direct test" | Y |
| 1.4 | GR:162; ch07:63/1940; Explainer:477, :1043 | "Any alternative ħ(ε) would fail at least one of these checks" (offered as "predictive content") | Circular: the 1/4 check is the calibration's own identity; the other two checks do not fix the O(1) prefactor | OVR | Consistency | Delete the sentence, or say "the three relations share the calibration and are not independent checks of it" | Y |
| 1.5 | GR:164; ch07:65/1942 | "The Gibbons–Hawking temperature … is recovered as a prediction, not used as an input" | GR:148 uses T_Q = ħκ/(2πck_B) as the input of Step 4 | **INC** | — | "The Gibbons–Hawking form ħκ/(2πc) is the KMS input of Step 4; the calibration fixes ħ in it" | Y (new) |
| 1.6 | ch18:160/4980 | the 1/4 listed among "predictions it makes that neither QM nor GR alone makes" | Semiclassical QM+GR yields the 1/4 (Hawking route; `quarter_indep.py` item 7) | **INC** | — | Remove the 1/4 (and ħ, and the RVM form) from that list | Y |
| 1.7 | GR:320; Explainer:521, :523; ch07:90/1967 | "historically introduced as a proportionality constant"; "a mystery for 50 years"; "historically unexplained" | GR:322's "T plus the first law fixes it" | NQ (GR:320); OVR (Explainer:523, ch07:90) | — | "introduced by Bekenstein (1973) with an undetermined coefficient, fixed by Hawking (1975) from T_H and the first law" | Y |
| 1.8 | appendix-a:110 (G4)/5663; :93 (row 24)/5646 | G4 and row 24: "C … No direct test" | GR §3–§5 | NQ (class correct) | C; Consistency | Keep C; empirical column "Consistency relation; no direct test". No count change | Y |
| 2.1 | GR:583 (+ GR:585, :587) | "a theorem of the reconstruction … attributes physical content to a gauge degree of freedom" | GR:356's two-completion countermodel | **INC** | Open (the coupling) | "…is invisible to every visible transition probability; whether it sources curvature is the open coupling question (§6.2)" | Y |
| 2.2 | GR:356, last two sentences | "never enters the stress-energy tensor; no decoupling mechanism is needed" | Same paragraph: "the dissolution is conditional" | OVR (§A.30 assert-then-qualify) | Conditional on Level G3 | "…on the proposal of §6.2 the zero-point sum does not enter the stress-energy tensor; that is the coupling step G3 leaves open" | Y |
| 2.3 | GR:24; GR:707 (CC clause); ch02:192/835; Explainer:533; ch18:140/4960, :142/4962, :144/4964 | "is dissolved by…" / "dissolves:" / "gravity couples to the classical substratum" (unconditional) | GR:356 | OVR / NQ | Conditional (C on G3) | Lead with the condition: "is addressed by a conditional proposal: …; the descriptive distinction is established, its gravitational form conditional on the open coupling step" | Y |
| 2.4 | ch07 §7.7: ch07:167/2044, :175/2052, :177/2054 | "The framework dissolves the problem"; "The classical substratum's vacuum energy is the gravitating object" | GR:356; ch07:14 | OVR (the book lags GR:356; the §7.7 body never states the condition) | C | Insert GR:356's condition in §7.7 and make :175 conditional | Y |
| 2.5 | GR:360; ch07:201/2078 | "eliminates the 122-digit cancellation entirely" | GR:356 | OVR | C | "…would eliminate the 122-digit cancellation if the open coupling step holds" | Y |
| 2.6 | GR:338 ("precisely observed"); GR:366; ch07:171/2048; ch07:195/2072; Explainer:549; GR:358 item (1) | "the value the framework expects"; "independent reason to expect" | `cc_indep.py`: ρ_crit is the Friedmann total density; Ω_Λ is an input; GR:360 concedes it is "set by initial conditions" | OVR | Postdiction / normalization | "…the observed density is of the Friedmann scale H²/G, as any O(1) component of a flat universe is; its value is an input" | Y |
| 2.7 | GR:366; ch07:191–193/2068–2070; ch18:142/4962; ch19:330/5506 | "10¹²² = S_dS"; "up to factors of order one"; "a derivable quantity"; "Dissolved (10¹²² = S_dS)" | `cc_indep.py`: the ratio is S_dS times (8/3)(l_p/l_cut)⁴, from 1/(96π²) to 8/3 by cutoff convention | NQ (identity); OVR (ch19:330) | Consistency (dimensional identity) | ch19:330 → "Descriptive distinction; gravitational form conditional (G3)", matching ch19:38 | Y |
| 2.8 | GR:368; ch07:199/2076 | "a triangulation that strengthens the empirical case for both programs" | No empirical content in the cited convergence | OVR (§A.32) | — | Delete the clause | Y |
| 2.9 | GR:581 (§8.3) | the electroweak V(φ_min) shift classed as an "absolute" energy | The GR:579 rule (relative differences between configurations gravitate) does not decide a transition between two configurations | NQ (hidden assumption) | Open | Add: "how the energy of the electroweak and QCD transitions couples is not fixed by the distinction and requires the same open coupling step" | Y |
| 2.10 | appendix-a:113 (G7)/5666; :119 (G14)/5672 | S for a descriptive relation and for a normalization identity | GR:356; G14's own column | OK, with a note | Consistency | No class change; never count these as "predictions matching observation" | Y |
| 3.1 | ch18:349/5169 | "Twenty-two parameter-free SM predictions match observation. Thirteen gravitational… match… Seven neutrino… match" | appendix-a:95, :121, :139, :231; SM:1298 | **INC** | Mixed; mostly Postdiction | Restate appendix-a:231 (text in §3.1) | Y |
| 3.2 | ch19:362/5538 | "preregistered structural predictions matching observation … is met across multiple sectors" | appendix-a:217: "no pre-registered forward confirmation" | **INC** | Postdiction | "…is retrodictive; the pre-registered forward set awaits data" | Y |
| 3.3 | ch19:28/5204 (+ Explainer:699) | "seven independent consistency checks and no fitted parameters" | GR:358 item (7): "three matched parameters … the <0.1% figures are fits" | **INC** | Consistency | "…seven mutually independent consistency relations, one of which (the coupling values) uses three matched parameters" | Y |
| 3.4 | appendix-a:217/5770 and :231/5784 (+ appendix-c:275/6543) | "the [rotational-]anisotropy amplitude" listed as genuinely pre-registered forward content | appendix-a:203 and SM:134: magnitude undetermined, "deliberately not listed as a forward prediction" | **INC** (that clause); the rest of :217 OK | Open | Drop "the anisotropy amplitude" from both lists | Y (new) |
| 3.5 | preface:7/78; appendix-c:275/6543; appendix-c:347/6615, :279/6547 | JUNO "matched at 0.07σ from a prediction made before the measurement"; "a *pre-registered* prediction made before the JUNO measurement"; "tested and confirmed (JUNO…)" | Juno:73; appendix-a:217; README:88; git: form first appears 054eb99a (2026-04-04), after JUNO's November 2025 result | **INC** (preface, appendix-c:275); OVR (:347, :279) | Postdiction (the match); Forward test (design-lifetime precision) | "…matched at 0.07σ by a retrodiction (the derivation postdates the measurement); JUNO's design-lifetime precision is the forward test" | Y (new) |
| 3.6 | ch00:97/333, ch05:13/1340, Explainer:862 ("twenty-two parameter-free/zero-parameter"); ch00:77/313 ("no parameters fit to the retrodicted quantities"); ch04:130/1249; Substratum:228; SM:1456; Structure:142, :56; appendix-c:273/6541 | all 22 called parameter-free or structural; "cosmological constant magnitude" listed as retrodicted | SM:1298 (7 S; 1 E fixes δ₀; R rows use matched (A,B)); GR:360 | OVR (appendix-c:273's CC-magnitude clause: **INC**) | — | "twenty-two classified SM observables (seven parameter-free structural [or the corrected count, §4])" | Y |
| 4 | appendix-a:74/5627 (+ SM:1262, SM:1298, ch06:297/1821, appendix-a:28/5581, :50/5603) | Cabibbo λ = 1/(π√2): "S, Layer 1, 0.04%" | SM:849–851 ("emergent dressing pending"; boson kernel rejected at ≈190σ); git history; PDG 2025 | OVR | Postdiction plus Conditional (C) | "C, Layer 1, 0.04% vs the unitarity-constrained fit (postdiction)"; S counts recomputed in §4.6 | Y |
| 5 | GR:603 vs ch18:164–180/4984–5000 and appendix-a:183 (F5)/5736, :208/5761 | GR: "no OI-specific echo … clean null"; book: "forward empirical signature: GW echoes"; F5 "testable at LVK next observing runs" | GR:603 is the maintained statement; ch18:172/:180 contradict F5 | **INC** (ch18 §18.6 and F5 against GR:603; F5 also against ch18:180) | Open (no derived amplitude) | Rewrite §18.6 to GR:603's statement; retire F5 (ID not reused or renumbered) | Y |
| 6 | GR:567 | "…which is (C4)'s realization — so the equivalence applies in our universe" | GR:20 and GR §2.2: C4 "Not presently discharged"; bidirectional coupling does not supply it | **INC** | Conditional on C4 | "…the application to our universe remains conditional on (C4), which is not discharged at the cosmological cut (§2.2)" | N |
| 7 | GR:711 | "[Main] establishes the equivalence…"; the synthesis "establishes that the SM, GR and the arrow of time are three faces …, with QM emerging as the unique self-consistent description" | Main:22 ("not promoted into a uniqueness theorem"); `oi_alone_not_qm` (kernel); G3 open (GR:12) | **INC** | Conditional / Open | "[Main] establishes a finite-horizon correspondence…; the synthesis proposes…, with the covariant field equations (G3) and the selection of operational QM open" | N |
| 8 | ch19:333/5509 and ch19:64/5240 (anchor scope: Main:632); Main:666 | "Dissolved (Bayesian updating)"; "applies to all the variants … at once"; "The Everettian measure problem dissolves" | Main:632: Lüders = Bayesian updating for the represented diagonal sector only; noncommuting interventions need the completion conditions | OVR (ch19); NQ (Main:666) | Open (interpretation) | ch19:333 → "Interpretation: fixed-basis records as Bayesian updating; coherent interventions under the completion conditions" | N |
| 9 | Substratum:356 (+ Explainer:930, ch02:196/839) | "No additional axiom is needed" | Main:728 calls (EM) "an explicit physical hypothesis"; Substratum:354: the clock is monotone only while ä > 0 | OVR | Conditional on (EM) | "…grounds in horizon growth (during ä > 0) and the observer-selection rule, which is conditional on (EM) and its rate condition" | N |
| 10 | Main:726 (+ Main:740 last two sentences, Substratum:56, :350, Complexity:204, Explainer:930, ch02:196/839) | "The rule replaces … the 'past hypothesis' … with a theorem conditional on (EM)" | Main:730–740: the selection rule needs (EM) and τ_mix ≪ τ_S; Main:740 says (EM) at that rate "is itself a physical hypothesis" | OVR | Conditional (the rule); Open (any replacement of the past hypothesis) | "…a selection rule on where observers can exist…; it does not supply the low-entropy initial condition, whose role in the direction of the arrow it leaves open" | N (coordinator addition) |
| 11 | ch19:339/5515; ch19:116/5292, :118/5294 | "Derived (total budget)"; "The framework derives the total budget" | G9: C, "Partly definitional budget"; ch19:116 itself: "equal to 1−Ω_B by construction" | OVR | Consistency (definitional) | "Concordance (total = 1−Ω_B by construction; split not derived)" | N |
| 12 | GR:709 | "The dark-sector corollary explains ~95% of the gravitational budget" | GR:358 item (4); G9 | OVR | Consistency | "…accounts for the ~95% as 1−Ω_B, which is partly definitional" | N |
| 13 | ch00:89/325 | "the MOND scale a₀ = cH/6 as a parameter-free prediction" (also "the 1/4 factor as a derivation"; "all follow from the single statement…") | G6: C, factor 1/6 imported from Verlinde; GR:12: the open coupling map; two tensions | OVR | Conditional, with an imported factor | "…a₀ = cH/6, conditional on the open coupling map and with the 1/6 taken from Verlinde" | N (1/4 clause: Y) |

Counts by defect class, over the 29 rows above:

- **INCORRECT: 11** (1.5, 1.6, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5, 5, 6, 7).
- **INCORRECT clauses inside mixed rows: 2.** Row 1.2 (the "postulate" premise) and row 3.6 (appendix-c:273's CC-magnitude clause).
- **OVERSTATED: 15** (1.1, 1.2, 1.3, 1.4, 2.2, 2.3, 2.4, 2.5, 2.6, 2.8, 4, 8, 9, 10, 11, 12, 13, 3.6). Row 1.2 is
  counted here and as an INCORRECT clause above.
- **NEEDS-QUALIFICATION: 4** (1.7 for GR:320, 1.8, 2.7, 2.9).
- **CONSISTENT: 1** (2.10).

Rows 1.5, 1.6, 3.4 and 3.5 were not in the input audit's §9.

***

## 1. Horizon entropy: ħ and the 1/4 coefficient (owner-named)

### 1.0 The decisive check (`quarter_indep.py`, independent of `quarter.py`)

GR's inputs:
- first law dE = c²κ dA/(aG), with a = 8π (GR:98);
- KMS temperature k_BT_Q = ħκ/(bc), with b = 2π (GR:148);
- mode density η = κ_mσ/ε² (GR:98, :104);
- calibration T_cl = T_Q (GR:150).

Results:

| # | Check | Result |
|---|---|---|
| 1 | S/(A/l_p²) after the calibration, with ħ solved from it | **b/a**; independent of ε, σ and κ_m. At a = 8π, b = 2π: **1/4** |
| 2 | Measured ħ held fixed; calibration solved for η | η = (b/a)/l_p² = 1/(4l_p²), so ε = 2√σ·l_p. Only ε/√σ is fixed |
| 3 | η an arbitrary positive function f(ε,σ) | b/a. The coefficient is an identity in η |
| 4 | 50 random exact rational mode densities | coefficient set {1/4} |
| 5 | Countercontrol: a = 16π, or b = π | 1/8 in both cases, so the test is not vacuous |
| 6 | Countercontrol: no calibration, ε = l_p, σ = 1 | S = A/l_p². The count alone carries no 1/4 |
| 7 | Hawking route, no mode count: dS/dA = (dE/dA)/T_H | l_p²·dS/dA = b/a = 1/4 |
| 8 | Transcription control | ħ = c³ε²/(4Gσ) matches the box at GR:154 |

**Verdict: confirmed.**
- Once the calibration is imposed, S = A/(4l_p²) holds for every ε and σ (indeed for every mode density).
- The coefficient is b/a = **2π/8π**: the KMS period over the first-law prefactor.
- It is the same identity by which T_H plus the first law fixes the Bekenstein–Hawking coefficient (check 7).
- The calibration fixes one relation, ε/√σ = 2l_p, and nothing else.
- GR itself says so twice:
  - GR:104: "the entropy law is a fixed point of the construction regardless".
  - GR:320: "The factor of 4 in ε² = 4σl_p² traces directly to §3 Step 4's thermal matching".

Line-reference check for the coordinator: the 2π/8π identity is at **GR:320**. GR:322 is the GW250114 paragraph. It
does carry two of the quoted phrases, "a derived structural constant" and "the coefficient is equivalent to the
Hawking-temperature normalization (T = ħκ/2πck_B plus the first law fixes it)". The input audit's "GR:320–322" is
therefore right about the phrases but wrong to cite both lines for the identity.

**Pressure test (§A.31, favourable reading).**
- Does the count contribute anything? It contributes the area proportionality and the identification S = ηA. It
  contributes nothing to the 1/4.
- Is "Derived" defensible in the owner's sense? The relation follows from stated inputs by a complete argument. Those
  inputs include the open H-slope condition, and the KMS and first-law normalizations whose ratio *is* the coefficient.
- Status therefore: **Consistency** (it agrees with Hawking's semiclassical result and does not independently predict
  it), **conditional** on H-slope and the horizon/frame conditions. Corpus class C, Layer 1, as G4 already has it.

### 1.1 "…the 1/4 coefficient by direct boundary-mode counting" — OVERSTATED
- **GR:12 (verbatim):** "…and obtains the Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ including the $1/4$ coefficient
  by direct boundary-mode counting — the three conditional on the infrared detailed-balance condition H-slope (§3.2) …,
  the counting $S = \sigma A/\epsilon^2$ itself unconditional…". GR is not mirrored in FULL.
- **Defect.** It attributes to the count what the calibration supplies (checks 1, 3 and 6). Mode counting at the
  calibrated cell size does return A/4l_p², so the sentence is not false. But it locates the coefficient's origin in the
  wrong step: claim/evidence boundary, "available → derived".
- **Paraphrases with the same defect:**
  - GR:707 "follows by direct mode counting, with the 1/4 coefficient fixed as the ratio…";
  - Substratum:324;
  - ch02:112/FULL:755 "follows as a consequence of the same mode-counting analysis";
  - ch02:192/835 "follows from direct mode counting";
  - ch03:118/994 "from boundary mode counting";
  - ch06:348/1872;
  - ch00:81/317 "obtains the 1/4 factor from mode counting";
  - ch07:90/1967 "a direct consequence of ε = 2√σ l_p … by boundary-mode counting";
  - Structure:452 "in OI by mode counting";
  - glossary:17/6639;
  - ch07:12/1889, which is #936's line (§5).
- **Replacement (GR:12):** "…and recovers the Bekenstein–Hawking entropy S = A/(4l_p²): with the calibration the
  boundary-mode count σA/ε² equals A/(4l_p²) for every ε and σ, the coefficient 1/4 being the ratio 2π/8π of the KMS
  period to the first-law prefactor — the three conditional on … H-slope …, the counting S = σA/ε² itself
  unconditional…"
- **Rationale.** The replacement keeps the conditions and the unconditional count, and moves the 1/4 to the step that
  produces it. It is GR:24's own wording, which is the maintained anchor.

### 1.2 "becomes a derivation rather than a postulate" — the premise is INCORRECT; "derivation" is OVERSTATED
- **ch00:21/257 (verbatim):** "The Bekenstein-Hawking factor of $1/4$ becomes a derivation rather than a postulate."
- **Same claim elsewhere:**
  - preface:7/78: "…becomes a derivation."
  - ch00:89/325: "the Bekenstein-Hawking $1/4$ factor as a derivation".
  - ch00:81/317: "…in the standard account the factor is a postulate."
  - glossary:17/6639: "The factor of $1/4$ is conventionally treated as a postulate of black-hole thermodynamics. The
    framework *derives* the $1/4$ factor as a structural consequence of mode counting…".
- **Defect.** The standard account does not postulate the 1/4. Hawking's T_H with the first law fixes it, and the
  corpus says so itself at GR:322: "T = ħκ/2πck_B plus the first law fixes it". The framework's route is the same
  identity (check 7). "Becomes a derivation" therefore claims a change of status that does not occur. That is
  "conditional → unconditional" plus a false contrast with the literature.
- **Replacement (ch00:21):** "The Bekenstein–Hawking factor 1/4 is recovered as a consistency relation between the
  classical and emergent horizon temperatures, conditional on the horizon conditions of Chapter 7; it has no direct
  test."
- **Replacement (glossary:17):** "…The factor 1/4 follows from the Hawking temperature and the first law. In the
  framework it is the ratio 2π/8π fixed by the horizon calibration of Chapter 7 (conditional on H-slope); the mode
  count reproduces it for any cell size once the calibration is imposed."

### 1.3 "a derived structural constant" — OVERSTATED
- **GR:322 (verbatim):** "The coefficient, fixed here as the exact ratio $2\pi/8\pi$ … is a derived structural
  constant with no direct empirical test at present…"
- **Same wording elsewhere:**
  - ch07:104/1981 (same sentence);
  - GR:707: "a structural constant rather than an empirical fit";
  - appendix-c:275/6543 and ch09:333/2813: "is derived but has no direct empirical test".
- **Defect.** "Derived" drops the H-slope condition. The coefficient is the ratio of the two input normalizations, not
  an output of the substratum.
- **Replacement:** "…is the ratio of the two normalizations that the calibration matches, conditional on H-slope and
  the horizon and frame conditions, with no direct empirical test at present." "Not an empirical fit" may stay.

### 1.4 "Any alternative ħ(ε) would fail at least one of these checks" — OVERSTATED (circular)
- **GR:162 (verbatim):** "The predictive content lies not in the gap equation alone but in its consequences. The specific
  relationship … produces: the Bekenstein-Hawking formula with the exact factor $1/4$ (§5), the CC dissolution with
  $S_{\text{dS}}$ as the compression ratio (§6.3), and the Type II running-vacuum form … (§7.1). Any alternative
  $\hbar(\epsilon)$ would fail at least one of these checks."
- **Mirrors:** ch07:63/1940; Explainer:477 and :1043.
- **Defect.** None of the three "checks" constrains the calibration independently of the calibration itself:
  - the 1/4 is satisfied by construction by whatever β the KMS and first-law normalizations fix (§1.0);
  - the S_dS ratio holds up to an O(1) factor that depends on the cutoff convention (§2.7);
  - GR:12 itself says the RVM form "is the local expansion shared by every smooth model".
- **Replacement:** delete the "predictive content … would fail" sentence. If one is wanted: "The three relations share
  the calibration; they are consequences of it, not independent checks of it."

### 1.5 GR:164 — "recovered as a prediction, not used as an input": INCORRECT (new)
- **GR:164 (verbatim):** "The Gibbons-Hawking temperature [2] $k_B T_{\text{GH}} = \hbar \kappa / (2\pi c)$ is recovered
  as a prediction, not used as an input." The same sentence is at ch07:65/1942.
- **Defect.** GR:148, Step 4, uses exactly this temperature as its input: "giving a KMS state at
  $T_Q = \hbar\kappa/(2\pi c k_B)$ with $\hbar$ unknown". Under the calibration T_cl = T_Q, T_cl equals T_GH
  identically.
- **Replacement:** "The Gibbons–Hawking form ħκ/(2πc) enters as the KMS temperature of Step 4; the calibration fixes
  the value of ħ in it."

### 1.6 ch18:160 — the 1/4 among "predictions … that neither QM nor GR alone makes": INCORRECT (new)
- **ch18:160/4980 (verbatim):** "The empirical content of the framework's treatment is in the predictions it makes that
  neither QM nor GR alone makes: the Bekenstein-Hawking $1/4$ coefficient, the dark sector concordance, the value of
  $\hbar$ from partition geometry, the running-vacuum dark-energy form, the MOND acceleration scale, and the
  gravitational wave echoes developed in the next section."
- **Defect.** Each listed item fails as stated:
  - QM on a GR background yields the 1/4 (check 7);
  - ħ is not predicted (only ε/√σ is fixed, GR:310);
  - the RVM form is shared by every smooth model (GR:12);
  - the dark-sector total is partly definitional (G9);
  - echoes contradict GR:603 (§6 below).
- **Replacement:** "…The framework's treatment carries conditional and consistency relations (the horizon calibration,
  the descriptive vacuum-energy distinction, the dark-sector reading) rather than predictions independent of QM and
  GR; its forward exposure is listed in Appendix A.5." The echo clause must go in any case (§6).

### 1.7 History of the coefficient
- **GR:320 (verbatim):** "The factor of $1/4$ in the Bekenstein-Hawking formula — historically introduced as a
  proportionality constant — is here fixed, under the conditions of the §3 calibration…"
  - **NQ.** Bekenstein (1973) did leave the coefficient undetermined, but Hawking (1975) fixed it **[mem; consistent
    with GR:322's own statement]**.
  - **Replacement:** "…introduced by Bekenstein with an undetermined coefficient and fixed by the Hawking temperature
    and the first law — is here recovered, under the conditions of the §3 calibration, as…"
  - The rest of GR:320 is the maintained anchor: "…not an arbitrary constant but the consistency condition between
    gravitational and quantum thermal physics, conditional on H-slope". Keep it.
- **Explainer:521:** "which Bekenstein and Hawking introduced as a proportionality constant in 1973". **OVR.**
- **Explainer:523:** "The 1/4 factor has been a mystery for 50 years…". **OVR.**
- **ch07:90/1967:** "historically unexplained constant … Standard derivations … treat the $1/4$ coefficient as either
  fitted to thermodynamic consistency…". **OVR.** The framework's own route *is* fixing the coefficient by thermodynamic
  consistency.
- **Replacement (Explainer:523 and ch07:90):** state that the standard derivation fixes 1/4 from T_H and the first law,
  and that the framework reproduces the same ratio from its calibration.

### 1.8 appendix-a G4 and row 24 — the class is correct; NQ on the empirical column
- **Verbatim:**
  - :110 "| G4 | Bekenstein-Hawking coefficient | $1/4$ | C | 1 | No direct test | Ch 7 §7.5 |";
  - :93 "| 24 | Bekenstein-Hawking entropy | $S = A/(4 l_p^2)$ | C | 1 | No direct test | Ch 7 §7.5 |".
- **Assessment.**
  - C (conditional on H-slope) is accurate. The input audit's proposal to reclassify the entry as an "identity" like
    G14 is a presentational choice, not a correction.
  - Minimal change: empirical column "Consistency relation; no direct test".
  - **Counts unchanged:** 13 gravitational and 24 in A.4.1.
  - Owner decision: whether a consistency relation belongs in a "prediction status" table at all. If it is removed,
    A.4.1 becomes 23 and the gravitational table 12, and every "thirteen gravitational-sector entries" site (§3.6
    list) changes.

***

## 2. Cosmological constant (owner-named)

### 2.0 Checks
- **GR:583 against GR:356: the contradiction is confirmed.**
  - GR:356 (verbatim): "Quantum transition data are invariant under $\Omega_{\rm eff}\to\Omega_{\rm eff}+CI$ (a global
    phase), so no ordinary observer statistic detects $C$; yet two gravitational completions,
    $\mathcal G_{\mu\nu}=8\pi G T^{\rm cl}_{\mu\nu}$ and $\mathcal G_{\mu\nu}=8\pi G(T^{\rm cl}_{\mu\nu}-\rho_Cg_{\mu\nu})$,
    can share the same substratum, partition, reduced transition law, fixed-basis representation and action-scale
    calibration while differing in exactly that offset. Invisibility to quantum mechanics is not decoupling from
    gravity; the latter is a coupling theorem and is what G3 names as open."
  - GR:583 (verbatim): "…it is a theorem of the reconstruction. An additive energy shift preserves every visible
    transition probability exactly (§3.3): the uniform offset of $\hat H$ is a gauge parameter of the marginalization …
    and the problem's premise (that this offset is a physical energy awaiting gravitational response) attributes
    physical content to a gauge degree of freedom."
  - GR:356 exhibits two completions with identical quantum data that differ in whether the offset gravitates. GR:583
    infers from quantum invisibility that the offset has no gravitational content. GR:356 refutes exactly that
    inference.
- **ρ ~ H²/G is the Friedmann normalization, not an output** (`cc_indep.py`).
  - ρ_crit = 3H²c²/(8πG) = 7.67×10⁻¹⁰ J/m³ at H₀ = 67.4. It is the *total* density of a flat universe. Any component
    with Ω = O(1) sits at "H²/G".
  - Ω_Λρ_crit = 5.25×10⁻¹⁰ J/m³ needs Ω_Λ ≈ 0.685 as an input.
  - GR:360 concedes the point: "The framework does not explain *why* ρ ~ H²/G; this is set by initial conditions via the
    Friedmann equation."
  - GR:338 ("precisely observed") and GR:366 ("the value the framework expects") restate a normalization as an
    expectation.
- **10¹²² = S_dS is a dimensional identity.**
  - (ρ_P/ρ_crit)/S_dS = 8/3 exactly, with no H dependence.
  - With a cutoff at ε: 8/3·(l_p/ε)⁴, which is 1/6 at ε = 2l_p.
  - With the explicit one-field zero-point integral cut at ε = 2l_p: 1/(96π²) ≈ 1.1×10⁻³.
  - Numbers: S_dS = 2.27×10¹²²; ρ_P/ρ_crit = 6.04×10¹²².
  - ch07:193's "up to factors of order one" spans about 10⁻³ to 3 depending on convention (NQ). It holds for any theory
    with a Planck cutoff and a Hubble-scale density.

### 2.1 GR:583 — INCORRECT
- **Wording:** quoted in §2.0.
- **Paraphrases:**
  - GR:585: "The dissolution applies to each for the same reason — gravity operates at the classical level (§6.2)…";
  - GR:587: "…and therefore does not source curvature".
- **Replacement (GR:583):** "*The reconstruction-gauge form of this claim.* An additive energy shift preserves every
  visible transition probability exactly (§3.3): the uniform offset of Ĥ is a gauge parameter of the marginalization,
  present in no visible transition statistics at any precision. The embedded observer's quantum data therefore contain
  no fact about the absolute zero-point offset. Whether the offset sources curvature is not settled by this invariance;
  it is the coupling question that §6.2 leaves open at Level G3. The scope of the argument is …[unchanged]."
- **GR:585 and :587:** prefix "On the geometry-first proposal of §6.2, conditional on the open coupling step,".

### 2.2 GR:356, final sentences — OVERSTATED (§A.30 assert-then-qualify)
- **Verbatim:** "…In the present framework, the zero-point sum is an artifact of the emergent description and never
  enters the stress-energy tensor; no decoupling mechanism is needed."
- **Replacement:** "In the present framework the zero-point sum belongs to the emergent description; that it does not
  enter the stress-energy tensor is the geometry-first proposal of this section, and establishing it is the coupling
  step that G3 leaves open."

### 2.3 Unconditional "dissolved/dissolves" — OVERSTATED or NQ
- **GR:24 (verbatim):** "The cosmological constant problem is dissolved by identifying … (§6); the descriptive
  distinction is established and the dynamical form of the dissolution is conditional on the G3 coupling theorem (§6.2)."
  **NQ**: the lead verb asserts, then the clause qualifies. Replacement: "The cosmological constant problem is addressed
  by identifying …; the descriptive distinction is established, and the dissolution is conditional on the G3 coupling
  theorem (§6.2)."
- **GR:707**, CC clause: "dissolved at the descriptive-levels register, … not a failure of cancellation". **NQ.** Append
  "conditional on the coupling step".
- **ch02:192/835:** "The cosmological constant problem dissolves:". **OVR.** Replacement: "The cosmological constant
  problem receives a conditional treatment: … are properties of logically distinct levels of description; the
  dissolution is conditional on the covariant coupling step (Chapter 7)."
- **Explainer:533:** "Now the cosmological constant problem dissolves." **OVR.**
- **ch18:140/4960, :142/4962, :144/4964:** "each dissolving when the geometry-first ordering is adopted"; "gravity
  couples to the classical substratum"; "a derivable quantity". **OVR.** Add the G3 condition, as ch18:160 already does.
- **Kept (legitimate):** ch19:38/5214 (the anchor), ch07:14/1891, ch07:315/2192, ch09:14/2494, ch09:48/2528, SM:1576,
  ch19:30/5206.

### 2.4 ch07 §7.7 body — OVERSTATED (the book lags GR:356)
- **Verbatim:**
  - ch07:167/2044: "The framework dissolves the problem rather than solving it."
  - ch07:175/2052: "The classical substratum's vacuum energy is the gravitating object; the emergent QFT's vacuum energy
    is bookkeeping…"
- **Defect.** No line of §7.7 (ch07:163–201) states the coupling condition. Grep for
  conditional/G3/"coupling theorem" in that range returns nothing. ch07:14/1891 states the condition only in the
  chapter overview. This is the §A.25 "book lags paper" pattern.
- **Replacement:**
  - ch07:167: "The framework proposes a dissolution rather than a solution. … The descriptive distinction is
    established; that the zero-point sum does not source curvature is the covariant coupling step that [GR §6.2] leaves
    open, so the dissolution is conditional on it."
  - ch07:175: "On this proposal the classical substratum's vacuum energy is the gravitating object…"

### 2.5 "eliminates the 122-digit cancellation entirely" — OVERSTATED
- **Sites:** GR:360 and ch07:201/2078.
- **Replacement:** "Conditional on the coupling step, the framework removes the need for the 122-digit cancellation;
  the remaining question…"

### 2.6 ρ ~ H²/G "expected" — OVERSTATED
- **GR:366 (verbatim):** "This is not a prediction awaiting future data — the observed vacuum energy sits at the
  classical geometric scale $\rho \sim H^2/G$, the value the framework expects."
- **Also:**
  - Explainer:549: "…sits exactly at the classical geometric scale — the value the framework expects … there is nothing
    to cancel";
  - ch07:195/2072: "the structural quantity that the framework has independent reason to expect";
  - GR:338 and ch07:171/2048: "precisely observed" / "precisely what is observed";
  - GR:358 item (1): "the observed vacuum energy sits at ρ ~ H²/G, the classical baseline, without fine-tuning".
- **Replacement (GR:366):** "…The observed vacuum energy is of the Friedmann scale H²/G, as is any O(1) component of a
  flat universe; its value is set by initial conditions (below), so this is a normalization, not a prediction."
- **Status:** normalization, which by the owner's classes is Postdiction or Consistency.

### 2.7 10¹²² = S_dS — NQ (identity); ch19:330 OVERSTATED
- **ch19:330/5506 (verbatim):** "| Cosmological constant | Worst prediction in physics | Dissolved ($10^{122}$ =
  $S_{\text{dS}}$) | Ch 7 §7.7 |"
- **Replacement:** "| … | Descriptive distinction established; gravitational form conditional (G3) | … |", matching the
  anchor ch19:38.
- **GR:366, ch07:191–193 and ch18:142:** add "a dimensional identity for any Planck-cutoff theory, holding up to a
  convention-dependent factor".

### 2.8 Triangulation — OVERSTATED (§A.32)
- **GR:368 and ch07:199/2076:** "a triangulation that strengthens the empirical case for both programs". Delete the
  clause. No empirical content is cited.

### 2.9 Phase-transition vacuum energy — NQ (hidden assumption, confirmed)
- **The rule (GR:579):** "Relative energy differences between configurations of the emergent fields … gravitate".
- **The classification (GR:581):** V(φ_min) is placed in the "absolute" class.
- **Why the rule does not decide it:** the electroweak and QCD transitions are differences between two configurations
  occupied at different epochs, so by GR:579's wording they are relative. GR:581's classification is an added
  assumption.
- **Add after GR:585:** "How the energy released in the electroweak and QCD transitions couples to gravity is not fixed
  by the relative/absolute distinction and requires the same open coupling step."

### 2.10 G7 and G14 class S — CONSISTENT, with a note
- G7 "Descriptive relation" and G14 "Normalization identity" are correctly described in their own empirical columns.
- The defect lies only in summaries that count them as predictions matching observation (§3.1).
- No class change; counts unchanged.

***

## 3. Standard Model and sector prediction counts (owner-named)

### 3.1 ch18:349 — INCORRECT
- **Verbatim (ch18:349/5169):** "Twenty-two parameter-free Standard Model predictions match observation. Thirteen
  gravitational-sector predictions match observation. Seven neutrino-sector predictions match observation."
- **Support:**
  - SM:1298: 7 of 22 are S. One E row fixes δ₀ from the U(1) coupling, and the R rows use matched (A,B).
  - appendix-a:121: the 13 gravitational entries are 2 S + 9 C + 2 L. Their empirical column reads conditional
    calibration, order-of-magnitude estimate, no direct test, not observed, partly definitional, scrambling open, upper
    bounds only, interacting protection open, and normalization identity. Only G6 ("within quoted systematics") and G8
    ("consistent at 2σ") are data comparisons.
  - appendix-a:139: N4 has upper bounds only; N7 makes no value commitment.
- **Replacement**, from appendix-a:231, the maintained statement: "Of the twenty-two Standard Model observables, seven
  are parameter-free structural retrodictions [corrected count: §4.6] and the remainder are layered, chained or fitted;
  the thirteen gravitational-sector entries are conditional relations, identities and estimates, two of them compared
  with data; the seven neutrino-sector entries include retrodictions and bound-only comparisons."
- The echo clause in the next sentence ("gravitational wave echoes") must go (§6).

### 3.2 ch19:362 — INCORRECT
- **Verbatim (ch19:362/5538):** "…The framework's evidential standard — preregistered structural predictions matching
  observation at the current empirical precision — is met across multiple sectors of physics with a uniformity that
  distinguishes it from frameworks tuned to fit specific empirical targets."
- **Support:** appendix-a:217: "The framework currently has no pre-registered forward confirmation. Its strongest
  empirical content is retrodictive". Also SM:1333.
- **Replacement:** "The record is retrodictive: the structural values match existing data at the precisions classified
  in Appendix A, and the pre-registered forward set (Appendix A.6) awaits its data." Also "seven neutrino-sector
  predictions" → "entries", and "record of resolved problems" → "record".

### 3.3 ch19:28 — INCORRECT
- **Verbatim (ch19:28/5204):** "The framework produces the quantum and gravitational sectors from the same axioms with
  seven independent consistency checks and no fitted parameters — the quantum representation under the translation
  hypothesis (T) ([Main §3.4]), and the gravitational results at the G1/G2 rungs."
- **Support.** The "seven" is GR:358's "seven of the entries are mutually independent". Its item (7) reads: "the three
  coupling values at M_Z being reproduced through three matched parameters (δ₀, A, B), so that the < 0.1% figures are
  fits". Item (6) imports the factor 1/6, and item (4) is partly definitional.
- **Replacement:** "…with seven mutually independent consistency relations ([GR §6.2]), one of which reproduces the
  coupling values through three matched parameters."
- **Paraphrase:** Explainer:699: "seven of them mutually independent". Keep the number and add the same caveat.

### 3.4 appendix-a:217 and :231 — one clause INCORRECT; otherwise the anchor
- **Verbatim, :217:** "The genuinely pre-registered content is forward-looking — DESI Y5 ($\nu$), the anisotropy
  amplitude, BTFR at $z > 1$, the A2 lattice thresholds, and JUNO design-lifetime precision…"
- **Verbatim, :231:** "(DESI Y5 $\nu$, the rotational-anisotropy amplitude, BTFR at $z>1$, …)".
- **Contradiction:**
  - appendix-a:203/5756: "The *rotational* Lorentz sector is deliberately **not** listed as a forward prediction … its
    magnitude is undetermined";
  - SM:134: the rotational E_g anisotropy is "in a more precarious position".
- **Replacement:** delete "the anisotropy amplitude" and "the rotational-anisotropy amplitude" from both lists, and
  from appendix-c:275/6543 ("DESI Y5, the anisotropy amplitude, …").
- The remainder of :217 ("no pre-registered forward confirmation … retrodictive") is accurate and is the anchor for
  §3.1 and §3.2.

### 3.5 JUNO "before the measurement" — INCORRECT
- **Verbatim, preface:7/78:** "The JUNO neutrino mixing angle is matched at $0.07\sigma$ from a prediction made before
  the measurement."
- **Verbatim, appendix-c:275/6543:** "JUNO solar mixing angle at 0.07$\sigma$ against the post-JUNO global fit — a
  *pre-registered* prediction made before the JUNO measurement. … but it is a retrodiction — the derivation postdates
  the measurement." This is assert-then-qualify (§A.30).
- **Support:**
  - Juno:73: "This derivation was carried out in 2026, after the JUNO first results";
  - appendix-a:217; README:88; ch00:21.
  - Git: `1/3 − 1/(4π²)` and 0.3080 occur in no tree before `054eb99a` (2026-04-04). I searched the parent tree for
    `1/(4\pi^2)`, `4\pi^2}`, `0.3080` and `0.30798`.
- **Also OVR:** appendix-c:347/6615 "tested and confirmed (JUNO, GW250114, Rett)" and appendix-c:279/6547.
- **Replacement (preface:7):** "The JUNO solar mixing angle is matched at 0.07σ by a parameter-free retrodiction — the
  derivation postdates the measurement — and JUNO's design-lifetime precision is a pre-registered forward test."
- **Status:** Postdiction for the match; Forward test for the precision test.

### 3.6 "Twenty-two parameter-free", and related paraphrases — OVERSTATED
- **Sites:**
  - ch00:97/333 and ch05:13/1340: "the twenty-two parameter-free retrodictions";
  - Explainer:862: "twenty-two zero-parameter quantitative predictions";
  - ch00:77/313: "with no parameters fit to the retrodicted quantities". SM:1298 restricts that statement to S and L;
    the R rows are fitted;
  - ch04:130/1249: "no adjustable parameters beyond a small acknowledged empirical input set" (borderline; keep, with
    "and three matched coupling parameters");
  - Substratum:228: "twenty-two structural retrodictions … each at ≲ 1σ";
  - SM:1456: "the twenty-two structural predictions of §7";
  - Structure:142: "twenty-two structural retrodictions in [SM §7] and [GR §7]". The 22 are SM only;
  - Structure:56: Cabibbo "at 0.05σ". SM:841 gives 0.12σ;
  - ch07:8/1885.
- **appendix-c:273/6541:** "Thirteen gravitational-sector observables (Bekenstein-Hawking entropy coefficient, MOND
  acceleration scale, cosmological constant magnitude, etc.)" listed as retrodicted. The CC-magnitude clause is
  **INCORRECT** (GR:360: the value is set by initial conditions and not explained).
- **Replacement pattern:** "twenty-two classified SM observables (seven parameter-free structural [corrected: §4.6]; the
  remainder layered, chained or fitted)". This is the wording of ch09:8 and ch02:228, which are correct as written,
  apart from the "seven" if §4 is adopted.

***

## 4. Cabibbo classification: appendix-a:74, S versus C (owner-named)

### 4.1 Source
- **Verbatim:** appendix-a:74/5627 "| 5 | Cabibbo $\lambda$ | $1/(\pi\sqrt{2})$ | S | 1 | 0.04% | Ch 6 §6.4 |".
- **Same status elsewhere:**
  - SM:1262 (S); SM:1298 ("7 are unconditional parameter-free structural predictions");
  - ch06:297/1821 (S, Cat A); ch06:318/1842 ("S = unconditional structural");
  - appendix-a:28/5581 (Cabibbo cited as an S example); appendix-a:50/5603 (Layer-1 example).

### 4.2 Support (SM:837–851)
- **Solid:** corner geometry π√2; the 1/|q| power, from chirality preservation in the staggered-fermion literature.
- **SM:849 (verbatim):** "This is a hypothesis, not a derivation … the unit prefactor … and the selection of the
  adjacent-corner distance (rather than another invariant of the same corner set) are commitments of the hypothesis
  rather than consequences of the geometry … the empirical match at $0.04\%$ confirms the commitment but does not
  derive it". The status is then raised to "established at the structural level", with "emergent dressing pending".
- **SM:851:**
  - The unit prefactor is "an algebraic identity of the staggered spin-taste map, with the finite computation serving as
    its witness. What remains beyond this structural level is the emergent-theory dressing."
  - The dispersion choice is discriminated against data: "the substrate boson kernel gives λ = 1/(2√2) = 0.3536,
    excluded by the measured Cabibbo angle at ≈190σ; the substrate fermion kernel is singular there; the emergent
    continuum dispersion gives λ = 1/(π√2) exactly".
  - My check: (0.35355 − 0.22500)/0.00067 = 192σ.

### 4.3 Dating (git log -S, full history)
- `\frac{1}{\pi\sqrt{2}}`, `1/(\pi\sqrt{2})`, `0.22508` and the comparison "0.2250 ± 0.0007 … 0.04%" all first appear
  **together** in `054eb99a` (2026-04-04 16:16, `Predictions.md` lines 51–55: form, value and "Observed … Match:
  0.12σ (0.04%)" in one commit).
- `git grep` over all 507 earlier commits finds no `π√2`, `pi\sqrt{2}` or "Cabibbo" anywhere, so no pre-comparison
  registration exists. The repository begins 2026-02-12.
- `054eb99a` justified the 1/|q| power with "because the generations are fermions". The chirality argument came later.
- `c_\lambda` first appears in `70ffe82f` (2026-07-05). The boson-kernel rejection (`190\sigma`, `0.3536`) first appears
  in `3124ef0a` (2026-07-06), confirmed by a `git grep` of `70ffe82f^`. Both are three months after the comparison.
- **The input audit's dating claim is confirmed.**

### 4.4 Agreement figure (PDG 2025, read first-hand; `cabibbo_cmp.py`)
1/(π√2) = 0.225079079.

| PDG 2025 quantity | Value | Pull | Relative |
|---|---|---|---|
| Global-fit λ, unitarity imposed, CKMfitter method, Eq. (12.26) | 0.22501 ± 0.00068 | 0.10σ | 0.031% |
| Global-fit λ, UTfit prescription | 0.22497 ± 0.00070 | 0.16σ | 0.049% |
| \|V_us\| from Kℓ3, f₊(0) with N_f = 2+1+1 | 0.2233 ± 0.0005 | **3.6σ** | 0.80% |
| \|V_us\| from Kμ2/πμ2, f_K/f_π | 0.2250 ± 0.0004 | 0.20σ | 0.035% |
| \|V_us\| PDG average, Eq. (12.8), error scaled by χ² = 2.5 | 0.22431 ± 0.00085 | 0.90σ | 0.34% |
| \|V_us\| from τ decays | 0.2207 ± 0.0014 | 3.1σ | 2.0% |

- PDG notes "a 2.3σ tension with unitarity in the 1st row".
- **Reading.** The "0.04%" figure holds against the unitarity-constrained global fit, which SM's cited PDG-2022 value
  also is. Against PDG's own direct |V_us| average the agreement is 0.34% (0.9σ), and against Kℓ3 alone it is 3.6σ.
- The quoted precision is therefore determination-dependent. The table should name the global fit as its source (NQ).
- This confirms the input audit's AW-10, which it had marked "[web], unverified".

### 4.5 Defect and class
- **OVERSTATED.**
  - AGENTS's S requires "chain walks end-to-end with all links Solid". SM:851 leaves the emergent dressing open.
  - appendix-a's own A.2 S definition ("fully determines the prediction's content … first-principles derivations") is
    likewise not met.
  - SM:1298's "unconditional" is contradicted by SM:851 and SM:1310 ("leaving the emergent-theory dressing as its
    residual open element").
- **Owner's classes:**
  - **Postdiction**: the form and its comparison were introduced together; λ has been known since 1963; one alternative
    was discarded against the measurement.
  - **Conditional** on the emergent dressing, together with the cubic commitment and H-link.
  - Corpus class: **C**, Layer 1.
- **Pressure test.**
  - SM's own S definition, "no fitted input" (SM:1255), *is* met: no continuous parameter is fitted.
  - So the defect is specifically the word "unconditional" and the AGENTS/appendix-a S definition. It is not a claim
    that a parameter was fitted.
- **Minimal replacement (appendix-a:74):** "| 5 | Cabibbo λ | 1/(π√2) | C | 1 | 0.04% (global fit; postdiction) | Ch 6
  §6.4 |"
- **SM:1262:** S → C; add "C = conditional" to SM:1255's legend. SM's table has no C class now.
- **SM:849:** replace "established at the structural level rather than merely hypothesized" with "the unit prefactor is
  established at the structural level; the emergent dressing is open, so the prediction is conditional on it".

### 4.6 Recomputed counts
|V_cb| = Aλ² (appendix-a row 7: "Conditional on 5,6") and sin²θ₁₃ = A⁴λ² (SM:1317, :1325; ch06:312) both inherit λ, so
both become C by the weakest-link rule. m_d/m_s inherits λ too but is already L.

| Inventory | Current | Corrected (Cabibbo and its two inheritors → C) | If the same rule also reaches the Koide amplitude (SM:895: "not yet derived from the dynamics — one-loop … undershooting") |
|---|---|---|---|
| SM §7.6, 22 observables | 7 S + 6 L + 3 R + 2 E + 3 M + 1 P | **4 S + 3 C** + 6 L + 3 R + 2 E + 3 M + 1 P | 2 S + 5 C + … (Koide Q and θ₀ → C) |
| appendix-a A.4.1, 24 rows | 8 S + 3 C + 8 L + 1 M + 2 R + 2 E | **5 S + 6 C** + 8 L + 1 M + 2 R + 2 E | 3 S + 8 C + … |
| appendix-a A.4.3, 7 rows | 2 S + 5 L | **1 S + 1 C + 5 L** (N2) | same |
| appendix-a A.4.2, 13 rows | 2 S + 9 C + 2 L | unchanged | unchanged |
| SM:1300 "7 structural + 6 layered = 13" | — | 4 S + 3 C + 6 L = 13 (the total survives) | — |

Notes on the table:
- The S column of the SM §7.6 table becomes Wolfenstein A, Koide Q, θ₀ and λ(M_Pl) = 0.
- In appendix-a A.4.1, rows 1, 6, 10, 11 and 22 remain S.
- Rows 6 (A), 10 and 11 (Koide), 13 and 22 were **not audited** beyond the dependency facts above. Applying the Koide
  test is an owner decision.

**Owner decision on the headline.** "Seven parameter-free structural" occurs at about 25 sites (§7). Two options:
- (a) Keep "seven parameter-free", which stays true since C entries are still unfitted, and change "structural" to
  "four unconditional, three conditional on the Cabibbo identification's emergent dressing".
- (b) Change the count to "four parameter-free structural".

Both require the §7 list. SM:1310's "two structurally independent prediction families" in the S set also changes: the
Cabibbo family becomes C.

***

## 5. Gravitational-wave echoes (owner-named)

### 5.1 The three sites, verbatim
- **GR:603:** "The framework therefore predicts that gravitational wave signatures from binary black-hole mergers follow
  standard general-relativistic ringdown morphology, with no OI-specific echo, comb, or wall-reflection features. A
  four-event coherent matched-filter stack on LVK O1–O4 strain data using a dedicated discreteness-scale echo template
  (with the predicted detector-frame delay $\Delta t = (r_+/c)\ln(r_+/\epsilon)$ …) returned a clean null: stacked
  statistic $-0.45$, empirical $p = 0.66$, with the previously hypothesized echo amplitude excluded at $5.9\sigma$."
- **ch18:164/4984:** "The framework's commitment to the discreteness scale … produces a forward empirical signature:
  gravitational wave echoes from black hole mergers. … the horizon's discrete structure at scale $\epsilon$ partially
  reflects outgoing gravitational radiation…"
  - ch18:172/4992: "The fraction … scales with $\epsilon / r_+$ … below current detection thresholds".
  - ch18:178/4998: falsified by "a *high-amplitude* echo detection at a timescale matching the framework's $\Delta t$…
    or by a *low-amplitude* echo detection at a timescale inconsistent with the logarithmic formula".
  - ch18:180/5000: "not directly testable at current precision".
- **appendix-a:183/5736:** "| F5 | Gravitational wave echoes | $\Delta t = (r_+/c)\ln(r_+/\epsilon)$ … | LIGO/Virgo/KAGRA
  next observing runs | Ch 18 §18.5 |".
- **appendix-a:208/5761:** "F5 …: null result at $\Delta t$ … would constrain the framework's substratum-level lattice
  scale."

### 5.2 Verdict — INCORRECT; the maintained statement is GR:603
- **Dating.**
  - An echo prediction with amplitude "FF = 0.19" existed in README from `fbe42ed5` (2026-03-31).
  - GR's "no OI-specific echo" with the null stack first appears in `8f50f9b6` (2026-04-09).
  - The book's §18.6 entered with `334eef0a` (2026-05-14) and does not cite GR:603.
- **Why GR:603 is maintained:**
  - it rests on the partition-relativity argument: the external observer's trace-out is over the cosmological horizon,
    not the black-hole horizon;
  - it rests on a reported analysis;
  - it is the referee-grade paper.
- **Why the book's version fails:**
  - It asserts a reflection fraction ∝ ε/r₊ with no derivation anywhere in the corpus (grep for "echo" across
    papers/book).
  - The book's own sections disagree. F5 says "testable at LVK next observing runs". ch18:172/:180 say the signal is
    below threshold and needs next-generation detectors. :208 says a null would constrain ε, while :178 says a null is
    the expected outcome.
- **Gem (§A.29).** After the earlier amplitude was excluded at 5.9σ, the book form re-states the prediction at an
  amplitude no current detector can reach. Its falsification clause (:178) makes any detectable echo a falsifier and
  non-detection expected. That is a variant adjustable to fit the outcome. It is not an independent prediction.
- **Retention gap (§A.42).** No echo-stack evidence is on `main`: grep of `verification/` and `tools/` found none. GR:603's
  numerical clause ("stacked statistic −0.45 … 5.9σ") rests on unretained evidence. The structural clause ("no
  OI-specific echo") does not depend on it. Owner decision: retain the stack evidence, or narrow GR:603 to its
  structural clause.
- **Status:** Open. No derived amplitude exists, and GR's maintained statement is that no OI-specific echo arises.
- **Replacement:**
  - ch18 §18.6 (164–182): state GR:603. "The framework predicts no OI-specific echo for external observers: a
    black-hole horizon does not change their partition, which is set by the cosmological horizon ([GR §8.4]), so
    ringdowns follow general relativity."
  - Retire the F5 row and its falsification bullet. Under §A.30 the ID F5 is not reused, the successors are not
    renumbered, and the gap is not annotated.
- **Paraphrases to correct:** ch18:28/4848, :160/4980, :339/5159, :349/5169; ch00:101/337; book/README:90 (not #936's
  line); appendix-c:277/6545, :279/6547, :303/6571, :347/6615.
- **Wrong section cross-reference:** appendix-a:183 and appendix-c:277/:303 cite "§18.5" where the echo section is §18.6.

***

## 6–13. Items outside the owner's named five (owner to include or defer)

### 6. GR:567 — INCORRECT
- **Verbatim:** "For the cosmological horizon application the mixing hypothesis holds for any generic chaotic hidden
  sector — the horizon complement is such a system, and its coupling reads the boundary degrees it writes, which is
  (C4)'s realization — so the equivalence applies in our universe."
- **Contradiction.**
  - GR §2.2 (lines 44–53): "Bidirectional coupling is a strengthened form of (C1) and persistence is (C2); neither, nor
    their conjunction, supplies the routing that (C4) asserts … (C4) is therefore a named realization condition at the
    cosmological cut. **Not presently discharged.**"
  - GR:20: "application of the memory-bearing equivalence to our universe remains conditional on C4".
- **Replacement:** "…the horizon complement is such a system, so the mixing hypothesis behind (C2) is motivated there;
  (C4) is a named realization condition not discharged at the cosmological cut (§2.2), and the application of the
  equivalence to our universe is conditional on it."

### 7. GR:711 — INCORRECT
- **Verbatim:** "[Main] establishes the equivalence between embedded observation and quantum mechanics … this four-paper
  synthesis … establishes that the Standard Model, general relativity, and the arrow of time are three faces of a single
  finite deterministic construction, with quantum mechanics emerging as the unique self-consistent description for any
  observer bounded by a causal horizon."
- **Support against it:**
  - Main:22: "the exact equivalence claim is at the finite observable-law level; universal Hilbert-space
    representability is not promoted into a uniqueness theorem for operational quantum mechanics entire";
  - kernel `oi_alone_not_qm` (`verification/lean-mathlib/OIBridge/GeneralCarrier.lean:160`): there exists a theory
    realizing the sealed OI core that is not exact finite operational QM;
  - GR:12: G3 open; GR:20: "unique selection open".
- **Replacement:** "[Main] establishes a finite-horizon correspondence between the recordable laws of an embedded
  observer and fixed-basis quantum laws …; the synthesis proposes that the Standard Model, general relativity and the
  arrow of time descend from one finite deterministic construction, with the covariant field equations (G3) and the
  selection of full operational quantum mechanics open."

### 8. Measurement problem — ch19:333 and ch19:64 OVERSTATED; Main:666 NQ
- **Verbatim:**
  - ch19:333/5509: "| Measurement problem | No interpretive consensus | Dissolved (Bayesian updating) |";
  - ch19:64/5240: "…There is no collapse — only Bayesian updating on the classical substratum. … The framework's
    resolution applies to all the variants of the measurement problem at once…";
  - Main:666: "The Everettian measure problem dissolves: the system evolves as a single reality…". Main:666 does contain
    the quoted sentence; it is the double-slit paragraph, as the coordinator noted.
- **Scope anchor (Main:632):** "The Lüders rule … transcribes Bayesian updating on the classical substratum (Lemma 3)
  for the represented diagonal sector — which is the transition-statistics layer, not the instrument algebra: the
  general operational update for noncommuting interventions belongs to that algebra, reached exactly under the
  operational completion conditions".
- **Defect.**
  - Bayesian updating covers fixed-basis records only.
  - Wigner's friend, which ch19:64 claims, needs a coherent intervention on the friend, so it lies outside that scope.
  - Main:666 already adds "What remains open is the common coherent operational extension", so it is milder: NQ.
- **Replacements:**
  - ch19:333: "Interpretation: fixed-basis records as Bayesian updating; coherent interventions under the completion
    conditions".
  - ch19:64: restrict "all the variants" to "fixed-basis measurement records".
- **Status:** Open (an interpretation).

### 9. Substratum:356 "No additional axiom is needed" — OVERSTATED
- **Defect.**
  - The cascade's selection step is Main §4.6, which is conditional on (EM). Main:728 calls (EM) "an explicit physical
    hypothesis", and Main:740 adds that it holds "at the required rate … is itself a physical hypothesis".
  - The horizon clock is monotone only "for as long as ä > 0" (Substratum:354), so it does not cover the decelerating era.
- **Replacement:** "…The chain grounds in horizon growth during the accelerating phase and in the observer-selection rule
  of [Main §4.6], which is conditional on the effective-mixing hypothesis (EM) and its rate condition."
- **Paraphrases:** Explainer:930 "No additional axiom required"; ch02:196/839 "No independent past-hypothesis axiom is
  required".

### 10. Main:726 "replaces … the past hypothesis" — OVERSTATED (coordinator addition)
- **Verbatim:** "An immediate corollary of (C1)–(C4) is a structural selection rule on where in a finite bijective
  $(S, \varphi)$ observers can exist. The rule replaces a postulate often imported from elsewhere — the "past hypothesis"
  of low initial entropy — with a theorem conditional on the effective-mixing hypothesis (EM) below; under (EM) it is
  derived from the framework's own definitions, and without (EM) it is a conjectural application."
- **Support (Main:730–740).** Under (EM), τ_B(V) ≤ τ_mix + O(ε). The exclusion needs, in addition, τ_mix ≪ τ_S
  (Main:740: "those do not compose"). Main:740 also says that every relevant equilibrium region satisfying (EM) at that
  rate "is itself a physical hypothesis … the theorem converts it into the selection rule and does not supply it".
- **Defect.**
  1. Line 726 omits the rate condition that Main:740 shows is necessary.
  2. The output is weaker than the past hypothesis. It says observers do not exist in sufficiently fast-mixing
     equilibrium. It does not supply a low-entropy state at a temporal boundary, or the direction of the arrow. In a
     finite recurrent (S,φ), non-equilibrium phases are fluctuations, and the rule does not say which side of a
     fluctuation observers occupy.
  3. One postulate is traded for another physical hypothesis: (EM) at the required rate.

  The theorem is correctly stated at Main:730. The overclaim is the word "replaces".
- **Pressure test.** Could "replaces" mean only "does the observer-selection work that the past hypothesis is sometimes
  used for"? Line 740's final sentence frames it that way ("to select observer-compatible configurations"). That
  narrower reading is defensible if stated. Line 726 instead names the past hypothesis as the replaced postulate
  without that restriction.
- **Status:** Conditional (the selection rule); Open (any replacement of the past hypothesis).
- **Replacement (Main:726):** "An immediate corollary of (C1)–(C4) is a structural selection rule on where in a finite
  bijective (S, φ) observers can exist: under the effective-mixing hypothesis (EM) below and the rate condition
  τ_mix ≪ τ_S, a sufficiently fast-mixing equilibrium region supports no observer satisfying (C1)–(C4). The rule
  performs the observer-selection role sometimes assigned to the "past hypothesis" of low initial entropy; it does not
  supply the low-entropy initial condition itself or the direction of the thermodynamic arrow."
- **Propagation:**
  - Main:740 last two sentences ("…is replaced here by a structural selection rule"): narrow them the same way;
  - Substratum:56 ("This replaces the low-entropy "past hypothesis""); Substratum:350;
  - Complexity:204 ("is replaced by the same theorem"); Explainer:930 ("the 'past hypothesis' … gets replaced by a
    theorem");
  - ch02:196/839.
- **Incidental, §A.33:** Main:740 has ALL-CAPS emphasis, "a SUFFICIENTLY FAST-MIXING equilibrium". Make it lowercase.

### 11. Dark-sector budget — OVERSTATED
- **Verbatim:**
  - ch19:339/5515: "| Dark sector budget | $95\%$ unexplained | Derived (total budget) |";
  - ch19:116/5292: "**Framework status.** Derived (total budget; …) … — though the total fraction is partly definitional,
    equal to $1-\Omega_B$ by construction";
  - ch19:118/5294: "The framework derives the total budget".
- **Support against it:**
  - G9: "C | 1 | Partly definitional budget";
  - GR:358 item (4): "the *fraction* is 1−Ω_B by construction";
  - G14: ρ_s = ρ_crit is a "Normalization identity".
- **Replacement:** ch19:339 "Concordance (total = 1−Ω_B by construction; split not derived)"; ch19:116 "Concordance
  (partly definitional): …"; ch19:118 "The total follows from the normalization ρ_s = ρ_crit; the split is not derived."
- **Status:** Consistency (definitional).

### 12. GR:709 — OVERSTATED
- **Verbatim:** "The dark-sector corollary explains ~95% of the gravitational budget of the universe without new
  fundamental particles".
- **Replacement:** "…accounts for the ~95% invisible fraction as 1 − Ω_B, which is partly definitional; the non-trivial
  content is the matter-like versus dark-energy-like split (§7.1–7.3)…"

### 13. ch00:89/325 — OVERSTATED
- **Verbatim:** "…the Bekenstein-Hawking $1/4$ factor as a derivation, the MOND scale $a_0 = cH/6$ as a parameter-free
  prediction, … — all follow from the single statement that observation occurs and four conditions on the partition."
- **Support against it:**
  - G6: C, "(factor imported)";
  - GR:12: "the dimensional factor imported from Verlinde", with the Jiao and Genzel tensions;
  - appendix-a:103 (#936's line, read only): "additionally require the open matter-to-boundary coupling map".
- **Replacement:** "…the Bekenstein–Hawking 1/4 as a consistency relation under the horizon calibration, the MOND scale
  a₀ = cH/6 conditional on the open coupling map and with its factor 1/6 taken from Verlinde, … — follow from that
  statement, the four conditions, and the named hypotheses of each chapter."
- The 1/4 clause belongs to item 1 (owner-named). The rest is outside the five.
- **Also flagged, not audited:** ch19:336/5512 "Hierarchy problem | Dissolved (lattice is UV)".

***

## 14. Propagation lists (corpus-wide grep at 687e885b; FULL mirrors by `grep -nxF`; all book sites below are mirrored)

**1/4 — change**
- GR:12, :162, :164, :320 (history clause), :322, :707;
- Substratum:324; Structure:340, :450, :452;
- Explainer:477, :521, :523, :697 ("which the paper derives"), :699 ("treats … the 1/4 factor as unexplained
  inputs"), :1043;
- book, with FULL lines in brackets: preface:7 [78]; ch00:21 [257], :81 [317], :89 [325];
  ch02:112 [755], :192 [835]; ch03:118 [994]; ch06:348 [1872];
  ch07:63 [1940], :65 [1942], :90 [1967], :96 [1973], :104 [1981];
  ch09:88 [2568], :333 [2813]; ch18:160 [4980]; glossary:17 [6639]; appendix-c:275 [6543];
  appendix-a:93 [5646] and :110 [5663] (column wording only).

**1/4 — keep (legitimate anchors):** GR:24, GR:104, GR:320 (body), GR:30, GR:358 (items 2–3), Substratum:451,
Structure:56, :183, SM:1576, ch02:120 [763], ch03:120 [996], ch04:28 [1147], :44 [1163], :134 [1253], :202 [1321],
ch07:14 [1891], :57 [1934], :106 [1983], :309 [2186], :315 [2192], ch09:14 [2494], :48 [2528], :118 [2598].

**CC — change**
- GR:24, :338, :356 (last two sentences), :358 (item 1), :360, :366, :368, :581/:585 (add the transition sentence),
  :583, :587, :707;
- Explainer:533, :549;
- ch02:192 [835]; ch07:167 [2044], :171 [2048], :175 [2052], :177 [2054], :193 [2070], :195 [2072], :199 [2076],
  :201 [2078]; ch18:140 [4960], :142 [4962], :144 [4964]; ch19:330 [5506];
- appendix-c:273 [6541] (the CC-magnitude clause).

**CC — keep:** ch19:38 [5214] (anchor; optionally make its "does not gravitate" conditional), ch07:14 [1891], ch07:315
[2192], ch09:14 [2494], ch09:48 [2528], ch19:30 [5206], SM:1576, GR:12 (Level-G1 register).

**Counts — change**
- ch18:349 [5169]; ch19:28 [5204], :362 [5538];
- appendix-a:217 [5770], :231 [5784] (anisotropy clause);
- appendix-c:8 [6276], :273 [6541], :275 [6543], :279 [6547], :347 [6615];
- preface:7 [78]; ch00:77 [313], :97 [333]; ch05:13 [1340]; ch07:8 [1885];
- Explainer:699, :862; Substratum:228; SM:1456; Structure:56 (0.05σ → 0.12σ), :142.

**The "seven parameter-free structural" count — change only if §4 is adopted**
- Explainer:679, :858; Structure:197, :944; Substratum:198; SM:1298, :1300, :1310;
- preface:7 [78]; ch00:21 [257], :89 [325]; ch02:228 [871]; ch03:42 [918]; ch04:202 [1321];
  ch05:196 [1523]; ch06:318 [1842], :320 [1844], :332 [1856] (Category A "seven independent relations");
  ch08:272 [2475]; ch09:8 [2488], :231 [2711], :325 [2805]; ch17:234 [4815]; ch19:362 [5538];
- appendix-a:95 [5648], :231 [5784]; appendix-c:8 [6276].
- The sum "8 S + 3 C + …" at appendix-a:95 [5648] and "2 S + 5 L" at :139 [5692] change with it.

**Cabibbo class**
- appendix-a:28 [5581], :50 [5603], :74 [5627];
- SM:1255 (legend), :1262, :1298, :849;
- ch06:297 [1821] and inheritors ch06:299 [1823], :312 [1836]; appendix-a rows 7 and 13 [5629, 5635]; N2 :132 [5685].

**Echoes:** §5.2 list, plus appendix-a:183 [5736] and :208 [5761].

**QM scope / arrow / dark:** GR:567, :711; Main:726, :740; Substratum:56, :350, :356; Complexity:204; Explainer:930;
ch02:196 [839]; ch19:64 [5240], :116 [5292], :118 [5294], :333 [5509], :339 [5515]; GR:709; ch00:89 [325].

**Derived artifacts.** Any edit to `papers/GR.md` requires regenerating `papers/GR.tex`/`.pdf` or flagging them stale in
the same commit. The same holds for `papers/{SM,Main,Substratum,Structure,Explainer,Complexity}` if touched, and for
`book/The-Incompleteness-of-Observation-FULL.{tex,pdf}`. After any count change, re-grep the totals corpus-wide.

***

## 15. Owned by #936 (no edits proposed; follow-ups after #936 lands)

| Line (at 687e885b) | FULL | Overclaim of mine that also sits on it | Follow-up |
|---|---|---|---|
| ch07:12 | 1889 | "Section 7.5 derives the Bekenstein-Hawking entropy … by direct boundary-mode counting" (§1.1); "Section 7.7 dissolves the cosmological constant problem" (§2.3) | Apply the §1.1 and §2.3 wording to #936's version of the line |
| book/README:64 | — | "with the 1/4 factor derived"; "the dissolution of the 10¹²² cosmological constant discrepancy" | Same |
| ch07:110 | 1987 | "the same mechanism that produced the cosmological constant dissolution in §7.7" | Make "dissolution" conditional |
| ch18:146, :150, :156, :158 | 4966, 4970, 4976, 4978 | CC "dissolution" paraphrases ("the same mechanism that produced the cosmological constant dissolution"; the CC ratio "being misidentified as an emergent quantity") | Align with §2.3 after #936 |
| ch19:334 | 5510 | (BH row; nothing of mine) | — |
| appendix-a:103 | 5656 | Read only, as the support for items 13 and 2.10 | — |
| glossary:113, ch19:72, GR:605/611/717 | — | Nothing of mine; GR:605 is adjacent to the echo site GR:603, which #936 does not change | — |

***

## 16. Notes on the input audit (S/paper/apps/AUDIT.md)
- **Confirmed:**
  - the 1/4 identity and 2π/8π (with the GR:320/322 citation correction in §1.0);
  - the GR:583 versus GR:356 contradiction;
  - ρ ~ H²/G as the Friedmann normalization;
  - the dimensional character of 10¹²² = S_dS (its "8/3" is mine too);
  - the Cabibbo dating (054eb99a, then 70ffe82f/3124ef0a);
  - the echo contradiction;
  - GR:567 and GR:711;
  - the count contradictions.
- **Corrected:**
  - "GR:320–322" for the identity should be GR:320. GR:322 is the GW250114 paragraph, which carries the "derived
    structural constant" phrase.
  - The scope anchor for the measurement reading is Main:632. Main:666 is the double-slit paragraph, which does contain
    "The Everettian measure problem dissolves".
- **Added here:**
  - GR:164 and ch07:65 (Gibbons–Hawking "not used as an input");
  - ch18:160 (1/4, ħ and the RVM form as "predictions neither QM nor GR makes");
  - the anisotropy-amplitude contradiction at appendix-a:217/231 against :203;
  - preface:7 and appendix-c:275 (JUNO "prediction made before the measurement");
  - sin²θ₁₃ = A⁴λ² as a λ-inheritor in the recount;
  - the echo-stack evidence missing from `main` (§A.42);
  - the post-falsification echo amplitude as a hard-to-vary concern (§A.29);
  - Main:740's ALL-CAPS emphasis (§A.33);
  - the O(1) factor range of ch07:193, about 10⁻³ to 3;
  - the PDG 2025 numbers, read first-hand.
- **Fixed point.** This was one depth-first pass per item. The §A.31 fixed point (3–4 passes with no NEW finding) was
  not reached. The last items examined (the arrow of time, the dark budget) still produced NEW findings.
