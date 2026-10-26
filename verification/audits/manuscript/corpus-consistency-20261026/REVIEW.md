# Independent review: corpus-consistency audit (draft PR #937, head afd7d1d0)

Reviewer: independent of the audit's author. Read-only: nothing in the repository was edited, committed or pushed.
- Corpus: `S/cc2/wt` (main `687e885b` + `afd7d1d0`). Full history: `S/ppe/repo`.
- #936 boundary: `S/bhfix/wt` at `b61cbaa9`.
- Every git command ran with `-c gc.auto=0 -c maintenance.auto=false`. Python ran with `python3 -I`.
- My own scripts are in `S/cc2/review/` (`mine/quarter3.py`; `run/` holds the replays).

`S` is the session scratch directory (absolute prefix elided).

## Overall verdict: ACCEPT WITH CHANGES

All 13 INCORRECT findings survive independent re-reading. No verdict is rejected. The audit's direction is right
throughout, so nothing blocks it. Before the record is used to drive manuscript edits, it needs the following fixes.

1. **Its own tally is wrong.**
   - The summary table has **34** rows, not 29.
   - The OVERSTATED list names **18** rows but is labelled "15".
   - Mixed rows (1.7, 2.3, 2.7, 3.5, 8) are classed inconsistently.
   - Corrected tally, by the primary class of each row: INC 11, OVR 18, NQ 4, OK 1 = 34. Add 2 INC clauses inside OVR
     rows (1.2, 3.6). Secondary OVR clauses sit in 1.7, 2.7 and 3.5; secondary NQ clauses in 2.3 and 8.
2. **Six replacements need rewording** (items 1.5, 1.6, 1.7, 3.3, 5 and 3.1's placeholder; wording below).
   - Item 1.5's replacement contradicts the audit's own item 1.6. It says the calibration "fixes the value of ħ", but GR:310
     says only ε/√σ is fixed.
3. **The Cabibbo S→C recount (§4.6) is internally inconsistent as proposed.**
   - Under the weakest-link rule the audit applies, Koide Q and θ₀ must go to C as well. SM:895 itself states that their
     open link is weaker than Cabibbo's.
   - Wolfenstein A and λ(M_Pl) = 0 were not audited, so "4 S" is provisional.
4. **Missed sites** (list below). The main gaps:
   - unconditional "does not gravitate" / "dissolved" sites: ch07:207, ch07:258, ch09:90, GR:32, Substratum:324,
     SM:132, Explainer:22, :547;
   - ch19:38, which must be made conditional, not left optional;
   - ch18:18 (echo);
   - the GR:358 / ch19:28 / Explainer:699 count "seven", once item 2.6 is accepted;
   - Main:740's corollary title.
5. **Record hygiene** (§A.28/§A.42):
   - `mirror.sh` hard-codes the session scratch path, so it does not run from a checkout of main.
   - AUDIT.md:6 reads "`S` = `S`".
   - AUDIT.md:9 cites `S/cc2/scripts/`, but the scripts are committed under `scripts/`.
   - The PDG digest is truncated. The full sha256 is
     `a0a78578971f38ff89c6fc5579bc608de41ec383a205dc25cba1d26f7145610a`.
   - "Nothing in the repository was edited, committed or pushed" is false for the committed record.
   - The #936 head is stale: `4c0d705e`, now `b61cbaa9`.
6. **Sequencing.**
   - Land after #936, or rebase onto it. Several proposed edits sit on lines adjacent to #936's edits: ch19:333 and :334
     are consecutive table rows (FULL 5509/5510), ch18:160 follows :158, and GR:603 sits near :605. Git will report these
     as conflicts.
   - The audit's exclusions are otherwise correct (§7).

***

## 1. Per-item table

Verdict key: **CONFIRMED** = verdict and replacement stand. **CHANGED** = verdict stands; the replacement, rationale or
scope is corrected (exact wording given). **REJECTED** = verdict does not stand (none).

| # | Audit class | Review | Reason / exact new wording |
|---|---|---|---|
| 1.1 | OVR | CONFIRMED | GR:12 attributes the 1/4 to the count. My third derivation (§3) shows the count contributes only S = ηA, and the calibration supplies b/a. GR:24 already carries the correct wording. |
| 1.2 | INC clause + OVR | CONFIRMED; CHANGED (scope) | The "postulate" premise is false. GR:322 itself says "T = ħκ/2πck_B plus the first law fixes it". The audit gives no replacement for ch00:81 or preface:7; add them. **ch00:81/317:** "…The framework recovers the 1/4, which the standard account fixes from the Hawking temperature and the first law, as the ratio 2π/8π of its horizon calibration, under the horizon conditions named in Chapter 7." **preface:7/78:** "The Bekenstein-Hawking factor of 1/4 is recovered as a consistency relation of the horizon calibration (conditional on the conditions of Chapter 7)." |
| 1.3 | OVR | CONFIRMED (spot) | GR:322 "derived structural constant" drops H-slope, which GR:320 states. |
| 1.4 | OVR | CONFIRMED (spot) | An "alternative ħ(ε)" would conflict only with Hawking's T_H, which uses the same KMS input. That is not an independent check. Prefer the audit's second option (rewrite) over deletion, so the content survives. |
| 1.5 | INC | CONFIRMED; CHANGED (replacement) | GR:148 inputs T_Q = ħκ/(2πck_B), so "not used as an input" is false. The audit's replacement says the calibration "fixes the value of ħ in it". That contradicts GR:310 ("a self-consistency condition, not an independent determination … fixes only the ratio ε/√σ = 2l_p") and the audit's own row 1.6. **New:** "The Gibbons–Hawking form ħκ/(2πc) enters as the KMS temperature of Step 4; the calibration relates the ħ in it to ε and σ through ħ = c³ε²/(4Gσ)." Same at ch07:65/1942. |
| 1.6 | INC | CONFIRMED; CHANGED (rationale and replacement) | **Rationale.** For the 1/4, "neither QM nor GR *alone*" is literally true: Hawking's result needs both. The defect for the 1/4 is that it is offered as "empirical content" while G4 records no direct test (OVR). The INC verdict rests on the ħ clause (GR:310) and the echo clause (GR:603). **Replacement.** The audit's version drops the MOND scale, which QM and GR do not yield; it is a conditional relation. **New:** "…The framework's treatment carries conditional and consistency relations — the horizon calibration with its 1/4 ratio, the descriptive vacuum-energy distinction, the dark-sector reading, and the MOND scale a₀ = cH/6 conditional on the open coupling map with its factor 1/6 imported — rather than predictions independent of QM and GR; its forward exposure is listed in Appendix A.5." |
| 1.7 | NQ / OVR | CONFIRMED; CHANGED (history wording) | The audit marks its history "[mem]". From memory as well (unverified here): Bekenstein (1973) gave a heuristic coefficient (ln 2/8π), not an undetermined one, and Hawking did not co-introduce it in 1973. **New (GR:320):** "…introduced by Bekenstein (1973) with a coefficient he could estimate only heuristically, and fixed at 1/4 by the Hawking temperature and the first law (Hawking 1975) — is here recovered, under the conditions of the §3 calibration, as…". Owner to confirm the citation first-hand. |
| 1.8 | NQ | CONFIRMED | G4 and row 24 are C. Counts are unchanged (13; 24). |
| 2.1 | INC | CONFIRMED | Favourable reading tried: "theorem of the reconstruction" can refer to the offset's invisibility, which is true. But the last clause ("the problem's premise … attributes physical content to a gauge degree of freedom") infers gravitational non-content from quantum invisibility. GR:356 refutes that inference with two completions that differ in exactly that offset. GR:585 ("applies to each … gravity operates at the classical level") and GR:587 ("therefore does not source curvature") carry the same inference. The replacement is accurate and adds no assumption. |
| 2.2 | OVR | CONFIRMED (spot) | GR:356 opens "dissolution is conditional" and closes "never enters … no decoupling mechanism is needed". This is §A.30 assert-then-qualify. |
| 2.3 | OVR / NQ | CONFIRMED; CHANGED (scope) | Add the missed sites in §4 below. ch19:38 moves from "keep, optionally" to **change**: it has the same assert-then-qualify shape as GR:356. **ch19:38 new:** "…The QFT zero-point energy belongs to the emergent description; that it does not gravitate is the coupling step that [GR §6.2] leaves open." |
| 2.4 | OVR | CONFIRMED | grep of ch07:163–201 for conditional/G3/"coupling theorem"/open returns nothing. |
| 2.5 | OVR | CONFIRMED (spot) | — |
| 2.6 | OVR | CONFIRMED; CHANGED (propagation) | Re-derived: ρ_crit is the Friedmann total, and GR:360 concedes "set by initial conditions". Missed consequence: GR:358 item (1) is one of the "seven mutually independent" entries. If it is a normalization, the count "seven" at GR:358, ch19:28 [5204] and Explainer:699 must be recounted or the item dropped from the count. |
| 2.7 | NQ / OVR | CONFIRMED | Re-derived by hand: (ρ_P/ρ_crit)/S_dS = 8/3; 1/6 at ε = 2l_p; 1/(96π²) for the one-field zero-point integral. Replay of `cc_indep.py` matches byte for byte. |
| 2.8 | OVR | CONFIRMED (spot) | — |
| 2.9 | NQ | CONFIRMED (spot) | GR:579's rule does not decide a transition between two occupied configurations. A hidden assumption; status Open. |
| 2.10 | OK | CONFIRMED | — |
| 3.1 | INC | CONFIRMED; CHANGED (placeholder) | The table counts contradict ch18:349 (§5). The replacement contains "[corrected count: §4.6]" and must be resolved before use. Precision fix: G12 (Σm_ν) is compared with upper bounds. **New gravitational clause:** "the thirteen gravitational-sector entries are conditional relations, identities and estimates, two of them compared with measured values (G6, G8) and one with upper bounds (G12)". The echo clause must go (item 5). |
| 3.2 | INC | CONFIRMED | appendix-a:217: "no pre-registered forward confirmation". The sentence asserts that the standard "is met". No weaker reading is available. |
| 3.3 | INC | CONFIRMED; CHANGED (replacement) | "No fitted parameters" is false by GR:358 item (7). Two further defects in the audit's replacement: (i) ch19:28 attributes the seven to "(T) and the G1/G2 rungs", but GR:358's list includes G4-level items (dark sector, MOND, Bullet Cluster), conditional on G3; (ii) item 2.6 removes item (1) from the independent set. **New:** "…with the consistency relations collected in [GR §6.2] — several conditional on G3, one (the gauge-coupling values) reproduced through three matched parameters, and one (the MOND scale) with an imported factor." |
| 3.4 | INC | CONFIRMED | The "not listed as a forward prediction … magnitude is undetermined" sentence (:203) entered on 2026-06-19 (`1486489e`), *before* the "anisotropy amplitude" was added to the pre-registered list (`9b4177c6`, 2026-07-02). No dated preregistration of a rotational-anisotropy amplitude exists under `verification/`. A clean internal contradiction. |
| 3.5 | INC / OVR | CONFIRMED | Juno:73: "carried out in 2026, after the JUNO first results". Note: the git search (no form before `054eb99a`) is uninformative, since the repository begins in 2026-02, after JUNO. Juno:73 is the decisive support. Optional precision: "parameter-free retrodiction, conditional on Condition 2" (the row is L; SM footnote ᶠ). |
| 3.6 | OVR + INC clause | CONFIRMED; CHANGED (scope) | appendix-c:273 has a second INC clause, missed: "These are all explained as *structural consequences* … not just fit to data" covers the gauge couplings, which are R/E (fitted; SM:1298 note ᵃ). It also lists "gauge group, generation count" among the twenty-two observables, which are not in the 22 (SM:1302, "In addition"). **New appendix-c:273:** "*What the framework retrodicts.* Twenty-two classified Standard Model observables (seven parameter-free structural [or the corrected count]; the remainder layered, chained or fitted, the gauge couplings among the fitted), thirteen gravitational-sector entries (conditional relations, identities and estimates), and the Rett wider therapeutic window." Also add ch09:73/2553 ("0.04%–1.01σ across 22 predictions", which includes the fitted couplings) to the 3.6 list. |
| 4 | OVR (S→C) | CONFIRMED (direction); CHANGED (§4.6 scope) | See §4 of this review. |
| 5 | INC | CONFIRMED; CHANGED (rationale, replacement, sites) | See §6 of this review. |
| 6 | INC | CONFIRMED | GR:52: "(C4) … Not presently discharged"; GR:20: "remains conditional on C4". GR:567 claims the coupling "is (C4)'s realization — so the equivalence applies in our universe". A direct contradiction. |
| 7 | INC | CONFIRMED | The second sentence ("establishes that … three faces … QM … the unique self-consistent description") contradicts Main:22 and the kernel theorem `oi_alone_not_qm` (GeneralCarrier.lean:160, read). The first clause ("establishes the equivalence") is OVR rather than INC, since Main does establish a finite-law equivalence. The replacement handles both. |
| 8 | OVR / NQ | CONFIRMED (spot) | Main:632 scopes Lüders = Bayesian updating to the represented diagonal sector. |
| 9 | OVR | CONFIRMED (spot) | Substratum:354: monotone "for as long as ä > 0". Main:728: (EM) is "an explicit physical hypothesis". |
| 10 | OVR | CONFIRMED; CHANGED (propagation) | Coordinator's input checked. Main:740, Substratum:56, Explainer:930 and Complexity:204 are all in the audit's propagation list. Missed: Main:740's **corollary title** "(past-hypothesis replacement, with its rate condition)" → "(observer-selection rule, with its rate condition)". Incidental §A.33: Substratum:350 narrates revision history ("Before §4.6, the arrow of time was treated as external…; With §4.6 in place…"). The ALL-CAPS "SUFFICIENTLY FAST-MIXING" at Main:740 is confirmed and rule-settled (§A.33). |
| 11 | OVR | CONFIRMED (spot) | ch19:116 says "Derived" and "partly definitional" in one breath. G9 is C. |
| 12 | OVR | CONFIRMED | — |
| 13 | OVR | CONFIRMED (spot) | G6: C, "(factor imported)". |

### The 13 INCORRECT findings at a glance
1.2 premise ✔ · 1.5 ✔ (replacement fixed) · 1.6 ✔ (rationale fixed) · 2.1 ✔ · 3.1 ✔ · 3.2 ✔ · 3.3 ✔ (replacement fixed)
· 3.4 ✔ · 3.5 ✔ · 3.6 appendix-c:273 CC clause ✔ (plus one missed INC clause) · 5 ✔ · 6 ✔ · 7 ✔ (first clause only OVR).

For each I asked whether a reading at the supported strength exists. Only two have a partial one, and neither rescues
the sentence:
- 1.6: the "alone" clause, for the 1/4 only;
- 7: "the equivalence", at the finite-law level.

None of the replacements narrates history in the §A.27/§A.30 sense. "The derivation postdates the measurement" and the
Bekenstein/Hawking history are status and history of physics, not self-narration. 3.1 carries an unresolved placeholder.

***

## 2. Spot checks of OVR/NQ (≥ 2 per area)
- **Horizon:** 1.1, 1.3, 1.4, 1.7, 1.8.
- **CC:** 2.2, 2.4, 2.6, 2.7, 2.9.
- **Counts:** 3.6 and the appendix-c:347/:279 clauses of 3.5.
- **Cabibbo:** 4, plus the 1.8 table logic.
- **Echo-adjacent and other:** appendix-c:279/:347 and ch18:182; items 8, 9, 10, 11, 13.

All are confirmed in class. Changes are as in the table.

***

## 3. The 1/4 verdict — third derivation (independent of both scripts)

`S/cc2/review/mine/quarter3.py` (no sympy) has three parts:

- **(A) Exact `Fraction` arithmetic.** π is carried as a formal factor (a = 8π, b = 2π), over 200 random rational
  (c, G, κ, ε, σ). The coefficient set is **{1/4}**.
  - Countercontrols: a = 8π, b = π gives 1/8; a = 4π, b = 2π gives 1/2.
- **(B) A Clausius route on a real Schwarzschild mass range** (10³⁰ to 3×10³¹ kg).
  - Integrate dS = c²dM / T_cl(M) with the *classical* T_cl = c²ε²κ/(8πGσ). This uses no T_H and no mode count.
  - ε comes from the calibration at measured ħ.
  - Result: ΔS / (ΔA/l_p²) = **0.250000000000** for σ = ln 2, 1 and ln 6.
- **(C) Countercontrol: no calibration** (ε = l_p, σ = 1). The ratio is 1, not 1/4.

**Verdict: confirmed.** The coefficient is b/a = 2π/8π, independent of ε, σ and the mode density. The count contributes
only the area proportionality.

**Scripts.**
- `quarter_indep.py`, `cc_indep.py` and `cabibbo_cmp.py` each replay byte-identical to their committed `.out`.
- quarter_indep's controls are non-vacuous:
  - check 5 (a or b varied → 1/8) and check 6 (no calibration → 1) can fail;
  - check 8 is a genuine transcription control against GR:154.
- Weaknesses, not defects:
  - Check 7 (Hawking route) is algebraically the same equation as check 1, so it is not an independent route.
  - The script and AUDIT §1.0 attribute η = κ_mσ/ε² to GR:98. GR:98 reads η = σ/ε²; κ_m appears in the component-count
    reconciliation. This is harmless, since check 3 covers every η.

***

## 4. Cabibbo (item 4)

### Dating
Re-checked with `git log -S` in `S/ppe/repo` (3,529 commits on HEAD, not shallow).
- `\frac{1}{\pi\sqrt{2}}`, `1/(\pi\sqrt{2})` and `0.22508` first appear in `054eb99a` (2026-04-04 16:16).
  - Its `Predictions.md` §4.1 carries the form, the value and "Observed … 0.22500 ± 0.00067. Match: 0.12σ (0.04%)"
    together.
  - Its justification is "because the generations are fermions".
- `git grep` of `054eb99a^`, with 507 commits before it, finds no "Cabibbo" and no `pi\sqrt{2}`.
- `c_\lambda` first appears in `70ffe82f` (2026-07-05). `190\sigma` and `0.3536` first appear in `3124ef0a` (2026-07-06),
  and its parent has none.
- **Confirmed.**

### Line reference (coordinator input)
- The quoted phrase "emergent dressing pending" is at **SM:849**.
- SM:851 carries the 190σ exclusion and "What remains beyond this structural level is the emergent-theory dressing".
- The audit's §4.2 places both correctly. Row 4 of §0 ("SM:849–851") and §4.5 ("SM:851 leaves the emergent dressing
  open") are accurate but should cite SM:849 for the quoted phrase.

### Reclassification S→C
- The direction is correct under the governing definitions:
  - AGENTS S: "all links Solid";
  - appendix-a A.2: S means "first-principles derivations"; C means "follows given an additional unverified relation".
- SM:849 and :851 leave the emergent dressing open. One alternative dispersion was discarded against the measurement
  (≈190σ; my check: (0.35355 − 0.22500)/0.00067 = 192σ).
- Postdiction plus Conditional is the right owner-scheme reading.
- Inheritors confirmed:
  - |V_cb| = Aλ² (SM table formula √(2/3)/(2π²); appendix-a row 7 already "Conditional on 5,6");
  - sin²θ₁₃ = A⁴λ² = 4/(18π²) (ch06:312; SM:1325 "tested … through its appearances in |V_cb|, sin²θ₁₃, and m_d/m_s").

### Consistency defect in §4.6
- The audit makes the Koide column optional ("owner decision").
- SM:895 says the Koide amplitude is "not yet derived from the dynamics — one-loop … gives A² ≈ 0.34, undershooting
  C₂ = 2", with θ₀ "the same footing". SM:849 calls Cabibbo's open link "complementary to (rather than the same footing
  as)" Koide's.
- Demoting Cabibbo while keeping Koide Q and θ₀ at S would rank the weaker chain above the stronger one.
- The same rule therefore *requires* Koide Q and θ₀ → C. Wolfenstein A (A² = C₂/d, same Casimir) and λ(M_Pl) = 0 are
  unaudited.
- Either:
  - (a) apply the strict S definition uniformly: SM S ≤ 2 (A, λ(M_Pl) = 0, pending their audit);
  - (b) keep SM's local S ("no fitted input", SM:1255) and strike "unconditional" from SM:1298 and ch06:318, which
    leaves the counts unchanged.

  The audit's middle course is not consistent.

### PDG
Checked against `S/cc2/pdg/ckm2025.txt`:
- 0.22501 ± 0.00068 (12.26); 0.22497 ± 0.00070 (UTfit); 0.2233 ± 0.0005 (Kℓ3); 0.2250 ± 0.0004 (Kμ2);
  0.22431 ± 0.00085 (12.8, χ² scale 2.5); 0.2207 ± 0.0014 (τ); "2.3σ tension with unitarity in the 1st row" — all
  verbatim.
- Pulls are reproduced.
- The review is "Revised April 2024", as the audit says.
- Addition: PDG also quotes a tree-level-only fit λ = 0.22509 ± 0.00068, which the audit omits. It does not change the
  reading.
- The "0.04%" holds against the unitarity-constrained fit only. The NQ on naming the source is confirmed.

***

## 5. Recomputed counts (from the tables themselves)

| Table | Rows | Recount | Matches stated? |
|---|---|---|---|
| SM §7.6 (SM:1259–1280) | 22 | S 7 (λ, A, \|V_cb\|, Koide Q, θ₀, sin²θ₁₃, λ(M_Pl)); L 6 (m_d/m_s, m_b, m_u/m_d, sin²θ₁₂, sin²θ₂₃, m_b/m_τ); R 3 (α₂, α₃, m_t); E 2 (α₁, J); M 3 (m_e, m_μ, m_H); P 1 (Q_down) | yes (SM:1298; SM:1300 "7 + 6 = 13") |
| appendix-a A.4.1 | 24 | S 8 (1, 5, 6, 7, 10, 11, 13, 22); C 3 (2, 23, 24); L 8 (8, 12, 14, 16, 17, 18, 19, 21); M 1 (15); R 2 (4, 20); E 2 (3, 9) | yes (:95) |
| appendix-a A.4.2 | 13 (G10 absent) | S 2 (G7, G14); C 9 (G1–G6, G9, G11, G13); L 2 (G8, G12) | yes (:121) |
| appendix-a A.4.3 | 7 | S 2 (N2, N5); L 5 (N1, N3, N4, N6, N7) | yes (:139) |
| ch07 gravitational table (ch07:294–307) | 14 | — | yes (ch07:323 "fourteen entries in this chapter's table"; a different inventory from A.4.2's 13, so no contradiction) |
| ch06 table | 24 | 8 S (7 Category A + one input row) | not in the audit's §4.6; three of its Class cells change under item 4 |

The audit's corrected counts check, *if* only Cabibbo, |V_cb| and sin²θ₁₃ move:
- SM: 4 S + 3 C + 6 L + 3 R + 2 E + 3 M + 1 P = 22;
- A.4.1: 5 S + 6 C + 8 L + 1 M + 2 R + 2 E = 24;
- A.4.3: 1 S + 1 C + 5 L.

With Koide Q and θ₀ (required, §4):
- SM: 2 S + 5 C + 6 L + 3 R + 2 E + 3 M + 1 P;
- A.4.1: 3 S + 8 C + 8 L + 1 M + 2 R + 2 E;
- A.4.3: unchanged from the line above.

**Count-site grep.**
- I grepped papers/ and book/ chapters for "twenty-two | thirteen | seven (parameter|neutrino|independent|structural|
  unconditional) | seven of | 7 structural | 22 (SM|predictions…)", and separately for "seven/7" within 60 characters of
  "parameter-free|structural|unconditional".
- Every hit is either in the audit's lists or is a different count. Different counts: the seven-category scheme, the 7/6
  sum rule, "seven structural inputs" (ch02:54), Explainer:769 and :860 (different sets), and the 24-element cube group.
- **Missed (count family):**
  - ch09:73/2553 "0.04%–1.01σ across 22 predictions" (includes fitted couplings; 3.6 family);
  - GR:358 "seven of the entries are mutually independent" (item 2.6 removes item (1)), with its echoes ch19:28 and
    Explainer:699;
  - ch04:74 "some S-class, some C-class" (currently no C row in SM's 22; becomes true only under item 4);
  - borderline, not required: Substratum:38, :322, :368, :404; ch03:10, :18, :122, :212, :240; ch02:218; ch06:287;
    Structure:380; readers-guide:27 ("twenty-two quantitative predictions/retrodictions", no "parameter-free").
- The audit's "seven parameter-free" list is complete against my grep.

***

## 6. Echoes (item 5)

### Is GR:603 the maintained statement?
- **Commit dates do not establish it.**
  - In full history, GR's "no OI-specific echo" and the 5.9σ null first appear in `30fb2bfc` (**2026-04-08**), not
    `8f50f9b6` (2026-04-09) as the audit says.
  - The book's §18.6 entered with `334eef0a` (2026-05-14), i.e. *later*, as a bulk "add book files".
  - Both were last touched on 2026-10-15, by `dcc90bf1` (GR) and `03131c9d` (book). Both commits are σ-mechanical
    (ε = 2√σ l_p) and do not change the echo stance.
- **Content does establish it.**
  - GR:603 gives an argument: the external observer's partition is set by the cosmological horizon, not the black-hole
    horizon.
  - The book's reflection fraction "∝ ε/r₊" has no derivation anywhere in papers/ or book/.
  - The book is self-inconsistent: F5 says "next observing runs", ch18:172/:180 say "below threshold", and :208 vs
    :178 disagree on a null.
- The verdict stands on content (§A.25: the most careful statement is the anchor). The audit's §5.2 "Dating" paragraph
  should say this, not imply priority.

### Retention claim
- `git ls-files` outside papers/ and book/, grepped for echo stack/template, matched-filter, "stacked statistic",
  5.9σ, p = 0.66 and O1–O4, finds nothing. The claim is **confirmed**.
- The off-main research archive (`4dc0321c`, not an ancestor of main) shows no echo-stack file either (cursory check).

### Replacement
The audit's ch18 replacement states "the framework predicts no OI-specific echo", while its own status is Open. Match
the status. **New ch18 §18.6 core:** "[GR §8.4] argues that a black-hole horizon does not change an external
observer's partition, which is set by the cosmological horizon, so no OI-specific echo, comb or wall-reflection
feature is expected and ringdowns follow general relativity; no echo amplitude is derived."

### Missed site
- ch18:18/FULL:4838: "Section 18.6 develops gravitational wave echoes as a forward prediction … the framework's most
  directly observable signature of substratum discreteness".

***

## 7. The #936 boundary

The changed lines were computed from `git diff -U0 687e885b..b61cbaa9`.

- **Correct at `4c0d705e`.** The audit's header ranges cover every line #936 changed at that head.
- **Stale at `b61cbaa9`.** #936 now also changes:
  - ch07:147 (FULL:2024 is inside the audit's FULL range, but ch07:147 is not in its chapter list);
  - GR:833 (inside "805–869").

  Neither line is touched by any proposed edit, so there is no overlap.
- **Over-excluded.** The ranges are wider than the changed lines:
  - ch18 "146–158 (even lines)" includes 152 and 154, which #936 does not change. 152/154 are "third dissolution"
    lines already scoped to G3, so nothing is lost.
  - ch07 "157–161" includes 158 and 160; "130–132" is exact.

  No overclaim is skipped because of this.
- **Overlap.** No proposed edit touches a #936 line. §15's per-line list is accurate.
- **Adjacency (merge-conflict, not ownership).**
  - ch19:333 and :334 (FULL 5509/5510), consecutive table rows;
  - ch18:160 after #936's :158;
  - GR:603 near :605.

  Land after #936.

***

## 8. Owner decisions — genuine vs settled

**Genuinely the owner's:**
1. Whether a consistency relation (G4, row 24) belongs in a prediction-status table (§1.8). This is presentation.
2. The headline wording, "seven parameter-free (four unconditional, three conditional)" vs a changed count (§4).
   Either is true once the classes are fixed.
3. Scope: whether items 6–13 go in this PR or a follow-up.
   - Items 6 and 7 are INCORRECT.
   - Once accepted, §A.27 "same-session propagation" weighs toward including them.
4. Echo evidence: whether the LVK stack evidence can be recovered and retained on main (§A.42).
   - If it cannot, narrowing GR:603 to its structural clause is required by §A.42 item 4. That part is not a choice.
5. The 1/4 phrasing choices (1.4: delete vs rewrite). These are editorial.
6. First-hand confirmation of the Bekenstein-1973 history wording (1.7).

**Settled by evidence or by the rules, not owner decisions:**
- Applying the S→C rule to Koide Q and θ₀ (SM:895 states their weaker footing; AGENTS/A.2 definitions). The only owner
  lever is to amend the S definition itself, i.e. option (b) in §4.
- ch19:38's "does not gravitate". It must be conditional, by the same evidence as 2.2.
- Main:740's ALL-CAPS (§A.33).
- F5's retirement mechanics (§A.30: no reuse, no renumbering, no gap annotation).
- The GR:358 "seven" recount if 2.6 is accepted.
- The audit's own tally (34 rows; OVR 18).

***

## 9. Missed sites (consolidated)

**Cosmological constant.** Coordinator input verified; all confirmed.
- preface:7/78, CC clause "becomes a calculable compression ratio";
- ch00:21/257, "calculable ratio rather than a fine-tuning failure";
- ch00:89/325, "as an information compression ratio … all follow";
- Explainer:22, "strongest piece of existing evidence";
- Explainer:547, "not a discrepancy. It equals S_dS" (it equals it only up to a convention-dependent factor of
  1/(96π²) to 8/3);
- ch19:38/5214, "does not gravitate" (must change, not optional).

Further, found by me:
- GR:32, "§6 dissolves the cosmological constant problem";
- Substratum:324, CC clause "dissolves the cosmological constant problem";
- SM:132, "the same classical priority of geometry that dissolves the cosmological-constant problem";
- ch07:207/2084, "Section 7.7 established that the emergent QFT's vacuum energy does not gravitate";
- ch07:258/2135, "(does not gravitate)";
- ch09:90/2570, "vacuum energy … that does not gravitate".

None of these is a #936 line.

**Echoes:**
- ch18:18/4838.

**Counts:**
- ch09:73/2553;
- GR:358, with ch19:28/5204 and Explainer:699 (the "seven", after 2.6);
- appendix-c:273/6541, second INC clause (gauge couplings "not just fit"; gauge group and generation count listed among
  the 22).

**Arrow of time:**
- Main:740, the corollary title;
- Substratum:350, §A.33 revision-history voice.

**Cabibbo:**
- the ch06 table's Class cells for the inheritors, in the §4.6 recount;
- appendix-a:95's "The conditional entries here are …" sentence, which changes with item 4.

**Record:**
- mirror.sh's hard-coded scratch path;
- AUDIT.md:6 and :9;
- the truncated digest;
- the stale #936 head;
- the "nothing … committed" sentence.
