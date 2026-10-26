# ħ and θ₀: owner decisions O1–O7, exactly specified

This document is read-only.

- **Base:** `main` at `b64919cd` (after #938). #938's hunks are one-for-one line replacements in Main:167/170, Explainer:353/373 and appendix-b:454–455. None of those lines is cited here, and no cited line number moved.
- **Exactness:** every OLD string below occurs **exactly once** in its line at `b64919cd`. Each `[FULL:n]` is the line of `book/The-Incompleteness-of-Observation-FULL.md` that is byte-identical to the chapter line, and the same OLD→NEW applies there. `book/README.md` is not mirrored.
- **Checks:** the strings were checked mechanically (`S/hbar-theta/dec/gen/gen.py`). No two edits on one line overlap, except edits that are alternative options of the same decision.
- **Simulation:** the full recommended set (the no-decision list plus every recommended option) was applied to a copy of `b64919cd` (`S/hbar-theta/dec/sim`). Results:
  - `mirror_check`: 0 chapter lines absent from FULL;
  - `claims_check`, `voice_check`, `duplicate_check`, `dependency_label_check` and `lean_manuscript_census`: all OK;
  - `coverage_check`: one expected failure, SUBSTRATUM:T-23 stale under O1-A. The required ledger re-affirmation is given in O1.
- **Fences:** each `text` fence holds the literal strings.

Sources for the numbers:
- **θ₀ and Q:** SM:903 (PDG 2024/25, $m_\tau = 1776.93 \pm 0.09$ MeV), with $m_e = 0.51099895000(15)$ MeV and $m_\mu = 105.6583755(23)$ MeV (PDG 2024).
- **Recomputation:** an independent recomputation (`S/hbar-theta/review/mine/theta0.py`, mpmath at 60 digits, controls green) gives:
  - θ₀ = 0.2222248 ± 0.0000063, which is +0.00114 % and 0.41σ;
  - Q = 0.6666645 ± 0.0000051, which is −0.00033 % and 0.43σ.

***

## O1 — Status of the ħ step in Substratum (§3.4 Stage 3, Theorem 23)

**(a) Question.** Should Substratum's Stage 3 lose "Status: Theorem" and carry H-slope, with the ħ clause of Theorem 23 and its two restatements (Structure:47, Methodology:339) carrying the same condition?

The background is three passages of GR:
- GR:148: "a conditional infrared calibration, not a theorem within the derived QFT";
- GR:76: H-slope is not implied by finite realization or reversibility;
- GR §3 contains no theorem for the gap equation's uniqueness.

**(b) Options.**

*O1-A (all five sites):*

**O1-1** `papers/Substratum.md:182`
```text
OLD: ([GR §3, Theorem])
NEW: ([GR §3.2])
```

**O1-2** `papers/Substratum.md:184`
```text
OLD: **Status:** Theorem.
NEW: **Status:** Conditional on H-slope with the horizon and frame conditions ([GR §3.2]).
```

**O1-3** `papers/Substratum.md:192`
```text
OLD: and $\hbar=c^3\epsilon^2/(4G\sigma)$, with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork.
NEW: and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope with the horizon and frame conditions of [GR §3.2], with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork.
```

**O1-4** `papers/Structure.md:47`
```text
OLD: and $\hbar=c^3\epsilon^2/(4G\sigma)$, $\sigma$ the entropy per boundary mode [GR §3.1].
NEW: and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope [GR §3.2], $\sigma$ the entropy per boundary mode [GR §3.1].
```

**O1-5** `papers/Methodology.md:339`
```text
OLD: and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ tying Planck's constant
NEW: and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$, conditional on H-slope ([GR §3.2]), tying Planck's constant
```


With O1-A, `verification/coverage/LEDGER.json` entry `SUBSTRATUM:T-23` must be re-affirmed in the same commit:
- `"fingerprint": "b69a16c2e08bd93f"` → `"fingerprint": "e6bf53b0d2ae0955"`. This is the value `tools/coverage_check.py` computes for the O1-3 text. Recompute it if any wording differs.
- `kernel` ("GAP"), `delta` ("not formalized") and `assumptions` ("see the statement") are unchanged.

*O1-B (Stage 3 only):* apply O1-1 and O1-2. Leave Theorem 23, Structure:47 and Methodology:339 as they are, so no ledger change follows.

**(c) What changes.**
- No prediction count changes: the calibration is already outside every count (GR:551, appendix-a:117, ch07:305).
- Under both options, the Stage 3 status moves from Theorem to "Conditional on H-slope …".
- Under O1-A, Theorem 23 gains one hypothesis, for its ħ clause only, and one ledger fingerprint changes.
- Lean census: no kernel anchor names Theorem 23 or Stage 3. I grepped `lean-manuscript-census.json`, the `.lean` sources and `tools/`, so §A.35 requires no registry change.
- Other citers of Theorem 23 (Complexity:314; Computation:68, :78; Methodology:333; Structure:138, :195, :768; ch03:8, :40, :104) carry no ħ clause, so nothing else moves.

**(d) Recommendation: O1-A.**
- Under O1-B, Theorem 23 would state its ħ clause without the condition that its own Stage 3 now carries. That is the omission being corrected.
- The correction to Substratum:180 (H41, below) is needed under both options.

***

## O2 — ch06 Category A: one Koide relation or two

**(a) Question.** In ch06 §6.8 Category A, are Koide $Q$ and $\theta_0$ counted as two relations or as one? SM:895 makes them independent observables, the amplitude and the phase, so "equivalently … the same prediction in dual form" is incorrect under either option.

**(b) Options.**

*O2-a (eight relations):*

**O2a-1** `book/ch06-matter-content.md:320` [FULL:1846]
```text
OLD: Koide $Q = 2/3$ (and equivalently Koide $\theta_0 = 2/9$ — the same prediction in dual form), and $\lambda(M_{\text{Pl}}) = 0$ from composite-Higgs structure. These seven relations are tested through five empirical channels
NEW: Koide $Q = 2/3$, Koide $\theta_0 = 2/9$ (independent of $Q$: the amplitude and the phase of the same parametrization, SM §7.2), and $\lambda(M_{\text{Pl}}) = 0$ from composite-Higgs structure. These eight relations are tested through five empirical channels
```

**O2a-2** `book/ch06-matter-content.md:320` [FULL:1846]
```text
OLD: lepton-mass dynamics (Koide $Q$)
NEW: lepton-mass dynamics (Koide $Q$ and $\theta_0$)
```

**O2a-3** `book/ch06-matter-content.md:332` [FULL:1858]
```text
OLD: eight Category A rows representing seven independent relations (the Koide relation and its angle have separate rows)
NEW: eight Category A rows, one for each relation
```


*O2-b (seven relations, Koide counted once):*

**O2b-1** `book/ch06-matter-content.md:320` [FULL:1846]
```text
OLD: Koide $Q = 2/3$ (and equivalently Koide $\theta_0 = 2/9$ — the same prediction in dual form)
NEW: the Koide entry — $Q = 2/3$ and $\theta_0 = 2/9$, two independent observables (amplitude and phase, SM §7.2) counted here as one relation
```

**O2b-2** `book/ch06-matter-content.md:332` [FULL:1858]
```text
OLD: representing seven independent relations (the Koide relation and its angle have separate rows)
NEW: representing seven relations (the Koide amplitude $Q$ and angle $\theta_0$, independent observables, are counted as one Koide relation with separate rows)
```


**(c) What changes.**
- **O2-a:** Category A relations go from 7 to 8. Category A rows stay at 8, table entries at 24, and empirical channels at 5 (Q and θ₀ share the lepton-mass channel).
- **O2-b:** no count change.
- No S/C/L class changes under either option. No other site quotes this count: grep for "seven (independent )?relations" finds only ch06:320 and :332.

**(d) Recommendation: O2-a.** Category A already counts relations by observable: $A$, $|V_{cb}| = A\lambda^2$ and $\sin^2\theta_{13} = A^4\lambda^2$ are listed separately although they share inputs. $Q$ and $\theta_0$ are two independent dimensionless combinations of the three lepton masses.

***

## O3 — ch09:71, the Level G4 row of "Predictions stratified by hierarchy level"

**(a) Question.** The Level G4 row lists $S = A/(4l_p^2)$, "ħ from partition geometry" and the CC dissolution as predictions. Should they be relabelled inside the "Predictions" cell, or removed from it, as #937 did for the ch07 table, GR §7.4 and the ch09 Tier 1 table?

**(b) Options.** O3-76 (ch09:76) applies under both options, because "strongest confirmations at the universality-class level" is false once the row holds consistency relations.

*O3-a (relabel):*

**O3a-1** `book/ch09-universality.md:71` [FULL:2551]
```text
OLD: | Level G4 (universality class) | $S = A/(4 l_p^2)$, CC dissolution, $\hbar$ from partition geometry, RVM form | structural ($1/4$ untested directly) |
NEW: | Level G4 (universality class) | $S = A/(4 l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ (consistency relations), CC dissolution (descriptive), RVM form | structural ($1/4$ untested directly) |
```

**O3-76** `book/ch09-universality.md:76` [FULL:2556]
```text
OLD: with the strongest confirmations at the universality-class level and the open research program
NEW: with the universality-class level consistent with observation rather than sharply tested and the open research program
```


*O3-b (remove from the cell):*

**O3b-1** `book/ch09-universality.md:71` [FULL:2551]
```text
OLD: | Level G4 (universality class) | $S = A/(4 l_p^2)$, CC dissolution, $\hbar$ from partition geometry, RVM form | structural ($1/4$ untested directly) |
NEW: | Level G4 (universality class) | RVM reading (form shared by every smooth model) | non-discriminating; the consistency relations $S = A/(4l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ and the descriptive CC distinction are stated in Chapter 7 §7.10 |
```

**O3-76** `book/ch09-universality.md:76` [FULL:2556]
```text
OLD: with the strongest confirmations at the universality-class level and the open research program
NEW: with the universality-class level consistent with observation rather than sharply tested and the open research program
```


**(c) What changes.** No count: the table has no totals. Only the status surface changes.

**(d) Recommendation: O3-b.** It applies the owner's #937 decision (item 2: consistency identities leave prediction tables and are stated as consistency results) to the last table that still lists them.

***

## O4 — The dressing bound at SM:940 and ch06:179

**(a) Question.** Which rule turns the θ₀ agreement into a bound on the taste-structured emergent mass-level dressing $\delta m/m$, and what does the text then say about the lepton-Yukawa loop of order $10^{-6}$?

**(e) Rule, stated before the comparison and not tuned to it.**

The rule:
- Let $\theta_{\rm pred}(\delta) = \tfrac29\,[1 + \kappa(1-r)\,\delta]$, with $\delta = \delta m/m$. This is the response SM:940 gives: "$d\theta_0/\theta_0 = \kappa(1-\lambda_E/\lambda_{A_1})(\delta m/m)$ and $\kappa \approx -35$", with $r = \lambda_E/\lambda_{A_1} \in [0.22, 0.24]$ (SM:940, ch06:179).
- A dressing $\delta$ is **allowed** iff $|\theta_{\rm pred}(\delta) - \theta_{\rm obs}| \le z\,\sigma_{\rm obs}$ for at least one $r \in [0.22, 0.24]$, with $z = 1.96$ (two-sided 95 %).
- The allowed set is reported **sign-resolved** as $[\delta_{\min}, \delta_{\max}]$, not symmetrized. A $\delta$ is excluded only if it is excluded for every admissible $r$.

Inputs:
- $\theta_{\rm obs} = 0.2222248$ and $\sigma_{\rm obs} = 0.0000063$. These are the full-precision PDG 2024 values; SM:903 rounds them to $0.222225 \pm 0.000006$.
- $\Delta = (\theta_{\rm obs} - \tfrac29)/\tfrac29 = 1.143\times10^{-5}$ and $s = \sigma_{\rm obs}/\tfrac29 = 2.835\times10^{-5}$.

Computation:
- The condition is $\Delta - zs \le \kappa(1-r)\delta \le \Delta + zs$, i.e. $-4.414\times10^{-5} \le \kappa(1-r)\delta \le 6.700\times10^{-5}$.
- Because $\kappa(1-r) < 0$, $\delta \in [(\Delta+zs)/(\kappa(1-r)),\,(\Delta-zs)/(\kappa(1-r))]$.

| $r$ | $\kappa(1-r)$ | allowed $\delta$ |
|---|---|---|
| 0.22 | −27.30 | [−2.454, +1.617] × 10⁻⁶ |
| 0.24 | −26.60 | [−2.519, +1.659] × 10⁻⁶ |
| union | | **[−2.52, +1.66] × 10⁻⁶**, quoted as $-2.5\times10^{-6} \lesssim \delta m/m \lesssim 1.7\times10^{-6}$ |

Notes on the result:
- **Rounding.** With SM:903's rounded inputs ($\Delta = 1.25\times10^{-5}$, $s = 2.70\times10^{-5}$) the union is [−2.46, +1.52] × 10⁻⁶. The quoted bound uses the full-precision inputs; a reader who repeats it from SM:903's rounding gets +1.5 rather than +1.7 on the positive side.
- **Where the old bound came from.** $0.002/(35 \times 0.77) = 7.4\times10^{-5} \approx 8\times10^{-5}$. It used the stale central deviation 0.2 % as if it were a limit.
- **Loop comparison.** A loop of order $10^{-6}$ lies inside the 95 % interval for either sign, by a factor of 1.7 for $\delta > 0$ and 2.5 for $\delta < 0$. That is order unity against an order-of-magnitude estimate, so it is compatible but not decisive.
- **Disclosure.** At 68 % ($z = 1$) the allowed set would be [−1.50, +0.64] × 10⁻⁶, and a $+10^{-6}$ loop would fall outside it. The 95 % level is chosen because it is the conventional two-sided exclusion level, not for its outcome.

**(b) Options.**

*O4-a (95 % rule, as above):*

**O4a-1** `papers/SM.md:940`
```text
OLD: The $0.2\%$ agreement of $\theta_0 = 2/9$ bounds the taste-structured part of an emergent mass-level dressing by $\delta m/m \lesssim 8 \times 10^{-5}$; a second-order lepton-Yukawa loop supplies $\sim 10^{-6}$.
NEW: The agreement of $\theta_0 = 2/9$ with the observed $\theta_0 = 0.222225 \pm 0.000006$ ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence (two-sided); a second-order lepton-Yukawa loop, of order $10^{-6}$, lies inside that interval for either sign, by a factor of about two, so the comparison is not decisive.
```

**O4a-2** `book/ch06-matter-content.md:179` [FULL:1705]
```text
OLD: constrains it to $\delta m/m \lesssim 8 \times 10^{-5}$, which a lepton-Yukawa loop satisfies (SM §7.2).
NEW: constrains it to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence, an interval that a lepton-Yukawa loop of order $10^{-6}$ lies inside for either sign, by a factor of about two (SM §7.2).
```


*O4-c (no quantitative bound):*

**O4c-1** `papers/SM.md:940`
```text
OLD: The $0.2\%$ agreement of $\theta_0 = 2/9$ bounds the taste-structured part of an emergent mass-level dressing by $\delta m/m \lesssim 8 \times 10^{-5}$; a second-order lepton-Yukawa loop supplies $\sim 10^{-6}$.
NEW: How tightly the observed $\theta_0$ bounds the taste-structured part of an emergent mass-level dressing, and whether a second-order lepton-Yukawa loop (of order $10^{-6}$) respects that bound, is not quantified here.
```

**O4c-2** `book/ch06-matter-content.md:179` [FULL:1705]
```text
OLD: constrains it to $\delta m/m \lesssim 8 \times 10^{-5}$, which a lepton-Yukawa loop satisfies (SM §7.2).
NEW: constrains it, and whether a lepton-Yukawa loop respects that constraint is not quantified (SM §7.2).
```


**(c) What changes.**
- **O4-a:** the bound tightens from $8\times10^{-5}$ to $[-2.5, +1.7]\times10^{-6}$, about 30–50× tighter. The stated loop margin falls from about 80× to 1.7–2.5×. "Satisfies" becomes "lies inside … not decisive".
- **O4-c:** the bound and the loop comparison are withdrawn from both sites.
- No classification changes under either option. θ₀ stays **C**.

**(d) Recommendation: O4-a.** The bound is a genuine, reproducible consequence of the data under a pre-stated rule, and the text reports the marginal outcome as it is. O4-c discards a valid result.

***

## O5 — "The sharpest" match

**(a) Question.** The corpus calls θ₀ the sharpest match (ch04:134, ch06:171, Substratum:446) and also calls Q the sharpest (ch06:12, appendix-a:98, :215). Which statement should stand, and on what metric?

On PDG 2024:

| Match | Relative deviation | Pull |
|---|---|---|
| Q | 0.00033 % | 0.43σ |
| θ₀ | 0.00114 % | 0.41σ |
| Cabibbo λ | 0.031 % against the global fit | 0.10σ |

"Sharpest" therefore depends on the metric: in relative precision it is Q; by pull it is λ.

**(b) Options.**

*O5-a (keep Q, name the metric, drop θ₀'s claim; SM:1329 "two of the tightest"):*

**O5a-1** `book/ch04-methodology.md:134` [FULL:1253]
```text
OLD: (matched to $0.001\%$, the sharpest empirical agreement in the framework)
NEW: (matched to $0.001\%$)
```

**O5a-2** `book/ch06-matter-content.md:171` [FULL:1697]
```text
OLD:  — the sharpest empirical agreement in the framework.
NEW: .
```

**O5a-3** `papers/Substratum.md:446`
```text
OLD: — the sharpest empirical match in the framework
NEW: — matched to observation
```

**O5a-4** `papers/SM.md:1329`
```text
OLD: the two tightest (
NEW: two of the tightest (
```

**O5a-5** `book/appendix-a-prediction-status.md:215` [FULL:5752]
```text
OLD: — the framework's sharpest individual empirical match.
NEW: — the framework's sharpest individual empirical match in relative precision.
```

**O5a-6** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: , the sharpest empirical agreement in the framework,
NEW: , the sharpest empirical agreement in the framework in relative precision,
```

**O5a-7** `book/appendix-a-prediction-status.md:98` [FULL:5635]
```text
OLD: — the sharpest framework prediction across all 23,
NEW: — the sharpest framework prediction across all 23 in relative precision,
```


*O5-c (no superlatives anywhere):* apply O5a-1, O5a-2, O5a-3 and O5a-4 above, plus:

**O5c-extra1** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: , the sharpest empirical agreement in the framework,
NEW: ,
```

**O5c-extra2** `book/appendix-a-prediction-status.md:215` [FULL:5752]
```text
OLD: **Sharpest single match.** Koide $Q = 2/3$ to better than 0.001% (entry 10) — the framework's sharpest individual empirical match.
NEW: **Koide match.** Koide $Q = 2/3$ to better than 0.001% (entry 10).
```

**O5c-extra3** `book/appendix-a-prediction-status.md:98` [FULL:5635]
```text
OLD: — the sharpest framework prediction across all 23, matching
NEW: — matching
```


**(c) What changes.** No count or classification changes. The θ₀ figure corrections on the same lines (T5, T8, T11) are in the no-decision list and do not overlap these edits.

**(d) Recommendation: O5-a.** It keeps the status surface's existing statement (appendix-a:215) and makes it true by naming its metric. θ₀'s superlative contradicts it on any metric.

***

## O6 — The ch06 m_μ rows quoting 105.74 MeV ("Koide closure") and the chain table

**(a) Question.** How should the three ch06 tables present $m_\mu$ and $m_e$?

Two facts settle what the figures mean:
- **105.74 MeV is reproducible.** It is the Koide closure using the *structural* ratio $m_e/m_\tau = 1/(36\pi^4)$, which gives $m_e = 0.5067$ MeV. The closure then gives 105.737 MeV at $m_\tau = 1776.86$ and 105.741 MeV at 1776.93. Against the observed 105.6584 MeV that is 0.074 % and 0.078 % respectively, with $m_\mu/m_\tau = 0.059508$. This is the chain that ch06:192's RG discussion describes.
- **The θ₀-based value is different.** It is 105.656 MeV (0.002 %), from SM:1270.

**(b) Options.**

*O6-A:* make each table state what it computes:
- (i) the §6.6 table keeps the structural closure, relabelled and moved to the PDG 2024 basis;
- (ii) the §6.8 summary table mirrors SM §7.6;
- (iii) the six-mass chain table uses the chain's own predicted $m_\tau = 1755$ MeV, as SM:983–984 does: $0.510983 \times 1755/1776.93 = 0.505$ and $105.656 \times 1755/1776.93 = 104.4$, both −1.2 %.

**O6-i-1** `book/ch06-matter-content.md:190` [FULL:1716]
```text
OLD: | $m_\mu$ | Koide closure with $m_e$, $m_\tau$ | $105.74$ MeV | $105.66$ | $0.07\%$ |
NEW: | $m_\mu$ | Koide closure with the structural $m_e/m_\tau = 1/(36\pi^4)$ and $m_\tau$ | $105.74$ MeV | $105.66$ | $0.08\%$ |
```

**O6-i-2** `book/ch06-matter-content.md:192` [FULL:1718]
```text
OLD: agrees with observation more tightly ($0.07\%$)
NEW: agrees with observation more tightly ($0.08\%$)
```

**O6-ii** `book/ch06-matter-content.md:305` [FULL:1831]
```text
OLD: | $m_\mu$ | Koide closure | $105.74$ MeV | $105.66$ MeV | $0.07\%$ |
NEW: | $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | $105.656$ MeV | $105.658$ MeV | $0.002\%$ |
```

**O6-iii-1** `book/ch06-matter-content.md:217` [FULL:1743]
```text
OLD: | Layer 1 | $0.51096$ MeV | $0.511$ | $0.007\%$ |
NEW: | Layer 1 | $0.505$ MeV | $0.511$ | $1.2\%$ |
```

**O6-iii-2** `book/ch06-matter-content.md:218` [FULL:1744]
```text
OLD: | $m_\mu$ | Koide closure | Layer 1 | $105.74$ MeV | $105.66$ | $0.07\%$ |
NEW: | $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | Layer 1 | $104.4$ MeV | $105.66$ | $1.2\%$ |
```


*O6-B:* replace (i) with the θ₀-based value and remove the closure's RG explanation; (ii) and (iii) as in O6-A.

**O6B-i-1** `book/ch06-matter-content.md:190` [FULL:1716]
```text
OLD: | $m_\mu$ | Koide closure with $m_e$, $m_\tau$ | $105.74$ MeV | $105.66$ | $0.07\%$ |
NEW: | $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | $105.656$ MeV | $105.658$ | $0.002\%$ |
```

**O6B-i-2** `book/ch06-matter-content.md:192` [FULL:1718]
```text
OLD: The implied $m_\mu/m_\tau = 0.0595$ from Koide closure agrees with observation more tightly ($0.07\%$) than the $m_e/m_\tau$ structural relation itself ($0.84\%$) — the pattern is consistent with electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, where the larger $m_\tau$ Yukawa receives proportionally smaller logarithmic corrections than the small $m_e$ Yukawa.
NEW: The $m_e/m_\tau$ structural relation itself lies at $0.84\%$.
```


**(c) What changes.**
- (i): 0.07 % → 0.08 % under A, because of the $m_\tau$ basis; under B, 105.74 → 105.656 and 0.07 % → 0.002 %.
- (ii): 105.74, 0.07 % → 105.656, 0.002 %.
- (iii): 0.51096, 0.007 % → 0.505, 1.2 %; and 105.74, 0.07 % → 104.4, 1.2 %.
- No class or count changes. ch06:219's "four Layer-1 relations" is unchanged.

**(d) Recommendation: O6-A.**
- Its values are reproducible and its labels say which closure is meant.
- O6-B would delete a scientific statement (the RG reading at ch06:192) that the data still support.
- (ii) and (iii) are not really choices: the §6.8 table mirrors SM §7.6, and a chain table must use the chain's $m_\tau$.

***

## O7 — The data basis for Koide Q

**(a) Question.** Should the Koide Q figures move to SM:903's PDG 2024 basis? The current figures use the PDG 2016–22 $m_\tau$ = 1776.86.

**(b) Options.**

*O7-a (harmonize):*

**O7a-1** `book/ch00-introduction.md:77` [FULL:313]
```text
OLD: the observed value is $0.666661 \pm 0.000007$, a match to better than $0.001\%$ ($0.8\sigma$)
NEW: the observed value is $0.666664 \pm 0.000005$, a match to better than $0.001\%$ ($0.4\sigma$)
```

**O7a-2** `book/glossary.md:97` [FULL:6697]
```text
OLD: Observed value $Q = 0.666661 \pm 0.000007$.
NEW: Observed value $Q = 0.666664 \pm 0.000005$.
```

**O7a-3** `book/glossary.md:97` [FULL:6697]
```text
OLD: the match is better than $0.001\%$ ($0.8\sigma$)
NEW: the match is better than $0.001\%$ ($0.4\sigma$)
```

**O7a-4** `papers/SM.md:1267`
```text
OLD: | 0.66667 | 0.66666 | $< 0.01\%$ |
NEW: | 0.66667 | 0.666664 | $0.0003\%$ |
```

**O7a-5** `book/ch06-matter-content.md:302` [FULL:1828]
```text
OLD: | $2/3$ | $0.66667$ | $0.001\%$ |
NEW: | $2/3$ | $0.666664$ | $0.0003\%$ |
```

**O7a-6** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: matched to $0.001\%$
NEW: matched to $0.0003\%$
```


*O7-b:* leave as is.

**(c) What changes.**

| | Value | Relative | Pull |
|---|---|---|---|
| Current (PDG 2016–22) | Q = 0.666661 ± 0.000007 | 0.0009 % | 0.8σ |
| O7-a (PDG 2024) | Q = 0.666664 ± 0.000005 | 0.0003 % | 0.4σ |

- "Better than 0.001 %" holds on both bases.
- SM:1267 changes from "< 0.01 %" to "0.0003 %". ch06:302 and ch06:12 change from "0.001 %" to "0.0003 %".
- No class or count changes.

**(d) Recommendation: O7-a.** The owner's directive asks for one authoritative basis, which is SM:903.

***

## Corrections needing no owner decision (the full change set)

These apply the audit's OVERSTATED and INCORRECT verdicts as amended by the review (`review/REVIEW.md`). The tags are:
- **INCORRECT:** H1, H4, H23, H38, H41, T11;
- **the six missed sites:** H2, H25, H31, H33, and ch09:76 and ch06:332, which are handled in O3 and O2;
- **reclassified needs-qualification:** H5;
- **OVERSTATED:** all others.

### ħ: the relation, not the value; calibration, not theorem

**H1** `book/ch07-gravity.md:10` [FULL:1889]
```text
OLD: The horizon's geometric and thermodynamic properties — surface gravity $\kappa$, area $A$, Hawking temperature $T$ — fix the values of the emergent physics: the action scale $\hbar$, the Bekenstein-Hawking entropy with its $1/4$ coefficient, the form of the dark-energy equation of state.
NEW: The horizon's thermodynamics relates the emergent action scale $\hbar$ to the discreteness scale $\epsilon$, with $\kappa$ and $A$ dropping out of $\hbar$ (Sections 7.3–7.4); it recovers the Bekenstein-Hawking entropy with its $1/4$ coefficient as a consistency relation of that calibration and supplies the dark-energy bookkeeping read in the running-vacuum channel (Section 7.8).
```

**H2** `book/ch07-gravity.md:14` [FULL:1893]
```text
OLD: the value of $\hbar$, the discreteness scale
NEW: the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the discreteness scale
```

**H3** `book/ch07-gravity.md:36` [FULL:1915]
```text
OLD: The most distinctive content of the framework's gravitational sector is the derivation of Planck's constant $\hbar$ as an emergent quantity determined by the cosmological horizon's thermodynamic properties. The standard view treats $\hbar$ as a fundamental constant of nature whose value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ is measured rather than derived.
NEW: The most distinctive content of the framework's gravitational sector is the treatment of Planck's constant $\hbar$ as an emergent action scale whose relation to the boundary geometry is fixed by the cosmological horizon's thermodynamics. The standard view treats $\hbar$ as a fundamental constant of nature, its value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ measured.
```

**H4** `book/ch07-gravity.md:50` [FULL:1929]
```text
OLD: a QFT on a bifurcate Killing horizon, under the H-Hawking conditions, background must be periodic in imaginary time with period $\beta = 2\pi c / \kappa$, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$. This is a theorem *within* the derived QFT, not an external import — the regularity requirement follows from the Wick rotation's analytic structure.
NEW: a QFT on this bifurcate Killing horizon background is periodic in imaginary time with period $\beta = 2\pi c / \kappa$ under the H-Hawking conditions, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$ when the emergent state belongs to that KMS class (H-spectrum). The step is therefore a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2]).
```

**H5** `book/ch07-gravity.md:82` [FULL:1961]
```text
OLD: This is not an additional empirical input but an algebraic consequence of the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ together with the definition of $l_p$.
NEW: It adds no relation beyond the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ and the definition of $l_p$, and its numerical value takes the measured $\hbar$ as input.
```

**H6** `book/ch01-observation.md:87` [FULL:431]
```text
OLD: Chapter 7 shows that the cosmological partition produces $\hbar$ as a thermodynamic identity at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following under the horizon conditions named there
NEW: Chapter 7 shows that, under the horizon conditions named there, the cosmological partition relates $\hbar$ to the discreteness scale through a thermal self-consistency condition at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following
```

**H7** `book/ch02-substratum.md:22` [FULL:665]
```text
OLD: Chapter 7 develops each of these as theorems;
NEW: Chapter 7 develops each of these under the conditions it names;
```

**H8** `book/ch02-substratum.md:110` [FULL:753]
```text
OLD: Stage 3 takes Stage 2's output and derives the emergent value of $\hbar$. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics — forces the relation
NEW: Stage 3 takes Stage 2's output and derives the emergent action-scale relation. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics, conditional on H-slope with the horizon and frame conditions named there — forces the relation
```

**H9** `book/ch02-substratum.md:112` [FULL:755]
```text
OLD: as the unique simultaneous solution.
NEW: as the unique simultaneous solution, which fixes only the ratio $\epsilon/\sqrt{\sigma} = 2\,\ell_P$.
```

**H10** `book/ch02-substratum.md:228` [FULL:871]
```text
OLD: the boundary thermodynamics, the value of $\hbar$, the Bekenstein-Hawking
NEW: the boundary thermodynamics, the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking
```

**H11** `book/ch00-introduction.md:97` [FULL:333]
```text
OLD: the Bekenstein-Hawking $1/4$ factor and the value of $\hbar$ from horizon thermodynamics under named horizon conditions
NEW: the Bekenstein-Hawking $1/4$ factor and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ as consistency relations of horizon thermodynamics under named horizon conditions
```

**H12** `book/ch04-methodology.md:204` [FULL:1323]
```text
OLD: the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from horizon thermodynamics are conditional on
NEW: the Bekenstein-Hawking $1/4$ coefficient and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ from horizon thermodynamics are consistency relations conditional on
```

**H13** `book/ch06-matter-content.md:348` [FULL:1874]
```text
OLD: the value of $\hbar$ from horizon thermodynamics,
NEW: the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ relating the action scale to the discreteness scale (a self-consistency condition, §7.4),
```

**H14a** `book/ch09-universality.md:14` [FULL:2494]
```text
OLD: Some predictions are *universality-class* results
NEW: Some results are *universality-class* results
```

**H14b** `book/ch09-universality.md:14` [FULL:2494]
```text
OLD: the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry conditional on the horizon conditions named in Chapter 7
NEW: the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$ from partition geometry, consistency relations conditional on the horizon conditions named in Chapter 7
```

**H15** `book/ch09-universality.md:48` [FULL:2528]
```text
OLD: the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry sit at the same level
NEW: the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, consistency relations, sit at the same level
```

**H16** `book/ch09-universality.md:92` [FULL:2572]
```text
OLD: *The value of $\hbar$ from partition geometry.*
NEW: *The action-scale relation from partition geometry.*
```

**H17** `book/ch09-universality.md:118` [FULL:2598]
```text
OLD: Bekenstein-Hawking $1/4$ and $\hbar$ from partition geometry under the horizon conditions of Chapter 7
NEW: the Bekenstein-Hawking $1/4$ and the action-scale relation for $\hbar$ as consistency relations under the horizon conditions of Chapter 7
```

**H18** `book/ch12-evolution-intelligence.md:197` [FULL:3449]
```text
OLD: — the value of $\hbar$, the Standard Model,
NEW: — the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the Standard Model,
```

**H19** `book/glossary.md:73` [FULL:6673]
```text
OLD: The framework's derivation of Planck's constant from horizon thermodynamics.
NEW: It relates Planck's constant to the discreteness scale, conditional on H-slope, and fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$: a self-consistency condition, not an independent determination of the value of $\hbar$.
```

**H20** `book/readers-guide.md:77` [FULL:177]
```text
OLD: the gap equation deriving $\hbar$
NEW: the gap equation relating $\hbar$ to the discreteness scale
```

**H21** `book/appendix-b-derivations.md:16` [FULL:5783]
```text
OLD: The framework derives Planck's constant $\hbar$ from a thermal self-consistency argument
NEW: The framework relates Planck's constant $\hbar$ to the discreteness scale through a thermal self-consistency argument
```

**H22** `book/appendix-b-derivations.md:173` [FULL:5940]
```text
OLD: The framework derives Planck's constant $\hbar$ as the unique self-consistent value matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory.
NEW: The framework derives the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ between Planck's constant and the discreteness scale by matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory, conditional on H-slope with the horizon and frame conditions of Chapter 7 §7.3; with $\epsilon$ not independently known, it fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ (Chapter 7 §7.4), not the value of $\hbar$.
```

**H23** `book/appendix-b-derivations.md:211` [FULL:5978]
```text
OLD: with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import.
NEW: with $\hbar$ unknown. The periodicity holds under the H-Hawking conditions and the KMS identification requires the emergent state to belong to that class (H-spectrum), so the matching below is a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2]).
```

**H24** `book/appendix-b-derivations.md:471` [FULL:6238]
```text
OLD: B.4 establishes the gap equation determining $\hbar$ from horizon thermodynamics
NEW: B.4 establishes the gap equation relating $\hbar$ to the discreteness scale through horizon thermodynamics
```

**H25** `book/appendix-c-objections.md:20` [FULL:6266]
```text
OLD: the gap equation deriving $\hbar$)
NEW: the gap equation for $\hbar$)
```

**H26** `book/appendix-c-objections.md:236` [FULL:6482]
```text
OLD: ## C.10 Circularity concerns: the gap equation deriving $\hbar$
NEW: ## C.10 Circularity concerns: the gap equation for $\hbar$
```

**H27** `book/appendix-c-objections.md:238` [FULL:6484]
```text
OLD: the framework's gap equation in Chapter 7 §7.4, which derives the Planck constant $\hbar$ from the cosmological horizon's geometric properties.
NEW: the framework's gap equation in Chapter 7 §7.3, which relates the Planck constant $\hbar$ to the discreteness scale through the cosmological horizon's thermodynamics.
```

**H28** `book/appendix-c-objections.md:242` [FULL:6488]
```text
OLD: The logical chain in Chapter 7 §7.4
NEW: The logical chain in Chapter 7 §7.3
```

**H29** `book/appendix-c-objections.md:257` [FULL:6503]
```text
OLD: - Classical-temperature matching → $\hbar$ fixed.
NEW: - Classical-temperature matching → $\hbar$ fixed in terms of $\epsilon$ (conditional on H-slope, Chapter 7 §7.3).
```

**H30** `book/appendix-c-objections.md:263` [FULL:6509]
```text
OLD: The framework's derivation of $\hbar$ is therefore consistent
NEW: The gap equation is therefore consistent
```

**H31** `book/README.md:64` (not mirrored in FULL)
```text
OLD: the framework's $\hbar$ derivation from thermal self-consistency at the cosmological horizon
NEW: the framework's action-scale relation for $\hbar$ from thermal self-consistency at the cosmological horizon
```

**H32** `papers/GR.md:18`
```text
OLD: — the value of $\hbar$, the Bekenstein-Hawking area law,
NEW: — the origin of the action scale $\hbar$, the Bekenstein-Hawking area law,
```

**H33** `papers/GR.md:170`
```text
OLD: Step 4 will fix its value via thermal matching.
NEW: Step 4 will fix it in terms of $\epsilon$ via thermal matching.
```

**H34** `papers/GR.md:336`
```text
OLD: The framework's predictions in Part II ($\hbar$, $S_{\text{dS}}$, the Type II RVM form of the dark energy) depend on
NEW: The framework's Part II results (the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, $S_{\text{dS}}$, the Type II RVM reading of the dark energy) depend on
```

**H35** `papers/Main.md:684`
```text
OLD: the framework derives $\hbar$ and the Bekenstein–Hawking coefficient downstream, and the derived bound
NEW: the framework relates $\hbar$ to the discreteness scale and recovers the Bekenstein–Hawking coefficient downstream, as consistency relations of its horizon calibration [GR §3–§5], and the derived bound
```

**H36** `papers/SM.md:1350`
```text
OLD: including the derivation of $\hbar$, the Bekenstein-Hawking area law, the dissolution of the cosmological constant problem,
NEW: including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking area law, the conditional dissolution of the cosmological constant problem ([GR §6.2]),
```

**H37** `papers/SM.md:1576`
```text
OLD: including the derivation of $\hbar$ from the cosmological horizon and the Bekenstein-Hawking area law including the $1/4$ coefficient (both conditional on the horizon conditions recorded there)
NEW: including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking area law with its $1/4$ coefficient (consistency relations, both conditional on the horizon conditions recorded there)
```

**H38** `papers/SM.md:1378`
```text
OLD: , ℏ = c³ε²/(4G), the Bekenstein-Hawking formula, and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems.
NEW: , and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems on the branch stated in §1 (Tier 2), with the conditions marked at each entry. The horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking coefficient it matches hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5]).
```

**H39** `papers/Substratum.md:22`
```text
OLD: the framework determines $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, for an entropy $\sigma$ per boundary mode, the Bekenstein-Hawking entropy with the $1/4$ coefficient, and the dissolution of the cosmological constant problem.
NEW: the framework relates the action scale to the discreteness scale through the calibration $\hbar = c^3 \epsilon^2 / (4G\sigma)$, which fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ for an entropy $\sigma$ per boundary mode, and recovers the Bekenstein-Hawking entropy with the $1/4$ coefficient as a consistency relation of that calibration, both conditional on H-slope [GR §3.2], and proposes a dissolution of the cosmological constant problem conditional on the covariant coupling step [GR §6.2].
```

**H40** `papers/Substratum.md:178`
```text
OLD: **Output:** The emergent value of $\hbar$ is $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]).
NEW: **Output:** The emergent action-scale relation $\hbar = c^3 \epsilon^2 / (4G\sigma)$, equivalently $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]); it fixes only $\epsilon/\sqrt{\sigma}$, not the value of $\hbar$ ([GR §4]).
```

**H41** `papers/Substratum.md:180`
```text
OLD: detailed balance (consequence of $\varphi$ being a bijection). No new structural assumptions beyond Stages 1–2.
NEW: and the infrared detailed-balance condition H-slope with the horizon and frame conditions ([GR §2, §3.2, §8.5]), which does not follow from $\varphi$ being a bijection ([GR §3.2]) and is an assumption beyond Stages 1–2.
```

**H42** `papers/Explainer.md:411`
```text
OLD: The value of ℏ is determined by the partition geometry — which is what Section 5 derives.
NEW: The action scale ℏ is fixed by the partition geometry in terms of the discreteness scale — which is what Section 5 derives.
```

**H43** `papers/Explainer.md:477`
```text
OLD: The gap equation relates one free geometric parameter (ε), at given σ, to one output (ℏ).
NEW: The gap equation, conditional on the infrared detailed-balance condition H-slope with the horizon and frame conditions [GR §3.2], relates one free geometric parameter (ε), at given σ, to one output (ℏ).
```

**H44** `papers/Explainer.md:662`
```text
OLD: It makes quantitative predictions — the value of ℏ and dark energy evolution — that interpretations do not, and it accounts for
NEW: It relates ℏ to the discreteness scale and carries a running-vacuum reading of dark energy whose falsifiable content is the Type II channel ([GR §7.1]) — content that interpretations do not have — and it accounts for
```

**H45** `papers/Explainer.md:992`
```text
OLD: which derives ℏ, the Bekenstein-Hawking area law, and dark-sector phenomenology
NEW: which relates ℏ to the discreteness scale, recovers the Bekenstein-Hawking area law, and develops dark-sector phenomenology
```


### θ₀ figure (SM:903, 0.001 %, 0.4σ) and labels

**T1** `papers/SM.md:14`
```text
OLD: the Koide angle $\theta_0 = 2/9$ to $0.02\%$
NEW: the Koide angle $\theta_0 = 2/9$ to $0.001\%$
```

**T2a** `papers/SM.md:928`
```text
OLD: misses the observed $0.2227$ by a factor of four
NEW: misses the observed $0.2222$ by a factor of four
```

**T2b** `papers/SM.md:928`
```text
OLD: The empirical match at $0.02\%$ does not
NEW: The empirical match at $0.001\%$ does not
```

**T3** `papers/SM.md:934`
```text
OLD: (observed $0.2227$)
NEW: (observed $0.222225$)
```

**T4** `papers/SM.md:1318`
```text
OLD: | Koide $\theta_0$ | $C_2/d^2 = 2/9$ | 0.2222 | 0.2222 | 0.02% |
NEW: | Koide $\theta_0$ | $C_2/d^2 = 2/9$ | 0.22222 | 0.222225 | 0.001% |
```

**T5** `papers/SM.md:1329`
```text
OLD: $\theta_0$ at $0.02\%$)
NEW: $\theta_0$ at $0.001\%$)
```

**T6** `papers/SM.md:1572`
```text
OLD: the Koide angle from the cubic-group quadratic Casimir to $0.02\%$
NEW: the Koide angle from the cubic-group quadratic Casimir to $0.001\%$
```

**T7** `papers/Juno.md:401`
```text
OLD: Koide θ₀ (0.02%)
NEW: Koide θ₀ (0.001%)
```

**T8** `papers/Substratum.md:446`
```text
OLD: (0.02%)
NEW: (0.001%)
```

**T9** `book/README.md:62` (not mirrored in FULL)
```text
OLD: Koide $\theta_0 = 2/9$ at $0.02\%$
NEW: Koide $\theta_0 = 2/9$ at $0.001\%$
```

**T10** `book/ch05-gauge-structure.md:196` [FULL:1525]
```text
OLD: the Koide relation $2/9$ matched to $0.02\%$
NEW: the Koide angle $\theta_0 = 2/9$ matched to $0.001\%$
```

**T11** `book/ch06-matter-content.md:171` [FULL:1697]
```text
OLD: which is the angular form of the $Q = 2/3$ relation under the standard $\mathbb{Z}_3$-symmetric parametrization of three masses by an angle. The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222220$ at $0.02\%$
NEW: which is the phase of the standard $\mathbb{Z}_3$-symmetric parametrization of three masses, independent of the amplitude that $Q = 2/3$ fixes (SM §7.2). The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222225 \pm 0.000006$ at $0.001\%$ ($0.4\sigma$)
```

**T12** `book/ch06-matter-content.md:303` [FULL:1829]
```text
OLD: | $2/9$ | $0.22222$ | $0.02\%$ |
NEW: | $2/9$ | $0.222225$ | $0.001\%$ |
```

**T13** `book/ch08-juno.md:68` [FULL:2271]
```text
OLD: the Koide angle at $0.02\%$
NEW: the Koide angle at $0.001\%$
```

**T14** `book/ch08-juno.md:177` [FULL:2380]
```text
OLD: the Koide angle at $0.02\%$
NEW: the Koide angle at $0.001\%$
```

**T15** `book/ch08-juno.md:210` [FULL:2413]
```text
OLD: the Koide angle at $0.02\%$
NEW: the Koide angle at $0.001\%$
```

**T16** `book/ch03-structural-realism.md:42` [FULL:918]
```text
OLD: the Koide relation $2/9$
NEW: the Koide angle $2/9$
```

**T17** `book/ch03-structural-realism.md:118` [FULL:994]
```text
OLD: the Koide relation as $2/9$
NEW: the Koide angle as $2/9$
```

**T18** `book/appendix-a-prediction-status.md:80` [FULL:5617]
```text
OLD: | C | 1 | Within 1% | Ch 6 §6.5 |
NEW: | C | 1 | 0.001% | Ch 6 §6.5 |
```


### Stale $m_\tau$ = 1776.86 mass rows (moved to PDG 2024, as SM:948–949 already are)

**M1** `papers/SM.md:1269`
```text
OLD: | 0.51096 MeV | 0.51100 MeV | 0.007% |
NEW: | 0.51098 MeV | 0.51100 MeV | 0.003% |
```

**M2** `papers/SM.md:1270`
```text
OLD: | 105.652 MeV | 105.658 MeV | 0.006% |
NEW: | 105.656 MeV | 105.658 MeV | 0.002% |
```

**M3** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: $\theta_0 = 2/9$ — at $0.007\%$.
NEW: $\theta_0 = 2/9$ — at $0.003\%$.
```

**M4a** `book/ch06-matter-content.md:181` [FULL:1707]
```text
OLD: (the tau mass $m_\tau = 1776.86$ MeV)
NEW: (the tau mass $m_\tau = 1776.93$ MeV)
```

**M4b** `book/ch06-matter-content.md:181` [FULL:1707]
```text
OLD: $m_e = 0.51096$ MeV and $m_\mu = 105.652$ MeV against $0.51100$ and $105.658$ observed ($0.007\%$ and $0.006\%$; SM §7.2)
NEW: $m_e = 0.51098$ MeV and $m_\mu = 105.656$ MeV against $0.51100$ and $105.658$ observed ($0.003\%$ and $0.002\%$; SM §7.2)
```

**M5** `book/ch06-matter-content.md:189` [FULL:1715]
```text
OLD: | $0.51096$ MeV | $0.5110$ | $0.007\%$ |
NEW: | $0.51098$ MeV | $0.51100$ | $0.003\%$ |
```

**M6** `book/ch06-matter-content.md:304` [FULL:1830]
```text
OLD: | $0.51096$ MeV | $0.51100$ MeV | $0.007\%$ |
NEW: | $0.51098$ MeV | $0.51100$ MeV | $0.003\%$ |
```

**M7** `book/ch06-matter-content.md:344` [FULL:1870]
```text
OLD: ($m_e$ at $0.007\%$ and $m_\mu$ at $0.006\%$
NEW: ($m_e$ at $0.003\%$ and $m_\mu$ at $0.002\%$
```


***

## After approval

1. **Regenerate artifacts.** Rebuild the `.tex`/`.pdf` of every edited paper (GR, SM, Main, Substratum, Structure, Methodology, Explainer, Juno) and the book (`sh ./build.sh --book`). `book/README.md` is not built.
2. **Coverage ledger.** Under O1-A only, re-affirm `SUBSTRATUM:T-23`, as given in O1.
3. **Re-grep for residue.** Check "value of $\hbar$", "derives Planck", "deriving $\hbar$", "0.02\%" with θ₀, "0.2227", "1776.86" and "105.74". The expected survivors are:
   - CONTEXT-OK sites per the audit (e.g. GR:108, :158; ch02:134 "the same value of $\hbar$");
   - the O6-A rows (i), which deliberately keep 105.74 with its new label.
