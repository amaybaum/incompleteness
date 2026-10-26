# Independent review: ħ framing and θ₀ audit (PR #939, 12e34875)

**Scope.** Read-only and independent. I reviewed `verification/audits/manuscript/hbar-theta0-20261026/` at `12e34875`,
whose only parent is `c967d6a9` (#937 merged). The PR adds only the audit record.

**How the snapshot was taken.**
- Sources come from `git archive 12e34875 papers book tools`, in `S/hbar-theta/review/snap`.
- The audit files come from `git show`, because `.gitattributes` marks `verification/audits` export-ignore and
  `git archive` therefore omits them. They are in `S/hbar-theta/review/audit`.

**Constraints observed.** No worktree, commit or push. Git ran with `-c gc.auto=0 -c maintenance.auto=false`; Python
with `python3 -I`. My own code is in `S/hbar-theta/review/mine/theta0.py`. I did not reuse `koide_theta0.py`; I only
replayed it.

## Verdict: ACCEPT WITH CHANGES

The audit's ħ account is correct, and its θ₀ recomputation reproduces exactly. All seven INCORRECT verdicts stand.

It needs the following before edits proceed:
- **one correction** (O6: "105.74 MeV" is reproduced; it is not a stale or unreproducible figure);
- **one rule** for O4 (a two-sided 95% interval; the central-value "bound" is not a valid rule);
- **six missed sites**;
- **four replacements** that still carry an overclaim from the same sentence;
- **one reclassification** (ch07:82 → needs-qualification).

***

## 1. What is derived about ħ — CONFIRMED

Read at GR:74–78, :108, :144, :148, :156–158 and :310.

| Item | Corpus text | Review |
|---|---|---|
| D1 | GR:78: the action scale $a_*$ is "what this section does"; GR:108: "By partition-relativity … ħ is derived, not free" | ✓ D1 is the right reading: fixed by the partition, not a free parameter of the emergent description, not a numerical value |
| D2/D3 | GR:144: boundary-only; A excluded by observer-universality, κ by universality, leaving $c^3\epsilon^2/G$ | ✓ Note that κ's exclusion rests on the *observed* universality of ħ, so D3 is a dimensional argument with an empirical premise |
| D4 | GR:148: "a conditional infrared calibration, not a theorem within the derived QFT" (H-Hawking, H-spectrum); GR:74: H-slope is the minimal condition; GR:76: H-slope is "a horizon-specific selection test on that open lift", not given by finite realization or reversibility | ✓ |
| Value | GR:158: "ε is the free geometric input, ħ is the output"; GR:310: "self-consistency condition, not an independent determination … fixes only the ratio ε/√σ = 2 l_p" | ✓ Not derived |

**Anchor note (not an audit error; for the owner).**
- GR:148 calls the matching "a conditional infrared calibration". It then ends: "The matching $T_{\rm cl} = T_Q$ is
  therefore not an additional assumption but a consequence of the boundary modes being the same physical objects."
- The two statements are compatible only if the forced part (equal temperatures for the same modes) is kept apart from
  the conditional part (that $T_Q$ has the KMS form, which needs H-Hawking, H-spectrum and H-slope).
- Downstream replacements should cite "conditional calibration" and should not quote the "not an additional assumption"
  clause.

## 2. Classifications

### 2.1 All seven INCORRECT verdicts — CONFIRMED

| Site | Review |
|---|---|
| ch07:10 [F1889] | ✓ It names κ and A as fixing "the values of … ħ". GR:144 and ch07:48/54 exclude both, and GR:310 rules out the value. **Replacement needs the change in §5 (R-a).** |
| ch07:50 [F1929] | ✓ Verbatim contrary to GR:148, and the sentence is garbled. The replacement is correct. |
| ch09:71 [F2551] | ✓ (status surface). See O3. |
| appendix-b:211 [F5978] | ✓ Verbatim contrary to GR:148. The replacement is correct. |
| SM:1378 | ✓ Consistency relations listed as "structural predictions … These are theorems". σ is missing from ħ = c³ε²/(4G). **Replacement needs R-c.** |
| Substratum:180 | ✓ "detailed balance (consequence of φ being a bijection)" is the opposite of GR:76. |
| Substratum:182/184 | ✓ GR §3 contains three theorems (Bohr-frequency completeness, D-gauge completeness, coherent-completion classification) and none for the gap equation's uniqueness. "[GR §3, Theorem]" and "Status: Theorem" are unsupported. |

### 2.2 OVERSTATED — spot-checked 31 of 37

All 31 quoted texts were verified to exist verbatim at the cited lines:
- **Book:** ch07:36, :82; ch01:87; ch02:22, :110, :228; ch00:97; ch04:204; ch06:348; ch09:14, :92; ch12:197;
  glossary:73; readers-guide:77; appendix-b:16, :173, :471; appendix-c:238, :257.
- **Papers:** GR:18, :336; Main:684; SM:1350, :1576; Substratum:22; Structure:47; Methodology:339; Explainer:411, :477,
  :662, :992.

Their classes are confirmed, with one exception:
- **ch07:82 → NEEDS-QUALIFICATION, not OVERSTATED.**
  - "Not an additional empirical input but an algebraic consequence of … $\hbar = c^3\epsilon^2/(4G\sigma)$ together
    with the definition of $l_p$" is literally true: the measured ħ is already inside $l_p$, so nothing *additional*
    enters.
  - The next sentence says "a *constraint* on ε, not an independent measurement".
  - The proposed replacement is still a useful clarification; keep it under the corrected class.

### 2.3 Misses

ħ (U+0127), ℏ (U+210F) and `\hbar` were all grepped against value / derive / determin / fix / predict / theorem /
identity / emerg / output. Six sites were missed:

| Site [F] | Text | Class | Replacement |
|---|---|---|---|
| ch07:14 [F1893] | "…stated where they are derived: the value of $\hbar$, the discreteness scale … and the Bekenstein-Hawking $1/4$ coefficient require … H-slope" | OVERSTATED (value) | "…stated where they are derived: the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the discreteness scale … and the Bekenstein-Hawking $1/4$ coefficient require …" |
| appendix-c:20 [F6266] | "circularity concerns (particularly around the gap equation deriving $\hbar$)" | OVERSTATED (as appendix-c:236) | "(particularly around the gap equation for $\hbar$)" |
| book/README:64 (not mirrored) | "the framework's $\hbar$ derivation from thermal self-consistency at the cosmological horizon" | OVERSTATED (as glossary:73) | "the framework's action-scale relation for $\hbar$ from thermal self-consistency at the cosmological horizon" |
| GR:170 | "Step 4 will fix its value via thermal matching" | OVERSTATED (in the anchor paper itself) | "Step 4 will fix it in terms of $\epsilon$ via thermal matching" |
| ch09:76 [F2556] | "…with the strongest confirmations at the universality-class level" | OVERSTATED (propagation of O3 and #937 owner item 2). That level now holds consistency relations, a descriptive distinction, the area theorem (preserved, not predicted) and a non-discriminating RVM form. | "…with the universality-class level consistent with observation rather than sharply tested and the open research program concentrated at the bijection-specific level" (matches ch09:132's own wording) |
| ch06:332 [F1858] | "eight Category A rows representing seven independent relations (the Koide relation and its angle have separate rows)" | INCORRECT once O2 is accepted (propagation) | See O2 |

**Not over-corrected.**
- GR:108 ("ħ is derived, not free", Step 1) and GR:158 ("a genuine determination", in a paragraph stating "ε is the free
  geometric input") are correctly CONTEXT-OK. The audit's edits to them are optional, and I recommend leaving both
  anchors untouched.
- Sampled CORRECT and CONTEXT-OK sites are correct as classified: GR:30, :164, :641 ("The ħ derivation (§3) uses:
  … H-slope"), ch07:57, :61 (the relation in the same sentence), Explainer:507, ch02:134, ch03:80.

## 3. θ₀ — independent recomputation (`mine/theta0.py`)

**Method.**
- θ₀ is taken as the argument of the discrete Fourier mode $\sum_k \sqrt{m_k}\,e^{-2\pi i k/3}$, with k = 0 τ, 1 e, 2 μ.
  This is a different route from the auditor's solver.
- A = 2|F|/(3μ). mpmath at 60 digits.
- Controls:
  - masses rebuilt to 3e-58;
  - Q − (1/3 + A²/6) = 0;
  - the exact Koide point returns 2/9 to 3e-61.
- The auditor's two scripts also replay byte-identical.

| m_τ (MeV) | θ₀ | rel. dev. | pull | Q | rel. dev. | pull |
|---|---|---|---|---|---|---|
| PDG 2024: 1776.93 ± 0.09 | 0.2222248 ± 0.0000063 | +0.00114 % | 0.41σ | 0.6666645 ± 0.0000051 | −0.00033 % | 0.43σ |
| PDG 2016–22: 1776.86 ± 0.12 | 0.2222296 ± 0.0000083 | +0.0033 % | 0.89σ | 0.6666605 ± 0.0000068 | −0.00092 % | 0.91σ |

**Results.**
- **SM:903's "0.001% (0.4σ)" is confirmed.**
- **"0.02%" is stale.** `git show bd7ae77c` (2026-08-11) changes "Observed: $\theta_0 = 0.22227$. Match: $0.02\%$" into
  the current SM:903 line, and updates the uniqueness table and the §7.6 row. The other sites were left behind.
- **SM:928/934's "0.2227" and SM:940's "0.2%"** are the dropped-digit form of 0.22227.
- **Mass chain:**
  - m_τ = 1776.93 gives m_e = 0.510983 MeV (−0.0031 %) and m_μ = 105.6562 MeV (−0.0021 %);
  - m_τ = 1776.86 gives 0.510963 (−0.0070 %) and 105.6520 (−0.0060 %).

  So "0.51096 / 105.652 (0.007 % / 0.006 %)" is the stale m_τ, as the audit says.
- **"m_μ = 105.74 MeV (0.07 %)" — the audit is WRONG to call this unreproduced.**
  - It is the Koide closure using the *structural* $m_e/m_\tau = 1/(36\pi^4)$, i.e. m_e = 0.5067 MeV, rather than the
    observed m_e.
  - That gives 105.737 MeV (m_τ 1776.86) or 105.741 MeV (1776.93), and $m_\mu/m_\tau = 0.059508$.
  - This is exactly what ch06:192 describes ("the implied $m_\mu/m_\tau = 0.0595$ from Koide closure agrees … ($0.07\%$)
    … than the $m_e/m_\tau$ structural relation itself ($0.84\%$)").
  - On PDG 2024 the deviation is 0.078 %, i.e. "0.08 %". See O6.
- **Koide Q (O7).** The #937 value at ch00:77 and glossary:97 (0.666661 ± 0.000007, 0.8σ) is on the PDG 2016–22 m_τ. On
  SM:903's PDG 2024 basis it is **0.666664 ± 0.000005 (0.4σ)**. "Better than 0.001 %" holds either way.

The θ₀ site list is complete against my grep, and the FULL mirror lines are verified for 24 sampled sites. The ch06:171
and ch06:320 INCORRECT verdicts are confirmed: θ₀ and Q are independent (SM:895, "Both Koide degrees of freedom").

## 4. Owner decisions O1–O7

| # | Real decision? | Recommendation |
|---|---|---|
| O1 Substratum §3.4 "Status: Theorem"; H-slope in Theorem 23 / Structure:47 / Methodology:339 | Largely **settled by evidence**: GR:148 says "not a theorem", GR §3 has no such theorem, GR:76 says H-slope is not implied, and the owner's directive covers it. | Apply. Lean census: no kernel anchor for "Theorem 23" or "Stage 3" (checked the census JSON and `.lean`), so no registry change under §A.35. The other citers of Theorem 23 (Complexity:314; Computation:68, :78; Methodology:333; Structure:138, :195, :768; ch03) carry no ħ clause, so no further propagation is needed. |
| O2 ch06:320 Q vs θ₀ | **Real**, because it changes a count, but the evidence favours (a). | (a) Eight relations. Category A counts relations by observable (A, \|V_cb\| and sin²θ₁₃ are listed separately despite shared inputs), and Q and θ₀ are independent observables. Propagate to ch06:332 [F1858], which the audit missed: "eight Category A rows representing seven independent relations (the Koide relation and its angle have separate rows)" → "eight Category A rows, each an independent relation". "Five empirical channels" is unchanged (Q and θ₀ share the lepton-mass channel). |
| O3 ch09:71 | **Settled by precedent.** In #937 the owner removed consistency identities from prediction tables (ch07, GR §7.4, ch09 Tier 1). | Remove them from the "Predictions" cell: "Level G4 (universality class) \| RVM reading (form shared by every smooth model) \| non-discriminating; the consistency relations $S = A/(4l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ and the descriptive CC distinction are stated in Chapter 7 §7.10". Also fix ch09:76 (§2.3). |
| O4 SM:940 / ch06:179 dressing bound | **Real**: the bound rule. It must be fixed on statistical grounds, before seeing which way the margin falls. | **Rule:** the dressing must keep the prediction inside the two-sided **95 % (2σ)** interval of the observed θ₀, sign-resolved. With dθ₀/θ₀ = −27 δm/m (κ = −35, 1 − λ_E/λ_A₁ = 0.76–0.78), Δ = +1.14e-5 and σ = 2.84e-5 (relative): δm/m ∈ [−2.5, +1.7]×10⁻⁶, i.e. **\|δm/m\| ≲ 1.7×10⁻⁶** on the tighter side. The audit's "central-value bound ≈ 4×10⁻⁷" is not a valid rule: a central deviation is a measurement, not an upper limit. Consequence: a "∼10⁻⁶" loop lies inside by a factor ≈ 1.7–2.5. That is order-unity, given that ∼10⁻⁶ is itself an order estimate. At 1σ it would fall outside on one sign. So the text must not say "satisfies". **Replacement (SM:940):** "The agreement of $\theta_0 = 2/9$ with the observed value ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing by $|\delta m/m| \lesssim 2\times10^{-6}$ at 95% confidence; a second-order lepton-Yukawa loop, of order $10^{-6}$, is compatible with that bound but not by a decisive margin." Mirror at ch06:179 [F1705]: "…the observed agreement constrains it to $|\delta m/m| \lesssim 2\times10^{-6}$ at 95% confidence, which a lepton-Yukawa loop of order $10^{-6}$ does not exceed, though not by a decisive margin." The older "~80×" margin was an artifact of the stale 0.2 %. |
| O5 "sharpest" | **Settled.** appendix-a:98 and :215, the status surface, already name Koide Q the sharpest; on PDG 2024, Q (0.0003 %) is tighter than θ₀ (0.001 %) in relative terms, with equal pulls. | Remove "the sharpest empirical agreement/match" from the θ₀ sites (ch04:134, ch06:171, Substratum:446). SM:1329: "the two tightest (λ at 0.04 %, θ₀ at 0.02 %)" → "two of the tightest (λ at 0.04 %, θ₀ at 0.001 %)". This is accurate, since Q is tighter than both, and it keeps the candidate-family argument, which concerns λ and θ₀. |
| O6 ch06 chain rows | **Mostly settled, once corrected.** | (i) **§6.6 table, ch06:190 [F1716]:** keep 105.74. Relabel the formula "Koide closure with the structural $m_e/m_\tau = 1/(36\pi^4)$ and $m_\tau$". On PDG 2024 the deviation is "0.08 %"; ch06:192's RG discussion stands, with 0.07 % → 0.08 %. m_e row: 0.51098 MeV, 0.003 %. (ii) **§6.8 table, ch06:304–305 [F1830–1831]:** mirror SM §7.6 (SM:1269–1270): m_e "Koide$(Q,\theta_0;\,m_\tau)$ \| 0.51098 MeV \| 0.003 %", m_μ "Koide$(Q,\theta_0;\,m_\tau)$ \| 105.656 MeV \| 0.002 %". The audit's values are right here; its reason is not. (iii) **Six-mass chain table, ch06:217–218:** the table is a chain from predicted m_τ = 1755, so its m_e and m_μ rows must use the chain's m_τ, as SM:983–984 does: "0.505 MeV \| 1.2 %", "Koide$(Q,\theta_0;\,m_\tau)$ \| 104.4 MeV \| 1.2 %". Settled by the chain's own definition. |
| O7 Koide Q basis | Nominal. Settled by the directive ("one authoritative definition" = SM:903, PDG 2024). | Harmonize: ch00:77 [F313] "the observed value is $0.666664 \pm 0.000005$, a match to better than $0.001\%$ ($0.4\sigma$)"; glossary:97 [F6697] the same. SM:1267 "0.66666 \| < 0.01 %" → "0.666664 \| 0.0003 %". ch06:302 [F1828] "0.66667, 0.001 %" → "0.666664, 0.0003 %". |

## 5. Replacements — four that leave an overclaim in the same sentence

**(R-a) ch07:10 [F1889].** The proposal keeps "fix … the Bekenstein-Hawking entropy … and the form of the dark-energy
equation of state" unconditional. GR:12 and §7.1 call the RVM form "a structural reading, not a derived law" and its
form "the local expansion shared by every smooth model". The audit notes this in §4 but leaves it in the sentence it
rewrites. Replace the last sentence with:

> "The horizon's thermodynamics relates the emergent action scale $\hbar$ to the discreteness scale $\epsilon$, with
> $\kappa$ and $A$ dropping out of $\hbar$ (Sections 7.3–7.4); it recovers the Bekenstein-Hawking entropy with its $1/4$
> coefficient as a consistency relation of that calibration and supplies the dark-energy bookkeeping read in the
> running-vacuum channel (Section 7.8)."

**(R-b) Explainer:662.** The proposal keeps "a quantitative prediction — dark energy evolution". Use:

> "It relates ℏ to the discreteness scale and carries a running-vacuum reading of dark energy whose falsifiable content
> is the Type II channel ([GR §7.1]) — content that interpretations do not have — and it accounts for …"

**(R-c) SM:1378.** The proposal keeps "These are theorems" for a list that includes the three generations, which are
conditional on the Tier-2 branch (SM:32). Use:

> "These are theorems on the branch stated in §1 (Tier 2), with the conditions marked at each entry."

**(R-d) SM:1350.** This sentence is being edited for ħ. Apply #937's standard to its CC clause in the same edit: "the
dissolution of the cosmological constant problem" → "the conditional dissolution of the cosmological constant problem
([GR §6.2])". Leave its "dynamical dark energy prediction" to the deferred dark-energy item.

**The rest are accepted.** Including ch07:50, appendix-b:173/:211, glossary:73, Substratum:22/178/180/184/192,
Structure:47, Methodology:339 and Main:684, the replacements:
- neither overclaim nor underclaim: each keeps the relation, the condition and "not the value";
- add no assumption beyond GR's stated conditions;
- carry no history narration;
- name FULL lines that match the sources.

## 6. Record nits

- AUDIT.md:8 says the scripts are "in `S/hbar-theta/scripts/`", but they are committed in `scripts/`.
- §2.3's row for ch06:189–190 "not reproduced" is wrong (O6).
- §1.4 counts must add the six misses: OVERSTATED 37 → 41 (ch07:14, appendix-c:20, README:64, GR:170); 1 site
  NEEDS-QUALIFICATION (ch07:82, moved out of OVERSTATED: 41 → 40); plus ch09:76 (O3) and ch06:332 (O2) as propagation
  sites.
- glossary:97 mirrors FULL:6697 (the audit gave no FULL line for it).

## Findings (numbered)

1. ħ account D1–D4 and "value not derived": **confirmed** (§1).
2. Seven INCORRECT: **all confirmed** (§2.1).
3. OVERSTATED spot-check (31/37): **confirmed**, except ch07:82 → NEEDS-QUALIFICATION.
4. Six missed sites (§2.3): ch07:14, appendix-c:20, book/README:64, GR:170, ch09:76, ch06:332.
5. CONTEXT-OK anchors GR:108 and GR:158: correctly left alone. Recommend not applying the optional rewordings.
6. θ₀ 0.001 % (0.41σ) and Q 0.0003 % (0.43σ) **independently confirmed**. 0.02 % is the pre-`bd7ae77c` figure; 0.2 %
   and 0.2227 are its dropped-digit form.
7. **Audit error:** 105.74 MeV is the closure with the structural $m_e/m_\tau$, reproduced exactly. Correct O6 as in §4.
8. O4 rule: two-sided 95 % interval, sign-resolved → |δm/m| ≲ 2×10⁻⁶. The loop is compatible, margin about two;
   "satisfies" must go. Exact text in §4.
9. Replacements R-a to R-d (§5) to avoid leaving overclaims in edited sentences.
10. GR:148's internal tension, "conditional calibration" vs "not an additional assumption", is flagged for the owner
    (anchor, not an audit error).
