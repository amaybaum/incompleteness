# R1-L8 Stage 1(i) — preregistration: horizon-entropy normalization provenance

**Status.** Writer's paper-only preregistration, committed and pushed before any result is
classified. The classification is `AUDIT.md` in this directory, in a later commit. Existing
evidence only: no new measure construction, no new physical assumption, no manuscript, Lean or
registry edit, no promotion of a conditional result. A1 (Main posit ledger item (ii)) remains open
and unadopted. Independent non-author review is required before any use of the audit; the unit
stops after the dependency verdict and that review.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7041456852](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7041456852),
2026-11-20T14:01:28Z, "Owner decision record: R1-L8 Stage 0 landed; Stage 1(i) authorized". Quoted:
"**Question:** which definition of horizon entropy actually supplies the normalization in OI's
gravitational results? Trace three alternatives: State-counting entropy … Clausius entropy …
Imported Bekenstein–Hawking normalization … For each alternative, trace the consequences for:
a₀ = cH/6; the Tully–Fisher normalization; ρ_s = ρ_crit; the 2/(d−1) concordance factor."
"**Deliverable:** classify each result as genuinely derived, externally calibrated, conditional, or
unresolved." "**Restrictions:** paper-only, using existing evidence; no new measure constructions;
no new physical assumptions; no manuscript changes; no promotion of conditional results." "**Stop
rule:** stop after the dependency verdict and an independent review. No successor is started
automatically."

**Goal link (§A.47), from the authorization.** "This decides whether OI's gravitational and
vacuum-energy outputs (a₀, Tully–Fisher, ρ_s) are derived, or depend on an imported normalization or
on R1's selected law. That bears on OI's target of explaining how vacuum energy gravitates." It does
not decide whether any law or hypothesis is physically justified.

**Source pin.** `main` at `371acccc9f8531465afa7fcf4b5d1262235d26d1` (includes the Stage 0 record).
`GR:n`, `SM:n`, `Sub:n`, `Str:n`, `Meth:n` are line `n` of `papers/GR.md`, `SM.md`,
`Substratum.md`, `Structure.md`, `Methodology.md`; `chNN:n`, `appA:n`, `appB:n`, `appC:n`,
`gloss:n` are lines of the `book/` chapter, appendix and glossary files; `FULL:n` is
`book/The-Incompleteness-of-Observation-FULL.md`, all at the pin.

## 1. The three alternatives (definitions fixed before tracing)

Notation as GR §§2–5: first law dE = (c²κ/8πG) dA; κ = cH on exact de Sitter; T_KMS = ħκ/(2πck_B)
(T_dS for κ = cH); l_p² = Għ/c³; σ the entropy per counted boundary mode; ε² the horizon area per
mode. β_E is the inverse-energy slope of the shell law, s′_count = ∂(σA/ε²)/∂E the slope of the
count through the first law.

| Id | Alternative | Normalization supplied by |
|---|---|---|
| A1 | **State-counting entropy** S = σA/ε², the log-count of boundary modes (GR §3.1, §5) | ε²/σ, which the gap equation fixes through the shell law's slope β_E (GR:78–80) and measured ħ (GR §4). Two pairings of a temperature with it are distinguished: **A1a**, the Clausius temperature of the count, T_cl = (∂S_count/∂E)⁻¹ through the first law (GR:98–100); **A1b**, the shell law's statistical temperature 1/(k_Bβ_E) (GR:58). They coincide when β_E = s′_count (H-count with uniform shell weights) |
| A2 | **Clausius entropy at T_dS**: dS = dE/T_dS with the first law and the KMS temperature at measured ħ | the first-law prefactor 8π and the KMS period 2π; no reference to the count or the law |
| A3 | **Imported Bekenstein–Hawking normalization** S = A/(4Għ) (or c³A/(4Għ)) taken as an external physical input, e.g. inside the cited Verlinde derivation (arXiv:1611.02269v2) | the external theory from which it is taken |

A2 and A3 have the same value; they differ in status (a Clausius computation from stated inputs,
versus an imported formula). Law variation is represented exactly as in Stage 0 (AUDIT §3, C1 notes;
P7B node 5): a shell law with slope k·β_E, k > 0, holding the other premises fixed. This is a
scalar device already on `main`; no law is constructed.

## 2. Scope: results to trace

Owner-named results, and every further consumer of the horizon-entropy normalization found by §3's
search:

| Id | Result | Primary sites |
|---|---|---|
| R1 | a₀ = cH/6 | GR:470–482, :510, :546; Stage 0 C1.d |
| R2 | Baryonic Tully–Fisher normalization v⁴ = GM_B·cH/6 (and the crossover radius r_M) | GR:486–490, :547–548 |
| R3 | ρ_s = ρ_crit | GR:420–430; Stage 0 C1.e, F5 |
| R4 | ρ_s/ρ_crit = 2/(d−1) and its use as a d = 3 filter | GR:440–446; SM:30, :180–200, :1424; Sub:88, :157 |
| R5+ | Further consumers found by §3 (expected candidates, to be confirmed or dropped by the trace: ħ = c³ε²/(4Gσ); ε = 2√σ l_p; the 1/4; a₀(z) = cH(z)/6; the dark-sector fraction; the §6.3 compression ratio; GR App. A.6–A.7) | as found |

Book mirrors and appendix-a rows are traced as mirrors of these sites; a mirror stating the same
content adds no result, but a mirror stating a different alternative, provenance or class is a
consistency finding (§6).

## 3. Trace procedure

1. For each result, list every load-bearing step from horizon thermodynamics to the displayed value,
   with file:line.
2. At each step record: which alternative (A1a, A1b, A2, A3, or none) the text uses, quoted; where ħ,
   G, k_B, ε, σ, H and any supplied cosmological parameter enter; whether any of them is fixed by a
   measured value in that step (calibration), and whether that measured value is the result itself
   or algebraically equivalent to it.
3. Evaluate the displayed value under each of A1a, A1b, A2, A3 and under the law-variation device
   (k ≠ 1). Algebra written in this audit is marked [W]; it re-reads displayed formulas and does not
   construct a law or add a premise.
4. Search `papers/*.md` and `book/*.md` (FULL mirrored) for: `cH/6`, `a_0`, `Verlinde`,
   `rho_s`/`ρ_s`, `rho_{\text{crit}}`, `2/(d-1)`, `\frac{2}{d-1}`, `concordance`, `1/4`,
   `A/(4`, `4\sigma`, `T_{\text{dS}}`, `T_{\text{cl}}`, `\sigma A/\epsilon^2`, `S_{\text{dS}}`,
   `derive(s|d) $\hbar`, `is derived, not free`, `value of $\hbar`. Record hit counts and the hits
   assigned to each result or mirror in AUDIT's coverage section.
5. External literature consulted is marked [LIT] with whether it was re-read for this audit.

## 4. Classes (fixed before classification)

Applied to a result's displayed value (form and numerical normalization) under a given alternative.

- **U — unresolved.** The text does not determine which alternative a load-bearing step uses and
  the value differs between the candidate alternatives, or a load-bearing step has no stated
  derivation or source on `main`.
- **X — externally calibrated.** Not U, and some load-bearing normalization of the value (a
  dimensionless coefficient, a scale, or a parameter the value depends on) is supplied from
  outside OI's own premises. Subtypes, all that apply recorded:
  - **Xm** — fixed by fitting to a measured value (including a parameter solved for from a measured
    constant);
  - **Xi** — taken over from an external theory result that is not derived on `main` (an imported
    formula or coefficient);
  - **Xa** — fails the native-content test N below: every quantity surviving in the value is an
    external theory input (GR first law, Friedmann equation, KMS temperature, Gauss's law), so the
    value is an ambient identity of those inputs whatever OI contributes.
- **C — conditional.** Not U or X, and the derivation on `main` is complete given named hypotheses
  of status posited or open; every such hypothesis is listed with the result.
- **D — genuinely derived.** Not U, X or C: every premise is an OI posit or a justified result on
  `main`, no normalization is external, and test N is passed.

Precedence U > X > C > D. Whatever the class, every named condition used is listed.

**Test N (native content).** Replace every OI-specific ingredient (σ, ε, the count, the shell law,
T_cl) by the textbook inputs of A2 (first law, T_KMS, Clausius). If the displayed value is
unchanged and no OI-specific quantity survives in it, the result has no OI-native content (Xa).

**Test K (law dependence).** The value is law-dependent under an alternative if it changes under the
slope k·β_E (k ≠ 1) with the other premises held fixed; otherwise law-independent.

**Test Z (circularity).** A result is circular if a parameter it depends on is calibrated from a
measured value Q and the result is either Q itself or algebraically equivalent to the calibration
equation, and the result is presented somewhere in the corpus as a prediction, derivation or
recovery rather than as a consistency relation. Each flagged site is cited.

**§A.23 axis.** Each result is typed **correctness** (a framework output not fitted to the data,
confronted with an independent measurement), **consistency** (coherence with the premises, or a
match to a known value, a retrodiction), or **none** (no observational comparison). The type is
recorded, not a band movement: this audit is consistency work and moves no correctness band.
External comparisons are typed raw/direct or inferred under §A.24.

## 5. The corpus reading

For each step the reading the corpus actually uses (**A\***) is the alternative the text at that
site uses, by quotation. If two sites assign different alternatives to the same step, both are
recorded and the result is classified under each; if no site determines it, the step is U.

## 6. Decision rule (fixed before classification)

The verdict is generated from the table:

1. **Per result**: its class under A1a, A1b, A2, A3 and A\*, with its Test K, N, Z outcomes and its
   §A.23 axis.
2. **Dependence on R1's selected law**: a result depends on the selected law exactly when its value
   under A\* is law-dependent by Test K. The verdict lists those results; for the others it states
   that the value is law-independent under A\*, and separately whether that independence is because
   the count's normalization cancels, does not enter, or enters only through calibration.
3. **Which entropy supplies the normalization**: for each result, the alternative whose
   normalization survives in the value under A\* (or "none survives").
4. **Internal consistency**: the corpus is internally consistent about the entropy it uses if every
   site for a step agrees on A\* and no site states a provenance or class for a result stronger than
   the trace supports (claim/evidence: available → derived; ambient/background → native; imported →
   substrate-derived; identity → explanation). Every exception is a finding with file:line.
5. **Circularity**: every Test Z flag is listed with its sites.
6. In every case: no conditional result is promoted; mathematical sufficiency is not reported as
   physical justification; A1 remains open and unadopted; nothing authorizes a successor unit or a
   manuscript change. Corrections to manuscript text are recommendations for a separately authorized
   correction unit.

Verdict text is written after the table, from it.

## 7. Controls (fixed in advance)

| Id | Control | Expected outcome of a valid scheme | Failure meaning |
|---|---|---|---|
| K1 | Textbook Gibbons–Hawking / Jacobson Clausius route [LIT, standard]: first law dE = (c²κ/8πG)dA, T = ħκ/(2πck_B), dS = dE/T ⇒ S = c³A/(4Għ); and S·T/V_H on exact de Sitter | Classified **Xa** (no OI-native content), law-independent by Test K, never D | If it lands in D or C, the scheme cannot separate OI derivations from textbook inputs; the audit's X/D verdicts are void |
| K2 | Countercontrol: the spherical link-density factor κ_m = 3/2 and ε² = (2/3)ε_lat² (GR:104), an exact lattice-point count under the single-link reading H-link | Classified **C** (native content present, no external normalization, conditional on H-link) | If it lands in X, the X tests are too broad and every X verdict is void |
| K3 | Known calibration: ε = 2√σ l_p, which GR:308 states is "a self-consistency condition, not an independent determination" | Classified **Xm**; Test Z applied to its sites | If not Xm, the calibration test is broken |
| K4 | Non-vacuity of Test K: the count's own value σA/ε² after calibration (Stage 0 C1.c, witness P7B node 5) | Law-dependent under A1 (A/(4k l_p²)) | If Test K finds no dependence here, it is vacuous |
| K5 | Exactness: every [W] step is exact symbolic algebra on displayed formulas; no numerical value is used as evidence of an identity | All identities stated as exact algebra | A numerical "identity" voids that step |

## 8. Reused records (not re-derived)

| Short name | Path on `main` | Used for |
|---|---|---|
| S0 | `verification/audits/foundations/r1-l8-stage0-20261120/AUDIT.md`, `PREREG.md` | rows C1.a–e, findings F4, F5, the law-variation device, D1 |
| P7B | `verification/audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | node 5 (every slope occurs), H4, 6.4 |
| REMAINDER | `verification/audits/foundations/a1-remainder-20261119/REMAINDER.md` | rows C1, C2 |
| Verlinde | arXiv:1611.02269v2 [LIT] | eqs. 1.2, 1.4–1.7, 2.12–2.15, 4.25–4.30 |

Every reused record keeps the layer it states for itself (§A.46 item 7). Stage 0's [W] readings F4
and F5 are inputs to be re-checked here, not premises.

## 9. Limits

Paper-only. No law is constructed, no hypothesis adopted or dropped, no manuscript, Lean or registry
edit. The trace is bounded by §3's searches; AUDIT states what was and was not traced.

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7041456852 | Authorization, scope, deliverable, restrictions, stop rule, goal link | Provenance; quoted above with author and time |
| #1169, #873, #1456 | Accountability; Stage 0 PR (merged at `371acccc`) | Provenance |
| arXiv:1611.02269v2 | Content of the imported factor | External literature [LIT]; not a `main` record |
